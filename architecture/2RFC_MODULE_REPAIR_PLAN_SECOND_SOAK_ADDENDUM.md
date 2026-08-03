# 2-RFC Module Repair Plan — Second-Soak Addendum

**Repository:** `Charlie-glitch83/2-RFC`  
**Branch:** `agent/triadic-proof-rebuild`  
**Status:** binding working amendment to `2RFC_MODULE_BY_MODULE_SCIENTIFIC_REPAIR_PLAN.md`  
**Method:** module-first scientific repair; no adoption of the old fixed run-engineering system

---

## 1. Why this addendum exists

A second architecture soak recovered several requirements that were either compressed too aggressively or absent from the first module-repair plan. They do not change the governing strategy:

- the module remains the unit of work;
- the science from RUN 000–013 is carried into Modules A and B;
- the old fixed run sequence, preflight bureaucracy, and single-next-run operating system are not copied;
- calculations, proofs, solvers, and reproductions are created only when the active module scientifically requires them.

This addendum controls wherever it sharpens the earlier repair plan. It is not a replacement for the exact source-reconciled architecture, proof lock, or individualized A–Q plans, which still need to be installed and verified by hash.

---

## 2. Additional global architecture requirements

### 2.1 Canonical namespace and translation law

The repaired repository must prevent collisions among older and new objects. Every imported source object receives a namespace:

```text
P29::       Presentation 29 objects
P30::       Presentation 30 and Appendix J objects
NB::        N-body manuscript objects
PLAN::A-Q   individualized module-plan objects
RFC2::A-Q   repaired 2-RFC module objects
```

Unqualified names such as `Module G`, `Module N`, `kernel`, `memory`, or `state` are prohibited in canonical schemas and theorem ledgers when more than one source object could be meant.

A source-translation registry must explicitly reconcile:

- `(CIF,QV,RFL)` versus any historical tuple order;
- `Recursive Fractal Lattice` versus the N-body source alias `Recursive Feedback Loop`;
- Presentation 29 kernel depth beginning at `j=1` versus the N-body convention beginning at `j=0`;
- P29 modules, P30 STEPs/SU objects, N-body theorem objects, and repaired A–Q modules.

No source alias or index shift is accepted by informal relabeling.

### 2.2 Dual status registry

Every load-bearing object receives two independent classifications.

**Physics status:**

```text
D1  directly triad-derived
D2  RFC effective or limiting law
I1  frozen interface physics
B1  benchmark only
G1  governance-only
```

**Evidence status:**

```text
SOURCE_DEFINITION
SOURCE_THEOREM
SOURCE_ALGORITHM
NEW_INTEGRATION_THEOREM_TARGET
MODULE_THEOREM_TARGET
COMPUTATIONAL_CERTIFICATE_TARGET
EMPIRICAL_CERTIFICATE_TARGET
ARCHITECTURE_RULE
```

This prevents architecture prose, a schema, a source theorem, an implementation, and an empirical result from being treated as the same evidence class.

### 2.3 Obligation tiers

Every module obligation is classified before repair:

```text
CORE          required to close the module's active claim
CONDITIONAL   activated only by a named upstream witness or claimed scope
FUTURE        preserved as an interface but not allowed to block present closure
```

`NOT_APPLICABLE` is accepted only with a typed domain and claim-scope proof. Optional physical lanes must not create another permanent Module B-style stall.

### 2.4 Universal module contract

Every repaired module exports the common state form

```text
H_i = (
  S_i,          physical state
  Sigma_i,      uncertainty and covariance
  R_i,          directed relation registry
  E_i,          event, route, and branch ledger
  Mrec_i,       recursive memory and ancestry
  O_i,          generated intrinsic observables
  Pi_i,         provenance, code identity, and hashes
  F_i           falsifiers and mandatory gates
)
```

Each module must define, at minimum:

1. physical domain;
2. entities and state variables;
3. directed relations and routes;
4. local witnesses;
5. governing equations;
6. approximations and validity domains;
7. initial and boundary conditions;
8. conserved and transferred quantities;
9. events and branches;
10. recursive memory;
11. scale promotion and reopening;
12. uncertainty model;
13. numerical method where applicable;
14. intrinsic observables;
15. benchmark and validation suites;
16. falsifiers;
17. complete child handoff.

This is a scientific contract, not a required ten-run template.

### 2.5 Five closure classes

A module is not accepted under one vague word such as “complete.” Its closure matrix must separately record:

