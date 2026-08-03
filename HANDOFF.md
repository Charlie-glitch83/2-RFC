# Handoff for Future Iterations

## Required read order

1. `README.md`
2. `architecture/2RFC_DETAILED_SCIENTIFIC_GAP_TO_LIBRARY_REPAIR_PLAN.md`
3. `architecture/2RFC_MODULE_BY_MODULE_SCIENTIFIC_REPAIR_PLAN.md`
4. `architecture/2RFC_WOLFRAM_INTEGRATION_RULES.md`
5. `modules/A/MODULE_A_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
6. `modules/A/MODULE_A_WOLFRAM_REVISION.md`
7. `modules/A/MODULE_A_TO_B_SCIENTIFIC_HANDOFF.md`
8. `modules/B/MODULE_B_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
9. `modules/B/MODULE_B_WOLFRAM_REVISION.md`
10. `modules/B/MODULE_B_TO_C_SCIENTIFIC_HANDOFF.md`
11. `modules/C/MODULE_C_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
12. `modules/C/MODULE_C_WOLFRAM_REVISION.md`
13. `modules/C/MODULE_C_TO_D_SCIENTIFIC_HANDOFF.md`
14. `modules/D/MODULE_D_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
15. `modules/D/MODULE_D_WOLFRAM_REVISION.md`
16. `modules/D/MODULE_D_TO_E_SCIENTIFIC_HANDOFF.md`
17. `modules/E/MODULE_E_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
18. `modules/E/MODULE_E_WOLFRAM_REVISION.md`
19. `modules/E/MODULE_E_TO_F_SCIENTIFIC_HANDOFF.md`
20. `modules/F/MODULE_F_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
21. `modules/F/MODULE_F_WOLFRAM_REVISION.md`
22. `modules/F/MODULE_F_TO_G_SCIENTIFIC_HANDOFF.md`
23. `modules/G/MODULE_G_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
24. `modules/G/MODULE_G_WOLFRAM_REVISION.md`
25. `modules/G/MODULE_G_TO_H_UNIT_SCIENTIFIC_HANDOFF.md`
26. `modules/H/MODULE_H_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
27. `modules/H/MODULE_H_WOLFRAM_REVISION.md`
28. `modules/H/MODULE_H_UNIT_TO_I_SCIENTIFIC_HANDOFF.md`
29. `modules/I/MODULE_I_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
30. `modules/I/MODULE_I_WOLFRAM_REVISION.md`
31. `modules/I/MODULE_I_TO_H_INSTANTIATED_SCIENTIFIC_HANDOFF.md`
32. `modules/J/MODULE_J_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
33. `modules/J/MODULE_J_WOLFRAM_REVISION.md`
34. `modules/J/MODULE_J_TO_K_SCIENTIFIC_HANDOFF.md`
35. `modules/K/MODULE_K_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
36. `modules/K/MODULE_K_WOLFRAM_REVISION.md`
37. `modules/K/MODULE_K_TO_L_SCIENTIFIC_HANDOFF.md`
38. `modules/L/MODULE_L_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
39. `modules/L/MODULE_L_WOLFRAM_REVISION.md`
40. `modules/L/MODULE_L_TO_M_SCIENTIFIC_HANDOFF.md`
41. `modules/M/MODULE_M_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
42. `modules/M/MODULE_M_WOLFRAM_REVISION.md`
43. `modules/M/MODULE_KLM_TO_N_SCIENTIFIC_HANDOFF.md`
44. `modules/N/MODULE_N_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
45. `modules/N/MODULE_N_WOLFRAM_REVISION.md`
46. `modules/N/MODULE_N_TO_O_SCIENTIFIC_HANDOFF.md`
47. `modules/O/MODULE_O_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
48. `modules/O/MODULE_O_WOLFRAM_REVISION.md`
49. `modules/O/MODULE_O_TO_P_SCIENTIFIC_HANDOFF.md`
50. `modules/P/MODULE_P_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
51. `modules/P/MODULE_P_WOLFRAM_REVISION.md`
52. `modules/O/MODULE_O_TO_Q_SCIENTIFIC_HANDOFF.md`
53. `modules/Q/MODULE_Q_DETAILED_SCIENTIFIC_REPAIR_PLAN.md`
54. `modules/Q/MODULE_Q_WOLFRAM_REVISION.md`
55. the existing 2-RFC module being repaired
56. the exact valid scientific sources named by the active module plan

Each `MODULE_X_WOLFRAM_REVISION.md` is a binding revision of the corresponding detailed plan, not an optional addendum.

## Governing method

- The module is the unit of work.
- The detailed gap-to-library repair plan is the primary scientific spine.
- Every child consumes a sealed parent state; it may not reconstruct missing parent science.
- Preserve correct science already present in 2-RFC.
- RUN 000–007 supply only completed Module A science.
- RUN 008–013 supply only completed Module B science.
- Reuse later library science only at its exact supported scope.
- Do not copy the old run system, numbering, preflights, lifecycle machinery, status taxonomies, repository schemas, gates, certificates, manifests, or evidence bureaucracy into the scientific architecture.
- Public observations may test the frozen universe in Module P but may not generate or repair it.
- Any mandatory normalized comparison component below `0.95` fails; no averaging may hide it.

