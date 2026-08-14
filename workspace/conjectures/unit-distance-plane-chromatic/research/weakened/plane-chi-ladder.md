# Ladder: colouring the plane at unit distance

Scope note, so the dials are read correctly.

- `exactness-trap` is **declared** as a difficulty because it is the single
  obstruction that has destroyed this kind of work before, but it is **never in
  any rung's `off` list**. Adjacency is `|x - y| = 1` exactly; a rung that
  relaxes it to a tolerance becomes a proximity-graph problem whose results do
  not transfer (a spurious edge can only raise the apparent chromatic number —
  the trap in `problem.md`). Exact algebraic coordinates are on in every rung,
  including the bottom one, because the bottom rung exists precisely to prove
  the exact path works.
- The infinite vertex set is already dialed off by De Bruijn–Erdős (a proved
  input needing a choice principle): `chi(G) >= 5` is equivalent to the
  existence of a *finite* unit-distance graph with `chi >= 5`. `continuum-space`
  below therefore means the space of *finite candidate point sets*, which is a
  continuum and is the real obstacle to enumeration.
- Stances reflect the claims ledger at the time of writing:
  `research/CLAIMS.md` holds only `asserted` claims, none `checked` or
  `formalised` here, and `CONTEXT.md` records a greenfield run. So **no rung is
  settled by this run** and every rung is `open` until a forward attempt closes
  it. No rung has been attacked and failed, so none carries a failure reason.

```ladder
goal: determine chi(G) for the unit-distance graph G on R^2 (vertices = all points of the plane, edges iff |x - y| = 1 exactly), i.e. close the standing gap 4 <= chi(G) <= 7 in either direction: exhibit a unit-distance graph with chi >= 5 in exact algebraic coordinates with complete machine verification, or prove every unit-distance graph is 4-colourable, or give an explicit 6-colouring of the plane with a computed separation margin
difficulties: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty, exactness-trap
status: open
```

The eight dials, one line each:

- `unbounded-n` — no known bound on the size of a minimal 5-chromatic unit-distance graph; the search is over unbounded n.
- `continuum-space` — candidate point sets fill R^2, so the space is not enumerable and search must be over *constructions* (ideas), not over a list; every universal claim about small n must also control the continuum of embeddings.
- `sparse-random` — random or greedy point sets have only O(n^{4/3}) unit distances, so density cannot be bought by sampling; rigidity must come from algebraic coincidence.
- `nonlocal-obstruction` — every small hand-written unit-distance graph is 4-colourable, easily; the obstruction to 5 must be accumulated global rigidity, not a local gadget.
- `exp-colour-test` — the complete k-colourability test is exponential in n, bounding how large a candidate can be checked and how far any census can go.
- `direction-unknown` — chi(G) could be 4, 5, 6 or 7; a search that only looks for 5-chromatic graphs may be chasing a graph that does not exist.
- `upper-novelty` — improving 7 to 6 needs a genuinely new colouring scheme; there is no structured search, only invention.
- `exactness-trap` — adjacency is `|x-y| = 1` exactly; floating point manufactures spurious edges that can only raise the apparent chromatic number. Declared so the ladder names it, never switched off.

```rung
id: R-moser-calibration
statement: build the 7-vertex Moser spindle from problem.md (two unit rhombi sharing a vertex, rotated so the far vertices are at unit distance) in exact arithmetic; symbolically certify all 11 claimed edges satisfy |x-y|^2 = 1 over the exact coordinate field; and by a complete k-colouring test prove chi = 4 (a 4-colouring exists, no 3-colouring exists)
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown, upper-novelty
stance: open
merge: oracle pair (exact edge certifier + complete colouring test) trusted; turn nonlocal-obstruction and exp-colour-test on by fixing the construction engine and censusing its outputs. First move: state and prove the exact pair-distance theorem for Minkowski sums A+B — which pairs (a1+b1, a2+b2) land at distance exactly 1 — over a fixed exact field such as Q(sqrt(3))
```

```rung
id: R-construction-census
statement: run the exact construction engine (Minkowski sums, rotations chosen for coincidence, spindling) over an explicitly bounded family of small seed graphs whose coordinates live in a fixed exact field; prove the pair-distance structure of each construction; record the chromatic number of every resulting unit-distance graph, the maximum chi reached, and the vertex count at which the complete colouring test stopped finishing
off: unbounded-n, continuum-space, sparse-random, direction-unknown, upper-novelty
stance: open
merge: turn continuum-space on by promoting the finite-family census into a universal claim over all embeddings: every unit-distance graph on at most N vertices is 4-colourable. First move: the structural lemma that a vertex of degree <= 3 is always removable (so a minimal 5-chromatic unit-distance graph has minimum degree >= 4), then classify or enumerate the rigid small-n embeddings that survive
```

```rung
id: R-size-bound
statement: prove that every unit-distance graph on at most N vertices is 4-colourable, for the largest N the run can establish, by a structural argument (a vertex of degree <= 3 is removable, so a minimal 5-chromatic witness has minimum degree >= 4, and its vertex-neighbourhoods lie on a unit circle with chord-1 edges at 60 degrees) combined with complete verification of any boundary cases the argument leaves open
off: unbounded-n, sparse-random, nonlocal-obstruction, direction-unknown, upper-novelty
stance: open
merge: turn nonlocal-obstruction back on by trying to break 4-colourability past N: grow the rigid at-most-N configurations via spindling and Minkowski sums and test the offspring at k=4 with the complete oracle. First move: spindling the Moser spindle — a theorem on what the operation does to chromatic number, and which rotated Minkowski sums create the extra unit-distance coincidences
```

```rung
id: R-lower-bound-five
statement: exhibit a unit-distance graph with chi >= 5, given as an explicit vertex list in exact algebraic coordinates, every edge certified |x-y|^2 = 1 symbolically, and non-4-colourability verified by a complete method, with the verification re-done independently of the code that produced the graph
off: upper-novelty
stance: open
merge: if settled, chi(G) >= 5 and only upper-novelty remains between the run and the answer (5 <= chi <= 7). A candidate that fails is still a result: record the construction and why it stays 4-colourable, because that names exactly which rigidity the obstruction still lacks
```

```rung
id: R-upper-bound-six
statement: give an explicit 6-colouring of the plane — a covering by 6 colour classes with a computed positive separation margin proving no two points at distance exactly 1 share a colour — i.e. a genuinely new scheme beating the 7-colour hexagonal tiling
off: unbounded-n, continuum-space, sparse-random, nonlocal-obstruction, exp-colour-test, direction-unknown
stance: open
merge: if settled, combined with the verified lower bound 4 it gives 4 <= chi <= 6, and with R-lower-bound-five settled it determines chi. First move: name the candidate class of colourings (periodic, tile-based) and compute the exact separation margin a 6-colouring must achieve to beat the 7-colour hexagonal benchmark
```