- **physical closure:** all processes necessary for the claimed state are executed or lawfully delegated and returned;
- **numerical closure:** equations, methods, convergence, conservation, and numerical error are established;
- **causal closure:** every output has a complete source, relation, route, event, and parent path;
- **uncertainty closure:** all material uncertainty and covariance are propagated;
- **observational closure:** where claimed, the actual measurable product and observation operator exist.

Most Modules A–N require the first four. Full instrument-facing observational closure belongs to P.

### 2.6 Universal triadic derivation tests

A claim that a law or state derives from the triad must address:

- sufficiency;
- necessity through ablation;
- irreducibility of CIF, QV, and RFL;
- identifiability against comparably flexible alternatives;
- persistence across scales and representations;
- recovery of established valid limits;
- at least one discriminating consequence frozen before comparison.

These are cross-module scientific tests, not Module P-only statistics.

### 2.7 Carrier lifecycle state machine

The carrier status must be explicit in every module:

```text
PRESERVED_DORMANT
GRAMMAR_ACTIVE
DOMAIN_ACTIVE(N)
EVENT_ACTIVE
PROMOTED_CONTINUUM
LATENT
REACTIVATED
```

- `GRAMMAR_ACTIVE` means packet, witness, route, branch, event, memory, and no-loss rules are used without claiming the Newtonian N-body dynamical theorem solves the domain.
- `DOMAIN_ACTIVE(N)` requires a domain-specialization theorem and activation witnesses.
- `PROMOTED_CONTINUUM` requires a reopening/no-loss certificate.
- `LATENT` and `REACTIVATED` are terminal/cross-cycle states, not ordinary downstream persistence.

Dormancy must be tested operationally:

1. the module's physical output is unchanged whether the dormant carrier is present or absent; and
2. the carrier payload itself remains content-equivalent and unmodified.

### 2.8 Infinite lawful manifestation target

Module A and the final proof must preserve the theorem target:

> The primitive triad is finite in constitution and unbounded in lawful manifestation.

Unbounded manifestation is carried through arbitrary finite-N extension, recursive depth, lawful route multiplicity, event and branch structure, scale promotion/reopening, records and observers, and recurrent cycles. It does not require one actually infinite body system.

### 2.9 Multi-fidelity science without run bureaucracy

The useful scientific fidelity ladder is retained:

```text
F0 exact and analytic
F1 fully resolved local
F2 coupled intermediate
F3 large statistical
F4 targeted reopening/refinement
```

These are fidelity classes, not fixed run numbers. A module uses only the fidelities needed for its active claim. Overlap regions must agree before a precision claim is admitted.

### 2.10 Numerical and reproduction standards

Where an exact proof is not sufficient:

- use at least three ordered resolutions or tolerances when estimating convergence;
- estimate observed convergence order where the algorithm predicts one;
- require an independent implementation for load-bearing results;
- declare the relevant reproduction class for every object:

```text
BITWISE
DETERMINISTIC_EVENT_EQUIVALENCE
TOLERANCE_DEFINED_STATE_EQUIVALENCE
STATISTICAL_DISTRIBUTION_EQUIVALENCE
PHYSICAL_EQUIVALENCE
SCIENTIFIC_CONCLUSION_EQUIVALENCE
```

### 2.11 Uncertainty, sensitivity, and identifiability

Every module must propagate parent, model, numerical, stochastic, branch, and interface uncertainty. Cross-module covariance may not be discarded when materially relevant.

Each major output requires a sensitivity map identifying:

- dominant dependencies;
- fragile claims;
- unidentifiable freedoms;
- error-amplifying interfaces;
- best discriminating observables.

Uncertainty propagation is allowed under no-retune. Public residuals may not alter the frozen generative uncertainty distribution within the same validation branch.

### 2.12 Conservation-surface handoffs

Every parent-child boundary is simultaneously a:

- state surface;
- conservation and transfer surface;
- identity surface;
- uncertainty/covariance surface;
- ancestry/provenance surface;
- restart surface.

A child may not recreate a missing parent quantity from public information or a conventional default.

### 2.13 Empirical calibration restriction

The lower-level standard describes temporary I1 calibration as a possible interface class, but the higher source-reconciled lock controls. No empirical calibration may enter A–O or Q unless an exact higher-authority object explicitly authorizes the specific anchor, role, dataset, and freeze point. Otherwise all public information remains confined to P.

---

## 3. Module-specific additions

## Module A additions

