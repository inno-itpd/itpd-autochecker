#!/usr/bin/env python3
"""Inspect saved feedback segments and optionally compare them to fresh updates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    apply_structured_segment_update,
    compute_report_impact,
    diff_segment_block,
    format_status_counts,
    fresh_segment_state_from_update,
    fresh_segment_state_to_dict,
    load_fresh_segment_updates,
    parse_feedback_report,
    parse_unresolved_section,
    segment_block_to_dict,
    segment_diff_to_dict,
    segment_selector_to_int,
)


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
    fresh_updates = load_fresh_segment_updates(fresh_payload) if fresh_payload else {}
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
    parser = argparse.ArgumentParser(description="Inspect saved feedback.md segment state.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to feedback.md")
    parser.add_argument("segments", nargs="+", help="Segment IDs such as S4 S8")
    parser.add_argument("--fresh-payload", help="Path to a structured fresh segment payload JSON")
    parser.add_argument("--format", choices=("text", "json"), default="json")
    args = parser.parse_args()

    output = build_output(
        args.assignment,
        Path(args.feedback_path),
        args.segments,
        Path(args.fresh_payload) if args.fresh_payload else None,
    )
    print(render_text(output, args.segments) if args.format == "text" else json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
