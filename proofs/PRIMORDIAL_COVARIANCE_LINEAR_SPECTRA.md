# Proof of Module J Primordial Covariance and Linear-Statistical Closure

## 1. Assumptions and scope

Fix one admitted Module I/H[I] parent branch. Assume:

1. Module I supplies a realized background inside the frozen Hᵁ domain.
2. H[I] supplies a complete independent physical unit-mode basis after gauge quotient and constraint closure.
3. The H[I] transfer operator is immutable and well posed on the declared support.
4. Module A route, shell, event, memory, uncertainty, and terminal N-body carriers remain attached.
5. All source carriers used below have explicit units, branch identity, support, and ancestry.
6. All integrals and finite sums are taken over the declared converged support.

The theorem is finite-relational and branch conditional. It does not assert empirical agreement or a unique physical branch beyond the admitted parent state.

---

## 2. Primordial source map

Let \(\mathscr S_J\) be the finite source-carrier Hilbert space generated from Big-Implosion ancestry, route classes, recursive shells, relative-sector carriers, fields, defects, helicity/parity carriers, and permitted memory variables.

Let \(\mathscr M_J\) be the physical H[I] primordial mode space. Define the linear incidence map

\[
\mathcal R_J(\kappa):\mathscr S_J\to\mathscr M_J
\]

by projecting kernel-weighted source carriers onto the frozen unit modes.

Let the source covariance satisfy

