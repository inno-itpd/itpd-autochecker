from __future__ import annotations

# Segment names must match the `- S<n>: <name>` lines in `A<N>/grading_prompt.md` exactly.
ASSIGNMENT_CONFIG: dict[str, dict] = {
    "A1": {
        "week": 1,
        "course_commit": "fe58ba70bbd90b92ffd6942d340f1e8b35b4bbb1",
        "primary_index": "reports/week-01/README.md",
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
}

FEEDBACK_ROOT = "itpd-assignments-feedback"


def default_paths(assignment: str) -> dict[str, str]:
    base = f"{FEEDBACK_ROOT}/{assignment}"
    return {
        "feedback_dir": f"{base}/feedback/markdown",
        "dev_output": f"{base}/dev.md",
        "release_output": f"{base}/feedback_release.csv",
    }