## Wolfram operating law

Wolfram is now an explicit computational instrument throughout A–Q.

It is authorized for exact symbolic derivation, arbitrary-precision numerics, asymptotics, graph and event analysis, differential and integral equations, optimization, uncertainty and covariance propagation, statistical comparison, and independent verification.

It is not an RFC source and may not supply missing physics, fitted constants, standard-cosmology replacements, public-data targets outside Module P, post-hoc repair, or empirical branch selection.

Every load-bearing Wolfram result must preserve its equations, assumptions, domains, units, branch conditions, code or query, precision, errors or residuals, uncertainty, interpretation, and independent check. A Wolfram disagreement stops the affected claim until localized and resolved; it never authorizes retuning.

## Completed scientific planning chain

```text
A
-> A→B -> B
-> B→C -> C
-> C→D -> D
-> D→E -> E
-> E→F -> F
-> F→G -> G
-> G→Hᵁ -> Hᵁ
-> Hᵁ→I -> I
-> I→H[I] -> H[I]
-> J
-> J→K -> K^(0)
-> K→L -> L^(0)
-> L→M -> M^(0)
-> classified K–L–M closure
-> (K*,L*,M*)→N -> N
-> N→O -> O
-> O→P -> P
-> O→Q -> Q
```

Every Module A–Q detailed scientific plan, its binding Wolfram revision, and every required parent-child scientific handoff now exists on `agent/triadic-proof-rebuild`.

These files are authoritative plans and boundary definitions. They are not yet the in-place implementation of the repaired proof modules.

## Protected architectures

### Early and linear

```text
G -> Hᵁ -> I -> H[I] -> J -> K
```

- `Hᵁ` is frozen before the realized Module I background.
- `H[I]` is immutable coefficient insertion, not operator redesign.
- Module J supplies primordial covariance, realized linear spectra, growth, finite-volume fields, and the nonlinear-promotion surface.

### Coupled nonlinear universe

```text
J -> K^(0) -> L^(0) -> M^(0)
K^(n) -> L^(n) -> M^(n) -> K^(n+1)
(K*,L*,M*) -> N
```

- K owns nonlinear gravity, phase space, collapse, structures, web/voids, metric, lensing, and lightcones.
- L owns hydrodynamics, MHD, thermochemistry, radiation, star formation, stellar evolution, feedback, remnants, and baryonic return.
- M owns isotope-resolved stellar/explosive nucleosynthesis, radioactive descendants, enrichment transport, dust, and composition feedback.
- Modules A–J remain frozen during K–L–M replay.
- Only a fixed point, bounded cycle, slowly evolving attractor, classified branch family, or explicit nonconvergence proceeds to N.

### Manifested universe and freeze

```text
(K*,L*,M*) -> N -> O
```

- N reconciles all domains as one physical universe, with one identity, event, causal, worldline/worldtube, conservation, lineage, record, observer-readiness, truth-lightcone, and truth-observable state.
- N stops at physically witnessed observer readiness and does not claim consciousness.
- O preserves one immutable parent, exact restart state, law and realization identity, uncertainty, covariance, lineage, restoration, restart continuity, and scientific equivalence.
- Failed restoration or reproduction never permits retuning the same parent.

### Final isolated branches

```text
N -> O -> {P,Q}
P -/-> O
P -/-> Q
Q -/-> O
```

- P is read-only empirical testing: observation operators, instruments, surveys, selection, noise, catalogues, covariance, public comparison, residuals, falsifiers, evidence decisions, forecasts, and replication.
- P exports evidence only and can never alter O, A–N, or Q.
- Q is isolated physical continuation from O's exact restart state under the frozen law stack.

## Module Q terminal-cycle locks

Successful canonical RFC cycle closure requires a Big-Rip-class result:

```text
finite-time Big Rip
or effective Big Rip
or asymptotic Big-Rip completion
```

Recollapse, terminal stasis, reconnection, no terminal event, terminal-law insufficiency, unresolved branches, and pathologies may be valid physical outputs, but they are nonclosure results for the canonical RFC cycle unless they satisfy the Big-Rip-class predicates.

The protected cycle order is:

```text
RFL_s^manifest
-> M_rec,s^latent
-> CIF_(s+1)^eff
-> RFL_A,(s+1)^pre
-> BigImplosion_(s+1)
-> RFL_B,(s+1)^phys
```

All five states are distinct.

- The old manifested RFL dissolves route by route.
- Latent memory is a qualified source-relevant residue, not an active surviving universe.
- Memory conditions but does not equal the next CIF.
- The unchanged First Action remains prephysical.
- The next Big Implosion remains Module B's sole first physical event.
- Module Q authorizes the next A→B sequence but does not execute the next Big Implosion.
- No external reset, exact-copy recurrence, memory-erasure recurrence, Module P input, or public branch selection is allowed.
- One cycle does not prove indefinite recurrence.

## Current scientific direction

The canonical A–Q scientific architecture, all detailed module/handoff plans, and the binding Wolfram revisions are complete.

The next work is the actual repository repair in module order. Start with Module A as already scientifically complete and frozen, integrate its full established science and its Wolfram verification workload into the repository, then repair Module B from its achieved boundary and continue through the sealed chain. Do not revive RUN014 or any old run-centered architecture.