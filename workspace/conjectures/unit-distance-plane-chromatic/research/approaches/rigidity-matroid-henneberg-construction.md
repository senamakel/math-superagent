# Approach: rigidity matroid + Henneberg moves as the geometric construction grammar

```approach
idea: Use combinatorial rigidity as the *complete, geometry-native construction
  grammar* for unit-distance graphs. Laman's theorem (1970) characterises generic
  rigidity in the plane by (2,3)-sparsity (|E|=2|V|-3 and every subgraph has at
  most 2|V'|-3 edges), and Henneberg's theorem (1911) says every such graph is
  built from a single edge by two moves: H1 — add a vertex adjacent to two
  existing vertices; H2 — split an edge uv, adding a vertex adjacent to u, v, and
  a third vertex z already adjacent to both u and v. In the unit-distance setting
  H1 places the new vertex at an intersection of the two unit circles centred at
  the chosen pair (an exact quadratic over the coordinate field, so the two new
  edges are unit *by construction*), and H2 places it at the exact common point of
  three unit circles (the rigid coincidence the problem says must be accumulated).
  The search becomes a walk over a finitely-branching construction tree, every
  node a certified unit-distance graph, covering all rigid frameworks.
mechanism: The run's named obstruction is "rigidity-deficit" — the obstruction to
  chi>=5 must be accumulated rigidity, and the adopted Minkowski-sum/spindling
  engine is one particular rigidity source that has so far stayed 4-colourable.
  The rigidity matroid is exactly the machine for accumulating rigidity, and
  Henneberg moves are its *complete* grammar: every generically rigid framework
  has an H1/H2 construction, so the search provably covers the whole class rather
  than a subfamily. This is the geometry-native analogue of the Hajos grammar the
  run already closed — and it fixes precisely the defect that killed Hajos:
  Henneberg moves preserve unit-distance realizability by design (they are
  geometric moves, placing vertices at circle intersections), whereas the Hajos
  join/merge is an abstract graph operation that does not keep graphs unit-distance.
  Each move is a finite exact-arithmetic choice (which vertices, which intersection
  branch), so no floating point and no spurious edges ever enter; the SAT oracle
  tests chi at each node, and the forced-pair harness tests the failed crux
  (a monochromatic-forced pair) on genuinely richer, more rigid base graphs.
status: adopted
first-step: Implement `code/lib/henneberg.py`: (1) `H1(points, u, v)` solving
  |w-u|^2 = |w-v|^2 = 1 exactly over the current coordinate field, returning both
  intersection roots and the extended point set with edges certified by
  `unit_graph`; (2) `circumradius_1(points, u, v, z)` computing the exact
  circumradius of u,v,z and returning the centre when it equals 1 (the H2
  coincidence); (3) a bounded H1-tree walk whose every node goes through
  `code/forced_pair.py` — a pair (u,v) with H+uv non-4-colourable in the complete
  SAT test is a critical edge and triggers an H2 coincidence closure.
falsifies: an H1/H2 step whose intersection point lies outside the field the run
  tracks (the coordinate field grows at each move), which caps the tree in a
  precise, reportable way; or the tree yields only 4-colourable graphs up to the
  feasible depth, a precise negative result about how much rigidity Henneberg
  accumulation can buy before the SAT oracle bounds the search.
precedent:
  - Pollaczek-Geiringer 1927 / Laman 1970, "On graphs and rigidity of plane
    skeletal structures", J. Eng. Math. 4:331–340 — generic rigidity in the plane
    <=> Laman (2,3)-sparsity (|E|=2|V|-3, every subgraph (2,3)-sparse).
  - Henneberg 1911, "Die graphische Statik der starren Systeme" — every Laman
    (generically rigid) graph is built from an edge by H1 (add vertex on two) and
    H2 (add vertex on three with one edge removed); the modulo-rigid-motions
    completeness statement is the Laman–Henneberg theorem.
  - Capco–Gallet–Grasegger–Koutschan–Lubbes–Schicho, "The number of realizations
    of a Laman graph", https://doi.org/10.1137/17m1118312 — CONFIRMS:
    (a) Laman graph <=> generically rigid; (b) <=> built from a single edge by
    H1/H2 moves.
  - Owen–Power, "The non-solvability by radicals of generic 3-connected planar
    Laman graphs", https://doi.org/10.1090/s0002-9947-06-04049-9 — realizations of
    generic Laman graphs are NOT solvable by radicals: the field grows far beyond
    quadratic/square-root at each H-move, so the candidate's "exact quadratic over
    the current field" H1/H2 claim FAILS for the generic (non-unit) case.
  - "On Galois groups of type-1 minimally rigid graphs", Discrete Comput. Geom.
    (2025) https://doi.org/10.1007/s00454-024-00711-4 — type-1 (H1-only) graphs
    have solvable (2-group) Galois groups, constructible by ruler-compass; type-2
    (with H2) graphs do not in general.
caveat:
  Two premises of the candidate are overclaimed, independently of the theorem being
  true:
  (1) HENNEBERG COMPLETENESS IS A GENERIC-RIGIDITY THEOREM, NOT A UNIT-ALL-EDGES
      THEOREM. Laman–Henneberg generates every *generically rigid* framework — a
      framework whose edges can be given arbitrary (algebraically independent)
      lengths preserving rigidity. A unit-distance graph is the very special case
      where ALL edges carry the SAME length 1, i.e. a *non-generic* edge-length
      labelling. There is NO theorem that every all-unit edge length Laman graph is
      reachable by unit-preserving H1/H2 moves, or that every H1/H2 unit-construction
      stays all-unit. The "realizability is built in" claim holds for a generic
      length assignment, not for the all-equal-unit assignment the problem needs.
      (The equilateral-triangle/lattice examples in the library are exactly
      non-generic all-unit rigid frameworks.)
  (2) H2 IS NOT A FREE MOVE — IT IS A CONGRUENCE COINCIDENCE. H2 adds a vertex w at
      distance 1 from THREE prescribed vertices u, v, z. A point at distance 1 from
      all three exists iff u, v, z are concyclic with circumradius EXACTLY 1 (w is
      then the centre). This is a strong non-generic coincidence: three unit circles
      centred at arbitrary u,v,z almost never share a point. So H2 is itself a
      realizability query — it does not eliminate the realizability oracle, it
      relocates it into a "do these three vertices admit a common unit neighbour"
      coincidence check. The generic H2 move (add vertex on 3 vertices and remove
      an edge, with no length constraint) is free; the *all-unit* H2 (the new vertex
      at distance 1 from all three) is not.
```

