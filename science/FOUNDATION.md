# Module A Foundation: Triad, Kernel, and Completed Relational Carrier

## 1. Scientific scope

Module A derives the **prephysical relational constitution** inherited by every later RFC module.

Its order is

```text
(CIF,QV,RFL)
-> First Action
-> recursive kernel
-> terminal finite-N relational completion
-> witnessed routes and events
-> protected memory and reopening
-> dormant or active downstream specialization
-> Module B
```

Module A contains no physical clock, spacetime, matter, radiation, stress-energy, thermodynamic history, or cosmological event. The Big Implosion remains Module B's sole first physical event.

The direct finite-N dynamics inherited from the N-body manuscript are Newtonian and domain-specific. The object exported universally is the **typed relational grammar**—source, action, stabilized output, directed relations, witnesses, routes, events, no-loss memory, promotion, uncertainty, and specialization—not Newtonian point-mass mechanics imposed on every domain.

---

## 2. Primitive ordered triad

The primitive triad is

\[
\mathcal T=(\mathrm{CIF},\mathrm{QV},\mathrm{RFL}),
\]

with role types

\[
\begin{aligned}
\mathrm{CIF}&:\text{admitted source-bearing possibility},\\
\mathrm{QV}&:\text{lawful action, selection, crossing, or compression},\\
\mathrm{RFL}&:\text{stabilized inheritable output in the Recursive Fractal Lattice}.
\end{aligned}
\]

The First Action is

\[
\boxed{\mathrm{QV}(\mathrm{CIF})\longrightarrow\mathrm{RFL}}.
\]

It is a dependency relation before it is a physical event.

### 2.1 Functional irreducibility

The three roles are not interchangeable:

- CIF without QV supplies no lawful transformation;
- QV without CIF has no admitted source;
- QV without RFL retains no stabilized result;
- RFL alone does not identify its source or lawful generation;
- changing the order changes the meaning of the construction.

A weighted triadic representation may be used where a later derivation authorizes it, but weights are not three independent fitted fields and are not needed to prove functional irreducibility. Historical numerical packets are not Module A theorem premises.

### 2.2 Source, memory, and manifestation are distinct

The generic return relation is typed as

\[
\mathrm{RFL}_{s}^{\mathrm{return}}
\longrightarrow
M_{\mathrm{rec},s}^{\mathrm{latent}}
\dashrightarrow
\mathrm{CIF}_{s+1}^{\mathrm{conditioned}}.
\]

The dashed arrow means lawful conditioning, not identity. Therefore

\[
\mathrm{RFL}_{s}^{\mathrm{return}}
\neq M_{\mathrm{rec},s}^{\mathrm{latent}}
\neq \mathrm{CIF}_{s+1}^{\mathrm{conditioned}}.
\]

Memory is not a fourth primitive. It preserves qualified information from a stabilized result and may condition a later source, but it does not replace CIF, perform QV, or become RFL by relabeling.

---

## 3. Recursive kernel constitution

For a normed feature family \(f_j(t)\), define the completion-compatible kernel

\[
K_f(t)=\sum_{j=0}^{\infty}
\delta^{-j}e^{-\alpha jt}f_j(t),
\qquad \delta>1,\quad \alpha\ge0,\quad t\ge0.
\]

The parameter \(t\) is an internal argument of the represented domain. In Module A it is not physical cosmological time. The depth index \(j\) orders inherited influence and memory; it is not an event clock.

Define

\[
q(t)=\frac{e^{-\alpha t}}{\delta},
\qquad 0<q(t)<1.
\]

### 3.1 Finite/infinite index reconciliation

Some source formulas begin at \(j=1\). The completion-compatible form begins at \(j=0\). They are reconciled exactly by

\[
K_f^{[0]}(t)=f_0(t)+K_f^{[1]}(t).
\]

The difference is the explicit basal mode, not a competing kernel law.

### 3.2 Absolute and uniform convergence

If

\[
\sup_{j,t}\|f_j(t)\|\le M,
\]

then

\[
\|K_f(t)\|
\le M\sum_{j=0}^{\infty}q(t)^j
=\frac{M}{1-q(t)}
\le\frac{M}{1-\delta^{-1}}.
\]

The Weierstrass majorant therefore gives absolute and uniform convergence on every certified domain with the stated bound.

### 3.3 Certified truncation

For the depth-\(m\) truncation

\[
K_f^{(m)}(t)=\sum_{j=0}^{m}
\delta^{-j}e^{-\alpha jt}f_j(t),
\]

the omitted tail obeys

\[
\boxed{
\|K_f(t)-K_f^{(m)}(t)\|
\le
M\frac{q(t)^{m+1}}{1-q(t)}
\le
M\frac{\delta^{-(m+1)}}{1-\delta^{-1}}
}.
\]

