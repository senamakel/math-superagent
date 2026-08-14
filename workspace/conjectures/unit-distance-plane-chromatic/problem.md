# Colouring the plane at unit distance

## Statement

Let `G` be the graph whose vertices are **all** the points of the Euclidean
plane `R^2`, with

```
x ~ y   if and only if   |x - y| = 1
```

where `|·|` is the ordinary Euclidean distance. `G` is an infinite graph of
infinite degree.

> **Question.** Determine `chi(G)`, the least number of colours needed to
> colour every point of the plane so that no two points at distance exactly `1`
> receive the same colour.

The quantity is finite and is known to satisfy

```
4  <=  chi(G)  <=  7
```

Both bounds are elementary and both are reproduced below. **Neither has moved
in decades.** Closing the gap in either direction — proving `chi(G) >= 5`, or
proving `chi(G) <= 6` — is the objective.

## What the statement does and does not say

- The relation is `|x - y| = 1` **exactly**. Points at distance `0.999` or
  `1.001` are not adjacent. The graph is not a geometric proximity graph and
  nothing about it is approximate.
- The colouring is of **every point of the plane**, not of a finite point set.
  There is no continuity, measurability or connectedness requirement on the
  colour classes, and imposing one changes the problem: the measurable and the
  "colour classes are nice regions" variants have their own, larger, known
  lower bounds and are **not** what is asked here. A statement proved under a
  measurability hypothesis is a result about that variant and must be recorded
  as such.
- The unit is a normalisation, not a constraint: scaling the plane carries any
  distance to `1`, so there is nothing special about the number.
- `chi(G) >= k` is equivalent to the existence of a **finite** subgraph with
  chromatic number `>= k`. This is the De Bruijn–Erdős reduction and it is the
  single most important structural fact here: because `G` has an ordinary
  compactness property, **the whole infinite problem is decided by finite
  configurations.** A lower-bound proof is therefore a finite object — a finite
  set of points in the plane, together with the fact that the graph they induce
  at unit distance is not `(k-1)`-colourable. Nothing infinite has to be
  reasoned about to raise the lower bound.

A finite set of points in the plane, with edges between pairs at distance
exactly `1`, is called a **unit-distance graph**. Restated:

> **Lower-bound form.** Exhibit a unit-distance graph that is not
> `4`-colourable, or prove no such graph exists.

## Where the bounds come from — reproduce both before doing anything else

**Upper bound `chi(G) <= 7`.** Tile the plane by regular hexagons of diameter
slightly less than `1`, and colour the tiling with `7` colours so that two
hexagons of the same colour are always more than `1` apart. Assign each point
its hexagon's colour, breaking boundary ties consistently. The margin is what
makes it work and it must be computed here, not asserted: state the hexagon
side length used and the exact minimum and maximum distance between same-coloured
hexagons.

**Lower bound `chi(G) >= 4`.** There is a `7`-vertex unit-distance graph with
chromatic number `4`, built from two rhombi of unit side sharing a vertex,
rotated relative to one another so that their far vertices are at distance `1`.
It contains two unit triangles per rhombus.

Both of these are inputs to be **verified in this workspace**, not quoted. Build
the `7`-vertex graph in exact arithmetic, confirm every claimed edge really has
length exactly `1`, and confirm by search that it needs `4` colours and no
fewer. A lower-bound pipeline that cannot re-derive `4` on this graph is broken,
and everything measured with it afterwards is worthless.

## The obstruction, stated honestly

The lower bound is where the problem is. The upper bound has resisted for a
different and less interesting reason — nobody has a construction beating the
hexagonal tiling — and improving it means inventing a genuinely new colouring
scheme, which is a much less structured search.

For the lower bound, the difficulty is precise and it is **not** that
`4`-colourability is hard to test. It is a search-space problem:

1. **Small unit-distance graphs are `4`-colourable, and they are `4`-colourable
   easily.** Every unit-distance graph anyone writes down by hand has a
   `4`-colouring, usually an obvious one. The obstruction to `5` is not
   fragile — it must be forced by accumulated rigidity, not by a local gadget.
2. **The space of unit-distance graphs is not a space you can enumerate.**
   Vertices are points in `R^2` — a continuum — and edges are determined by the
   embedding rather than chosen. You cannot enumerate graphs and ask which are
   unit-distance; you must construct point sets, and the useful ones are not
   random. So the search has to be over *constructions*, which means over ideas.
