from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys

import pytest

from scripts.render_feedback_report import (
    INCOMPLETE_SEGMENT_EVIDENCE,
    INCOMPLETE_SEGMENT_PLACEHOLDER,
    render_feedback_report,
    run,
)
from tests.conftest import ROOT
from tests.report_builder import REPO, SHA, build_report
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.feedback_report import parse_feedback_text, parse_unresolved_section
from tools.grader_tools.validate import validate_report

A1_DEFS = ASSIGNMENT_CONFIG["A1"]["segment_defs"]


def segment_updates(assignment: str, statuses: dict[int, str], gaps: set[int]) -> dict[str, dict[str, object]]:
    updates: dict[str, dict[str, object]] = {}
    for seg_num in ASSIGNMENT_CONFIG[assignment]["segment_defs"]:
        status = statuses.get(seg_num, "met")
        has_gap = seg_num in gaps
        updates[f"S{seg_num}"] = {
            "status": status,
            "evidence_gaps": has_gap,
            "evidence": [f"S{seg_num} evidence."],
            "verified_shortfalls": [f"S{seg_num} shortfall."] if status in ("partial", "missing") else [],
            "unverified_checks": [f"S{seg_num} blocked check."] if has_gap else [],
        }
    return updates


def full_payload(
    output_path: Path,
    assignment: str = "A1",
    statuses: dict[int, str] | None = None,
    gaps: set[int] | None = None,
) -> dict[str, object]:
    statuses = statuses or {}
    gaps = gaps or set()
    return {
        "output_path": str(output_path),
        "team": 3,
        "repository": REPO,
        "snapshot": SHA,
        "summary": ["First shortfall.", "Second shortfall.", "Third shortfall."],
        "strengths": ["A verified strength."],
        "main_issues_to_fix": ["A fixable issue."],
        "segment_updates": segment_updates(assignment, statuses, gaps),
        "unresolved_evidence_gaps": {f"S{num}": [f"S{num} gap detail."] for num in sorted(gaps)},
    }


def full_update() -> dict[str, object]:
    return {
        "status": "met",
        "evidence_gaps": False,
        "evidence": ["S10 evidence."],
        "verified_shortfalls": [],
        "unverified_checks": [],
    }


def fail_render(tmp_path: Path, payload: dict[str, object], match: str, *, assignment: str = "A1") -> None:
    payload_path = tmp_path / "payload.json"
    payload_path.write_text(json.dumps(payload), encoding="utf-8")
    output_value = payload.get("output_path")
    lines: list[str] = []
    assert run([assignment, str(payload_path)], out=lines.append) == 2
    assert lines and lines[0].startswith("ERROR: ")
    assert match.lower() in lines[0].lower()
    if isinstance(output_value, str):
        assert not Path(output_value).exists()