A finite-depth implementation must carry this bound rather than treating truncation as exact completion.

### 3.4 Perturbation stability

If two admissible feature families satisfy

\[
\sup_{j,t}\|f_j(t)-g_j(t)\|\le\varepsilon,
\]

then

\[
\boxed{
\|K_f(t)-K_g(t)\|
\le\frac{\varepsilon}{1-q(t)}
\le\frac{\varepsilon}{1-\delta^{-1}}
}.
\]

The kernel is therefore uniformly stable to bounded admissible feature perturbations.

### 3.5 Conditional termwise differentiation

If every \(f_j\) is differentiable and

\[
\sup_{j,t}\|f_j(t)\|\le M,
\qquad
\sup_{j,t}\|\partial_t f_j(t)\|\le M_1,
\]

then

\[
\partial_tK_f(t)
=
\sum_{j=0}^{\infty}
\delta^{-j}e^{-\alpha jt}
\left(\partial_t f_j(t)-\alpha j f_j(t)\right),
\]

with majorant

\[
\boxed{
\|\partial_tK_f(t)\|
\le
\frac{M_1}{1-q(t)}
+
\alpha M\frac{q(t)}{(1-q(t))^2}
}.
\]

Differentiability is therefore conditional on the stated regularity; convergence alone does not imply it.

### 3.6 Depth-tagged modal basis

An admitted finite or countable basis is written

\[
\mathfrak B_f=\{(j,f_j,\mathsf{type}_j,\mathsf{source}_j,
\mathsf{validity}_j,\mathsf{uncertainty}_j)\}_{j\ge0}.
\]

Every mode retains its depth, type, source, validity domain, and uncertainty. A mode with missing source or validity information is not silently admitted.

### 3.7 Recursive-depth influence distribution

For \(0<q<1\), define

\[
p_j=(1-q)q^j,
\qquad
\sum_{j=0}^{\infty}p_j=1.
\]

The associated depth-dispersion functional is

\[
S_{\mathrm{rec}}(q)
=-\sum_{j=0}^{\infty}p_j\log p_j
=-\log(1-q)-\frac{q\log q}{1-q}.
\]

This is a mathematical distribution of inherited influence across recursive depth. It is not thermodynamic entropy and is not physical time in Module A.

---

## 4. Terminal finite-N relational completion

Let \(\mathbf C_N=\{c_1,\ldots,c_N\}\) be a typed finite constituent set. Its directed non-self relation set is

\[
L_N=\{(i\mid j):1\le i,j\le N,\ i\ne j\}.
\]

Hence

\[
\boxed{|L_N|=N(N-1)}
\]

and

\[
\boxed{|L_{N+1}|-|L_N|=2N}.
\]

The increase is exact directed relational capacity. Strict physical solution growth requires at least one newly admitted witnessed non-gauge closure; lane growth alone does not prove it.

### 4.1 Route-indexed kernel

For a lawful route class \([r]\), the terminal relational kernel is

\[
K_{[r],N}(t)
=
\sum_{j=0}^{\infty}
\delta^{-j}e^{-\alpha jt}
\Phi_{j,[r],N}(t).
\]

The finite-N lift changes the modal content from \(f_j\) to \(\Phi_{j,[r],N}\) while preserving the depth law. Singleton reduction returns the base kernel. The N-body construction therefore completes the terminal end of the kernel instead of creating a second foundation.

### 4.2 Direct dynamical scope

When specialized to the N-body manuscript's Newtonian domain, a finite system carries positive masses, finite initial data, one declared normalized dynamical time, and the governing Newtonian residuals. That direct theorem remains finite-N and domain-specific.

The universal Module A carrier does **not** export mass, Newton's constant, Euclidean coordinates, Newtonian acceleration, or normalized N-body time as prephysical primitives. A later domain must derive its own law and physical variables before activating the inherited relational grammar.

---

## 5. Witness-governed route admission

A route is lawful only when it has a locally generated witness. The repository fixes the six scientific witness blocks as

\[
\mathsf W_r=
(
W_{\mathrm{law}},
W_{\mathrm{inv}},
W_{\mathrm{proj}},
W_{\mathrm{packet}},
W_{\mathrm{event}},
W_{\Phi}
).
\]

They contain:

1. **law residual:** differential, algebraic, variational, or evolution residual;
2. **invariant block:** required conservation or invariant drift;
3. **projection block:** constituent, lane, and representation consistency;
4. **packet block:** CIF/QV/RFL, return-memory, source, and route continuity;
5. **event block:** collision, boundary, branch, and ancestry status;
6. **kernel block:** boundedness, convergence, truncation, and modal validity.

A known orbit or public solution may test a frozen prediction later. It cannot become the reason a route was admitted.

### 5.1 Local route theorem

For a finite noncollision source state and a declared domain law whose vector field or evolution operator satisfies the needed local regularity, a complete witness certifies a unique local route in the declared route class.

