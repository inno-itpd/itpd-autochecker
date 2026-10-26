from __future__ import annotations

# Segment names must match the `- S<n>: <name>` lines in `A<N>/grading_prompt.md` exactly.
# `week_window_start` is 00:00 on the first day of the assignment's week and
# `issue_cutoff` is its hard deadline, both ISO 8601 in Innopolis time (UTC+3),
# the only timezone the course states, so the deadline facts live in one place.
# A team whose deadline differs from the assignment's default is listed in
# `team_issue_cutoffs` under its exact `submissions/` directory name; `issue_cutoff_for`
# reads the override. The prompt states the same rule for the grader.
ASSIGNMENT_CONFIG: dict[str, dict] = {
    "A1": {
        "week": 1,
        "course_commit": "fe58ba70bbd90b92ffd6942d340f1e8b35b4bbb1",
        "primary_index": "reports/week-01/README.md",
        "week_window_start": "2026-09-25T00:00:00+03:00",
        "issue_cutoff": "2026-10-02T23:59:59+03:00",
        "segment_defs": {
            1: {"name": "Repository setup and branch protection"},
            2: {"name": "CI checks and supply-chain hygiene"},
            3: {"name": "Collaboration through pull requests"},
            4: {"name": "Alternatives research"},
            5: {"name": "Comparison and gap analysis"},
            6: {"name": "Value proposition and assumptions"},
            7: {"name": "Customer kickoff meeting"},
            8: {"name": "Week report and submission"},
            9: {"name": "AI usage and research honesty"},
        },
    },
    "A2": {
        "week": 2,
        "course_commit": "a949e8d7ff7f677ed3b97fa1b9bd9291b4a05bc1",
        "primary_index": "reports/week-02/README.md",
        "week_window_start": "2026-10-02T00:00:00+03:00",
        "issue_cutoff": "2026-10-10T23:59:59+03:00",
        "segment_defs": {
            1: {"name": "Issue forms, labels, and task workflow"},
            2: {"name": "Decisions and assumptions in the Week 2 format"},
            3: {"name": "Markdown CI and research entry format"},
            4: {"name": "Product vision and context diagram"},
            5: {"name": "User stories and acceptance criteria"},
            6: {"name": "Minimum usable product candidate"},
            7: {"name": "Prototypes and customer-driven change"},
            8: {"name": "Customer validation meeting"},
            9: {"name": "Week report and submission"},
            10: {"name": "AI usage and research honesty"},
        },
    },
    "A3": {
        "week": 3,
        "course_commit": "23b22a6d637c0ac9c6a3350b377ae333cb42a082",
        "primary_index": "reports/week-03/README.md",
        "week_window_start": "2026-10-09T00:00:00+03:00",
        "issue_cutoff": "2026-10-17T23:59:59+03:00",
        "segment_defs": {
            1: {"name": "Threshold of success"},
            2: {"name": "Project plan and sprint milestones"},
            3: {"name": "Risk register"},
            4: {"name": "Stack decision and dependencies"},
            5: {"name": "Definition of Done and contributing guide"},
            6: {"name": "Issue fields and GitHub project"},
            7: {"name": "Minimum usable product on main"},
            8: {"name": "Documentation site and setup page"},
            9: {"name": "Week 2 action points and open questions"},
            10: {"name": "Customer validation of the working software"},
            11: {"name": "Changelog and first release"},
            12: {"name": "Week report and submission"},
            13: {"name": "AI usage and honesty"},
        },
    },
    "A4": {
        "week": 4,
        "course_commit": "35c9294415d31c81a8598042b8b7419ea4481a46",
        "primary_index": "reports/week-04/README.md",
        "week_window_start": "2026-10-16T00:00:00+03:00",
        "issue_cutoff": "2026-10-25T23:59:59+03:00",
        "team_issue_cutoffs": {
            "Team 2 - OK_10938_assignsubmission_file": "2026-10-26T23:59:59+03:00",
        },
        "segment_defs": {
            1: {"name": "Sprint plan and estimates"},
            2: {"name": "Product backlog refinement and issue fields"},
            3: {"name": "Quality requirements and priority matrix"},
            4: {"name": "Container view and responsibilities"},
            5: {"name": "Functional requirements and index"},
            6: {"name": "Architecture drivers and vision link"},
            7: {"name": "Architectural decision records and index"},
            8: {"name": "Issue catch-up"},
            9: {"name": "Glossary and team AGENTS.md"},
            10: {"name": "Week 3 action points and open questions"},
            11: {"name": "Customer validation of stories and architecture"},
            12: {"name": "REL-04 release"},
            13: {"name": "Sprint close and retrospective"},
            14: {"name": "Documentation site and navigation"},
            15: {"name": "Week report and submission"},
            16: {"name": "AI usage and honesty"},
        },
    },
}

FEEDBACK_ROOT = "itpd-assignments-feedback"


def issue_cutoff_for(assignment: str, team_dir: str) -> str:
    """Return the cutoff for one team, honoring its per-team override."""
    config = ASSIGNMENT_CONFIG[assignment]
    return config.get("team_issue_cutoffs", {}).get(team_dir, config["issue_cutoff"])


def default_paths(assignment: str) -> dict[str, str]:
    base = f"{FEEDBACK_ROOT}/{assignment}"
    return {
        "feedback_dir": f"{base}/feedback",
        "dev_output": f"{base}/dev.md",
        "release_output": f"{base}/feedback_release.csv",
    }
