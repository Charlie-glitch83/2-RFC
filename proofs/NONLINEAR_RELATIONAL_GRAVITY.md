# Module K — Nonlinear Relational Gravity Proof

## Theorem K.1 — No-rescale nonlinear promotion

Let `P_J->K(j)` be an admitted Module J branch with complete finite-volume fields, phases, species labels, covariance, constraints, and promotion surface. Let `Pi_J->K` preserve the declared field moments, long modes, phase identity, species ownership, metric state, covariance, and conserved quantities.

Then the promoted Module K state is physically equivalent to the Module J state on the overlap domain if and only if every mandatory overlap residual satisfies its frozen componentwise bound.

### Proof

The promotion map is defined as a representation change, not a new realization. Partition-of-unity loading preserves total mass and the constrained first and higher moments by construction. Phase and long-mode identity are copied from the sealed Fourier/harmonic realization. Gauge-invariant fields and constraints are evaluated before and after promotion. Therefore the two representations describe the same physical quotient precisely when all field, spectrum, constraint, covariance, and conservation residuals lie inside their declared bounds. Any amplitude rescaling, new phase draw, species reassignment, or hidden smoothing changes at least one invariant and violates equivalence. ∎

---

## Theorem K.2 — Local finite-N evolution between events

For a regular admitted branch with finite constituent number, locally Lipschitz route forces, nonsingular metric/interaction operators, and fixed active witness set, the finite-N Module K state has a unique local solution until the first event, singularity, obstruction, or representation boundary.

### Proof

The state equations form a finite first-order system with locally Lipschitz right-hand side on the regular branch domain. Picard–Lindelöf gives local existence and uniqueness. The maximal interval ends only when the solution exits that domain, which is represented by the event multifunction, a singularity, obstruction, or promotion/reopening boundary. ∎

---

## Theorem K.3 — Internal momentum and angular-momentum closure

Suppose every internal pair or route contribution satisfies equal-and-opposite force and zero net internal torque after inclusion of its field/metric carrier. Then total linear and angular momentum change only through declared boundary fluxes and external or inter-sector exchange.

### Proof

Summing pair forces cancels each internal contribution. Summing `x_i × F_ij + x_j × F_ji` vanishes for central pair terms; noncentral route terms are paired with the corresponding field/metric angular-momentum carrier. Thus only boundary and declared exchange terms remain. ∎

---

## Theorem K.4 — Vlasov and particle correspondence

Let a sequence of positive empirical phase-space measures converge weakly to `f_a`, with uniformly controlled relevant moments and forces converging on the declared domain. Then the particle representation converges to the Module K phase-space transport law before unresolved singular events.

### Proof

Weak convergence transfers bounded test-function moments. Force convergence and moment control permit passage to the weak transport equation. Route classes remain separately labeled, so convergence does not quotient physically independent streams. Failure of moment or force control triggers refinement or obstruction. ∎

---

## Theorem K.5 — Shell-crossing continuation

Let `x(q,t)` be a regular Lagrangian map before `t_e`, and suppose its Jacobian has a bracketed first rank loss at `(q_e,t_e)`. If the underlying phase-space sheet remains finite, then the Module K state continues uniquely as a multistream phase-space measure even though a single-valued velocity field fails.

### Proof

The Eulerian density representation becomes singular when the Jacobian vanishes, but the phase-space map `(q -> x,p)` remains a finite measure under the stated condition. Multiple preimages of one Eulerian position generate distinct streams. Because stream labels, orientation, route, and ancestry are retained, continuation is represented by the phase-space state rather than by an invalid single-stream closure. ∎

---

## Theorem K.6 — Caustic certification

A density maximum is a certified caustic only if accompanied by Jacobian/rank loss, stream multiplicity or orientation change, conservation closure, event bracketing, and ancestry continuity.

### Proof

A density maximum can arise from smoothing, sampling, or ordinary compression without a fold. The listed conditions identify the geometric phase-space singularity and distinguish it from numerical or single-stream compression. ∎

---

## Theorem K.7 — Bound-object sufficiency

A candidate is a qualified bound nonlinear object when it possesses persistent constituent or weighted membership, negative separation-relative energy or its lawful geometric replacement, bounded outward unbound flux, stable or classified oscillatory invariants, tidal consistency, constraint closure, and a reopening path.

### Proof

Negative separation-relative energy prevents immediate free separation in the stated domain. Bounded outward flux and persistent membership exclude transient catalogue adjacency. Stable/classified invariants and tidal consistency establish persistence relative to the environment. Constraint closure and reopening preserve physical validity and no-loss ancestry. A density threshold alone proves none of these. ∎

---

## Theorem K.8 — Event-truth ancestry

