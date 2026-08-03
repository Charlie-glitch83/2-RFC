#!/usr/bin/env python3
"""Dependency-free integrity and finite-algebra checks through the Module C boundary."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def solve_linear(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    aug = [row[:] + [rhs] for row, rhs in zip(matrix, vector)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        require(abs(aug[pivot][col]) > 1e-14, "singular validation matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return [aug[row][-1] for row in range(n)]


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(column) for column in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def close(a: float, b: float, tol: float = 1e-11) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def main() -> None:
    required = [
        "README.md",
        "STATE.json",
        "PLAN.md",
        "HANDOFF.md",
        "science/FOUNDATION.md",
        "science/PHYSICAL_REALIZATION.md",
        "science/MICROSCOPIC_PHYSICS.md",
        "science/CLAIMS.md",
        "proofs/KERNEL_COMPLETION.md",
        "proofs/GENESIS_REALIZATION.md",
        "proofs/MICROSCOPIC_CONSTITUTION.md",
        "modules/A/MODULE_A_TO_B_SCIENTIFIC_HANDOFF.md",
        "modules/B/MODULE_B_TO_C_SCIENTIFIC_HANDOFF.md",
        "modules/C/MODULE_C_DETAILED_SCIENTIFIC_REPAIR_PLAN.md",
        "modules/C/MODULE_C_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/C/MODULE_C_WOLFRAM_INTEGRATION_REVISION.md",
        "modules/C/MODULE_C_WOLFRAM_VERIFICATION.md",
        "modules/C/MODULE_C_TO_D_SCIENTIFIC_HANDOFF.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_module"] == "C", "Module C must be active")
    require(
        state["status"]
        == "MODULES_A_B_COMPLETE_FROZEN_MODULE_C_PARTIALLY_IMPLEMENTED_ACTIVE",
        "unexpected project state",
    )
    require("MODULE_A_COMPLETE_AND_FROZEN" in state["completed"], "Module A completion missing")
    require("MODULE_B_COMPLETE_AND_FROZEN" in state["completed"], "Module B completion missing")
    require(
        "MODULE_C_CONSTITUTIVE_UNDERDETERMINATION_THEOREM" in state["completed"],
        "Module C underdetermination theorem missing",
    )
    require(state["score_rule"]["aggregation_can_override_failure"] is False, "failure rule drifted")

    microscopic = (ROOT / "science/MICROSCOPIC_PHYSICS.md").read_text(encoding="utf-8")
    microproof = (ROOT / "proofs/MICROSCOPIC_CONSTITUTION.md").read_text(encoding="utf-8")
    claims = (ROOT / "science/CLAIMS.md").read_text(encoding="utf-8")
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")

    for phrase in [
        "Basis-independent candidate-capacity space",
        "Kinematic automorphisms are not physical gauge symmetry",
        "Exact constitutive underdetermination",
        "Admission witness for the physical microscopic law",
        "Module C is **partially implemented and active**",
    ]:
        require(phrase in microscopic, f"microscopic constitution missing: {phrase}")

    for phrase in [
        "Symmetry nonselection theorem",
        "Mass nonselection theorem",
        "Probability nonselection theorem",
        "Interaction nonselection theorem",
        "ACTIVE_FRONTIER",
    ]:
        require(phrase in microproof, f"microscopic proof missing: {phrase}")

    require("Candidate-capacity coordinates are already physical particles" in claims, "claim boundary missing")
    require("Module C: PARTIALLY_IMPLEMENTED_ACTIVE" in handoff, "handoff state drifted")

    # Representative Module B directed branch remains valid.
    w = [[0.0, 2.0, 0.0], [1.0, 0.0, 3.0], [0.0, 1.0, 0.0]]
    c = [[w[i][j] + w[j][i] for j in range(3)] for i in range(3)]
    degrees = [sum(row) for row in c]
    lap = [[(degrees[i] if i == j else 0.0) - c[i][j] for j in range(3)] for i in range(3)]
    delta = 2.5
    ell = 1.0 / (delta - 1.0)
    system = [[(1.0 if i == j else 0.0) + ell * lap[i][j] for j in range(3)] for i in range(3)]
    x_minus = [3.0, -1.0, 2.0]
    x_plus = solve_linear(system, x_minus)
    reopened = matvec(system, x_plus)
    require(all(close(a, b) for a, b in zip(reopened, x_minus)), "Big-Implosion reopening failed")
    require(close(sum(x_plus), sum(x_minus)), "global carrier conservation failed")

    current = [[ell * w[i][k] * (x_plus[i] - x_plus[k]) for k in range(3)] for i in range(3)]
    flux = [[current[i][k] - current[k][i] for k in range(3)] for i in range(3)]
    for i in range(3):
        require(close(x_plus[i] - x_minus[i] + sum(flux[i]), 0.0), "local continuity failed")

    # Exact Module C capacity and underdetermination counts for the historical 6+2 test case.
    ordinary_dimension = 6
    radiative_dimension = 2
    candidate_dimension = ordinary_dimension + radiative_dimension
    full_orthogonal_dimension = candidate_dimension * (candidate_dimension - 1) // 2
    sector_orthogonal_dimension = (
        ordinary_dimension * (ordinary_dimension - 1) // 2
        + radiative_dimension * (radiative_dimension - 1) // 2
    )
    sector_symmetric_parameters = (
        ordinary_dimension * (ordinary_dimension + 1) // 2
        + radiative_dimension * (radiative_dimension + 1) // 2
    )
    require(candidate_dimension == 8, "historical candidate capacity changed")
    require(full_orthogonal_dimension == 28, "so(8) dimension failed")
    require(sector_orthogonal_dimension == 16, "sector automorphism dimension failed")
    require(sector_symmetric_parameters == 24, "mass-family parameter count failed")

    # Distinct protected signatures admit only the identity permutation.
    signatures = tuple(f"sig-{index}" for index in range(candidate_dimension))
    identity_permutation = tuple(range(candidate_dimension))
    require(
        all(signatures[index] == signatures[target] for index, target in enumerate(identity_permutation)),
        "identity permutation failed",
    )
    swap_permutation = (1, 0, 2, 3, 4, 5, 6, 7)
    require(
        not all(signatures[index] == signatures[target] for index, target in enumerate(swap_permutation)),
        "distinct signatures failed to block nontrivial permutation",
    )

    # Two different nonnegative diagonal spectra preserve the same sectors and signatures.
    spectrum_a = [0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 0.0, 1.0]
    spectrum_b = [1.0, 1.0, 4.0, 9.0, 16.0, 25.0, 0.0, 4.0]
    require(all(value >= 0.0 for value in spectrum_a + spectrum_b), "negative mass-squared test value")
    require(spectrum_a != spectrum_b, "mass nonuniqueness example collapsed")
    require(len(spectrum_a) == candidate_dimension == len(spectrum_b), "spectrum dimension mismatch")

    # A real normalized vector does not select a unique complex phase assignment.
    real_state = [1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)]
    complex_phase_state = [complex(real_state[0], 0.0), complex(0.0, real_state[1])]
    norm_real = sum(value * value for value in real_state)
    norm_complex = sum(abs(value) ** 2 for value in complex_phase_state)
    require(close(norm_real, 1.0) and close(norm_complex, 1.0), "norm example failed")
    require(complex_phase_state != [complex(value, 0.0) for value in real_state], "phase nonuniqueness failed")

    print("2-RFC validation: PASS")
    print("Modules A and B are frozen; Module C is partially implemented and active.")
    print("Checked Module B reopening/conservation and Module C capacity, symmetry, mass, and probability underdetermination.")
    print("This script does not derive the missing microscopic constitutive law or establish empirical truth.")


if __name__ == "__main__":
    main()
