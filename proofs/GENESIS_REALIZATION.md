# Active Proof: Genesis Realization

## Purpose

Construct the first noncircular map from the completed abstract carrier \(\mathcal C_N\) to a physically typed state. This proof owns the boundary between the terminal kernel and the Big Implosion.

## Current theorem frontier

The positive graph metric and resolvent already derived in 1RFC can supply spatial/pregeometric compression, but they cannot supply causal signature or physical time alone. RUN 006 supplies an append-only protected signature containing event ancestry; it also explicitly states that kernel depth measures inherited influence dispersion and is not physical time. Therefore kernel depth \(j\) cannot lawfully be repurposed as event succession.

Bridge Lemma 1 below extracts the order that the admitted source actually earns: immutable construction ancestry. Causal Enrichment Lemma 2 owns the still-open promotion from ancestry to physical causal precedence.

## Bridge Lemma 1 — append-only ancestry order

### Candidate construction

Represent every prephysical carrier event by

\[
e=(c,a,\rho,b,\sigma),
\]

where \(c\in\mathbb N\) is cycle index, \(a\in\mathbb N\) is append-only ancestry rank, \(\rho\) is a witnessed route identifier, \(b\) is branch identity, and \(\sigma\) is the protected no-loss signature. The rank \(a\) is ledger/derivation order, not kernel depth \(j\) and not physical duration.

Admit a directed edge \(e\to e'\) only if:

1. the source and target signatures pass the witness and no-loss predicates;
2. the child packet is appended after its immutable parent and carries the parent's identifier in its protected event ancestry;
3. either \(c'=c\) and \(a'>a\), or a certified terminal-memory transition has occurred and \(c'=c+1\);
4. a cross-cycle edge terminates physical ancestry in cycle \(c\), passes through a prephysical qualified-memory/CIF state, and begins a new carrier in cycle \(c+1\).

Define \(e\prec_0 e'\) when an admitted edge exists and \(e\prec e'\) by nonempty directed reachability.

### Proof obligation

Prove, without using Newtonian or cosmological time, that:

- \(\prec\) is irreflexive and transitive;
- witness/no-loss signatures are preserved along every path;
- finite \(N\), finite admitted branching, and bounded depth intervals give local finiteness;
- the construction does not make kernel depth or ancestry rank identical to eventual physical duration;
- the cross-cycle rule does not place the next CIF inside the old cycle's physical event set.

### Proof draft

RUN 006 defines return memory as an append-only typed ledger and includes event ancestry in the protected signature. Give every newly appended packet the next ancestry rank and assign each carrier event the lexicographic rank \(r(e)=(c,a)\). Every admitted same-cycle parent-child edge strictly increases \(a\); every admitted cross-cycle ancestry edge strictly increases \(c\). Therefore every directed path strictly increases lexicographic rank. A nonempty path from \(e\) to itself would require \(r(e)<r(e)\), impossible, so reachability is irreflexive. Concatenation of nonempty paths proves transitivity.

Each edge is admitted only after its protected signature passes the witness/no-loss predicate. Induction on path length preserves the signature ancestry along finite paths. If the number of admitted routes and branches at each event is finite and only finitely many integer ancestry ranks lie between two ranks, the interval \(\{z:e\prec_A z\prec_A e'\}\) is finite.

The rank proves ancestry, not duration: no map from \(a\), kernel depth \(j\), or cycle index \(c\) to seconds has been defined. The qualified-memory and conditioned-CIF objects are explicitly outside \(\mathsf P_D\); a cross-cycle carrier edge records derivational ancestry but is not a later physical event in the terminated cycle.

### Current status

`PROVED_AS_ANCESTRY_ORDER`.

The source review resolves the earlier open issue: kernel depth is not event succession, so a strict-kernel-depth rule would be a new and invalid type identification. Append-only event ancestry supports the theorem above, but ancestry alone is not yet physical causality.

## Causal Enrichment Lemma 2 — active

Let \(\prec_A\) be the proved ancestry order. Derive a source-owned witness predicate \(W_{\rm causal}(e,e')\), independent of public targets, and define

\[
e\prec_C e'
\quad\Longleftrightarrow\quad
e\prec_A e'
\ \text{and}\ 
W_{\rm causal}(e,e')=\mathrm{PASS}.
\]

The witness must come from the realized QV/domain law and establish the discrete analogue of causal admissibility, including compatibility with the governing evolution, locality or declared nonlocality, constraint propagation, and branch ancestry. Because a subset of an acyclic ancestry relation remains acyclic, the mathematical order is inherited; the missing proof is why the selected edges have **physical causal meaning**.

RUN 006 explicitly generates candidate event branches from a declared domain law. Therefore R1 and R4 are coupled: the causal witness cannot be completed before the governing physical law is derived, and the law cannot use an undeclared clock or geometry. The next derivation must construct these together rather than label an ancestry edge “causal.”

## Realization obligations R1–R9

| ID | State | Current evidence | Exact missing item |
|---|---:|---|---|
| R1 | ACTIVE | Bridge Lemma 1 proves append-only ancestry order; graph-resistance insufficiency theorem proved | QV/domain-law causal witness and physical interpretation |
| R2 | OPEN | Dimensionless kernel and graph operators typed | Derive scale map or prove the minimal external unit convention |
| R3 | OPEN | Abstract carrier state only | Define physically dimensioned state variables |
| R4 | ACTIVE_WITH_R1 | Graph resolvent is a candidate map; RUN 006 requires a declared domain law | Derive action/generator, allowed histories, and the causal witness jointly |
| R5 | OPEN | Graph total-mode preservation | Derive constraints/conservation from R4 |
| R6 | OPEN | Finite-N and zero-backreaction refinement | Prove graph/carrier refinement or declared finite validity regime |
| R7 | OPEN | None admitted | Define observer/instrument maps before target inspection |
| R8 | OPEN | No-target rule frozen | Predeclare CIF/QV/RFL, depth, memory, and carrier ablations |
| R9 | OPEN | Big Implosion/Big Rip predicates specified | Prove unique first and terminal physical events |

## Exit gate

This proof closes only when R1–R9 are `PROVED` or `NOT_APPLICABLE_WITH_PROOF`, an independent derivation reproduces the critical results, and no physical primitive appears upstream of its declared realization.
