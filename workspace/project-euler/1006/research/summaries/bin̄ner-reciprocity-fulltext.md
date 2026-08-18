# Binner — Reciprocity Relations for Summations of Squares of Floor Functions (arXiv:2107.08308)

<!-- source: https://arxiv.org/html/2107.08308v1 | full text read 2026-08-19 -->

Full text: `research/sources/bin̄ner-reciprocity-fulltext.full.md` (also the short landing page
`research/sources/binner-reciprocity-floor-square-functions.full.md`).

## What it establishes

Damanvir Singh Binner (Simon Fraser) gives reciprocity relations that evaluate the following sums
for positive coprime a,b and natural h **in O(log t) steps**, t = max(a,b):

- T₁(a,b;h) = Σ_{i=1}^{h} {ib/a}²   (squares of fractional parts)
- T₂(a,b;h) = Σ_{i=1}^{h} i·⌊ib/a⌋   (first moment with index weight)
- T₃(a,b;h) = Σ_{i=1}^{h} ⌊ib/a⌋²   (squares of floors)

with T₃ obtained from T₁, T₂ and the division algorithm. The key machinery: a 2020 reciprocity
relation of the author (Theorem 3), Σ_{i=1}^{d}⌊ib/a⌋ + Σ_{i=1}^{K}⌊ia/b⌋ = dK with K = ⌊bd/a⌋ —
the same Euclidean reciprocity the AtCoder/universal-Euclidean floor_sum recursion rests on — and
a partial-fraction/generating-function coefficient count (Lemmas 4–5) using Sylvester's theorem
(number of nonrepresentable integers = (a−1)(b−1)/2) and Brown–Shiue's sum formula.

Verified worked example (2732, 8411, 1221): Σr_i² = 28850219593, Σi·q_i = 196956430, Σq_i² = 63853169.

## Why it matters here

- This is the **academic, journal-grade anchor** for the floor-second-moment primitive the run's
  universal-Euclidean monoid implements (`universal-euclidean-geometric-floor-sum`,
  `governing-universal-euclidean`): it proves the O(log) reciprocity for exactly the
  Σ⌊ib/a⌋²-type sums (with index weight) that Ψ(k)'s telescoped second moment reduces to.
- It answers part of the request for a *citable non-competitive-programming treatment* of the
  floor-moment recursion (the competitive-programming sources fhq/OI-wiki/LOJ138 are the algorithm
  templates; Binner is the peer-reviewed statement of the reciprocal-step mathematics).
- Boundary: Binner treats the plain floor sums Σ⌊ib/a⌋ᵏ with polynomial-in-i weights; the run's
  Ψ also needs the geometric weight 10^j in front of the floor terms. The reciprocity itself
  (Theorem 3) is the shared Euclidean step, so the geometric-weight extension is exactly what the
  fhq/OI-wiki monoid provides; Binner does not state the geometric-weight form.

## Claims anchored here

Corroborates `governing-universal-euclidean` / `universal-euclidean-geometric-floor-sum` and the
request `citable-name-treatment-0c91` (adds a journal-grade anchor alongside the existing notes).
No new claim block needed.
