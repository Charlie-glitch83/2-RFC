# Module A — Wolfram Integration Revision

This file is a binding revision to `MODULE_A_DETAILED_SCIENTIFIC_REPAIR_PLAN.md` and must be read with `architecture/2RFC_WOLFRAM_INTEGRATION_RULES.md`.

## Authorized work

Use Wolfram to verify and extend only the already established Module A mathematics:

- exact triadic-weight normalization and role separation;
- convergence, norm bounds, truncation error, perturbation stability, and conditional differentiability of the recursive kernel;
- exact lane count `N(N-1)` and add-one growth `2N`;
- graph, route, witness, branch, and event combinatorics;
- local existence assumptions, Jacobians, singular sets, and maximal noncollision continuation conditions;
- equivalence-class and quotient injectivity tests;
- memory encode/decode and promotion/reopening identities;
- zero-backreaction and finite-to-continuum limits;
- symbolic counterexamples to overstrong claims such as unchanged positive-mass trajectories.

## Required methods

Prefer exact symbolic evaluation, `Assuming`, `FullSimplify`, spectral decomposition, graph invariants, exact series, interval bounds, and arbitrary-precision continuation. Every simplification must expose assumptions.

## Independent checks

Pair Wolfram results with analytic proof, direct combinatorial counting, or an independent numerical route solver. Route multiplicity must be checked modulo gauge equivalence, not by raw solution count.

## Forbidden use

Wolfram may not invent a missing triad law, choose constants from known trajectories, import a standard N-body solution as a generative witness, or turn numerical route existence into a global all-time theorem.

## Completion addition

Module A implementation is not complete until every load-bearing symbolic identity and bound has a reproducible Wolfram check and at least one independent non-Wolfram witness.