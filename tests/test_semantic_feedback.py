"""Tests for the semantic feedback companion file validator."""

from __future__ import annotations

import hashlib

from tools.grader_tools.semantic_feedback import (
    validate_claim_ledger,
    validate_semantic_feedback,
)

SNAPSHOT = "a" * 40
REPOSITORY = "https://github.com/example/repo"
DIMENSIONS = ("Setup", "Tests", "Plan", "Customer loop", "Publication")


def _default_help(verdict: str) -> str:
    return "What would make it stronger" if verdict == "adequate" else "What would make it adequate"


def _dimension(name: str, verdict: str, help_heading: str) -> str:
    return f"""## {name}

**Verdict:** {verdict}

**What works.** The artifact does its job for a reader who was not in the room.

**What breaks first.** One load-bearing part is still unproven.

**{help_heading}.** Add the check before the next sprint.

**Evidence:**

- [`docs/deployment.md`]({REPOSITORY}/blob/{SNAPSHOT}/docs/deployment.md) names the environments.
"""


def build_semantic(
    *,
    dimensions: tuple[str, ...] = DIMENSIONS,
    verdicts: dict[str, str] | None = None,
    help_headings: dict[str, str] | None = None,
    where_to_start: tuple[str, ...] = ("Add the check.", "Record the verdict.", "Plan the sprint."),
    team: int = 5,
    repository: str = REPOSITORY,
    snapshot: str = SNAPSHOT,
    how_to_read: str = "This file judges whether the artifacts do their job, and it changes no status.",
    title_assignment: str = "5",
) -> str:
    verdicts = verdicts or {}
    help_headings = help_headings or {}
    body = "\n".join(
        _dimension(
            name,
            verdicts.get(name, "thin"),
            help_headings.get(name, _default_help(verdicts.get(name, "thin"))),
        )
        for name in dimensions
    )
    bullets = "\n".join(f"- {bullet}" for bullet in where_to_start)
    return f"""# Assignment {title_assignment} Semantic Feedback

- Team: {team}
- Repository: `{repository}`
- Snapshot: `{snapshot}`
- Structural report: [`agent-feedback.md`](./agent-feedback.md)

## How to read this

{how_to_read}

{body}
## Where to start

{bullets}
"""


def build_report(
    *,
    team: int = 5,
    repository: str = REPOSITORY,
    snapshot: str = SNAPSHOT,
) -> str:
    return f"""# Assignment 5 Feedback Report

- Team: {team}
- Repository reviewed: `{repository}`
- Snapshot reviewed: `{snapshot}`
- Primary index reviewed: none

- Notes about the snapshot: no permalink.

## Overall assessment
"""


def errors_for(text: str, report_text: str | None = None) -> list[str]:
    return validate_semantic_feedback(text, "A5", report_text=report_text or build_report())


def test_valid_file_passes() -> None:
    assert errors_for(build_semantic()) == []


def test_adequate_dimension_uses_the_stronger_block() -> None:
    text = build_semantic(verdicts={"Publication": "adequate"})
    assert errors_for(text) == []


def test_adequate_dimension_with_the_adequate_block_fails() -> None:
    text = build_semantic(
        verdicts={"Publication": "adequate"},
        help_headings={"Publication": "What would make it adequate"},
    )
    assert any("blocks must be" in error for error in errors_for(text))


def test_unknown_verdict_fails() -> None:
    text = build_semantic(verdicts={"Tests": "ok"})
    assert any("has verdict `ok`" in error for error in errors_for(text))


def test_too_few_dimensions_fail() -> None:
    text = build_semantic(dimensions=("Setup", "Tests"))
    assert any("between 3 and 5" in error for error in errors_for(text))


def test_out_of_order_dimensions_fail() -> None:
    text = build_semantic(dimensions=("Setup", "Plan", "Tests", "Customer loop", "Publication"))
    assert any("follow the assignment prompt's order" in error for error in errors_for(text))


def test_status_vocabulary_fails() -> None:
    text = build_semantic().replace("One load-bearing part is still unproven.", "The outcome is partial.")
    assert any("status vocabulary" in error for error in errors_for(text))


def test_mentor_wording_fails() -> None:
    text = build_semantic().replace("Add the check before the next sprint.", "Ask a mentor before the next sprint.")
    assert any('"mentor" wording' in error for error in errors_for(text))


def test_evidence_without_a_link_fails() -> None:
    text = build_semantic().replace(
        f"- [`docs/deployment.md`]({REPOSITORY}/blob/{SNAPSHOT}/docs/deployment.md) names the environments.",
        "- The deployment names the environments.",
        1,
    )
    assert any("needs at least one link" in error for error in errors_for(text))


def test_blob_link_with_another_snapshot_fails() -> None:
    text = build_semantic().replace(f"/blob/{SNAPSHOT}/", f"/blob/{'b' * 40}/", 1)
    assert any("the snapshot is" in error for error in errors_for(text))


def test_metadata_mismatch_with_the_report_fails() -> None:
    text = build_semantic(team=6)
    assert any("does not match `agent-feedback.md`" in error for error in errors_for(text))


def test_missing_report_preamble_fails() -> None:
    errors = validate_semantic_feedback(build_semantic(), "A5", report_text="# Assignment 5 Feedback Report\n")
    assert any("does not carry a readable" in error for error in errors)


def test_where_to_start_needs_two_bullets() -> None:
    text = build_semantic(where_to_start=("Add the check.",))
    assert any("must contain 2-3 bullets" in error for error in errors_for(text))


def test_nested_evidence_bullet_fails() -> None:
    text = build_semantic().replace(
        f"- [`docs/deployment.md`]({REPOSITORY}/blob/{SNAPSHOT}/docs/deployment.md) names the environments.",
        f"  - [`docs/deployment.md`]({REPOSITORY}/blob/{SNAPSHOT}/docs/deployment.md) names the environments.",
        1,
    )
    errors = errors_for(text)
    assert errors and "nested evidence bullets" in errors[0]


def test_assignment_without_dimensions_fails() -> None:
    text = build_semantic(title_assignment="4")
    errors = validate_semantic_feedback(text, "A4", report_text=None)
    assert any("no semantic dimensions" in error for error in errors)


def _ledger(report_text: str) -> dict[str, object]:
    return {
        "assignment": "A5",
        "team_dir": "Team 5 - TmpTeam_12345_assignsubmission_file",
        "snapshot": SNAPSHOT,
        "report_sha256": hashlib.sha256(report_text.encode("utf-8")).hexdigest(),
        "claims": [],
        "conflicts": [],
    }


def test_ledger_with_the_current_report_hash_passes() -> None:
    report = build_report()
    assert validate_claim_ledger(_ledger(report), report) == []


def test_ledger_with_a_stale_report_hash_fails() -> None:
    report = build_report()
    ledger = _ledger(report)
    ledger["report_sha256"] = "0" * 64
    errors = validate_claim_ledger(ledger, report)
    assert errors and "does not match agent-feedback.md" in errors[0]


def test_ledger_without_a_report_hash_fails() -> None:
    ledger = _ledger(build_report())
    del ledger["report_sha256"]
    errors = validate_claim_ledger(ledger, build_report())
    assert errors == ["the claim ledger has no `report_sha256`"]


def test_ledger_must_be_a_json_object() -> None:
    assert validate_claim_ledger([], build_report()) == ["the claim ledger must be a JSON object"]
