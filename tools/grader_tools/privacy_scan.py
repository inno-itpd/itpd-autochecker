"""Scan a fetched snapshot or a finished feedback report for private-only material.

The rules follow the course's sensitive-information reference: personal email
addresses, phone numbers, ``.env`` and key files, recording links, and the
member name tokens from the PDF table.  Recording links are only reported
outside meeting artifacts, because the meeting segment owns personal data
inside them.

``scripts/scan_privacy.py`` prints one line per file with a hit count, grouped
by rule, plus per-rule hit and file totals; matched values never reach stdout.
Inline ``data:...;base64,`` payloads are stripped before matching, including
payloads that wrap across lines, and a digit run right after a decimal point
is not reported as a phone number.  The scanner reads
``itpd-assignments-feedback/<assignment>/work/<team_dir>/pdf-info.json``
(written by ``scripts/fetch_team_snapshot.py``) for the snapshot directory, the
recording link, the GitHub usernames, and the member name and email tokens.
With ``no_snapshot`` it instead derives those tokens from the submission PDF,
so a feedback report can still be scanned after ``work/<team_dir>/`` is cleaned.
"""

from __future__ import annotations

import json
import os
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT
from tools.grader_tools.submission_pdf import (
    PDF_INFO_FILENAME,
    SNAPSHOT_DIRNAME,
    SubmissionPdfError,
    select_submission_pdf,
)

BINARY_SNIFF_BYTES = 8192
MAX_TEXT_BYTES = 5 * 1024 * 1024
MIN_NAME_TOKEN_LENGTH = 4

BASE64_PAYLOAD_PATTERN = re.compile(r"data:[^\s,]*?;base64,[A-Za-z0-9+/=\s]*", re.IGNORECASE)

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
IGNORED_EMAIL_DOMAINS = frozenset(
    {
        "example.com",
        "example.org",
        "example.net",
        "example.edu",
        "localhost",
        "github.com",
        "users.noreply.github.com",
    }
)
IGNORED_EMAIL_DOMAIN_SUFFIXES = (".example",)

# A dot before a digit-leading pattern marks a decimal coordinate, as in an
# Excalidraw ``translate(663.83071091152 147.375)``, not a phone number.
PHONE_PATTERNS = (
    re.compile(r"(?<![\w])\+[0-9]{1,3}(?:[\s.\-]?\([0-9]{2,4}\))?(?:[\s.\-]?[0-9]{2,4}){2,4}(?![\w])"),
    re.compile(r"(?<![\w])\([0-9]{3,5}\)(?:[\s.\-]?[0-9]{2,4}){1,3}(?![\w])"),
    re.compile(
        r"(?<![\w.])[78][\s.\-]?\(?[0-9]{3}\)?[\s.\-]?[0-9]{3}[\s.\-]?[0-9]{2}[\s.\-]?[0-9]{2}(?![\w])"
    ),
)
MIN_PHONE_DIGITS = 10
MAX_PHONE_DIGITS = 15

