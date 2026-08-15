# Laman–Henneberg theorem for generically rigid plane graphs

**Subject:** The complete construction grammar for generically rigid (minimally
rigid) frameworks in the plane — the technique-tier foundation of the adopted
`rigidity-matroid-henneberg-construction` approach
(`research/approaches/rigidity-matroid-henneberg-construction.md`).

## Source (exact statements retrieved server-side; full text not held)

Primary statements verified against **three independent authoritative
treatments** (all retrieved via the server-side search/retrieval layer; direct
download to this workspace is blocked at the network boundary):

- **C. S. Borcea, I. Streinu,** "The Number of Embeddings of Minimally Rigid
  Graphs", Discrete Comput. Geom. 31 (2004) 287–303;
  https://doi.org/10.1007/s00454-003-2902-0 (and arXiv:math/0207126).
- **J. Capco, M. Gallet, G. Grasegger, C. Koutschan, N. Lubbes, J. Schicho,**
  "The Number of Realizations of a Laman Graph", SIAM J. Appl. Algebra Geom.
  2 (2018); https://doi.org/10.1137/17m1118312.
- **J. C. Owen, S. C. Power,** "The non-solvability by radicals of generic
  3-connected planar Laman graphs", Trans. AMS 359 (2007);
  https://doi.org/10.1090/s0002-9947-06-04049-9 (and arXiv:math/0503717).
- Ancillary: **A. Nixon, J. Owen,** "An Inductive Construction of (2,1)-tight
  Graphs", arXiv:1103.2967 — which states the classical result as
  "[Henneberg [10], Lovász and Yemini [13], Recski [20]]".

## What the sources establish (exact statements)

**Def. (Laman / (2,3)-tight graph).** A finite simple graph G = (V, E) is
(2,3)-tight iff `|E| = 2|V| − 3` and every nonempty subset X ⊆ V spans at most
`2|X| − 3` edges. (Laman's count; the (2,3)-sparsity count.)

**Theorem A (Laman, 1970; and the classical Pollaczek–Geiringer 1927 result
for the generic direction).** A graph G is *generically rigid* in the plane iff
G is Laman / (2,3)-tight.

**Theorem B (Henneberg 1911, H1/H2 moves; Laman's constructive form).** Every
generically rigid (Laman) plane graph is built from a single edge K2 by
iterating exactly two moves:
- **H1** (vertex addition): add a new vertex t joined to two existing vertices
  u, v.
- **H2** (edge splitting / 1-extension): given three existing vertices u, v, w
  with edge {u,v} present, remove {u,v} and add a new vertex t joined to u, v,
  w (three new edges).
Conversely, any graph obtained from K2 by H1/H2 moves is generically rigid.
(Borcea–Streinu Theorem; Capco et al. §; Nixon–Owen Theorem 1.2.)

**Theorem C (number of realizations / algebraicity).** A Laman graph has
finitely many realizations up to rigid motions for a general (generic) choice
of edge lengths. Realizable **Henneberg-I** (H1-only) graphs have at most
`2n − 2` realizations, and there exist edge-length choices attaining exactly
`2n − 2` (Borcea–Streinu). Realizations of **generic** Laman graphs are in
general **not solvable by radicals**: for a generic 3-connected planar Laman
graph with a normalized unit base edge and rational placements of that base
edge, not all coordinates lie in a radical extension of the distance field
(Owen–Power, Theorem 1.1 — proving a conjecture of Owen 1991).

## Bearing on this problem

These are the exact statements the adopted Henneberg construction approach
rests on, and they *sharpen* rather than support the original framing:

1. **Completeness is generic, not all-unit.** Laman–Henneberg generates every
   *generically* rigid framework (arbitrary edge lengths). A unit-distance
   graph is the non-generic case where **all** edges carry the same length 1;
   there is no theorem that every all-unit Laman graph is reachable by
   unit-preserving H1/H2 moves. The approach note already records this as
   caveat (1).
2. **Field growth is real.** Theorem C: realizations of generic Laman graphs
   need not be solvable by radicals, so successive H1/H2 steps do **not** stay
   in a tame quadratic field (caveat: H1-only graphs are constructible by
   ruler-and-compass, so type-1 safe; H2 is not). This is exactly the exact-
   arithmetic discipline in GOAL.md — the coordinate field grows, and the
   approach must account for which rungs stay quadratic.
3. The *useful* residue (which the approach note adopts) is that **H1 is a
   free, exact, quadratic move** (intersection of two unit circles), and
   **H2 is a circumradius-1 coincidence** to be sought and certified. Each tree
   node is a certified unit-distance graph fed to the forced-pair SAT harness.

## Sourced claim

```claim
id: laman-henneberg-generic-rigidity
statement: >
  A finite simple graph is generically rigid in the plane iff it is (2,3)-tight:
  |E| = 2|V|-3 with every nonempty X ⊆ V spanning ≤ 2|X|-3 edges (Laman). Every
  such graph is built from K2 by H1 (add a vertex joined to two existing) and H2
  (remove edge uv, add a vertex joined to u,v,w) moves, and these moves preserve
  generic rigidity (Henneberg–Laman). The generic (2,3)-tight count is
  |E| = 2|V|-3; a unit-distance graph is the non-generic all-edge-length-1 case.
hypotheses: finite simple graphs; generic rigidity in the plane; (2,3)-sparsity.
holds-here: yes as a construction grammar for rigid frameworks; BUT the all-unit
  case is NOT covered by the completeness theorem (generic, not all-unit).
status: asserted (verified against three independent authoritative statements
  retrieved server-side; not machine-checked here). One concrete consequence —
  the H1 move is an exact intersection of two unit circles — is independently
  verified in this run's sharp_nbhd_cert and forced-pair machinery.
bearing: the exact construction grammar behind the adopted
  rigidity-matroid-henneberg approach; fixes that H1 is the free quadratic move
  and H2 is a circumradius-1 coincidence; Theorem C bounds the coordinate-field
  growth (non-solvability by radicals for generic Laman graphs).
anchor: research/sources/laman-henneberg-generic-rigidity-theorem.md
falsifies: a unit-distance-specific completeness theorem for all-unit Laman
  graphs would change the method (none is claimed by these sources); a H1 move
  whose two unit-circle intersections are not exact quadratic would break the
  exact-arithmetic discipline.
```

## What could not be obtained

The full verbatim publisher texts (Borcea–Streinu DOI, the SIAM Capco et al.,
the Trans-AMS Owen–Power) are blocked at the network boundary. The exact theorem
statements above were retrieved server-side and are cross-confirmed by the three
treatments; the (2,3)-sparsity count itself is elementary and reproduced in this
run's own verified constructions. Recorded so nobody re-attempts those hosts.
