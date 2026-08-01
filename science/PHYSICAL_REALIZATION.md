# Physical-Realization Interface

## Target theorem

For an abstract completed carrier \(\mathcal C_N\), an admissible realization

\[
\mathcal R_D:\mathsf C_N\rightharpoonup\mathsf P_D
\]

must produce a physical state by derivation, not by relabeling. The map is certified only when all nine obligations below are proved separately.

| ID | Required output | Question that must be answered |
|---|---|---|
| R1 | Causal or precausal order | What distinguishes before/after, spacelike/timelike/null, or their discrete analogues? |
| R2 | Dimensions and scale ancestry | Where do units and every dimensionful scale come from? |
| R3 | Physical state variables | What quantities carry geometry, fields, matter, radiation, and uncertainty? |
| R4 | Action, Hamiltonian, or evolution law | What law selects allowed histories and produces evolution? |
| R5 | Constraints and conservation | Which identities follow from the law, and how are they checked? |
| R6 | Refinement/continuum control | What survives increasing resolution or constituent number, and in what regime? |
| R7 | Observable map | How do internal states generate quantities an instrument can measure? |
| R8 | Triadic nondegeneracy | Which preregistered ablations show the triad/carrier is causally necessary rather than decorative? |
| R9 | Boundary events | Why is the Big Implosion uniquely first and the Big Rip terminal within a cycle? |

## The graph-resolvent result retained from 1RFC

For a finite connected weighted undirected graph with symmetric weight matrix \(C\), Laplacian \(L\), and \(\ell>0\),

\[
Q=(I+\ell L)^{-1},\qquad x^+=Qx^-
\]

is well-defined. Since \(L\succeq0\), \(Q\) is symmetric positive definite; it preserves the constant mode, contracts nonconstant Laplacian modes, and decreases the graph Dirichlet energy. These are useful pregeometry/compression results.

### Physical-typing necessity theorem

**Theorem.** The pair \((Q,d_R)\), where \(d_R\) is effective-resistance distance, is insufficient by itself to establish a Lorentzian spacetime, physical time, a stress-energy tensor, or a dark-sector identity.

**Proof.** On a connected graph,

\[
d_R(i,j)=(e_i-e_j)^TL^+(e_i-e_j)
\]

is nonnegative, symmetric, and zero only when \(i=j\). A Lorentzian quadratic form is indefinite: it admits positive, negative, and nonzero null directions, and distinct null-related events can have zero interval. No identification that uses only the positive separating metric \(d_R\) can preserve those Lorentzian interval types. Therefore additional causal/signature structure is necessary.

If \(L\), \(\ell\), and \(x\) are dimensionless, then \(Qx\) is dimensionless and invariant under arbitrary changes of physical units; no unique duration, length, mass, or energy scale follows without a declared scale map. Finally, an undirected smoothing operator supplies neither a physical action nor an interpretation of its spectral subspaces. Orthogonal parity projectors can partition a vector space, but names such as ordinary, radiative, compression relic, or dissipative tail require independent dynamical and observational discriminants. ∎

This theorem does not discard Module B's algebra. It locates it correctly: \(Q\) is a candidate compression/pregeometry component inside \(\mathcal R_D\), not a completed physical realization.

## Preferred bridge route

The most source-compatible route is a **discrete causal realization** built from the carrier's event lift:

\[
\mathcal R_{\rm dc}(\mathcal C_N)
=(E,\prec,\Sigma,\Phi,S,\mathcal C,U,\mathcal O).
\]

Here \(E\) is an event set, \(\prec\) a witness-certified precedence relation, \(\Sigma\) spatial/pregeometric data on suitable slices, \(\Phi\) physical state variables, \(S\) the governing action or generator, \(\mathcal C\) constraints, \(U\) the dimension/scale map, and \(\mathcal O\) observables.

The event order must be derived without importing Newtonian time. Recursion depth, route order, event order, cycle index, and later physical time remain different types. [The active proof](../proofs/GENESIS_REALIZATION.md) begins with that requirement.
