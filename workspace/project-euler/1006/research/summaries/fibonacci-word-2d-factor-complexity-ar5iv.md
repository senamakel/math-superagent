# Sivasankar & Rama — *Two-dimensional Fibonacci Words: Tandem Repeats and Factor Complexity* (arXiv:2204.13977)

Source: https://ar5iv.labs.arxiv.org/html/2204.13977 (full text: [[fibonacci-word-2d-factor-complexity-ar5iv.full]])
PDF version: https://arxiv.org/pdf/2204.13977 ([[fibonacci-word-2d-factor-complexity-sivasankar-rama.full]])

## What this source establishes

A paper about tandems in 2D Fibonacci arrays; for this run only §5 is relevant.

**Convention.** The paper's infinite Fibonacci word f_∞ is the fixed point of
h(a)=b, h(b)=ba, i.e. f_∞ = babbabab… = **the rabbit sequence** (1 0 1 1 0 1 0
1 1 …), which is the 1↔0-complement of the problem's word S = 010010100…
(also shifted). Factor sets are NOT invariant under digit swap + the whole paper
talks about the *complement* convention — the problem's word is the other one.
So the paper's *position theorem* transfers only after complementing digits:
its z_j are factors of the rabbit word; the problem's factors are the digit-wise
complements of those; the *count* theorem transfers unchanged.

**Proposition 4 (factor complexity of the infinite Fibonacci word).**
p_{f_∞}(n) = n+1 for the rabbit-word convention. Since complexity is
preserved by the 0↔1 swap, this confirms the k+1 count for the problem's word
too (matching the problem statement, the brute oracle, and Perrin–Restivo).

**Theorem 7 (position theorem).** For F(n) ≤ k < F(n+1), the k+1 distinct
length-k factors of f_∞, in order of first occurrence, are
  z_j^(k) = f[j+1 … j+k] for 0 ≤ j ≤ F(n)−1,
  z_j^(k) = f[j+F(n+1)−k … j+F(n+1)−k+k] for F(n) ≤ j ≤ k
(with f[i … i+k] the length-k substring starting at i). I.e. the first F(n)
factors are the prefixes at positions 1..F(n), then the remaining k+1−F(n)
factors have shifted starts — a precise, enumerable description of the factor
set of the rabbit word. For the problem's word, complement the digits.

**Theorem 8 (finite-word factor complexity).** For the finite Fibonacci word
f_n (|f_n| = F(n)), the number of distinct length-k factors is
  p_k(f_n) = k+1 for 1 ≤ k ≤ F(n−2);
  F(n−2)+2 for F(n−2)+1 ≤ k ≤ F(n−1)−1;
  F(n)+1−k for F(n−1) ≤ k ≤ F(n).
Table 1 gives n=2..6. This gives the exact minimal word length needed for the
brute oracle: to see all k+1 factors of the infinite word inside the finite
f_n, Theorem 8 says you need F(n) ≥ 2k+… — matching the run's empirical finding
that len ≥ 3k is always safe and 2k is not always sufficient (k=15 needs 35).

**Corollary 1.** p(f_n) = Σ_{k=1}^{F(n)} p_k(f_n).

## What it implies for PE1006

1. The k+1 factor count (problem statement, brute oracle) is a theorem in the
   literature (Prop 4), valid for both digit conventions.
2. Theorem 7's explicit first-occurrence list is a *second independent route*
   to the factor set (complemented): it could generate the k+1 factors of S
   directly by position without any mechanical-word modelling, for small k a
   cross-check of the mechanical-word construction; for large k it is
   enumeration, so the floor-sum route remains primary.
3. Theorem 8 explains the oracle's word-length bound: the minimal safe S_n
   length is the smallest F(n) with F(n) ≥ 2k + (≤2); hence the "3k rule" is
   comfortably safe for all k and reveals why 2k occasionally fails.

## Claims anchored here

`governing-factor-complexity` (Prop 4), and the position theorem is the source
anchor listed for `mechanical-word-digit-rule`'s "equivalently … first-occurrence
positions" parenthetical.

## What it does NOT establish

- Nothing about reading factors as decimals or summing squares.
- Nothing about the mechanical-word / floor-sum primitive.
- The rabbit-sequence (complement) convention is a source of confusion — flag
  any cross-check that compares its factor strings directly to the problem's
  without complementing.