\[
\Xi_J(\kappa,\kappa')
=\mathcal L_J(\kappa)\mathcal L_J(\kappa')^\dagger.
\]

Define

\[
\mathcal P_J(\kappa,\kappa')
=\mathcal R_J(\kappa)\Xi_J(\kappa,\kappa')
\mathcal R_J(\kappa')^\dagger.
\]

This is the Module J primordial covariance.

---

## 3. Hermiticity theorem

Because

\[
\Xi_J(\kappa,\kappa')
=\Xi_J(\kappa',\kappa)^\dagger,
\]

we have

\[
\begin{aligned}
\mathcal P_J(\kappa',\kappa)^\dagger
&=\left[
\mathcal R_J(\kappa')\Xi_J(\kappa',\kappa)
\mathcal R_J(\kappa)^\dagger
\right]^\dagger\\
&=\mathcal R_J(\kappa)
\Xi_J(\kappa',\kappa)^\dagger
\mathcal R_J(\kappa')^\dagger\\
&=\mathcal P_J(\kappa,\kappa').
\end{aligned}
\]

Therefore the covariance is Hermitian.

---

## 4. Positive-semidefinite theorem

For arbitrary square-integrable test vector \(v(\kappa)\), define

\[
w=\int d\mu(\kappa)\,
\mathcal L_J(\kappa)^\dagger
\mathcal R_J(\kappa)^\dagger v(\kappa).
\]

Then

\[
\begin{aligned}
&\int d\mu(\kappa)d\mu(\kappa')
 v(\kappa)^\dagger
\mathcal P_J(\kappa,\kappa')v(\kappa')\\
&=w^\dagger w\ge0.
\end{aligned}
\]

Hence \(\mathcal P_J\succeq0\).

A zero eigenvalue is allowed when the corresponding physical mode has no source support, is exactly compensated, or is removed by a proved no-loss quotient. A negative eigenvalue is inconsistent with the construction except for bounded numerical error.

---

## 5. Gauge and constraint support theorem

Let \(P_{\mathrm{phys}}\) be the frozen H[I] physical projector and suppose

\[
\mathcal R_J=P_{\mathrm{phys}}\mathcal R_J.
\]

Then

\[
P_{\mathrm{phys}}\mathcal P_JP_{\mathrm{phys}}^\dagger
=\mathcal P_J.
\]

For every frozen constraint \(\mathbb C_H\) with \(\mathbb C_HP_{\mathrm{phys}}=0\),

\[
\mathbb C_H\mathcal P_J=0,
\qquad
\mathcal P_J\mathbb C_H^\dagger=0.
\]

Therefore the ensemble has no pure-gauge or constraint-violating covariance support.

---

## 6. Symmetry-projection theorem

Suppose a generated symmetry group \(G_J\) acts unitarily through \(U(g)\). Define

\[
\mathcal P_J^G
=\int_{G_J}U(g)\mathcal P_JU(g)^\dagger d\mu_G(g).
\]

Hermiticity follows by adjunction under the invariant measure. For any vector \(v\),

\[
v^\dagger\mathcal P_J^Gv
=\int_{G_J}(U(g)^\dagger v)^\dagger
\mathcal P_J(U(g)^\dagger v)d\mu_G(g)\ge0.
\]

Thus generated symmetry projection preserves positive semidefiniteness. Symmetry projection is lawful only for symmetries proved for the branch.

---

## 7. Finite-power theorem

Assume the source covariance has converged finite support or a trace-class tail bound:

\[
\int_{\mathcal K_J}
\operatorname{Tr}[\Xi_J(\kappa,\kappa)]d\mu_J(\kappa)<\infty,
\]

and the incidence map is bounded:

\[
\|\mathcal R_J(\kappa)\|\le M_R(\kappa)
\]

with

\[
\int M_R(\kappa)^2
\operatorname{Tr}[\Xi_J(\kappa,\kappa)]d\mu_J(\kappa)<\infty.
\]

Then

\[
\operatorname{Tr}[\mathcal P_J]
\le \|\mathcal R_J\|^2\operatorname{Tr}[\Xi_J]
\]

pointwise, and the admitted total power is finite.

Therefore infrared and ultraviolet admissibility reduce to explicit source-tail and incidence-map bounds. A divergent branch is obstructed.

---

## 8. Transfer-covariance theorem

Let \(T_H(t)\) be the immutable H[I] response operator. Define

\[
P_X(t,t')=T_H(t)\mathcal P_JT_H(t')^\dagger.
\]

Hermiticity follows from

\[
P_X(t',t)^\dagger=P_X(t,t').
\]

For equal times and arbitrary vector \(v\),

\[
v^\dagger P_X(t,t)v
=(T_H(t)^\dagger v)^\dagger
\mathcal P_J(T_H(t)^\dagger v)\ge0.
\]

Therefore all generated equal-time species, sector, metric, and radiative covariance matrices remain positive semidefinite.

No modification of \(T_H\) is required or allowed.

---

## 9. Projected-spectrum theorem

Let \(\Delta_\ell^X(\kappa)\) be the frozen H[I] projection row for channel \(X\). Define

\[
C_\ell^{XY}
=\int d\mu_J(\kappa)
\Delta_\ell^X(\kappa)
\mathcal P_J(\kappa)
\Delta_\ell^Y(\kappa)^\dagger.
\]

For any complex channel coefficients \(c_X\),

\[
\sum_{X,Y}c_X^*C_\ell^{XY}c_Y
=\int d\mu_J
\left(\sum_Xc_X\Delta_\ell^X\right)
\mathcal P_J
\left(\sum_Yc_Y\Delta_\ell^Y\right)^\dagger
\ge0.
\]

Thus the complete projected channel matrix is Hermitian and positive semidefinite at each multipole or generalized projection label.

Parity-odd channels vanish only if the generated symmetry and covariance blocks require it.

---

## 10. Growth-rate identity

For positive auto-spectrum \(P_{aa}(t)\), define

\[
D_a(t;t_\star)=\sqrt{P_{aa}(t)/P_{aa}(t_\star)}.
\]

Then

\[
\frac{d\ln D_a}{dt}
=\frac{1}{2P_{aa}}\frac{dP_{aa}}{dt}.
\]

On a monotone scale branch with \(d\ln a_I/dt=H_I\),

\[
\boxed{
f_a=\frac{1}{2H_IP_{aa}}\frac{dP_{aa}}{dt}.}
\]

Since H[I] obeys \(\dot T=AT\),

\[
\dot P=AP+PA^\dagger,
\]

so the growth rate is computable directly from the frozen response operator and Module J covariance without external normalization.

---

## 11. Ensemble-equivalence theorem

Let \(\xi\) be a declared unit-covariance random vector:

\[
\mathbb E[\xi]=0,
\qquad
\mathbb E[\xi\xi^\dagger]=I.
\]

Choose a lawful covariance factor \(L_J\) such that

\[
\mathcal P_J=L_JL_J^\dagger,
\]

and set

\[
q=\mu+L_J\xi.
\]

Then

\[
\mathbb E[(q-\mu)(q-\mu)^\dagger]
=L_JL_J^\dagger=\mathcal P_J.
\]

After direct H[I] evolution \(Y=T_Hq\),

\[
\mathbb E[(Y-\bar Y)(Y-\bar Y)^\dagger]
=T_H\mathcal P_JT_H^\dagger.
\]

Therefore direct ensemble evolution and analytic covariance contraction are exactly equivalent in expectation. Finite-ensemble disagreement is governed by sampling and numerical uncertainty.

---

## 12. Reality theorem for finite-volume fields

For each independent transform mode \(k\), impose

\[
q(-k)=q(k)^*.
\]

Then the inverse transform satisfies

\[
X(x)^*=X(x),
\]

because the \(k\) and \(-k\) terms pair under complex conjugation. Zero and self-conjugate boundary modes are sampled from the appropriate real covariance.

Thus real physical fields follow from the paired complex mode representation without altering phases or covariance.

---

## 13. Finite-volume covariance recovery theorem

Let \(\widehat P\) be the bin estimator over \(N_k\) modes. Under the declared ensemble law,

\[
\mathbb E[\widehat P]=P+\mathcal B_{\mathrm{bin}}+\mathcal B_{\mathrm{window}},
\]

where bin and window biases are explicitly calculable from the finite volume and transform basis.

As volume, shell occupancy, ensemble size, and resolution increase while aliasing and missing-mode terms are controlled,

\[
\widehat P\to P
\]

in mean square on the admitted support.

Therefore Module J can certify covariance recovery with explicit finite-volume and sampling uncertainty rather than assuming one realization is exact.

---

## 14. Linearity-domain theorem

Let \(\epsilon_a(\kappa,t,s,r)\) be the mandatory physical error witnesses defined in the science file. Define

\[
\mathcal D_{\mathrm{lin}}
=\bigcap_a
\{(\kappa,t,s,r):\epsilon_a\le\epsilon_a^{\max}\}.
\]

Then membership is a conjunction of mandatory conditions. If any one witness fails, the point lies outside \(\mathcal D_{\mathrm{lin}}\), regardless of the values of other witnesses.

The first crossing time

\[
t_{\mathrm{prom}}(\kappa,s,r)
=\inf\{t:(\kappa,t,s,r)\notin\mathcal D_{\mathrm{lin}}\}
\]

defines the nonlinear-promotion surface when the infimum lies in the represented domain and the crossing is physically bracketed.

No aggregate score can override this result.

---

## 15. Restart theorem

The Module J restart state contains:

- parent identities;
- covariance generator and factorization identity;
- mode, route, branch, and symmetry state;
- transfer and projection identities;
- field volume, boundary, mesh, and transform state;
- seeds, phases, ensemble identifiers;
- covariance, spectra, growth, constraints, uncertainty;
- linearity witnesses and promotion events;
- memory and ancestry.

Because all stochastic and deterministic state variables are explicit, replay with the same frozen parent and restart state reproduces the same realization and statistical products within declared numerical precision.

---

## 16. Completion theorem

Under the assumptions above, Module J constructs:

1. a Hermitian positive-semidefinite primordial covariance with finite admitted power;
2. complete physical support on the frozen mode quotient;
3. generated symmetry, scalar/vector/tensor, parity, helicity, entropy, compensated, relative-sector, field, defect, and memory blocks;
4. immutable transfer contraction into complete linear spectra and growth histories;
5. a direct ensemble with the same covariance in expectation;
6. real finite-volume fields with preserved phase, constraints, covariance, branch, memory, and ancestry;
7. a componentwise physical linearity domain and first nonlinear-promotion surface;
8. a complete restartable parent state for Module K.

These conclusions hold only on admitted branches and declared support. They do not establish nonlinear structure, public-data agreement, or empirical truth.