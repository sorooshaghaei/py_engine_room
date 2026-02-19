# Team Workflow

A lightweight workflow for small and medium teams.

## Branch strategy

- `main`: always releasable.
- `feature/<topic>`: one focused change.
- `fix/<topic>`: bugfix branch.
- `chore/<topic>`: maintenance-only changes.

## Pull requests

Each PR should include:

- Problem statement
- Scope and non-goals
- Test evidence (`pytest`, examples run)
- Risk notes (behavior, performance, migration)

Keep PRs small and reviewable.

## Commit messages

Use imperative style and focused commits.

Examples:

- `feat: add pipeline context metrics serialization`
- `fix: handle missing config keys in loader`
- `docs: clarify __init__.py public API rules`

## Code review checklist

- Correctness and edge cases
- Readability and maintainability
- Logging and error messages
- Test coverage for changed behavior
- Backward compatibility for public API

## Issues and planning

- One issue = one problem.
- Include acceptance criteria.
- Link PRs to issues.
- Track technical debt with explicit labels.

## Notebook policy in teams

- Notebooks are for exploration and explanation.
- Repeated logic moves to `src/`.
- Clear outputs before commit unless outputs are required artifacts.
