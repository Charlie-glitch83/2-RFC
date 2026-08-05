# Validation

Run `python validation/validate_repo.py` from the repository root.

The script checks:

- `STATE.json` and required entry files;
- the five-source manifest, exact hashes, and public `1RFC` paths;
- triad weights and frozen constants;
- directed-lane counts and add-one growth;
- kernel partial sums against the analytic bound;
- graph-resolvent algebra on a fixed three-node example;
- absence of duplicate machine-state files.

`wolfram_checks.wl` independently states the symbolic/numeric checks intended for Wolfram Language. The executed result is recorded in `WOLFRAM_RESULT.md`. Neither file certifies R1–R9 or empirical truth.
