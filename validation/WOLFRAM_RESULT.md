# Wolfram Independent Check

**Executed:** 2026-08-01 UTC  
**Input:** `validation/wolfram_checks.wl`, repeated with exact rational forms for the frozen decimals.

## Exact result

```text
WeightTotal      = 1
LaneGrowth       = 2 n
KernelBound      = True for t >= 0
QEigenvalues     = {1, 1/2, 1/4}
TotalPreserved   = True
DirichletChange  = -63/2
```

The kernel sum was returned in the equivalent exact form

\[
1+\left(-1+\frac{11673}{2500}
e^{256831t/10000000}\right)^{-1},
\]

which equals \((1-\delta^{-1}e^{-\alpha t})^{-1}\) for \(\delta=4.6692\) and \(\alpha=0.0256831\).

## Interpretation

Wolfram independently confirms the weight normalization, lane-growth identity, geometric-kernel bound, and the fixed graph-resolvent example. This is an internal algebra certificate only. It neither supplies the missing causal/physical realization nor validates RFC against observations.
