from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from scripts.patch_feedback_report import patch_report
from scripts.regrade_feedback_segments import build_subset_payload
from tests.conftest import ROOT
from tests.report_builder import REPO, SHA, build_report, unresolved_preamble
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import apply_structured_segment_update, parse_feedback_text, parse_unresolved_section
from tools.grader_tools.validate import validate_report

A1_DEFS = ASSIGNMENT_CONFIG["A1"]["segment_defs"]
A1_INDEX = ASSIGNMENT_CONFIG["A1"]["primary_index"]
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
    team_dir = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file"
    team_dir.mkdir(parents=True)
    feedback = team_dir / "agent-feedback.md"
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


def metadata_report(notes: str = "The PDF permalink could not be resolved."):
    return parse_feedback_text(build_report("A1", preamble_text=unresolved_preamble("A1", notes=notes)), A1_DEFS)


@pytest.mark.parametrize("repository", ["itpd-team-3/meeting-notes", REPO])
def test_patch_resolves_metadata_and_removes_notes(repository: str) -> None:
    rendered = patch_report(
        "A1",
        metadata_report(),
        {
            "report": {"repository": repository, "snapshot": SHA},
            "segment_updates": {"S4": CLEAR_S4},
        },
    )
    assert "- Team: 3" in rendered
    assert rendered.startswith("# Assignment 1 Feedback Report\n")
    assert f"- Repository reviewed: `{REPO}`" in rendered
    assert f"- Snapshot reviewed: `{SHA}`" in rendered
    assert f"- Primary index reviewed: [`{A1_INDEX}`]({REPO}/blob/{SHA}/{A1_INDEX})" in rendered
    assert "Notes about the snapshot" not in rendered
    assert validate_report("A1", parse_feedback_text(rendered, A1_DEFS)) == []


def test_patch_keeps_unresolved_metadata_and_notes() -> None:
    notes = "The repository was not reachable."
    rendered = patch_report(
        "A1",
        metadata_report(notes),
        {"report": {"repository": None, "snapshot": None}, "segment_updates": {"S4": CLEAR_S4}},
    )
    assert "- Repository reviewed: none" in rendered
    assert "- Snapshot reviewed: none" in rendered
    assert "- Primary index reviewed: none" in rendered
    assert f"- Notes about the snapshot: {notes}" in rendered
    assert validate_report("A1", parse_feedback_text(rendered, A1_DEFS)) == []


def test_patch_requires_notes_when_the_pair_is_unresolved() -> None:
    report = parse_feedback_text(build_report("A1"), A1_DEFS)
    with pytest.raises(ValueError, match="notes"):
        patch_report("A1", report, {"report": {"snapshot": None}, "segment_updates": {"S4": CLEAR_S4}})


def test_patch_rejects_notes_when_the_pair_is_resolved() -> None:
    with pytest.raises(ValueError, match="notes"):
        patch_report(
            "A1",
            metadata_report(),
            {
                "report": {"repository": REPO, "snapshot": SHA, "notes": "Not needed."},
                "segment_updates": {"S4": CLEAR_S4},
            },
        )


def test_patch_rejects_a_different_primary_index() -> None:
    with pytest.raises(ValueError, match="primary_index"):
        patch_report(
            "A1",
            metadata_report(),
            {"report": {"primary_index": "reports/week-02/README.md"}, "segment_updates": {"S4": CLEAR_S4}},
        )


def test_patch_replaces_report_sections() -> None:
    rendered = patch_report(
        "A1",
        parse_feedback_text(build_report("A1"), A1_DEFS),
        {
            "sections": {
                "summary": ["New first.", "New second.", "New third."],
                "strengths": ["New strength."],
                "main_issues_to_fix": ["New issue."],
            },
            "segment_updates": {"S4": CLEAR_S4},
        },
    )
    patched = parse_feedback_text(rendered, A1_DEFS)
    assert patched.summary_body == "- New first.\n- New second.\n- New third."
    assert patched.strengths_body == "- New strength."
    assert patched.main_issues_body == "- New issue."
    assert validate_report("A1", patched) == []


