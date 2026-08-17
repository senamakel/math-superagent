# Approach: clique-complex homology of the triangle geometry

```approach
idea: Change representation from "graph + geometry" to "2-dimensional simplicial
  complex": the clique complex X of a putative srg(99,14,1,2). X has 99 vertices,
  693 edges, and 231 maximal 2-simplices (the triangles, since lambda=1 forbids
  K4). Every vertex link is a perfect matching 7K2 (c5), so X is a 2-complex
  whose vertex links are 7 disjoint edges. X has Euler characteristic
  chi = 99 - 693 + 231 = -363. The mu=2 condition is a statement about pairs of
  non-collinear points having a specific 2-flag count. Attack existence through
  the combinatorial topology / homology of X rather than through its
  adjacency spectrum.
mechanism: A 2-complex whose every vertex-link is a (disconnected) matching is a
  tightly constrained local-to-global object: it is far from a pseudomanifold
  (links are disconnected), so no surface/triangulation theorem applies, but the
  link structure forces triangle adjacencies locally. The clique complex of an
  SRG has a fully determined face data (f-vector (99,693,231) fixed by
  parameters) yet its homology is a genuinely graph-dependent invariant: the
  reduced rational homology ranks of the triangle-complex of two SRGs with the
  same parameters need not agree, so this is NOT parameter-determined in the
  sense that killed the SNF route (which was forced by the spectrum alone). The
  natural lever: relate the structure of the link at each vertex (7 edges on 14
  points) to a local homology / a "2-acyclic pasting" condition, and test
  whether any such X with the mu=2 flag-counting exists. Because 9 and 243 have
  triangulation-complexes with different face controls (rook: 6 triangles
  chi=1; BvLS: 891 triangles), an obstruction stated on the local
  matching-link geometry + mu=2 flag count is a =7/14-specific statement with a
  real chance of surviving on controls only in a harmless way.
first-step: (exact) Build the clique complex of both controls (lib.srg rook(3),
  bvls_graph()) as a simplicial complex (vertex->edges->triangles), compute its
  reduced homology over Q and Z (e.g. via the boundary maps / rank over Z in
  sympy, or a homology library), and the Euler characteristic. Record what
  homology "carries" for 9 and 243. Then enumerate all local 2-complexes on the
  matching-link constraints (a fixed vertex 0 with N(0)=7K2 and the 12-regular
  outer graph as the 1-skeleton of the second link), and ask whether the
  flag-count / boundary-operator equations can be satisfied at 99 -- this is a
  finite design/topology question, not an eigenvalue argument, and it is
  admissible only if it does NOT also fail at 9 and 243 (name that step).
status: refuted
killed-by: homology obstruction is parameter-determined (Cioaba/Neumaier s=-m
  list), no 99-vs-243 separation; null result on controls.

## Decision (inventor, converge round)

REFUTED (converge round). The change of representation is genuinely the most
divergent of the three, but it has no checkable 99-specific lever: the f-vector
(99,693,231) is fixed by parameters, and the Cioaba/Neumaier H1-verdict — the
only homology result with concrete content — is keyed to a parameter-determined
hypothesis (smallest eigenvalue −m and a list that already includes the rook
lattice-graph control), the exact shape directive 21 says is refuted on arrival.
No named obstruction separates 99 (s=−4, λ=1) from 243 (s=−5, λ=1) on the
matching-link geometry, and the honest first step (compute H1 of both controls)
returns at best a null result. Thinner precedent, weaker control-gate arithmetic,
and no a=7/14-specific consequence — the shape that closed terwilliger.

killed-by: homology obstruction is parameter-determined (Cioaba/Neumaier
  s=−m list), no 99-vs-243 separation, plausible null result on controls.
```

Notes: highly speculative -- the homology of a clique complex of an SRG is not a
classically-studied obstruction in this literature, so the precedent is thin; but
the change of representation (graph -> 2-complex with prescribed links) is
genuinely different from every closed route (none is a topological/homological
representation), and the f-vector is fixed while the homology is free, which is
exactly the shape of a non-parameter-determined invariant. The concrete deliverable
is either a homology/2-acyclicity obstruction at 99, or an honest statement that
the topology carries no obstruction (which is itself the a=7-specific negative
result the run lacks).