def test_render_matches_the_report_builder(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    rendered, output_path = render_feedback_report("A1", payload)
    assert rendered == build_report("A1", statuses={4: "unverified"}, gaps={4})
    assert output_path == tmp_path / "agent-feedback.md"
    assert not output_path.exists()


def test_a2_payload_renders_a_valid_report(tmp_path: Path) -> None:
    output = tmp_path / "agent-feedback.md"
    payload = full_payload(output, assignment="A2", statuses={2: "missing", 5: "partial", 8: "unverified"}, gaps={8})
    rendered, _ = render_feedback_report("A2", payload)
    defs = ASSIGNMENT_CONFIG["A2"]["segment_defs"]
    assert validate_report("A2", parse_feedback_text(rendered, defs)) == []


def test_cli_writes_a_report_that_passes_the_validator(tmp_path: Path) -> None:
    output = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file" / "agent-feedback.md"
    payload = full_payload(output, statuses={1: "partial", 4: "unverified"}, gaps={4, 7})
    payload_path = tmp_path / "payload.json"
    payload_path.write_text(json.dumps(payload), encoding="utf-8")

    lines: list[str] = []
    assert run(["A1", str(payload_path)], out=lines.append) == 0
    assert lines == [f"Wrote {output}"]
    assert validate_report("A1", parse_feedback_text(output.read_text(encoding="utf-8"), A1_DEFS)) == []

    validate = subprocess.run(
        [sys.executable, "scripts/validate_feedback_report.py", "A1", str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert validate.returncode == 0, validate.stdout + validate.stderr


def test_missing_snapshot_uses_none_and_notes(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload.pop("repository")
    payload.pop("snapshot")
    payload["snapshot_notes"] = "The PDF permalink could not be resolved."
    rendered, _ = render_feedback_report("A1", payload)
    assert "- Repository reviewed: none" in rendered
    assert "- Snapshot reviewed: none" in rendered
    assert "- Primary index reviewed: none" in rendered
    assert "- Notes about the snapshot: The PDF permalink could not be resolved." in rendered
    assert validate_report("A1", parse_feedback_text(rendered, A1_DEFS)) == []


def test_partial_payload_renders_unverified_placeholders(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    updates = payload["segment_updates"]
    assert isinstance(updates, dict)
    for selector in ("S8", "S9"):
        updates.pop(selector)

    rendered, _ = render_feedback_report("A1", payload)
    report = parse_feedback_text(rendered, A1_DEFS)
    assert validate_report("A1", report) == []

    for seg_num in (8, 9):
        block = report.segment_blocks[seg_num]
        assert block.status == "unverified"
        assert block.evidence_gaps is True
        assert block.verified_shortfalls == []
        assert block.evidence == [INCOMPLETE_SEGMENT_EVIDENCE]
        assert block.unverified_checks == [INCOMPLETE_SEGMENT_PLACEHOLDER]

    assert report.segment_blocks[1].status == "met"
    assert report.segment_blocks[4].status == "unverified"
    assert "- Met: `6/9`" in report.assessment_body
    assert "- Unverified: `3/9`" in report.assessment_body

    unresolved = parse_unresolved_section(report.unresolved_body, A1_DEFS)
    assert unresolved[4] == ["S4 gap detail."]
    assert unresolved[8] == [INCOMPLETE_SEGMENT_PLACEHOLDER]
    assert unresolved[9] == [INCOMPLETE_SEGMENT_PLACEHOLDER]


def test_placeholder_segments_never_render_as_met(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload["segment_updates"].pop("S9")

    rendered, _ = render_feedback_report("A1", payload)
    report = parse_feedback_text(rendered, A1_DEFS)
    row = next(line for line in rendered.splitlines() if line.startswith("| [S9:"))
    assert row.endswith("| unverified | yes |")
    assert report.segments_table.statuses[9] == "unverified"
    assert report.segments_table.evidence_gaps[9] is True
    assert report.segment_blocks[9].status != "met"
    assert "| Manual review required | yes | |" in rendered


def test_partial_payload_preserves_supplied_gap_bullets(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    payload["segment_updates"].pop("S9")
    payload["unresolved_evidence_gaps"] = {"S4": ["A hand-written S4 bullet."]}

    rendered, _ = render_feedback_report("A1", payload)
    report = parse_feedback_text(rendered, A1_DEFS)
    assert validate_report("A1", report) == []
    unresolved = parse_unresolved_section(report.unresolved_body, A1_DEFS)
    assert unresolved[4] == ["A hand-written S4 bullet."]
    assert unresolved[9] == [INCOMPLETE_SEGMENT_PLACEHOLDER]


def test_cli_writes_a_partial_report_that_passes_the_validator(tmp_path: Path) -> None:
    output = tmp_path / "A1" / "feedback" / "Team 3_1_assignsubmission_file" / "agent-feedback.md"
    payload = full_payload(output)
    updates = payload["segment_updates"]
    assert isinstance(updates, dict)
    for selector in ("S5", "S6", "S7", "S8", "S9"):
        updates.pop(selector)
    payload_path = tmp_path / "payload.json"
    payload_path.write_text(json.dumps(payload), encoding="utf-8")

    lines: list[str] = []
    assert run(["A1", str(payload_path)], out=lines.append) == 0
    assert lines == [f"Wrote {output}"]

    validate = subprocess.run(
        [sys.executable, "scripts/validate_feedback_report.py", "A1", str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert validate.returncode == 0, validate.stdout + validate.stderr


def test_failed_render_keeps_an_existing_report(tmp_path: Path) -> None:
    output = tmp_path / "agent-feedback.md"
    output.write_text("old report\n", encoding="utf-8")
    payload = full_payload(output)
    updates = payload["segment_updates"]
    assert isinstance(updates, dict)
    updates["S1"]["status"] = "great"
    payload_path = tmp_path / "payload.json"
    payload_path.write_text(json.dumps(payload), encoding="utf-8")

    lines: list[str] = []
    assert run(["A1", str(payload_path)], out=lines.append) == 2
    assert lines[0].startswith("ERROR: ")
    assert "status" in lines[0]
    assert output.read_text(encoding="utf-8") == "old report\n"


def test_rejects_unparsable_payload(tmp_path: Path) -> None:
    payload_path = tmp_path / "payload.json"
    payload_path.write_text("{not json", encoding="utf-8")
    lines: list[str] = []
    assert run(["A1", str(payload_path)], out=lines.append) == 2
    assert "Cannot parse payload" in lines[0]


def test_rejects_non_object_payload(tmp_path: Path) -> None:
    payload_path = tmp_path / "payload.json"
    payload_path.write_text("[1, 2]", encoding="utf-8")
    lines: list[str] = []
    assert run(["A1", str(payload_path)], out=lines.append) == 2
    assert "must be a JSON object" in lines[0]


def test_rejects_unknown_assignment(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Unknown assignment"):
        render_feedback_report("A9", full_payload(tmp_path / "agent-feedback.md"))


@pytest.mark.parametrize(
    ("mutate", "match"),
    [
        pytest.param(lambda payload: payload.pop("output_path"), "output_path", id="missing-output-path"),
        pytest.param(lambda payload: payload.__setitem__("team", "3"), "team", id="team-not-an-integer"),
        pytest.param(lambda payload: payload.__setitem__("team", 0), "team", id="team-zero"),
        pytest.param(
            lambda payload: payload.__setitem__("repository", "github.com/o/r"), "repository", id="bad-repository"
        ),
        pytest.param(lambda payload: payload.__setitem__("snapshot", SHA.upper()), "snapshot", id="uppercase-snapshot"),
        pytest.param(lambda payload: payload.__setitem__("snapshot", SHA[:8]), "snapshot", id="short-snapshot"),
        pytest.param(lambda payload: payload.__setitem__("summary", ["One.", "Two."]), "summary", id="short-summary"),
        pytest.param(lambda payload: payload.__setitem__("strengths", []), "strengths", id="empty-strengths"),
        pytest.param(
            lambda payload: payload.__setitem__("main_issues_to_fix", None), "main_issues_to_fix", id="missing-issues"
        ),
        pytest.param(lambda payload: payload.__setitem__("sumary", []), "unexpected payload", id="typo-top-level-key"),
    ],
)
def test_rejects_bad_top_level_fields(tmp_path: Path, mutate, match: str) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    mutate(payload)
    fail_render(tmp_path, payload, match)


def test_rejects_notes_when_metadata_is_complete(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload["snapshot_notes"] = "Not needed."
    fail_render(tmp_path, payload, "snapshot_notes")


def test_requires_notes_when_snapshot_is_missing(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload["snapshot"] = None
    fail_render(tmp_path, payload, "snapshot_notes")


@pytest.mark.parametrize(
    ("mutate", "match"),
    [
        pytest.param(
            lambda payload: payload.__setitem__("segment_updates", ["S1"]),
            "segment_updates",
            id="segment-updates-not-an-object",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"].__setitem__("S10", full_update()),
            "not a segment",
            id="unknown-segment",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].__setitem__("status", "great"),
            "status",
            id="bad-status",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].pop("evidence"), "evidence", id="missing-evidence"
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].pop("evidence_gaps"),
            "evidence_gaps",
            id="missing-gaps-flag",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].__setitem__("verified_shortfall", []),
            "unexpected payload",
            id="typo-segment-key",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S2"].__setitem__("status", "partial"),
            "verified_shortfalls",
            id="partial-without-verified-shortfalls",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].__setitem__("verified_shortfalls", ["Should be dropped."]),
            "must be empty",
            id="met-with-verified-shortfalls",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S2"].__setitem__("evidence_gaps", True),
            "unverified_checks",
            id="gap-without-unverified-checks",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].__setitem__("unverified_checks", ["Not blocked."]),
            "must be empty",
            id="unverified-checks-without-gap",
        ),
        pytest.param(
            lambda payload: payload["segment_updates"]["S1"].__setitem__("status", "unverified"),
            "evidence_gaps",
            id="unverified-without-gap",
        ),
    ],
)
def test_rejects_bad_segment_updates(tmp_path: Path, mutate, match: str) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    mutate(payload)
    fail_render(tmp_path, payload, match)


def test_rejects_unresolved_bullets_for_a_segment_without_gaps(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload["unresolved_evidence_gaps"] = {"S3": ["Not a gap."]}
    fail_render(tmp_path, payload, "evidence_gaps")


def test_requires_unresolved_bullets_for_gap_segments(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    payload["unresolved_evidence_gaps"] = {}
    fail_render(tmp_path, payload, "needs bullets for: S4")


def test_rejects_empty_unresolved_bullets(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    payload["unresolved_evidence_gaps"] = {"S4": []}
    fail_render(tmp_path, payload, "at least 1 bullet")


def test_rejects_multi_line_bullets(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md")
    payload["summary"] = ["One.", "Two.\nThree.", "Four."]
    fail_render(tmp_path, payload, "single lines")


def test_payload_is_not_mutated(tmp_path: Path) -> None:
    payload = full_payload(tmp_path / "agent-feedback.md", statuses={4: "unverified"}, gaps={4})
    before = copy.deepcopy(payload)
    render_feedback_report("A1", payload)
    assert payload == before
