#!/usr/bin/env python3
"""Inspect saved feedback segments and optionally compare them to fresh updates.

With `--fresh-payload`, the output also predicts the report-level changes the
same payload would make to the metadata preamble and to the Summary,
Strengths, and Main issues sections.  The script stays read-only: it never
writes the report or any saved state.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.patch_feedback_report import (
    SECTION_BODY_KEYS,
    resolve_report_metadata,
    resolve_sections,
)
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    SEGMENT_SELECTOR_PATTERN,
    ReportMetadata,
    apply_structured_segment_update,
    compute_report_impact,
    diff_segment_block,
    format_status_counts,
    fresh_segment_state_from_update,
    fresh_segment_state_to_dict,
    fresh_segment_updates_from_payload,
    load_patch_payload,
    parse_feedback_report,
    parse_preamble,
    parse_unresolved_section,
    segment_block_to_dict,
    segment_diff_to_dict,
    segment_selector_to_int,
)

SECTION_LABELS = {
    "summary": "summary",
    "strengths": "strengths",
    "main_issues_to_fix": "main issues",
}


def _payload_has_segments(payload: dict[str, object]) -> bool:
    return "segment_updates" in payload or any(
        isinstance(key, str) and SEGMENT_SELECTOR_PATTERN.fullmatch(key.strip()) for key in payload
    )


def _metadata_to_dict(metadata: ReportMetadata) -> dict[str, object]:
    return {
        "team": metadata.team,
        "repository": metadata.repository,
        "snapshot": metadata.snapshot,
        "primary_index": metadata.primary_index,
        "notes": metadata.notes,
    }


def _metadata_changes(saved: ReportMetadata, predicted: ReportMetadata) -> list[str]:
    changes: list[str] = []
    for field in ("snapshot", "repository", "primary_index"):
        old = getattr(saved, field)
        new = getattr(predicted, field)
        if old != new:
            changes.append(f"{field} {old if old is not None else 'none'} -> {new if new is not None else 'none'}")
    if saved.notes != predicted.notes:
        if predicted.notes is None:
            changes.append("notes removed")
        elif saved.notes is None:
            changes.append(f"notes added: {predicted.notes}")
        else:
            changes.append("notes updated")
    return changes


def _sections_to_dict(bodies: dict[str, str]) -> dict[str, str]:
    return {key: bodies[key].strip() for key in SECTION_BODY_KEYS}


def _section_changes(saved: dict[str, str], predicted: dict[str, str]) -> list[str]:
    return [
        f"{SECTION_LABELS[key]} updated"
        for key in SECTION_BODY_KEYS
        if saved[key].strip() != predicted[key].strip()
    ]


def _diff_labels(diff: dict[str, object]) -> list[str]:
    labels: list[str] = []
    if diff["status_changed"]:
        labels.append("status changed")
    if diff["evidence_gaps_changed"]:
        labels.append("evidence gap changed")
    if diff["evidence_added"] or diff["evidence_removed"]:
        labels.append("evidence changed")
    if diff["verified_shortfalls_added"] or diff["verified_shortfalls_removed"]:
        labels.append("verified shortfalls changed")
    if diff["unverified_checks_added"] or diff["unverified_checks_removed"]:
        labels.append("unverified checks changed")
    return labels


def _interpret_diff(saved: dict[str, object], fresh: dict[str, object], diff: dict[str, object]) -> list[str]:
    interpretations: list[str] = []
    if diff["status_changed"]:
        interpretations.append(f"status {saved['status']} -> {fresh['status']}")
    if saved["evidence_gaps"] and not fresh["evidence_gaps"]:
        interpretations.append("evidence gap cleared")
    if not diff["status_changed"] and (diff["evidence_added"] or diff["evidence_removed"]):
        interpretations.append("status unchanged, but evidence changed")
    return interpretations


def build_output(assignment: str, feedback_path: Path, selectors: list[str], fresh_payload: Path | None) -> dict[str, object]:
    segment_defs = ASSIGNMENT_CONFIG[assignment]["segment_defs"]
    report = parse_feedback_report(feedback_path, segment_defs)
    unresolved = parse_unresolved_section(report.unresolved_body, segment_defs)
    payload = load_patch_payload(fresh_payload) if fresh_payload else None
    fresh_updates = (
        fresh_segment_updates_from_payload(payload)
        if payload is not None and _payload_has_segments(payload)
        else {}
    )
    predicted_blocks = dict(report.segment_blocks)

    segments: dict[str, object] = {}
    for selector in selectors:
        seg_num = segment_selector_to_int(selector)
        block = report.segment_blocks[seg_num]
        segment_output: dict[str, object] = {"saved_state": segment_block_to_dict(block, unresolved.get(seg_num, []))}
        if selector in fresh_updates:
            name = segment_defs[seg_num]["name"]
            fresh_state = fresh_segment_state_from_update(seg_num, name, fresh_updates[selector])
            segment_output["fresh_state"] = fresh_segment_state_to_dict(fresh_state)
            segment_output["diff"] = segment_diff_to_dict(diff_segment_block(block, fresh_state))
            predicted_blocks[seg_num] = apply_structured_segment_update(block, fresh_updates[selector], name)
        segments[selector] = segment_output

    output: dict[str, object] = {
        "feedback_path": str(feedback_path),
        "saved_manual_review_required": report.segments_table.manual_review_required,
        "segments": segments,
    }
    if payload is not None and "report" in payload:
        saved_metadata = parse_preamble(report.preamble)
        predicted_metadata = resolve_report_metadata(assignment, saved_metadata, payload)
        output["predicted_report_metadata"] = {
            "saved": _metadata_to_dict(saved_metadata),
            "predicted": _metadata_to_dict(predicted_metadata),
            "changes": _metadata_changes(saved_metadata, predicted_metadata),
        }
    if payload is not None and ("sections" in payload or any(key in payload for key in SECTION_BODY_KEYS)):
        saved_sections = {
            "summary": report.summary_body,
            "strengths": report.strengths_body,
            "main_issues_to_fix": report.main_issues_body,
        }
        predicted_sections = resolve_sections(payload, saved_sections)
        output["predicted_report_sections"] = {
            "saved": _sections_to_dict(saved_sections),
            "predicted": _sections_to_dict(predicted_sections),
            "changes": _section_changes(saved_sections, predicted_sections),
        }
    if fresh_payload:
        impact = compute_report_impact(report, segment_defs, predicted_blocks)
        output["predicted_report_impact"] = {
            "saved_counts": impact.saved_counts,
            "predicted_counts": impact.predicted_counts,
            "saved_manual_review_required": impact.saved_manual_review_required,
            "predicted_manual_review_required": impact.predicted_manual_review_required,
        }
    return output


def render_text(output: dict[str, object], selectors: list[str]) -> str:
    lines = [
        f"Feedback: {output['feedback_path']}",
        f"Saved report: manual_review={output['saved_manual_review_required']}",
    ]
    for selector in selectors:
        segment = output["segments"][selector]
        saved = segment["saved_state"]
        lines.extend(
            [
                "",
                f"{selector} {saved['name']}",
                f"- Saved: status={saved['status']}, evidence_gaps={'yes' if saved['evidence_gaps'] else 'no'}",
            ]
        )
        if "fresh_state" in segment:
            fresh, diff = segment["fresh_state"], segment["diff"]
            lines.append(f"- Fresh: status={fresh['status']}, evidence_gaps={'yes' if fresh['evidence_gaps'] else 'no'}")
            labels = _diff_labels(diff)
            lines.append(f"- Diff: {', '.join(labels) if labels else 'no changes'}")
            interpretations = _interpret_diff(saved, fresh, diff)
            if interpretations:
                lines.append(f"- Interpretation: {'; '.join(interpretations)}")
            if fresh.get("source"):
                lines.append(f"- Source: {fresh['source']}")
            if fresh.get("checked_at"):
                lines.append(f"- Checked at: {fresh['checked_at']}")
            lines.extend(f"- Note: {note}" for note in fresh.get("notes", []))

    metadata = output.get("predicted_report_metadata")
    if isinstance(metadata, dict) and metadata.get("changes"):
        lines.extend(["", "Predicted metadata changes:", *[f"- {change}" for change in metadata["changes"]]])

    sections = output.get("predicted_report_sections")
    if isinstance(sections, dict) and sections.get("changes"):
        lines.extend(["", "Predicted section changes:", *[f"- {change}" for change in sections["changes"]]])

    impact = output.get("predicted_report_impact")
    if isinstance(impact, dict):
        lines.extend(
            [
                "",
                "Predicted report impact: "
                f"statuses [{format_status_counts(impact['saved_counts'])}] -> [{format_status_counts(impact['predicted_counts'])}], "
                f"manual_review {impact['saved_manual_review_required']} -> {impact['predicted_manual_review_required']}",
            ]
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect saved agent-feedback.md segment state.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to agent-feedback.md")
    parser.add_argument("segments", nargs="+", help="Segment IDs such as S4 S8")
    parser.add_argument("--fresh-payload", help="Path to a structured fresh segment payload JSON")
    parser.add_argument("--format", choices=("text", "json"), default="json")
    args = parser.parse_args()

    try:
        output = build_output(
            args.assignment,
            Path(args.feedback_path),
            args.segments,
            Path(args.fresh_payload) if args.fresh_payload else None,
        )
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(2)
    print(render_text(output, args.segments) if args.format == "text" else json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