def test_patch_accepts_the_main_issues_alias() -> None:
    rendered = patch_report(
        "A1",
        parse_feedback_text(build_report("A1"), A1_DEFS),
        {"sections": {"main_issues": ["Aliased issue."]}, "segment_updates": {"S4": CLEAR_S4}},
    )
    assert parse_feedback_text(rendered, A1_DEFS).main_issues_body == "- Aliased issue."


@pytest.mark.parametrize(
    ("sections", "match"),
    [
        pytest.param({"summary": ["One.", "Two."]}, "at least 3", id="short-summary"),
        pytest.param({"strengths": []}, "at least 1", id="empty-strengths"),
        pytest.param({"main_issues_to_fix": []}, "at least 1", id="empty-main-issues"),
        pytest.param({"summary": ["One.", "Two.", "Three.\nFour."]}, "single lines", id="multi-line-bullet"),
    ],
)
def test_patch_rejects_invalid_sections(sections: dict[str, object], match: str) -> None:
    with pytest.raises(ValueError, match=match):
        patch_report(
            "A1",
            parse_feedback_text(build_report("A1"), A1_DEFS),
            {"sections": sections, "segment_updates": {"S4": CLEAR_S4}},
        )


def test_patch_rejects_a_section_supplied_both_ways() -> None:
    with pytest.raises(ValueError, match="both"):
        patch_report(
            "A1",
            parse_feedback_text(build_report("A1"), A1_DEFS),
            {
                "sections": {"summary": ["One.", "Two.", "Three."]},
                "summary": "- One.\n- Two.\n- Three.",
                "segment_updates": {"S4": CLEAR_S4},
            },
        )


def test_patch_keeps_the_top_level_string_sections() -> None:
    rendered = patch_report(
        "A1",
        parse_feedback_text(build_report("A1"), A1_DEFS),
        {"summary": "- Only one.\n- Only two.\n- Only three.", "segment_updates": {"S4": CLEAR_S4}},
    )
    assert parse_feedback_text(rendered, A1_DEFS).summary_body == "- Only one.\n- Only two.\n- Only three."


def regrade_payload(include_metadata: bool = True) -> dict[str, object]:
    payload: dict[str, object] = {
        "segment_updates": {"S4": CLEAR_S4},
        "sections": {
            "summary": ["New first.", "New second.", "New third."],
            "strengths": ["New strength."],
            "main_issues_to_fix": ["New issue."],
        },
    }
    if include_metadata:
        payload["report"] = {"repository": "itpd-team-3/meeting-notes", "snapshot": SHA}
    return payload


