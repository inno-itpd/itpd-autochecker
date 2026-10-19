from __future__ import annotations

from datetime import datetime, time, timedelta
import re

import pytest

from tests.conftest import ROOT
from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG

SEGMENT_LINE = re.compile(r"^- S(\d+): (.+)$", re.MULTILINE)
STATUS_HEADING = re.compile(r"^### S(\d+) — (.+)$", re.MULTILINE)

A3_SPRINT_HARD_DEADLINES = {
    "SPRINT-03": "2026-10-17",
    "SPRINT-04": "2026-10-23",
    "SPRINT-05": "2026-10-30",
    "SPRINT-06": "2026-11-06",
    "SPRINT-07": "2026-11-13",
    "SPRINT-08": "2026-11-20",
    "SPRINT-09": "2026-11-27",
}
A3_STALE_SPRINT_DEADLINES = {
    "2026-10-29": "2026-10-30",
    "2026-11-05": "2026-11-06",
    "2026-11-12": "2026-11-13",
    "2026-11-19": "2026-11-20",
    "2026-11-26": "2026-11-27",
}
SYLLABUS_YEAR = 2026
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
WEEK_HEADING = re.compile(r"^### Week (\d+):", re.MULTILINE)
HARD_DEADLINE = re.compile(
    r"\*\*Deadline\*\*: soft \*\*[A-Z][a-z]+ \d{1,2} at \d{2}:\d{2} \([A-Z][a-z]+\)\*\*, "
    r"hard \*\*(?P<month>[A-Z][a-z]+) (?P<day>\d{1,2}) at \d{2}:\d{2} \([A-Z][a-z]+\)\*\*"
)


def _s2_guardrails(text: str) -> str:
    after_s2 = text.split("### S2 ", 1)[1]
    return after_s2.split("**Guardrails:**", 1)[1].split("\n### ", 1)[0]


def _prompt_sprint_deadlines(text: str) -> dict[str, str]:
    for line in _s2_guardrails(text).splitlines():
        if "`SPRINT-03`" in line and "`SPRINT-09`" in line:
            dates = ISO_DATE.findall(line)
            assert len(dates) == len(A3_SPRINT_HARD_DEADLINES), line
            return dict(zip(A3_SPRINT_HARD_DEADLINES, dates))
    raise AssertionError("the S2 guardrails carry no SPRINT-03 to SPRINT-09 deadline list")


def _syllabus_hard_deadlines(text: str) -> dict[int, str]:
    parts = WEEK_HEADING.split(text)
    deadlines: dict[int, str] = {}
    for week, block in zip(parts[1::2], parts[2::2]):
        match = HARD_DEADLINE.search(block)
        if match is None:
            continue
        parsed = datetime.strptime(
            f"{match['month']} {match['day']} {SYLLABUS_YEAR}", "%B %d %Y"
        )
        deadlines[int(week)] = parsed.date().isoformat()
    return deadlines


@pytest.mark.parametrize("assignment", sorted(ASSIGNMENT_CONFIG))
def test_prompt_segments_match_config(assignment: str) -> None:
    text = (ROOT / assignment / "grading_prompt.md").read_text(encoding="utf-8")
    expected = {
        num: definition["name"]
        for num, definition in ASSIGNMENT_CONFIG[assignment]["segment_defs"].items()
    }
    params = text.split("## Assignment parameters", 1)[1].split("\n## ", 1)[0]
    found = {int(num): name.strip() for num, name in SEGMENT_LINE.findall(params)}
    assert found == expected
    assert len(found) == len(expected)
    assert ASSIGNMENT_CONFIG[assignment]["primary_index"] in params

    guide = text.split("## Status guide", 1)[1].split("\n## ", 1)[0]
    headings = {int(num): name.strip() for num, name in STATUS_HEADING.findall(guide)}
    assert headings == expected
    assert len(headings) == len(expected)
    assert len(SEGMENT_LINE.findall(params)) == len(expected)


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


def test_a3_sprint_hard_deadlines_match_the_syllabus() -> None:
    prompt = (ROOT / "A3" / "grading_prompt.md").read_text(encoding="utf-8")
    assert _prompt_sprint_deadlines(prompt) == A3_SPRINT_HARD_DEADLINES

    syllabus = ROOT / "A3" / "itpd" / "course" / "syllabus.md"
    if not syllabus.exists():
        return
    deadlines = _syllabus_hard_deadlines(syllabus.read_text(encoding="utf-8"))
    expected = list(A3_SPRINT_HARD_DEADLINES.values())
    assert [deadlines[week] for week in range(4, 10)] == expected[1:]
    assert deadlines[3] == expected[0]


@pytest.mark.parametrize("stale_date", sorted(A3_STALE_SPRINT_DEADLINES))
def test_a3_sprint_deadlines_reject_a_restored_soft_date(stale_date: str) -> None:
    prompt = (ROOT / "A3" / "grading_prompt.md").read_text(encoding="utf-8")
    hard_date = A3_STALE_SPRINT_DEADLINES[stale_date]
    assert hard_date in _s2_guardrails(prompt)
    restored = prompt.replace(hard_date, stale_date)
    assert restored != prompt
    assert _prompt_sprint_deadlines(restored) != A3_SPRINT_HARD_DEADLINES


def test_a3_markdown_has_no_stale_sprint_deadlines() -> None:
    offenders = [
        f"{path.relative_to(ROOT)}: {stale_date}"
        for path in sorted((ROOT / "A3").rglob("*.md"))
        for stale_date in A3_STALE_SPRINT_DEADLINES
        if stale_date in path.read_text(encoding="utf-8")
    ]
    assert offenders == []
