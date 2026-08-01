# Kernel Completion Proof Record

## K1 — Kernel convergence

**Status:** `PROVED` under bounded-feature, \(\delta>1\), \(\alpha\ge0\), \(t\ge0\) assumptions.

The proof is recorded in `science/FOUNDATION.md`. Uniform bounds also justify the stated derivative when feature coefficients are time-independent.

## K2 — Finite lane growth

**Status:** `PROVED`.

\[
|\Lambda_N|=N(N-1),\qquad
|\Lambda_{N+1}\setminus\Lambda_N|=2N.
\]

This is structural capacity, not proof of a physical solution.

## K3 — Route normalization

**Status:** `CONDITIONAL`.

For a finite nonempty admitted route family \(\mathcal R_N\) with strictly positive finite weights \(w_\rho\),

\[
Z_N=\sum_{\rho\in\mathcal R_N}w_\rho
\]

is finite and nonzero, so \(p_\rho=w_\rho/Z_N\) is normalized. The singleton route used on a maximal noncollision solution interval has \(Z_N=1\). Infinite or singular route families require a separate measure/convergence proof and are not silently covered.

## K4 — Corrected add-one-body refinement

**Status:** `PROVED_CONDITIONALLY`; the original unchanged-trajectory inclusion statement is rejected.

Let \(x_N(t)\) be an \(N\)-body Newtonian solution on \([0,T]\) whose relevant pair separations remain at least \(d>0\). Add a body of mass \(\mu\) with an admissible trajectory that also remains at least \(d\) from the original bodies. For each original body, the added acceleration has magnitude at most

\[
\frac{G\mu}{d^2}.
\]

On a compact noncollision neighborhood the first-order ODE vector field is locally Lipschitz with constant \(L\). Continuous dependence and Grönwall's inequality give a bound of the form

\[
\sup_{0\le t\le T}
\|\pi_Nx_{N+1}^{(\mu)}(t)-x_N(t)\|
\le C_T\mu,
\]

where \(C_T\) depends on the compact domain, masses, \(d\), and \(T\), but not on \(\mu\) near zero. Hence the projected augmented solution converges to the original solution as \(\mu\to0^+\).

For every positive \(\mu\), the additional acceleration is generally nonzero; exact unchanged trajectory inclusion is not true. The lawful refinement is the expanded source/problem map plus the zero-backreaction limit, not literal preservation of the old orbit.

## K5 — Event lift and no-loss memory

**Status:** `CONSTRUCTION_PROVED_WITH_SCOPE`.

A partial set-valued event lift may carry branch packets across a singular boundary only when each output retains a protected signature containing source identity, route/witness identity, invariants or residuals, branch identity, uncertainty, and ancestry. A quotient is lossless only if the protected signature factors injectively through it.

This proves a safe representation protocol. It does not solve every collision, establish all-time regularity, or choose a unique physical continuation.

## Kernel completion conclusion

K1–K5 establish the abstract relational carrier needed at the terminal triad kernel. Physical activation is delegated to the realization interface. That interface is the current proof frontier.
