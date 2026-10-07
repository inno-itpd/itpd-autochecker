"""Build valid feedback reports for tests."""

from __future__ import annotations

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import render_report, render_segment_block, SegmentBlock

REPO = "https://github.com/itpd-team-3/meeting-notes"
SHA = "0123456789abcdef0123456789abcdef01234567"


def preamble(assignment: str, team: int = 3) -> str:
    index = ASSIGNMENT_CONFIG[assignment]["primary_index"]
    return "\n".join(
        [
            f"# Assignment {assignment[1:]} Feedback Report",
            "",
            f"- Team: {team}",
            f"- Repository reviewed: `{REPO}`",
            f"- Snapshot reviewed: `{SHA}`",
            f"- Primary index reviewed: [`{index}`]({REPO}/blob/{SHA}/{index})",
        ]
    )


def block(seg_num: int, name: str, status: str, evidence_gaps: bool = False) -> SegmentBlock:
    verified = [f"S{seg_num} shortfall."] if status in ("partial", "missing") else []
    unverified = [f"S{seg_num} blocked check."] if evidence_gaps else []
    evidence = [f"S{seg_num} evidence."]
    return SegmentBlock(
        seg_num=seg_num,
        name=name,
        markdown=render_segment_block(seg_num, name, status, evidence_gaps, evidence, verified, unverified),
        status=status,
        evidence_gaps=evidence_gaps,
        evidence=evidence,
        verified_shortfalls=verified,
        unverified_checks=unverified,
    )


def build_report(assignment: str, statuses: dict[int, str] | None = None, gaps: set[int] | None = None, team: int = 3) -> str:
    segment_defs = ASSIGNMENT_CONFIG[assignment]["segment_defs"]
    statuses = statuses or {}
    gaps = gaps or set()
    blocks = {
        seg_num: block(seg_num, segment_def["name"], statuses.get(seg_num, "met"), seg_num in gaps)
        for seg_num, segment_def in segment_defs.items()
    }
    return render_report(
        preamble=preamble(assignment, team),
        segment_defs=segment_defs,
        segment_blocks=blocks,
        unresolved_gaps={seg_num: [f"S{seg_num} gap detail."] for seg_num in gaps},
        summary_body="- First shortfall.\n- Second shortfall.\n- Third shortfall.",
        strengths_body="- A verified strength.",
        main_issues_body="- A fixable issue.",
    )
