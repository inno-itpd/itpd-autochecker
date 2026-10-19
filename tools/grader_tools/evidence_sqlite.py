"""Project the saved GitHub evidence dumps into a queryable SQLite database.

The collector writes ``issues.json``, ``prs.json``, ``labels.json``,
``milestones.json``, and, on request, ``issue-fields.json`` into one team work
directory.  Those dumps are large and their optional arrays are sometimes
``null``, so ad-hoc ``jq`` over them fails with ``Cannot iterate over null``.
This module writes ``evidence.sqlite`` beside them with the Python standard
library only, so a grader can answer the S6 and S7 questions with one SQL query.

``build_evidence_database`` works from already-parsed dumps and a target path,
so it is unit-testable without touching ``gh``.  ``write_evidence_database``
reads the saved dumps from a work directory and rebuilds the database; a missing
``issue-fields.json`` is not an error, and a null or absent array becomes zero
rows or a NULL value rather than an exception.
``live_evidence.collect_github_evidence`` calls it after writing the dumps and
again after ``--issue-fields``, and ``scripts/collect_github_evidence.py`` calls
it in ``--summary`` mode, which never calls ``gh``.

The ``issue_projection`` view joins the tables into one row per issue with
``number``, ``state``, ``title``, ``type``, ``milestone``, ``milestone_due_on``,
``labels``, ``assignees``, and ``closing_pull_requests``.  The multi-valued
columns are comma-separated and empty (never NULL) when the dump had no array.
States are lowercased so ``issues.json`` (``OPEN``) and ``issue-fields.json``
(``open``) answer the same query.  The database is rebuilt from scratch on every
write, so it never accumulates rows from an earlier collection.

``tests/test_evidence_sqlite.py`` holds ``ISSUE_DUMP_KEYS``, ``PR_DUMP_KEYS``,
and ``ISSUE_FIELDS_DUMP_KEYS`` equal to the collector's ``ISSUE_FIELDS``,
``PR_FIELDS``, and issue-fields projection keys, so the two files cannot drift.
"""

from __future__ import annotations

import json
import os
import sqlite3
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

EVIDENCE_DB_FILENAME = "evidence.sqlite"
ISSUES_FILENAME = "issues.json"
LABELS_FILENAME = "labels.json"
MILESTONES_FILENAME = "milestones.json"
PRS_FILENAME = "prs.json"
ISSUE_FIELDS_FILENAME = "issue-fields.json"
DUMP_FILENAMES = (
    LABELS_FILENAME,
    MILESTONES_FILENAME,
    ISSUES_FILENAME,
    PRS_FILENAME,
    ISSUE_FIELDS_FILENAME,
)

# These mirror the collector's field lists and the issue-fields projection; the
# tests compare them with live_evidence.ISSUE_FIELDS, PR_FIELDS, and
# project_issue_fields() output so a new dump key forces a schema decision here.
ISSUE_DUMP_KEYS = (
    "number",
    "title",
    "labels",
    "state",
    "stateReason",
    "createdAt",
    "closedAt",
    "body",
    "url",
    "author",
    "closedByPullRequestsReferences",
)
PR_DUMP_KEYS = (
    "number",
    "title",
    "author",
    "headRefName",
    "baseRefName",
    "state",
    "createdAt",
    "mergedAt",
    "closedAt",
    "body",
    "closingIssuesReferences",
    "reviews",
    "files",
    "url",
)
ISSUE_FIELDS_DUMP_KEYS = (
    "number",
    "state",
    "title",
    "type",
    "milestone",
    "assignees",
    "field_values",
)

SCHEMA_TABLES = (
    "issues",
    "labels",
    "issue_labels",
    "milestones",
    "issue_assignees",
    "issue_closing_references",
    "issue_field_values",
    "pull_requests",
    "pr_reviews",
    "pr_files",
    "pr_closing_references",
)

