from __future__ import annotations

from datetime import datetime, time, timedelta
import re

import pytest

from tests.conftest import ROOT
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG


@pytest.mark.parametrize("assignment", sorted(ASSIGNMENT_CONFIG))
def test_prompt_segments_match_config(assignment: str) -> None:
    text = (ROOT / assignment / "grading_prompt.md").read_text(encoding="utf-8")
    params = text.split("## Assignment parameters", 1)[1].split("\n## ", 1)[0]
    found = {int(num): name.strip() for num, name in re.findall(r"^- S(\d+): (.+)$", params, re.MULTILINE)}
    assert found == {num: d["name"] for num, d in ASSIGNMENT_CONFIG[assignment]["segment_defs"].items()}
    assert ASSIGNMENT_CONFIG[assignment]["primary_index"] in params


@pytest.mark.parametrize("assignment", sorted(ASSIGNMENT_CONFIG))
def test_extractor_wrapper_exists(assignment: str) -> None:
    wrapper = (ROOT / assignment / "extract_feedback.py").read_text(encoding="utf-8")
    assert f'ASSIGNMENT = "{assignment}"' in wrapper


@pytest.mark.parametrize("assignment", sorted(ASSIGNMENT_CONFIG))
def test_assignment_windows_are_innopolis_timestamps(assignment: str) -> None:
    config = ASSIGNMENT_CONFIG[assignment]
    start = datetime.fromisoformat(config["week_window_start"])
    cutoff = datetime.fromisoformat(config["issue_cutoff"])
    assert start.utcoffset() == timedelta(hours=3)
    assert cutoff.utcoffset() == timedelta(hours=3)
    assert start.time() == time(0, 0)
    assert cutoff.time() == time(23, 59, 59)
    assert start < cutoff


def test_assignment_windows_match_the_published_schedule() -> None:
    assert ASSIGNMENT_CONFIG["A1"]["week_window_start"] == "2026-09-25T00:00:00+03:00"
    assert ASSIGNMENT_CONFIG["A1"]["issue_cutoff"] == "2026-10-02T23:59:59+03:00"
    assert ASSIGNMENT_CONFIG["A2"]["week_window_start"] == "2026-10-02T00:00:00+03:00"
    assert ASSIGNMENT_CONFIG["A2"]["issue_cutoff"] == "2026-10-10T23:59:59+03:00"
    assert ASSIGNMENT_CONFIG["A3"]["week_window_start"] == "2026-10-09T00:00:00+03:00"
    assert ASSIGNMENT_CONFIG["A3"]["issue_cutoff"] == "2026-10-17T23:59:59+03:00"


def test_a2_prompt_carries_the_config_issue_cutoff() -> None:
    text = (ROOT / "A2" / "grading_prompt.md").read_text(encoding="utf-8")
    assert ASSIGNMENT_CONFIG["A2"]["issue_cutoff"] in text


def test_a3_prompt_carries_the_config_issue_cutoff() -> None:
    text = (ROOT / "A3" / "grading_prompt.md").read_text(encoding="utf-8")
    assert ASSIGNMENT_CONFIG["A3"]["issue_cutoff"] in text


@pytest.mark.parametrize("assignment", sorted(ASSIGNMENT_CONFIG))
def test_prompt_carries_the_pinned_course_commit(assignment: str) -> None:
    text = (ROOT / assignment / "grading_prompt.md").read_text(encoding="utf-8")
    assert ASSIGNMENT_CONFIG[assignment]["course_commit"] in text
