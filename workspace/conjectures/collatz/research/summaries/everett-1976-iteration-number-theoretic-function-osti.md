# Everett 1976 — Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2

<!-- source: https://www.osti.gov/servlets/purl/7357908 (LA-6449-MS, Los Alamos Scientific Laboratory, July 1976; published as Advances in Math. 25 (1977) 42-45, DOI 10.1016/0001-8708(77)90087-1). Full text held: the OSTI technical-report PDF, OCR with some noise but the mathematics is readable. -->

**C. J. Everett, 1976. Primary text held.**

## What it establishes

The map f(2n) = n, f(2n+1) = 3n+2 is *exactly the accelerated Collatz map*
T(x) = x/2 (x even), (3x+1)/2 (x odd) (substitute x = 2n, x = 2n+1). The
paper proves the canonical density-1 finite-descent theorem for it, with the
parity-vector machinery.

- **Theorem 1 (parity-vector correspondence)**: the assignment
  m ↦ (x₀, x₁, …, x_{N−1}) (x_n = parity of f^n(m)) is a one-to-one map of
  the positive integers m < 2^N onto the set of all 2^N dyadic (0/1) vectors.
  Moreover m = a_{N−1} + 2^N Q and m_n = f^n(m) = b_{n−1} + 3^n Q' — the affine
  form of the iterates in terms of the parity vector.
- **Theorem 2 (density-1 descent)**: A(M) = # {m ≤ M : ∃k, f^k(m) < m}
  satisfies A(M)/M → 1 as M → ∞. I.e. **almost every positive integer has a
  finite stopping time** (an iterate strictly below the start).
- Method: for M = 2^N use the parity correspondence; the ratio
  m_{n+1}/m_n = 1/2 if x_n = 0, and < 5/3 if x_n = 1 (m_n > 1). So after N
  steps m_N/m_0 < (5/3)^X (1/2)^{N−X} where X = #ones, which is < 1 iff
  X/N < L = log 2 / log(10/3) ≈ 0.5757. Chebyshev's inequality (Uspensky)
  gives #H_N/2^N ≥ 1 − 1/(4ε²N) for sequences with 1/2 − ε < X/N < 1/2 + ε,
  which forces the density of descent to 1. Interpolation between powers of 2
  (eqns 10–12) completes the limit.

## Why it matters for this run

This is the primary source for the **density-1 finite-stopping-time theorem**
that ROOT previously carried only via secondary accounts (Terras 1976,
Garner 1981, Gluck–Taylor 2001, Hercher 2022). The result is now primary-
backed. It also provides the parity-vector correspondence in a form that
underlies:
- the "prescribed-parity class" restricted-class results in the weakened
  ladder (T^k(n) < n for parity vectors with 3^a < 2^b), and
- the general structure of a cycle/divergence analysis by parity strings.
Historically Terras (Acta Arith. 30, 1976) and Everett (LA-6449-MS, July
1976; Advances 25, 1977) proved this independently at the same time; the
Terras paper itself is still not held (scanned, no text layer) but the
theorem no longer depends on it.

```claim
id: everett-parity-vector-bijection
statement: For the accelerated Collatz map T(x) = x/2 (x even), (3x+1)/2 (x odd), the map m ↦ (x_0, …, x_{N−1}) (x_n = parity of T^n(m)) is a bijection from {1 ≤ m < 2^N} onto {0,1}^N; and T^n(m) = a + 3^n·q for integers a, q depending only on the parity vector, while m = a' + 2^N·q'.
hypotheses: T the accelerated map; N ≥ 1; m positive with m < 2^N.
holds-here: true — the actual map, in accelerated form.
evidence: proved in source (Everett 1976 LA-6449-MS, Theorem 1 + Corollary), read in full text.
status: proved (in source; not yet Lean-formalised here)
falsifies: a parity vector of length N without a unique preimage m < 2^N, or two different m < 2^N with the same first-N parities (small-N oracle check).
```

```claim
id: everett-density-1-finite-stopping-time
statement: Almost every positive integer has a finite stopping time: if A(M) = #{m ≤ M : T^k(m) < m for some k}, then A(M)/M → 1 as M → ∞.
hypotheses: T the accelerated Collatz map; natural density.
holds-here: true.
evidence: proved in source (Everett 1976, Theorem 2 + §III), read in full text. Same theorem as Terras 1976 (Acta Arith. 30, 241-252), whose primary text is not held; this is now the primary-backed route.
status: proved (in source; not yet Lean-formalised here)
falsifies: a positive lower density of m whose first N parities are all "0-1 balanced" with X/N ≥ L = log 2/log(10/3) ≈ 0.5757 (the balance condition that forces descent) — i.e. a violation of the Chebyshev bound (6), checkable in distribution for large N.
```
