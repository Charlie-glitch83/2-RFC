# Module Hᵁ — Universal Linear Boltzmann Dynamics and Transfer-Operator Closure

## 1. Scientific boundary

Modules A through G are complete and frozen. Module H has two protected phases:

```text
G -> Hᵁ -> I -> H[I] -> J
```

This file completes only the first phase, **Module Hᵁ**. It constructs and freezes the background-parameterized linear response operator before Module I supplies the realized RFC background.

Module Hᵁ consumes the sealed branch-specific parent

\[
P_{G\to H^U}(\gamma_G)
=(\mathrm{Identity}_G,\mathrm{Coord}_G,\mathrm{GeometrySchema}_G,
\mathrm{Sector}_G,\mathrm{Species}_G,\mathrm{Thermo}_G,\mathrm{Recomb}_G,
\mathrm{Atomic}_G,\mathrm{Photon}_G,\mathrm{Polarization}_G,\mathrm{Neutrino}_G,
\mathrm{Opacity}_G,\mathrm{OpticalDepth}_G,\mathrm{Visibility}_G,
\mathrm{LastScattering}_G,\mathrm{Drag}_G,\mathrm{Acoustic}_G,
\mathrm{Diffusion}_G,\mathrm{Damping}_G,\mathrm{Collision}_G,
\mathrm{Source}_G,\mathrm{PerturbationSeed}_G,\mathrm{MetricInterface}_G,
\mathrm{Dark}_G,\mathrm{Field}_G,\Sigma_G,\mathrm{Memory}_G,
\mathrm{Ancestry}_G,\mathrm{Restart}_G).
\]

The completed Hᵁ theorem is:

> Given an admitted Module G branch, the enhanced completed Module A triad kernel, the frozen A–G physical law stack, and a typed background placeholder in a declared admissible domain, RFC derives a finite-refinement, background-parameterized, multi-species linear perturbation operator. The operator preserves gauge equivalence, physical constraints, collision balance, species and route identity, scalar/vector/tensor typing, recombination ancestry, uncertainty, covariance, memory, and restart structure; generates a complete regular unit-mode basis, direct hierarchy propagator, stiff-regime and asymptotic reductions, line-of-sight source grammar, Green-function and response-derivative grammar; and is frozen before Module I supplies the realized background. Module I may later instantiate the operator only through the declared insertion map.

The result is complete at a **finite-relational, background-parameterized, linear-response scope**. It does not yet contain the realized Module I background, instantiated transfer histories, primordial covariance, final spectra, nonlinear structure, late reionization, or empirical comparison.

---

## 2. Enhanced completed Module A kernel

Every Hᵁ object descends from the enhanced completed Module A kernel

\[
\widehat{\mathcal K}_{A}(\tau)
=
\sum_{j=1}^{n_A}
\sum_{[r]\in\mathcal A_A(\tau)}
\delta^{-j}e^{-\alpha j\tau}
W_{j,[r]}(\tau)\Phi_{j,[r]}(\tau).
\]

The inherited kernel carries:

- the ordered primitive triad \((CIF,QV,RFL)\);
- the First Action \(QV(CIF)\to RFL\);
- recursive depth, damping, modal structure, and bounded tails;
- directed relations, route classes, and local witnesses;
- event lift, inverse/conjugate routes, and legal incidence;
- no-loss quotienting;
- branch and obstruction laws;
- protected identity, memory, promotion, refinement, and reopening;
- uncertainty and covariance;
- terminal N-body relational and solution-generating completion.

The terminal N-body carrier is active in the multi-species perturbation graph, collision and momentum-transfer edges, angular/momentum hierarchies, mode and route refinement, field/geometry coupling, and transfer composition. Where no linear physical witness exists, the carrier remains dormant, information-bearing, unchanged, and nonbackreacting.

---

## 3. Module Hᵁ triadic specialization

Define

\[
CIF_{H^U}
=\Phi_{H^U}(P_{G\to H^U},\widehat{\mathcal K}_A,M_G),
\]

\[
QV_{H^U}
=\Psi_{H^U}(CIF_{H^U},P_{G\to H^U},\widehat{\mathcal K}_A,\mathcal B),
\]

\[
RFL_{H^U}
=\Omega_{H^U}(QV_{H^U},P_{G\to H^U},\widehat{\mathcal K}_A),
\]