ENV_FILE_PATTERN = re.compile(r"^\.env(?:\.[A-Za-z0-9_-]+)*$")
ENV_EXAMPLE_PREFIXES = (".env.example", ".env.sample", ".env.template", ".env.dist")
KEY_FILE_NAMES = frozenset({"id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", "id_ecdsa_sk", "id_ed25519_sk"})
KEY_FILE_SUFFIXES = (".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".ppk", ".p8")

URL_PATTERN = re.compile(r"https?://[^\s\"'<>()\[\]]+")
URL_TRAILING_CHARS = ".,;:!?"
RECORDING_HOST_SUFFIXES = (
    "zoom.us",
    "telemost.yandex.ru",
    "telemost.yandex.com",
    "drive.google.com",
    "disk.yandex.ru",
    "disk.yandex.com",
    "yadi.sk",
    "youtube.com",
    "youtu.be",
    "vkvideo.ru",
)

MEETING_COMPONENT_PATTERN = re.compile(r"(?:^|[-_.])(?:meeting|meetings|kickoff)(?:[-_.]|$)", re.IGNORECASE)

PRIVACY_RULES: tuple[tuple[str, str], ...] = (
    ("email", "email address"),
    ("phone", "phone number"),
    ("secret-file", "env and key files"),
    ("recording", "recording link"),
    ("member-name", "member name token"),
)


class PrivacyScanError(RuntimeError):
    """The work-directory metadata or the scan target is missing or unreadable."""


@dataclass(frozen=True)
class PrivacyTokens:
    name_tokens: tuple[str, ...]
    email_tokens: tuple[str, ...]
    github_usernames: tuple[str, ...]
    recording_link: str | None
    snapshot_dir: str | None
    snapshot_fetched: bool | None


@dataclass(frozen=True)
class Finding:
    """One rule's hits in one file, with the hit count and matched line numbers."""

    rule: str
    kind: str
    path: str
    count: int = 1
    lines: tuple[int, ...] = ()


@dataclass(frozen=True)
class PrivacyScanResult:
    assignment: str
    team_dir: str
    target: str
    mode: str
    name_token_count: int
    email_token_count: int
    findings: tuple[Finding, ...]
    scanned_files: int
    skipped_binary: int
    skipped_large: int
    skipped_symlinks: int
    ignored_short_name_tokens: int
    skipped_name_matches: int
    summary_lines: tuple[str, ...]

    @property
    def has_findings(self) -> bool:
        return bool(self.findings)


@dataclass
class _Counts:
    scanned: int = 0
    binary: int = 0
    large: int = 0
    symlinks: int = 0
    unreadable: int = 0
    skipped_name_matches: int = 0


def load_privacy_tokens(path: Path) -> PrivacyTokens:
    if not path.is_file():
        raise PrivacyScanError(
            f"missing {path}; run scripts/fetch_team_snapshot.py <assignment> <team_dir> first"
        )
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PrivacyScanError(f"cannot parse {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise PrivacyScanError(f"{path} does not hold a JSON object")
    raw_tokens = payload.get("privacy_tokens")
    tokens = raw_tokens if isinstance(raw_tokens, dict) else {}
    recording_link = payload.get("recording_link")
    snapshot_dir = payload.get("snapshot_dir")
    snapshot_fetched = payload.get("snapshot_fetched")
    return PrivacyTokens(
        name_tokens=_token_tuple(tokens.get("name_tokens")),
        email_tokens=_token_tuple(tokens.get("email_tokens")),
        github_usernames=_token_tuple(payload.get("github_usernames")),
        recording_link=recording_link if isinstance(recording_link, str) and recording_link else None,
        snapshot_dir=snapshot_dir if isinstance(snapshot_dir, str) and snapshot_dir else None,
        snapshot_fetched=snapshot_fetched if isinstance(snapshot_fetched, bool) else None,
    )


def load_submission_privacy_tokens(assignment: str, team_dir: str, root: Path = Path(".")) -> PrivacyTokens:
    """Derive the privacy tokens from the submission PDF instead of pdf-info.json.

    ``--no-snapshot`` uses this after ``work/<team_dir>/`` is cleaned; it reads
    the same member table, recording link, and email tokens that
    ``scripts/fetch_team_snapshot.py`` writes to pdf-info.json.
    """
    config = ASSIGNMENT_CONFIG[assignment]
    submission_dir = root / FEEDBACK_ROOT / assignment / "submissions" / team_dir
    if not submission_dir.is_dir():
        raise PrivacyScanError(
            f"missing submission directory {submission_dir}; --no-snapshot needs the submission PDF "
            f"under {FEEDBACK_ROOT}/{assignment}/submissions/{team_dir}/"
        )
    try:
        metadata = select_submission_pdf(submission_dir, str(config["primary_index"]))
    except (SubmissionPdfError, OSError) as exc:
        raise PrivacyScanError(f"cannot read the submission PDF in {submission_dir}: {exc}") from exc
    return PrivacyTokens(
        name_tokens=tuple(sorted({token for member in metadata.members for token in member.name_tokens})),
        email_tokens=tuple(sorted(set(metadata.email_tokens))),
        github_usernames=tuple(sorted({member.github_username for member in metadata.members})),
        recording_link=metadata.recording_link,
        snapshot_dir=None,
        snapshot_fetched=None,
    )


def _token_tuple(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    return tuple(sorted({str(token).casefold() for token in value if isinstance(token, str) and token}))


def build_name_pattern(tokens: Iterable[str]) -> re.Pattern[str] | None:
    """Match name tokens of at least four characters as whole words.

    Shorter fragments match too much ordinary prose (``max`` inside
    ``max-smirnov`` or a three-letter prefix), so they are ignored entirely.
    """
    ordered = sorted(
        {token.casefold() for token in tokens if len(token.casefold()) >= MIN_NAME_TOKEN_LENGTH},
        key=len,
        reverse=True,
    )
    if not ordered:
        return None
    alternatives = "|".join(re.escape(token) for token in ordered)
    return re.compile(rf"(?<!\w)(?:{alternatives})(?!\w)", re.IGNORECASE)


def build_username_pattern(usernames: Iterable[str]) -> re.Pattern[str] | None:
    """Match known GitHub usernames case-insensitively, for fragment skips."""
    ordered = sorted({username.casefold() for username in usernames if username}, key=len, reverse=True)
    if not ordered:
        return None
    alternatives = "|".join(re.escape(username) for username in ordered)
    return re.compile(rf"(?:{alternatives})", re.IGNORECASE)


def count_ignored_short_name_tokens(tokens: Iterable[str]) -> int:
    return sum(1 for token in tokens if len(token.casefold()) < MIN_NAME_TOKEN_LENGTH)


def is_ignored_email(value: str, email_tokens: Iterable[str] = ()) -> bool:
    folded = value.casefold()
    if folded in email_tokens:
        return False
    domain = folded.rsplit("@", 1)[-1].rstrip(".")
    if domain in IGNORED_EMAIL_DOMAINS:
        return True
    return any(domain.endswith(suffix) for suffix in IGNORED_EMAIL_DOMAIN_SUFFIXES)


def is_phone_like(candidate: str) -> bool:
    digits = [character for character in candidate if character.isdigit()]
    return MIN_PHONE_DIGITS <= len(digits) <= MAX_PHONE_DIGITS


def classify_secret_file(relative_path: str) -> str | None:
    name = PurePosixPath(relative_path).name.casefold()
    if ENV_FILE_PATTERN.match(name) and not _is_env_example(name):
        return "env file"
    if name in KEY_FILE_NAMES or name.endswith(KEY_FILE_SUFFIXES):
        return "key file"
    return None


def _is_env_example(name: str) -> bool:
    return any(name == prefix or name.startswith(f"{prefix}.") for prefix in ENV_EXAMPLE_PREFIXES)


def clean_url(value: str) -> str:
    return value.rstrip(URL_TRAILING_CHARS)


def is_recording_url(url: str, recording_link: str | None = None) -> bool:
    candidate = clean_url(url)
    if recording_link and clean_url(recording_link) == candidate:
        return True
    parts = urlsplit(candidate)
    host = (parts.hostname or "").casefold()
    if not host:
        return False
    if host == "vk.com" and parts.path.startswith("/video"):
        return True
    return any(host == suffix or host.endswith(f".{suffix}") for suffix in RECORDING_HOST_SUFFIXES)


def is_meeting_artifact(relative_path: str) -> bool:
    return any(MEETING_COMPONENT_PATTERN.search(part) for part in PurePosixPath(relative_path).parts)


def iter_snapshot_files(scan_root: Path) -> Iterator[Path]:
    for directory, dirnames, filenames in os.walk(scan_root):
        dirnames[:] = sorted(name for name in dirnames if name != ".git")
        for filename in sorted(filenames):
            path = Path(directory) / filename
            if path.is_symlink() or path.is_file():
                yield path


@dataclass
class _FindingGroup:
    kind: str
    lines: list[int] = field(default_factory=list)
    line_set: set[int] = field(default_factory=set)
    file_hits: int = 0


class _Collector:
    """Group hits by ``(rule, path)`` so each file is reported once per rule."""

    def __init__(self) -> None:
        self._groups: dict[tuple[str, str], _FindingGroup] = {}

    def add(self, rule: str, kind: str, path: str, line: int | None = None) -> None:
        key = (rule, path)
        group = self._groups.get(key)
        if group is None:
            group = _FindingGroup(kind=kind)
            self._groups[key] = group
        if line is None:
            group.file_hits += 1
        elif line not in group.line_set:
            group.line_set.add(line)
            group.lines.append(line)

    def ordered(self) -> list[Finding]:
        rule_order = {rule: index for index, (rule, _) in enumerate(PRIVACY_RULES)}
        findings = [
            Finding(
                rule=rule,
                kind=group.kind,
                path=path,
                count=len(group.lines) + group.file_hits,
                lines=tuple(group.lines),
            )
            for (rule, path), group in self._groups.items()
        ]
        return sorted(findings, key=lambda finding: (rule_order[finding.rule], finding.path))


def scan_privacy(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
    *,
    feedback_path: Path | None = None,
    no_snapshot: bool = False,
) -> PrivacyScanResult:
    if assignment not in ASSIGNMENT_CONFIG:
        raise PrivacyScanError(f"unknown assignment: {assignment}")
    if no_snapshot and feedback_path is None:
        raise PrivacyScanError("no_snapshot requires a feedback report path; pass --feedback <path>")
    info_path = root / FEEDBACK_ROOT / assignment / "work" / team_dir / PDF_INFO_FILENAME
    tokens = (
        load_submission_privacy_tokens(assignment, team_dir, root)
        if no_snapshot
        else load_privacy_tokens(info_path)
    )
    collector = _Collector()
    counts = _Counts()
    scan_args = _ScanArgs(
        collector=collector,
        name_pattern=build_name_pattern(tokens.name_tokens),
        username_pattern=build_username_pattern(tokens.github_usernames),
        recording_link=tokens.recording_link,
        email_tokens=frozenset(tokens.email_tokens),
    )

    if feedback_path is not None:
        target_path = feedback_path if feedback_path.is_absolute() else root / feedback_path
        if not target_path.is_file():
            raise PrivacyScanError(f"missing feedback report: {feedback_path}")
        mode = "feedback"
        target = _display(target_path, root)
        _scan_file(target_path, target, is_meeting=False, counts=counts, args=scan_args)
    else:
        if tokens.snapshot_fetched is False:
            raise PrivacyScanError(
                f"{info_path} reports snapshot_fetched=false; repository-dependent checks are stopped, "
                "so the snapshot cannot be scanned (see docs/grader-policy.md#submission-and-snapshot-rules)"
            )
        snapshot_dir = tokens.snapshot_dir or f"{FEEDBACK_ROOT}/{assignment}/work/{team_dir}/{SNAPSHOT_DIRNAME}"
        scan_root = root / snapshot_dir
        if not scan_root.is_dir():
            raise PrivacyScanError(
                f"missing snapshot directory {snapshot_dir}; run scripts/fetch_team_snapshot.py "
                f"{assignment} {team_dir} first"
            )
        mode = "snapshot"
        target = _display(scan_root, root)
        for path in iter_snapshot_files(scan_root):
            if path.is_symlink():
                counts.symlinks += 1
                continue
            relative = path.relative_to(scan_root).as_posix()
            _scan_file(
                path,
                f"{target}/{relative}",
                is_meeting=is_meeting_artifact(relative),
                counts=counts,
                args=scan_args,
            )

    findings = tuple(collector.ordered())
    ignored_short_name_tokens = count_ignored_short_name_tokens(tokens.name_tokens)
    summary = _summary_lines(
        assignment=assignment,
        team_dir=team_dir,
        target=target,
        mode=mode,
        tokens=tokens,
        ignored_short_name_tokens=ignored_short_name_tokens,
        findings=findings,
        counts=counts,
    )
    return PrivacyScanResult(
        assignment=assignment,
        team_dir=team_dir,
        target=target,
        mode=mode,
        name_token_count=len(tokens.name_tokens),
        email_token_count=len(tokens.email_tokens),
        findings=findings,
        scanned_files=counts.scanned,
        skipped_binary=counts.binary,
        skipped_large=counts.large,
        skipped_symlinks=counts.symlinks,
        ignored_short_name_tokens=ignored_short_name_tokens,
        skipped_name_matches=counts.skipped_name_matches,
        summary_lines=tuple(summary),
    )


@dataclass(frozen=True)
class _ScanArgs:
    collector: _Collector
    name_pattern: re.Pattern[str] | None
    username_pattern: re.Pattern[str] | None
    recording_link: str | None
    email_tokens: frozenset[str]


def _scan_file(
    path: Path,
    display_path: str,
    *,
    is_meeting: bool,
    counts: _Counts,
    args: _ScanArgs,
) -> None:
    kind = classify_secret_file(display_path)
    if kind is not None:
        args.collector.add("secret-file", kind, display_path)
    try:
        size = path.stat().st_size
    except OSError:
        counts.unreadable += 1
        return
    if size > MAX_TEXT_BYTES:
        counts.large += 1
        return
    try:
        data = path.read_bytes()
    except OSError:
        counts.unreadable += 1
        return
    if b"\x00" in data[:BINARY_SNIFF_BYTES]:
        counts.binary += 1
        return
    counts.scanned += 1
    text = data.decode("utf-8", errors="replace")
    _scan_text(text, display_path, is_meeting, args, counts)


def strip_base64_payloads(text: str) -> str:
    """Blank inline ``data:...;base64,...`` payloads before any matching.

    The payload may wrap across lines.  Removed characters become spaces and
    existing newlines are kept, so reported line numbers still point at the
    original file.  The run stops at the first character outside the base64
    alphabet and whitespace, so text after the URI is still scanned.
    """
    return BASE64_PAYLOAD_PATTERN.sub(_blank_base64_payload, text)


def _blank_base64_payload(match: re.Match[str]) -> str:
    return "".join("\n" if character == "\n" else " " for character in match.group(0))


def _scan_text(text: str, path: str, is_meeting: bool, args: _ScanArgs, counts: _Counts) -> None:
    for line_number, line in enumerate(strip_base64_payloads(text).splitlines(), 1):
        for match in EMAIL_PATTERN.finditer(line):
            if not is_ignored_email(match.group(0), args.email_tokens):
                args.collector.add("email", "email address", path, line_number)
        for pattern in PHONE_PATTERNS:
            if any(is_phone_like(match.group(0)) for match in pattern.finditer(line)):
                args.collector.add("phone", "phone number", path, line_number)
                break
        if not is_meeting:
            for match in URL_PATTERN.finditer(line):
                if is_recording_url(match.group(0), args.recording_link):
                    args.collector.add("recording", "recording link", path, line_number)
        if args.name_pattern is not None:
            username_spans = _pattern_spans(args.username_pattern, line)
            reported = False
            for match in args.name_pattern.finditer(line):
                if _inside_spans(match.start(), match.end(), username_spans):
                    counts.skipped_name_matches += 1
                    continue
                reported = True
            if reported:
                args.collector.add("member-name", "member name token", path, line_number)


def _pattern_spans(pattern: re.Pattern[str] | None, line: str) -> tuple[tuple[int, int], ...]:
    if pattern is None:
        return ()
    return tuple((match.start(), match.end()) for match in pattern.finditer(line))


def _inside_spans(start: int, end: int, spans: tuple[tuple[int, int], ...]) -> bool:
    return any(span_start <= start and end <= span_end for span_start, span_end in spans)


def _summary_lines(
    *,
    assignment: str,
    team_dir: str,
    target: str,
    mode: str,
    tokens: PrivacyTokens,
    ignored_short_name_tokens: int,
    findings: tuple[Finding, ...],
    counts: _Counts,
) -> list[str]:
    lines = [
        f"{assignment} / {team_dir}",
        f"  target: {target} ({mode})",
        f"  privacy tokens: {len(tokens.name_tokens)} name token(s), {len(tokens.email_tokens)} email token(s)",
    ]
    if ignored_short_name_tokens:
        lines.append(
            f"  note: {ignored_short_name_tokens} name token(s) shorter than "
            f"{MIN_NAME_TOKEN_LENGTH} characters ignored"
        )
    if counts.skipped_name_matches:
        lines.append(
            f"  note: {counts.skipped_name_matches} name-token match(es) inside known GitHub username(s) skipped"
        )
    for rule, label in PRIVACY_RULES:
        rule_findings = [finding for finding in findings if finding.rule == rule]
        if not rule_findings:
            lines.append(f"  {label}: none")
            continue
        rule_hits = sum(finding.count for finding in rule_findings)
        lines.append(f"  {label}: {rule_hits} hit(s) in {len(rule_findings)} file(s)")
        for finding in rule_findings:
            lines.append(f"    {finding.path}: {finding.kind} (x{finding.count})")
    lines.append(
        f"  files: {counts.scanned} scanned, {counts.binary} binary skipped, "
        f"{counts.large} oversized skipped, {counts.symlinks} symlink(s) skipped, "
        f"{counts.unreadable} unreadable"
    )
    if findings:
        total_hits = sum(finding.count for finding in findings)
        file_count = len({finding.path for finding in findings})
        lines.append(
            f"  result: {len(findings)} finding(s), {total_hits} hit(s) in {file_count} file(s)"
        )
    else:
        lines.append("  result: no findings")
    return lines


def _display(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()