# Foreign keys are declared for readability but not enforced: a partial dump
# (for example a pull request whose issue is not in issues.json) still builds,
# because every INSERT here is null-safe and never aborts on a missing parent.
SCHEMA_SQL = """
CREATE TABLE issues (
    number INTEGER PRIMARY KEY,
    state TEXT,
    state_reason TEXT,
    title TEXT,
    body TEXT,
    url TEXT,
    author_login TEXT,
    created_at TEXT,
    closed_at TEXT,
    issue_type TEXT,
    milestone_title TEXT
);

CREATE TABLE labels (
    name TEXT PRIMARY KEY,
    description TEXT
);

CREATE TABLE issue_labels (
    issue_number INTEGER NOT NULL REFERENCES issues(number),
    label_name TEXT NOT NULL REFERENCES labels(name),
    PRIMARY KEY (issue_number, label_name)
);

CREATE TABLE milestones (
    title TEXT PRIMARY KEY,
    due_on TEXT,
    open_issues INTEGER NOT NULL DEFAULT 0,
    closed_issues INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE issue_assignees (
    issue_number INTEGER NOT NULL REFERENCES issues(number),
    login TEXT NOT NULL,
    PRIMARY KEY (issue_number, login)
);

CREATE TABLE issue_closing_references (
    issue_number INTEGER NOT NULL REFERENCES issues(number),
    pull_request_number INTEGER,
    repository TEXT,
    url TEXT
);

CREATE TABLE issue_field_values (
    issue_number INTEGER NOT NULL REFERENCES issues(number),
    name TEXT,
    data_type TEXT,
    value TEXT
);

CREATE TABLE pull_requests (
    number INTEGER PRIMARY KEY,
    title TEXT,
    state TEXT,
    author_login TEXT,
    head_ref_name TEXT,
    base_ref_name TEXT,
    created_at TEXT,
    merged_at TEXT,
    closed_at TEXT,
    url TEXT,
    body TEXT
);

CREATE TABLE pr_reviews (
    pull_request_number INTEGER NOT NULL REFERENCES pull_requests(number),
    author_login TEXT,
    state TEXT,
    submitted_at TEXT,
    body TEXT
);

CREATE TABLE pr_files (
    pull_request_number INTEGER NOT NULL REFERENCES pull_requests(number),
    path TEXT,
    change_type TEXT,
    additions INTEGER NOT NULL DEFAULT 0,
    deletions INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE pr_closing_references (
    pull_request_number INTEGER NOT NULL REFERENCES pull_requests(number),
    issue_number INTEGER,
    repository TEXT,
    url TEXT
);

CREATE VIEW issue_projection AS
SELECT
    i.number AS number,
    i.state AS state,
    i.title AS title,
    i.issue_type AS type,
    i.milestone_title AS milestone,
    m.due_on AS milestone_due_on,
    COALESCE(
        (
            SELECT group_concat(a.label_name, ', ')
            FROM issue_labels AS a
            WHERE a.issue_number = i.number
        ),
        ''
    ) AS labels,
    COALESCE(
        (
            SELECT group_concat(a.login, ', ')
            FROM issue_assignees AS a
            WHERE a.issue_number = i.number
        ),
        ''
    ) AS assignees,
    COALESCE(
        (
            SELECT group_concat(c.pull_request_number, ', ')
            FROM issue_closing_references AS c
            WHERE c.issue_number = i.number AND c.pull_request_number IS NOT NULL
        ),
        ''
    ) AS closing_pull_requests
FROM issues AS i
LEFT JOIN milestones AS m ON m.title = i.milestone_title;
"""


class EvidenceDatabaseError(RuntimeError):
    """A saved dump cannot be read, or the database cannot be written."""


@dataclass(frozen=True)
class EvidenceDatabase:
    """The written database and its row counts, for the collector's summary."""

    path: Path
    counts: dict[str, int]

    def summary_line(self, root: Path | None = None) -> str:
        """One collector output line, with the path relative to ``root`` when it is under it."""
        display = self.path.as_posix()
        if root is not None:
            try:
                display = self.path.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                display = self.path.as_posix()
        return (
            f"  evidence.sqlite: {len(SCHEMA_TABLES)} tables, "
            f"{_count_label(self.counts['issues'], 'issue')}, "
            f"{_count_label(self.counts['pull_requests'], 'pull request')} -> {display}"
        )


