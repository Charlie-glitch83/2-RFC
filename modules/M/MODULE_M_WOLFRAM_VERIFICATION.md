# Module M — Wolfram and Independent Verification

## Scope

Representative finite checks for the Module M law, proof, and corrected derivation lock. These verify algebra, positivity, conservative finite systems, covariance, restart, adaptive-network logic, and K–L–M recurrence classification. They are not empirical abundance validation.

## Wolfram checks

Exact Wolfram evaluation returned:

```text
BaryonResidual -> {0,0,0,0,0,0,0}
ChargeResidual -> {0,0,0,0,0,0,0}
EntropyCounterexample -> False
DecayColumnSums -> {0,0,0}
DecayRestartResidual -> zero 3x3 matrix
YieldPartitionResidual -> {0,0,0,0}
DustSubsetMargins -> {9/8,27/40,3/8,9/40}
TransportMassResidual -> 0
TransportNonnegative -> True
PhaseExchangeResidual -> {0,0,0}
AncestryColumnSums -> {1,1}
OpacityPositive -> True
CovariancePositive -> True
AdaptiveBeforeMax -> 2/25
AdaptiveAfterMax -> 3/500
AdaptiveDetectsAndCloses -> {True,True}
KLMFixedPoint -> {70034/50451,14409/16817,23912/50451}
KLMFixedPointResidual -> {0,0,0}
KLMSpectralRadiusNumeric -> 0.3023252586261425714...
KLMContractive -> True
KLMNonconvergentEigenvalues -> {101/100,2/5,1/5}
KLMNonconvergentDetected -> True
```

Positive operator eigenvalues were:

```text
OpacityEigenvaluesNumeric ->
{0.60674740867381052039...,0.10025259132618947961...}

CovarianceEigenvaluesNumeric ->
{1.14141540277189322805...,0.47658459722810677195...}
```

The entropy evaluation searched the positive domain for a counterexample to `(x-y) Log[x/y] >= 0` and returned `False`.

## Independent check

An independently written SciPy/NumPy script returned:

```text
MODULE_M_INDEPENDENT_CHECK: PASS
reaction_baryon_conservation=PASS
reaction_charge_conservation=PASS
network_positivity=PASS
network_invariant_AplusC=PASS
network_invariant_BplusC=PASS
detailed_balance_entropy_nonnegative=PASS
nuclear_energy_closure=PASS
radioactive_mass_conservation=PASS
radioactive_positivity=PASS
radioactive_restart=PASS
delayed_energy_partition=PASS
yield_decomposition=PASS
yield_nonnegative=PASS
dust_is_phase_subset=PASS
transport_mass_conservation=PASS
transport_positivity=PASS
gas_dust_exchange_conservation=PASS
source_ancestry_normalization=PASS
opacity_operator_psd=PASS
covariance_pushforward_psd=PASS
adaptive_growth_detects_incomplete=PASS
adaptive_growth_certifies_refined=PASS
klm_contractivity_classified=PASS
klm_fixed_point_residual=PASS
klm_nonconvergence_classified=PASS
```

Representative values:

```text
minimum entropy production = 1.461647935542746e-14
transport mass error = 5.551115123125783e-17
opacity eigenvalues = [0.10025259,0.60674741]
covariance eigenvalues = [0.47658460,1.14141540]
KLM spectral radius = 0.30232525862614273
KLM fixed point = [1.38815881,0.85681156,0.47396484]
```

The finite reaction coefficients were synthetic and used only to verify the declared law. No public rates, yields, or abundance targets generated the check.

## What is verified

At representative finite scope:

- baryon and charge invariants;
- positive reversible evolution and detailed-balance entropy production;
- energy-ledger closure;
- daughter-chain conservation and restart;
- exact yield partition and dust subset consistency;
- conservative positive isotope transport and phase exchange;
- normalized source ancestry;
- positive-semidefinite composition and covariance operators;
- adaptive-network incompleteness detection and refined closure;
- distinction between contractive and nonconvergent recurrence branches.

## Claim boundary

These checks do not prove empirical masses, rates, stellar or explosive yields, observed chemical agreement, a unique instantiated cosmic history, Module N assembly, Module O freeze, Module P comparison, or Module Q terminal closure. They establish internal consistency of the repaired Module M law at the declared finite-verification scope.
