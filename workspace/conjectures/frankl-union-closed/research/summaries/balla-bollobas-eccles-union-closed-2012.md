# Balla, Bollobás, Eccles, "Union-closed families of sets" (JCTA 120, 2013; arXiv Nov 2011)

**Source URL:** https://www.igorballa.com/nov-30-UC.pdf
(full text at `research/sources/balla-bollobas-eccles-union-closed-2012.full.md`)

## What it is
Primary source for the union-closed *size problem* and the large-family
threshold. Determines `f(n,m)`, the minimum total size of a union-closed family
of `m` subsets of `[n]`, verifying a conjecture of Czédli–Maróti–Schmidt.

## What it establishes
- **Union-closed size problem solved**: `f(n,m)` determined precisely for all
  n, m, with extremal families given. This implies `m0 = 2^⌈2n/3⌉` (where m0 is
  the threshold above which every union-closed family has average set size ≥
  mn/2, hence satisfies UC).
- **Consequence (large families)**: the union-closed conjecture holds for
  families in P(n) with at least `2^(3n/2)` (= 2^(2n/3) × 2^n? — the bound is
  `m ≥ 2^(3.2 n)` in their notation = `2^(2n/3 · ... )`) elements. The threshold
  is `|F| ≥ 2^(3n/2)` per the standard reading (Karpas and the survey both state
  BBE as `|F| ≥ 2^(3n/2)`).
- Context: Czédli proved `2^n − m0 ≥ ⌊2^(n/2)⌋`; Czédli–Maróti–Schmidt proved
  `m0 ≥ 2^⌈2n/3⌉`. BBE settle it: `m0 = 2^⌈2n/3⌉`.
- **Roberts–Simpson bound stated here as**: if q is the smallest ground set over
  counterexamples, any counterexample has `|A| ≥ 4q−1`; since `q ≥ 12`, this
  gives UC for **`|A| ≤ 46`** (BBE's phrasing) — note discrepancy with the
  survey's "≤ 50".
- The `d_A(x) ≥ |A|/2` folklore attribution: says the conjecture was "well known
  by the mid-1970s as a folklore conjecture".

## Why it matters to this run
Primary source for the `large-family-progression` and `survey-theorem30-bbe`
claims; pins the exact large-family threshold and the extremal structure.

## Status
Sourced (author PDF, primary). Claims are theorems in the source. **Discrepancy to
resolve**: BBE says Roberts–Simpson gives UC for |A|≤46; the survey says ≤50
(this comes from 4·q−1 vs the small-case push to m≤12 → 4·12−1=47, and the
difference is how the 4m−1 and m≤12 combine — 47 vs 50 vs 46 need reconciliation
in the note reading Corollary 19's derivation).

## Discrepancy on the small-family bound
- Survey Corollary 19: "UC holds for union-closed families with at most 50 sets"
- BBE: "Roberts–Simpson implies the conjecture for |A| ≤ 46"
These differ; likely the survey uses m≤12 (Thm 17, Živković–Vučković computer)
→ 4·12−1 = 47 → "≤ 46"? and separately counts, while BBE writes 46 directly
from 4q−1 with q≥12. Record both, flag for the note.
