# Cycles in graphs without proper subgraphs of minimum degree 3

**Erdős, Faudree, Gyárfás, Schelp**. Ars Combinatoria 25B (1988) 195–201.
**FULL TEXT HELD** at
`research/sources/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.full.md`
(Rényi archive PDF).

<!-- source: https://www.renyi.hu/~p_erdos/1988-06.pdf -->

## What the source establishes

This is the **foundational paper** that defines and initiates the study of
*degree-3-critical graphs*. Notation (non-induced sense): $\mathcal{G}^*(n,m)$
= graphs with $n$ vertices, $m$ edges, and **no proper subgraph** of minimum
degree 3.

- $G \in \mathcal{G}^*(n, 2n-2)$ has minimum degree exactly 3 (Cor 1); every
  $G \in \mathcal{G}(n,2n-2)$ contains a subgraph of min degree 3 (best
  possible: some $G \in \mathcal{G}(n,2n-3)$ has none mod its own subgraphs).
- **Theorem 1**: the vertices of $G \in \mathcal{G}'(n,2n-2)$ can be ordered
  with a prescribed-degree degeneracy structure ($d^+(x_1) \le \dots$).
- **Theorem 2**: for $n \ge 5$, $G \in \mathcal{G}'(n,2n-2)$ contains a $C_3$
  and a $C_4$ (and, per the NPS retelling, a $C_5$).
- **Theorem 3**: if $n \ge 6$ and $G \in \mathcal{G}^*(n,2n-4)$ then girth
  $g(G) \le 4$; for $G \in \mathcal{G}^*(n,2n-6)$, $g(G) \le 5$.
- **Theorem 4**: for every $r$ there is $c = c(r)$ and a graph
  $G \in \mathcal{G}^*(n, 2n - c(r))$ with girth $> r$ — high-girth balanced
  constructions exist up to an edge-cost tradeoff.
- **Theorem 5**: if $G \in \mathcal{G}^*(n,2n-2)$ then $G$ contains a cycle of
  length at least $(\log n)$. (Largest cycle is $\Omega(\log n)$.)
- **The EFGS Conjecture**: if $G \in \mathcal{G}^*(n,2n-2)$, then $G$ contains
  all cycles of length at most $k$, where $k \to \infty$ with $n$. **This is
  the conjecture NPS (2017) disproved** (no 23-cycle for an infinite family,
  in the *induced* reading).

## Why it matters to the Erdős–Gyárfás run

- This 1988 paper is the **origin of the degree-3-critical class** that the
  run's near-cubic spine thread lives in. It establishes the baseline:
  degree-3-critical graphs force $C_3, C_4, C_5$ and a cycle of length
  $\Omega(\log n)$, plus high-girth constructions.
- Direct relevance to E–G: a minimal E–G counterexample is degree-3-closed
  downward, so its "spine" is a degree-3-critical graph. EFGS guarantee
  $\Omega(\log n)$ as the longest cycle, which does **not** itself force a
  power of two (a power of two can be as large as one needs, but the presence
  of a long cycle is compatible with missing several 2-powers).
- The EFGS Conjecture (all small cycle lengths) is what NPS refuted; that
  refutation (no 23-cycle at arbitrary size in degree-3-critical graphs) is
  the sharpest caution available that **degree-3-criticality alone does not
  force a prescribed sparse cycle length** — the $\delta \ge 3$ guard in E–G is
  doing work *beyond* mere degree-3-criticality and beyond short-cycle
  richness.

## Status

Read from the full text (Rényi PDF). Theorem statements verified as present;
not independently recomputed. This is the primary source for the degree-3-
critical class; previously the library held only retellings (NPS, Di Braccio,
Rautenbach). Closes a long-standing gap.

```claim
id: efg degree-3-critical-longest-cycle-omega-logn
statement: If G is an n-vertex graph with 2n-2 edges and no proper subgraph of minimum degree 3 (degree-3-critical), then G contains a cycle of length at least log n; and (n>=5) cycles of length 3 and 4.
hypotheses: G in G^*(n,2n-2), n >= 5
holds-here: yes (the near-cubic spine of a minimal E-G counterexample is degree-3-critical, so its longest cycle is at least logarithmic and it has C3, C4)
status: asserted (full text held, Rényi PDF)
bearing: baseline cycle lengths of the degree-3-critical class; a log n longest cycle does NOT force a power of two, and the class can avoid length 23 at arbitrary size (NPS). So short-force + one long cycle is all 3-criticality gives; the 2-power must come from structure beyond it.
anchor: research/sources/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.full.md
```

```claim
id: efg-conjecture-refuted-by-nps
statement: EFGS conjectured every degree-3-critical graph (induced reading) has all cycles of length at most k, k -> inf; this is FALSE per Narins-Pokrovskiy-Szabo (infinite family with no 23-cycle).
hypotheses: degree-3-critical (induced sense), n -> inf
holds-here: yes (refutation establishes degree-3-critical graphs need NOT have all short cycle lengths)
status: asserted (both full texts held)
bearing: marks the precise limit of what degree-3-criticality forces on cycle lengths; short-cycle richness is bounded (C3,C4 and stuff up to some length about 18 for even 1-3 trees per NPS Thm 1.3, but 23 can be missing). Directly relevant to whether the near-cubic spine can force a 2-power.
anchor: research/sources/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.full.md
```