The first plan already captured most Module A science. Add these explicit requirements:

- store the exact carrier lifecycle state in every downstream handoff;
- distinguish `GRAMMAR_ACTIVE` from `DOMAIN_ACTIVE` so relational governance can be used without overclaiming a domain solution;
- prove dormancy by physical-output equivalence and payload preservation;
- assign evidence status to inherited theorems versus new integration targets;
- register the infinite-lawful-manifestation theorem target;
- make source translation and namespace closure part of Module A acceptance.

## Module B additions

The first plan correctly carries RUN 008–013 science. Add:

- separate the **first physical geometry/pregeometry constitution** from the mature cosmological background solved in I;
- classify dimension, signature, topology, connection, locality, and causal structure as a lawful branch family until uniquely selected by source law;
- specify which sector laws are background laws, perturbation laws, constitutive laws, or dormant interfaces;
- require a complete Module C parent packet containing stress-energy/constraint registries and sector transfer contracts;
- preserve the distinction between graph-resolvent compression, relational geometry, physical causal structure, and later relativistic geometry.

## Module C additions

Add explicit completion items from the individualized plan:

- anomaly cancellation and gauge consistency;
- normalized microscopic probability law;
- massless-state protection;
- elementary/effective/collective/composite classification;
- flavor, generation, mixing, oscillation, and CP-facing structures;
- a derived or explicitly frozen asymmetry-source contract rather than an assigned baryon asymmetry;
- a complete prethermal equation of state and uncertainty packet.

Module C stops before thermal chronology. Electroweak and strong-sector thermal events belong to D even when C defines the microscopic identities needed for them.

## Module D additions

The initial repair plan understated Module D. The repaired module must explicitly include:

- a lawful map among physical time, temperature, early geometric scale, recursive depth, and cycle index while keeping all five types distinct;
- species temperatures or full phase-space distributions when one scalar temperature is invalid;
- a channel-complete collision network and reverse-rate/detailed-balance audit;
- nonequilibrium electroweak-facing transition or crossover;
- baryogenesis/leptogenesis, conversion, transport, spectator effects, washout, and survival;
- strong-sector thermal transition and hadronization;
- particle-antiparticle pair balance and annihilation;
- general freeze-out and decoupling surfaces;
- neutrino transport and electron-positron entropy transfer;
- visible-dark transport and decoupling;
- plasma collective, magnetic, turbulent, shock, defect, and gravitational-wave source lanes only when dynamically generated;
- a thermal-memory packet preserving phase order, freeze-out order, entropy transfer, chemical history, defects, relics, neutrinos, branches, and route ancestry.

Two terminal states with identical temperatures and densities may remain physically distinct when their histories differ. They cannot be scalar-quotiented without a no-loss theorem.

## Module E additions

Add:

- reverse reactions derived from the same registry as forward rates;
- partition-function, chemical-potential, equilibrium, and microscopic-reversibility checks;
- plasma, screening, finite-temperature, recoil, weak-magnetism, radiative, density, and quantum-statistical corrections where material;
- radiation, lepton, entropy, and background feedback when required by precision;
- backward isotope-ancestry queries from final species to reaction paths;
- a full abundance trajectory and event history, not only the terminal abundance vector;
- correlated multi-isotope predictions from one frozen parent universe.

## Module F additions

Module F is not only persistence bookkeeping. It must:

- evolve the time-temperature-density-scale relation across the full post-nuclear interval;
- preserve isotope and reaction ancestry after nuclear freeze-out;
- evolve photons, electrons/positrons, ions, nuclei, neutrinos, dark sectors, fields, perturbations, transport coefficients, and spectral distortions;
- carry radioactive decay schedules and residual reaction channels;
- generate the atomic-capture/recombination-readiness witness without performing G's recombination;
- keep astrophysical reionization outside F and G's primordial chronology.

## Module G additions

Add:

- materially relevant deuterium and light-element atomic effects;
- frequency-dependent line and continuum transport;
- resonance escape, redistribution, and two-photon processes;
- separate finite probability surfaces for photon last scattering and baryon drag release;
- complete visibility moments, width, skewness, spatial perturbation, and frequency dependence;
- recombination radiation and intrinsic spectral distortions;
- a separate extension interface for later astrophysical reionization so primordial recombination is never conflated with it.

## Module H additions

Add:

