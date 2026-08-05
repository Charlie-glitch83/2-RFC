# Module Hᵁ — Wolfram and Independent Verification

## Scope

This file records representative exact and numerical checks for:

- `science/LINEAR_BOLTZMANN_TRANSFER_OPERATOR.md`
- `proofs/LINEAR_BOLTZMANN_TRANSFER_OPERATOR.md`

These checks verify finite algebraic and implementation consequences. They do not establish a realized RFC background, public Boltzmann-code agreement, observed transfer functions, final CMB or matter spectra, or empirical truth.

## 1. Scalar/vector/tensor projector algebra

For representative exact orthogonal projectors `P_S`, `P_V`, and `P_T`, Wolfram returned zero residuals for:

```text
P_A^2 - P_A
P_A P_B, A != B
P_S + P_V + P_T - I
```

The independent implementation also passed idempotence, orthogonality, and completeness.

## 2. Weighted gauge projector

For gauge generator `G` and positive state metric `W`, the tested projector

```text
P_phys = I - G (G^T W G)^+ G^T W
```

satisfied:

```text
P_phys G = 0
P_phys^2 = P_phys.
```

This verifies the finite no-loss quotient algebra for the representative gauge direction.

## 3. Constraint propagation identity

For representative matrices `C`, `A`, and `M`, Wolfram and the independent implementation verified

```text
C A = M C
```

for constant `C`, which is the finite special case of

```text
Cdot + C A = M C.
```

Thus an initially vanishing constraint residual remains zero in the tested system.

## 4. Collision conservation

For a representative column-conservative collision generator, the tested left conservation vector satisfied

```text
1^T Q = 0.
```

This verifies conservation of the corresponding integrated collision moment in that finite example.

## 5. Fundamental-matrix composition

For the representative stable two-state operator

```text
A = {{-1/4,1},{-1,-1/6}},
```

the independent implementation verified

```text
Exp[A t2] Exp[A t1] = Exp[A (t1+t2)]
```

within `1e-12`. This checks transfer composition and split/restart identity on an autonomous subinterval.

## 6. Stiff Schur reduction

For a representative slow-fast block, the generated effective slow operator

```text
A_eff = A - B D^+ C
```

was finite and returned

```text
A_eff = 0.07500000000000001.
```

This checks the algebraic reduction formula only. The science file's spectral-gap, overlap, conservation, constraint, and error conditions remain mandatory.

## 7. Covariance positivity

For positive-semidefinite `Sigma_0` and representative transfer matrix `T`, the independent check formed

```text
Sigma = T Sigma_0 T^T
```

and returned eigenvalues

```text
0.37213719
0.53833326
```

so the propagated covariance remained positive definite in the tested realization.

## 8. Direct-versus-line-of-sight identity

For a scalar damped propagation problem with source `exp(-eta)`, the direct analytic Duhamel solution was compared with independent numerical line-of-sight quadrature. The absolute difference was

```text
1.569968599568483e-10.
```

This verifies one representative direct/LOS equivalence, not the full future photon hierarchy.

## 9. Hierarchy-extension stability

A toy damped streaming chain was solved at five and six retained moments. The common lower moments agreed within `1e-6` in the tested interval. This checks one representative refinement behavior; every material Module H hierarchy still requires its own convergence ladder.

## 10. Wolfram exact outputs retained

The representative Wolfram calculation returned:

```text
SVT projector residuals = 0
projector sum = I
gauge annihilation residual = 0
gauge idempotence residual = 0
constraint residual = 0
collision-conservation residual = 0
fundamental composition residual = 0
covariance eigenvalues = {(11+2 Sqrt[11])/2,(11-2 Sqrt[11])/2,0}
```

The zero covariance eigenvalue in that exact toy example is allowed positive semidefiniteness. These are representative algebraic checks rather than physical transfer predictions.

## 11. Independent implementation

A separate NumPy/SciPy implementation returned:

```text
MODULE_H_UNIT_INDEPENDENT_CHECK: PASS
svt_projectors=PASS
gauge_projector=PASS
constraint_propagation=PASS
collision_conservation=PASS
propagator_composition=PASS
schur_reduction_finite=PASS
covariance_psd=PASS
los_direct_agreement=PASS
hierarchy_extension=PASS
```

It used:

- exact block projectors;
- a weighted gauge quotient;
- a finite propagated constraint;
- a conservative collision matrix;
- matrix-exponential transfer composition;
- a slow-fast Schur complement;
- covariance pushforward;
- direct analytic versus numerical Duhamel/LOS evolution;
- a damped hierarchy extension test.

## 12. What these checks establish

They support the finite claims that the representative constructions possess:

- exact SVT projector algebra;
- a valid finite gauge quotient;
- propagated constraints;
- conserved collision moments;
- transfer composition and restart identity;
- finite controlled Schur reduction algebra;
- positive-semidefinite covariance pushforward;
- direct/line-of-sight consistency;
- stable lower moments under one hierarchy extension.

## 13. What these checks do not establish

They do not establish:

- that a realized Module I background lies in `D_B`;
- the later H[I] instantiation;
- complete physical convergence of every species/momentum/multipole hierarchy;
- measured or public transfer functions;
- final angular CMB spectra, matter spectra, growth, or lensing;
- public CLASS/CAMB reproduction;
- empirical agreement.

The exact assumptions, branches, finite support, public-data firewall, and claim boundaries in the science and proof files remain controlling.