def test_inspect_reports_metadata_and_section_changes(tmp_path: Path) -> None:
    feedback = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file" / "agent-feedback.md"
    feedback.parent.mkdir(parents=True)
    feedback.write_text(build_report("A1", preamble_text=unresolved_preamble("A1")), encoding="utf-8")
    before = feedback.read_text(encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(json.dumps(regrade_payload()), encoding="utf-8")

    text = run_script(
        "scripts/inspect_feedback_segments.py",
        "A1",
        str(feedback),
        "S4",
        "--fresh-payload",
        str(payload),
        "--format",
        "text",
    )
    assert text.returncode == 0, text.stderr
    assert "Predicted metadata changes:" in text.stdout
    assert f"- snapshot none -> {SHA}" in text.stdout
    assert "- notes removed" in text.stdout
    assert "Predicted section changes:" in text.stdout
    assert "- summary updated" in text.stdout
    assert "- main issues updated" in text.stdout
    assert feedback.read_text(encoding="utf-8") == before

    data = run_script(
        "scripts/inspect_feedback_segments.py",
        "A1",
        str(feedback),
        "S4",
        "--fresh-payload",
        str(payload),
        "--format",
        "json",
    )
    assert data.returncode == 0, data.stderr
    output = json.loads(data.stdout)
    metadata = output["predicted_report_metadata"]
    assert metadata["saved"]["snapshot"] is None
    assert metadata["predicted"]["snapshot"] == SHA
    assert f"snapshot none -> {SHA}" in metadata["changes"]
    assert "notes removed" in metadata["changes"]
    sections = output["predicted_report_sections"]
    assert sections["predicted"]["summary"] == "- New first.\n- New second.\n- New third."
    assert "summary updated" in sections["changes"]
    assert feedback.read_text(encoding="utf-8") == before


def test_regrade_cli_applies_metadata_and_sections(tmp_path: Path) -> None:
    team_dir = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file"
    team_dir.mkdir(parents=True)
    feedback = team_dir / "agent-feedback.md"
    feedback.write_text(build_report("A1", preamble_text=unresolved_preamble("A1")), encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(json.dumps(regrade_payload()), encoding="utf-8")

    regrade = run_script("scripts/regrade_feedback_segments.py", "A1", str(feedback), str(payload), "S4", "--quiet")
    assert regrade.returncode == 0, regrade.stderr
    assert regrade.stdout.startswith("OK A1:")

    patched = parse_feedback_text(feedback.read_text(encoding="utf-8"), A1_DEFS)
    assert validate_report("A1", patched) == []
    assert patched.segment_blocks[4].evidence == ["Instructor-reviewed: the comparison board is public."]
    assert f"- Snapshot reviewed: `{SHA}`" in feedback.read_text(encoding="utf-8")
    assert "Notes about the snapshot" not in feedback.read_text(encoding="utf-8")
    assert patched.summary_body == "- New first.\n- New second.\n- New third."
    assert (tmp_path / "A1" / "dev.md").exists()


def test_regrade_fails_closed_and_keeps_the_report(tmp_path: Path) -> None:
    team_dir = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file"
    team_dir.mkdir(parents=True)
    feedback = team_dir / "agent-feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    before = feedback.read_text(encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(
        json.dumps(
            {
                "segment_updates": {
                    "S4": {
                        "status": "partial",
                        "evidence_gaps": False,
                        "evidence": ["A shortfall without a verified bullet."],
                        "verified_shortfalls": [],
                        "unverified_checks": [],
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    regrade = run_script("scripts/regrade_feedback_segments.py", "A1", str(feedback), str(payload), "S4", "--quiet")
    assert regrade.returncode == 2
    assert regrade.stdout.startswith("ERROR:")
    assert "Patched report would not validate" in regrade.stdout
    assert feedback.read_text(encoding="utf-8") == before
    assert not (tmp_path / "A1" / "dev.md").exists()


def test_regrade_fails_closed_on_invalid_metadata(tmp_path: Path) -> None:
    team_dir = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file"
    team_dir.mkdir(parents=True)
    feedback = team_dir / "agent-feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    before = feedback.read_text(encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(
        json.dumps({"report": {"snapshot": None}, "segment_updates": {"S4": CLEAR_S4}}),
        encoding="utf-8",
    )

    regrade = run_script("scripts/regrade_feedback_segments.py", "A1", str(feedback), str(payload), "S4", "--quiet")
    assert regrade.returncode == 2
    assert regrade.stdout.startswith("ERROR:")
    assert "notes" in regrade.stdout
    assert feedback.read_text(encoding="utf-8") == before


def test_patch_cli_fails_closed_and_keeps_the_report(tmp_path: Path) -> None:
    feedback = tmp_path / "agent-feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    before = feedback.read_text(encoding="utf-8")
    payload = tmp_path / "payload.json"
    payload.write_text(json.dumps({"sections": {"summary": ["One.", "Two."]}}), encoding="utf-8")

    patched = run_script("scripts/patch_feedback_report.py", "A1", str(feedback), str(payload))
    assert patched.returncode == 2
    assert patched.stdout.startswith("ERROR:")
    assert feedback.read_text(encoding="utf-8") == before


def test_patch_keeps_none_when_only_the_snapshot_is_resolved() -> None:
    rendered = patch_report(
        "A1",
        metadata_report(),
        {"report": {"snapshot": SHA}, "segment_updates": {"S4": CLEAR_S4}},
    )
    assert "- Repository reviewed: none" in rendered
    assert f"- Snapshot reviewed: `{SHA}`" in rendered
    assert "- Primary index reviewed: none" in rendered
    assert "- Notes about the snapshot: The PDF permalink could not be resolved." in rendered
    assert validate_report("A1", parse_feedback_text(rendered, A1_DEFS)) == []


def test_patch_rejects_removing_required_notes() -> None:
    with pytest.raises(ValueError, match="required"):
        patch_report("A1", metadata_report(), {"report": {"notes": None}, "segment_updates": {"S4": CLEAR_S4}})
