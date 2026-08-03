# Module Hᵁ — Wolfram and Independent Verification

## Scope

This file records representative exact and numerical checks for:

- `science/LINEAR_BOLTZMANN_TRANSFER_OPERATOR.md`
- `proofs/LINEAR_BOLTZMANN_TRANSFER_OPERATOR.md`

These checks verify finite algebraic and implementation consequences. They do not establish a realized cosmological background, public Boltzmann-code agreement, measured transfer functions, final spectra, or empirical truth.

## 1. Scalar/vector/tensor projector algebra

For six representative state components, define

```wl
PS = DiagonalMatrix[{1,1,0,0,0,0}];
PV = DiagonalMatrix[{0,0,1,1,0,0}];
PT = DiagonalMatrix[{0,0,0,0,1,1}];
```

Wolfram returned zero matrices for

```text
PS.PV
PS.PT
PV.PT
```

and the identity matrix for

```text
PS + PV + PT.
```

This verifies representative orthogonality and completeness of the sector decomposition.

## 2. Weighted gauge quotient

For the representative gauge generator

```wl
G = {{1},{1},{0},{0},{0},{0}};
W = IdentityMatrix[6];
Pphys = I - G (G^T W G)^+ G^T W;
```

Wolfram returned zero for

```text
Pphys.Pphys - Pphys
Pphys.G.
```

Thus the tested projector is idempotent and annihilates the pure-gauge direction.

## 3. Constraint propagation identity

For

```wl
C = {{1,-1,0,0,0,0}};
A = DiagonalMatrix[{-1,-1,-2,-2,-3,-3}];
M = {{-1}};
```

Wolfram returned zero for

```text
C.A - M.C.
```

This is a representative instance of

```text
Cdot + C A = M C
```

with constant `C`.

## 4. Transfer composition and restart identity

For the same constant generator, Wolfram returned zero for

```text
MatrixExp[2 A].MatrixExp[A] - MatrixExp[3 A].
```

This verifies a representative semigroup/transfer-composition identity.

## 5. Positive Schur reduction

For

```wl
Dfast = DiagonalMatrix[{-4,-6}];
B = IdentityMatrix[2];
Cfast = IdentityMatrix[2];
Aeff = -B.Inverse[Dfast].Cfast;
```

Wolfram returned the positive diagonal entries

```text
1/4, 1/6.
```

The independent implementation returned eigenvalues

```text
0.16666667, 0.25.
```

This supports the claimed positive generated slow transport form when the fast block is stable and negative on its physical subspace.

## 6. Covariance positivity

For

```wl
Sigma0 = {{2,1},{1,2}};
T = MatrixExp[DiagonalMatrix[{-1,-2}]];
SigmaOut = T.Sigma0.Transpose[T] + IdentityMatrix[2]/10;
```

Wolfram returned positive eigenvalues

```text
0.380821474298286...
0.126480369952407...
```

The independent implementation returned the same values to numerical precision.

## 7. Direct versus line-of-sight Duhamel identity

For the representative scalar system

```text
x' = -x + 2,
x(0)=0,
```

the direct solution at `t=1` is

```text
2 (1-exp(-1)).
```

The line-of-sight/Duhamel integral

```text
integral_0^1 exp[-(1-u)] 2 du
```

gives the identical result.

This verifies one exact finite instance of direct-versus-source-propagator closure.

## 8. Independent implementation

A separate NumPy/SciPy implementation returned:

```text
MODULE_H_UNIT_INDEPENDENT_CHECK: PASS
svt_projectors=PASS
gauge_projector=PASS
constraint_propagation=PASS
semigroup_restart=PASS
positive_schur_reduction=PASS
covariance_psd=PASS
direct_los_duhamel=PASS
Aeff_eigenvalues= [0.16666667 0.25]
Sigma_eigenvalues= [0.12648037 0.38082147]
```

The implementation used:

- exact finite scalar/vector/tensor projectors;
- a rank-one gauge generator and pseudoinverse quotient;
- a propagated linear constraint;
- matrix-exponential composition;
- stable fast-block elimination;
- covariance pushforward with positive forcing;
- one exact Duhamel/line-of-sight reconstruction.

## 9. What these checks establish

They support the finite claims that the representative constructions possess:

- orthogonal complete sector projectors;
- a lawful physical gauge quotient;
- propagated constraints;
- transfer composition and restart consistency;
- positive stable Schur reduction;
- positive-semidefinite covariance propagation;
- direct/source-propagator agreement in a manufactured problem.

## 10. What these checks do not establish

They do not establish:

- a realized Module I background;
- completed H[I] instantiation;
- convergence of every future full species/momentum/multipole realization;
- public CLASS/CAMB agreement;
- observed CMB or matter transfer functions;
- primordial covariance or final spectra;
- empirical validation.

The assumptions, background domain, finite support, branch conditions, truncation bounds, and claim boundaries in the science and proof files remain controlling.