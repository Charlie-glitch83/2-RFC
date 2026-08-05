# Module H[I] — Immutable Instantiation Proof

## Theorem

Let `P_H^U^op` be the frozen Module Hᵁ operator packet, let `B_I` be a realized Module I background satisfying `B_I in D_B`, and let `Instantiate` be the frozen background insertion map.

Then:

1. `B_H[I] = Instantiate(B_RFC, B_I)` preserves the Hᵁ state dimension, equation grammar, mode basis, gauges, constraints, collisions, hierarchies, source grammar, truncation laws, tolerances, uncertainty model, and intrinsic signatures;
2. every coefficient history in H[I] is supplied by the Module I background packet or by a frozen upstream Module G history explicitly retained by Hᵁ;
3. the instantiated system has a unique finite-refinement solution on every regular branch interval;
4. gauge covariance, propagated constraints, collision balance, conservation, transfer composition, and restart identity remain valid;
5. direct hierarchy and line-of-sight responses are two formulations of the same frozen operator and must agree within their frozen channel tolerances;
6. the exported basis-normalized responses are sufficient for Module J without assigning primordial amplitudes or covariance.

## Proof

### Structural invariance

The insertion map acts only on typed coefficient slots. It does not act on the operator graph, state vector, mode basis, gauge maps, constraint maps, hierarchy layout, collision forms, or source definitions. Therefore the structural hash before and after insertion is identical.

### Existence and uniqueness

Because `B_I in D_B`, all required coefficient histories are complete, bounded, piecewise differentiable, and represented at the frozen sampling/interpolation accuracy. The instantiated finite linear system therefore has a unique propagator on each regular interval.

### Gauge and constraints

The Hᵁ identities

```text
A G - Gdot = G R
Cdot + C A = M C
```

are algebraic-functional identities over the admissible background domain. Substitution of a compliant `B_I` preserves them, so gauge-related states remain gauge related and initially satisfied constraints remain satisfied.

### Conservation

The frozen left invariants of every collision and transfer block remain left invariants after coefficient substitution because instantiation changes coefficient histories but not the route pairing or operator form. Hence energy, momentum, charge, number, and compensation conditions close subject to their declared route assumptions.

### Transfer composition

The unique fundamental matrix of the instantiated linear system obeys

```text
T(eta3,eta1) = T(eta3,eta2) T(eta2,eta1).
```

This also proves split/restart identity when the complete state, branch, approximation, covariance, and ancestry packet is restored.

### Direct and line-of-sight equivalence

The line-of-sight representation follows by Duhamel decomposition of the same instantiated photon hierarchy. Therefore exact formulations agree. Any numerical disagreement above the frozen tolerance is an implementation or representation obstruction.

### Covariance

Linear pushforward of positive-semidefinite parent covariance remains positive semidefinite. Adding positive-semidefinite discretization, truncation, interpolation, switch, solver, and branch contributions preserves this property.

### Child sufficiency

H[I] exports the complete frozen mode basis, direct and line-of-sight unit responses, species and metric transfers, Green functions, source kernels, Jacobians, covariance maps, diagnostics, branch, memory, ancestry, and restart state. Module J therefore needs only to derive primordial covariance and perform the lawful contraction; it does not need to reconstruct Module I or H physics.

This proves the theorem within the finite-relational, realized-background, linear-response boundary.

## Obstructions

H[I] is obstructed if:

- `B_I` fails any Hᵁ domain condition;
- the operator structural identity changes;
- an undeclared coefficient or public input enters;
- gauge, constraint, conservation, restart, hierarchy, or direct/LOS closure fails;
- an independent mode is removed or renormalized after instantiation;
- a branch is selected for observational resemblance;
- primordial covariance or final spectra are inserted inside H[I].