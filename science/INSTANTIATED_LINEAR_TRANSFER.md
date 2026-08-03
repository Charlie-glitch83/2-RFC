# Module H[I] — Immutable Instantiation on the Realized Module I Background

## 1. Protected operation

Module H[I] begins only after Module I proves

\[
\mathcal B_I\in\mathcal D_{\mathcal B},
\]

where \(\mathcal D_{\mathcal B}\) and the operator family \(\mathbb B_{\mathrm{RFC}}[\mathcal B]\) were frozen in Module Hᵁ before Module I existed.

The only lawful operation is

\[
\boxed{
\mathbb B_{H[I]}
=\operatorname{Instantiate}
\left(\mathbb B_{\mathrm{RFC}}[\mathcal B],\mathcal B_I\right).
}
\]

Instantiation replaces typed background placeholders by realized Module I coefficient histories. It does not redesign the operator.

---

## 2. Immutable parent pair

The two immutable parents are:

\[
P_{H[I],\mathrm{in}}
=(P_{H^U}^{\mathrm{op}},P_I^{\mathrm{bg}}).
\]

The Hᵁ parent fixes:

- perturbation-state dimension;
- species and sector identities;
- scalar/vector/tensor, helicity, and parity decomposition;
- gauge transformations and gauge-invariant observables;
- geometric and species constraints;
- collision and momentum-transfer forms;
- photon, polarization, matter, neutrino, free-streaming, compression-relic, dissipative-tail, field, and dark hierarchies;
- initial-mode basis and normalization;
- tight-coupling, fluid, free-streaming, truncation, and switching rules;
- direct hierarchy, line-of-sight, Green-function, derivative, covariance, and uncertainty grammar;
- scientific tolerances, falsifiers, and operator identity.

The Module I parent supplies:

- realized geometry, clocks, coordinates, scale, expansion, curvature, topology, anisotropy, and averaging state;
- ordinary, radiative, relic, compression-relic, dissipative-tail, field, defect, and transfer histories;
- recombination-facing background functions required by Hᵁ;
- event, horizon, redshift, distance, derivative, interpolation, covariance, branch, memory, ancestry, and restart state;
- the Hᵁ domain-compliance result.

Neither parent may be reconstructed or altered inside H[I].

---

## 3. Deterministic coefficient insertion

Let the frozen Hᵁ operator be

\[
\frac{d}{d\eta}\delta X
=\mathbb A_H(k,\eta;\mathcal B)\delta X
+\mathbb S_H(k,\eta;\mathcal B)u.
\]

The insertion map is

\[
\mathcal I_H:\mathcal B_I
\mapsto
\{C_a[\mathcal B_I]\}_{a\in\mathcal A_H},
\]

where \(\mathcal A_H\) is the frozen coefficient-address registry.

Thus

\[
\boxed{
\mathbb A_{H[I]}(k,\eta)
=\mathbb A_H(k,\eta;\mathcal B_I),
\qquad
\mathbb S_{H[I]}(k,\eta)
=\mathbb S_H(k,\eta;\mathcal B_I).
}
\]

Only predeclared slots may be populated. Missing slots, unit mismatch, derivative mismatch, out-of-domain extrapolation, or structural sparsity change obstructs instantiation.

---

## 4. Structural invariance

Define the operator grammar signature

\[
\mathfrak S_H
=(\dim X_H,\mathrm{sparsity},\mathrm{block\ types},\mathrm{mode\ basis},
\mathrm{gauge},\mathrm{constraints},\mathrm{collisions},\mathrm{sources},
\mathrm{closures},\mathrm{switches},\mathrm{tolerances}).
\]

H[I] requires

\[
\boxed{
\mathfrak S_{H[I]}=\mathfrak S_{H^U}.
}
\]

Realized coefficient values may change with time and branch. The scientific grammar may not.

---

## 5. Basis-normalized responses

For every frozen unit mode \(e_A(k)\), define the direct response

\[
\delta X_A(k,\eta)
=\mathbb T_{H[I]}(k;\eta,\eta_i)e_A(k),
\]

where

\[
\frac{\partial}{\partial\eta}\mathbb T_{H[I]}
=\mathbb A_{H[I]}\mathbb T_{H[I]},
\qquad
\mathbb T_{H[I]}(\eta_i,\eta_i)=I.
\]

For projection \(P_X\),

\[
T_X^A(k,\eta)=P_X\mathbb T_{H[I]}e_A.
\]

The response registry contains, where active:

- photon temperature/intensity and E/B polarization responses;
- baryon density, velocity, pressure, and stress;
- ordinary-matter responses;
- neutrino and free-streaming multipoles;
- compression-relic and dissipative-tail density, velocity, pressure, sound, and stress responses;
- scalar, vector, tensor, curvature, entropy, relative-velocity, field, defect, and memory-mode responses;
- metric, Weyl, slip, lensing-source, and integrated-source responses;
- scale-dependent growth and velocity-divergence responses;
- direct hierarchy and line-of-sight histories;
- response Jacobians and Green functions;
- covariance and numerical diagnostics.

