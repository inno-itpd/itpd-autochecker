#!/usr/bin/env python3
"""Patch selected segment blocks in a feedback report and recompute the rollups."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    ParsedFeedbackReport,
    apply_structured_segment_update,
    load_patch_payload,
    parse_feedback_report,
    parse_segment_blocks,
    parse_unresolved_section,
    render_report,
    segment_selector_to_int,
)


def _as_body(value: object, section_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Patch payload `{section_name}` must be a non-empty string")
    return value.strip()


def patch_report(assignment: str, report: ParsedFeedbackReport, payload: dict[str, object]) -> str:
    segment_defs = ASSIGNMENT_CONFIG[assignment]["segment_defs"]
    segment_blocks = dict(report.segment_blocks)
    replacements = payload.get("segments")
    structured = payload.get("segment_updates")
    if not isinstance(replacements, dict) and not isinstance(structured, dict):
        raise ValueError("Patch payload must include a `segments` object or a `segment_updates` object")

    if isinstance(replacements, dict):
        for selector, markdown in replacements.items():
            seg_num = segment_selector_to_int(selector)
            if not isinstance(markdown, str) or not markdown.strip():
                raise ValueError(f"Replacement for {selector} must be a non-empty string")
            parsed = parse_segment_blocks(markdown.strip(), segment_defs)
            if list(parsed) != [seg_num]:
                raise ValueError(f"Replacement for {selector} must contain exactly one matching segment block")
            segment_blocks[seg_num] = parsed[seg_num]

    if isinstance(structured, dict):
        for selector, update in structured.items():
            seg_num = segment_selector_to_int(selector)
            segment_blocks[seg_num] = apply_structured_segment_update(
                segment_blocks[seg_num], update, segment_defs[seg_num]["name"]
            )

    unresolved = parse_unresolved_section(report.unresolved_body, segment_defs)
    payload_unresolved = payload.get("unresolved_evidence_gaps")
    if payload_unresolved is not None:
        if not isinstance(payload_unresolved, dict):
            raise ValueError("Patch payload `unresolved_evidence_gaps` must be an object")
        unresolved = {}
        for selector, bullets in payload_unresolved.items():
            if not isinstance(bullets, list) or not bullets or not all(isinstance(item, str) and item.strip() for item in bullets):
                raise ValueError(f"Unresolved bullets for {selector} must be a non-empty string list")
            unresolved[segment_selector_to_int(selector)] = [item.strip() for item in bullets]

    return render_report(
        preamble=report.preamble,
        segment_defs=segment_defs,
        segment_blocks=segment_blocks,
        unresolved_gaps=unresolved,
        summary_body=_as_body(payload.get("summary", report.summary_body), "summary"),
        strengths_body=_as_body(payload.get("strengths", report.strengths_body), "strengths"),
        main_issues_body=_as_body(payload.get("main_issues_to_fix", report.main_issues_body), "main_issues_to_fix"),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch selected segments in feedback.md.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to feedback.md")
    parser.add_argument("patch_payload", help="Path to JSON patch payload")
    args = parser.parse_args()

    feedback_path = Path(args.feedback_path)
    report = parse_feedback_report(feedback_path, ASSIGNMENT_CONFIG[args.assignment]["segment_defs"])
    rendered = patch_report(args.assignment, report, load_patch_payload(Path(args.patch_payload)))
    feedback_path.write_text(rendered, encoding="utf-8")
    print(f"Patched {feedback_path}")


if __name__ == "__main__":
    main()
