# Module K — Wolfram and Independent Verification

## Scope

Representative finite checks for:

- `science/NONLINEAR_RELATIONAL_GRAVITY.md`
- `proofs/NONLINEAR_RELATIONAL_GRAVITY.md`

They verify algebra, analytic limits, and synthetic finite systems only. They do not establish a unique full nonlinear universe, public halo/lensing agreement, hydrodynamic closure, or empirical truth.

## Wolfram checks

Wolfram returned:

```text
pair momentum residual = 0
pair torque identity residual = 0
shell-crossing Jacobian = 1 - a cos(q)
first shell-crossing amplitude = a -> 1
Jacobi residual = 0
velocity-Verlet map determinant = 1
K-L-M fixed point = {200/119,310/119}
fixed-point residual = {0,0}
covariance eigenvalues = {(11+3 sqrt(13))/2,(11-3 sqrt(13))/2}
```

This supports exact representative identities for internal momentum/torque closure, first shell crossing, symplectic volume preservation, Jacobi transport, covariance positivity, and recurrence classification.

The evaluator emitted undefined-symbol warnings while still returning the intended exact expressions. The warnings are retained; the check is not described as warning-free.

## Independent NumPy/SciPy check

```text
MODULE_K_INDEPENDENT_CHECK: PASS
promotion_mass=PASS
promotion_momentum=PASS
finiteN_momentum=PASS
finiteN_energy_bounded=PASS
restart_composition=PASS
mesh_force_overlap=PASS
shell_crossing_prepositive=PASS
shell_crossing_postnegative=PASS
binding_bound=PASS
binding_unbound=PASS
web_topology_persistent=PASS
void_registry_nonempty=PASS
jacobi_analytic_overlap=PASS
covariance_psd=PASS
klm_fixed_point=PASS
klm_nonconvergence_detected=PASS
```

Representative residuals:

```text
relative energy drift = 2.607436110761065e-12
momentum residual = 7.494943393176885e-15
mesh-force maximum error = 2.7430314963883262e-17
restart residual = 0
Jacobi error = 1.971756091734278e-13
topology component counts = {2,2,2,2}
K-L-M synthetic fixed point = {1.68067227,2.60504202}
```

## Interpretation

The checks support representative finite claims that:

- no-rescale promotion can preserve mass and momentum;
- pairwise finite-N evolution closes momentum and bounded energy drift;
- checkpoint/restart composition is exact in the tested deterministic branch;
- an independent mesh solve reproduces a manufactured force field;
- shell crossing is distinguished by Jacobian sign change;
- binding witnesses distinguish bound and unbound states;
- a protected web topology persists under small threshold and field perturbations;
- a void registry is nonempty in the synthetic field;
- direct analytic and Jacobi transport agree;
- covariance pushforward remains positive semidefinite;
- a contractive K-L-M map converges and a superunit spectral-radius map is detected as nonconvergent.

## Boundaries

These checks do not establish:

- a completed full-universe nonlinear numerical realization;
- converged halo populations or merger histories;
- hydrodynamics, stars, feedback, or composition return;
- final K-L-M closure;
- public nonlinear spectra, halo statistics, concentrations, or lensing agreement;
- empirical validation.

The science file, proof assumptions, convergence requirements, public-data firewall, and first-pass/final-closure distinction remain controlling.