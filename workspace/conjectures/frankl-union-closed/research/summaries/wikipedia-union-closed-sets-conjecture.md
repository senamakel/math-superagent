# Wikipedia — "Union-closed sets conjecture" (encyclopedic entry)

**Source URL:** https://en.wikipedia.org/wiki/Union-closed_sets_conjecture · **Full text:** [[wikipedia-union-closed-sets-conjecture.full]]

## Why it is in the library

The canonical encyclopedic entry, cited by the library's own survey sources
(Bruhn–Schaudt 2013). It fixes the statement, the history, the concise summary
of partial results, and the graph formulation. It is a secondary reference — the
numbers here are retellings of the primary papers already held — but it is the
cheapest way to (a) cross-check the run's established claims and (b) catch any
settled class or current record the library has missed.

## What it establishes (cross-checked against the primary sources already held)

- **Best constant:** an element belongs to at least **0.38271** of the sets
  (Liu, arXiv:2306.08824) — matching library claim `daswu-record-0-3823455` /
  `liu-conditionally-iid`; built on Gilmer's 0.01, improved the same week to
  `(3−√5)/2 ≈ 0.381966` (Gilmer 2211.09055; AHS/Pebody/Sawin/Chase–Lovett).
- **Verified ranges:** families of at most **50 sets** (Roberts–Simpson 4q−1
  plus Vučković–Živković n≥13), and families whose union has at most **12
  elements** (Vučković–Živković 2017, improving Bošnjak–Marković 2008). Matches
  `verified-m-small`, `verified-n12-comp-primary`.
- **Smallest set:** 1- or 2-element smallest set ⟹ UC (Sarvate–Renaud 1989);
  **not** true for 3-element sets (Sarvate–Renaud, Graham). Matches
  `sarvate-renaud-2set`, `eil-small-sets`.
- **Large families:** `≥ (1/2 − ε)2ⁿ` subsets, unpublished preprint (Karpas
  2017). Matches `karpas-large-families`.
- **Chain condition class (NEW to library):** families with every chain of
  length ≤ 3 (short chain no more than 3) or ≥ n−1 (long chain no less than
  n−1) satisfy UC — attributed to **Tian (2021)**. This is a settled class not
  previously in the library's claim list; the library holds Colbert's
  chain-condition work but not this specific Tian reference.
- **Graph formulation:** equivalent to "every finite non-empty graph contains
  two adjacent non-heavy vertices"; automatically true with an odd cycle;
  bipartite case is the heart. Settled for chordal bipartite, bipartite
  series-parallel, and bipartite max-degree-three graphs. Matches `graph-*`.

```claim
id: wikipedia-current-record
statement: As of this encyclopedic entry, the best known constant for the
  union-closed sets conjecture is 0.38271 (Liu, arXiv:2306.08824), built on
  Gilmer's breakthrough 0.01 and the same-week improvement to (3−√5)/2 ≈ 0.381966.
  Verified ranges: |F| ≤ 50 and |∪F| ≤ 12.
hypotheses: F nonempty finite union-closed family.
holds-here: yes — agrees with the primary sources in the library
  (daswu-record-0-3823455, liu-conditionally-iid, verified-m-small,
  verified-n12-comp-primary). Note the encyclopedic source cites Liu 0.38271 as
  the headline number without flagging that it is a preprint/conditional; the
  library's published-record claim (published-record-c) correctly separates the
  published record (Yu 0.38234, Entropy 2023) from the preprint 0.38271.
status: sourced (encyclopedic secondary; cross-checked against primary sources
  already in library)
bearing: independent confirmation that the library's record and verification
  claims match the current encyclopedic understanding; records the preprint-vs-
  published distinction as the one place the encyclopedia is looser than the run.
anchor: research/sources/wikipedia-union-closed-sets-conjecture.full.md
```

```claim
id: tian-chain-class
statement: The union-closed sets conjecture holds for families in which every
  chain of sets has length (number of members) either ≤ 3 or ≥ n−1 (short chain
  no more than 3, or long chain no less than n−1), where n = |ground set|.
hypotheses: F union-closed, finite, nonempty; chain-length constraint on all
  maximal chains.
holds-here: yes — a settled restricted class via the chain-length condition.
status: asserted-by-source (Wikipedia cites Tian 2021; the Tian paper is NOT yet
  in the library — this is a NEW lead, see REQUESTS).
bearing: a restricted class the run could either verify from the primary source
  or find a neighbouring chain-class result for; complements Colbert's
  chain-condition work already in the library.
anchor: research/sources/wikipedia-union-closed-sets-conjecture.full.md
  (Wikipedia note 9 → Tian (2021))
```