\[
H_{H^U}
=\Gamma_{H^U}(CIF_{H^U},QV_{H^U},RFL_{H^U},P_{G\to H^U},\widehat{\mathcal K}_A).
\]

The roles are indispensable:

- **CIF\(_{H^U}\)** opens the complete lawful perturbation-state, mode, gauge, species, route, collision, source, background-domain, and propagation possibility space;
- **QV\(_{H^U}\)** performs linearization, gauge/constraint selection, collision and transport evolution, stiff-regime reduction, hierarchy refinement, source projection, and branch/obstruction resolution;
- **RFL\(_{H^U}\)** stabilizes the frozen operator family, admissible background domain, unit-mode basis, direct/line-of-sight grammar, uncertainty map, memory, ancestry, and Module I export.

The triad is not a scalar modulation of a public Boltzmann solution.

---

## 4. Typed background placeholder

Module Hᵁ does not receive the realized Module I background. It defines the typed placeholder

\[
\mathcal B
=(a,\mathcal H,t,\eta,g_{\mu\nu}^{(0)},K^{(0)},
\{\rho_s,p_s,w_s,c_{a,s}^2,\pi_s\}_s,
\{\Gamma_r\}_r,\mathcal D_{\mathrm{dark}},\mathcal U),
\]

where every component has a fixed dimensional type, differentiability class, species/sector identity, event-surface rule, covariance slot, and insertion address.

The admissible background domain \(\mathcal D_{\mathcal B}\) contains only packets satisfying:

1. complete required variables and dimensions;
2. monotone physical and conformal clocks on each declared chart;
3. positive scale/volume carrier and nondegenerate background geometry;
4. piecewise \(C^1\) coefficient histories, with declared event jumps and matching maps;
5. finite densities, pressures, interaction rates, and required derivatives;
6. exact total background conservation and active sector-transfer closure;
7. positive distribution support and lawful species identities;
8. stable/hyperbolic constitutive blocks over the claimed domain;
9. bounded opacity, collision, source, and interpolation operators;
10. explicit curvature, horizon, anisotropy, and dark-sector status;
11. no unresolved singular transition inside an integration chart;
12. sampling/interpolation errors below the frozen Hᵁ bound.

Module I must later prove

\[
\mathcal B_I\in\mathcal D_{\mathcal B}.
\]

If it does not, the result is a domain obstruction. Hᵁ may not be silently redesigned.

---

## 5. Parent nonlinear state and exact linearization

Let \(X\) denote the complete A–G physical state restricted to the linear-transfer domain, and let

\[
\frac{dX}{d\eta}=\mathcal F_{A:G}(X;\mathcal B)
\]

be the frozen finite-relational evolution assembled from the inherited geometry, species, collision, recombination, field, dark, memory, and event laws.

For an admissible background trajectory \(\bar X(\eta;\mathcal B)\), write

\[
X=\bar X+\varepsilon\,\delta X+O(\varepsilon^2).
\]

The universal linear operator is the Fréchet derivative

\[
\boxed{
\mathbb A_{H^U}(k,\eta;\mathcal B)
=
D_X\mathcal F_{A:G}[\bar X(\eta;\mathcal B)]
}
\]

after Fourier/harmonic decomposition on the declared relational geometry.

The complete linear system is

\[
\boxed{
\frac{d}{d\eta}\delta X(k,\eta)
=
\mathbb A_{H^U}(k,\eta;\mathcal B)\delta X(k,\eta)
+\mathbb S_{H^U}(k,\eta;\mathcal B)u(k,\eta).
}
\]

Here \(u\) contains only inherited event, defect, field, or externally timed **internal RFC** source carriers already authorized by Modules A–G. It contains no public forcing or target spectrum.

This derivative construction prevents Module Hᵁ from importing an independent conventional perturbation engine.

---

## 6. Complete perturbation state

For each \((k,\eta)\), define

\[
\delta X
=
\left(
\delta g,
\delta T,
\delta f_\gamma,
\delta f_\nu,
\delta f_b,
\delta f_{\mathrm{cr}},
\delta f_{\mathrm{dt}},
\delta f_{\mathrm{other}},
\delta\mathcal E,
\delta M
\right).
\]

Every component carries:

- physical and dimensional definition;
- scalar/vector/tensor and helicity/parity type;
- gauge transformation rule;
- species and sector identity;
- collision and source partners;
- conservation role;
- numerical representation and refinement index;
- uncertainty/covariance slot;
- route, event, source, scale, and recursive ancestry;
- export status.

