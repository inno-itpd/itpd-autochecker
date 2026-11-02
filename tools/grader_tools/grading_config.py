"""Read the grading settings shared by the batch tooling.

`grading.json` at the repository root carries the parallel batch size and the
per-team resume budget.  The harness agent reads it directly, but the helper
scripts need the same numbers, so this module owns the parsing and the
fallbacks: a missing file, a non-object, or a value that is not a positive
integer degrades to the documented default instead of stopping a batch.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_FILENAME = "grading.json"
DEFAULT_TEAM_BATCH_SIZE = 8
DEFAULT_MAX_AGENT_RESUMES = 4


@dataclass(frozen=True)
class GradingConfig:
    """The batch size and the per-team resume budget."""

    team_batch_size: int = DEFAULT_TEAM_BATCH_SIZE
    max_agent_resumes: int = DEFAULT_MAX_AGENT_RESUMES

    @property
    def line(self) -> str:
        return (
            f"grading: team_batch_size={self.team_batch_size}, "
            f"max_agent_resumes={self.max_agent_resumes}"
        )


def _positive_int(value: object, default: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return default
    return value


def parse_grading_config(payload: object) -> GradingConfig:
    """Build the config from decoded JSON, falling back per field."""
    if not isinstance(payload, dict):
        return GradingConfig()
    return GradingConfig(
        team_batch_size=_positive_int(payload.get("team_batch_size"), DEFAULT_TEAM_BATCH_SIZE),
        max_agent_resumes=_positive_int(payload.get("max_agent_resumes"), DEFAULT_MAX_AGENT_RESUMES),
    )


def load_grading_config(root: Path | None = None) -> GradingConfig:
    """Read `<root>/grading.json`, defaulting when it is missing or unreadable."""
    path = (ROOT if root is None else Path(root)) / CONFIG_FILENAME
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return GradingConfig()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return GradingConfig()
    return parse_grading_config(payload)
