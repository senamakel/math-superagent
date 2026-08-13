# Sutherland 2004 — Counting points on superelliptic curves (method source)

Source: A.V. Sutherland, "Counting points on superelliptic curves in average
polynomial time", arXiv:2004.10189v5 (2004/2020). Full text:
`research/sources/sutherland-counting-superelliptic-2004.full.md`.
URL: https://arxiv.org/html/2004.10189v5

## What the paper establishes

An average-polynomial-time algorithm to count points on superelliptic curves
`X: y^m = f(x)` over Q (m ≥ 2, f ∈ Z[x] squarefree of degree d ≥ 3): given N, it
computes `#X(F_p)` for **all primes p ≤ N** not dividing `m·lc(f)·disc(f)` in
time `O(m d³ N log³ N log log N)`, via the trace of the Cartier–Manin matrix of
the reductions of X (and the p-rank/zeta-numerator as byproducts).

## Bearing for this run — method background, not a claim source

- This is the **counting-points engine behind the effective Diophantine
  pipeline**: the same Cartier/ℓ-adic machinery that computes zeta functions and
  p-ranks feeds the Chabauty–Coleman-style determination of rational points on
  the hyperelliptic/superelliptic curves `C(x,k1)=C(y,k2)` (the run's k2=2/3/4/5
  small-column families are hyper/superelliptic: `Y² = poly`, `Y³−Y =
  6C(x,k1)`, etc.).
- It does **not** establish any theorem about Singmaster, does not bound N(a),
  and is not a route to uniformity: the algorithm's complexity grows with the
  specific curve's degree and discriminant, i.e. with (k1,k2) per pair. It is
  filed for breadth — the practitioner's reference for "how the effective small-p
  verification bounds (BBW 10^6/10^60, Singmaster 2^48) and the BMSST-type
  integral-point computations are actually done".
- No claim block is warranted: nothing the run relies on is sourced from this
  paper, and no ledger fact depends on it.

```claim
id: sutherland-superelliptic-counting-method
statement: Sutherland (arXiv:2004.10189): #X(F_p) for all p <= N on a
  superelliptic curve y^m = f(x) (f squarefree degree d, good primes) in
  O(m d^3 N log^3 N log log N) via the Cartier-Manin matrix trace; computes
  p-rank and zeta-numerator modulo p as byproducts.
hypotheses: m >= 2, d >= 3, f squarefree, p good primes only.
holds-here: N/A — method background for the effective integral-point pipeline on
  the run's hyper/superelliptic binomial curves; no Singmaster claim rests on it.
status: asserted-by-source (abstract + algorithm description; not re-derived)
bearing: identifies the practical engine behind effective small-(k1,k2)
  verification; per-curve cost, no uniformity content.
anchor: research/sources/sutherland-counting-superelliptic-2004.full.md
```