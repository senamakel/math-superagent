# Bruhn, Charbit, Schaudt, Telle, "The graph formulation of the union-closed sets conjecture" (EJC 2015; arXiv:1212.4175)

**Full text:** [[bruhn-charbit-schaudt-telle-graph-formulation-2015.full]]

Gives an equivalent graph formulation: UC ⟺ every finite graph with an edge has two adjacent vertices each in at most half the maximal stable (=independent dominating) sets.

```claim
id: graph-formulation
statement: Frankl's union-closed conjecture is equivalent to: every finite graph G with at least one edge has two adjacent vertices each belonging to at most half of the maximal stable sets of G.
hypotheses: finite graphs with ≥1 edge
holds-here: yes (the union-closed family is the maximal stable sets of a suitable graph)
status: proved
bearing: gives the admission-rejection "graph" reformulation; the conjecture being open only for bipartite graphs (see below).
anchor: research/sources/bruhn-charbit-schaudt-telle-graph-formulation-2015.full.md
```

```claim
id: graph-bipartite-equivalent
statement: The graph formulation is equivalent to: every finite bipartite graph with an edge has, in each bipartition class, a vertex in at most half the maximal stable sets. The conjecture is trivial for non-bipartite graphs.
hypotheses: finite bipartite graphs with ≥1 edge
holds-here: yes
status: proved
bearing: the bipartite case is the heart; the family of maximal stable sets of a bipartite graph is an intersection-closed family — this is where the conjecture "reduces to bipartite graphs."
anchor: research/sources/bruhn-charbit-schaudt-telle-graph-formulation-2015.full.md
follows-from: graph-formulation
```

```claim
id: graph-settled-classes
statement: The graph formulation holds for chordal bipartite, subcubic bipartite, bipartite series-parallel, and bipartitioned circular interval graphs.
hypotheses: the listed graph classes
holds-here: yes
status: proved
anchor: research/sources/bruhn-charbit-schaudt-telle-graph-formulation-2015.full.md
```

**Bearing:** the graph formulation is one of the two reformulations in problem.md worth having sourced (with lattice). The bipartite graph case being open and equivalent to UC means a structural theorem about maximal independent sets of bipartite graphs is the same prize as UC.

**Does not settle:** general bipartite graphs; the run could target the subcubic/planar case but those are already settled here.
