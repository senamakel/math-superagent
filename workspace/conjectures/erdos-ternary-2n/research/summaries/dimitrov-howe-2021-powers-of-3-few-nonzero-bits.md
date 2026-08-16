# Dimitrov & Howe, "Powers of 3 with few nonzero bits and a conjecture of Erdős"

Source: arXiv:2105.06440v4 (math.NT), 2023. Full text: `research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md`. Published: Rocky Mountain Journal of Mathematics.

## What it establishes

**Theorem 1.1.** The only powers of 3 writable as the sum of ≤ 22 distinct powers of 2 are `3^x` with `0 ≤ x ≤ 25`. I.e. the binary representation of `3^x` has > 22 ones exactly when `x > 25`.

**Theorem 1.2 (directly on Erdős).** The only powers of 2 writable as the sum of ≤ 25 distinct powers of 3 are
```
2^0 = 1 = 3^0
2^2 = 4 = 3^0 + 3^1
2^8 = 256 = 3^0 + 3^1 + 3^2 + 3^5
```
Equivalently: if `x ∉ {0, 2, 8}` then the base-3 expansion of `2^x` contains either at least one digit `2`, **or at least twenty-six 1s**.

This is the strongest structural bound on the conjecture: any counterexample to Erdős (a `2^x` with no digit 2, `x > 8`) must have **≥ 26 ones** in its ternary expansion.

## Method (important for the sieve route)

Fully elementary. Solve the exponential Diophantine equation `2^x = 3^a1 + ... + 3^an` (n ≤ 25) by working modulo a carefully chosen chain of moduli `M1 | M2 | ...`. At each modulus they enumerate which combinations of distinct powers of 3 equal a power of 2 mod `M`, and the chain refines the integer solution space to a single lift. Example used in detail: `n=3` with `M1 = 5440 = 2^6·5·17`, `M2 = 2^7·5·17·257`.

They note (footnote 1) Stewart's effective bound is astronomically larger here: the largest `x` with `3^x` having ≤ 22 ones satisfies a growth condition giving `B(22) > 4.9×10^46` — so the elementary congruence method beats linear-forms-in-logarithms by many orders of magnitude for these small counts.

They also prove (Section 3) a necessary condition on any modulus `M` that resolves equations (1)/(2): a modulus providing all solutions must satisfy an unexpected (Wieferich-like) valuation condition. This is directly relevant to whether the modular sieve on `2^n mod 3^k` can close.

## Relevance

- Confirms the witnesses `{0, 2, 8}` survive under the sparse-ones restriction.
- Gives the constant: "at most 25 ones" is the boundary.
- The nested-modulus method is exactly the shape of the run's sieve instrument, and their Wieferich-condition section is a specific obstruction to sieving — worth reading in full.

## Claims

```claim
id: DIMITROV-HOWE-26-ONES
statement: The only powers of 2 writable as a sum of <= 25 distinct powers of 3
  are 2^0, 2^2, 2^8. Equivalently: if x ∉ {0,2,8} then (2^x)_3 contains either
  at least one digit 2, or at least twenty-six 1s.
hypotheses: x a nonnegative integer.
holds-here: yes — any counterexample to Erdős (digit-2-free, x > 8) must have
  >= 26 ones in ternary.
status: asserted-by-source (proved in the peer-reviewed paper; statement verified
  here against the full text, proof not re-derived here)
bearing: the strongest structural restriction on the conjecture. The residual
  open case is exactly ">= 26 ones and no 2s". Improving the 26, or proving
  something about the 26-one residual, is this run's most concrete lever.
anchor: research/sources/dimitrov-howe-2021-powers-of-3-few-nonzero-bits.pdf.full.md
```

## Status

Sourced, peer-reviewed (Rocky Mountain J. Math).
