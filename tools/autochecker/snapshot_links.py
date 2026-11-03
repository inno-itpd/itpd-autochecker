"""Check relative links and heading anchors in a fetched snapshot's Markdown.

GitHub renders a heading's anchor from a slug of its rendered text: the text is
lowercased, punctuation is dropped except hyphens and connector punctuation such
as ``_``, spaces become hyphens, and a duplicate slug gets a ``-1``, ``-2``, ...
suffix.  A raw HTML heading that carries an ``id`` attribute uses that id
verbatim.  This module implements those rules, resolves a relative link against
the file that contains it, and checks its fragment against the target file's
anchors.

Pre-cut research anchors (``#alt-NN-<title>``, ``#gap-NN-<title>``,
``#vp-NN-<title>``) are listed separately, because the A2 prompt greps for them
with ``#(alt|gap|vp)-[0-9]{2}-``.  ``--issue-bodies`` checks the anchors that a
dumped ``issues.json`` points at against the same snapshot headings.

``scripts/check_snapshot_links.py`` prints the summary; the exit code is 0 when
the check is clean, 1 when it has findings, and 2 when it cannot run.
"""

from __future__ import annotations

import html
import json
import os
import posixpath
import re
import unicodedata
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

ATX_HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
RAW_HTML_HEADING = re.compile(
    r"^ {0,3}<h(?P<level>[1-6])(?P<attrs>[^>]*)>(?P<text>.*?)(?:</h(?P=level)[ \t]*>)?[ \t]*$",
    re.IGNORECASE,
)
HTML_ID_ATTRIBUTE = re.compile(r"\bid[ \t]*=[ \t]*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))", re.IGNORECASE)
SETEXT_UNDERLINE = re.compile(r"^ {0,3}(?P<line>=+|-+)[ \t]*$")
SETEXT_TEXT_GUARD = re.compile(r"^ {0,3}(?:>|[-*+] |\d{1,9}[.)] |#|`{3,}|~{3,}|\|)")
FENCED_CODE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})")

