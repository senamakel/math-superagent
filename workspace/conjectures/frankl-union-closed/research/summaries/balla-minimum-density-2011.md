# Balla, "Minimum density of union-closed families" (arXiv:1106.0369, 2011)

**Source URL:** https://arxiv.org/pdf/1106.0369 (downloaded; full text at
`research/sources/balla-minimum-density-2011.full.md`)

## What it is
Igor Balla, 2011. Proves Wójcik's density conjecture. The pre-entropy,
combinatorial (Reimer-based) line — it predates Gilmer's 2022 breakthrough.

## What it establishes
- **Density bound**: For a union-closed family F with n = |∪F|, the density
  (average set size over n) is at least (log₂ n)/(2n), verifying Wójcik's
  conjecture; asymptotically s_n = (1+o(1))·(log₂ n)/(2n).
- **Corollary 2**: For n ≥ 16, some element appears in at least
  √((log₂ n)/n)·(|F|/2) sets of F.
- States Conjecture 2 (Wójcik): the minimizer of density is of the form
  {A : A ⊆ [k]} ∪ {[n]} with k = ⌊log₂ n⌋ or ⌈log₂ n⌉.
- Uses **Reimer's result** (the "average set size / average complement" bound)
  as the engine — Reimer's theorem is a load-bearing input here.

## Why it matters to this run
- It is the canonical source for the **large-family / density** regime:
  element in ≥ √((log₂ n)/n)·(|F|/2) sets. This is one of the `problem.md`
  "predating and asymptotically weaker than Gilmer's" bounds — now primary-sourced.
- Corollary 2: for n ≥ 16 the guaranteed fraction is √((log₂ n)/n)/2, which
  exceeds 1/2 when... (log₂ n)/n > 1, i.e. never for the 1/2 target directly —
  it is a low-density regime bound, weakest where Gilmer is strong.
- The Wójcik density conjecture and its minimizer shape are relevant to the
  "minimal counterexample" structural programme.

## Status
Sourced (arXiv 2011). Claims marked as theorems in the source; not yet checked
numerically here.

```claim
id: balla-min-density
statement: For a union-closed family F with n=|∪F|, density (average set size over n) ≥ (log₂n)/(2n); asymptotically s_n=(1+o(1))(log₂n)/(2n). Cor 2: for n≥16 some element appears in ≥√((log₂n)/n)·(|F|/2) sets. This is Balla's proof of Wójcik's density conjecture, Reimer-based.
hypotheses: F finite union-closed, n=|∪F| (Cor 2 needs n≥16)
holds-here: yes (it is the small-density/large-family regime; weakest where the entropy line is strong)
status: asserted (theorems in the source; not re-checked here)
bearing: the pre-Gilmer density bound; also poses Wójcik's minimizer conjecture ({A:A⊆[k]}∪{[n]}, k≈⌊log₂n⌋) relevant to minimal-counterexample structure.
anchor: research/sources/balla-minimum-density-2011.full.md
```

## Bearing
Clarify: this is a *density* result, not a UC constant result — it lives in the
regime the entropy method does not cover, and does not approach 1/2 directly.
