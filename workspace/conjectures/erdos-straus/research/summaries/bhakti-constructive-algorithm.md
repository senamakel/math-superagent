# Bhakti (Suzuki), "An Efficient Constructive Algorithm for the Erdős–Straus Conjecture: Solutions for Massive Integers"

Source: https://www.jstage.jst.go.jp/article/iar/3/0/3_28/_pdf
Full text: `research/sources/bhakti-constructive-algorithm.full.md`

## What it establishes (sourced; algorithmic, not a covering identity)

A per-n constructive algorithm, not a family identity. For n prime of the form
`n = 4s + 1`:

- **Known Fact 1**: in a solution with `x ≤ y, x ≤ z`, `s < x` (so
  `x = s + k`, `k ≥ 1`).
- **Known Fact 2**: for prime n, n divides y or z (or both).
- **Theorem (N&S)**: for n = 4s+1 prime, an ESC solution exists iff there are
  natural numbers `k ≥ 1, A ≥ 1` with
  `(4k−1)A − (s+k) | A·n·(s+k)`, in which case
  `x = s+k`, `y = An`, `z = An(s+k)/((4k−1)A − (s+k))` solves ESC
  (or the symmetric case with y,z swapped). This is the Bradford two-variable
  reduction restated with `A = y/n`, `d = ...`; the proof is direct algebra.

This is **not** a polynomial identity covering the class n ≡ 1 (mod 840):
k and A are found per-n by a guided search (k=1 with A ≈ n/10 starting with 7
works most often; k=2 with A starting with 3 as backup), not as
polynomials in k. Numerical results:
- Numerical Calc 1: n = 840·10^i + m for the six m, i = 1..3000 (18,000 cases,
  numbers to >3000 digits): 92% success, ~3.5 msec/case.
- Numerical Calc 2: n = 840·i + m, i = 1..10000 (60,000 cases): **100%**
  success, ~142 msec/case, using the relaxed search space.
- Note: both grids are finite families (special forms), not the whole residue
  class; 100% on a tested prefix is not a covering system.

## Why the run needs it

- Confirms the open classes are solvable per-n with small x-offset (k=1 gives
  `x = (n+3)/4 + ...` i.e. `x ≈ ⌈n/4⌉`), consistent with Bradford's tables and
  Mihnea–Dumitru's counting.
- Marks the boundary: an algorithm with 100% on tested prefixes of the open
  class still does not settle the class; only an identity family (or covering
  system) does. The paper's theorem is a clean N&S reparametrisation the
  oracle can verify on the witnesses.

```claim
id: bhakti-suzuki-nand-s
statement: For n = 4s+1 prime, ESC has a solution iff there exist k ≥ 1, A ≥ 1 with (4k−1)A − (s+k) | A·n·(s+k), in which case x = s+k, y = An, z = An(s+k)/((4k−1)A−(s+k)) (or y,z swapped) solves 4/n = 1/x+1/y+1/z.
hypotheses: n = 4s+1 prime; x ≤ y,z WLOG.
holds-here: true — the six open classes are primes ≡ 1 (mod 840) ⊆ ≡ 1 (mod 4) = 4s+1.
status: sourced (Suzuki/Bhakti 2025, IAR paper; elementary proof + numerical validation; not yet re-checked by this run's oracle — flagged unverified here).
bearing: another parametrisation of the same solution set (x = ⌈n/4⌉+k, one denominator divisible by n); the obstruction to a covering family remains, per Schinzel Theorem 1, unless the family leaves the Z[x] identity shape.
anchor: research/sources/bhakti-constructive-algorithm.full.md
```

```claim
id: bhakti-calc-open-classes-100pct
statement: A guided (k,A)-search finds ESC solutions for all 60,000 tested n = 840·i + m, i = 1..10000, m in {1,121,169,289,361,529} (100% success), and for 92% of the 18,000 massive n = 840·10^i + m; no covering identity is given.
hypotheses: n in the stated finite grids (1 ≤ i ≤ 10000 or 1 ≤ i ≤ 3000), six residues m.
holds-here: true — evidence the open classes are pointwise easy; not a class identity.
status: sourced (Suzuki/Bhakti 2025, numerical; unverified independently here).
bearing: do not mistake per-n solvability of tested prefixes for a covering family; the deliverable remains an identity family or a covering system.
anchor: research/sources/bhakti-constructive-algorithm.full.md
```