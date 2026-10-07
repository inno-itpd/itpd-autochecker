from __future__ import annotations

from tests.report_builder import REPO, SHA, build_report
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import parse_feedback_text
from tools.grader_tools.validate import validate_report


def errors_for(text: str, assignment: str = "A1") -> list[str]:
    return validate_report(assignment, parse_feedback_text(text, ASSIGNMENT_CONFIG[assignment]["segment_defs"]))


def test_valid_reports_pass() -> None:
    assert errors_for(build_report("A1")) == []
    assert errors_for(build_report("A1", statuses={1: "partial", 2: "missing", 3: "unverified"}, gaps={2, 3})) == []
    assert errors_for(build_report("A2", statuses={10: "partial"}), "A2") == []


def test_wrong_title() -> None:
    text = build_report("A1").replace("Feedback Report", "Grading Report", 1)
    assert any("Title must be" in error for error in errors_for(text))


def test_short_sha_rejected() -> None:
    text = build_report("A1").replace(f"`{SHA}`", "`0123456`")
    assert any("Snapshot reviewed" in error for error in errors_for(text))


def test_primary_index_must_point_at_snapshot() -> None:
    text = build_report("A1").replace(f"{REPO}/blob/{SHA}/", f"{REPO}/blob/main/")
    assert any("Primary index reviewed" in error for error in errors_for(text))


def test_primary_index_none_requires_notes() -> None:
    lines = build_report("A1").splitlines()
    lines = [("- Primary index reviewed: none" if line.startswith("- Primary index reviewed:") else line) for line in lines]
    text = "\n".join(lines)
    assert any("Notes about the snapshot" in error for error in errors_for(text))
    with_notes = text.replace(
        "- Primary index reviewed: none",
        "- Primary index reviewed: none\n- Notes about the snapshot: The PDF had no permalink.",
    )
    assert errors_for(with_notes) == []


def test_unverified_requires_gap() -> None:
    text = build_report("A1", statuses={3: "unverified"})
    assert any("must have `Evidence gaps: yes`" in error for error in errors_for(text))


def test_table_and_details_status_must_agree() -> None:
    text = build_report("A1", statuses={2: "partial"}).replace("| partial | no |", "| met | no |")
    assert any("does not match table status" in error for error in errors_for(text))


def test_met_must_not_list_shortfalls() -> None:
    text = build_report("A1").replace(
        "- S1 evidence.",
        "- S1 evidence.\n\n**Why not met (verified):**\n\n- Stray shortfall.",
    )
    assert any("is `met`" in error for error in errors_for(text))


def test_overall_assessment_counts_must_match() -> None:
    text = build_report("A1", statuses={1: "partial"}).replace("- Met: `8/9`", "- Met: `9/9`")
    assert any("Overall assessment" in error for error in errors_for(text))


def test_gap_segments_need_unresolved_bullets() -> None:
    text = build_report("A1", gaps={4}).replace("  - S4 gap detail.\n", "")
    assert any("nested bullets" in error for error in errors_for(text))


def test_summary_bullet_count() -> None:
    text = build_report("A1").replace("- Third shortfall.\n", "")
    assert any("3-5 bullets" in error for error in errors_for(text))