def build_evidence_database(dumps: Mapping[str, object], path: Path) -> EvidenceDatabase:
    """Write ``path`` from already-parsed dumps, replacing any earlier database."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.unlink(missing_ok=True)
    connection = sqlite3.connect(temporary)
    try:
        connection.executescript(SCHEMA_SQL)
        _insert_labels(connection, _rows(dumps.get(LABELS_FILENAME)))
        _insert_milestones(connection, _rows(dumps.get(MILESTONES_FILENAME)))
        _insert_issues(connection, _rows(dumps.get(ISSUES_FILENAME)))
        _insert_issue_fields(connection, _rows(dumps.get(ISSUE_FIELDS_FILENAME)))
        _insert_pull_requests(connection, _rows(dumps.get(PRS_FILENAME)))
        connection.commit()
        counts = {table: _count(connection, table) for table in SCHEMA_TABLES}
    except (OSError, sqlite3.Error) as exc:
        connection.close()
        temporary.unlink(missing_ok=True)
        raise EvidenceDatabaseError(f"cannot build {path}: {exc}") from exc
    except BaseException:
        connection.close()
        temporary.unlink(missing_ok=True)
        raise
    connection.close()
    try:
        os.chmod(temporary, 0o600)
        temporary.replace(path)
    except OSError as exc:
        temporary.unlink(missing_ok=True)
        raise EvidenceDatabaseError(f"cannot write {path}: {exc}") from exc
    return EvidenceDatabase(path=path, counts=counts)


def write_evidence_database(work_dir: Path) -> EvidenceDatabase:
    """Rebuild ``<work_dir>/evidence.sqlite`` from the dumps saved there.

    A missing dump is an empty table: only ``issue-fields.json`` is optional in
    practice, but reading every dump the same way keeps a partial collection
    from raising.
    """
    work_dir = Path(work_dir)
    dumps = {filename: _load_dump(work_dir / filename) for filename in DUMP_FILENAMES}
    return build_evidence_database(dumps, work_dir / EVIDENCE_DB_FILENAME)


def _load_dump(path: Path) -> object | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise EvidenceDatabaseError(f"cannot parse {path}: {exc}") from exc
    except OSError as exc:
        raise EvidenceDatabaseError(f"cannot read {path}: {exc}") from exc


def _rows(value: object) -> list[Mapping[str, object]]:
    """Return the JSON objects of a dump array, with a null or absent array becoming ``[]``."""
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _text(value: object) -> str | None:
    if value is None:
        return None
    return value if isinstance(value, str) else str(value)


def _state(value: object) -> str | None:
    text = _text(value)
    return text.lower() if text is not None else None


def _number(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def _count_field(value: object) -> int:
    number = _number(value)
    return number if number is not None else 0


def _login(value: object) -> str | None:
    if isinstance(value, Mapping):
        return _text(value.get("login"))
    return value if isinstance(value, str) else None


def _logins(value: object) -> list[str]:
    """Return the logins of a user array, with a null or absent array becoming ``[]``.

    ``issue-fields.json`` stores plain login strings, while a raw REST issue
    stores ``{"login": ...}`` objects, so both shapes are accepted.
    """
    if not isinstance(value, list):
        return []
    logins: list[str] = []
    for item in value:
        login = _login(item)
        if login is not None and login not in logins:
            logins.append(login)
    return logins


def _name(value: object) -> str | None:
    if isinstance(value, Mapping):
        return _text(value.get("name"))
    return _text(value)


def _milestone_title(value: object) -> str | None:
    if isinstance(value, Mapping):
        return _text(value.get("title"))
    return _text(value)


def _repository(value: object) -> str | None:
    if isinstance(value, str):
        return value or None
    if not isinstance(value, Mapping):
        return None
    name = value.get("name")
    owner = value.get("owner")
    login = owner.get("login") if isinstance(owner, Mapping) else None
    if isinstance(name, str) and name and isinstance(login, str) and login:
        return f"{login}/{name}"
    return None


def _value_text(value: object) -> str | None:
    """Render an issue-field value as text, keeping a multi-select list as JSON."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        return json.dumps(list(value), ensure_ascii=False)
    if isinstance(value, Mapping):
        return json.dumps(dict(value), sort_keys=True, ensure_ascii=False)
    return str(value)


def _insert_labels(connection: sqlite3.Connection, rows: list[Mapping[str, object]]) -> None:
    for row in rows:
        name = _text(row.get("name"))
        if name is None:
            continue
        connection.execute(
            "INSERT OR IGNORE INTO labels (name, description) VALUES (?, ?)",
            (name, _text(row.get("description"))),
        )


def _insert_milestones(connection: sqlite3.Connection, rows: list[Mapping[str, object]]) -> None:
    for row in rows:
        title = _text(row.get("title"))
        if title is None:
            continue
        connection.execute(
            "INSERT OR REPLACE INTO milestones (title, due_on, open_issues, closed_issues) "
            "VALUES (?, ?, ?, ?)",
            (
                title,
                _text(row.get("due_on")),
                _count_field(row.get("open_issues")),
                _count_field(row.get("closed_issues")),
            ),
        )


