# Notebooks Guide

Use notebooks for learning and exploration, not hidden production logic.

## Good notebook habits

- Start with objective + expected output.
- Keep each cell small and single-purpose.
- Import from `src/` instead of redefining core logic repeatedly.
- End with a short conclusions cell.

## Reproducibility rules

- Pin dependencies.
- Use deterministic seeds when randomness exists.
- Keep data paths explicit and relative.
- Avoid environment-specific assumptions.

## Team collaboration rules

- Strip noisy outputs before commit.
- Name notebooks with numeric prefixes for order.
- Move reusable functions into modules under `src/`.
- Add a short "next actions" markdown cell.

## Common mistakes

- Hidden state from out-of-order execution
- Copy-pasted business logic duplicated across notebooks
- Credentials in notebook cells
- Massive binary outputs in version control

## Active learning pattern

For every notebook section:

1. Explain concept briefly.
2. Run a tiny example.
3. Add a recall prompt ("without looking, explain why").
4. Add a transfer prompt ("adapt this to another project type").
