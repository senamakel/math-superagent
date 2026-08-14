# de Bruijn–Erdős compactness for colouring infinite graphs

**Source:** N.G. de Bruijn, P. Erdős, "A Colour Problem for Infinite Graphs and a
Problem in the Theory of Relations", Indagationes Mathematicae (Proc.) 54 =
Indagationes Math. 13 (1951), 369–373. See also Rado's selection principle and
Tychonoff compactness formulations.

## The theorem

If an infinite graph G is such that every **finite** subgraph is k-colourable,
then G itself is k-colourable.

Equivalent contrapositive (the form used for Hadwiger–Nelson): if the chromatic
number of the infinite plane-distance graph equals chi, then there exists a
**finite** subgraph with chromatic number chi. So chi(G_plane) >= k iff there is
a finite unit-distance graph with chromatic number >= k.

## Why it applies to Hadwiger–Nelson

The plane graph G has vertices = all of R^2, edges = pairs at distance exactly 1.
Colouring G with k colours is a partial order / compactness fact: the product of
finite colour-sets is compact (Tychonoff / Rado selection), so the infinite
colouring that avoids monochromatic unit edges exists iff every finite subset
can be so coloured.

Proof uses the Boolean prime ideal theorem / a choice principle (Tychonoff for
finite spaces, or Rado's selection principle / ultrafilter). Record as a proved
input: the lower-bound problem is exactly the existence of a finite
non-(k-1)-colourable unit-distance graph.

## Reproduced statement to verify in-workspace

The 7-vertex graph in problem.md is the witness for chi >= 4: a finite
unit-distance graph that is 4-colourable and not 3-colourable. Its existence is
what the compactness theorem converts into a lower bound on the whole plane.

```claim
id: debruijn-erdos-compactness
statement: An infinite graph G is k-colourable iff every finite subgraph of G is k-colourable. Hence the chromatic number of the unit-distance graph of the plane equals the supremum of chromatic numbers of its finite subgraphs, and chi >= k is equivalent to the existence of a finite non-(k-1)-colourable unit-distance graph.
hypotheses: G an ordinary (possibly infinite) graph; k a positive integer; uses a choice principle (Rado selection / Tychonoff for finite spaces).
holds-here: true — this is the single most load-bearing structural fact of the problem; it reduces the whole infinite colouring question to finite unit-distance graphs.
status: proved (classical, 1951 de Bruijn–Erdős)
bearing: The entire lower-bound search operates on finite unit-distance graphs; nothing infinite needs reasoning about.
anchor: research/sources/debruijn-erdos-colour-problem-1951.md
```

Status: theorem stated from source; the exact original proof is not on disk
(download of the 1951 paper and its retellings was network-blocked). The
statement and its application are classical and can be independently verified by
the Tychonoff/selection argument.