No primordial amplitudes or mode mixture are assigned. Those belong to Module J.

---

## 6. Gauge, constraint, and conservation closure

The frozen gauge-covariance identity and physical projector remain unchanged after insertion. H[I] verifies:

\[
\mathbb A_{H[I]}\mathbb G_H-\dot{\mathbb G}_H
=\mathbb G_HR_H,
\]

\[
\dot{\mathbb C}_H+\mathbb C_H\mathbb A_{H[I]}
=\mathbb M_H\mathbb C_H,
\]

and all frozen collision-conservation left-null identities.

Gauge-invariant observables must agree across the frozen alternate formulations. Local species/mode/event residuals remain visible; no integrated average can hide a failed condition.

---

## 7. Direct and line-of-sight equivalence

For every mandatory radiative channel,

\[
\Delta_{\ell,\mathrm{LOS}}^{X,A}
=\int d\eta\,
\mathcal P_\ell^X[\mathcal B_I]\,S_X^A[\mathcal B_I],
\]

is compared with the direct hierarchy response.

The residual

\[
\mathcal R_{\mathrm{LOS}}^{X,A}
=\Delta_{\ell,\mathrm{direct}}^{X,A}
-\Delta_{\ell,\mathrm{LOS}}^{X,A}
\]

must remain below the frozen Hᵁ tolerance under hierarchy, time, interpolation, source, and precision refinement.

---

## 8. Restart and composition

For lawful checkpoints,

\[
\mathbb T(\eta_3,\eta_1)
=\mathbb T(\eta_3,\eta_2)\mathbb T(\eta_2,\eta_1)
\]

within frozen numerical bounds.

Restart identity includes state vectors, phase, normalization, constraints, hierarchy state, stiff-regime state, source histories, branch, covariance, memory, and ancestry.

---

## 9. Covariance map

For any later Module J primordial covariance \(\Sigma_J^{\mathrm{prim}}\), H[I] supplies the frozen propagation map

\[
\Sigma_X
=\mathbb T_{H[I]}\Sigma_J^{\mathrm{prim}}
\mathbb T_{H[I]}^\dagger
+\Sigma_{H[I],\mathrm{proc}}.
\]

Before Module J supplies that covariance, H[I] exports only basis-response covariance, background-response derivatives, and numerical/physical uncertainty operators.

The background contribution is propagated from \(\Sigma_I\) through the frozen response derivative schema.

---

## 10. Complete H[I] export to Module J

Define

\[
\boxed{
P_{H[I]\to J}
=(\mathrm{OperatorIdentity}_{H^U},\mathrm{BackgroundIdentity}_I,
\mathrm{InstantiationIdentity}_{H[I]},\mathrm{DomainCompliance}_I,
\mathrm{ModeBasis}_H,\mathrm{UnitResponses}_{H[I]},
\mathrm{SpeciesTransfer}_{H[I]},\mathrm{MetricTransfer}_{H[I]},
\mathrm{PhotonTransfer}_{H[I]},\mathrm{PolarizationTransfer}_{H[I]},
\mathrm{GrowthResponse}_{H[I]},\mathrm{DirectHierarchy}_{H[I]},
\mathrm{LOSResponse}_{H[I]},\mathrm{Green}_{H[I]},
\mathrm{ResponseDerivative}_{H[I]},\mathrm{CovarianceMap}_{H[I]},
\mathrm{Constraint}_{H[I]},\mathrm{Conservation}_{H[I]},
\mathrm{Gauge}_{H[I]},\mathrm{Approximation}_{H[I]},
\mathrm{Signature}_{H[I]},\mathrm{Memory}_{H[I]},
\mathrm{Ancestry}_{H[I]},\mathrm{Restart}_{H[I]}).
}
\]

Module J may combine these basis-normalized responses with an internally derived primordial covariance. It may not reconstruct missing H[I] physics.

---

## 11. Claim boundary

H[I] establishes:

- deterministic instantiation of the frozen Hᵁ operator on the compliant Module I background;
- exact preservation of operator grammar;
- basis-normalized direct, Green-function, and line-of-sight response definitions;
- realized species, metric, radiative, polarization, dark-sector, and growth-response histories at the frozen linear scope;
- gauge, constraint, conservation, restart, approximation, derivative, covariance, memory, and ancestry closure;
- complete `P_H[I]->J`.

H[I] does not establish:

- primordial mode amplitudes or covariance;
- realized stochastic spectra;
- observed CMB or matter spectra;
- fitted normalization, tilt, running, tensor ratio, or mode mixture;
- nonlinear structure;
- public Boltzmann-code agreement;
- empirical validation.

Within these boundaries, **H[I] is complete and frozen** once the instantiated operator passes the frozen Module H checks. Module J is then active.