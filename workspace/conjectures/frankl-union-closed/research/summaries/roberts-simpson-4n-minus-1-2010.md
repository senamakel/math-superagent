# Roberts & Simpson, "A note on the union-closed sets conjecture" (AJC 47:265-267, 2010)

**Source URL:** http://ajc.maths.uq.edu.au/pdf/47/ajc_v47_p265.pdf
(full text at `research/sources/roberts-simpson-4n-minus-1-2010.full.md`)

## What it is
Primary source for the `4q−1` lower bound on the size of a minimal
counterexample.

## What it establishes
- **Theorem 4**: If A is a minimal counterexample to the union-closed sets
  conjecture, then `|A| ≥ 4q − 1`, where `q` is the minimum cardinality of
  `∪A` taken over all counterexamples.
- **Corollary 5**: Since Bošnjak–Marković showed `q ≥ 12` (any minimal
  counterexample has ground set ≥ 12), a minimal counterexample has
  `|A| ≥ 47`.
- The proof: for a minimal counterexample with `|A| = 2n+1`, using the sets
  `Cx = ∪{A∈A : x∉A}` and the decomposition into H-elements (frequency exactly n)
  and the non-H elements, shows `n ≥ 2q−1`, hence `|A| = 2n+1 ≥ 4q−1`.
- Notes earlier bounds: `|A| ≥ 37` (Morris) and `|∪A| ≥ 12` (Bošnjak–Marković).
- The result applies to both the version that excludes the empty set and the
  version that allows it.

## Why it matters to this run
Primary source for the `verified-m-small` and `faro-roberts-simpson-40` claims;
closes a gap where the bound was anchored only to survey mentions.

## Status
Sourced (journal note, primary). Not numerically checked here.
