from __future__ import annotations

import pytest

from tests.report_builder import build_report
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import (
    NO_REVIEW_TEXT,
    apply_structured_segment_update,
    format_status_counts,
    parse_feedback_text,
    parse_unresolved_section,
    render_report,
    segment_anchor,
    segment_selector_to_int,
    status_counts,
)

A1_DEFS = ASSIGNMENT_CONFIG["A1"]["segment_defs"]


def test_segment_anchor_matches_github_slug() -> None:
    assert segment_anchor(1, "Issue forms, labels, and task workflow") == "#s1-issue-forms-labels-and-task-workflow"


def test_parse_reads_statuses_and_gaps() -> None:
    report = parse_feedback_text(build_report("A1", statuses={2: "partial", 5: "unverified"}, gaps={5}), A1_DEFS)
    assert report.segments_table.statuses[2] == "partial"
    assert report.segments_table.statuses[5] == "unverified"
    assert report.segments_table.evidence_gaps[5] is True
    assert report.segments_table.manual_review_required == "yes"
    assert report.segment_blocks[2].verified_shortfalls == ["S2 shortfall."]
    assert report.segment_blocks[5].unverified_checks == ["S5 blocked check."]


def test_render_round_trip_is_stable() -> None:
    text = build_report("A2", statuses={1: "missing"}, gaps={3})
    defs = ASSIGNMENT_CONFIG["A2"]["segment_defs"]
    report = parse_feedback_text(text, defs)
    rerendered = render_report(
        report.preamble,
        defs,
        report.segment_blocks,
        parse_unresolved_section(report.unresolved_body, defs),
        report.summary_body,
        report.strengths_body,
        report.main_issues_body,
    )
    assert rerendered == text


def test_no_gaps_uses_no_review_sentence() -> None:
    report = parse_feedback_text(build_report("A1"), A1_DEFS)
    assert report.unresolved_body == NO_REVIEW_TEXT
    assert "`complete`" in report.assessment_body


def test_structured_update_rerenders_block() -> None:
    report = parse_feedback_text(build_report("A1", statuses={4: "partial"}), A1_DEFS)
    updated = apply_structured_segment_update(
        report.segment_blocks[4],
        {"status": "met", "verified_shortfalls": [], "evidence": ["Instructor-reviewed: board is public."]},
        A1_DEFS[4]["name"],
    )
    assert updated.status == "met"
    assert "Why not met (verified)" not in updated.markdown
    assert updated.evidence == ["Instructor-reviewed: board is public."]


def test_structured_update_rejects_unknown_status() -> None:
    report = parse_feedback_text(build_report("A1"), A1_DEFS)
    with pytest.raises(ValueError, match="status"):
        apply_structured_segment_update(report.segment_blocks[1], {"status": "great"}, A1_DEFS[1]["name"])


def test_status_counts_formatting() -> None:
    counts = status_counts(["met", "met", "partial", "unverified"])
    assert format_status_counts(counts) == "met 2 · partial 1 · unverified 1"


def test_selector_parsing() -> None:
    assert segment_selector_to_int("s10") == 10
    with pytest.raises(ValueError):
        segment_selector_to_int("segment 1")
