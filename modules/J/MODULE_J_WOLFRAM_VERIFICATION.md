# Module J — Wolfram and Independent Verification

## Scope

This file records representative exact and numerical checks for:

- `science/PRIMORDIAL_COVARIANCE_LINEAR_SPECTRA.md`
- `proofs/PRIMORDIAL_COVARIANCE_LINEAR_SPECTRA.md`

The checks verify finite algebraic and implementation consequences. They do not establish a unique full RFC primordial covariance, measured spectra, public Boltzmann-code agreement, nonlinear structure, or empirical truth.

---

## 1. Exact covariance construction

For a representative source factor `L` and mode-incidence map `R`, Wolfram evaluated

```text
P = R L L† R†
```

and returned:

```text
Hermitian residual = 0
raw covariance eigenvalues = {2,1,0}
```

The zero eigenvalue is lawful positive semidefiniteness in the representative constrained mode space.

This verifies the exact factorized covariance theorem, not a physical amplitude or spectral shape.

---

## 2. Generated symmetry projection

For a representative finite unitary symmetry action, Wolfram formed

```text
P_sym = mean_g U(g) P U(g)†
```

and returned positive eigenvalues

```text
{1,1,1}.
```

This checks that averaging over an actually generated unitary symmetry preserves Hermiticity and positive semidefiniteness.

It does not authorize imposing homogeneity, isotropy, parity, or any other symmetry on an RFC branch where that symmetry has not been derived.

---

## 3. Transfer-covariance contraction

For a representative frozen transfer matrix `T`, Wolfram evaluated

```text
P_out = T P T†
```

and returned

```text
P_out = {{7,5/2+Sqrt[3]},
         {5/2+Sqrt[3],2+Sqrt[3]}}
```

with eigenvalues

```text
(9+Sqrt[3] ± Sqrt[65+10 Sqrt[3]])/2.
```

Both eigenvalues are nonnegative. This verifies that immutable linear response contraction preserves covariance positivity in the exact representative case.

---

## 4. Constraint support

For a representative physical-mode constraint row `C`, Wolfram returned

```text
C P = 0.
```

The independent implementation also verified the constraint residual before and after transfer evolution over the sampled scale/time domain.

This checks covariance support on a constrained physical quotient. It does not replace the full H[I] gauge and constraint registry.

---

## 5. Projected spectrum matrix

For representative projection rows and positive quadrature weights, Wolfram produced a Hermitian projected channel matrix with eigenvalues

```text
(28-2 Sqrt[3] ± Sqrt[229-52 Sqrt[3]])/4.
```

The independent implementation generated three-channel projected matrices over multiple generalized multipoles and returned a minimum eigenvalue

```text
0.002205.
```

This verifies the positive-semidefinite projection theorem in finite examples. It does not establish physical CMB spectra.

---

## 6. Growth-rate identity

Wolfram symbolically verified the identity

```text
D = Sqrt[P/P_ref]
f = d Log[D] / d Log[a]
  = (1/(2 H P)) dP/dt
```

under `d Log[a]/dt = H`.

The independent implementation compared the analytic covariance derivative

```text
dP/dt = A P + P A^T
```

with a numerical derivative of the covariance-normalized growth and returned

```text
maximum growth-rate disagreement = 5.461e-08.
```

No external growth normalization entered.

---

## 7. Covariance uncertainty pushforward

For a representative covariance and Jacobian, Wolfram returned

```text
Sigma_out = {{31/12,7/24},{7/24,23/24}}
```

with eigenvalues

```text
(85 ± Sqrt[1717])/48,
```

both positive.

The independent implementation returned

```text
minimum covariance eigenvalue = 0.354702.
```

This verifies representative positive-semidefinite uncertainty propagation.

---

## 8. Direct ensemble versus analytic contraction

A separate NumPy/SciPy implementation constructed a six-component constrained mode system, generated a four-dimensional physical covariance from route/memory factors, propagated it through a frozen stable transfer operator, and compared:

1. analytic covariance contraction;
2. direct evolution of `160000` complex realizations.

It returned

```text
relative covariance disagreement = 0.000941.
```

The imaginary antisymmetric sampling residual remained within the same finite-ensemble scale.

This verifies representative direct-ensemble/transfer equivalence. It does not establish convergence of every physical RFC mode or branch.

