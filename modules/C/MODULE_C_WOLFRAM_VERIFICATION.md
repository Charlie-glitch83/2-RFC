# Module C Wolfram Verification

## Scope

This record verifies exact linear-algebra consequences of the current Module C candidate-capacity boundary. Wolfram is used as a derivation and verification engine, not as a source of particle physics.

No named particle, gauge group, measured mass, coupling, mixing value, lifetime, abundance, or Standard Model constant entered these checks.

## Exact test case

The historical controlled candidate registry contains:

\[
n_o=6,
\qquad
n_r=2,
\qquad
n=8.
\]

It is retained only as a finite representation test case.

## Verified results

### 1. Orthogonal automorphism dimensions

For a real eight-dimensional carrier,

\[
\dim\mathfrak{so}(8)=\frac{8\cdot7}{2}=28.
\]

For sector-preserving automorphisms,

\[
\dim\bigl(\mathfrak{so}(6)\oplus\mathfrak{so}(2)\bigr)
=\frac{6\cdot5}{2}+\frac{2\cdot1}{2}=16.
\]

Wolfram returned:

```text
FullOrthogonalLieAlgebraDimension = 28
SectorPreservingOrthogonalLieAlgebraDimension = 16
ExpectedSectorDimension = 16
```

### 2. Protected-signature commutant

For eight distinct protected signatures represented by a generic diagonal signature operator, the full matrix commutant is the eight-dimensional diagonal algebra.

Restricting to real continuous orthogonal generators leaves zero Lie-algebra dimension. The only signature-preserving permutation is the identity.

Wolfram returned:

```text
ProtectedSignatureCommutantDimension = 8
ProtectedSignaturePreservingContinuousOrthogonalDimension = 0
ProtectedSignaturePreservingPermutationCount = 1
```

This demonstrates that preserving sector labels only and preserving every protected identity are different symmetry requirements.

### 3. Sector-preserving mass-operator freedom

A real symmetric operator on a six-dimensional ordinary block has

\[
\frac{6\cdot7}{2}=21
\]

parameters. A symmetric operator on a two-dimensional radiative block has

\[
\frac{2\cdot3}{2}=3.
\]

The sector-preserving family therefore has

\[
21+3=24
\]

free real parameters before additional physical constraints.

Wolfram returned:

```text
SectorPreservingSymmetricOperatorParameterCount = 24
```

### 4. Signature-preserving diagonal spectra

Under eight distinct protected identities, the diagonal mass-squared family retains eight independent entries:

\[
\mathcal M^2
=\operatorname{diag}(m_1^2,\ldots,m_8^2).
\]

Wolfram returned:

```text
SignaturePreservingDiagonalMassParameterCount = 8
DiagonalMassEigenvalues = {m[1]^2,...,m[8]^2}
DiagonalMassCommutesWithSector = True
DiagonalMassCommutesWithSignatures = True
```

This proves that identity preservation and sector preservation do not determine a unique spectrum.

## Interpretation

The computations establish exact underdetermination results:

- the parent sector split permits a large kinematic basis group;
- individual protected signatures reduce that freedom but do not supply a physical gauge law;
- many positive-semidefinite mass operators remain compatible with the inherited structure;
- no particle spectrum follows from the candidate count.

These results do not prove a microscopic action, probability law, gauge group, particle identity, mass hierarchy, or interaction theory.

## Independent analytic check

Each dimension count follows directly from:

\[
\dim\mathfrak{so}(n)=\frac{n(n-1)}2,
\qquad
\dim\operatorname{Sym}(n)=\frac{n(n+1)}2.
\]

For a generic diagonal matrix with distinct entries, commutation forces every off-diagonal matrix entry to vanish. This independently reproduces the diagonal commutant and trivial permutation stabilizer.

## Failure boundary

A favorable Wolfram eigensystem, named algebra, or fitted mass matrix cannot close Module C. The missing microscopic constitutive law must be derived from authorized RFC sources and the sealed parent, then checked by Wolfram and an independent formulation.