# Kruskal-Katona theorem and extremal simplicial complexes

Sources:
- J. B. Kruskal, "The number of simplices in a complex" (1963);
  G. O. H. Katona, "A theorem of finite sets" (1968).
- Statement source used here: "f-Vectors Implying Vertex Decomposability",
  Discrete Comput. Geom. (2012), URL: https://link.springer.com/article/10.1007/s00454-012-9477-6
  (retrieved via read_sources).

## Statement

For a family U of k-subsets of [n], the lower shadow ΔU = { (k-1)-subsets
contained in some member of U }. Kruskal-Katona: among families of m k-sets the
shadow size is minimised by the first m sets in the squashed order, and
|ΔU| >= |ΔS_k(m)|. If m = C(a_k,k)+C(a_{k-1},k-1)+... (a_k>a_{k-1}>..., the k-th
binomial decomposition of m), then
|ΔS_k(m)| = C(a_k,k-1)+C(a_{k-1},k-2)+...

The 2012 paper proves: an extremal pure simplicial complex (achieving equality
in the Kruskal-Katona bound) is **vertex decomposable** and hence
Cohen-Macaulay over any field — a combinatorial proof of a Herzog-Hibi theorem.

## Why it is here

Kruskal-Katona is the exact extremal tool behind the "induced subgraphs of
hypercubes" counting of full vertices (a vertex is full iff all k neighbours are
in S, a shadow/upward-closed condition). It is the primary machinery for a
maximum-producing count on the cube — the kind of tool the obstruction in
problem.md says a D(S) lower bound would have to come from.

## Claim block

```claim
id: kruskal-katona-shadow-formula
statement: For a family U of m k-sets, |lower shadow| >= C(a_k,k-1)+C(a_{k-1},k-2)+...
  where the a's come from the k-binomial decomposition of m; equality (extremal
  complexes) are vertex decomposable / Cohen-Macaulay (KK; Moradi-Khosh-Ahang /
  2012 combinatorial proof).
hypotheses: U family of k-subsets of [n].
holds-here: yes — the shadow formula is the engine for counting degree-k
  (full) vertices and is a maximum-producing tool on the cube.
status: asserted-by-source.
bearing: the technical route by which a count of high-degree vertices in Q_k[S]
  is proved; relevant to any D(S) lower-bound attempt at the 2^{n-1}+1 size.
anchor: kruskal-katona; vertex-decomposability-2012
```