No active species is represented only by its background density when its perturbations materially affect the operator.

---

## 7. Scalar, vector, and tensor decomposition

Let \(P_S,P_V,P_T\) be the generated harmonic projectors. They satisfy

\[
P_A^2=P_A,
\qquad
P_AP_B=0\ (A\ne B),
\qquad
P_S+P_V+P_T=I
\]

on the complete linear state.

Thus

\[
\delta X
=\delta X^{(S)}\oplus\delta X^{(V)}\oplus\delta X^{(T)}.
\]

For a symmetry-preserving background,

\[
P_A\mathbb A_{H^U}P_B=0
\qquad(A\ne B).
\]

If the generated RFC background, field, defect, anisotropy, or event state breaks that decoupling, the nonzero cross-blocks remain explicit and branch typed.

A sector is removed only when its source and homogeneous regular solution spaces are both proved immaterial over the claimed domain.

---

## 8. Gauge constitution and physical quotient

Let \(\xi\) be the finite gauge-generator vector and

\[
\delta X\mapsto\delta X+\mathbb G_H\xi
\]

the linear gauge action.

With positive state metric \(W_H\), define the weighted physical projector

\[
\boxed{
P_{\mathrm{phys}}
=I-\mathbb G_H
(\mathbb G_H^\dagger W_H\mathbb G_H)^+
\mathbb G_H^\dagger W_H.
}
\]

It satisfies

\[
P_{\mathrm{phys}}\mathbb G_H=0,
\qquad
P_{\mathrm{phys}}^2=P_{\mathrm{phys}}.
\]

Gauge covariance of the evolution requires an operator \(R_H\) such that

\[
\boxed{
\mathbb A_{H^U}\mathbb G_H-\dot{\mathbb G}_H
=\mathbb G_HR_H.
}
\]

Then gauge-related initial data remain gauge related, and all physical claims are made using

\[
\delta X_{\mathrm{phys}}=P_{\mathrm{phys}}\delta X
\]

or an independently reconstructed gauge-invariant observable registry.

At least one evolution gauge and one alternate gauge or gauge-invariant formulation are frozen for verification. Gauge reduction is a no-loss quotient, not deletion of physical modes.

---

## 9. Constraints and their propagation

Let

\[
\mathbb C_H(\eta,k;\mathcal B)\delta X=0
\]

collect the linearized geometric, charge, momentum, normalization, and species constraints.

Constraint propagation is built into Hᵁ by requiring a finite operator \(\mathbb M_H\) with

\[
\boxed{
\dot{\mathbb C}_H+\mathbb C_H\mathbb A_{H^U}
=\mathbb M_H\mathbb C_H.
}
\]

Therefore any initially constrained solution remains constrained:

\[
\mathbb C_H\delta X(\eta_i)=0
\Longrightarrow
\mathbb C_H\delta X(\eta)=0.
\]

Constraint residuals are monitored continuously. Gauge conditions are never used to hide an unclosed physical constraint.

---

## 10. Conservation and collision balance

Let \(Q_A\) be a conserved charge or stress-energy moment and \(\ell_A^\dagger\) its left linear functional. For every internal collision/interaction block \(\mathbb C_r\),

\[
\ell_A^\dagger\mathbb C_r=0
\]

when route \(r\) conserves \(Q_A\).

For transfer between sectors \(s\) and \(u\),

\[
\delta J_{s\to u}=-\delta J_{u\to s}.
\]

The total perturbative stress-energy interface is

\[
\delta T^{\mu}{}_{\nu,\mathrm{tot}}
=\sum_s\delta T^{\mu}{}_{\nu,s},
\]

and its divergence/constraint relation is inherited from the linearized frozen geometry law.

The collision and transfer registry therefore preserves:

- species number where physically conserved;
- electric and other generated charges;
- total energy and momentum;
- photon-number conditions for elastic routes;
- route and source ancestry;
- branch probability and covariance typing.

---

## 11. Relational Boltzmann graph

At refinement \(N\), define the directed sparse graph

\[
\mathcal G_H^{(N)}
=(V_H^{(N)},E_H^{(N)},\mathcal H_H^{(N)}),
\]

