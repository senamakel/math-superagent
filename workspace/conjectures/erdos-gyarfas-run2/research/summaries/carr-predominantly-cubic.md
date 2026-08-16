# Carr 2026 — Minimal counterexample is predominantly cubic

Source: arXiv:2605.22844 "Every Minimal Counterexample to the Erdős–Gyárfás
Conjecture is Predominantly Cubic" (Avery Carr, 13 May 2026, 4 pp).
Full text: [[carr-predominantly-cubic.full]] (landing page/abstract held; the
proof body is not in the library — this note rests on the abstract).

## What it establishes

A **minimal counterexample** is a graph of minimum possible order and size,
δ ≥ 3, containing no cycle of length a power of two.

Three structural statements about any minimal counterexample:

1. **Markström's structure** (attributed, restated): the deg-≥4 vertices form
   an independent set; the remaining vertices (a non-empty set) have degree
   exactly 3. Equivalently, no edge joins two vertices of degree ≥ 4.
2. Every vertex is adjacent to a vertex of degree exactly 3.
3. At least 4/7 of the vertices have degree exactly 3.
4. Consequence of (1): every **regular** minimal counterexample is cubic.

## What it implies here

The independent-set fact is the load-bearing structure this run's argument
attacks. It constrains the degree distribution hard: cubics dominate (≥4/7),
deg-≥4 vertices form an independent set and touch only degree-3 vertices. A
minimal counterexample is therefore *nearly* cubic, and where it departs from
cubic it does so in a controlled way. Bensmail's near-misses (all 2-power
cycles of length 4-only or 8-only) are cubic and consistent — they are not
eliminated by any of this.

## Not settled

- The abstract gives no explicit non-constant lower bound on n beyond ≥ 32
  (Balaji SMS). The 4/7 bound is the strongest quantitative degree-density
  statement available.

```claim
id: ce-deg-structure
statement: In a minimal counterexample the degree-≥4 vertices form an independent set and the remaining (non-empty) vertices have degree exactly 3.
hypotheses: G a vertex- and edge-minimal counterexample (δ ≥ 3, no power-of-2 cycle)
holds-here: yes (this is exactly the counterexample class under attack)
status: proved (Markström, in primary source; restated in Carr abstract)
bearing: every non-cubic vertex sits among degree-3 vertices; regular CE is cubic
anchor: research/sources/markstrom-extremal-graphs-cycles.full.md
answers: where-degree-4-vertices-live
```

```claim
id: ce-predominantly-cubic
statement: Every vertex of a minimal counterexample is adjacent to a degree-3 vertex, and at least 4/7 of its vertices have degree exactly 3.
hypotheses: G a minimal counterexample
holds-here: yes
status: asserted (Carr abstract; proof body not in library)
bearing: degree-3 vertices form a dominating "spine"; bounds the excess above cubic
anchor: research/summaries/carr-predominantly-cubic.md
```

```claim
id: regular-ce-is-cubic
statement: Every regular minimal counterexample is cubic.
hypotheses: G a minimal counterexample that is d-regular
holds-here: yes
status: proved
follows-from: ce-deg-structure
anchor: research/summaries/carr-predominantly-cubic.md
```
