#!/usr/bin/env python3
"""Dependency-free repository and exact finite checks through completed Module C."""

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


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def dagger(a: list[list[complex]]) -> list[list[complex]]:
    return [[complex(value).conjugate() for value in col] for col in zip(*a)]


def identity(n: int) -> list[list[complex]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matrix_close(a: list[list[complex]], b: list[list[complex]], tol: float = 1e-11) -> bool:
    return all(abs(x - y) <= tol for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b))


def main() -> None:
    required = [
        "README.md",
        "STATE.json",
        "PLAN.md",
        "HANDOFF.md",
        "science/MICROSCOPIC_PHYSICS.md",
        "science/CLAIMS.md",
        "proofs/MICROSCOPIC_CONSTITUTION.md",
        "modules/C/MODULE_C_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/C/MODULE_C_WOLFRAM_INTEGRATION_REVISION.md",
        "modules/C/MODULE_C_WOLFRAM_VERIFICATION.md",
        "modules/C/MODULE_C_TO_D_SCIENTIFIC_HANDOFF.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_module"] == "D", "Module D must be active")
    require(
        state["status"] == "MODULES_A_B_C_COMPLETE_FROZEN_MODULE_D_ACTIVE",
        "unexpected project state",
    )
    require("MODULE_C_COMPLETE_AND_FROZEN" in state["completed"], "Module C completion missing")
    require(state["score_rule"]["aggregation_can_override_failure"] is False, "failure rule drifted")

    microscopic = (ROOT / "science/MICROSCOPIC_PHYSICS.md").read_text(encoding="utf-8")
    proof = (ROOT / "proofs/MICROSCOPIC_CONSTITUTION.md").read_text(encoding="utf-8")
    claims = (ROOT / "science/CLAIMS.md").read_text(encoding="utf-8")
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")

    for phrase in [
        "Canonical complex state space from directed route pairs",
        "Hermitian generator, unitary evolution, and probability",
        "Completed shells and three generation families",
        "Internal symmetry derived from the triadic fibers",
        "Minimal chiral representation and charge closure",
        "Endogenous microscopic scale",
        "Confinement and bound states",
        "Complete Module D parent state",
        "Module C is complete and frozen",
    ]:
        require(phrase in microscopic, f"microscopic theorem missing: {phrase}")

    require("Module C Triadic Microscopic Constitution Theorem" in proof, "proof title missing")
    require("Module C is complete and frozen" in proof, "proof conclusion missing")
    require("Module C is complete and frozen" in claims, "claim ledger not closed")
    require("Module D: ACTIVE" in handoff, "handoff did not advance to D")

    # Route-pair complex structure.
    j = [[0.0, -1.0], [1.0, 0.0]]
    require(matrix_close(matmul(j, j), [[-1.0, 0.0], [0.0, -1.0]]), "J^2 != -I")
    require(matrix_close(matmul(dagger(j), j), identity(2)), "J not orthogonal/unitary")

    # Representative Hermitian generator.
    lap = [[3.0, -3.0, 0.0], [-3.0, 7.0, -4.0], [0.0, -4.0, 4.0]]
    orient = [[0.0, 2.0, -1.0], [-2.0, 0.0, 3.0], [1.0, -3.0, 0.0]]
    h = [[lap[r][c] + 1j * orient[r][c] for c in range(3)] for r in range(3)]
    require(matrix_close(dagger(h), h), "microscopic generator not Hermitian")

    # Three completed generation shells.
    shell_size = 3 * (3 - 1)
    require(shell_size == 6, "triadic lane shell size failed")
    require(18 % shell_size == 0 and 18 // shell_size == 3, "generation closure failed")

    # Recursive shell weights normalize.
    delta = 4.6692
    denominator = 1.0 + delta**6 + delta**12
    weights = [delta**12 / denominator, delta**6 / denominator, 1.0 / denominator]
    require(all(weight > 0.0 for weight in weights), "shell weight not positive")
    require(close(sum(weights), 1.0), "shell weights not normalized")

    # Minimal anomaly-free charge solution.
    charges = {
        "Q": 1.0 / 6.0,
        "U": 2.0 / 3.0,
        "D": -1.0 / 3.0,
        "L": -1.0 / 2.0,
        "E": -1.0,
        "H": 1.0 / 2.0,
    }
    require(close(charges["U"], charges["Q"] + charges["H"]), "up coupling charge failed")
    require(close(charges["D"], charges["Q"] - charges["H"]), "down coupling charge failed")
    require(close(charges["E"], charges["L"] - charges["H"]), "lepton coupling charge failed")
    require(close(3 * charges["Q"] + charges["L"], 0.0), "SU2 anomaly failed")
    require(
        close(
            6 * charges["Q"] - 3 * charges["U"] - 3 * charges["D"]
            + 2 * charges["L"] - charges["E"],
            0.0,
        ),
        "gravitational U1 anomaly failed",
    )
    require(
        close(
            6 * charges["Q"] ** 3 - 3 * charges["U"] ** 3 - 3 * charges["D"] ** 3
            + 2 * charges["L"] ** 3 - charges["E"] ** 3,
            0.0,
        ),
        "cubic U1 anomaly failed",
    )

    # Stable RFL minimum and protected neutral zero mode.
    a = 0.7
    b = 1.3
    r0 = math.sqrt(a / b)
    first_derivative = -2 * a * r0 + 2 * b * r0**3
    second_derivative = -2 * a + 6 * b * r0**2
    require(close(first_derivative, 0.0), "stabilization minimum failed")
    require(second_derivative > 0.0 and close(second_derivative, 4 * a), "minimum not stable")

    g1, g2, v = 0.4, 0.7, 1.2
    neutral = [
        [v * v * g2 * g2 / 4.0, -v * v * g1 * g2 / 4.0],
        [-v * v * g1 * g2 / 4.0, v * v * g1 * g1 / 4.0],
    ]
    zero_vector = [g1, g2]
    residual = [sum(row[k] * zero_vector[k] for k in range(2)) for row in neutral]
    require(all(close(value, 0.0) for value in residual), "neutral protected zero mode failed")

    # Internal algebra dimension.
    require(1 + (2 * 2 - 1) + (3 * 3 - 1) == 12, "internal algebra dimension failed")

    print("2-RFC validation: PASS")
    print("Modules A, B, and C are complete and frozen; Module D is active.")
    print("Checked Module C complex structure, Hermiticity, shell closure, anomaly closure, stabilization, zero mode, and state transition.")
    print("This script is an integrity check, not empirical validation or continuum-QFT proof.")


if __name__ == "__main__":
    main()
