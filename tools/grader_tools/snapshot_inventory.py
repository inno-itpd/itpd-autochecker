"""Write a bounded digest of a fetched snapshot into a team work directory.

A grader that explores a snapshot with broad searches spends its run on the tree
instead of on the judgment, and a provider failure then costs the whole review.
This module writes the tree once, as a short Markdown digest, so the grader reads
one bounded file instead of walking directories: the root files, the counts that
decide an assignment's segment minima, the ``docs/`` and ``reports/`` trees, the
workflow names, and the site-config candidates.

Every listing is sorted and capped, so the digest is deterministic and its size
does not depend on the repository.  ``scripts/snapshot_inventory.py`` prints the
counts and the path only, the same contract the other helper scripts follow.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tools.grader_tools.assignment_config import FEEDBACK_ROOT

INVENTORY_FILENAME = "inventory.md"
SNAPSHOT_DIRNAME = "snapshot"
WORK_DIRNAME = "work"

ROOT_FILE_LIMIT = 40
COUNT_NAME_LIMIT = 10
TREE_DEPTH = 2
DOCS_LIMIT = 60
REPORTS_LIMIT = 40
WORKFLOW_LIMIT = 20
SITE_LIMIT = 10

QR_DIR = "docs/quality-requirements/qr"
FR_DIR = "docs/functional-requirements/fr"
ADR_DIR = "docs/architecture/adr"
SITE_CONFIG_NAMES = (
    "book.toml",
    "docusaurus.config.js",
    "mkdocs.yml",
    "mkdocs.yaml",
    "zensical.toml",
)


class SnapshotInventoryError(Exception):
    """Raised when the snapshot cannot be read or the work directory cannot be written."""


@dataclass(frozen=True)
class Inventory:
    """One written digest and the counts the grader needs beside it."""

    path: Path
    line_count: int
    counts: dict[str, int]

    @property
    def summary_lines(self) -> tuple[str, ...]:
        counts = ", ".join(f"{name} {value}" for name, value in self.counts.items())
        return (
            f"inventory: {self.path} ({self.line_count} lines)",
            f"counts: {counts}",
            "result: ok",
        )


def team_work_dir(root: Path, assignment: str, team_dir: str) -> Path:
    """Return ``<root>/itpd-assignments-feedback/<assignment>/work/<team_dir>``."""
    return Path(root) / FEEDBACK_ROOT / assignment / WORK_DIRNAME / team_dir


def _numbered_files(directory: Path, prefix: str) -> list[str]:
    """Return the sorted ``<prefix>*.md`` file names in a directory, hidden ones skipped."""
    if not directory.is_dir():
        return []
    try:
        entries = sorted(directory.iterdir(), key=lambda path: path.name.lower())
    except OSError:
        return []
    return [
        entry.name
        for entry in entries
        if entry.is_file() and not entry.name.startswith(".") and entry.name.upper().startswith(prefix)
    ]


def _tree_lines(base: Path, relative_root: str, *, depth: int, limit: int) -> list[str]:
    """Return the sorted relative paths under ``relative_root``, capped at ``limit``.

    Directories end with ``/`` so a reader can tell them from files, and every
    entry whose name starts with a dot is skipped, so a fetched snapshot's
    ``.git`` never enters the digest.
    """
    root = base / relative_root
    if not root.is_dir():
        return []
    lines: list[str] = []

    def walk(directory: Path, level: int) -> None:
        if level > depth or len(lines) >= limit:
            return
        try:
            entries = sorted(directory.iterdir(), key=lambda path: (not path.is_dir(), path.name.lower()))
        except OSError:
            return
        for entry in entries:
            if len(lines) >= limit:
                return
            if entry.name.startswith("."):
                continue
            relative = entry.relative_to(base).as_posix()
            lines.append(f"{relative}/" if entry.is_dir() else relative)
            if entry.is_dir():
                walk(entry, level + 1)

    walk(root, 0)
    return lines


def _root_files(base: Path) -> list[str]:
    """Return the root entries, directories marked with a trailing slash."""
    try:
        entries = sorted(base.iterdir(), key=lambda path: (not path.is_dir(), path.name.lower()))
    except OSError as exc:
        raise SnapshotInventoryError(f"cannot read the snapshot directory {base}: {exc}") from exc
    lines = [f"{entry.name}/" if entry.is_dir() else entry.name for entry in entries]
    return lines[:ROOT_FILE_LIMIT]


def _site_configs(base: Path) -> list[str]:
    """Return the site-generator config files the snapshot carries at its root."""
    return [name for name in SITE_CONFIG_NAMES if (base / name).is_file()]


def build_inventory(snapshot_dir: Path) -> tuple[tuple[str, ...], dict[str, int]]:
    """Build the digest lines and the artifact counts for one fetched snapshot."""
    snapshot_dir = Path(snapshot_dir)
    if not snapshot_dir.is_dir():
        raise SnapshotInventoryError(f"no snapshot directory at {snapshot_dir}")

    qr_files = _numbered_files(snapshot_dir / QR_DIR, "QR-")
    fr_files = _numbered_files(snapshot_dir / FR_DIR, "FR-")
    adr_files = _numbered_files(snapshot_dir / ADR_DIR, "ADR-")
    counts = {"QR": len(qr_files), "FR": len(fr_files), "ADR": len(adr_files)}

    lines: list[str] = [
        "# Snapshot inventory",
        "",
        "Generated by `scripts/snapshot_inventory.py`. Paths are relative to the snapshot root.",
        "Long listings are capped; use rg or the file-reading tools for the contents.",
        "",
        "## Root files",
        "",
    ]
    lines.extend(f"- {name}" for name in _root_files(snapshot_dir))
    lines.extend(["", "## Counts that decide segment minima", ""])
    for label, names, prefix in (
        ("QR-nn files", qr_files, QR_DIR),
        ("FR-nnn files", fr_files, FR_DIR),
        ("ADR-nnn files", adr_files, ADR_DIR),
    ):
        lines.append(f"- {label}: {len(names)}")
        lines.extend(f"  - {prefix}/{name}" for name in names[:COUNT_NAME_LIMIT])
        if len(names) > COUNT_NAME_LIMIT:
            lines.append(f"  - (+{len(names) - COUNT_NAME_LIMIT} more)")
    lines.extend(["", "## docs/ tree", ""])
    lines.extend(f"- {line}" for line in _tree_lines(snapshot_dir, "docs", depth=TREE_DEPTH, limit=DOCS_LIMIT))
    lines.extend(["", "## reports/ tree", ""])
    lines.extend(
        f"- {line}" for line in _tree_lines(snapshot_dir, "reports", depth=TREE_DEPTH, limit=REPORTS_LIMIT)
    )
    lines.extend(["", "## .github/workflows", ""])
    workflow_lines = _tree_lines(snapshot_dir, ".github/workflows", depth=1, limit=WORKFLOW_LIMIT)
    lines.extend(f"- {line}" for line in workflow_lines)
    if not workflow_lines:
        lines.append("- none")
    lines.extend(["", "## Site config candidates", ""])
    site_configs = _site_configs(snapshot_dir)
    lines.extend(f"- {name}" for name in site_configs)
    if not site_configs:
        lines.append("- none")
    return tuple(lines), counts


def write_inventory(
    root: Path,
    assignment: str,
    team_dir: str,
    *,
    snapshot_dir: Path | None = None,
    output_path: Path | None = None,
) -> Inventory:
    """Write ``<work>/inventory.md`` for one team and return the counts beside it."""
    work_dir = team_work_dir(root, assignment, team_dir)
    if output_path is None:
        output_path = work_dir / INVENTORY_FILENAME
    if snapshot_dir is None:
        snapshot_dir = work_dir / SNAPSHOT_DIRNAME
    lines, counts = build_inventory(Path(snapshot_dir))
    output_path = Path(output_path)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError as exc:
        raise SnapshotInventoryError(f"cannot write {output_path}: {exc}") from exc
    return Inventory(path=output_path, line_count=len(lines), counts=counts)
