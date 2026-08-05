# Module I — Wolfram and Independent Verification

## Scope

This file records representative exact and numerical checks for:

- `science/REALIZED_BACKGROUND_GEOMETRY.md`
- `proofs/REALIZED_BACKGROUND_GEOMETRY.md`

These checks verify finite algebraic and implementation consequences only. They do not establish a measured cosmological background, public distance agreement, observed dark-sector behavior, or empirical truth.

## 1. Sector-transfer conservation

For a representative four-sector transfer generator `Q` with ordinary, radiative, compression-relic, and dissipative-tail columns, Wolfram returned

```text
column sums = {0,0,0,0}
left conservation residual = {0,0,0,0}
```

Thus each internal transfer is paired and total transfer vanishes in the tested system.

## 2. Total continuity and geometric constraint

For the representative generated background reduction

```text
dr_s/dx = -d (1+w_s) r_s + (Q r)_s
H^2 = C_geom sum_s r_s
```

Wolfram symbolically reduced the summed continuity equation to zero when the transfer-column sums vanish.

The independent implementation checked

```text
max |sum_s dr_s/dx + d sum_s(1+w_s)r_s| = 3.552713678800501e-15
max |H^2 - C_geom sum_s r_s| < 1e-12
```

for a synthetic internally specified branch.

## 3. Compression-relic and dissipative-tail equations of state

For generated energy laws

```text
E_comp(V) proportional to V^sig
E_tail(V) proportional to V^nu
```

with `rho=E/V` and `p=-dE/dV`, Wolfram returned

```text
w_comp = -sig
w_tail = -nu
```

under the declared exponent convention.

This verifies that pressure follows from the generated volume dependence. It does not select any physical exponent or insert dust, a cosmological constant, or a fitted `w(a)`.

## 4. Constraint propagation identity

For a representative constraint `C(X)=H^2-C_geom rho_tot`, the symbolic derivative reduced to zero when the generated continuity and expansion derivative were substituted.

This checks the finite isotropic special case of constraint propagation. The full relational action and branch constraints remain controlling.

## 5. Distance reciprocity

Under metric propagation and photon-number conservation, Wolfram evaluated

```text
D_A = D_M/(1+z)
D_L = (1+z) D_M
D_L - (1+z)^2 D_A = 0
```

exactly.

The independent implementation also returned zero residual on several internally generated emission events.

## 6. Volume-distance identity

For the declared isotropic convention, Wolfram returned

```text
D_V^3 = z D_H D_M^2
```

exactly from the definition. This is an internal geometric identity, not a BAO likelihood or public ruler input.

## 7. Immutable H[I] coefficient substitution

For a representative frozen operator schema `A[B]`, Wolfram substituted a generated background coefficient packet and returned zero structural residual between the predeclared symbolic grammar and the instantiated coefficient matrix.

The independent implementation confirmed that the nonzero block pattern of the operator remained unchanged at separated background times.

## 8. Transfer composition and restart identity

For a representative instantiated three-state linear operator, the independent implementation compared:

```text
direct evolution x0 -> x1
```

against

```text
x0 -> xm -> x1
```

and obtained

```text
maximum composition residual = 6.661338147750939e-16.
```

This checks one finite H[I] restart/composition realization.

## 9. Covariance positivity

Wolfram evaluated a representative covariance pushforward and returned

```text
Sigma_out = {{31/12,5/8},{5/8,9/16}}
eigenvalues = {(151+Sqrt[13009])/96,(151-Sqrt[13009])/96}
```

both positive.

The independent Module I/H[I] example returned

```text
minimum covariance eigenvalue = 0.22052952400532388.
```

## 10. Independent dual-formulation background check

A separate NumPy/SciPy implementation solved the same synthetic internally specified four-sector system using:

1. logarithmic scale as the integration variable;
2. physical time with scale as a dynamical variable.

It returned

```text
maximum sector-state disagreement = 7.277772134939298e-14
internal-time disagreement = 7.762679388179095e-13.
```

No public background or measured parameter entered the synthetic test.

## 11. Null-distance dual reconstruction

The independent implementation reconstructed the same radial null distance by:

1. integrating conformal time as part of the background state;
2. independently applying refined composite quadrature to `1/(aH)`.

It returned

```text
maximum distance disagreement = 1.3171685964152857e-12.
```

## 12. Horizon monotonicity

For positive generated propagation speeds and positive expansion, the representative particle and sound reach integrals were nondecreasing over the tested interval.

This checks one finite branch. It does not prove that every future horizon exists or remains finite.

## 13. Background derivative consistency

The independent implementation compared the analytic derivative

```text
dH/dx = C_geom (d rho_tot/dx)/(2H)
```

with high-resolution numerical differentiation and returned

```text
maximum interior derivative disagreement = 9.622774799211697e-09.
```

## 14. Hᵁ domain-compliance example

The representative generated branch passed the tested conjunction:

```text
positive and monotone scale
positive sector densities
finite positive expansion
zero-sum transfer
continuity closure
geometric constraint closure
dual-formulation agreement
distance reconstruction agreement
horizon monotonicity
immutable operator grammar
restart composition
positive covariance
```

No aggregate score overrode an individual requirement.

## 15. Independent implementation result

The final independent implementation returned:

```text
MODULE_I_INDEPENDENT_CHECK: PASS
dual_formulation_background=PASS
sector_transfer_zero_sum=PASS
total_continuity=PASS
geometric_constraint=PASS
background_derivative_consistency=PASS
null_distance_dual_reconstruction=PASS
distance_reciprocity=PASS
horizon_monotonicity=PASS
h_unit_grammar_immutable=PASS
h_i_restart_composition=PASS
covariance_psd=PASS
h_domain_compliance=PASS
```

Representative final synthetic values were

```text
final sector state =
{0.00493569,0.00039745,0.00062551,0.05972972}

final internal physical time = 7.2366536239137345
final conformal time = 2.2933753775296895
```

These are synthetic verification values, not RFC predictions or public cosmological values.

## 16. What these checks establish

They support the finite claims that the representative constructions possess:

- zero-sum internal sector transfer;
- total continuity and geometric-constraint closure;
- pressure derived from generated energy-volume dependence;
- metric distance reciprocity;
- consistent distance and horizon constructions;
- dual-formulation background agreement;
- stable derivative reconstruction;
- immutable H[I] coefficient substitution;
- transfer composition/restart identity;
- positive-semidefinite covariance;
- conjunction-based Hᵁ domain compliance.

## 17. What these checks do not establish

They do not establish:

- a unique realized physical branch for the full RFC source packet;
- measured `H0`, density fractions, curvature, age, or distances;
- a public sound horizon or BAO ruler;
- observed supernova, siren, or chronometer agreement;
- public CLASS/CAMB or background-code reproduction;
- a fitted cold-dark-matter or dark-energy law;
- primordial covariance or final spectra;
- nonlinear structure or terminal Big-Rip dynamics;
- empirical confirmation.

The science file, proof, branch conditions, finite-support assumptions, public-data firewall, and frozen Hᵁ domain remain controlling.