# Pipeline Style Guide

This guide defines a reusable architecture:

`config -> steps -> artifacts -> logs -> metrics`

## Why this pattern works

- **Config**: one source of truth for behavior and paths.
- **Steps**: isolated units of work you can test and reorder.
- **Artifacts**: concrete outputs (files, tables, reports) for traceability.
- **Logs**: human-readable runtime history for debugging.
- **Metrics**: machine-readable quality/performance signals for decisions.

## Core objects

- `PipelineContext`: shared mutable state passed through steps.
- `PipelineStep`: protocol/base for any step with `run(ctx) -> ctx`.
- `run_pipeline(config)`: orchestrates step execution and returns context.

## Minimal contract

```python
@dataclass
class PipelineContext:
    run_name: str
    root_dir: Path
    config: dict[str, Any]
    artifacts: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)

class PipelineStep(Protocol):
    name: str
    def run(self, ctx: PipelineContext) -> PipelineContext: ...
```

## Step design rules

- One responsibility per step.
- No hidden global state.
- Read from `ctx.config`; write outputs to `ctx.artifacts` and `ctx.metrics`.
- Log every meaningful state transition.
- Keep steps deterministic when possible.

## Artifact conventions

- Write under `outputs/<run_name>/...`
- Keep filenames stable and explicit.
- Record produced paths in `ctx.artifacts`.

## Logging conventions

- Use `logging`, not `print`, in `src/` code.
- Include step names in log messages.
- Keep logs concise and structured for scanning.

## Metrics conventions

- Use stable keys (for example: `records_processed`, `duration_seconds`).
- Keep numeric values serializable.
- Store final metrics in a small JSON artifact.

## Failure strategy

- Fail fast on invalid config.
- Raise explicit exceptions with actionable messages.
- Let `main.py` map exceptions to non-zero exit codes.

## Adapting to project types

- **App/service**: add I/O boundary steps and deployment entrypoints.
- **Library**: keep pipeline optional and expose pure reusable functions.
- **Research**: keep exploratory notebooks, but productionize repeated logic into steps.
