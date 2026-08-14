# The AMP exact embeddability solver — L0–L3 move system

**Source:** arxiv.org/abs/2412.11914 (HTML: arxiv.org/html/2412.11914)
**Authors:** Boris V. Alexeev, Dustin G. Mixon, Hans Parshall (2024)
**Full text:** NOT on disk — download_document is network-blocked on arxiv host
in this run; content below is from a server-side read_sources pass over the
arXiv HTML, which included the paper's own description of the algorithm.

## What this establishes — the exact embeddability algorithm

The problem the paper solves as a subroutine: decide whether a given simple
graph G has a unit-distance embedding f: V(G) → C (identifying R^2 with C),
i.e. |f(u) − f(v)| = 1 for every edge uv. This is exactly half of this run's
`unit_graph` oracle requirement, done graph-first rather than point-set-first.

The solver is a sequence of **logic moves** (L0–L3) on a linearized
formulation, with linear algebra over C on the kernel of a constraint matrix:

- **L0 (rhombus linearization).** For every 4-cycle v1–v2–v3–v4–v1 of G, any
  unit-distance embedding forces the four images to be the vertices of a
  rhombus, hence f(v1) + f(v3) = f(v2) + f(v4). All these constraints are
  collected into a single linear system A0 f = 0.
- **L1a (vertex-collision refutation).** If the linear constraints force
  f(v1) = f(v2) for two *distinct* vertices v1, v2 (i.e. the collision holds on
  every member of ker(A_s)), then G has no unit-distance embedding. Example
  given: G = K4 — the rhombus constraints collapse the kernel to scalar
  multiples of the all-ones vector, forcing every pair to coincide, so K4 is
  not unit-distance. (Consistent with the Globus–Parshall K4 ∈ F≤5.)
- **L1b (unit-modulus consistency).** For a candidate relation
  f(v1) − f(v2) = ω(f(v3) − f(v4)) forced on ker(A_s), compute
  B: ker(A_s) → C^2, B(f) = (f(v1)−f(v2), f(v3)−f(v4)). If im(B) is
  1-dimensional, the ratio ω = −y/x is forced; if |ω| ≠ 1 the constraint
  contradicts unit distances, and no embedding exists.
- **L2 (complementary test).** Same idea with the structural relation
  v1↔v2, v3↔v4; a forced ω with |ω| ≠ 1 refutes embeddability.
- **L3 (branching).** ∃[f|G_i, A_s] ⇒ ∃[f|G_i, A_{s0}] ∨ ∃[f|G_i, A_{s1}].

The solver returns "embeds", "does not embed", or "don't know". The authors
state this is much faster in practice than cylindrical algebraic decomposition
(which is double-exponential and impractical beyond ~10 vertices), and is what
let them decide embeddability for the F-free enumeration at 16–30 vertices.

**Context the paper supplies (consecutive to this):** u(n) (max unit distances
among n points) upper bounds improved for n ∈ {16,…,30}; for n ≤ 21 the bounds
match the best known lower bounds and the densest graphs are fully enumerated.
Uses Globus–Parshall's 74 forbidden subgraphs and nauty-based F-free graph
generation, plus "totally unfaithful unit-distance graphs" as a pruning tool.
  A search-result passage from the paper supplies one concrete value: the
  21-vertex Minkowski-sum graph (unit triangle + 6-wheel) attains **57
  unit-distance edges (u(21) ≥ 57)**, matching the previously published lower
  bound — the pre-paper state of the art was 57 ≤ u(21) ≤ 68.

## Why it matters here

This is a blueprint for the run's own graph-side embeddability oracle: exact
linear algebra over C (no floating point anywhere — the tests are kernel
dimension and |ω| = 1 exactness), with refutations certified by the constraint
system itself. The rhombus-linearization of 4-cycles is a structural fact the
run's construction engine should exploit directly: any 4-cycle in a candidate
point set is a rhombus, which is a rigid algebraic constraint.

```claim
id: amp-embedder-rhombus-linearization
statement: A graph with a 4-cycle v1-v2-v3-v4-v1 has every unit-distance embedding satisfy the rhombus equation f(v1)+f(v3) = f(v2)+f(v4); collecting these over all 4-cycles gives a linear system A0 f = 0 whose kernel constrains all embeddings. Embeddability is then decidable by the L0-L3 move system (kernel computations, forced-ratio unit-modulus tests, branching) more efficiently than CAD.
hypotheses: Plane embeddings identified with C; edges exactly at distance 1; the moves may return "don't know" rather than a decision.
holds-here: yes — this is the exact-arithmetic, graph-first embeddability method the run's unit_graph oracle can implement as a complement to point-list certification.
status: sourced (arXiv 2412.11914, section on the embedder; read via server-side read_sources, full text not on disk)
bearing: blueprint for the embeddability half of the oracle; the rhombus linearization is a rigidity fact the construction engine can use.
anchor: research/sources/amp-embeddability-solver.md
```

```claim
id: amp-ud-bounds-16-30
statement: Alexeev-Mixon-Parshall improve every upper bound on u(n), the maximum number of unit distances among n points in the plane, for n in {16,...,30}; for n <= 21 the upper bounds match the best known lower bounds and the densest unit-distance graphs are fully enumerated.
hypotheses: n points in R^2, distances exact; F-free enumeration (Globus-Parshall F<=9) plus the L0-L3 embeddability solver.
holds-here: yes for the census and size lower-bound effort - edge-count ceilings per n are exactly what 5-criticality (G-crit: delta >= 4, e >= 2n) converts into per-n chromatic bounds. The bound VALUES are not on disk; only their existence and ranges are sourced.
status: sourced (arXiv 2412.11914 abstract; read via read_sources)
bearing: for n <= 21, edge-count ceilings exist that could rule out 5-critical unit-distance graphs when 2n exceeds them; the run's own verifier must supply the numbers.
anchor: research/sources/amp-embeddability-solver.md
```

## Note on download

Full text download failed at the network layer (arxiv.org unreachable from
download_document in this run; 13/13 download attempts across hosts have
failed). Content above is from the server-side read_sources pass, which
included the algorithm description. Status: **sourced via read_sources; full
text not on disk**.