where vertices are species/mode/multipole/momentum/field variables and edges/hyperedges are generated streaming, collision, geometry, source, and transfer couplings.

The operator is the graph realization

\[
\mathbb A_{H^U}^{(N)}
=\mathbb A_{\mathrm{stream}}^{(N)}
+\mathbb A_{\mathrm{geom}}^{(N)}
+\mathbb A_{\mathrm{coll}}^{(N)}
+\mathbb A_{\mathrm{dark}}^{(N)}
+\mathbb A_{\mathrm{field}}^{(N)}.
\]

Every nonzero block carries a parent law, witness, route class, units, domain, branch, covariance, and reopening map. No edge is added because it improves a later public comparison.

---

## 12. Photon intensity and polarization hierarchies

Using the Module G photon angular/polarization basis, write

\[
\delta f_\gamma(k,q,\hat n,\eta)
=\sum_{\ell,m,p}
F_{\gamma,\ell mp}(k,q,\eta)\,\mathcal Y_{\ell mp}(\hat n).
\]

The finite hierarchy is

\[
\boxed{
\dot{\mathbf F}_\gamma
=\mathbb S_\gamma(k,\mathcal B)\mathbf F_\gamma
+\mathbb C_\gamma[\mathrm{Opacity}_G,\mathrm{Drag}_G,\mathrm{Polarization}_G]\mathbf F_\gamma
+\mathbb G_\gamma\delta g
+\mathbf s_\gamma^G.
}
\]

The collision block is inherited from Module G’s generated electron, opacity, visibility, line/scattering, and polarization state. It is not replaced by a public optical-depth template.

The hierarchy preserves:

- intensity and polarization state;
- finite-width visibility sources;
- temperature, velocity, quadrupole, spectral, and field sources;
- elastic collision invariants;
- angular selection and parity/helicity rules;
- recombination and last-scattering ancestry;
- truncation and covariance data.

E- and B-type polarization are retained wherever generated by the harmonic/parity decomposition. A B/vector/tensor branch is dormant only when its source and homogeneous response are proved absent or immaterial.

---

## 13. Baryon, charged-matter, and neutral-matter blocks

For each material species or lawful fluid reduction, define density, momentum, pressure, entropy, anisotropic stress, composition, and charge moments by projections of its inherited distribution.

The species block is

\[
\dot{\mathbf U}_s
=\mathbb A_s[\mathcal B]\mathbf U_s
+\sum_u\mathbb C_{su}[P_{G\to H^U}]\mathbf U_u
+\mathbb G_s\delta g
+\mathbf s_s.
\]

Baryon/photon drag, electron-ion locking, residual charge separation, viscosity, conduction, and diffusion use the generated Module F/G operators.

A single-fluid reduction is admitted only when the full kinetic/multifluid block and its Schur complement agree within the frozen error bound. Otherwise separate velocity, temperature, stress, composition, and charge variables remain active.

---

## 14. Neutrino and free-streaming hierarchies

For each generated neutrino or other free-streaming branch,

\[
\delta f_s(k,q,\mu,\eta)
=\sum_{\ell}(-i)^\ell(2\ell+1)
F_{s\ell}(k,q,\eta)P_\ell(\mu).
\]

The hierarchy is

\[
\dot{\mathbf F}_s
=\mathbb S_s(k,q,\mathcal B)\mathbf F_s
+\mathbb C_s[P_{G\to H^U}]\mathbf F_s
+\mathbb G_s\delta g.
\]

Momentum integration must reconstruct the density, velocity, pressure, and anisotropic stress used by the metric/constraint blocks.

Massless, massive-transition, collisional, and free-streaming limits are generated from the inherited dispersion and interaction laws. A fixed public neutrino hierarchy or mass prescription is not imported.

---

## 15. Compression-relic and dissipative-tail perturbations

The compression-relic and dissipative-tail sectors retain distinct Module B ancestry and constitutive laws.

Their perturbation operators are the Fréchet derivatives of their frozen upstream evolution:

\[
\mathbb A_{\mathrm{cr}}
=D\mathcal F_{\mathrm{cr}}[\bar X;\mathcal B],
\qquad
\mathbb A_{\mathrm{dt}}
=D\mathcal F_{\mathrm{dt}}[\bar X;\mathcal B].
\]

The active state may include density, momentum, pressure, entropy, stress, internal field, memory, and exchange variables only where generated.