- a complete regular initial-mode basis over every active scalar, vector, tensor, entropy, compensated, and dark-sector mode;
- adaptive multipole, momentum, species, time, and wavenumber refinement;
- direct hierarchy versus line-of-sight reconstruction agreement;
- computational-gauge independence of physical observables;
- exact normalization and branch compatibility among the mode basis, `H^U`, `I`, and `H[I]`;
- Green functions, basis responses, derivatives, and covariance-propagation maps as explicit J exports.

## Module I additions

The repaired Module I must additionally:

- reproduce the finalized D, E, F, and G chronology on the accepted background rather than overwrite it;
- derive or explicitly classify Etherington reciprocity and any RFC violation;
- generate redshift drift, lookback/age, standard-clock, ruler, and siren maps;
- generate internal BAO-ruler and supernova geometric packets without observational calibration fitting;
- classify flatness, isotropy, topology, averaging, and backreaction rather than assuming them;
- test ghost-like, gradient, sound-speed, hyperbolicity, superluminal, horizon, transfer-current, and curvature pathologies;
- retain all lawful curvature, exchange, and dark-sector branches rather than selecting one by public data.

## Module J additions

Add:

- explicit separation of internal realization/cosmic variance from instrument and survey covariance, which belongs to P;
- a complete covariance closure family rather than forced diagonality;
- finite positive mass, position, velocity, momentum, stress, metric, and species carriers for K;
- conservation and reconstruction tests proving the promoted finite realization recovers the parent linear fields;
- explicit infrared/ultraviolet control and a witnessed nonlinear-validity surface;
- branch preservation for exact source degeneracies, mode families, parity, helicity, and non-Gaussian structure.

## Module K additions

Add:

- void formation, compensation walls, merging/crushing, velocity, topology, dark-sector response, and lensing as physical dynamics rather than catalogue emptiness;
- object-finder and web-classifier covariance;
- an explicit compact-object/strong-field promotion boundary carrying mass, momentum, spin, charge, multipoles, recoil, gravitational-wave interfaces, uncertainty, and ancestry;
- independent direct-geodesic, Jacobi, lens-plane, and Born/harmonic lensing routes over their shared domains;
- nonlinear compression-relic, dissipative-tail, neutrino, and free-streaming treatment according to their own constitutive laws rather than standard templates;
- final acceptance only after K–L–M convergence or lawful branch/cycle classification.

## Module L additions

Add:

- the initial mass function as the distribution of physically completed stellar-birth events, not an imposed sampling rule;
- multiplicity, clusters, angular momentum, and birth correlations generated from the collapse state;
- coordinated supernova dynamics with M so energy, remnant, and yields remain one event;
- compact-remnant and binary lineages with strong-field/GW handoff to K;
- cosmic-dawn, ionizing-source, and astrophysical-reionization packets for N;
- overlap tests between directly resolved stars and promoted stellar populations.

## Module M additions

Add:

- explicit separation of total, net, retained, fallback, escaped, radioactive, and dust-bearing yields;
- spatially resolved enrichment parcels and delayed deposition;
- chemical inhomogeneity, incomplete mixing, source clustering, gradients, phase segregation, host variance, and enrichment age;
- prohibition on replacing the state with one homogeneous metallicity scalar;
- composition-dependent opacity, emissivity, cooling, heating, and radiation coupling;
- molecular chemistry only where source-identified and materially necessary; planetary, prebiotic, and biospheric chemistry remain outside the claim;
- isotope mass and source ancestry conservation through every phase exchange.

## Module N additions

The repaired Module N must explicitly implement three observer tiers:

```text
Tier 1  geometric observer event
Tier 2  physical observing system
Tier 3  recursive identity candidate
```

- Tier 1 owns location, four-velocity, tetrad, proper time, causal past, and frame.
- Tier 2 requires receiving channels, physical state transitions, memory storage, finite resolution, internally generated noise, energy/information costs, causal position, outputs, and degradation/decoherence history.
- Tier 3 additionally requires a defined dynamical state space, memory/feedback relation, identity-continuity criterion, stability/attractor analysis, energy/dissipation account, and lineage.

No tier proves subjective experience. Cognitive/self-model extensions remain a separate theorem.

Module N must also:

- distinguish observer, apparatus, target, signal, environment, record, and branch identity;
- distinguish physical decoherence, stochastic branching, deterministic multichart continuation, unresolved model branching, ensemble variance, numerical splitting, and discarded numerical branches;
- classify identity through persistence, transformation, replacement, copying, splitting, merging, dormancy, reactivation, termination, and descendant relations;
- distinguish recursive memory, dynamical memory, physical records, numerical checkpoints, and archival provenance;
- freeze astrophysical reionization and later radiation backgrounds from generated sources;
- preserve the consciousness firewall.