Overlapping unique local charts patch to a maximal noncollision route domain. The maximal domain ends at the first boundary where the current chart loses admissibility or requires event treatment.

This is local/maximal noncollision existence—not universal all-time regularity.

### 5.2 Route classes

Module A distinguishes:

- **representative equivalence:** notation or encoding differences only;
- **gauge equivalence:** different representatives of the same protected closure;
- **independent multiroute:** different lawful protected closures for the same admitted source problem;
- **obstruction:** no witnessed lawful closure.

A finite nonempty route family with finite positive class weights has

\[
Z_N=\sum_{[r]}w_{[r],N}>0,
\qquad
p_{[r]}=\frac{w_{[r],N}}{Z_N}.
\]

This normalization statement is conditional. An infinite or singular route family requires its own measure and convergence theorem.

---

## 6. Correct add-one-constituent refinement

The lawful refinement is not unchanged positive-influence trajectory inclusion.

Let an admitted \(N\)-constituent solution germ be extended by one fixed admissible constituent specialization. Then:

1. the old source/problem family embeds into the enlarged problem;
2. the enlarged relation set contains the old lanes plus exactly \(2N\) new lanes;
3. the enlarged locally regular problem has its own solution germ on the certified domain;
4. positive added influence generally perturbs the old subsystem;
5. on a compact noncollision interval, continuous dependence controls the perturbation;
6. the old trajectory is recovered only in the zero-backreaction limit.

For the Newtonian specialization with added mass \(\mu\), minimum separation \(d>0\), and compact-domain Lipschitz control, the projected difference has the form

\[
\sup_{0\le t\le T}
\|\pi_Nx_{N+1}^{(\mu)}(t)-x_N(t)\|
\le C_T\mu,
\]

so

\[
\pi_Nx_{N+1}^{(\mu)}\longrightarrow x_N
\quad\text{as}\quad\mu\to0^+.
\]

For \(\mu>0\), exact unchanged trajectories are generally false.

---

## 7. Partial event multifunction

At a route boundary, define the witnessed event map

\[
\mathcal E_A:
(\text{pre-event state},\text{event witness})
\rightharpoonup
\mathcal P(\text{post-event branches}).
\]

It returns exactly one scientific class:

```text
OBSTRUCTION
UNIQUE_CONTINUATION
GAUGE_FAMILY
INDEPENDENT_MULTI_ROUTE_FAMILY
```

The classification is determined by complete protected signatures:

- no lawful signature gives `OBSTRUCTION`;
- one lawful signature gives `UNIQUE_CONTINUATION`;
- multiple representatives of one signature give `GAUGE_FAMILY`;
- multiple independent lawful signatures give `INDEPENDENT_MULTI_ROUTE_FAMILY`.

The event map never invents an outgoing branch and never selects a branch from a public target.

---

## 8. Protected no-loss state

The repository fixes the Module A protected signature as eighteen typed fields:

1. source identity;
2. constituent identities and types;
3. represented state and state type;
4. dimensional or prephysical type declaration;
5. directed relation identities and orientation;
6. route identity and route class;
7. witness identity and witness blocks;
8. invariants, residuals, and validity domain;
9. branch identity;
10. event identity and event status;
11. topology or adjacency identity;
12. kernel and depth ancestry;
13. scale ancestry;
14. uncertainty and covariance or interval state;
15. numerical precision, truncation, and error state;
16. manuscript and derivation provenance;
17. memory ancestry and return identity;
18. permissions, claim boundary, and falsifiers.

Write this tuple as \(\sigma_{\mathrm{prot}}(x)\).

A no-loss quotient is lawful only under

\[
x\sim_{\mathrm{NL}}y
\quad\Longleftrightarrow\quad
\sigma_{\mathrm{prot}}(x)=\sigma_{\mathrm{prot}}(y).
\]

The induced signature map on quotient classes must remain injective. Any independent protected difference forbids quotient deletion.

---

## 9. Identity-preserving memory

Memory is an information-bearing map on the protected state:

\[
\operatorname{Encode}_M:
\sigma_{\mathrm{prot}}(x)\mapsto M_x,
\]

\[
\operatorname{Decode}_M(M_x)
=
\sigma_{\mathrm{prot}}(x).
\]

Thus

\[
\boxed{
\operatorname{Decode}_M\circ\operatorname{Encode}_M
=\operatorname{id}
}
\]

on the protected image.

Event ancestry is append-only. Its order records parentage and derivation, not physical duration. Memory preserves branch, route, source, scale, uncertainty, and provenance identity but does not guarantee unlimited storage depth or indefinite cosmic recurrence.

---

## 10. Scale promotion and reopening

A scale promotion is typed as

