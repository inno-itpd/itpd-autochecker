"""Extract feedback reports into the instructor triage table and the release CSV."""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, default_paths
from tools.grader_tools.feedback_report import format_status_counts, parse_feedback_report, status_counts
from tools.grader_tools.validate import validate_report

# Moodle exports one directory per team, e.g. `Team 3_12345_assignsubmission_file`.
TEAM_NAME_PATTERN = re.compile(r"(Team\s+\d+)")


@dataclass(frozen=True)
class ExtractedEntry:
    group: str
    team_dir: str
    feedback_path: str = ""
    segment_statuses: dict[int, str] = field(default_factory=dict)
    manual_review_required: str = "no"
    feedback: str = ""
    parsed_ok: bool = True
    issue: str = ""


def parse_team_name(dirname: str) -> str:
    match = TEAM_NAME_PATTERN.match(dirname)
    return match.group(1) if match else dirname


def team_sort_key(group: str) -> tuple[int, int | str]:
    match = re.search(r"Team\s+(\d+)", group)
    if match:
        return (0, int(match.group(1)))
    return (1, group)


def _blank_entry(team_dir: Path, issue: str) -> ExtractedEntry:
    return ExtractedEntry(
        group=parse_team_name(team_dir.name),
        team_dir=team_dir.name,
        manual_review_required="yes",
        parsed_ok=False,
        issue=issue,
    )


def parse_feedback_file(assignment: str, path: Path) -> ExtractedEntry:
    report = parse_feedback_report(path, ASSIGNMENT_CONFIG[assignment]["segment_defs"])
    errors = validate_report(assignment, report)
    if errors:
        raise ValueError("\n".join(errors))
    return ExtractedEntry(
        group=parse_team_name(path.parent.name),
        team_dir=path.parent.name,
        feedback_path=path.as_posix(),
        segment_statuses=dict(report.segments_table.statuses),
        manual_review_required=report.segments_table.manual_review_required or "no",
        feedback=report.summary_body,
    )


def scan_feedback_dir(assignment: str, input_dir: Path) -> tuple[list[ExtractedEntry], list[str]]:
    entries: list[ExtractedEntry] = []
    warnings: list[str] = []

    for team_dir in sorted(input_dir.iterdir()):
        if not team_dir.is_dir():
            continue
        feedback_path = team_dir / "feedback.md"
        if not feedback_path.exists():
            warnings.append(f"{team_dir.name}: missing feedback.md")
            entries.append(_blank_entry(team_dir, "missing feedback"))
            continue
        try:
            entries.append(parse_feedback_file(assignment, feedback_path))
        except ValueError as exc:
            warnings.append(f"{team_dir.name}: malformed feedback.md: " + str(exc).replace("\n", " ; "))
            entries.append(_blank_entry(team_dir, "malformed feedback"))

    entries.sort(key=lambda entry: team_sort_key(entry.group))
    return entries, warnings


def _relative_markdown_target(output_path: Path, target_path: Path, anchor: str = "") -> str:
    relative = os.path.relpath(target_path, start=output_path.parent).replace(os.sep, "/")
    return quote(relative + anchor, safe="/#._-")


def _table_cell_text(text: str, separator: str = " ") -> str:
    flattened = separator.join(line.strip() for line in text.splitlines() if line.strip())
    return flattened.replace("|", "\\|")


def write_dev_md(entries: list[ExtractedEntry], output_path: Path, assignment: str) -> None:
    lines = [
        f"# {assignment} Feedback Triage",
        "",
        "| team | gaps | gaps section | statuses | feedback |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        if entry.parsed_ok:
            feedback_target = Path(entry.feedback_path)
            team_cell = f"[{entry.group}]({_relative_markdown_target(output_path, feedback_target)})"
            gaps_target = _relative_markdown_target(output_path, feedback_target, "#unresolved-evidence-gaps")
            gaps_section_cell = f"[Unresolved evidence gaps]({gaps_target})"
            counts = status_counts([entry.segment_statuses[n] for n in sorted(entry.segment_statuses)])
            statuses_cell = format_status_counts(counts)
            feedback_cell = _table_cell_text(entry.feedback, separator=" <br> ")
            gaps_cell = entry.manual_review_required
        else:
            team_cell = entry.group
            gaps_cell = "yes"
            gaps_section_cell = f"feedback file is {'missing' if entry.issue == 'missing feedback' else 'malformed'}"
            statuses_cell = ""
            feedback_cell = ""
        lines.append(f"| {team_cell} | {gaps_cell} | {gaps_section_cell} | {statuses_cell} | {feedback_cell} |")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} rows to {output_path}")


def write_release_csv(entries: list[ExtractedEntry], output_path: Path, segment_numbers: list[int]) -> None:
    segment_columns = [f"s{n}" for n in segment_numbers]
    fieldnames = ["group", *segment_columns, "manual_review", "feedback"]
    with open(output_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="|")
        writer.writeheader()
        for entry in entries:
            row = {name: "" for name in fieldnames}
            row["group"] = entry.group
            if entry.parsed_ok:
                for seg_num, column in zip(segment_numbers, segment_columns, strict=True):
                    row[column] = entry.segment_statuses.get(seg_num, "")
                row["manual_review"] = entry.manual_review_required
                row["feedback"] = entry.feedback.replace("\n", "\\n")
            writer.writerow(row)
    print(f"Wrote {len(entries)} rows to {output_path}")


def run_extraction(assignment: str, input_dir: Path, dev_output: Path, release_output: Path) -> int:
    if assignment not in ASSIGNMENT_CONFIG:
        print(f"Error: unknown assignment {assignment}", file=sys.stderr)
        return 1
    if not input_dir.is_dir():
        print(f"Error: {input_dir} is not a directory", file=sys.stderr)
        return 1

    entries, warnings = scan_feedback_dir(assignment, input_dir)
    if not entries:
        print("No team feedback directories found.", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)

    write_dev_md(entries, dev_output, assignment)
    write_release_csv(entries, release_output, sorted(ASSIGNMENT_CONFIG[assignment]["segment_defs"]))
    return 0


def build_parser(assignment: str) -> argparse.ArgumentParser:
    defaults = default_paths(assignment)
    parser = argparse.ArgumentParser(description=f"Extract {assignment} feedback reports into dev.md and the release CSV.")
    parser.add_argument("--input", default=defaults["feedback_dir"], help=f"Team feedback directories (default: {defaults['feedback_dir']})")
    parser.add_argument("--dev-output", default=defaults["dev_output"], help=f"Triage table path (default: {defaults['dev_output']})")
    parser.add_argument("--release-output", default=defaults["release_output"], help=f"Release CSV path (default: {defaults['release_output']})")
    return parser
