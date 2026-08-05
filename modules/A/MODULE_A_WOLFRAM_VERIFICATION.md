# Module A — Wolfram Verification Record

## Scope

This file records exact symbolic checks performed during the Module A repair. It is governed by `architecture/2RFC_WOLFRAM_INTEGRATION_RULES.md`.

Wolfram is used here as an independent algebraic verifier. It is not an RFC source and supplies no physical law, fitted constant, public target, or branch choice.

## Assumptions

```text
delta > 1
alpha >= 0
t >= 0
m is a nonnegative integer
n is a positive integer
q = exp(-alpha t)/delta, so 0 < q < 1
```

## Exact checks

### 1. Infinite geometric kernel majorant

Input form:

```wolfram
Sum[delta^(-j) Exp[-alpha j t], {j, 0, Infinity}]
```

Exact result:

```text
1 + 1/(-1 + delta Exp[alpha t])
= 1/(1 - Exp[-alpha t]/delta)
= 1/(1-q)
```

This verifies the scalar geometric majorant used in the kernel norm proof.

### 2. Truncation tail

Input form:

```wolfram
Sum[delta^(-j) Exp[-alpha j t], {j, m + 1, Infinity}]
```

Exact result:

```text
1/(delta^m Exp[alpha m t] (-1 + delta Exp[alpha t]))
= q^(m+1)/(1-q)
```

This verifies the exact tail underlying the certified truncation bound.

### 3. Derivative-depth majorant

Input form:

```wolfram
Sum[j delta^(-j) Exp[-alpha j t], {j, 0, Infinity}]
```

Exact result:

```text
delta Exp[alpha t]/(-1 + delta Exp[alpha t])^2
= q/(1-q)^2
```

This verifies the depth factor in the conditional derivative estimate.

### 4. Add-one directed-lane growth

Input form:

```wolfram
FullSimplify[(n + 1)n - n(n - 1),
 Assumptions -> n >= 1 && Element[n, Integers]]
```

Exact result:

```text
2 n
```

This independently verifies the structural capacity identity.

### 5. Promotion/reopening left inverse

A finite symbolic matrix example was evaluated with a promotion matrix `P` and reopening matrix `R` satisfying `R.P`.

Exact result:

```text
IdentityMatrix[2]
```

This verifies the algebraic meaning of a split monomorphism in an explicit finite example. It does not prove that any particular downstream physical coarse graining is valid.

### 6. Recursive-depth entropy

For

```text
p_j=(1-q)q^j
```

Wolfram returned an expression algebraically equivalent to

```text
-log(1-q) - q log(q)/(1-q)
```

under `0<q<1`.

This checks the closed form of the recursive-depth dispersion functional. The result is not thermodynamic entropy.

## Independent checks

The repository validation script independently checks finite numerical instances of:

- triad-weight normalization;
- lane growth through `N=1000`;
- geometric sums and tails over multiple depths and internal arguments;
- recursive-depth normalization and entropy;
- four event-output classes;
- protected memory and promotion reopening on a finite example;
- dormant zero output and zero backreaction;
- positive-influence perturbation and the zero-backreaction boundary;
- append-only ancestry acyclicity.

The script is an integrity and finite-instance check. It is not a substitute for the analytic proof or a physical validation.

## Limitations

These Wolfram checks do not prove:

- universal all-time N-body regularity;
- a physically infinite-N state;
- a valid physical specialization for every later module;
- physical time, spacetime, matter, or cosmology;
- indefinite memory capacity;
- empirical truth.

Within those limits, the exact symbolic results agree with the repaired Module A kernel, lane-growth, reopening, and recursive-depth formulas.