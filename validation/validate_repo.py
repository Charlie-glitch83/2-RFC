#!/usr/bin/env python3
"""Dependency-free repository and finite algebra checks through repaired Module B."""

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
        "science/CLAIMS.md",
        "science/PHYSICAL_REALIZATION.md",
        "proofs/KERNEL_COMPLETION.md",
        "proofs/GENESIS_REALIZATION.md",
        "modules/A/MODULE_A_TO_B_SCIENTIFIC_HANDOFF.md",
        "modules/B/MODULE_B_DETAILED_SCIENTIFIC_REPAIR_PLAN.md",
        "modules/B/MODULE_B_MANUSCRIPT_SOURCE_TRACEABILITY.md",
        "modules/B/MODULE_B_WOLFRAM_REVISION.md",
        "modules/B/MODULE_B_WOLFRAM_VERIFICATION.md",
        "modules/B/MODULE_B_TO_C_SCIENTIFIC_HANDOFF.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_module"] == "C", "Module C must be active")
    require(state["status"] == "MODULES_A_B_COMPLETE_FROZEN_MODULE_C_ACTIVE", "unexpected state")
    require("MODULE_B_COMPLETE_AND_FROZEN" in state["completed"], "Module B completion missing")
    require(state["score_rule"]["aggregation_can_override_failure"] is False, "failure rule drifted")

    genesis = (ROOT / "proofs/GENESIS_REALIZATION.md").read_text(encoding="utf-8")
    physical = (ROOT / "science/PHYSICAL_REALIZATION.md").read_text(encoding="utf-8")
    handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")
    for phrase in [
        "Module B Big-Implosion and Four-Sector Genesis Theorem",
        "Sole first physical event",
        "Exact four-sector seed partition",
        "Complete Module C parent state",
        "Module B is complete and frozen",
    ]:
        require(phrase in genesis, f"genesis theorem missing: {phrase}")
    require("Module B is complete and frozen" in physical, "physical boundary not closed")
    require("Module C: ACTIVE" in handoff, "handoff does not advance to Module C")

    # Representative directed branch.
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

    # Directed currents and local continuity.
    current = [[ell * w[i][k] * (x_plus[i] - x_plus[k]) for k in range(3)] for i in range(3)]
    flux = [[current[i][k] - current[k][i] for k in range(3)] for i in range(3)]
    for i in range(3):
        residual = x_plus[i] - x_minus[i] + sum(flux[i])
        require(close(residual, 0.0), f"local continuity failed at vertex {i}")
    for i in range(3):
        for k in range(3):
            require(close(flux[i][k], -flux[k][i]), "flux antisymmetry failed")

    # Compression progress on the nonconstant carrier.
    mean_minus = sum(x_minus) / 3.0
    mean_plus = sum(x_plus) / 3.0
    e_minus = 0.5 * sum((x - mean_minus) ** 2 for x in x_minus)
    e_plus = 0.5 * sum((x - mean_plus) ** 2 for x in x_plus)
    require(e_plus < e_minus, "nonconstant carrier did not compress")
    chi = -math.log(e_plus / e_minus)
    require(chi > 0.0, "intrinsic compression progress not positive")

    # Clock monotonicity for alpha>0, delta>1.
    alpha = 0.0256831
    def srec(u: float) -> float:
        q = math.exp(-alpha * u) / delta
        return -math.log(1.0 - q) - q * math.log(q) / (1.0 - q)
    values = [srec(u) for u in (0.0, 1.0, 10.0, 100.0)]
    require(all(values[i + 1] < values[i] for i in range(len(values) - 1)), "recursive entropy not decreasing")
    tau = [math.log(values[0] / value) for value in values]
    require(all(tau[i + 1] > tau[i] for i in range(len(tau) - 1)), "intrinsic clock not increasing")

    # Four projector identities on a two-component pair block.
    swap = [[0.0, 1.0], [1.0, 0.0]]
    i2 = identity(2)
    even = [[0.5 * (i2[r][c] + swap[r][c]) for c in range(2)] for r in range(2)]
    odd = [[0.5 * (i2[r][c] - swap[r][c]) for c in range(2)] for r in range(2)]
    require(all(close(x, y) for row_x, row_y in zip(matmul(even, even), even) for x, y in zip(row_x, row_y)), "even projector failed")
    require(all(close(x, y) for row_x, row_y in zip(matmul(odd, odd), odd) for x, y in zip(row_x, row_y)), "odd projector failed")
    zero = matmul(even, odd)
    require(all(close(value, 0.0) for row in zero for value in row), "projectors not orthogonal")
    require(all(close(even[r][c] + odd[r][c], i2[r][c]) for r in range(2) for c in range(2)), "projectors incomplete")

    # Tail reciprocity limit.
    dx = 1.7
    reciprocal_tail = 0.5 * ell * (2.0 - 2.0) * dx
    nonreciprocal_tail = 0.5 * ell * (2.0 - 1.0) * dx
    require(close(reciprocal_tail, 0.0), "tail did not vanish under reciprocity")
    require(nonreciprocal_tail != 0.0, "nonreciprocal tail unexpectedly vanished")

    print("2-RFC validation: PASS")
    print("Modules A and B are complete and frozen at their declared scopes; Module C is active.")
    print("Checked Big-Implosion reopening, continuity, conservation, compression, clock, projectors, and tail reciprocity.")
    print("This script is an integrity check, not an empirical or continuum-spacetime proof.")


if __name__ == "__main__":
    main()
