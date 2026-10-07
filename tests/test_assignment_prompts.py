from __future__ import annotations

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
