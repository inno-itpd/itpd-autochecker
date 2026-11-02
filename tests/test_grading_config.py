"""Check the grading settings loader and the repo's grading.json.

`grading.json` is read by the orchestrating agent and by the helper scripts, so
a malformed file degrades to the defaults instead of stopping a batch.  These
tests pin the fallbacks, the repo file itself, and the guide naming the keys.
"""

from __future__ import annotations

import json
from pathlib import Path

from tests.conftest import ROOT
from tools.grader_tools.grading_config import (
    DEFAULT_MAX_AGENT_RESUMES,
    DEFAULT_TEAM_BATCH_SIZE,
    GradingConfig,
    load_grading_config,
    parse_grading_config,
)

GRADING_CONFIG = ROOT / "grading.json"
AGENTS_GUIDE = ROOT / "AGENTS.md"
REQUIRED_KEYS = ("team_batch_size", "max_agent_resumes")


def test_repo_config_has_the_documented_keys() -> None:
    config = json.loads(GRADING_CONFIG.read_text(encoding="utf-8"))
    assert isinstance(config, dict)
    assert [key for key in REQUIRED_KEYS if key in config] == list(REQUIRED_KEYS)


def test_repo_grading_config_loads_positive_values() -> None:
    config = load_grading_config()
    for value in (config.team_batch_size, config.max_agent_resumes):
        assert isinstance(value, int) and not isinstance(value, bool)
        assert value > 0


def test_agents_guide_names_both_keys_and_the_defaults() -> None:
    guide = AGENTS_GUIDE.read_text(encoding="utf-8")
    for key in REQUIRED_KEYS:
        assert key in guide, key
    assert "Default to `8` and `4`" in guide


def test_missing_config_file_degrades_to_the_documented_defaults(tmp_path: Path) -> None:
    config = load_grading_config(tmp_path)
    assert config == GradingConfig(DEFAULT_TEAM_BATCH_SIZE, DEFAULT_MAX_AGENT_RESUMES)


def test_invalid_json_and_non_objects_degrade_to_defaults(tmp_path: Path) -> None:
    (tmp_path / "grading.json").write_text("{not json", encoding="utf-8")
    assert load_grading_config(tmp_path) == GradingConfig()
    assert parse_grading_config(["not", "a", "dict"]) == GradingConfig()


def test_invalid_values_fall_back_per_field() -> None:
    config = parse_grading_config({"team_batch_size": 12, "max_agent_resumes": "4"})
    assert config.team_batch_size == 12
    assert config.max_agent_resumes == DEFAULT_MAX_AGENT_RESUMES

    for bad in (0, -3, True, 2.5, None):
        parsed = parse_grading_config({"team_batch_size": bad, "max_agent_resumes": bad})
        assert parsed == GradingConfig(DEFAULT_TEAM_BATCH_SIZE, DEFAULT_MAX_AGENT_RESUMES)


def test_valid_values_are_read_from_the_file(tmp_path: Path) -> None:
    (tmp_path / "grading.json").write_text('{"team_batch_size": 3, "max_agent_resumes": 2}', encoding="utf-8")
    assert load_grading_config(tmp_path) == GradingConfig(3, 2)


def test_line_renders_both_settings() -> None:
    assert GradingConfig(10, 4).line == "grading: team_batch_size=10, max_agent_resumes=4"
