# Union-Closed Sets Conjecture — Library Root

This file is the phase-1 deliverable: it pins the structure of a minimal
counterexample, the current verification bound, and the restricted classes
already settled, each tied to a primary source in `research/sources/`.

The statement (union-closed sets / Frankl's conjecture, 1979): every finite
union-closed family `F ≠ {∅}` has an element present in at least `|F|/2`
members. `n` = ground set size (`|∪F|`), `m` = number of member sets (`|F|`).

## The current best constant (the live frontier)

Source: the entropy-era arXiv line (all downloaded).

- **Gilmer, arXiv:2211.09055** (Nov 2022): first constant bound, `c = 0.01`,
  by entropy. His method: `A,B` independent uniform in `F`; `A∪B ∈ F`, so
  `H(A∪B) ≤ log|F| = H(A) = H(B)`; if every element had density `< c`, an
  entropy inequality forces `H(A∪B) > H(A)`, a contradiction.
- **The `(3−√5)/2 ≈ 0.3819` bound** (the "barrier"): reached within days and
  independently by **Alweiss–Huang–Sellke** (2211.11731), **Chase–Lovett**
  (2211.11689, extends to `(1−ε)`-approximate union-closed), **Sawin**
  (2211.11504), **Pebody** (2211.13139). Key one-variable inequality
  `h(x²) ≥ φ·x·h(x)`, `φ = (1+√5)/2` (golden ratio); Boppana gave the elegant
  proof (arXiv:2301.09664).
- **What `(3−√5)/2` is a barrier FOR**: it is the *maximal constant obtainable
  by the tight iid-OR entropy inequality* — the minimum over distributions of
  `E[H(XY)] / E[H(X)]` (see AHS). It is **not** a barrier to the full
  conjecture. Sawin (2211.11504) showed a dependent-coupling (non-iid)
  refinement strictly exceeds it, and disproved a Gilmer conjecture that would
  have implied UC.
- **The current record**: **≈ 0.38234** made explicit by **Yu**
  (arXiv:2212.00658, Dimension-Free Bounds; obtainable form) and **Cambie**
  (arXiv:2212.12500), via Sawin-type dependent samples. **Liu**
  (arXiv:2306.08824, conditionally-IID coupling) analytically exceeds
  `0.3823455`, reaching **≈ 0.38271** under numerically verified hypotheses.
- **Where the entropy method is structurally capped**: no entropy proof to date
  reaches `1/2`. `1/2` is the conjecture and every entropy argument so far is
  bounded away from it by the shape of the inequality, not slack in estimates.

## Verified ranges (exact, by method)

Source: Bošnjak–Marković (arXiv:0711.3298, EJC 2008); Bruhn–Schaudt survey
(arXiv:1309.3297); Lo Faro / Roberts–Simpson.

- **Ground set `n ≤ 11`**: proved by Bošnjak–Marković (EJC 15 R88, 2008).
- **Ground set `n ≤ 12`**: Vučković–Živković, computer-assisted (per survey,
  unpublished / announced).
- **Families with `|F| ≤ 50`**: Lo Faro + the `|F| ≥ 4·n_ground − 1` bound
  (Roberts–Simpson 2010, AJC 47, and independently Lo Faro).
- **Large families**: `|F| ≥ 2^((3/2)n)` → UC, Balla–Bollobás–Eccles (JCTA
  2012); improved to `|F| ≥ 2^(n−1)` by Karpas (arXiv:1708.01434).
- **Minimal-counterexample structure (Roberts–Simpson / Lo Faro)**: if `q` is
  the minimal universe size over all counterexamples, any counterexample has
  `|F| ≥ 4q − 1`. With `q ≥ 12`: **any counterexample has `|F| ≥ 47`.**

## Restricted classes already settled (with hypotheses)

- **Contains a singleton `{x}`** → `x` abundant (trivial).
- **Contains a 2-element set `{x,y}`** → one of `x,y` abundant
  (Sarvate–Renaud).
- **Contains a 3-element set**: *does not* force UC. Ellis–Ivan–Leader
  (arXiv:2201.11484) construct, for any ε>0, a UC family with smallest set `S`
  of size `k` whose elements all appear in fraction `(1+o(1))·(log₂k)/(2k)`
  — in particular `< 1/2` for `k = 3`. (This is the fault line flagged in
  `problem.md`, now sourced.)
- **Lattice classes** (Poonen lattice formulation; JCTA 1992):
  distributive, complemented, geometric lattices (Poonen); modular (Abe–Nakano
  1998); lower semimodular (Reinhold); planar semimodular and large
  semimodular (Czédli–Schmidt 2008); breadth ≤ 2, and upper semimodular with
  few join-irreducibles (Joshi–Waphare 2019). Upper semimodular in general:
  **open**.
- **Graph formulation** (Bruhn–Charbit–Schaudt–Telle, EJC 2015): UC is
  equivalent to "every nontrivial graph has two adjacent vertices each in at
  most half its maximal stable sets." Trivially true for non-bipartite graphs;
  settled for chordal bipartite and bipartitioned circular interval graphs;
  open in general (bipartite case is the heart).
- **Approximate union-closed**: Chase–Lovett (2211.11689): for
  `(1−ε)`-approximate union-closed families (`ε < 1/2`), some element is in at
  least `ψ − δ` fraction, `ψ = (3−√5)/2`; and `ψ` is **optimal** for this
  relaxation. This shows the entropy method's barrier is real *for iid* but
  escapable by dependent couplings.
- **Separating families** (elements pairwise separable): UC holds if
  `|F| ≤ 2·n + n·log₂n − log₂log₂n` (Maßberg, arXiv:1508.05718, improving
  Falgas-Ravry's `2n`, arXiv:1101.2589).

## The three negative controls (from `problem.md`)

1. **`1/2` is attained**: power set `2^[n]` has every element at density
   exactly `1/2`. Any argument proving `> 1/2` is refuted.
2. **Union-closure must be used**: drop it and an antichain of large sets on a
   big ground set has all elements rare.
3. **Finiteness must be used**: infinite analogues fail (Bruhn–Schaudt survey
   notes the infinite family `{{i,i+1,…}}` has no infinite-frequency element).

## Entropy-method prizes available (relative value, after `problem.md`)

- **A proved barrier**: turn "the entropy method can't pass `c₀`" into a
  theorem with the extremal object exhibited. (The `(3−√5)/2` tightness is only
  for the iid-OR inequality.)
- **A better constant than the record** with a verified script checking the
  underlying inequality.
- **UC for a new class** (a lattice class, a graph class, families containing
  a specified small set).
- **A structural theorem about a minimal counterexample** (bounds on `n`, on
  `|F|`, on set sizes, on the density profile).

## Source library index

Full texts in `research/sources/*.full.md`; short digests in
`research/summaries/*.md`. All arXiv downloads carry their URL in the file.
Covered threads: entropy era (Gilmer, AHS, Chase–Lovett, Sawin, Pebody,
Boppana, Yu, Cambie, Liu), survey (Bruhn–Schaudt 2013), graph formulation
(Bruhn–Charbit–Schaudt–Telle 2015), lattice & minimal counterexamples
(Poonen refs, Bouchard 2025, Czédli–Schmidt refs, Joshi–Waphare refs),
verification (Bošnjak–Marković 2008, Marić–Živković–Vučković FC-families 2012),
small sets (Ellis–Ivan–Leader 2022, Pulaj 2021), large/separating families
(Balla–Bollobás–Eccles refs, Falgas-Ravry 2011, Maßberg refs, Karpas 2017).
