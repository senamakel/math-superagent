# Kruskal–Katona on the degree-ceiling complex: bound |S| from the max internal degree

```approach
idea: Invert the problem. Instead of lower-bounding D(S) for a fixed size
|S| = 2^{n-1}+1, upper-bound the size of any set S ⊆ Q_n with D(S) ≤ d. Write
g_d(n) = max { |S| : S ⊆ Q_n, D(S) ≤ d }. Then f(n) > d  ⇔  g_d(n) < 2^{n-1}+1,
so a sharp upper bound on g_d(n) is exactly a lower bound on f(n). Attack g_d(n)
with the Kruskal–Katona shadow theorem and the machinery of vertex-decomposable
simplicial complexes on the hypercube, via compression (shifting).

mechanism: A set S with D(S) ≤ d is a "d-independent" subset of Q_n (induced
subgraph of max degree ≤ d). The key move is to pass from the vertex set S to a
simplicial complex whose f-vector controls |S| through the degree ceiling d. Two
concrete encodings, both making the degree ceiling a *face* constraint rather
than an average:

  (1) Down-closure encoding. For a vertex v ∈ S let B(v) = {coordinates on which
      the neighbours of v lie in S} ⊆ [n]; then deg_S(v) = |B(v)| ≤ d. The family
      { B(v) : v ∈ S } is a family of subsets of [n] of size ≤ d, and the shadow
      of each B(v) (all its subsets) corresponds to the vertices reachable from v
      by flipping coordinates that keep the walk inside S. Kruskal–Katona then
      bounds how large S can be: a family all of whose members have shadow of
      size ≤ d cannot have more than g_d(n) members.

  (2) Compression invariance. The shift (coordinate compression) on {0,1}^n is
      known to not increase the maximum internal degree (the induced-subgraph
      degree is monotone under shifting), so an extremal S for g_d(n) can be
      taken down-closed in the product order. Down-closed S ⊆ {0,1}^n is exactly
      an order ideal of the Boolean lattice, whose face numbers are controlled by
      the Kruskal–Katona/LYM bounds with the *maximal* elements (the "roof") each
      contributing ≤ d shadow edges inside S.

The quantity this produces is a maximum by construction: the degree ceiling d is
baked in as a per-vertex face bound, and KK gives a bound on the *cardinality*
of the whole family — inverting a size bound to a degree bound. This is the
opposite side of the ledger's existing `induced-subgraphs-hypercube-full-vertices-kk`
claim (which maximises the number of *full* vertices via KK); here KK is run on
the *bounded-degree* (d-independent) complex instead, targeting the exact
inverse function g_d(n) of f(n).

covers: reproduces the d=0 line (g_0(n) = 2^{n-1}, the parity classes, by the
LYM/sphere-packing bound on order ideals with empty internal shadow) and the
exact small values f(1..5) = 1,2,2,2,3 by computing g_d(n) for n ≤ 5. Scholze's
rule holds for the d=0 line; the new content is the d ≥ 1 regime, which the
closed spectral route only bounds from below (√n) without pinning.

status: refuted
killed-by: two independent failures. (1) The load-bearing compression claim —
"an extremal S for g_d(n) can be taken down-closed in the product order" — is
FALSE. The d=0 extremal sets g_0(n) = 2^{n-1} are the two parity classes
(verified in this run), which are NOT order ideals; at n=2 the only
down-closed order ideals of size 2 are {00,01} and {00,10}, both with D=1, so no
down-closed independent (D=0) order ideal of size 2 exists. Compression to
down-closed sets therefore destroys the degree ceiling on the very d=0 line the
proposal claims to reproduce. (2) Even if compression worked, the KK-shadow
bound's natural output is the volume of the d-skeleton, sum_{i<d} C(n,i), which
already exceeds 2^{n-1} only for d ~ n/2, i.e. far above the true f(n) = Theta(sqrt n).
Inverting a bound of that scale could never certify f(n) >= sqrt(n); it points to
the wrong order of magnitude (linear, not sqrt), so the route caps far above the
truth and cannot be sharp. The KK shadow technique itself is genuine and stays in
the library (`induced-subgraphs-hypercube-full-vertices-kk`) but only at the
high-degree/full-vertex end of Q_k[S], not the 2^{n-1}+1 low-degree end this
proposal targets.
precedent:
  - induced-subgraphs-hypercube-full-vertices-kk (KK shadow counts HIGH-degree
    vertices; wrong end) — https://www.sciencedirect.com/science/article/pii/S0195669812001680
  - kruskal-katona-shadow-formula (KK vertex-decomposability) — library source
  - Large-indiced-subgraphs-of-bounded-degree literature bounds OTHER classes
    (Alon-Krivelevich-Sudakov nearly-regular https://doi.org/10.48550/arxiv.0710.2106;
    D'Elia-Frati outerplanar/planar https://doi.org/10.48550/arxiv.2412.14784) —
    none address Q_n at |S|=2^{n-1}+1.
  - No source found applying KK-shadow to the max-internal-degree quantity g_d(n).

first-step: (repositioned — only as an instrument) Use the existing ILP oracle
  (code/lib/fmax.py) to
  compute g_d(n) = max feasible |S| with D(S) ≤ d for n = 1..6, d = 0..n, and
  record g_d(n) against the KK/LYM upper bounds. The inversion check is
  f(n) = min{ d : g_d(n) ≥ 2^{n-1}+1 }; confirm it reproduces f(1..5)=1,2,2,2,3.
  Then test the compression claim directly: for n = 4,5 compute whether shifting
  an extremal S preserves D(S) and whether some extremal S is down-closed. If
  g_d(n) matches the KK shadow bound at small n, the route is grounded and the
  next move is an induction on n splitting Q_n into two Q_{n-1} copies, applying
  KK to the cross-edges.
```
