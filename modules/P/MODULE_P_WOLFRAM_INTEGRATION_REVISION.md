# Module P — Wolfram Integration Revision

Binding revision to `MODULE_P_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`; governed by `architecture/2RFC_WOLFRAM_INTEGRATION_RULES.md`.

## Authorized work

Use Wolfram inside the read-only empirical branch for:

- signal, propagation, instrument, beam, cadence, selection, mask, foreground, noise, and catalogue operators;
- synthetic observations and public-data transformations;
- covariance, likelihood, posterior-predictive, residual, robustness, and cross-probe calculations;
- identifiability, information loss, sensitivity, multiple-testing, and look-elsewhere analysis;
- preregistered statistics, mandatory component scores, falsifiers, and evidence decisions;
- branch, ensemble, realization, finite-volume, and observer-location marginalization;
- independent reproduction of all comparison outputs.

## Required methods

Freeze code, assumptions, data roles, transformations, statistics, nuisance rules, and decision thresholds before unblinding. Preserve exact dataset versions and transformation lineage. Use arbitrary precision when numerical conditioning can affect a mandatory decision.

## Mandatory score rule

Every mandatory normalized component below `0.95` fails. Wolfram-computed averages, likelihoods, or global fits may not hide a failed component.

## Forbidden use

No P-derived parameter, residual, branch ranking, nuisance estimate, empirical repair, or public-data object may alter Modules A–O or enter Module Q.

## Completion addition

Every claim decision requires reproducible Wolfram code, full residual and covariance structure, robustness and identifiability analysis, preserved forecasts, and materially independent replication.