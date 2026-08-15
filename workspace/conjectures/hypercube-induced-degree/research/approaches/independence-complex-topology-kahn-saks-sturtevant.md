# Topological route: independence-complex connectivity and Kahn–Saks–Sturtevant

```approach
idea: Read D(S) through the topology of the independence complex. For S ⊆ Q_n,
let I(Q_n[S]) be the simplicial complex whose faces are the independent sets of
the induced subgraph Q_n[S]. A vertex v ∈ S has internal degree deg_S(v), and
the link of v in I(Q_n[S]) sits on exactly deg_S(v) vertices — so the maximum
internal degree D(S) is the largest possible vertex count in any link. Bound
D(S) from below by the connectivity (homology vanishing) of I(Q_n[S]), via
Meshulam's homological domination theorem and the Kahn–Saks–Sturtevant
(KSS) theory of topological obstructions on products of graphs.

mechanism: This is the same topological world that powers the Boolean-function
complexity side of the problem (the ledger's "Connections to Boolean function
complexity" lead): sensitivity of a Boolean function is a max internal degree of
a subcube, and decision-tree/homological lower bounds on sensitivity go through
the independence (or box) complex. Two named machines are available:

  (1) Meshulam's domination theorem: a simplicial complex on N vertices whose
      links are all (k−1)-acyclic has non-vanishing cohomology in a controlled
      dimension; inverted, if a complex on a known number of vertices is forced
      to be (r)-connected by the structure of Q_n, then some link — hence some
      vertex of S — must sit on many vertices, i.e. have large internal degree.

  (2) Kahn–Saks–Sturtevant / Lovász: the box complex B(G) and its Z_2-index give
      lower bounds on the chromatic number and on decision-tree complexity of a
      graph/product. Q_n = K_2^□n is a topological join/threshold structure;
      its Z_2-index is n. The hope (speculative) is that a set S of size
      2^{n-1}+1 forces the induced subgraph Q_n[S] to have box-complex index
      growing like √n, and the KSS bound converts index into a vertex of large
      internal degree.

The quantity produced is a maximum by construction, not an average: homology
vanishing and Z_2-index are integer homotopy invariants, and Meshulam/KSS
convert them into a statement that *some specific vertex* has a large link.

covers: re-derives the d=0 line (S independent ⇔ I(Q_n[S]) is the full simplex
on S, contractible, index 0, so topology sees nothing and g_0(n)=2^{n-1} is
compatible) and is orthogonal to the spectral route — it would give an
*independent second proof* of a √n-type lower bound, which GOAL.md asks for
("a result needs a second, different route"). It is a genuinely different world
(topology/equivariant obstruction theory) from the closed Clifford/Delsarte/
entropy lines and from the adopted Dirac-frame line.

status: refuted
killed-by: the load-bearing incidence claim is FALSE and inverted. The link of v
in I(Q_n[S]) sits on the NON-neighbors of v — a face {v}∪σ where σ is an
independent set of the induced subgraph on S \ (N(v)∪{v}) — so its vertex count
is |S| − 1 − deg_S(v), NOT deg_S(v). Checked at n=2, S={00,11} (parity, deg=0):
link(00) sits on 1 vertex (= |S|−1−0 = 1 = the non-neighbour 11), while
deg_S(v)=0. Hence a LARGE internal degree corresponds to a SMALL link, exactly
inverting the proposed direction "D(S) is the largest possible link size". The
incidence deg = #neighbours is carried by the complement of the link vertex set,
not by the link itself, so Meshulam-style connectivity of the complex forces
nothing about the largest link. The named machinery is real but is a chromatic/
graph-colouring tool: (a) Meshulam's domination-homology theorem (Meshulam 2003,
"Domination numbers and homology", JCTA 102) ties vanishing of reduced homology
of I(G) to domination numbers of G — nothing here forces a high internal degree;
(b) Kahn-Saks-Sturtevant type Z2-index / box-complex bounds (Lovasz 1978; Babson-
Kozlov proof of Lovasz conjecture, Annals 165; Matousek-Ziegler) lower-bound the
CHROMATIC number χ(G), and χ(Q_n[S]) = 2 for every S since the cube is bipartite,
so the bound is vacuous (2 ≥ χ = 2, no force). No published source applies
independence-complex homology to a max-internal-degree quantity; the topology
regime (square/link incidence through vertex deletion, not link size) points
away, not toward, a sqrt bound.
precedent:
  - Meshulam, "Domination numbers and homology", J. Combin. Theory Ser. A 102
    (2003) 321-330 — https://www.sciencedirect.com/science/article/pii/S0097316503000451
  - Adamaszek-Barmak connectivity of independence complex (Discrete Math 2011) —
    https://doi.org/10.1016/j.disc.2011.06.010
  - Babson-Kozlov, "Proof of the Lovasz conjecture", Annals of Math 165 (2007) —
    https://doi.org/10.4007/annals.2007.165.965
  - Matousek-Ziegler, "Topological lower bounds for the chromatic number: a
    hierarchy", arXiv math/0208072 — https://arxiv.org/abs/math/0208072
  - Domination numbers and homology overview (Chordal/fractional star-domination)
    — https://www.sciencedirect.com/science/article/pii/S0097316512001628
  - All bound χ(G) (bipartite → vacuous here) or independence-complex homology;
    none bound max internal degree D(S).

first-step: (positioned as an obstruction-recording instrument, not a sqrt route)
  For n = 1..4 compute, for every admissible S, the actual smallest-link vertex
  count (= |S|−1−D(S)) of I(Q_n[S]) and confirm it tracks the inverse of D(S),
  then state precisely what the homology of I(Q_n[S]) can and cannot force about
  D(S). If no homology invariant forces D(S) ≥ √n at these sizes (expected, since
  the complex is far from dominating-condition regimes and the chromatic via
  bipartiteness is vacuous), that is itself the precise "topology cannot see √n"
  obstruction to record.
```
