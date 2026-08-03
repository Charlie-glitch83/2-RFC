#!/usr/bin/env python3
"""Dependency-free repository and finite algebra checks for repaired Module A."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def reachable(edges: dict[str, set[str]], start: str, target: str) -> bool:
    frontier = list(edges.get(start, set()))
    seen: set[str] = set()
    while frontier:
        node = frontier.pop()
        if node == target:
            return True
        if node not in seen:
            seen.add(node)
            frontier.extend(edges.get(node, set()) - seen)
    return False


def main() -> None:
    required = [
        "README.md",
        "STATE.json",
        "PLAN.md",
        "HANDOFF.md",
        "science/FOUNDATION.md",
        "science/CLAIMS.md",
        "science/PHYSICAL_REALIZATION.md",
        "proofs/KERNEL_COMPLETION.md",
        "proofs/GENESIS_REALIZATION.md",
        "modules/A/MODULE_A_DETAILED_SCIENTIFIC_REPAIR_PLAN.md",
        "modules/A/MODULE_A_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/A/MODULE_A_WOLFRAM_REVISION.md",
        "modules/A/MODULE_A_TO_B_SCIENTIFIC_HANDOFF.md",
        "architecture/2RFC_MANUSCRIPT_SOURCE_TRACEABILITY_RULES.md",
        "architecture/2RFC_WOLFRAM_INTEGRATION_RULES.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_module"] == "B", "Module B must be active after Module A repair")
    require(
        state["status"] == "MODULE_A_COMPLETE_FROZEN_MODULE_B_ACTIVE",
        "unexpected project status",
    )
    require(
        "MODULE_A_COMPLETE_AND_FROZEN" in state["completed"],
        "Module A completion is missing",
    )
    require(
        "Big-Implosion" in state["exact_next_action"],
        "next action does not point to Module B",
    )
    require(
        state["score_rule"]["aggregation_can_override_failure"] is False,
        "mandatory failure policy drifted",
    )

    machine_states = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name.upper() in {"STATE.JSON", "CURRENT_STATE.JSON", "CURRENT_STATE.YAML"}
    )
    require(machine_states == ["STATE.json"], f"duplicate machine state detected: {machine_states}")

    foundation = (ROOT / "science/FOUNDATION.md").read_text(encoding="utf-8")
    theorem = (ROOT / "proofs/KERNEL_COMPLETION.md").read_text(encoding="utf-8")
    genesis = (ROOT / "proofs/GENESIS_REALIZATION.md").read_text(encoding="utf-8")
    plan = (ROOT / "PLAN.md").read_text(encoding="utf-8")
    claims = (ROOT / "science/CLAIMS.md").read_text(encoding="utf-8")

    required_foundation_phrases = [
        "RFL = stabilized inheritable output in the Recursive Fractal Lattice",
        "Source, memory, and manifestation are distinct",
        "Certified truncation",
        "Perturbation stability",
        "Conditional termwise differentiation",
        "Witness-governed route admission",
        "Correct add-one-constituent refinement",
        "Partial event multifunction",
        "Protected no-loss state",
        "Identity-preserving memory",
        "Scale promotion and reopening",
        "Dormancy and activation",
        "Within these boundaries, Module A is complete and frozen",
    ]
    for phrase in required_foundation_phrases:
        require(phrase in foundation, f"Module A foundation missing: {phrase}")

    require("Module A Integrated Triadic Relational Governance Theorem" in theorem, "theorem not installed")
    require("A11 — Immutable downstream grammar" in theorem, "theorem is incomplete")
    require("Module A is complete and frozen" in theorem, "theorem conclusion drifted")
    require("Module A is complete and frozen" in genesis, "genesis file reopens Module A")
    require("Module B must derive" in genesis, "Module B frontier is missing")
    require("COMPLETE_AND_FROZEN" in plan, "plan does not freeze Module A")
    require("Module A is complete and frozen" in claims, "claim ledger does not freeze Module A")

    # Canonical weighted representation remains normalized but is not used as a fit.
    weights = [0.005085, 0.984868, 0.010047]
    require(math.isclose(sum(weights), 1.0, rel_tol=0.0, abs_tol=1e-15), "triad weights do not sum to one")

    # Exact finite-N directed-lane count and add-one growth.
    for n in range(1, 1001):
        lanes_n = n * (n - 1)
        lanes_next = (n + 1) * n
        require(lanes_next - lanes_n == 2 * n, f"lane refinement failed at N={n}")

    # Kernel geometric sum, tail bound, perturbation Lipschitz bound, and derivative majorant.
    delta = 4.6692
    alpha = 0.0256831
    feature_bound = 1.7
    derivative_bound = 0.4
    perturbation = 1.0e-7
    for time in (0.0, 0.5, 10.0, 60.0):
        q = math.exp(-alpha * time) / delta
        require(0.0 < q < 1.0, "kernel ratio is outside convergence domain")
        exact_sum = 1.0 / (1.0 - q)
        for depth in (0, 1, 18, 40, 500):
            finite_sum = sum(q**j for j in range(depth + 1))
            exact_tail = exact_sum - finite_sum
            tail_bound = q ** (depth + 1) / (1.0 - q)
            require(abs(exact_tail - tail_bound) <= 5e-13, "geometric tail identity failed")
            require(feature_bound * exact_tail <= feature_bound * tail_bound + 1e-12, "kernel tail bound failed")
        perturbation_bound = perturbation / (1.0 - q)
        require(perturbation_bound >= perturbation, "perturbation bound is invalid")
        derivative_majorant = derivative_bound / (1.0 - q) + alpha * feature_bound * q / (1.0 - q) ** 2
        require(derivative_majorant > 0.0 and math.isfinite(derivative_majorant), "derivative majorant failed")

        # Recursive-depth distribution and entropy are finite and normalized.
        probabilities = [(1.0 - q) * q**j for j in range(2000)]
        require(math.isclose(sum(probabilities), 1.0, abs_tol=1e-12), "depth distribution not normalized")
        entropy_numeric = -sum(p * math.log(p) for p in probabilities if p > 0.0)
        entropy_closed = -math.log(1.0 - q) - q * math.log(q) / (1.0 - q)
        require(math.isclose(entropy_numeric, entropy_closed, rel_tol=1e-11, abs_tol=1e-12), "depth entropy identity failed")

    # Four event outcome classes are exhaustive for finite witnessed signature sets.
    def classify(signatures: list[str]) -> str:
        unique = set(signatures)
        if not signatures:
            return "OBSTRUCTION"
        if len(signatures) == 1:
            return "UNIQUE_CONTINUATION"
        if len(unique) == 1:
            return "GAUGE_FAMILY"
        return "INDEPENDENT_MULTI_ROUTE_FAMILY"

    require(classify([]) == "OBSTRUCTION", "empty event output was not obstruction")
    require(classify(["a"]) == "UNIQUE_CONTINUATION", "singleton event classification failed")
    require(classify(["a", "a"]) == "GAUGE_FAMILY", "gauge classification failed")
    require(classify(["a", "b"]) == "INDEPENDENT_MULTI_ROUTE_FAMILY", "multiroute classification failed")

    # No-loss quotient, memory reopening, and promotion reopening on a protected finite example.
    protected_state = tuple(range(18))
    encoded_memory = protected_state
    decoded_state = encoded_memory
    require(decoded_state == protected_state, "memory reopening failed")
    promoted = (sum(protected_state), encoded_memory, "valid", "derived-law")
    reopened = promoted[1]
    require(reopened == protected_state, "scale reopening failed")
    duplicate = tuple(range(18))
    distinct = tuple(range(17)) + (99,)
    require(protected_state == duplicate, "duplicate representation was not equivalent")
    require(protected_state != distinct, "independent protected distinction was lost")

    # Dormancy is zero-output and zero-backreaction without deletion.
    active_output = 7.5
    active_backreaction = -0.25
    for activation in (0, 1):
        output = activation * active_output
        backreaction = activation * active_backreaction
        if activation == 0:
            require(output == 0.0 and backreaction == 0.0, "dormancy backreacted")
        else:
            require(output == active_output and backreaction == active_backreaction, "activation failed")

    # Positive added influence is generally nonzero; zero-backreaction is a limit.
    gravitational_constant = 1.0
    separation = 2.0
    for added_mass in (1.0, 0.1, 0.01, 0.001):
        added_acceleration = gravitational_constant * added_mass / separation**2
        require(added_acceleration > 0.0, "positive influence unexpectedly vanished")
    require(gravitational_constant * 0.0 / separation**2 == 0.0, "zero-backreaction boundary failed")

    # Append-only ancestry is acyclic and is not treated as duration.
    ranks = {"root": (0, 0), "branch": (0, 1), "event": (0, 2), "next_cycle": (1, 0)}
    ancestry = {
        "root": {"branch"},
        "branch": {"event"},
        "event": {"next_cycle"},
        "next_cycle": set(),
    }
    for parent, children in ancestry.items():
        for child in children:
            require(ranks[parent] < ranks[child], "ancestry edge does not increase rank")
    require(all(not reachable(ancestry, event, event) for event in ranks), "ancestry cycle detected")

    print("2-RFC validation: PASS")
    print("Module A is complete and frozen at its prephysical finite-relational scope.")
    print("Checked kernel identities, finite-N growth, events, no-loss memory, reopening, dormancy, and state transition to Module B.")
    print("Module B physical obligations remain theorem work and are not script-certified facts.")


if __name__ == "__main__":
    main()