Module Hᵁ does not insert a cold-fluid compression relic or constant-equation-of-state tail. Clustering, smoothness, sound/propagation speed, anisotropic stress, stability, causality, and visible coupling are consequences of the inherited operators.

If a sector has zero witnessed perturbative backreaction in the admitted domain, that zero is recorded rather than silently omitting the sector.

---

## 16. Initial-mode basis

At the initial surface \(\eta_i\), let \(\mathbb L_i(k;\mathcal B)\) collect the leading regularity, constraint, collision-dominated, and gauge conditions.

The physical regular mode space is

\[
\mathcal M_i
=\ker\mathbb L_i\,/\,\operatorname{im}\mathbb G_H(\eta_i).
\]

Choose a weighted orthonormal basis

\[
E_H(k)=\{e_A(k)\}_{A=1}^{d_i}
\]

by rank-revealing factorization on the physical quotient.

Every mode records:

- scalar/vector/tensor, helicity, and parity type;
- regularity order and remainder bound;
- gauge behavior and gauge-invariant content;
- active species/sector support;
- adiabatic, entropy, compensated, relative-velocity, field, defect, or route-specific interpretation where derived;
- unit normalization and phase convention;
- branch, source, route, and recursive ancestry;
- lawful cross-correlation partners for later Module J use.

Module Hᵁ freezes the basis but does not choose the realized primordial covariance or mode mixture.

---

## 17. Superhorizon and early-time series

For each basis mode, seek a regular series

\[
\delta X_A(k,\eta)
=\sum_{n=0}^{N_s}x_{A,n}(k)(\eta-\eta_i)^n
+R_{A,N_s+1}.
\]

The coefficients solve the order-by-order operator and constraint equations generated from \(\mathbb A_{H^U}\), including collision-dominated and massive-species limits.

The initialization packet contains:

- coefficient recursion;
- gauge-mode removal;
- constraint residual by order;
- regularity and branch conditions;
- truncation remainder bound;
- matching point and overlap with direct integration;
- covariance and ancestry.

Series coefficients are not copied from a public model when the RFC sector or geometry laws differ.

---

## 18. Tight-coupling and other stiff-regime reductions

Partition the state into slow and fast variables:

\[
\frac{d}{d\eta}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}A&B\\C&D/\varepsilon\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}.
\]

When the generated fast block is stable and invertible on its physical subspace, the leading reduced operator is

\[
\boxed{
A_{\mathrm{eff}}=A-BD^+C.
}
\]

The controlled expansion is generated recursively in \(\varepsilon\), where \(\varepsilon\) is defined from the actual collision/propagation/background rates.

A stiff reduction is active only when:

1. the fast spectral gap exceeds all retained physical rates by the frozen margin;
2. the reconstruction residual is below tolerance;
3. conservation and constraints close;
4. the reduced and full systems overlap within error;
5. state and derivative matching are continuous;
6. switch hysteresis prevents branch chatter.

The exit event is determined by the generated error estimator, not a fixed public coordinate.

---

## 19. Fluid and free-streaming limits

For a projection \(P_r\) and reconstruction \(R_r\), a limit is admitted only when

\[
P_rR_r=I
\]

on retained moments and

\[
\sup_{O\in\mathcal O_H}
|O(X)-O(R_rP_rX)|
\le\varepsilon_r.
\]

The witnessed limit registry includes, where generated:

- perfect and imperfect fluid behavior;
- acoustic propagation;
- diffusion damping;
- collisionless free streaming;
- nonrelativistic growth response;
- relativistic anisotropic stress;
- weak- and strong-coupling limits.

A fluid closure is never retained after its witness fails.

---

## 20. Hierarchy truncation and no-reflection closure

Let \(P_N\) retain the represented multipole/momentum/species domain and \(Q_N=I-P_N\) its omitted tail. Partition

\[
\mathbb A
=\begin{pmatrix}
A_{PP}&A_{PQ}\\
A_{QP}&A_{QQ}
\end{pmatrix}.
\]

The frequency-domain exact effective retained operator is

\[
\boxed{
A_{\mathrm{eff}}(z)
=A_{PP}+A_{PQ}(zI-A_{QQ})^{-1}A_{QP}.
}
\]

A time-local asymptotic closure is admitted only when it approximates this tail resolvent within the declared domain and does not create a reflected incoming mode at the hierarchy boundary.

The truncation estimator combines:

