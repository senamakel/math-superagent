# Narins–Pokrovskiy–Szabó, "Graphs without proper subgraphs of minimum degree 3 and short cycles"

**Source:** Lothar Narins, Alexey Pokrovskiy, Tibor Szabó, *Graphs without proper subgraphs of minimum degree 3 and short cycles*, Combinatorica 37 (2017) 1219–1237 (published 2016 online); arXiv:1408.5289. Full text on disk: `research/sources/narins-pokrovskiy-szabo-degree3-critical.full.md` (from the arXiv HTML).

## What the source establishes

**Setting.** A *degree-3-critical* graph is an $n$-vertex graph with exactly
$2n-2$ edges and no proper *induced* subgraph of minimum degree 3. Every graph
with $n$ vertices and at least $2n-2$ edges contains an induced subgraph of
minimum degree 3 (Lemma 4.2), so degree-3-critical graphs are the edge-minimal
members of the $\delta \ge 3$ world. Erdős–Faudree–Gyárfás–Schelp (1988)
conjectured

> **Conjecture 1.1 (EFGS 1988).** Every degree-3-critical graph on $n$
> vertices contains cycles of all lengths $3, 4, 5, \dots, C(n)$ for some
> $C(n) \to \infty$.

**Theorem 1.2 (disproof of Conjecture 1.1).** There is an infinite sequence of
degree-3-critical graphs $(G_n)$ that contain **no cycle of length 23**.

The construction: $G(T)$ from an even 1-3 tree $T$ (tree with all degrees 1 or
3, leaves in one bipartition class) by adding two adjacent universal-type
vertices $x, y$ each joined to all leaves. Lemma 2.1 gives the exact cycle
correspondence:

- $G(T)$ has a cycle of length $2k+1$ iff $T$ has a leaf-to-leaf path of
  length $2k-2$.
- $G(T)$ has a cycle of length $2k$ iff $T$ has two vertex-disjoint
  leaf-to-leaf paths of total length $2k-4$, or a single leaf-to-leaf path of
  length $2k-2$.

The missing 23-cycle comes from a periodic 20-avoiding odd-even sequence
(Theorem 2.5), producing trees $T_n$ with no leaf-to-leaf path of length 20.

**Theorem 1.3.** (i) Every sufficiently large even 1-3 tree contains
leaf-to-leaf paths of every even length $0, 2, \dots, 18$. (ii) There is an
infinite family of even 1-3 trees with no leaf-to-leaf path of length 20.
This is sharp in the sense that length 20 is exactly what an infinite family
can avoid: $2m$-avoiding sequences exist exactly for $2m \ge 20$.

**Theorem 1.4 (characterization, non-induced version).** If $G$ is an
$n$-vertex graph with $2n-2$ edges and *no proper (not necessarily induced)
subgraph* of minimum degree 3, then $G$ is **pancyclic** (contains cycles of
every length $3, \dots, n$). Such graphs are exactly the wheels and the graphs
obtained by gluing two copies of $H_i, H_j$ at their connectors (Theorem 4.1).

**Proposition 5.1.** Every degree-3-critical graph on $n \ge 6$ vertices
contains a 6-cycle.

**Ordering lemma (Lemma 4.3).** Every degree-3-critical graph has an ordering
$x_1, \dots, x_n$ with forward degrees $3, 2, 2, \dots, 2, 1$ and (for
$n \ge 7$) $d(x_n) \ge 4$. This is a strong structural handle: degree-3-critical
graphs are "almost 2-degenerate" in a peeled ordering.

**Problem 6.1 (open).** Is there $C(n) \to \infty$ such that every
degree-3-critical graph contains cycles of all lengths $4, 6, 8, \dots,
2C(n)$? — i.e., can even lengths be forced in an initial segment? Open as of
this paper.

## Why it matters for this problem

A minimal counterexample $G$ to the Erdős–Gyárfás conjecture has
$\delta(G) \ge 3$ and, by Carr's Lemma 0.1 (every proper subgraph $H$ has
$\delta(H) \le 2$), every proper subgraph has a vertex of degree $\le 2$. The
NPS class is *exactly* the same property restricted to induced subgraphs with
$2n-2$ edges. So NPS is the structural theory of the near-class a minimal
counterexample belongs to:

- EFGS 1988's conjecture, which NPS disproved, was an *interval* statement
  (all short cycle lengths) about degree-3-critical graphs. Its disproof shows
  the interval approach cannot be rescued by "minimality under edge count"
  alone: even in the tight $2n-2$-edge regime, a specific short length (23)
  can be missing.
- The 1-3-tree ↔ cycle correspondence (Lemma 2.1) is the *prescribed-length*
  machinery this run needs: it converts "missing a cycle of length $L$" into
  "missing a leaf-to-leaf path of a certain length", a purely tree question
  about 1-3 trees, which was solved exactly by the $2m$-avoiding sequences.
  Powers of two among even lengths: the correspondence shows cycles of length
  $2^k$ in $G(T)$ come from leaf-to-leaf paths of length $2^k - 2$ (odd power,
  even length) or from two disjoint paths summing to $2^k - 4$. So a
  power-of-two-free degree-3-critical graph $G(T)$ corresponds to a 1-3 tree
  avoiding specific leaf-to-leaf lengths — a concrete construction target for
  any EG-counterexample attempt built from trees.