INLINE_LINK = re.compile(
    r"!?\[[^\]]*\]\(\s*(?P<target><[^<>]*>|[^()\s]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
INLINE_CODE = re.compile(r"(`+)(.+?)\1")
BARE_URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")

PRECUT_ANCHOR = re.compile(r"#(?:alt|gap|vp)-[0-9]{2}-[^\s)\]\"'`,<>]*", re.IGNORECASE)
LINE_FRAGMENT = re.compile(r"L\d+(?:-L\d+)?")
URL_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
GITHUB_BLOB_URL = re.compile(
    r"^https?://(?:www\.)?github\.com/[^/\s]+/[^/\s]+/blob/(?P<rest>[^?#\s]+)",
    re.IGNORECASE,
)
URL_TRAILING_CHARS = ".,;:!?"

MD_CODE_SPAN = re.compile(r"`+([^`]*)`+")
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
MD_REF_LINK = re.compile(r"!?\[([^\]]*)\]\[[^\]]*\]")
MD_STRONG_STAR = re.compile(r"\*\*(.+?)\*\*")
MD_STRONG_UNDERSCORE = re.compile(r"(?<![A-Za-z0-9_])__(.+?)__(?![A-Za-z0-9_])")
MD_EM_STAR = re.compile(r"\*(.+?)\*")
MD_EM_UNDERSCORE = re.compile(r"(?<![A-Za-z0-9_])_(.+?)_(?![A-Za-z0-9_])")
MD_STRIKE = re.compile(r"~~(.+?)~~")
HTML_TAG = re.compile(r"<[^>]*>")

KIND_ORDER = {"broken-link": 0, "missing-anchor": 1, "precut-anchor": 2}


class SnapshotLinksError(RuntimeError):
    """The snapshot or the issue body dump is missing or unreadable."""


@dataclass(frozen=True)
class LinkFinding:
    kind: str
    path: str
    line: int | None
    target: str
    detail: str

    @property
    def location(self) -> str:
        return f"{self.path}:{self.line}" if self.line is not None else self.path


@dataclass(frozen=True)
class SnapshotLinksResult:
    snapshot_dir: Path
    markdown_files: int
    findings: tuple[LinkFinding, ...]
    issue_bodies_checked: int
    issue_anchor_targets: int
    summary_lines: tuple[str, ...]

    @property
    def broken_links(self) -> tuple[LinkFinding, ...]:
        return tuple(finding for finding in self.findings if finding.kind == "broken-link")

    @property
    def missing_anchors(self) -> tuple[LinkFinding, ...]:
        return tuple(finding for finding in self.findings if finding.kind == "missing-anchor")

    @property
    def precut_anchors(self) -> tuple[LinkFinding, ...]:
        return tuple(finding for finding in self.findings if finding.kind == "precut-anchor")

    @property
    def has_findings(self) -> bool:
        return bool(self.findings)


@dataclass(frozen=True)
class _Link:
    line: int
    target: str


@dataclass(frozen=True)
class _Occurrence:
    line: int
    target: str


@dataclass(frozen=True)
class _Heading:
    text: str
    explicit: str | None = None


@dataclass(frozen=True)
class _ParsedMarkdown:
    anchors: frozenset[str]
    links: tuple[_Link, ...]
    precut: tuple[_Occurrence, ...]


class _AnchorIndex:
    def __init__(self) -> None:
        self.slugs: set[str] = set()
        self._counts: dict[str, int] = {}

    def add_text(self, text: str) -> str:
        base = github_slug(text)
        count = self._counts.get(base, 0)
        self._counts[base] = count + 1
        slug = base if count == 0 else f"{base}-{count}"
        self.slugs.add(slug)
        return slug

    def add_explicit(self, anchor: str) -> None:
        self.slugs.add(anchor)


def github_slug(text: str) -> str:
    """Return the GitHub heading anchor for a heading's raw Markdown text."""
    plain = _plain_heading_text(text)
    kept = [character if _is_anchor_character(character) else "" for character in plain.lower()]
    return "".join(kept).replace(" ", "-")


def _plain_heading_text(text: str) -> str:
    text = MD_CODE_SPAN.sub(r"\1", text)
    text = MD_IMAGE.sub(r"\1", text)
    text = MD_LINK.sub(r"\1", text)
    text = MD_REF_LINK.sub(r"\1", text)
    text = MD_STRONG_STAR.sub(r"\1", text)
    text = MD_STRONG_UNDERSCORE.sub(r"\1", text)
    text = MD_EM_STAR.sub(r"\1", text)
    text = MD_EM_UNDERSCORE.sub(r"\1", text)
    text = MD_STRIKE.sub(r"\1", text)
    text = HTML_TAG.sub("", text)
    return html.unescape(text)


def _is_anchor_character(character: str) -> bool:
    if character in " -":
        return True
    category = unicodedata.category(character)
    return category[0] in "LMN" or category == "Pc"


def parse_markdown(text: str, *, bare_urls: bool = False) -> _ParsedMarkdown:
    lines = text.splitlines()
    fenced = _fenced_lines(lines)
    anchors = _AnchorIndex()
    links: list[_Link] = []
    precut: list[_Occurrence] = []
    heading_lines: set[int] = set()
    for index, line in enumerate(lines):
        number = index + 1
        precut.extend(_precut_occurrences(line, number))
        if fenced[index]:
            continue
        heading = _heading_at(lines, index, heading_lines, fenced)
        if heading is not None:
            heading_lines.add(index)
            if heading.explicit is not None:
                anchors.add_explicit(heading.explicit)
            else:
                anchors.add_text(heading.text)
        code_masked = INLINE_CODE.sub(lambda match: " " * len(match.group(0)), line)
        matches = list(INLINE_LINK.finditer(code_masked))
        seen_targets = {match.group("target") for match in matches}
        links.extend(_Link(number, match.group("target")) for match in matches)
        if bare_urls:
            for match in BARE_URL.finditer(code_masked):
                target = _clean_bare_url(match.group(0))
                if target and target not in seen_targets:
                    seen_targets.add(target)
                    links.append(_Link(number, target))
    return _ParsedMarkdown(frozenset(anchors.slugs), tuple(links), tuple(precut))


def _fenced_lines(lines: Sequence[str]) -> list[bool]:
    inside: list[bool] = []
    fence_character = ""
    fence_length = 0
    for line in lines:
        if fence_character:
            inside.append(True)
            stripped = line.strip()
            if (
                stripped
                and len(set(stripped)) == 1
                and stripped[0] == fence_character
                and len(stripped) >= fence_length
            ):
                fence_character = ""
            continue
        match = FENCED_CODE_OPEN.match(line)
        if match:
            fence_character = match.group(1)[0]
            fence_length = len(match.group(1))
            inside.append(True)
        else:
            inside.append(False)
    return inside


def _heading_at(
    lines: Sequence[str],
    index: int,
    heading_lines: set[int],
    fenced: Sequence[bool],
) -> _Heading | None:
    atx = ATX_HEADING.match(lines[index])
    if atx:
        return _Heading(text=atx.group(2) or "")
    raw = RAW_HTML_HEADING.match(lines[index])
    if raw:
        id_match = HTML_ID_ATTRIBUTE.search(raw.group("attrs"))
        if id_match:
            explicit = next(group for group in id_match.groups() if group is not None)
            return _Heading(text="", explicit=explicit)
        return _Heading(text=raw.group("text"))
    if index == 0 or fenced[index - 1] or index - 1 in heading_lines:
        return None
    underline = SETEXT_UNDERLINE.match(lines[index])
    previous = lines[index - 1].strip()
    if (
        underline
        and len(underline.group("line")) >= 2
        and previous
        and not SETEXT_TEXT_GUARD.match(lines[index - 1])
    ):
        return _Heading(text=previous)
    return None


def _precut_occurrences(line: str, number: int) -> list[_Occurrence]:
    return [_Occurrence(number, match.group(0)) for match in PRECUT_ANCHOR.finditer(line)]


def _clean_bare_url(url: str) -> str:
    return url.rstrip(URL_TRAILING_CHARS)


def iter_markdown_files(root: Path) -> Iterator[Path]:
    for directory, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(name for name in dirnames if name != ".git")
        for filename in sorted(filenames):
            if filename.casefold().endswith(".md"):
                path = Path(directory) / filename
                if path.is_file():
                    yield path


def load_issue_bodies(path: Path) -> list[tuple[int | None, str]]:
    if not path.is_file():
        raise SnapshotLinksError(f"missing issue body dump: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SnapshotLinksError(f"cannot parse {path}: {exc}") from exc
    if not isinstance(payload, list):
        raise SnapshotLinksError(f"{path} does not hold a JSON array of issues")
    bodies: list[tuple[int | None, str]] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        body = item.get("body")
        if not isinstance(body, str):
            continue
        number = item.get("number")
        bodies.append((number if isinstance(number, int) else None, body))
    return bodies


def check_snapshot_links(
    snapshot_dir: Path,
    *,
    issue_bodies_path: Path | None = None,
) -> SnapshotLinksResult:
    root = Path(snapshot_dir)
    if not root.is_dir():
        raise SnapshotLinksError(f"missing snapshot directory: {snapshot_dir}")

    parsed: dict[str, _ParsedMarkdown] = {}
    for path in iter_markdown_files(root):
        relative = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            raise SnapshotLinksError(f"cannot read {relative}: {exc}") from exc
        parsed[relative] = parse_markdown(text)

    findings: list[LinkFinding] = []
    for relative, scan in parsed.items():
        for link in scan.links:
            finding = _check_snapshot_link(root, relative, scan, parsed, link)
            if finding is not None:
                findings.append(finding)
        findings.extend(
            LinkFinding("precut-anchor", relative, occurrence.line, occurrence.target, "pre-cut anchor")
            for occurrence in scan.precut
        )

    issue_bodies_checked = 0
    issue_anchor_targets = 0
    if issue_bodies_path is not None:
        issue_findings, issue_bodies_checked, issue_anchor_targets = _check_issue_bodies(
            root, issue_bodies_path, parsed
        )
        findings.extend(issue_findings)

    findings.sort(key=lambda finding: (KIND_ORDER[finding.kind], finding.path, finding.line or 0, finding.target))
    ordered = tuple(findings)
    summary = _summary_lines(
        root=root,
        markdown_files=len(parsed),
        findings=ordered,
        issue_bodies_checked=issue_bodies_checked,
        issue_anchor_targets=issue_anchor_targets,
        has_issue_bodies=issue_bodies_path is not None,
    )
    return SnapshotLinksResult(
        snapshot_dir=root,
        markdown_files=len(parsed),
        findings=ordered,
        issue_bodies_checked=issue_bodies_checked,
        issue_anchor_targets=issue_anchor_targets,
        summary_lines=tuple(summary),
    )


def _check_snapshot_link(
    root: Path,
    relative: str,
    scan: _ParsedMarkdown,
    parsed: dict[str, _ParsedMarkdown],
    link: _Link,
) -> LinkFinding | None:
    path_part, fragment = _split_target(link.target)
    if _is_external(path_part) or (not path_part and fragment is None):
        return None
    if path_part:
        resolved = _resolve_path(root, relative, path_part)
        if resolved is None:
            return LinkFinding("broken-link", relative, link.line, link.target, "target is outside the snapshot")
        if not resolved.exists():
            return LinkFinding("broken-link", relative, link.line, link.target, "missing file")
        if fragment is None or _is_line_fragment(fragment):
            return None
        if not resolved.is_file() or resolved.suffix.casefold() != ".md":
            return LinkFinding("missing-anchor", relative, link.line, link.target, "target has no Markdown headings")
        target_relative = resolved.relative_to(root).as_posix()
        anchors = parsed[target_relative].anchors if target_relative in parsed else frozenset()
    else:
        if fragment is None or _is_line_fragment(fragment):
            return None
        anchors = scan.anchors
    if fragment in anchors:
        return None
    return LinkFinding("missing-anchor", relative, link.line, link.target, "no such heading")


def _check_issue_bodies(
    root: Path,
    issue_bodies_path: Path,
    parsed: dict[str, _ParsedMarkdown],
) -> tuple[list[LinkFinding], int, int]:
    bodies = load_issue_bodies(issue_bodies_path)
    display = issue_bodies_path.as_posix()
    findings: list[LinkFinding] = []
    anchor_targets = 0
    for number, body in bodies:
        label = f"{display} #{number}" if number is not None else display
        scan = parse_markdown(body, bare_urls=True)
        findings.extend(
            LinkFinding("precut-anchor", label, occurrence.line, occurrence.target, "pre-cut anchor")
            for occurrence in scan.precut
        )
        for link in scan.links:
            finding, anchor_checked = _check_issue_target(root, parsed, label, link)
            if anchor_checked:
                anchor_targets += 1
            if finding is not None:
                findings.append(finding)
    return findings, len(bodies), anchor_targets


def _check_issue_target(
    root: Path,
    parsed: dict[str, _ParsedMarkdown],
    label: str,
    link: _Link,
) -> tuple[LinkFinding | None, bool]:
    path_part, fragment = _split_target(link.target)
    blob = GITHUB_BLOB_URL.match(link.target.strip().strip("<>"))
    resolved: Path | None = None
    relative: str | None = None
    if blob:
        found = _longest_existing(root, blob.group("rest"))
        if found is not None:
            relative, resolved = found
    elif path_part and not _is_external(path_part):
        resolved = _resolve_path(root, None, path_part)
        if resolved is not None and resolved.exists():
            relative = resolved.relative_to(root).as_posix()
        else:
            resolved = None
    if resolved is None or relative is None or fragment is None or _is_line_fragment(fragment):
        return None, False
    if not resolved.is_file() or resolved.suffix.casefold() != ".md":
        return None, False
    anchors = parsed[relative].anchors if relative in parsed else frozenset()
    if fragment in anchors:
        return None, True
    return LinkFinding("missing-anchor", label, link.line, link.target, "no such heading"), True


def _longest_existing(root: Path, rest: str) -> tuple[str, Path] | None:
    parts = [unquote(part) for part in rest.split("/") if part]
    for start in range(1, len(parts)):
        relative = "/".join(parts[start:])
        candidate = root / relative
        if candidate.is_file():
            return relative, candidate
    return None


def _split_target(target: str) -> tuple[str, str | None]:
    value = target.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1].strip()
    path_part, separator, fragment = value.partition("#")
    path_part = path_part.partition("?")[0]
    decoded_path = unquote(path_part)
    decoded_fragment = unquote(fragment) if separator else None
    return decoded_path, decoded_fragment


def _is_external(path: str) -> bool:
    return bool(URL_SCHEME.match(path)) or path.startswith("//")


def _is_line_fragment(fragment: str) -> bool:
    return bool(LINE_FRAGMENT.fullmatch(fragment))


def _resolve_path(root: Path, source_relative: str | None, path: str) -> Path | None:
    if path.startswith("/"):
        combined = path.lstrip("/")
    elif source_relative is None:
        combined = path
    else:
        combined = posixpath.join(posixpath.dirname(source_relative), path)
    normalized = posixpath.normpath(combined)
    if normalized == ".." or normalized.startswith("../"):
        return None
    return root / normalized


def _summary_lines(
    *,
    root: Path,
    markdown_files: int,
    findings: tuple[LinkFinding, ...],
    issue_bodies_checked: int,
    issue_anchor_targets: int,
    has_issue_bodies: bool,
) -> list[str]:
    broken = [finding for finding in findings if finding.kind == "broken-link"]
    missing = [finding for finding in findings if finding.kind == "missing-anchor"]
    precut = [finding for finding in findings if finding.kind == "precut-anchor"]
    lines = [f"{root.as_posix()} (snapshot)", f"  markdown files: {markdown_files} scanned"]
    for label, group in (
        ("broken relative links", broken),
        ("missing anchors", missing),
        ("pre-cut anchors", precut),
    ):
        if not group:
            lines.append(f"  {label}: none")
            continue
        lines.append(f"  {label}: {len(group)}")
        lines.extend(f"    {finding.location}: {finding.target} ({finding.detail})" for finding in group)
    if has_issue_bodies:
        lines.append(
            f"  issue bodies: {issue_bodies_checked} checked, {issue_anchor_targets} anchor target(s)"
        )
    lines.append(f"  result: {len(findings)} finding(s)" if findings else "  result: no findings")
    return lines