\[
\epsilon_N
=\max\left(
\|P_NX^{(N+1)}-X^{(N)}\|,
\|\mathcal R_{\mathrm{constraint}}\|,
\|\mathcal R_{\mathrm{conservation}}\|,
\|\mathcal R_{\mathrm{tail}}\|
\right).
\]

Module A promotion extends multipole, momentum, species, route, frequency, time, and \(k\)-support until all claimed responses stabilize.

---

## 21. Direct hierarchy propagator

For fixed admissible \(\mathcal B\), define the fundamental matrix

\[
\boxed{
\frac{\partial}{\partial\eta}
\mathbb T_{H^U}(k;\eta,\eta_i\mid\mathcal B)
=\mathbb A_{H^U}(k,\eta;\mathcal B)
\mathbb T_{H^U}(k;\eta,\eta_i\mid\mathcal B),
\quad
\mathbb T_{H^U}(\eta_i,\eta_i)=I.
}
\]

It obeys composition

\[
\mathbb T(\eta_2,\eta_1)\mathbb T(\eta_1,\eta_0)
=\mathbb T(\eta_2,\eta_0).
\]

The inhomogeneous solution is

\[
\delta X(\eta)
=\mathbb T(\eta,\eta_i)\delta X_i
+\int_{\eta_i}^{\eta}
\mathbb T(\eta,u)\mathbb S(u)u(u)\,du.
\]

The direct solver remains the reference realization for gauge, reduction, line-of-sight, restart, and independent-formulation checks.

---

## 22. Unit responses and Green functions

For unit initial mode \(e_A\), define

\[
\delta X_A(k,\eta;\mathcal B)
=\mathbb T_{H^U}(k;\eta,\eta_i\mid\mathcal B)e_A(k).
\]

For observable/species projection \(P_X\),

\[
\boxed{
T_X^A(k,\eta;\mathcal B)
=P_X\mathbb T_{H^U}(k;\eta,\eta_i\mid\mathcal B)e_A.
}
\]

The retarded Green operator is

\[
\mathbb G_H(k;\eta,u\mid\mathcal B)
=\Theta(\eta-u)\mathbb T_{H^U}(k;\eta,u\mid\mathcal B).
\]

Distinct basis responses may not be quotient-merged because they resemble each other in one output channel. Equality requires a no-loss equivalence theorem over the complete response registry.

---

## 23. Line-of-sight source grammar

For radiative channel \(X\) and mode \(A\), split the photon hierarchy into a propagating block and physical source block inherited from Module G and the coupled Hᵁ state.

The line-of-sight response is

\[
\boxed{
\Delta_{\ell}^{X,A}(k;\eta_o\mid\mathcal B)
=
\int_{\eta_i}^{\eta_o}
\mathcal P_{\ell}^{X}
(k;\eta_o,u\mid\mathcal B)
S_X^A(k,u\mid\mathcal B)\,du.
}
\]

The projection kernel \(\mathcal P_\ell^X\) is generated by the homogeneous photon streaming/polarization operator on the declared background placeholder. The source registry includes, where active:

- intrinsic temperature/intensity;
- velocity/Doppler;
- polarization quadrupole;
- finite-width visibility and its derivatives;
- metric-interface and integrated sources;
- vector and tensor sources;
- spectral, defect, field, and dark-sector sources.

Source rearrangements by integration by parts must reconstruct the same direct hierarchy response. Line-of-sight compression never deletes the direct hierarchy reference.

---

## 24. Direct-versus-line-of-sight closure

At verification points, define

\[
\mathcal R_{\mathrm{LOS}}^{X,A}
=
\Delta_{\ell,\mathrm{direct}}^{X,A}
-\Delta_{\ell,\mathrm{LOS}}^{X,A}.
\]

The line-of-sight grammar is accepted only when

\[
\sup_{k,\ell,A,X}
\|\mathcal R_{\mathrm{LOS}}^{X,A}\|
\le\varepsilon_{\mathrm{LOS}}
\]

under source, interpolation, time, hierarchy, precision, and projection refinement.

This equality is an operator-level test, not a comparison to public spectra.

---

## 25. Response derivatives and adjoints

For background or upstream variable \(\theta_p\), the transfer derivative satisfies

