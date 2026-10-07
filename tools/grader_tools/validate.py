"""Validation of feedback reports against `docs/grading-feedback-format.md`."""

from __future__ import annotations

import re
from pathlib import Path

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    HEADING_UNVERIFIED,
    HEADING_VERIFIED,
    NO_REVIEW_TEXT,
    SHORTFALL_STATUSES,
    ParsedFeedbackReport,
    SegmentDefs,
    has_subheading,
    parse_feedback_report,
    parse_unresolved_section,
    render_overall_assessment,
    render_segments_table,
)

METADATA_PREFIXES = [
    "- Team:",
    "- Repository reviewed:",
    "- Snapshot reviewed:",
    "- Primary index reviewed:",
]
NOTES_PREFIX = "- Notes about the snapshot:"
TEAM_LINE = re.compile(r"^- Team: \d+$")
REPOSITORY_LINE = re.compile(r"^- Repository reviewed: (`https://github\.com/[^/`\s]+/[^/`\s]+`|none)$")
SNAPSHOT_LINE = re.compile(r"^- Snapshot reviewed: (`[0-9a-f]{40}`|none)$")


def _validate_preamble(assignment: str, preamble: str, primary_index: str) -> list[str]:
    errors: list[str] = []
    lines = [line.strip() for line in preamble.splitlines() if line.strip()]
    if len(lines) < 5:
        return ["Preamble must include the title and four repository metadata bullets"]

    expected_title = f"# Assignment {assignment[1:]} Feedback Report"
    if lines[0] != expected_title:
        errors.append(f"Title must be `{expected_title}`")

    metadata = lines[1:5]
    for expected_prefix, line in zip(METADATA_PREFIXES, metadata, strict=True):
        if not line.startswith(expected_prefix):
            errors.append(f"Metadata line must start with `{expected_prefix}`")
    if errors:
        return errors

    if not TEAM_LINE.fullmatch(metadata[0]):
        errors.append("`- Team:` must be a plain team number")
    if not REPOSITORY_LINE.fullmatch(metadata[1]):
        errors.append("`- Repository reviewed:` must be a backticked `https://github.com/<org>/<repo>` URL or `none`")
    if not SNAPSHOT_LINE.fullmatch(metadata[2]):
        errors.append("`- Snapshot reviewed:` must be a backticked full 40-character SHA or `none`")

    primary_content = metadata[3][len("- Primary index reviewed:") :].strip()
    canonical_primary = re.compile(rf"^\[`{re.escape(primary_index)}`\]\(https://github\.com/[^)]+/blob/[0-9a-f]{{40}}/{re.escape(primary_index)}\)$")
    if primary_content != "none" and not canonical_primary.fullmatch(primary_content):
        errors.append(
            f"`Primary index reviewed` must be `` [`{primary_index}`](https://github.com/<org>/<repo>/blob/<sha>/{primary_index}) `` or `none`"
        )

    extra = lines[5:]
    if primary_content == "none":
        if len(extra) != 1 or not extra[0].startswith(NOTES_PREFIX):
            errors.append(f"`{NOTES_PREFIX}` must follow the metadata when the primary index is `none`")
    elif extra:
        if extra[0].startswith(NOTES_PREFIX):
            errors.append(f"`{NOTES_PREFIX}` is only allowed when `Primary index reviewed` is `none`")
        else:
            errors.append("Do not add extra preamble content before `## Overall assessment`")
    return errors


