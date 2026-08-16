# Iannucci–Foster — Kaprekar Triples

Source: https://cs.uwaterloo.ca/journals/JIS/VOL8/Iannucci/iannucci45.pdf
(`research/sources/iannucci-foster-kaprekar-triples.full.md`).
Journal of Integer Sequences, Vol. 8 (2005), Article 05.4.8.

**Definition (n-Kaprekar triple).** k satisfies k³ = p·10^{2n} + q·10^n + r and
k = p + q + r with 0 ≤ r < 10^n, 0 ≤ q < 10^n, p > 0. Examples: 8³=512 (5+1+2),
45³=91125 (9+11+25), 297³=26198073 (26+198+073). Generalises Kaprekar numbers
(two-block) to three-block splits of the *cube*.

**What it establishes.**
- **Theorem 1:** If N ≢ 1 (mod 4), every k ∈ K(N) is divisible by a unitary
  divisor d of N − 1; writing k = dm, m satisfies a stated divisibility
  condition for a pair d₁,d₂ of unitary divisors of N − 1 with d₁d₂ = (N−1)/d.
- **Theorem 2:** for n ≥ 3, 5·10^{n−1}(10^n ± 1) are 2n-Kaprekar triples.
- **Theorem 3:** every even perfect number is a binary Kaprekar triple.
- **Theorem 4:** for n ≥ 3, 5·10^{3n−1} + 5·10^{n−1} is a 4n-Kaprekar triple.
- Comments: an n-Kaprekar triple may exist only when ω(10^n − 1) is large;
  ω(10^n − 1) = 2 when n = 19, 23, 317; no 317-Kaprekar triples exist; K(N) = ∅
  for N > 8 of the form p^α + 1 (odd prime p, α ≥ 1). So triples do not exist
  for every n.

**Bearing on PE 719.** This is the **three-block-of-the-cube** analogue, not the
2+-block-of-the-square S-number rule. It confirms the general "split powers into
blocks summing to the base" family of which S-numbers are one instance (blocks
of a *square*, arbitrary block count). It gives no enumeration route for
T(10¹²) — the recursion over block cuts of m² is still needed. Supplementary
context establishing the wider family and its generation-from-unitary-divisors
structure (which only works at fixed, small block counts).

**Does not help** give the answer; context for the surrounding theory only.
