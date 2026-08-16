# Bruhn & Schaudt, "The journey of the union-closed sets conjecture" — full body (arXiv:1309.3297, 2013)

**Source URL:** https://arxiv.org/html/1309.3297v2
(full body at `research/sources/bruhn-schaudt-journey-survey-2013-body.full.md`)

## What it is
The canonical pre-entropy survey (the map of everything before late 2022).
This file is the *full body* (105 KB), which was previously only abstract-only
in the library. It is the primary anchor for the verification ranges, lattice
classes, FC-family history, and large-family thresholds.

## What it establishes (by section)

### 3.2 Lattice results (confirmed)
```claim
id: lattice-settled-classes-survey
statement: Rival mentions without proof that UC holds for distributive and
  geometric lattices. Poonen explicitly proved distributive, geometric and
  complemented lattices. Abe–Nakano proved modular lattices (includes
  distributive). Reinhold generalised to lower semimodular lattices, currently
  the strongest lattice-class result.
hypotheses: L a finite lattice of the stated class with >1 element.
holds-here: true (these are the settled lattice classes, now primary-sourced).
status: asserted-by-source (survey reports them; primary lattice proofs are in
  the cited papers, Poonen JCTA 1992, Abe–Nakano, Reinhold).
bearing: the lattice classes already settled; any new class proof is a result.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §3.2
```

### 5 Local configurations (Poonen's theorem, Sarvate–Renaud)
```claim
id: sarvate-renaud-2set
statement: Sarvate–Renaud observed that any singleton in a union-closed family
  is abundant, and of the two elements of a 2-set at least one is abundant.
hypotheses: A ∪-closed, contains a singleton / 2-element set.
holds-here: true.
status: asserted-by-source (survey reports; original Sarvate–Renaud 1989).
bearing: the "small sets force abundance" line; the 2-set case is the boundary —
  the 3-set case (EIL) does NOT force abundance.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §5
```

```claim
id: poonen-fc-characterisation
statement: A union-closed family L with universe [k] is FC (every union-closed
  A ⊇ L satisfies UC, with an abundant element in [k]) iff there are reals
  c_1,...,c_k ≥ 0, Σc_i=1, such that for every union-closed K ⊆ 2^[k] with
  K = L ⊎ K, Σ c_i |K_i| ≥ (1/2)|K|.
hypotheses: L union-closed on [k].
holds-here: true (this is the exact FC/weight-characterisation).
status: asserted-by-source (Theorem 16 of survey, from Poonen [50]).
bearing: the FC/weight formulation GOAL.md cites; the engine of pre-2022 progress.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §5 Thm 16
```

### 5.1 Small finite families (verification ranges)
```claim
id: survey-thm17-m12
statement: The union-closed sets conjecture holds for union-closed families on
  at most 12 elements (Živković–Vučković [68], computer-assisted).
hypotheses: |U(A)| ≤ 12, ||closed.
holds-here: true.
status: asserted-by-source (survey Theorem 17; computer-assisted).
bearing: minimal counterexample has |∪A| ≥ 13.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §5.1
```

```claim
id: survey-lemma18-4m-minus-1
statement: (Lo Faro lemma, rediscovered by Roberts–Simpson) under the assumption
  that UC fails, if m is the minimum universe size over counterexamples, any
  counterexample has at least 4m−1 member-sets. This gives, with Theorem 17
  (m≤12), Corollary 19: UC holds for union-closed families with at most 50 sets.
hypotheses: A counterexample, m = min universe size over counterexamples.
holds-here: true.
status: asserted-by-source (survey Lemma 18 / Corollary 19; independently
  Roberts–Simpson primary source in this library).
bearing: minimal counterexample has |A| >= 4q-1. With the survey's m<=12 this
  was >= 47; with the later Zivkovic-Vuckovic m>=13 (2017 computer-assisted)
  and Hu's Theorem 1 the value is >= 4*13-1 = 51 (claim hu-theorem1-4m-minus-1,
  research/summaries/hu-union-closed-2017.md). Superseded numerical value, not a
  contradiction: the 47 used the older m<=12, the 51 uses m>=13. |F| <= 50
  settled either way.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §5.1
```

### History of small-case verification
Sarvate–Renaud [62]: n≤11 and (63): n≤19 (variant excluding empty set). Poonen
via his Theorem 16: m≤7, n≤28. Lo Faro [22]: m≤9, n≤36. Morris [46]: again
m≤9, n≤36 via FC-families. Marković [45]: m≤10 via weights. Bošnjak–Marković
[10]: m=11. Živković–Vučković [68]: m≤12 (computer).

### 6.4 Up-compression / large families
```claim
id: survey-theorem30-bbe
statement: (Balla, Bollobás, Eccles [9], Theorem 30) solves the union-closed
  size problem: determines the minimum average size of a set in a union-closed
  family of m subsets of an n-element ground set, verifying a conjecture of
  Czédli–Maróti–Schmidt; consequently UC holds when |F| ≥ 2^{3n/2}.
hypotheses: |F| ≥ 2^{3n/2}, F union-closed ⊆ 2^[n].
holds-here: true (large-family threshold).
status: asserted-by-source (survey Theorem 30; primary BBE in this library).
bearing: the large-family settled class ~2^{3n/2}; RHS threshold for a
  counterexample.
anchor: research/sources/bruhn-schaudt-journey-survey-2013-body.full.md, §6.4
```

## Why it matters to this run
This full body is the load-bearing primary anchor for nearly every
"asserted-by-source" claim in CLAIMS.md (lattice classes, verification ranges,
FC characterisation, large families, Sarvate–Renaud 2-set). It converts those
rows from "recalled / synthesized" to "on disk, citeable".

## Status
Sourced (survey, primary anchor). Not numerically checked here.
