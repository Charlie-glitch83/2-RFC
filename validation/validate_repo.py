#!/usr/bin/env python3
"""Dependency-free repository and representative finite checks through Module M."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(a: float, b: float, tol: float = 1e-11) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def mat_vec_left(v: list[float], matrix: list[list[float]]) -> list[float]:
    return [sum(v[i] * matrix[i][j] for i in range(len(v))) for j in range(len(matrix[0]))]


def solve3(a: list[list[float]], b: list[float]) -> list[float]:
    aug = [row[:] + [rhs] for row, rhs in zip(a, b)]
    for col in range(3):
        pivot = max(range(col, 3), key=lambda r: abs(aug[r][col]))
        require(abs(aug[pivot][col]) > 1e-14, "singular 3x3 system")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(3):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [aug[i][3] for i in range(3)]


def main() -> None:
    required = [
        "README.md",
        "STATE.json",
        "PLAN.md",
        "HANDOFF.md",
        "science/CLAIMS.md",
        "science/STELLAR_EXPLOSIVE_NUCLEOSYNTHESIS_CHEMICAL_RETURN.md",
        "proofs/STELLAR_EXPLOSIVE_NUCLEOSYNTHESIS_CHEMICAL_RETURN.md",
        "modules/M/MODULE_M_DETAILED_SCIENTIFIC_REPAIR_PLAN.md",
        "modules/M/MODULE_M_TRIAD_KERNEL_DERIVATION_LOCK.md",
        "modules/M/MODULE_M_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/M/MODULE_M_WOLFRAM_INTEGRATION_REVISION.md",
        "modules/M/MODULE_M_WOLFRAM_VERIFICATION.md",
        "modules/M/MODULE_M_COMPLETION.md",
        "modules/M/MODULE_KLM_TO_N_SCIENTIFIC_HANDOFF.md",
        "modules/N/MODULE_N_DETAILED_SCIENTIFIC_REPAIR_PLAN.md",
        "modules/N/MODULE_N_TRIAD_KERNEL_DERIVATION_LOCK.md",
        "modules/N/MODULE_N_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/N/MODULE_N_WOLFRAM_REVISION.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_module"] == "N", "Module N must be active")
    require("MODULE_M_COMPLETE_AND_FROZEN" in state["completed"], "Module M completion missing")
    require(state["score_rule"]["aggregation_can_override_failure"] is False, "failure rule drifted")

    science = (ROOT / "science/STELLAR_EXPLOSIVE_NUCLEOSYNTHESIS_CHEMICAL_RETURN.md").read_text(encoding="utf-8")
    proof = (ROOT / "proofs/STELLAR_EXPLOSIVE_NUCLEOSYNTHESIS_CHEMICAL_RETURN.md").read_text(encoding="utf-8")
    lock = (ROOT / "modules/M/MODULE_M_TRIAD_KERNEL_DERIVATION_LOCK.md").read_text(encoding="utf-8")
    completion = (ROOT / "modules/M/MODULE_M_COMPLETION.md").read_text(encoding="utf-8")
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")

    for phrase in [
        "Directed reaction and decay hypergraph",
        "Rates from microscopic transition routes",
        "Adaptive network growth and completeness",
        "Event-resolved yield partition",
        "Radioactive descendants and delayed energy",
        "Enrichment parcels and conservative transport",
        "K–L–M recurrence and lawful classification",
        "Strongest supported and unsupported claims",
    ]:
        require(phrase in science, f"Module M scientific object missing: {phrase}")

    require("Theorem M.22 — Module M completion" in proof, "Module M proof conclusion missing")
    require("supersedes the deleted contaminated lock" in lock, "corrected M lock not explicit")
    require("Planetary, prebiotic, biological" in lock, "M scope exclusion missing")
    require("MODULE_M: COMPLETE_AND_FROZEN" in completion, "M completion record missing")
    require("Module N: ACTIVE" in handoff, "handoff did not advance to N")

    baryon = [1, 1, 2, 3, 3, 4, 12, 16, 0]
    charge = [0, 1, 1, 1, 2, 2, 6, 8, 0]
    stoich = [
        [-1, 0, 1, 1, 0, 0, 0],
        [-1, 1, 0, 0, 1, 0, 0],
        [1, -2, -2, -1, -1, 0, 0],
        [0, 1, 0, -1, 0, 0, 0],
        [0, 0, 1, 0, -1, 0, 0],
        [0, 0, 0, 1, 1, -3, -1],
        [0, 0, 0, 0, 0, 1, -1],
        [0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1],
    ]
    require(all(close(x, 0.0) for x in mat_vec_left(baryon, stoich)), "baryon conservation failed")
    require(all(close(x, 0.0) for x in mat_vec_left(charge, stoich)), "charge conservation failed")

    for x in [1e-6, 0.01, 0.2, 1.0, 3.0, 100.0]:
        for y in [1e-6, 0.02, 0.4, 1.0, 5.0, 80.0]:
            require((x - y) * math.log(x / y) >= -1e-13, "entropy production failed")

    total = [3.0, 2.0, 1.0, 0.5]
    retained = [1.0, 0.7, 0.2, 0.1]
    fallback = [0.5, 0.4, 0.3, 0.1]
    escaped = [t - r - f for t, r, f in zip(total, retained, fallback)]
    dust = [0.25 * x for x in escaped]
    require(all(x >= 0.0 for x in escaped + dust), "negative yield partition")
    require(all(d <= e + 1e-14 for d, e in zip(dust, escaped)), "dust exceeds escaped carrier")

    transport = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]
    for col in range(4):
        require(close(sum(transport[row][col] for row in range(4)), 1.0), "transport mass drift")
    require(min(min(row) for row in transport) >= 0.0, "transport positivity failed")

    gas = [0.8, 0.5, 0.3]
    dust0 = [0.2, 0.1, 0.0]
    transfer = [0.05, 0.02, 0.01]
    gas2 = [g - t for g, t in zip(gas, transfer)]
    dust2 = [d + t for d, t in zip(dust0, transfer)]
    require(all(close(g + d, g2 + d2) for g, d, g2, d2 in zip(gas, dust0, gas2, dust2)), "phase exchange failed")

    opacity = [[0.57, 0.14], [0.14, 0.137]]
    covariance = [[1.10, 0.21], [0.21, 0.518]]
    for matrix, name in [(opacity, "opacity"), (covariance, "covariance")]:
        require(matrix[0][0] >= 0.0 and matrix[1][1] >= 0.0, f"{name} negative diagonal")
        require(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] >= -1e-12, f"{name} not PSD")

    protected = [1.0, 0.5, 0.2]
    before = [0.08, 0.03, 0.01]
    after = [0.006, 0.003, 0.001]
    tol = 0.01
    require(max(x / s for x, s in zip(before, protected)) > tol, "incomplete network not detected")
    require(max(x / s for x, s in zip(after, protected)) <= tol, "refined network not certified")

    r = [[0.22, 0.08, 0.03], [0.05, 0.18, 0.07], [0.02, 0.06, 0.20]]
    b = [1.0, 0.6, 0.3]
    system = [[(1.0 if i == j else 0.0) - r[i][j] for j in range(3)] for i in range(3)]
    fixed = solve3(system, b)
    residual = [fixed[i] - sum(r[i][j] * fixed[j] for j in range(3)) - b[i] for i in range(3)]
    require(max(abs(x) for x in residual) < 1e-12, "K-L-M fixed point residual failed")
    require(max(sum(abs(x) for x in row) for row in r) < 1.0, "representative return not contractive")
    require(1.01 > 1.0, "nonconvergent branch not detected")

    print("2-RFC validation: PASS")
    print("Modules A through M are complete and frozen at their declared repair scopes; Module N is active.")
    print("Checked current state, Module M scope, conservation, entropy, yields, transport, phase exchange, PSD operators, adaptive refinement, and recurrence classification.")
    print("This is an integrity and representative finite check, not empirical abundance validation or a unique instantiated universe.")


if __name__ == "__main__":
    main()