\[
\Pi_{\uparrow}(x)=
(
\operatorname{Aggregate}(x),
\operatorname{Encode}_M(\sigma_{\mathrm{prot}}(x)),
\mathsf{validity},
\mathsf{interaction\ law}
).
\]

A lawful reopening satisfies

\[
\boxed{
\Pi_{\downarrow}\Pi_{\uparrow}x=x
}
\]

on the declared protected state. Promotion is therefore a split monomorphism over the protected image.

This abstract law does not prove that every later physical coarse graining is valid. Each child module must derive the aggregation, effective interaction, validity range, and physically meaningful observables for its own domain.

---

## 11. Dormancy and activation

Let \(a_D\in\{0,1\}\) be a witnessed activation predicate for a domain specialization \(D\). Its contribution and backreaction are

\[
\mathcal O_D=a_D\,\mathcal O_D^{\mathrm{active}},
\qquad
\mathcal B_D=a_D\,\mathcal B_D^{\mathrm{active}}.
\]

When \(a_D=0\),

\[
\boxed{\mathcal O_D=0,\qquad\mathcal B_D=0}
\]

while its carrier identity and ancestry remain stored. Activation requires both a route-local witness and a domain-specialization certificate. Dormancy is not deletion and is not hidden activity.

---

## 12. Uncertainty and sensitivity

Every inherited object carries:

- uncertainty type;
- covariance, interval, or admissible-set representation;
- derivation source;
- transformation law;
- validity range;
- numerical error and truncation state;
- freeze status.

Where a differentiable transformation \(F\) is justified,

\[
\Sigma_{\mathrm{out}}=J_F\Sigma_{\mathrm{in}}J_F^{\mathsf T}
+\Sigma_{\mathrm{model}}
+\Sigma_{\mathrm{numeric}}.
\]

Uncertainty is never permission to tune, hide a failed condition, or collapse an unresolved branch.

---

## 13. Completed Module A carrier

The completed carrier is

\[
\boxed{
\widehat{\mathcal K}_N
=
\operatorname{Complete}_{NB}
\left(
K_f,
\mathbf C_N,
\mathsf{Witness},
\mathsf{Route},
\mathsf{Event},
\mathsf{Memory},
\mathsf{NoLoss},
\mathsf{Promote},
\mathsf{Specialize},
\mathsf{Uncertainty}
\right)
}
\]

for every finite \(N\) on its maximal witnessed admissible atlas.

A clean export is

\[
H_A=
(S_A,\Sigma_A,\mathcal R_A,\mathcal E_A,M_A,
\mathcal S_A,\Pi_A,F_A,C_A),
\]

where the components carry the triadic/kernel state, uncertainty, relational carrier, event grammar, memory, specialization/promotion law, permissions/provenance, falsifiers, and completion/child boundary.

### 13.1 Universal downstream grammar

Every later module \(i\) must derive

\[
\mathrm{CIF}_i
=\mathsf{Src}_i(H_A,H_{i-1},M_i),
\]

\[
\mathrm{QV}_i
=\mathsf{Act}_i(\mathrm{CIF}_i,H_A,H_{i-1}),
\]

\[
\mathrm{RFL}_i
=\mathsf{Stab}_i
\left(\mathrm{QV}_i(\mathrm{CIF}_i),H_A,H_{i-1}\right),
\]

\[
H_i
=\mathsf{Export}_i
(\mathrm{CIF}_i,\mathrm{QV}_i,\mathrm{RFL}_i,H_A,H_{i-1}).
\]

The child must preserve witnesses, events, memory, no-loss distinctions, uncertainty, provenance, and falsifiers. It may not rename an unresolved physical law as a triadic output.

---

## 14. Exact Module A claim boundary

Module A establishes:

- the ordered primitive triad and prephysical First Action;
- the convergent, bounded, truncatable, perturbation-stable recursive kernel;
- conditional differentiability under named assumptions;
- finite-N directed relational capacity and exact add-one lane growth;
- source-generated local witnesses;
- local/maximal noncollision route construction under a declared regular domain law;
- route, gauge, multiroute, and obstruction distinctions;
- corrected positive-influence refinement with zero-backreaction recovery;
- the partial witnessed event multifunction;
- a protected no-loss quotient;
- exact protected memory and scale reopening;
- dormant zero contribution and zero backreaction;
- uncertainty-bearing immutable downstream inheritance.

Module A does not establish:

- one physically infinite-N state;
- universal all-time regularity;
- unconditional strict physical solution growth;
- unchanged trajectories after adding positive influence;
- thermodynamic entropy from recursive depth;
- physical time before the Big Implosion;
- a Lorentzian spacetime, particles, fields, or cosmological evolution;
- empirical proof that nature realizes the carrier;
- indefinite memory capacity or infinite recurrence.

Within these boundaries, Module A is complete and frozen. Module B is its proper physical child.