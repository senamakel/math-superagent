# Wikipedia — Rule 90 (elementary cellular automaton)

**Full text:** `research/sources/wikipedia-rule-90.full.md`
**Source URL:** https://en.wikipedia.org/wiki/Rule_90 (good article; retrieved 2026)

## What this is and why the run needs it

This is the canonical encyclopedic reference for the mechanism at the heart of the
run's **proved** interior claim (rule90-interior-xor / block-lemma apex:
a {0,2} block's halved entries evolve under XOR = Rule 90 = Pascal mod 2).
CONTEXT.md's Established section has long cited "Wikipedia (Rule 90)" and
"Wolfram MathWorld" as independent confirmation of that identification, but
neither page was on disk. This closes that empty- citation gap: the reference
tier for a claim the run treats as proved is now in the library.

## What it establishes

- **Definition.** Rule 90 is the elementary cellular automaton (Wolfram code 90 =
  `01011010_2`) in which each cell's next state is the **XOR of its two
  neighbours** — equivalently modulo-2 addition of left and right neighbours
  (`Mod[p + r, 2]`).
- **Deterministic solution (explicit formula).** After `n` iterations from
  initial configuration `x ∈ {0,1}^ℤ`:
  `[F^n(x)]_j = Σ_{i=0}^{n} C(n,i)·x_{2i−n+j} mod 2`.
  This is exactly the run's block-lemma apex formula restricted to the {0,2}
  halved regime: it is a mod-2 sum of binomial coefficients times initial bits.
- **Sierpiński triangle / Pascal mod 2.** Started from a single live cell, the
  time-space diagram is a Sierpiński triangle; a 1 appears exactly where Pascal's
  triangle has an odd entry (binomial mod 2 via XOR). Independent confirmation of
  the run's Sierpinski/Pascal-mod-2 identification.
- **Superposition / additivity.** Rule 90 is an additive CA: configuration evolves
  as the XOR of separately-evolved sub-configurations — the decomposition
  property the interior identification relies on.
- **Replication / Gould's sequence.** Row counts are powers of two (Gould's
  sequence A001316); the number of nonzeros in row `i` is `2^{s_2(i)}` where
  `s_2(i)` is the popcount of `i`. (Matches CONTEXT's claim about the Sierpinski
  gasket row counts `2^{s_2(k)}`.)
- **THE GILBREATH CONNECTION, stated explicitly.** The article's "Stunted trees
  and triangular clearings" section says: the Rule-90 automaton (on one of its two
  independent sub-configurations) was investigated in the early 1970s to gain
  insight into **Gilbreath's conjecture**. "When a contiguous subsequence of values
  in one row of the triangle are all 0 or 2, then Rule 90 can be used to determine
  the corresponding subsequence in the next row." This is *exactly* the run's
  proved rule90-interior-xor statement, stated in the literature. It cites the
  primary study: **Miller, J. C. P. (1970), "Periodic forests of stunted trees",
  Phil. Trans. R. Soc. Lond. A 266(1172) 63–111**, doi 10.1098/rsta.1970.0003 —
  the tree-growth metaphor ("a tree begins growing at each position whose value is
  1, branches grow upward-left/right when unopposed") reproducing Rule 90.
- **Surjectivity / predecessors.** Every configuration has exactly four
  predecessors; Rule 90 is surjective but not injective (no Garden of Eden).

## Bearing on this problem

- **Independently grounds** the run's proved interior identification
  (rule90-interior-xor) in an encyclopedic source *and* in a named 1970 primary
  paper (Miller), which the run did not previously hold.
- The "triangular clearings" / forest structure is a Rule-90 object worth noting:
  a consecutive row becoming simultaneously zero and then refilling from both
  ends is the erosion-and-regeneration picture in metaphor; Miller studied
  periodic configurations where all clearings stay bounded — the *boundedness* of
  clearings is a Rule-90 property that a regeneration argument could in principle
  harness (but per the run's refutations, must anyway face the CHT/Eppstein
  obstructions; Rule 90 alone does not regenerate the block boundary).

## Miller 1970 — next library step

The article points at a primary source the run does not hold and that is
directly on the proved-mechanism axis: **J. C. P. Miller, "Periodic forests of
stunted trees", Phil. Trans. R. Soc. Lond. A 266 (1970) 63–111** — the original
1970 study connecting Rule 90 to Gilbreath's conjecture via the tree-growth model.
Filing this would put a peer-reviewed simultaneous-treatment of the {0,2}/
forward-difference/Rule-90 object in the library where only derived summaries
sit now.

```claim
id: rule90-wikipedia-interior-confirmation
statement: Rule 90 (each cell is XOR of its two neighbours, = Pascal mod 2) has explicit deterministic solution [F^n(x)]_j = Σ_i C(n,i) x_{2i−n+j} mod 2; started from a single cell it produces the Sierpinski triangle; and for Gilbreath's conjecture a contiguous subsequence of {0,2} values in one row determines the corresponding subsequence in the next row by Rule 90.
hypotheses: binary cell values; halved {0,2} entries = bits.
holds-here: yes — this is exactly the proved rule90-interior-xor statement, independently confirmed.
status: sourced (encyclopedic), consistent with the run's proved derivation.
bearing: closes the empty-citation for the interior identification; surfaces Miller 1970 as a primary simultaneous treatment.
anchor: research/sources/wikipedia-rule-90.full.md
```

```claim
id: miller-1970-periodic-forests-stunted-trees
statement: Miller (1970) studied Rule 90 via a forest-of-growing-trees metaphor equivalent to the automaton, in connection with Gilbreath's conjecture, and found periodic initial configurations where all triangular clearings (simultaneously-zero rows refilled from the ends) stay bounded.
hypotheses: as recorded by Wikipedia; primary text not yet held.
holds-here: open (paper not yet in library).
status: asserted-by-source (Wikipedia summary).
bearing: a named 1970 peer-reviewed primary treatment of the {0,2}/Rule-90 interior; candidate next download.
anchor: research/sources/wikipedia-rule-90.full.md
```

```claim
id: rule90-rowcount-popcount
statement: In the i-th row of the Rule-90 Sierpinski pattern the number of live cells is 2^{s_2(i)} (Gould's sequence A001316), where s_2(i) is the number of 1-bits in the binary expansion of i.
hypotheses: single live cell initial condition.
holds-here: yes (matches the run's Sierpinski-gasket row-count form).
status: sourced.
bearing: independent encyclopedic confirmation of the Sierpinski gasket row-count structure the run cites.
anchor: research/sources/wikipedia-rule-90.full.md
```
