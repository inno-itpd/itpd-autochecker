from __future__ import annotations

from pathlib import Path

from tests.conftest import ROOT

PROMPT = ROOT / "A3" / "grading_prompt.md"

# These selections drifted from the live schema and are not documented routes:
# the project description field is gone, the project fields connection is a
# union, and the ordered issue connection rejected the documented selection.
STALE_SELECTIONS = (
    "ProjectV2.description",
    "projectV2.fields",
    "repository.issues(orderBy:",
)

DOCUMENTED_SOURCES = (
    *sorted((ROOT / "scripts").glob("*.py")),
    *sorted((ROOT / "tools" / "grader_tools").glob("*.py")),
    ROOT / "agents" / "grader.md",
    PROMPT,
)


def test_no_documented_route_uses_a_stale_project_selection() -> None:
    offenders = [
        f"{path.relative_to(ROOT)}: {stale}"
        for path in DOCUMENTED_SOURCES
        for stale in STALE_SELECTIONS
        if stale in path.read_text(encoding="utf-8")
    ]
    assert offenders == []


def test_s6_documents_the_current_project_routes() -> None:
    text = PROMPT.read_text(encoding="utf-8")
    for route in (
        "gh project list --owner <org> --format json",
        "gh project field-list <number> --owner <org> --format json",
        "gh project view <number> --owner <org> --format json",
        "shortDescription",
        "items(first: 100)",
        "fieldValues(first: 20)",
        "views(first: 20)",
    ):
        assert route in text, route


def test_s6_says_which_project_route_answered() -> None:
    text = PROMPT.read_text(encoding="utf-8")
    assert "which route answered" in text
    assert "say in `**Evidence:**` which route answered" in text


def test_agents_prompt_keeps_the_current_project_fields_connection() -> None:
    text = (ROOT / "agents" / "grader.md").read_text(encoding="utf-8")
    assert ".data.organization.projectV2.items.nodes[]" in text
    assert ".fieldValues.nodes // []" in text
