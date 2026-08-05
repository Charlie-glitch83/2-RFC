# Module Hᵁ — Linear Boltzmann Transfer-Operator Proof

## Theorem

Let `P_G->H^U` be an admitted, nonobstructed Module G branch with complete recombination, opacity, optical-depth, visibility, drag, collision, source, perturbation, dark-sector, field, covariance, memory, ancestry, and restart state. Let `B` belong to the frozen admissible background domain `D_B`. Let the enhanced completed Module A triad kernel and the frozen A–G law stack generate the finite operator `A_H^U(k,eta;B)` defined in `science/LINEAR_BOLTZMANN_TRANSFER_OPERATOR.md`.

Then, on every declared finite species, mode, momentum, multipole, wavenumber, and time refinement:

1. the linear initial-value problem has a unique solution;
2. scalar, vector, and tensor sectors remain separated unless a generated background or field source lawfully couples them;
3. gauge-related initial data remain gauge related, and physical quotient observables are gauge independent;
4. geometric, charge, normalization, and species constraints propagate;
5. collision and interaction blocks preserve their exact conserved charges and paired energy-momentum exchange;
6. photon intensity/polarization, matter, neutrino/free-streaming, compression-relic, dissipative-tail, field, and dark-sector blocks are complete at the declared refinement;
7. regular physical initial modes form a finite independent basis modulo gauge;
8. tight-coupling, fluid, free-streaming, and hierarchy reductions are lawful only inside their witnessed error domains and admit reopening;
9. the fundamental matrix obeys composition and restart identity;
10. line-of-sight responses reconstruct direct hierarchy responses within the frozen error bound;
11. covariance propagation preserves positive semidefiniteness for positive process covariance;
12. the frozen `P_H^U->I` packet is sufficient for Module I to derive a realized background and later instantiate H[I] without redesigning Hᵁ.

## Proof

### 1. Existence and uniqueness

On a finite declared refinement, `A_H^U(k,eta;B)` is a finite matrix whose coefficients are piecewise continuous by the definition of `D_B`. Standard finite-dimensional linear evolution therefore gives a unique fundamental matrix and unique inhomogeneous solution on each chart. Declared event maps concatenate the chart solutions.

### 2. Scalar, vector, and tensor typing

The generated harmonic projectors satisfy idempotence, orthogonality, and completeness. On a symmetry-preserving background, the linearized operator commutes with the sector projectors, so all off-diagonal sector blocks vanish. When an inherited anisotropy, field, defect, or event source breaks that symmetry, the nonzero cross-block is retained explicitly. Thus sector removal cannot occur by convenience.

### 3. Gauge covariance

Gauge covariance is encoded by

```text
A G - Gdot = G R.
```

If `deltaX_2 = deltaX_1 + G xi` initially and `xidot = R xi`, direct differentiation shows that the difference remains `G xi` at later times. The weighted physical projector annihilates `G` and is idempotent, so projected physical observables agree for gauge-related solutions.

### 4. Constraint propagation

The identity

```text
Cdot + C A = M C
```

implies

```text
d(C deltaX)/deta = M(C deltaX).
```

A zero initial constraint vector therefore remains zero. Continuous residual monitoring detects numerical or constitutive failure.

### 5. Conservation and collision balance

For every conserved left functional `ell_A`, each conserving internal collision block satisfies `ell_A^dagger C_r=0`. Paired sector exchange terms are equal and opposite. Hence the total conserved perturbative quantity has zero collision contribution. The geometry-interface contribution closes through the frozen linearized geometry/constraint law.

### 6. Completeness of species and hierarchy blocks

The relational Boltzmann graph contains every active species/mode/multipole/momentum/field variable admitted by the frozen parent and refinement witnesses. Module A promotion adds a missing carrier whenever it opens a material route or closes a conservation, source, covariance, or ancestry gap. The branch closes only after all claimed responses stabilize under refinement.

### 7. Initial-mode basis

The regular constrained initial data form the kernel of the finite leading-condition matrix. Quotienting the image of the gauge generator removes only pure gauge directions. Rank-revealing factorization on the physical quotient therefore yields a finite independent basis. Every physical regular initial state has a unique expansion in that basis.

### 8. Lawful reductions and reopening

A reduction is admitted only when projection and reconstruction preserve retained moments and every material observable residual is bounded. Stable fast-block elimination gives the Schur complement `A-B D^+ C`; hierarchy truncation approximates the exact omitted-tail resolvent. When an error or witness fails, Module A promotion restores the finer representation. Thus no accepted reduction permanently deletes material state.

### 9. Fundamental-matrix composition

Uniqueness of the linear initial-value problem implies that evolution from `eta_0` to `eta_2` equals evolution from `eta_0` to `eta_1` followed by evolution from `eta_1` to `eta_2`. Hence

```text
T(eta_2,eta_1) T(eta_1,eta_0) = T(eta_2,eta_0).
```

This is also the restart identity.

### 10. Direct and line-of-sight equivalence

The line-of-sight expression is the Duhamel solution after splitting the photon hierarchy into homogeneous propagation and generated source terms. Therefore, with exact propagation and quadrature, it equals the direct hierarchy solution. The implemented approximation is accepted only when the residual converges below the frozen tolerance under source, hierarchy, interpolation, time, and precision refinement.

### 11. Covariance positivity

For positive semidefinite initial covariance and process covariance,

```text
Sigma(eta)=T Sigma_i T^dagger + integral T Q T^dagger
```

is a sum of positive semidefinite matrices. Therefore propagated covariance remains positive semidefinite.

### 12. Child completeness and freeze

The export contains the operator family, admissible background domain, complete state and mode registries, gauge and constraint grammar, collision and source laws, all hierarchy/reduction rules, direct and line-of-sight solution grammars, Green functions, derivatives, covariance map, signatures, ancestry, memory, restart state, and immutable insertion map. Module I can therefore derive `B_I` against the declared domain without reconstructing or modifying Hᵁ.

This proves the theorem within the finite-relational, background-parameterized, linear-response boundary.

## Falsifiers and obstructions

Module Hᵁ fails on a branch if any mandatory condition occurs:

- incomplete species, sector, mode, collision, or source state;
- persistent gauge disagreement in physical observables;
- constraint or conservation drift beyond tolerance;
- nonregular or linearly dependent physical initial basis;
- uncontrolled tight-coupling, fluid, free-streaming, or hierarchy reduction;
- hierarchy-boundary reflection or nonconvergence;
- direct/line-of-sight disagreement beyond tolerance;
- unstable or acausal unclassified physical mode;
- negative covariance generated from positive inputs;
- need to redesign the operator after receipt of Module I background;
- inability to define a nonempty admissible background domain;
- incomplete `P_H^U->I`;
- public background, transfer, spectrum, peak, power, or likelihood information used to generate or select the operator.

A failure obstructs the branch. It does not authorize retuning Modules A–G or relaxing the public-data firewall.