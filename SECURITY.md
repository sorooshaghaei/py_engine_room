# Security

## Secrets policy

- Never commit secrets (tokens, keys, passwords).
- Keep local secrets in `.env` (gitignored).
- Use environment variables in runtime code.
- Use separate credentials per environment.

## Data policy

- Treat raw and generated data as non-source artifacts.
- Keep `data/` and `outputs/` out of git by default.
- Document external data sources and access assumptions.

## Dependency policy

- Keep dependencies minimal.
- Prefer well-maintained packages.
- Review dependency updates before merging.

## Incident basics

If a secret is exposed:

1. Revoke/rotate immediately.
2. Remove from history if needed.
3. Document impact and remediation.