\[
\frac{d}{d\eta}
\frac{\partial\mathbb T}{\partial\theta_p}
=
\mathbb A\frac{\partial\mathbb T}{\partial\theta_p}
+
\frac{\partial\mathbb A}{\partial\theta_p}\mathbb T.
\]

For scalar objective \(J\), the adjoint obeys

\[
-\dot\lambda
=\mathbb A^\dagger\lambda
+\frac{\partial j}{\partial X}.
\]

These maps export sensitivities and covariance propagation without refitting the operator.

---

## 26. Covariance propagation grammar

For any supplied initial covariance \(\Sigma_i\), the linear propagation map is

\[
\boxed{
\Sigma(\eta)
=\mathbb T(\eta,\eta_i)\Sigma_i
\mathbb T(\eta,\eta_i)^\dagger
+\Sigma_{\mathrm{proc}}(\eta).
}
\]

Equivalently,

\[
\dot\Sigma
=\mathbb A\Sigma+\Sigma\mathbb A^\dagger+\mathbb Q_H,
\qquad
\mathbb Q_H\succeq0.
\]

Module Hᵁ supplies this map but does not choose the realized primordial \(\Sigma_i\). Module J later derives that covariance.

The Hᵁ uncertainty state separates:

- Module G physical/recombination uncertainty;
- background-placeholder and later Module I covariance interfaces;
- gauge/reconstruction uncertainty;
- stiff-regime and switch error;
- hierarchy, momentum, frequency, time, and \(k\)-truncation error;
- interpolation and line-of-sight error;
- solver, precision, and branch uncertainty.

---

## 27. Stability, causality, and pathology domain

The operator family is admitted only on background/mode/refinement branches satisfying:

- a positive physical state metric/symmetrizer where required;
- no ghostlike negative-norm physical quotient modes;
- bounded characteristic/propagation speeds within the inherited causal law;
- no unresolved gradient instability;
- no singular gauge map;
- no runaway dark/field mode hidden by truncation;
- collision entropy production/damping signs consistent with the inherited route law;
- no hierarchy-boundary reflection above tolerance;
- no negative distribution artifact caused by reduction;
- no switch-induced discontinuity or branch chatter;
- bounded constraint and conservation residuals;
- stable interpolation and coefficient insertion.

A physically generated instability may remain as a classified branch. An unexplained numerical or constitutive instability obstructs the claim.

---

## 28. Intrinsic transfer-signature registry

Before Module I instantiation or any public comparison, Hᵁ freezes definitions for:

- mode and route support;
- scalar/vector/tensor and parity/helicity response channels;
- acoustic phase-response operators;
- finite-width visibility and drag response effects;
- diffusion/damping response operators;
- compression-relic clustering/stress response;
- dissipative-tail perturbative response;
- neutrino/free-streaming anisotropic-stress response;
- gauge-invariant metric-slip and Weyl-source response;
- field/defect/memory response or witnessed null results;
- operator eigenmode and transient-growth structure;
- transfer covariance and cross-response maps;
- falsifiers and domain conditions.

These signatures are definitions of frozen internal response objects, not claims of observational agreement.

---

## 29. Triad-and-kernel necessity

| Removal or corruption | Necessary consequence |
|---|---|
| remove CIF | no complete species, mode, gauge, route, source, or background-domain possibility space |
| remove QV | no lawful linearization, constraint selection, collision evolution, stiff reduction, propagation, or branch resolution |
| remove RFL | no frozen operator, stable basis, transfer composition, uncertainty map, memory, or Module I export |
| reorder the triad | possible perturbations, physical evolution, and stabilized operator become type-inconsistent |
| remove recursive kernel | route/depth weighting, hierarchy promotion, bounded tails, and response ancestry lose their generator |
| remove terminal N-body completion | multi-species graph, collision lanes, angular/momentum hierarchies, fields, and refinement are incomplete |
| remove witnesses | modes, collision blocks, approximations, closures, or source channels enter without lawful support |
| remove gauge quotient | gauge artifacts can become physical transfer responses |
| remove constraints | geometry and species evolution can drift off the physical manifold |
| remove collision ancestry | Module G recombination/opacity physics is replaced by an untyped scattering template |
| remove finite-width visibility | line-of-sight and source histories lose the physical CMB-surface structure |
| remove direct hierarchy | reductions and line-of-sight outputs lose their physical reference |
| remove basis distinction | Module J cannot assign a complete covariance over independent modes |
| receive Module I background before freeze | the operator can be redesigned around one realized history |
| import public transfer/spectra | the RFC universe ceases to generate its own linear response law |