---

## 9. Finite-volume field reality

The independent implementation generated paired Fourier coefficients satisfying

```text
q(-k) = Conjugate[q(k)]
```

for a three-field covariance and performed inverse transforms over a 64-cell periodic volume.

It returned

```text
maximum imaginary field component = 6.906e-17.
```

Thus the paired-mode construction produced real fields to numerical precision.

---

## 10. Finite-volume covariance recovery

Across `5000` finite-volume realizations, the recovered representative shell covariance differed from its target by

```text
relative Frobenius error = 0.025928.
```

The discrepancy lies within the expected finite-ensemble scale for the test. This verifies one realization grammar and estimator, not a full production-volume convergence ladder.

---

## 11. Primordial covariance support and transfer positivity

Across 20 internally specified scale points, the independent implementation returned:

```text
maximum Hermitian residual < 1e-12
maximum primordial constraint residual = 6.323e-16
minimum primordial covariance eigenvalue = -1.642e-16
minimum transferred covariance eigenvalue = -1.988e-16.
```

The tiny negative values are roundoff-level residuals around exact semidefinite zero modes, not clipped physical eigenvalues.

---

## 12. Componentwise linearity domain

The independent implementation defined separate amplitude, second-order, displacement, constraint, and direct/transfer witnesses over a scale/time grid.

A point was retained only if every mandatory witness passed its own threshold. Every rejected point was independently confirmed to violate at least one component condition.

The fraction of represented scales acquiring a finite first-promotion time inside the tested interval was

```text
0.225.
```

This value is specific to the synthetic example and is not an RFC prediction. The check verifies that no average score overrode a failed witness.

---

## 13. Restart and transfer composition

For a representative frozen transfer operator, the independent implementation compared direct propagation with split propagation and returned

```text
maximum restart/composition residual = 2.776e-16.
```

This checks one finite realization of the restart identity required by the Module J→K packet.

---

## 14. Independent implementation result

The final independent implementation returned:

```text
MODULE_J_INDEPENDENT_CHECK: PASS
primordial_hermitian_psd=PASS
constraint_support=PASS
transfer_contraction_psd=PASS
projected_spectrum_psd=PASS
direct_ensemble_agreement=PASS
finite_volume_reality=PASS
finite_volume_covariance=PASS
growth_rate_consistency=PASS
covariance_pushforward_psd=PASS
linearity_domain_componentwise=PASS
restart_composition=PASS
```

Representative numerical details were:

```text
primordial minimum eigenvalue = -1.642e-16
transferred minimum eigenvalue = -1.988e-16
projected minimum eigenvalue = 2.205e-03
direct-ensemble relative error = 0.000941
finite-volume covariance relative error = 0.025928
growth-rate maximum error = 5.461e-08
uncertainty covariance minimum eigenvalue = 0.354702
restart residual = 2.776e-16
```

All inputs were synthetic internally specified matrices and kernels. No public primordial spectrum, amplitude, tilt, cosmological parameter, transfer function, observed spectrum, or normalization entered.

---

## 15. What these checks establish

They support the finite claims that the representative constructions possess:

- factorized Hermitian positive-semidefinite covariance;
- physical constraint support;
- positivity-preserving symmetry projection;
- positivity-preserving transfer contraction;
- positive-semidefinite projected spectrum matrices;
- covariance-derived growth-rate consistency;
- direct ensemble and analytic covariance agreement;
- real finite-volume fields under mode pairing;
- finite-volume covariance recovery within sampling error;
- positive-semidefinite uncertainty pushforward;
- componentwise nonlinear-promotion decisions;
- transfer restart/composition identity.

---

## 16. What these checks do not establish

They do not establish:

- the unique realized full RFC primordial covariance;
- complete convergence over every physical mode, route, scale, time, multipole, branch, volume, and higher moment;
- measured primordial amplitude, tilt, running, features, tensor ratio, or mode mixture;
- observed CMB, matter, lensing, or growth agreement;
- public CLASS/CAMB reproduction;
- nonlinear collapse, halos, galaxies, or feedback;
- terminal Big-Rip dynamics;
- empirical confirmation.

The science file, proof assumptions, exact parent identities, branch conditions, finite-support bounds, public-data firewall, and Module J→K handoff remain controlling.