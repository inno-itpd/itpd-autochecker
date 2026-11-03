"""Validation of the optional semantic feedback companion file.

The format lives in `docs/semantic-feedback-format.md`.
This module parses one `agent-semantic-feedback.md` and checks its schema; it
does not judge the prose.  The checks are limited to what a script can settle:
the metadata, the dimension order, the verdict vocabulary, the required blocks,
the evidence links and their snapshot SHA, and the forbidden status and mentor
vocabulary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG

VERDICTS = ("adequate", "thin", "not yet adequate")
HELP_HEADINGS = {
    "adequate": "What would make it stronger",
    "thin": "What would make it adequate",
    "not yet adequate": "What would make it adequate",
}

TITLE_PATTERN = re.compile(r"^# Assignment (\d+) Semantic Feedback$")
TEAM_PATTERN = re.compile(r"^- Team: (\d+)$")
REPOSITORY_PATTERN = re.compile(r"^- Repository: `(https://github\.com/[^/`\s]+/[^/`\s]+)`$")
SNAPSHOT_PATTERN = re.compile(r"^- Snapshot: `([0-9a-f]{40})`$")
STRUCTURAL_PATTERN = re.compile(r"^- Structural report: \[`agent-feedback\.md`\]\(\./agent-feedback\.md\)$")
VERDICT_PATTERN = re.compile(r"^\*\*Verdict:\*\*\s*(.*)$")
BLOCK_PATTERNS = {
    "What works": re.compile(r"^\*\*What works\.\*\*\s*(.*)$"),
    "What breaks first": re.compile(r"^\*\*What breaks first\.\*\*\s*(.*)$"),
    "What would make it adequate": re.compile(r"^\*\*What would make it adequate\.\*\*\s*(.*)$"),
    "What would make it stronger": re.compile(r"^\*\*What would make it stronger\.\*\*\s*(.*)$"),
    "Evidence": re.compile(r"^\*\*Evidence:\*\*\s*$"),
}
SECTION_PATTERN = re.compile(r"^## (.+?)\s*$")
BULLET_PATTERN = re.compile(r"^- (.*)$")
NESTED_BULLET_PATTERN = re.compile(r"^\s+- ")
MARKDOWN_URL_PATTERN = re.compile(r"\]\((https?://[^)\s]+)\)")
BARE_URL_PATTERN = re.compile(r"https?://[^\s<>()]+")
BLOB_LINK_PATTERN = re.compile(
    r"https://github\.com/(?P<owner>[^/\s]+)/(?P<repo>[^/\s]+)/blob/(?P<ref>[^/\s]+)(?:/[^\s]*)?"
)
STATUS_WORDING = re.compile(r"\b(met|partial|missing|unverified)\b", re.IGNORECASE)
MENTOR_WORDING = re.compile(r"\bmentor", re.IGNORECASE)

REPORT_REPOSITORY_PATTERN = re.compile(
    r"^- Repository reviewed: `(https://github\.com/[^/`\s]+/[^/`\s]+)`$", re.MULTILINE
)
REPORT_SNAPSHOT_PATTERN = re.compile(r"^- Snapshot reviewed: `([0-9a-f]{40})`$", re.MULTILINE)
REPORT_TEAM_PATTERN = re.compile(r"^- Team: (\d+)$", re.MULTILINE)

HEADING_HOW_TO_READ = "How to read this"
HEADING_WHERE_TO_START = "Where to start"

MIN_DIMENSIONS = 3
MIN_WHERE_TO_START = 2
MAX_WHERE_TO_START = 3


class SemanticFeedbackError(ValueError):
    """Raised when the file cannot be parsed at all."""


@dataclass
class Dimension:
    name: str
    verdict: str = ""
    blocks: dict[str, list[str]] = field(default_factory=dict)
    block_order: list[str] = field(default_factory=list)

    @property
    def evidence(self) -> list[str]:
        return self.blocks.get("Evidence", [])

    def text(self, heading: str) -> str:
        return " ".join(self.blocks.get(heading, [])).strip()


@dataclass
class SemanticFeedback:
    assignment: str
    team: int
    repository: str
    snapshot: str
    how_to_read: str
    dimensions: list[Dimension]
    where_to_start: list[str]


def _split_sections(text: str) -> tuple[str, list[str], list[tuple[str, list[str]]]]:
    """Return the title, the preamble, and the `##` sections with their bodies."""
    lines = text.splitlines()
    title_index = next((index for index, line in enumerate(lines) if line.strip()), None)
    if title_index is None:
        raise SemanticFeedbackError("the file is empty")
    preamble: list[str] = []
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_body: list[str] = []
    for line in lines[title_index + 1 :]:
        match = SECTION_PATTERN.match(line)
        if match:
            if current_heading is not None:
                sections.append((current_heading, current_body))
            current_heading = match.group(1)
            current_body = []
            continue
        if current_heading is None:
            preamble.append(line)
        else:
            current_body.append(line)
    if current_heading is not None:
        sections.append((current_heading, current_body))
    return lines[title_index].strip(), preamble, sections


def _metadata(preamble: list[str]) -> tuple[int, str, str]:
    bullets = [line for line in preamble if line.strip()]
    if len(bullets) != 4:
        raise SemanticFeedbackError("the metadata must be exactly the four bullets after the title")
    team_match = TEAM_PATTERN.match(bullets[0])
    repository_match = REPOSITORY_PATTERN.match(bullets[1])
    snapshot_match = SNAPSHOT_PATTERN.match(bullets[2])
    if not (team_match and repository_match and snapshot_match and STRUCTURAL_PATTERN.match(bullets[3])):
        raise SemanticFeedbackError(
            "the metadata must be `- Team:`, `- Repository:`, `- Snapshot:`, and the relative "
            "`- Structural report:` bullet, in that order"
        )
    team = int(team_match.group(1))
    if team < 1:
        raise SemanticFeedbackError("`- Team:` must be a positive number")
    return team, repository_match.group(1), snapshot_match.group(1)


def _dimension(name: str, body: list[str]) -> Dimension:
    dimension = Dimension(name=name)
    current: str | None = None
    for line in body:
        if not line.strip():
            continue
        verdict_match = VERDICT_PATTERN.match(line)
        if verdict_match:
            current = "Verdict"
            dimension.block_order.append(current)
            dimension.verdict = verdict_match.group(1).strip()
            dimension.blocks[current] = []
            continue
        block_match = next(
            ((heading, pattern.match(line)) for heading, pattern in BLOCK_PATTERNS.items() if pattern.match(line)),
            None,
        )
        if block_match is not None:
            heading, match = block_match
            current = heading
            dimension.block_order.append(current)
            dimension.blocks[current] = []
            remainder = match.group(1).strip() if match.groups() else ""
            if remainder:
                dimension.blocks[current].append(remainder)
            continue
        if current is None:
            raise SemanticFeedbackError(f"`## {name}` starts with text before the `**Verdict:**` line")
        if current == "Evidence" and NESTED_BULLET_PATTERN.match(line):
            raise SemanticFeedbackError(f"`## {name}` must not contain nested evidence bullets")
        if current == "Evidence":
            dimension.blocks[current].append(line.rstrip())
        else:
            dimension.blocks[current].append(line.strip())
    return dimension


def parse_semantic_feedback(text: str, assignment: str) -> SemanticFeedback:
    """Parse one semantic feedback file, raising on a structural error."""
    title, preamble, sections = _split_sections(text)
    title_match = TITLE_PATTERN.match(title)
    if not title_match:
        raise SemanticFeedbackError("the title must be `# Assignment <N> Semantic Feedback`")
    if title_match.group(1) != assignment.lstrip("A"):
        raise SemanticFeedbackError(f"the title names Assignment {title_match.group(1)}, not {assignment}")
    team, repository, snapshot = _metadata(preamble)

    if not sections or sections[0][0] != HEADING_HOW_TO_READ:
        raise SemanticFeedbackError(f"the first section must be `## {HEADING_HOW_TO_READ}`")
    if sections[-1][0] != HEADING_WHERE_TO_START:
        raise SemanticFeedbackError(f"the last section must be `## {HEADING_WHERE_TO_START}`")

    how_to_read = " ".join(line.strip() for line in sections[0][1] if line.strip())
    dimensions = [_dimension(name, body) for name, body in sections[1:-1]]
    where_body = sections[-1][1]
    nested = [line for line in where_body if NESTED_BULLET_PATTERN.match(line)]
    if nested:
        raise SemanticFeedbackError(f"`## {HEADING_WHERE_TO_START}` must not contain nested bullets")
    where_to_start = [match.group(1).strip() for line in where_body if (match := BULLET_PATTERN.match(line))]

    return SemanticFeedback(
        assignment=assignment,
        team=team,
        repository=repository,
        snapshot=snapshot,
        how_to_read=how_to_read,
        dimensions=dimensions,
        where_to_start=where_to_start,
    )


def _dimension_names(assignment: str) -> list[str]:
    return list(ASSIGNMENT_CONFIG.get(assignment, {}).get("semantic_dimensions", []))


def _urls(text: str) -> list[str]:
    urls = [match.group(1).rstrip(".,;:") for match in MARKDOWN_URL_PATTERN.finditer(text)]
    if not urls:
        urls = [match.group(0).rstrip(".,;:") for match in BARE_URL_PATTERN.finditer(text)]
    return urls


def _validate_links(text: str, repository: str, snapshot: str, label: str, require: bool) -> list[str]:
    errors: list[str] = []
    urls = _urls(text)
    if not urls:
        return [f"{label} needs at least one link"] if require else []
    expected_slug = repository.removeprefix("https://github.com/")
    for url in urls:
        blob = BLOB_LINK_PATTERN.match(url)
        if blob is not None:
            if f"{blob.group('owner')}/{blob.group('repo')}" != expected_slug:
                errors.append(f"{label} links a blob in another repository: {url}")
            if blob.group("ref") != snapshot:
                errors.append(f"{label} cites `{blob.group('ref')}`; the snapshot is `{snapshot}`")
    return errors


def _validate_dimension(dimension: Dimension, expected_names: list[str]) -> list[str]:
    errors: list[str] = []
    if dimension.name not in expected_names:
        errors.append(f"unknown dimension `## {dimension.name}`; expected one of: {', '.join(expected_names)}")
    if dimension.verdict not in VERDICTS:
        errors.append(f"`## {dimension.name}` has verdict `{dimension.verdict}`; expected one of: {', '.join(VERDICTS)}")
        return errors
    required = ["Verdict", "What works", "What breaks first", HELP_HEADINGS[dimension.verdict], "Evidence"]
    for heading in required:
        if heading not in dimension.blocks:
            errors.append(f"`## {dimension.name}` is missing `**{heading}.**`")
    if dimension.block_order != required:
        errors.append(
            f"`## {dimension.name}` blocks must be `**Verdict:**`, `**What works.**`, `**What breaks first.**`, "
            f"`**{HELP_HEADINGS[dimension.verdict]}.**`, and `**Evidence:**`, in that order"
        )
    for heading in required[:-1]:
        if heading == "Verdict":
            continue
        if heading in dimension.blocks and not dimension.text(heading):
            errors.append(f"`## {dimension.name}` has an empty `**{heading}.**` block")
    if not dimension.evidence:
        errors.append(f"`## {dimension.name}` needs at least one `**Evidence:**` bullet")
    for bullet in dimension.evidence:
        if not bullet.startswith("- "):
            errors.append(f"`## {dimension.name}` evidence must be a single-level bullet list")
            break
    return errors


def validate_semantic_feedback(
    text: str,
    assignment: str,
    report_text: str | None = None,
) -> list[str]:
    """Return every error in one semantic feedback file, or an empty list."""
    try:
        feedback = parse_semantic_feedback(text, assignment)
    except SemanticFeedbackError as exc:
        return [str(exc)]

    errors: list[str] = []
    expected_names = _dimension_names(assignment)
    if not expected_names:
        return [f"{assignment} defines no semantic dimensions in `tools/grader_tools/assignment_config.py`"]

    if not feedback.how_to_read:
        errors.append(f"`## {HEADING_HOW_TO_READ}` must carry a short paragraph")
    if not MIN_DIMENSIONS <= len(feedback.dimensions) <= len(expected_names):
        errors.append(f"the file must carry between {MIN_DIMENSIONS} and {len(expected_names)} dimension sections")

    names = [dimension.name for dimension in feedback.dimensions]
    if len(names) != len(set(names)):
        errors.append("a dimension section appears twice")
    order = [expected_names.index(name) for name in names if name in expected_names]
    if order != sorted(order):
        errors.append("dimension sections must follow the assignment prompt's order")

    if not MIN_WHERE_TO_START <= len(feedback.where_to_start) <= MAX_WHERE_TO_START:
        errors.append(
            f"`## {HEADING_WHERE_TO_START}` must contain {MIN_WHERE_TO_START}-{MAX_WHERE_TO_START} bullets"
        )
    for bullet in feedback.where_to_start:
        if not bullet:
            errors.append(f"`## {HEADING_WHERE_TO_START}` must not contain an empty bullet")
        if bullet.strip().strip("`").lower() == "none":
            errors.append(f"`## {HEADING_WHERE_TO_START}` must not say `None`")

    for dimension in feedback.dimensions:
        errors.extend(_validate_dimension(dimension, expected_names))
        if dimension.verdict in VERDICTS:
            for heading in ("What works", "What breaks first", HELP_HEADINGS[dimension.verdict]):
                body = dimension.text(heading)
                if body:
                    errors.extend(
                        _validate_links(
                            body,
                            feedback.repository,
                            feedback.snapshot,
                            f"`## {dimension.name}` `**{heading}.**`",
                            require=False,
                        )
                    )
        for bullet in dimension.evidence:
            errors.extend(
                _validate_links(
                    bullet,
                    feedback.repository,
                    feedback.snapshot,
                    f"`## {dimension.name}` evidence",
                    require=True,
                )
            )

    if STATUS_WORDING.search(text):
        errors.append("the file must not use status vocabulary (`met`, `partial`, `missing`, `unverified`)")
    if MENTOR_WORDING.search(text):
        errors.append('the file must not use "mentor" wording')

    if report_text is not None:
        team_match = REPORT_TEAM_PATTERN.search(report_text)
        repository_match = REPORT_REPOSITORY_PATTERN.search(report_text)
        snapshot_match = REPORT_SNAPSHOT_PATTERN.search(report_text)
        if team_match is None or repository_match is None or snapshot_match is None:
            errors.append("the structural report does not carry a readable Team, Repository, and Snapshot preamble")
        else:
            if int(team_match.group(1)) != feedback.team:
                errors.append("`- Team:` does not match `agent-feedback.md`")
            if repository_match.group(1) != feedback.repository:
                errors.append("`- Repository:` does not match `agent-feedback.md`")
            if snapshot_match.group(1) != feedback.snapshot:
                errors.append("`- Snapshot:` does not match `agent-feedback.md`")
    return errors


def default_report_path(path: Path) -> Path:
    """Return the structural report that must sit beside the semantic file."""
    return path.parent / "agent-feedback.md"