---

## 30. Frozen Module Hᵁ export to Module I

Define

\[
\boxed{
P_{H^U\to I}
=(\mathbb B_{\mathrm{RFC}}[\mathcal B],\mathcal D_{\mathcal B},
\mathrm{PerturbationState}_H,\mathrm{ModeBasis}_H,\mathrm{Gauge}_H,
\mathrm{Constraint}_H,\mathrm{Conservation}_H,\mathrm{SVT}_H,
\mathrm{PhotonHierarchy}_H,\mathrm{PolarizationHierarchy}_H,
\mathrm{MatterHierarchy}_H,\mathrm{NeutrinoHierarchy}_H,
\mathrm{DarkHierarchy}_H,\mathrm{Collision}_H,\mathrm{SourceGrammar}_H,
\mathrm{InitialSeries}_H,\mathrm{StiffRegime}_H,\mathrm{Truncation}_H,
\mathrm{DirectSolver}_H,\mathrm{LOSGrammar}_H,\mathrm{GreenSchema}_H,
\mathrm{ResponseDerivativeSchema}_H,\mathrm{UncertaintyOperator}_H,
\mathrm{BackgroundInsertionMap}_H,\mathrm{IntrinsicSignature}_H,
\mathrm{Memory}_H,\mathrm{Ancestry}_H,\mathrm{Restart}_H,
\mathrm{FrozenOperatorIdentity}_H).
}
\]

Module I receives enough information to derive \(\mathcal B_I\) inside \(\mathcal D_{\mathcal B}\). It may not modify the Hᵁ state dimension, equation grammar, mode basis, gauge system, collision forms, hierarchy structure, closure rules, source grammar, uncertainty model, or scientific error criteria.

---

## 31. Protected later H[I] instantiation

After Module I derives and freezes \(\mathcal B_I\), the later phase performs only

\[
\boxed{
\mathbb B_{H[I]}
=\operatorname{Instantiate}
(\mathbb B_{\mathrm{RFC}}[\mathcal B],\mathcal B_I).
}
\]

Lawful instantiation may populate declared coefficient histories, normalization maps, background derivatives, horizon/curvature histories, interaction-rate histories, interpolation nodes, and background covariance.

It may not redesign the operator.

If \(\mathcal B_I\notin\mathcal D_{\mathcal B}\), H[I] is obstructed. A new operator version would require a separate pre-comparison construction and freeze.

Module H is therefore **not yet complete as a two-phase module**. Only Hᵁ is complete and frozen here.

---

## 32. Completion and claim boundary

Module Hᵁ establishes at its declared scope:

- immutable consumption of the complete Module G parent;
- explicit CIF/QV/RFL specialization of the enhanced Module A kernel;
- a typed admissible background domain independent of the realized Module I history;
- a complete multi-species perturbation state;
- scalar/vector/tensor and parity/helicity typing;
- gauge action, physical quotient, gauge-covariant evolution, and alternate-formulation verification grammar;
- propagated geometric, charge, normalization, and species constraints;
- collision, energy-momentum, and inter-sector conservation balance;
- photon intensity/polarization, baryon, charged/neutral matter, neutrino/free-streaming, compression-relic, dissipative-tail, field, and dark blocks where active;
- a complete regular initial-mode basis and early-time series grammar;
- controlled tight-coupling, fluid, free-streaming, and other stiff/asymptotic reductions;
- hierarchy truncation with tail-resolvent and no-reflection control;
- a direct fundamental-matrix propagator and composition law;
- unit responses, Green functions, line-of-sight source/projection grammar, and direct-versus-LOS closure;
- response derivatives, adjoints, covariance propagation, stability/pathology domain, intrinsic signatures, memory, ancestry, and restart closure;
- a frozen `P_H^U->I` operator packet.

Module Hᵁ does not claim:

- the realized Module I background;
- completed H[I] instantiation;
- realized basis-response histories;
- a primordial mode covariance or mode mixture;
- final CMB, matter, lensing, or growth spectra;
- nonlinear structure or astrophysical reionization;
- public Boltzmann-code agreement;
- empirical validation.

Within those boundaries, **Module Hᵁ is complete and frozen**. Module I is the active child. The later H[I] phase remains blocked until Module I returns a compliant realized background.