# Foundation: Types, Kernel, and Terminal Carrier

## 1. Primitive triad

The ordered primitive triad is

\[
\mathcal T=(\mathrm{CIF},\mathrm{QV},\mathrm{RFL}),
\qquad
\mathrm{QV}(\mathrm{CIF})\longrightarrow\mathrm{RFL}.
\]

`CIF` is lawful possibility or admissible configuration; `QV` is lawful action/selection/transformation; `RFL` is Recursive Fractal Lattice, the stabilized and inheritable manifestation. The First Action is ontological dependency, not yet a physical event.

The canonical weighted representation is

\[
\boldsymbol\omega=(0.005085,\ 0.984868,\ 0.010047),
\qquad \sum_a\omega_a=1.
\]

These weights are a triadic representation, not three unrelated fit parameters.

## 2. Recursive kernel

For a normed feature sequence \(f_j\), define

\[
K_f^{(n)}(t)=\sum_{j=0}^{n}\delta^{-j}f_j e^{-\alpha jt},
\quad \delta>1,\quad \alpha\ge 0,\quad t\ge0.
\]

With \(\|f_j\|\le M\), the infinite-depth kernel converges absolutely and uniformly because

\[
\sum_{j=0}^{\infty}\left\|\delta^{-j}f_j e^{-\alpha jt}\right\|
\le M\sum_{j=0}^{\infty}\delta^{-j}
=\frac{M}{1-\delta^{-1}}.
\]

If the \(f_j\) are independent of \(t\), termwise differentiation is also uniformly controlled:

\[
\left\|\frac{dK_f}{dt}\right\|
\le \alpha M\sum_{j=0}^{\infty}j\delta^{-j}
=\alpha M\frac{\delta^{-1}}{(1-\delta^{-1})^2}.
\]

This proves a bounded memory-bearing kernel under stated assumptions. It does not assign physical units or physical time to \(t\).

## 3. The terminal finite-N lift

For \(N\) constituents, the abstract directed lane set is

\[
\Lambda_N=\{(i\mid j):1\le i,j\le N,\ i\ne j\},
\qquad |\Lambda_N|=N(N-1).
\]

Adding one constituent adds exactly

\[
|\Lambda_{N+1}|-|\Lambda_N|=2N
\]

directed lanes.

The completed carrier is typed as

\[
\mathcal C_N=
(K_f,\Lambda_N,\mathcal R_N,\mathcal W_N,
\mathcal E_N,\mathcal M_N,\sim_{\!\mathrm{lossless}},\mathcal P_N),
\]

where routes \(\mathcal R_N\) require witnesses \(\mathcal W_N\), event lift \(\mathcal E_N\) is partial and branch-aware, memory \(\mathcal M_N\) is typed, the quotient may remove duplicate representation only when every protected signature is preserved, and \(\mathcal P_N\) controls promotion to later scales.

This lift is integrated at the terminal kernel:

\[
\mathcal T\xrightarrow{\mathcal K}K_f
\xrightarrow{\mathcal L_N}\mathcal C_N.
\]

It is not a separate cosmological module. Later domains inherit \(\mathcal C_N\) through a realization map.

## 4. Prephysical/physical separation

Use four disjoint types:

\[
\mathsf T\xrightarrow{\mathcal K}\mathsf K
\xrightarrow{\mathcal L_N}\mathsf C_N
\xrightarrow{\mathcal R_D}\mathsf P_D.
\]

- \(\mathsf T\): ontological triad statements.
- \(\mathsf K\): recursive kernel objects.
- \(\mathsf C_N\): abstract relational carriers.
- \(\mathsf P_D\): physical states in domain \(D\).

Mass, Newton's constant, spatial coordinates, Newtonian acceleration, temperature, stress-energy, and physical time belong to \(\mathsf P_D\). They may verify a physical specialization of the carrier after \(\mathcal R_D\); they may not be silently used to construct the prephysical carrier.

This separation makes the N-body contribution stronger: its reusable theorem is the witnessed relational grammar for arbitrary finite \(N\), while Newtonian N-body mechanics is one domain corollary rather than a hidden axiom of cosmogenesis.