def _validate_segments(report: ParsedFeedbackReport, segment_defs: SegmentDefs) -> list[str]:
    errors: list[str] = []
    table = report.segments_table
    blocks = report.segment_blocks

    for seg_num, segment_def in sorted(segment_defs.items()):
        if seg_num not in table.statuses:
            errors.append(f"Missing S{seg_num} in the segments table")
            continue
        if seg_num not in blocks:
            errors.append(f"Missing segment details block for S{seg_num}")
            continue

        expected_name = segment_def["name"]
        if table.seen_names.get(seg_num) != expected_name:
            errors.append(f"S{seg_num} name is `{table.seen_names.get(seg_num, '')}`, expected `{expected_name}`")

        block = blocks[seg_num]
        if block.status != table.statuses[seg_num]:
            errors.append(f"S{seg_num} details status `{block.status}` does not match table status `{table.statuses[seg_num]}`")
        if block.evidence_gaps != table.evidence_gaps[seg_num]:
            errors.append(f"S{seg_num} details evidence-gaps line does not match the table")
        if block.status == "unverified" and not block.evidence_gaps:
            errors.append(f"S{seg_num} is `unverified`, so it must have `Evidence gaps: yes`")

        if not block.evidence:
            errors.append(f"S{seg_num} needs at least one `**Evidence:**` bullet")

        has_verified = has_subheading(block.markdown, HEADING_VERIFIED)
        if block.status in SHORTFALL_STATUSES and not block.verified_shortfalls:
            errors.append(f"S{seg_num} is `{block.status}`, so it needs `**{HEADING_VERIFIED}:**` bullets")
        if block.status == "met" and has_verified:
            errors.append(f"S{seg_num} is `met`, so it must not contain `**{HEADING_VERIFIED}:**`")

        has_unverified = has_subheading(block.markdown, HEADING_UNVERIFIED)
        if block.evidence_gaps and not block.unverified_checks:
            errors.append(f"S{seg_num} has evidence gaps, so it needs `**{HEADING_UNVERIFIED}:**` bullets")
        if not block.evidence_gaps and has_unverified:
            errors.append(f"S{seg_num} has `Evidence gaps: no`, so it must not contain `**{HEADING_UNVERIFIED}:**`")

    expected_review = "yes" if any(table.evidence_gaps.values()) else "no"
    if table.manual_review_required is None:
        errors.append("Missing `Manual review required` row")
    elif table.manual_review_required != expected_review:
        errors.append("`Manual review required` does not match the segment `Evidence gaps` flags")

    if not errors:
        if report.segments_body.strip() != render_segments_table(segment_defs, blocks).strip():
            errors.append("`## Segments` must use the canonical table formatting")
        statuses = [blocks[seg_num].status for seg_num in sorted(segment_defs)]
        canonical_assessment = render_overall_assessment(statuses, expected_review == "yes")
        if report.assessment_body.strip() != canonical_assessment.strip():
            errors.append("`## Overall assessment` must use the canonical formatting and match the segment statuses")
    return errors


def _validate_unresolved(report: ParsedFeedbackReport, segment_defs: SegmentDefs) -> list[str]:
    gap_segments = {seg_num for seg_num, has_gap in report.segments_table.evidence_gaps.items() if has_gap}
    body = report.unresolved_body.strip()
    if not gap_segments:
        if body != NO_REVIEW_TEXT:
            return [f"`## Unresolved evidence gaps` must be exactly `{NO_REVIEW_TEXT}` when no gaps remain"]
        return []
    if body == NO_REVIEW_TEXT:
        return ["`## Unresolved evidence gaps` cannot use the no-review sentence while a segment has `Evidence gaps: yes`"]

    try:
        unresolved = parse_unresolved_section(body, segment_defs)
    except ValueError as exc:
        return [str(exc)]
    if set(unresolved) != gap_segments:
        expected = ", ".join(f"S{n}" for n in sorted(gap_segments))
        actual = ", ".join(f"S{n}" for n in sorted(unresolved)) or "none"
        return [f"Unresolved evidence gaps bullets do not match the segment gap flags (expected {expected}; got {actual})"]
    empty = [f"S{n}" for n, bullets in sorted(unresolved.items()) if not bullets]
    if empty:
        return [f"Unresolved evidence gaps need nested bullets for: {', '.join(empty)}"]
    return []


def _validate_summary(summary_body: str) -> list[str]:
    bullets = [line for line in summary_body.splitlines() if line.strip().startswith("- ")]
    if not 3 <= len(bullets) <= 5:
        return ["`## Summary` must contain 3-5 bullets"]
    return []


def validate_report(assignment: str, report: ParsedFeedbackReport) -> list[str]:
    config = ASSIGNMENT_CONFIG[assignment]
    segment_defs = config["segment_defs"]
    errors = _validate_preamble(assignment, report.preamble, config["primary_index"])
    errors.extend(_validate_segments(report, segment_defs))
    errors.extend(_validate_unresolved(report, segment_defs))
    errors.extend(_validate_summary(report.summary_body))
    return errors


def validate_feedback_file(assignment: str, path: Path) -> list[str]:
    try:
        report = parse_feedback_report(path, ASSIGNMENT_CONFIG[assignment]["segment_defs"])
    except ValueError as exc:
        return [str(exc)]
    return validate_report(assignment, report)