3. **A random or greedy point set has too few edges.** A unit-distance graph on
   `n` points has `O(n^{4/3})` edges, so density cannot be bought. Any graph
   forcing a high chromatic number has to be **rigid**: its unit distances must
   be highly coincidental, which happens only for point sets with algebraic
   structure.

The productive framing is therefore:

> **The question is which algebraic structures on the plane produce point sets
> whose unit-distance graph is unexpectedly rigid, and whether the rigidity can
> be accumulated far enough to defeat `4` colours.**

The standard machine for accumulating it is the **Minkowski sum**: given point
sets `A` and `B`, form `A + B = { a + b }`. Sums of small unit-distance graphs
produce large ones with far more unit distances than their size suggests,
because a unit distance in the sum can arise from many different pairs. Rotating
one summand by an angle chosen so that extra unit distances appear is the other
half of the machine. Both are cheap to implement, and neither has been pushed
systematically here.

The honest position: it is not known whether `chi(G)` is `4`, `5`, `6` or `7`,
and opinions have been offered for all four. **Do not assume the answer is
greater than `4`.** A rigorous proof that every unit-distance graph is
`4`-colourable would settle the problem just as completely, and an attack that
only ever looks for `5`-chromatic examples cannot find it.

## The oracle, and the trap it exists to prevent

Success here is **machine-checkable**, which is unusual and should be exploited
to the fullest. A claimed lower bound of `5` is a finite list of points, and it
is correct if and only if two independently checkable things hold:

1. **Every claimed edge is a genuine unit distance,** verified in **exact
   arithmetic**. Points will have coordinates in a field like
   `Q(sqrt(3), sqrt(11), ...)`; the verification must be symbolic or exact, never
   floating-point.
2. **The graph is not `4`-colourable,** verified by a complete method — a SAT
   solver returning UNSAT on the `4`-colouring encoding, or an exhaustive search.

**The trap is step 1, and it is the one that has destroyed this kind of work
before.** Floating-point coordinates make near-unit distances look like unit
distances. A graph assembled with a tolerance of `1e-9` will contain edges that
do not exist, and a spurious edge can only *increase* the apparent chromatic
number. So a floating-point pipeline reliably produces false `5`-chromatic
graphs, and they look completely convincing until checked exactly.

Therefore: **coordinates are exact algebraic numbers from the first line of
code.** Not floats, not floats with a tolerance, not rationals approximating
irrationals. If a construction cannot be carried out exactly, the construction
is what has to change.

A second, weaker trap: a SAT solver reporting UNSAT is a claim about the CNF it
was given, not about the graph. Check that the encoding is right by feeding it
the `7`-vertex graph and confirming it reports SAT for `4` colours and UNSAT for
`3`.

## Leads — verify each before relying on it

These are directions, not established facts. Each needs a primary source where
one exists, and its own claim block with an explicit status.

- **The De Bruijn–Erdős reduction** — that `chi` of the infinite graph equals the
  supremum of `chi` over its finite subgraphs. State the hypotheses it needs
  (it uses a choice principle) and record it as a proved input.
- **The `O(n^{4/3})` bound on unit distances** among `n` points in the plane.
  This is the constraint that says density cannot be bought, so the run should
  know it exactly and know what it does *not* forbid.
- **Minkowski sums and rotations of small unit-distance graphs.** The main
  construction engine. Verify that a sum of unit-distance graphs is a
  unit-distance graph, and work out exactly which pairs in `A + B` land at
  distance `1` — this is the calculation the whole approach rests on.
- **Spindling.** The operation that produced the `7`-vertex graph from two
  rhombi generalises: given a graph and two vertices forced to differ, rotate a
  copy about a shared vertex so the two far vertices coincide or become
  adjacent. Work out what it does to the chromatic number in general.
- **Point sets with algebraic structure** — rings of integers, lattices in
  quadratic or cyclotomic fields, and other sets closed under the operations
  that create unit distances. The question is which fields make unit distances
  abundant.
- **Upper-bound side.** Colourings of the plane by shapes other than hexagons.
  Any construction using fewer than `7` colours would be at least as large a
  result as the lower bound, and the direction is much less explored.