## Research verdict — GROUNDED theorem, but TWO of its three advertised advantages are false

**The theorem is real and sourced.** Pollaczek-Geiringer/Laman and Henneberg,
confirmed by three independent modern treatments (Capco et al.; Owen–Power; the
2025 Discrete-Comput.-Geom. Galois paper), state precisely:

> **Laman–Henneberg theorem.** A graph G is *generically rigid* in the plane iff
> it is Laman: |E| = 2|V|-3 and every subgraph H has |E(H)| <= 2|V(H)|-3. Equivalently,
> G is obtained from a single edge by repeatedly applying H1 (add a vertex adjacent
> to exactly two existing vertices) and H2 (add a vertex adjacent to three existing
> vertices and delete one of the edges among them).

This is the **complete construction grammar for generically rigid frameworks** — a
real theorem, and the natural contrast to the refuted Hajos grammar (which is
abstract and not UDP-preserving). So the *framing* is right: this is the geometry-
native complete grammar.

### Where the candidate overclaims

**Overclaim 1 — "no realizability oracle is needed."** Henneberg completeness is a
*generic* rigidity statement. Laman graphs model frameworks that are rigid for a
*general choice of edge lengths*. The unit-distance problem is the *non-generic*
case where every edge has the same length 1. There is no proved completeness
statement for unit-all-equal realisations, and (worse) the generic realization of a
Laman graph is typically NOT solvable by radicals (Owen–Power), so successive H1/H2
steps do not stay in a tame coordinate field — they force exactly the algebraic-
degree explosions the exact-arithmetic discipline worries about. H1-only (type-1)
graphs are constructible by ruler-and-compass (solvable 2-groups, per the 2025
Galois paper), so H1-only constructions are safe; H2 steps are not.