If every nonlinear interaction event is represented by a bracketed local witness with pre/post states and invariant-transfer ledger, then the directed event graph preserves object identity through merger, stripping, disruption, fragmentation, ejection, promotion, and reopening.

### Proof

The event edge explicitly maps progenitor identities and transferred invariants to remnants and debris. Composition of such edges gives a causal ancestry path. Temporary non-detection or representation change does not erase identity because restart and reopening pointers remain attached. ∎

---

## Theorem K.9 — Web and void no-loss classification

A web or void feature retained across an admitted filtration/refinement interval with attached classifier covariance is a stable topological object at that declared resolution. Disagreement among lawful classifiers remains branch/covariance information rather than a contradiction.

### Proof

Persistent features survive the specified perturbation of filtration or resolution. Since classifiers probe different physical projections, equality is not required. Retaining method identity and covariance prevents false uniqueness while preserving the common resolved feature. ∎

---

## Theorem K.10 — Nonlinear sector conservation

Let every ordinary, compression-relic, dissipative-tail, neutrino, radiation, field, and returned-sector exchange be represented by typed currents `Q_s^mu` satisfying `sum_s Q_s^mu = 0`. Then total stress-energy is conserved up to declared domain-boundary and gravitational-radiative flux.

### Proof

Summing the sector balance laws cancels all internal exchange currents. The remaining terms are precisely the declared boundary and gravitational-radiative carriers. Unnamed exchange would violate the identity and obstruct the branch. ∎

---

## Theorem K.11 — Lensing is geometry-derived

Given the generated nonlinear metric or lawful geometric replacement, direct ray transport and Jacobi transport describe the same first-order neighboring-ray map on their common regular domain.

### Proof

The Jacobi equation is the linearization of the geodesic deviation map about the reference ray. Therefore its solution equals the derivative of the direct geodesic flow with respect to initial screen displacement, provided both use the same metric, tetrad, affine convention, and boundary data. Disagreement beyond numerical error signals an implementation or domain failure. ∎

---

## Theorem K.12 — Covariance positivity under nonlinear tangent propagation

For tangent map `J_K` and positive-semidefinite parent covariance `Sigma_J`, the deterministic pushforward `J_K Sigma_J J_K^T` is positive semidefinite. Adding independently justified positive-semidefinite process and representation covariance preserves positivity.

### Proof

For every vector `v`, `v^T J_K Sigma_J J_K^T v = (J_K^T v)^T Sigma_J (J_K^T v) >= 0`. The sum of positive-semidefinite matrices is positive semidefinite. ∎

---

## Theorem K.13 — Restart composition

For deterministic evolution between the same ordered event surfaces, exact checkpoint state and solver identity imply

`Phi(t3,t1) = Phi(t3,t2) o Phi(t2,t1)`.

### Proof

Uniqueness on each regular branch makes both sides the same solution through the same checkpoint state. Event, branch, refinement, and representation state are part of the checkpoint; omitting them invalidates the premise. ∎

---

## Theorem K.14 — First-pass Module L sufficiency

If `P_K->L^(0)` contains the complete nonlinear geometry, force/metric, phase-space, species/sector, baryonic gravity, dark/relic sectors, objects, web/voids, event graph, tides, collapse candidates, refinement, strong-field boundaries, lensing/lightcones, constraints, covariance, memory, ancestry, and restart state, then Module L can begin without reconstructing gravitational physics.

### Proof

These fields cover every gravitational parent variable required by the sealed K→L handoff. Module L may derive baryonic response but need not invent geometry, environments, object identity, phase space, events, or gravitational uncertainty. ∎

---

## Theorem K.15 — K–L–M closure classification

Let the completed return map be `F_KLM`. A fixed point is certified only when the full physically weighted residual vanishes within every mandatory component bound. A bounded cycle, attractor, branch set, or nonconvergence is retained when witnessed instead.

### Proof

A fixed point requires equality of the full returned state, not a selected scalar. Componentwise bounds prevent averaging away a failed geometry, sector, object, topology, event, lensing, conservation, or covariance condition. Spectral-radius or nonlinear stability analysis classifies local fixed-point behavior; event and branch analysis handles cycles, attractors, bifurcations, and nonconvergence. Artificial damping changes the physical map and is forbidden. ∎

---

## Module K completion theorem

Under the named regularity, finite-support, representation-overlap, conservation, event, stability, and numerical-convergence assumptions, Module K constructs one complete first-pass nonlinear gravitational state `K^(0)` from the immutable Module J parent and exports a sufficient restartable state to Module L without empirical tuning or identity loss.

This theorem does not claim final K–L–M closure. Final `K*` remains pending Modules L and M and classification of their coupled recurrence.