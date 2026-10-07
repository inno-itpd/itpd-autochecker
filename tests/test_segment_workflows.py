from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from scripts.patch_feedback_report import patch_report
from scripts.regrade_feedback_segments import build_subset_payload
from tests.conftest import ROOT
from tests.report_builder import build_report
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import apply_structured_segment_update, parse_feedback_text, parse_unresolved_section
from tools.grader_tools.validate import validate_report

A1_DEFS = ASSIGNMENT_CONFIG["A1"]["segment_defs"]
CLEAR_S4 = {
    "status": "met",
    "evidence_gaps": False,
    "evidence": ["Instructor-reviewed: the comparison board is public."],
    "verified_shortfalls": [],
    "unverified_checks": [],
}


def test_patch_clears_gap_and_recomputes_rollups() -> None:
    report = parse_feedback_text(build_report("A1", statuses={4: "unverified"}, gaps={4}), A1_DEFS)
    rendered = patch_report("A1", report, {"segment_updates": {"S4": CLEAR_S4}, "unresolved_evidence_gaps": {}})
    patched = parse_feedback_text(rendered, A1_DEFS)
    assert validate_report("A1", patched) == []
    assert patched.segments_table.manual_review_required == "no"
    assert "- Met: `9/9`" in patched.assessment_body


def test_subset_payload_keeps_untouched_gap_bullets() -> None:
    report = parse_feedback_text(build_report("A1", statuses={4: "unverified"}, gaps={4, 7}), A1_DEFS)
    predicted = dict(report.segment_blocks)
    predicted[4] = apply_structured_segment_update(predicted[4], CLEAR_S4, A1_DEFS[4]["name"])
    saved_unresolved = parse_unresolved_section(report.unresolved_body, A1_DEFS)
    subset = build_subset_payload({}, {"S4": CLEAR_S4}, ["S4"], predicted, saved_unresolved)
    assert subset["unresolved_evidence_gaps"] == {"S7": ["S7 gap detail."]}


def test_subset_payload_requires_bullets_for_new_gaps() -> None:
    report = parse_feedback_text(build_report("A1"), A1_DEFS)
    new_gap = {**CLEAR_S4, "status": "partial", "evidence_gaps": True, "verified_shortfalls": ["x"], "unverified_checks": ["y"]}
    predicted = dict(report.segment_blocks)
    predicted[4] = apply_structured_segment_update(predicted[4], new_gap, A1_DEFS[4]["name"])
    with pytest.raises(ValueError, match="S4 still has evidence gaps"):
        build_subset_payload({}, {"S4": new_gap}, ["S4"], predicted, {})


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)


def test_regrade_cli_end_to_end(tmp_path: Path) -> None:
    team_dir = tmp_path / "A1" / "feedback" / "markdown" / "Team 3_1_assignsubmission_file"
    team_dir.mkdir(parents=True)
    feedback = team_dir / "feedback.md"
    feedback.write_text(build_report("A1", statuses={4: "unverified"}, gaps={4}), encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(json.dumps({"segment_updates": {"S4": CLEAR_S4}}), encoding="utf-8")

    inspect = run_script("scripts/inspect_feedback_segments.py", "A1", str(feedback), "S4", "--fresh-payload", str(payload), "--format", "text")
    assert inspect.returncode == 0, inspect.stderr
    assert "status unverified -> met" in inspect.stdout

    dry = run_script("scripts/regrade_feedback_segments.py", "A1", str(feedback), str(payload), "S4", "--dry-run")
    assert dry.returncode == 0, dry.stderr
    assert "unverified" in feedback.read_text(encoding="utf-8")

    regrade = run_script("scripts/regrade_feedback_segments.py", "A1", str(feedback), str(payload), "S4", "--quiet")
    assert regrade.returncode == 0, regrade.stderr
    assert regrade.stdout.startswith("OK A1:")
    assert (tmp_path / "A1" / "dev.md").exists()
    assert (tmp_path / "A1" / "feedback_release.csv").exists()

    validate = run_script("scripts/validate_feedback_report.py", "A1", str(feedback))
    assert validate.returncode == 0, validate.stdout