## Module O additions

Add:

- artifact-specific equivalence classes: bitwise, numerical, statistical, physical, and scientific;
- adversarial checks for hidden caching, copied outputs, mutable shared state, rollback, seed drift, precision drift, environment drift, and branch contamination;
- archive redundancy and integrity verification;
- semantic migration rules that preserve scientific identity if formats or media change;
- deterministic restoration for deterministic objects and controlled statistical replay for stochastic/ensemble objects;
- a proof that every protected object is reachable from one universe root manifest.

A ZIP file and checksum list are not sufficient.

## Module P additions

Add:

- explicit dataset roles: calibration, validation, and prediction/withheld future test;
- a registry of microscopic/laboratory/local-gravity, expansion, CMB/recombination, abundance, linear-growth, nonlinear-structure, lensing/relativity, stellar/chemical, compact-object/GW/transient, and Big-Implosion/cycle probes;
- multiple-testing control, coverage/calibration tests, posterior-predictive checks where applicable, outlier/tail analysis, systematic-error decomposition, and cross-survey consistency;
- full map/catalogue/event-level forward modeling before summary statistics;
- source-identifiability tests against comparably flexible alternatives;
- preservation of prediction status and first-exposure timestamps;
- no cross-probe cancellation of a mandatory failure.

## Module Q additions

Module Q received the largest second-soak correction.

It must separately track:

```text
S_therm      thermodynamic entropy
S_horizon    horizon/geometric entropy
S_ent        entanglement entropy for a declared partition
S_coarse     representation-dependent coarse-grained entropy
S_rec        recursive depth-memory entropy
```

No next-cycle claim may rely on an unexplained global entropy reset.

Every terminal degree of freedom receives one information status:

```text
ManifestAndAccessible
ManifestButCausallyInaccessible
TransferredToRadiation
EncodedOnOrAcrossHorizon
DynamicallyErased
CoarseGrainedOnly
GaugeOrRepresentationRedundant
QualifiedLatentMemory
NotResolvedWithinModel
```

Simulation provenance does not automatically count as physical surviving memory.

The terminal equivalence relation and no-loss quotient must preserve every distinction required by any permitted next-source construction. The module must prove memory capacity is finite or has a controlled infinite-depth representation.

The terminal branch taxonomy must distinguish:

- finite-time Big-Rip class;
- effective route-separation Big-Rip class;
- asymptotic dissipative completion capable of lawful memory qualification;
- tail-transition realization;
- nonclosure or other lawful terminal result.

Under the higher canonical cycle lock, successful canonical closure requires a Big-Rip-class realization. Other lawful outcomes are retained as exact nonclosure/falsification results, not renamed as successful cycles.

The claim ledger must distinguish:

```text
one terminal branch established
one completed cycle established
finite multi-cycle behavior established
indefinite-cycle theorem established
```

These claims are not interchangeable.

Verification must include at least a two-cycle replay and finite multi-cycle tests for:

- memory drift;
- saturation;
- refresh;
- obstruction;
- branch proliferation;
- law/source identity;
- cumulative hidden retuning;
- novelty versus exact-copy failure;
- memory-erasure failure.

Module Q constructs the qualified memory, next effective CIF, and authorization packet. The next Module B instance—not Q—executes the next Big Implosion.

---

## 4. Revised module repair acceptance record

For each module, the repository should maintain a compact decision table:

```text
objectID
sourceNamespace
physicsStatus
 evidenceStatus
obligationTier
repairDecision       KEEP | STRENGTHEN | REPLACE | ADD | QUARANTINE
parentDependencies
childUses
closureClasses
validationMethod
reproductionClass
claimAuthorized
claimBlocked
falsifier
```

This replaces vague statements that a module “looks complete.”

---

## 5. Effect on the repair sequence

The repair sequence remains unchanged:

1. install and verify exact architecture, lock, and A–Q plans;
2. repair A using RUN 000–007 science without its machinery;
3. repair B using RUN 008–013 science without its machinery;
4. repair C through J in causal order, preserving the H/I split;
5. repair K, L, and M individually and close their coupled physical state;
6. repair N, freeze O, and open isolated P/Q siblings.

The additional standards are applied inside each module. They do not create a new global run bureaucracy or another prerequisite wall before scientific progress.