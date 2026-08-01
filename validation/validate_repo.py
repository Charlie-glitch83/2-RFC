#!/usr/bin/env python3
"""Minimal, dependency-free integrity and algebra checks for 2-RFC."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def solve_linear(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Solve a small dense system by Gauss-Jordan elimination."""
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


def quadratic(vector: list[float], matrix: list[list[float]]) -> float:
    return sum(a * b for a, b in zip(vector, matvec(matrix, vector)))


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
        "proofs/GENESIS_REALIZATION.md",
        "science/FOUNDATION.md",
        "science/PHYSICAL_REALIZATION.md",
    ]
    for relative in required:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    manifest = json.loads((ROOT / "sources/SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
    require(manifest["repository"] == "Charlie-glitch83/1RFC", "source repository drifted")
    require(manifest["ref"] == "main", "source ref drifted")
    require(len(manifest["sources"]) == 5, "source manifest must contain exactly five sources")
    require(len({source["id"] for source in manifest["sources"]}) == 5, "duplicate source ID")
    for source in manifest["sources"]:
        digest = source["sha256"]
        require(len(digest) == 64 and all(char in "0123456789abcdef" for char in digest), f"invalid hash for {source['id']}")
        require(source["url"].startswith("https://github.com/Charlie-glitch83/1RFC/blob/main/"), f"invalid source URL for {source['id']}")

    state = json.loads((ROOT / "STATE.json").read_text(encoding="utf-8"))
    require(state["active_milestone"] == "M3_PHYSICAL_REALIZATION", "unexpected milestone")
    require("Causal Enrichment Lemma 2" in state["exact_next_action"], "next action drifted")
    require(state["score_rule"]["aggregation_can_override_failure"] is False, "gate policy drifted")

    machine_states = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path.name.upper() in {"STATE.JSON", "CURRENT_STATE.JSON", "CURRENT_STATE.YAML"}
    )
    require(machine_states == ["STATE.json"], f"duplicate machine state detected: {machine_states}")

    weights = [0.005085, 0.984868, 0.010047]
    require(math.isclose(sum(weights), 1.0, rel_tol=0.0, abs_tol=1e-15), "triad weights do not sum to one")

    for n in range(1, 101):
        lanes_n = n * (n - 1)
        lanes_next = (n + 1) * n
        require(lanes_next - lanes_n == 2 * n, f"lane refinement failed at N={n}")

    delta = 4.6692
    alpha = 0.0256831
    bound = 1.0 / (1.0 - 1.0 / delta)
    for time in (0.0, 0.5, 10.0, 60.0):
        for depth in (0, 1, 18, 40, 500):
            total = sum(delta ** (-j) * math.exp(-alpha * j * time) for j in range(depth + 1))
            require(total <= bound + 1e-14, "kernel bound violated")

    # Three-node path graph: L is positive semidefinite and Q=(I+L)^-1.
    laplacian = [
        [1.0, -1.0, 0.0],
        [-1.0, 2.0, -1.0],
        [0.0, -1.0, 1.0],
    ]
    system = [[(1.0 if i == j else 0.0) + laplacian[i][j] for j in range(3)] for i in range(3)]
    before = [2.0, -1.0, 4.0]
    after = solve_linear(system, before)
    require(math.isclose(sum(after), sum(before), abs_tol=1e-12), "constant/total mode not preserved")
    require(quadratic(after, laplacian) <= quadratic(before, laplacian) + 1e-12, "Dirichlet energy increased")

    # Positive added mass generally adds nonzero acceleration; exact trajectory inclusion is prohibited.
    gravitational_constant = 1.0
    added_mass = 0.1
    separation = 2.0
    added_acceleration = gravitational_constant * added_mass / separation**2
    require(added_acceleration > 0.0, "positive-mass perturbation unexpectedly vanished")

    # Append-only ancestry ranks give a strict order; they are not physical durations.
    ranks = {"root": (0, 0), "branch_a": (0, 1), "rip": (0, 2), "next_cycle": (1, 0)}
    ancestry = {
        "root": {"branch_a"},
        "branch_a": {"rip"},
        "rip": {"next_cycle"},
        "next_cycle": set(),
    }
    for parent, children in ancestry.items():
        for child in children:
            require(ranks[parent] < ranks[child], "ancestry edge does not increase lexicographic rank")
    require(all(not reachable(ancestry, event, event) for event in ranks), "ancestry cycle detected")

    print("2-RFC validation: PASS")
    print("Checked source manifest, repository state, kernel bounds, lane growth, graph smoothing, and add-body correction.")
    print("Physical-realization obligations R1-R9 remain theorem work, not script-certified facts.")


if __name__ == "__main__":
    main()
