# Gyárfás, "Problems and Memories" (Erdős 100 memorial, 2013)

**Source:** András Gyárfás, "Problems and Memories", talk at Erdős 100, July 22 2013; arXiv:1307.1768v1. Hosted at the Rényi Institute: https://www.renyi.hu/~gyarfas/Cikkek/ar2erdos.pdf. Full text on disk: `research/sources/gyarfas-problems-memories.full.md`.

## What the source establishes

A memoir by one of the two authors of the Erdős–Gyárfás conjecture. It is a
problem-collection talk, not a research paper; its value for this run is
primary-source statements of the **degree-3-critical problem lineage**, which
is the closest structural class to a minimal counterexample.

**Section 2.1 — "Cycles in graphs without proper subgraphs of minimum degree 3".**

- **Observation (Erdős–Faudree–Rousseau–Schelp [9]).** Graphs with $n$
  vertices and $2n-1$ edges must contain proper subgraphs of minimum degree 3,
  but this fails for graphs with $n$ vertices and $2n-2$ edges; the wheel is
  such a graph.
- **EFGS [7] results.** The family $G(n)$ of graphs with $n$ vertices, $2n-2$
  edges and no proper subgraph of minimum degree 3: every $G \in G(n)$
  contains cycles $C_3, C_4, C_5$ and $C_k$ for $k \ge \log_2 n$, but not
  necessarily for $k \ge c\sqrt{n}$.
- **Conjecture 1 (EFGS [7] 1988).** Every $G \in G(n)$ contains cycles of
  length $i$ for every integer $3 \le i \le k$ where $k$ tends to infinity
  with $n$.

This is exactly the conjecture Narins–Pokrovskiy–Szabó disproved (a missing
23-cycle in infinitely many degree-3-critical graphs), stated here by one of
its authors, with the earlier EFGS results that motivated it. It anchors the
provenance: the *interval-of-short-cycle-lengths* conjecture for the
minimum-degree-3-critical class failed; the run's target (a *prescribed sparse
length*) is the harder version standing behind it.

The memoir also records, for context, the earliest Erdős–Gyárfás joint
problems (monochromatic path/cycle covers, (p,q)-colorings, balanced
colorings of $K_n$), several of which are still open — showing the range of
Erdős–Gyárfás work, none of which is the 2-power conjecture itself (which the
memoir does not state; the 2-power conjecture is in Erdős's 1997 Discrete
Math. problem paper, whose abstract-only page is also on disk).

## Why it matters for this problem

Primary-source confirmation of the exact chain:

1. EFRS 1990: $2n-1$ edges forces a proper δ≥3 subgraph; $2n-2$ does not.
2. EFGS 1988: the $G(n)$ class (2n−2 edges, no proper δ≥3 subgraph) has C3,
   C4, C5 and a cycle of length ≥ log₂n — but not necessarily ≥ c√n; and the
   conjecture that all short lengths 3..k, k→∞, appear (DISPROVED by NPS).
3. A minimal EG counterexample (Carr) sits in the *non-induced relaxation* of
   this class: no proper subgraph has δ≥3, but the edge count 2n−2 is not
   forced. NPS's Theorem 1.4 shows the non-induced version at 2n−2 edges is
   pancyclic — so the run's class (minimal counterexample, edge count free,
   non-induced condition) is genuinely intermediate: not the pancyclic
   non-induced class, not the not-necessarily-pancyclic induced class.

This is the cleanest structural-position statement the library now has: where
a minimal counterexample lives relative to the EFGS/NPS theory.

```claim
id: EG-EFRS-2n-1-forces-proper-d3
statement: Every graph with n vertices and 2n−1 edges contains a proper subgraph with minimum degree 3; this fails for 2n−2 edges (the wheel is a 2n−2-edge graph with no such proper subgraph). Due to Erdős–Faudree–Rousseau–Schelp, stated in Gyárfás's memorial.
hypotheses: finite simple graph, n vertices, 2n−1 edges
holds-here: yes — this is the boundary that makes degree-3-critical graphs (and hence the near-class of a minimal counterexample) edge-tight at 2n−2
status: proved (source; folklore-verifiable)
bearing: bounds the edge count regime where no-proper-δ≥3-subgraph graphs can live; a minimal counterexample may have anywhere from 3n/2 to 2n−2 edges, so the 2n−2 boundary is the top of its range
anchor: research/summaries/gyarfas-problems-memories.md
```

```claim
id: EG-EFGS-1988-short-cycles
statement: Every graph with n vertices, 2n−2 edges and no proper subgraph of minimum degree 3 contains cycles of lengths 3, 4, 5 and at least one of length ≥ log2 n; but not necessarily any cycle of length ≥ c√n. (EFGS 1988, as reported by Gyárfás.)
hypotheses: n vertices, 2n−2 edges, no proper δ≥3 subgraph
holds-here: no — the class is not a minimal-counterexample class (edge count mismatch); but the log2 n guaranteed cycle is the reason the power-of-two conjecture is *plausible* for this class: log2 n ≥ 4 already at n=16
status: proved (in EFGS 1988; historically settled, restated by Gyárfás)
bearing: the log2 n short-cycle guarantee is the closest known pro-power-of-two evidence in the near-minimal class; a minimal counterexample would need to break this pattern while being allowed more edges
anchor: research/summaries/gyarfas-problems-memories.md
```

```claim
id: EG-EFGS-conjecture-1988-disproved
statement: EFGS (1988) conjectured that every G ∈ G(n) (n vertices, 2n−2 edges, no proper δ≥3 subgraph) contains cycles of every length 3..k with k→∞; this conjecture is FALSE (NPS: infinitely many such graphs have no 23-cycle). Stated by Gyárfás in the memoir as Conjecture 1; disproved by Narins–Pokrovskiy–Szabó 2016.
hypotheses: G(n) class as above
holds-here: no (class mismatch) — but it is the canonical example of an interval-of-short-lengths conjecture failing in the exact near-class, and it is what makes the run's prescribed-sparse-length target strictly harder
status: disproved (NPS; both sources in library)
bearing: closes the "all short intervals" route in the near-minimal class; the open question NPS pose (can even lengths 4,6,…,2C(n) be forced?) is the run's nearest neighbour among published open problems
anchor: research/summaries/gyarfas-problems-memories.md
```