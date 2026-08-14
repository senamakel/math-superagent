# Colour-critical graphs — the minimum-degree backbone for G-crit

**Sources:**
- A. Kostochka, "Color-Critical Graphs and Hypergraphs with Few Edges: A
  Survey", doi.org/10.1007/978-3-540-32439-3_9 (2006)
- "Graph coloring Parameters — A Survey", IJSRASET (2019)
- G.A. Dirac, "The structure of k-chromatic graphs", Fund. Math. 40 (1953)
  42–55 (the origin of k-critical graphs; cited by both surveys)
**Full texts:** NOT on disk — read via server-side search results.

## What this establishes — the G-crit claim's source

The `G-crit` gap in BACKWARD.md states: a vertex-minimal unit-distance graph of
chromatic number ≥ 5 is 5-critical, hence has minimum degree ≥ 4. The critical
graph theory behind it is standard and multiply sourced:

- **Definition (Dirac 1953).** A graph G is *k-critical* if χ(G) = k and every
  proper subgraph has χ < k (vertex-critical: every proper induced subgraph;
  edge-critical: every proper subgraph). A vertex-minimal graph of chromatic
  number k is vertex-critical.
- **Minimum degree bound (classic, in both surveys).** *If G is k-critical,
  then the minimum degree of G is at least k − 1.* Proof structure: if some
  vertex v had degree ≤ k−2, a (k−1)-colouring of G−v would extend to v since
  v sees at most k−2 colours among its neighbours and k−1 colours are
  available.
- **Consequences.** A 5-critical graph has δ ≥ 4 and hence e ≥ 5n/2 > 2n;
  a 5-critical graph on n vertices has at least 2n edges (e ≥ n·δ/2 ≥ 2n).
  This is the edge-count floor the size-lower-bound skeleton converts into
  per-n exclusion against the u(n) ceilings.
- The survey also notes: connectivity properties of k-critical graphs (Stiebitz
  1982 on Gallai's conjecture) — k-critical graphs are 2-connected for k ≥ 3,
  which further constrains a minimal counterexample's structure.

## Why it matters here

G-crit is the second gap of the size-lower-bound skeleton and a premise of the
G-exhaust sweep (5-critical ⇒ δ ≥ 4 ⇒ e ≥ 2n). This source establishes the
claim with a one-line proof and names Dirac as origin.

```claim
id: k-critical-min-degree
statement: If G is k-critical (chi(G)=k, every proper subgraph has chi<k), then the minimum degree of G is at least k-1; in particular a 5-critical graph has delta >= 4 and at least 2n edges on n vertices. A vertex-minimal k-chromatic graph is vertex-critical.
hypotheses: finite simple graphs; standard chromatic theory.
holds-here: yes - vertex-minimal unit-distance graphs of chi >= 5 are 5-critical, so any minimal counterexample has min degree >= 4 and e >= 2n.
status: sourced (Dirac 1953; stated in Kostochka 2006 survey and Suresh Kumar 2019 survey, via search excerpts; the delta >= k-1 proof is one line and standard)
bearing: serves gap G-crit; the e >= 2n floor is the chromatic wall the search must beat against the u(n) edge ceilings.
anchor: research/sources/kostochka-colour-critical-survey-2006.md
```

## Note on download

Full texts network-blocked. Status: **sourced via search excerpts; full texts
not on disk**.