def _insert_issues(connection: sqlite3.Connection, rows: list[Mapping[str, object]]) -> None:
    for row in rows:
        number = _number(row.get("number"))
        if number is None:
            continue
        connection.execute(
            "INSERT OR REPLACE INTO issues "
            "(number, state, state_reason, title, body, url, author_login, created_at, closed_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                number,
                _state(row.get("state")),
                _state(row.get("stateReason")),
                _text(row.get("title")),
                _text(row.get("body")),
                _text(row.get("url")),
                _login(row.get("author")),
                _text(row.get("createdAt")),
                _text(row.get("closedAt")),
            ),
        )
        for label in _rows(row.get("labels")):
            name = _text(label.get("name"))
            if name is None:
                continue
            connection.execute(
                "INSERT OR IGNORE INTO labels (name, description) VALUES (?, ?)",
                (name, _text(label.get("description"))),
            )
            connection.execute(
                "INSERT OR IGNORE INTO issue_labels (issue_number, label_name) VALUES (?, ?)",
                (number, name),
            )
        for reference in _rows(row.get("closedByPullRequestsReferences")):
            connection.execute(
                "INSERT INTO issue_closing_references "
                "(issue_number, pull_request_number, repository, url) VALUES (?, ?, ?, ?)",
                (
                    number,
                    _number(reference.get("number")),
                    _repository(reference.get("repository")),
                    _text(reference.get("url")),
                ),
            )


def _insert_issue_fields(connection: sqlite3.Connection, rows: list[Mapping[str, object]]) -> None:
    for row in rows:
        number = _number(row.get("number"))
        if number is None:
            continue
        issue_type = _name(row.get("type"))
        milestone = _milestone_title(row.get("milestone"))
        updated = connection.execute(
            "UPDATE issues SET issue_type = ?, milestone_title = ? WHERE number = ?",
            (issue_type, milestone, number),
        )
        if updated.rowcount == 0:
            # The issue-fields dump also carries issues the issue dump missed.
            connection.execute(
                "INSERT INTO issues (number, state, title, issue_type, milestone_title) "
                "VALUES (?, ?, ?, ?, ?)",
                (number, _state(row.get("state")), _text(row.get("title")), issue_type, milestone),
            )
        for login in _logins(row.get("assignees")):
            connection.execute(
                "INSERT OR IGNORE INTO issue_assignees (issue_number, login) VALUES (?, ?)",
                (number, login),
            )
        for value in _rows(row.get("field_values")):
            connection.execute(
                "INSERT INTO issue_field_values (issue_number, name, data_type, value) "
                "VALUES (?, ?, ?, ?)",
                (
                    number,
                    _text(value.get("name")),
                    _text(value.get("data_type")),
                    _value_text(value.get("value")),
                ),
            )


def _insert_pull_requests(connection: sqlite3.Connection, rows: list[Mapping[str, object]]) -> None:
    for row in rows:
        number = _number(row.get("number"))
        if number is None:
            continue
        connection.execute(
            "INSERT OR REPLACE INTO pull_requests "
            "(number, title, state, author_login, head_ref_name, base_ref_name, created_at, "
            "merged_at, closed_at, url, body) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                number,
                _text(row.get("title")),
                _state(row.get("state")),
                _login(row.get("author")),
                _text(row.get("headRefName")),
                _text(row.get("baseRefName")),
                _text(row.get("createdAt")),
                _text(row.get("mergedAt")),
                _text(row.get("closedAt")),
                _text(row.get("url")),
                _text(row.get("body")),
            ),
        )
        for reference in _rows(row.get("closingIssuesReferences")):
            connection.execute(
                "INSERT INTO pr_closing_references "
                "(pull_request_number, issue_number, repository, url) VALUES (?, ?, ?, ?)",
                (
                    number,
                    _number(reference.get("number")),
                    _repository(reference.get("repository")),
                    _text(reference.get("url")),
                ),
            )
        for review in _rows(row.get("reviews")):
            connection.execute(
                "INSERT INTO pr_reviews "
                "(pull_request_number, author_login, state, submitted_at, body) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    number,
                    _login(review.get("author")),
                    _state(review.get("state")),
                    _text(review.get("submittedAt")),
                    _text(review.get("body")),
                ),
            )
        for file in _rows(row.get("files")):
            connection.execute(
                "INSERT INTO pr_files "
                "(pull_request_number, path, change_type, additions, deletions) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    number,
                    _text(file.get("path")),
                    _state(file.get("changeType")),
                    _count_field(file.get("additions")),
                    _count_field(file.get("deletions")),
                ),
            )


def _count(connection: sqlite3.Connection, table: str) -> int:
    row = connection.execute(f"SELECT count(*) FROM {table}").fetchone()
    return int(row[0]) if row is not None else 0


def _count_label(count: int, singular: str) -> str:
    return f"{count} {singular}" if count == 1 else f"{count} {singular}s"
