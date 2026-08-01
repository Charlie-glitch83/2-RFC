# Active Proof: Genesis Realization

## Purpose

Construct the first noncircular map from the completed abstract carrier \(\mathcal C_N\) to a physically typed state. This proof owns the boundary between the terminal kernel and the Big Implosion.

## Current theorem frontier

The positive graph metric and resolvent already derived in 1RFC can supply spatial/pregeometric compression, but they cannot supply causal signature or physical time alone. The next proposition derives an event order from RFC's own typed recursion structure before any physical clock is introduced.

## Bridge Lemma 1 — witness-certified acyclic event order

### Candidate construction

Represent every prephysical carrier event by

\[
e=(c,d,\rho,b,\sigma),
\]

where \(c\in\mathbb N\) is cycle index, \(d\in\mathbb N\) is recursion/event depth, \(\rho\) is a witnessed route identifier, \(b\) is branch identity, and \(\sigma\) is the protected no-loss signature.

Admit a directed edge \(e\to e'\) only if:

1. the source and target signatures pass the witness and no-loss predicates;
2. either \(c'=c\) and \(d'>d\), or a certified terminal-memory transition has occurred and \(c'=c+1\);
3. a same-cycle edge never decreases or preserves depth;
4. a cross-cycle edge terminates physical ancestry in cycle \(c\), passes through a prephysical qualified-memory/CIF state, and begins a new carrier in cycle \(c+1\).

Define \(e\prec_0 e'\) when an admitted edge exists and \(e\prec e'\) by nonempty directed reachability.

### Proof obligation

Prove, without using Newtonian or cosmological time, that:

- \(\prec\) is irreflexive and transitive;
- witness/no-loss signatures are preserved along every path;
- finite \(N\), finite admitted branching, and bounded depth intervals give local finiteness;
- the construction does not make recursion depth identical to eventual physical duration;
- the cross-cycle rule does not place the next CIF inside the old cycle's physical event set.

### Proof draft

Assign each carrier event the lexicographic rank \(r(e)=(c,d)\). Every admitted same-cycle edge strictly increases \(d\); every admitted cross-cycle edge strictly increases \(c\). Therefore every directed path strictly increases lexicographic rank. A nonempty path from \(e\) to itself would require \(r(e)<r(e)\), impossible, so reachability is irreflexive. Concatenation of nonempty paths proves transitivity.

Each edge is admitted only after its protected signature passes the witness/no-loss predicate. Induction on path length preserves the signature ancestry along finite paths. If the number of admitted routes and branches at each event is finite and only finitely many integer depths lie between two ranks, the interval \(\{z:e\prec z\prec e'\}\) is finite.

The rank proves order, not duration: no map from \(d\) or \(c\) to seconds has been defined. Thus this lemma supplies a precausal partial order candidate without importing a physical clock. The qualified-memory and conditioned-CIF objects are explicitly outside \(\mathsf P_D\); a cross-cycle carrier edge records ancestry but is not a later physical event in the terminated cycle.

### Current status

`DRAFT_PROOF_REQUIRES_INDEPENDENT_REVIEW`.

Open issue: determine whether route/event source rules guarantee the strict-depth edge condition, or whether that condition is a new axiom. If it is new, it must be derived from the First Action/kernel grammar or declared transparently; it may not be hidden inside “admission.”

## Realization obligations R1–R9

| ID | State | Current evidence | Exact missing item |
|---|---:|---|---|
| R1 | ACTIVE | Bridge Lemma 1 draft; graph-resistance insufficiency theorem proved | Source-derived strict-depth rule; causal/signature enrichment |
| R2 | OPEN | Dimensionless kernel and graph operators typed | Derive scale map or prove the minimal external unit convention |
| R3 | OPEN | Abstract carrier state only | Define physically dimensioned state variables |
| R4 | OPEN | Graph resolvent is a candidate map | Derive action/generator and allowed histories |
| R5 | OPEN | Graph total-mode preservation | Derive constraints/conservation from R4 |
| R6 | OPEN | Finite-N and zero-backreaction refinement | Prove graph/carrier refinement or declared finite validity regime |
| R7 | OPEN | None admitted | Define observer/instrument maps before target inspection |
| R8 | OPEN | No-target rule frozen | Predeclare CIF/QV/RFL, depth, memory, and carrier ablations |
| R9 | OPEN | Big Implosion/Big Rip predicates specified | Prove unique first and terminal physical events |

## Exit gate

This proof closes only when R1–R9 are `PROVED` or `NOT_APPLICABLE_WITH_PROOF`, an independent derivation reproduces the critical results, and no physical primitive appears upstream of its declared realization.