- The forward-degree ordering (Lemma 4.3: $3, 2, \dots, 2, 1$) is a candidate
  tool for the run's own structural argument: if a minimal EG counterexample
  admits such a peeling order, then cycle-length questions reduce to studying
  the forward neighborhoods, exactly as NPS do for the 6-cycle.

## Caveats

- NPS's degree-3-critical is *induced* proper subgraphs AND fixes $2n-2$
  edges; a minimal EG counterexample is **not** known to have $2n-2$ edges
  (its degree distribution is 3 and ≥4 mix, so $|E| \ge \tfrac32 n$, not $2n$).
  The non-induced characterization (Theorem 4.1, wheels + $H_i H_j$ gluings)
  does not directly apply to a minimal counterexample, but its *methods*
  (peeling order, forward degrees, absence of two adjacent degree-≥4 vertices)
  are the same style as Carr's independent-set result.
- A minimal EG counterexample with no power-of-two cycle has no cycle of
  length 4 or 8 or 16 etc.; NPS show a *single* odd length (23) can be
  missing in infinitely many degree-3-critical graphs, and all even lengths
  $4, \dots, 2C(n)$ are open (Problem 6.1). So the run's target — missing an
  *infinite sparse set* of lengths — is strictly harder than NPS's single
  missing length, and Problem 6.1 says even the finite-even-initial-segment
  version is open.

```claim
id: EG-NPS-degree3critical-no-23
statement: There exists an infinite family of degree-3-critical graphs (n vertices, 2n−2 edges, no proper induced subgraph with minimum degree 3) containing no cycle of length 23; hence cycles 3,4,5,…,C(n) for C(n)→∞ are NOT forced in this class (disproof of EFGS 1988 Conjecture 1.1).
hypotheses: degree-3-critical = n vertices, exactly 2n−2 edges, no proper induced δ≥3 subgraph
holds-here: partial — a minimal EG counterexample satisfies only the "no proper subgraph with δ≥3" part (Carr Lemma 0.1), with no control on edge count; so the class is a relaxation of the EG-minimal-counterexample hypothesis, not a match
status: proved
bearing: shows interval-of-short-cycle-length statements fail for the edge-minimal δ≥3 class; the prescribed-length difficulty (missing a specific sparse length) is real even at 2n−2 edges.
anchor: research/summaries/narins-pokrovskiy-szabo-degree3-critical.md
```

```claim
id: EG-NPS-tree-cycle-correspondence
statement: For an even 1-3 tree T, the graph G(T) (add two adjacent vertices x,y each adjacent to all leaves of T) is degree-3-critical, and its cycles are exactly: lengths 2k+1 from leaf-to-leaf paths of length 2k−2 in T, and lengths 2k from either two vertex-disjoint leaf-to-leaf paths of total length 2k−4 or one leaf-to-leaf path of length 2k−2. Consequently a 2-power-free degree-3-critical G(T) exists iff a 1-3 tree avoids the corresponding leaf-to-leaf lengths.
hypotheses: T an even 1-3 tree (all degrees 1 or 3, leaves in one bipartition class)
holds-here: yes as a construction tool — this is the concrete prescribed-length machinery: converting a missing cycle length into a missing tree-path length
status: proved
bearing: any tree-based construction of an EG near-counterexample must first solve the leaf-to-leaf path-avoidance question; NPS solved it for length 20 (single length), the run's target is avoiding a whole power-of-two family, strictly harder
anchor: research/summaries/narins-pokrovskiy-szabo-degree3-critical.md
```

```claim
id: EG-NPS-pancyclic-noninduced
statement: Every n-vertex graph with 2n−2 edges and no proper (not necessarily induced) subgraph with minimum degree 3 is pancyclic (cycles of all lengths 3..n); the class consists exactly of wheels and gluings of two H_i, H_j graphs at their connectors.
hypotheses: 2n−2 edges, no proper NON-induced δ≥3 subgraph
holds-here: no — a minimal EG counterexample does not satisfy 2n−2 edges nor the non-induced condition (deleting an edge between two degree-4 vertices can create a δ≥3 subgraph)
status: proved
bearing: a warning: strengthening "proper" to non-induced reverses the picture completely (pancyclic!), so the induced/non-induced distinction is load-bearing in this corner
anchor: research/summaries/narins-pokrovskiy-szabo-degree3-critical.md
```

```claim
id: EG-NPS-forward-degree-order
statement: Every degree-3-critical graph has a vertex ordering x1,…,xn with forward degrees 3,2,2,…,2,1, and d(xn)≥4 for n≥7 (NPS Lemma 4.3, after EFGS 1988).
hypotheses: G degree-3-critical
holds-here: unknown — a minimal EG counterexample is not known to have 2n−2 edges, so the lemma's proof (which uses the edge count) does not transfer; the run's near-class counterpart would need a new argument
status: proved (for the stated class)
bearing: the peeling-order method is how NPS prove the 6-cycle; the run's own structural attack should look for an analogous peeling order under δ≥3 + no-power-of-two, a genuinely open question
anchor: research/summaries/narins-pokrovskiy-szabo-degree3-critical.md
```