**Overclaim 2 — "H2 is a free unit move."** H2 places the new vertex at a common
point of three unit circles centred at u, v, z. Such a point exists iff u, v, z are
concyclic with circumradius exactly 1 (the new vertex is the centre). For a
*generic* triple this fails; it is a coincidence the problem says must be
*accumulated*. So the all-unit H2 is itself a realizability/coincidence query — it
does not remove the oracle, it moves it into "do these three exist with a common
unit neighbour." (My analytic check: two unit circles always co-intersect in up to
two points — that is H1, genuinely free; three unit circles co-intersect only in
the measure-zero circumradius-1 coincidence — that is H2, non-generic.)

### What the approach genuinely buys

- A **complete, decidable, exact-arithmetic construction grammar for rigid
  frameworks**, distinct from the Minkowski-sum/spindling engine. The H1 move is a
  genuine free move (two-unit-circle intersection — always exactly quadratic).
- It is a **machine-checkable generator** of "richer base graphs" for the
  forced-pair harness: every node is a certified unit-distance graph, so the run
  can feed the forced-pair SAT test genuinely more rigid structures than Moser and
  Moser+Moser.
- The forced-pair crux (`G-forced-pair-exists`) could be supplied by a Henneberg-
  built graph; this is the concrete payoff and the first-step tests it at the n=12
  rung.

### Verdict

`status: grounded` — but the two load-bearing premises of the framing are false
(no-oracle-needed, and H2-free), and must be corrected to "H1 is the free move;
H2 is a coincidence/resolvability query; completeness is generic-only, not all-
unit." Refited precisely: the value is H1-only construction (safe, exact, free)
plus H2 as a deliberately sought rigidity coincidence, each node machine-certified
and fed to the forced-pair harness — NOT a claim that Henneberg covers the all-unit
class or removes the realizability oracle. Recorded as `caveat`, because the
*method* (walk the exact H1/H2 tree, certify every node, test forced pairs) is
viable and valuable even with the overclaims corrected.

## Why this is not a restatement of a closed idea

- Not the Hajos grammar (refuted: join/Hajos not UDP-preserving; realizability is
  ER-complete): Henneberg moves ARE geometric and DO preserve unit-distance
  realizability where they are freely executable (H1; H2 in the coincidence case) —
  no abstract realizability oracle, no ER-completeness.
- Not the Minkowski-sum engine (live thread): that is one rigidity source; Henneberg
  is the complete grammar for *rigid* frameworks, a structurally guaranteed
  superset.
- Not the P^1(K) line (refuted as a coordinate relabelling): Henneberg is a
  construction operation with a completeness theorem, not a reparametrisation.

## Decision (convergence pass) — ADOPTED

Adopted over the other two candidates because it is the only line that attacks the
run's *named obstruction* — the forced-pair crux `G-forced-pair-exists` needs a
richer 4-chromatic base graph — with a concrete, exact, machine-verifiable engine,
and its first step starts today on code the run already owns
(`code/lib/unitfield.py` exact field arithmetic, `code/forced_pair.py` complete
SAT forced-pair harness, `code/lib/unitgraph.py` edge certifier).

The research pass corrected two overclaims without killing the method:
- Henneberg completeness is generic-length, not all-unit; and
- H2 (three unit circles) is a circumradius-1 coincidence, not a free move.
These *sharpen* the method: H1 is the free move (two unit circles, always an exact
quadratic intersection, tame field), H2 is the rigidity coincidence to seek and
certify. The criticality synthesis is the targeting rule that makes the search
principled: H1-only graphs are planar, hence 4-colourable (four-colour theorem),
so a forced pair (u,v) — detected exactly when H+uv is non-4-colourable in the
complete SAT test — is a critical edge of a prospective 5-critical graph, and the
first H2 coincidence that realizes such a pair is the 5th-colour closure.

Final first-step (tool_builder-ready): implement `henneberg.py` with
(1) `H1(points, u, v)` solving |w-u|^2 = |w-v|^2 = 1 exactly over
Q(sqrt3, sqrt11, ...), returning both intersection roots and the extended point
set, edges certified by `unit_graph`; (2) `circumradius_1(points, u, v, z)`
computing the exact circumradius of u,v,z and returning the centre when it equals
1 (the H2 coincidence); (3) a bounded H1-tree walk to ~12 vertices whose every
node goes through `forced_pair.py` — a pair returning UNSAT on H+uv is the
critical edge, and is the trigger for an H2 coincidence closure.
