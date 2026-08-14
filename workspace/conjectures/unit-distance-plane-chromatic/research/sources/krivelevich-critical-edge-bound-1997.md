# Improved bound on minimal edges in color-critical graphs — Krivelevich 1997

**Source:** Michael Krivelevich, "An improved bound on the minimal number of
edges in color-critical graphs", The Electronic Journal of Combinatorics 5(1)
(1998), #R4. Submitted 1997-06-26, accepted 1997-11-24.
URL: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v5i1r4
DOI: 10.37236/1342. Full text fetched server-side via read_sources (abstract
and article page); PDF at
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v5i1r4/pdf/.

## What this establishes

The sharpest published lower bound on the number of edges in a k-critical
graph on n vertices, k >= 4, n > k:

- **Trivial bound (Dirac; every vertex degree >= k-1):**
  |E(G)| >= (k-1)/2 · |V(G)|.
- **Gallai 1963:** for k >= 4, G not K_k:
  |E(G)| >= ((k-1)/2 + (k-3)/(2(k^2-3))) · |V(G)|.
- **Krivelevich (Theorem):** for k >= 4, |V(G)| > k:
  |E(G)| >= ((k-1)/2 + (k-3)/(2(k^2-2k-1))) · |V(G)|.

For k = 5, Krivelevich's coefficient is
(5-1)/2 + (5-3)/(2(25-10-1)) = 2 + 2/28 = 2 + 1/14 ≈ 2.07143, versus Gallai's
2 + 2/(2·22)= 2 + 1/22 ≈ 2.04545, versus the trivial 2. So a 5-critical graph
on n > 5 vertices has e >= (29/14)n — a strict improvement over the
e >= 2n floor used in the run's size-lower-bound skeleton.

**Method:** decomposition of a k-critical graph G into the subgraph L(G) of
low-degree (degree k-1) vertices and H(G) of high-degree vertices. L(G) is a
k-Gallai forest (Gallai's structure theorem), whose edge count is bounded via
Gallai's and Stiebitz's results; combining the L and H contributions yields the
improved coefficient.

## Why it matters here

The run's G-crit gap and the size-lower-bound skeleton use the e >= 2n floor on
5-critical graphs (from delta >= 4). Krivelevich sharpens this floor to
e >= (29/14)n ≈ 2.0714n for every 5-critical graph with n > 5. Against the
Alexeev–Mixon–Parshall u(n) edge-count ceilings (which bound edges, not
chromatic number), a strictly higher edge floor excludes more small n from
hosting a minimal 5-chromatic unit-distance graph — the direction of progress
the size-lower-bound route needs.

## Note on download

Downloaded via server-side read_sources (article view page); the PDF is a
4-page note, freely accessible at the EJC URL above. This is a technique-tier
tool theorem (edge-minimality of colour-critical graphs), not answer-tier
material for the Hadwiger–Nelson problem.

```claim
id: krivelevich-5-critical-edge-bound
statement: For k >= 4 and every k-critical graph G on more than k vertices, |E(G)| >= ((k-1)/2 + (k-3)/(2(k^2-2k-1))) * |V(G)| (Krivelevich 1997, EJC 5(1) #R4, DOI 10.37236/1342). For k = 5 this is e >= (29/14)n, strictly stronger than the e >= 2n bound that follows from minimum degree >= 4 (Dirac). Improves Gallai 1963's ((k-1)/2 + (k-3)/(2(k^2-3))) coefficient.
hypotheses: G finite simple k-critical graph (chi(G)=k, every proper subgraph has chi < k); k >= 4; |V(G)| > k.
holds-here: yes — a vertex-minimal 5-chromatic unit-distance graph would be 5-critical, so any such graph on n > 5 vertices has e >= (29/14)n; combined with u(n) edge-count ceilings this excludes more small n from hosting a minimal counterexample than the e >= 2n floor did.
status: sourced (primary abstract and article text read verbatim via read_sources; theorem statement quoted in full above)
bearing: strengthens the edge-count floor in the G-crit gap and the size-lower-bound skeleton (G-exhaust); turns a tighter floor into wider per-n exclusions.
anchor: research/sources/krivelevich-critical-edge-bound-1997.md
```

```claim
id: krivelevich-method-lhv-decomposition
statement: Krivelevich's proof decomposes a k-critical graph into low-degree (degree k-1) vertices L(G) and high-degree vertices H(G); L(G) is a k-Gallai forest, and the edge bound follows from Gallai's/Stiebitz's structural results on these forests combined with the H(G) contribution.
hypotheses: k-critical graphs, k >= 4.
holds-here: yes — gives the run a structural vocabulary (low/high vertex decomposition, Gallai forests) for analysing any candidate minimal counterexample's edge distribution.
status: sourced (described in the article's abstract and the EJC page)
bearing: structural handle for attacking candidate 5-critical unit-distance graphs: their low-vertex subgraph must be a 5-Gallai forest.
anchor: research/sources/krivelevich-critical-edge-bound-1997.md
```