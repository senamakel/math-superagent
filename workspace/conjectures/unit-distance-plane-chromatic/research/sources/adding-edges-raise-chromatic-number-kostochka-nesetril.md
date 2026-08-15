# Adding edges to increase the chromatic number: Kostochka & Nešetřil (2016)

**Subject:** The abstract graph theory governing whether adding edges to a
`k`-chromatic graph can force a higher chromatic number — the graph-level
backbone of the run's OPEN question in `research/REQUESTS.md` (whether
spindling / Minkowski-sum accumulation can force a `4`-colourable unit-distance
graph to become non-`4`-colourable by adding one more constrained edge, i.e. a
vertex pair forced monochromatic at distance `>= 1/2`).

This is **not** answer-tier: it makes no claim about the chromatic number of the
plane and constructs no unit-distance `5`-chromatic graph. It is the general
combinatorial fact that says *how much* edge-addition is needed to force a
colour jump, which the forced-pair/spindling machinery is an instance of.

## Source

- **Alexandr Kostochka, Jaroslav Nešetřil**, *Adding Edges to Increase the
  Chromatic Number of a Graph*, Combinatorics, Probability and Computing **25**
  (2016), DOI 10.1017/s0963548316000146.
  Retrieved via `read_sources` on 2026 run (server-side; direct publisher
  download blocked at the network boundary).

## What it establishes (exact statements)

**Theorem (Kostochka–Nešetřil, proving a conjecture of Bollobás).** For every
`k >= 3` there exists a `k`-chromatic graph `G_k` such that adding **any**
`C(k,2) - 1` edges to `G_k` leaves its chromatic number at `k`; but a suitable
`C(k,2)`-edge *set* can force a `K_{k+1}`, raising the chromatic number above
`k`.

Immediate companion fact: for any connected `n`-vertex graph with `n >= k+1`,
one can add `C(k,2) = k(k-1)/2` edges so that the resulting graph contains
`K_{k+1}`, hence has chromatic number `> k`.

**Reading for k = 4 (the run's case).** `C(4,2) = 6`: any connected graph with
`>= 5` vertices can be made to contain a `K_5` by adding 6 well-chosen edges,
forcing non-`4`-colourability; yet there exist `4`-chromatic graphs that resist
becoming non-`4`-colourable under **any** addition of at most 5 edges.

## Why it matters here

- **Positivity of the forced-edge direction.** The theorem shows it is *not* a
  graph-theoretic impossibility that adding a small number of edges to a
  `4`-chromatic graph forces a colour jump — indeed `6` edges always suffice to
  create a `K_5`. So the run's forced-pair/spindling route is not blocked by a
  general theorem saying edge-addition never raises the chromatic number; the
  obstruction, if any, is specifically that in the **unit-distance** setting the
  edges one is allowed to add are highly constrained (only pairs at distance
  exactly 1, and spindling adds *one* such edge / identification at a time).
- **One edge is too few to guarantee a jump.** The theorem's tightness
  (resistance to `C(k,2)-1 = 5` edge additions for `k=4`) is the abstract
  counterpart of the run's *measured* fact that a single forced pair is hard to
  arrange: forcing a `5`-chromatic jump from a `4`-chromatic graph by adding
  edges generically needs several coordinated additions, not one. This bounds
  what a single spindling step can be expected to do on its own, and points
  accumulation (gluing many forcements) as the only viable route — matching the
  run's Minkowski-sum/accumulation thread.
- **Caveat on applicability.** The theorem is about *arbitrary* graphs and
  *arbitrary* edge sets of a given size; it does not carry over verbatim to
  unit-distance graphs, where adding an edge requires the two endpoints to be
  at distance exactly `1`. So it is context and a positivity check, not a
  transferable construction.

## Basis and status

- Exact statements sourced (abstract + body via `read_sources`).
- Not machine-verified here (abstract graph theory; the + one edge can never
  force a jump by itself is elementary: adding one edge to a k-chromatic graph
  can keep chromatic number k whenever the two endpoints have some common
  colour available in a k-colouring with them different, which is the case iff
  they are not forced monochromatic — the run's own forced-pair oracle decides
  this exactly).
- Recorded as context for the OPEN forced-pair/spindling row, not as a claim
  about chi(plane).

## Claim block

```claim
id: adding-edges-raise-chromatic-number
statement: For every k >= 3 there is a k-chromatic graph G_k such that adding
  any C(k,2)-1 edges leaves its chromatic number at k, while some C(k,2)-edge
  set forces a K_{k+1} and hence chromatic number > k; and every connected
  graph on >= k+1 vertices can, by adding C(k,2) suitable edges, be made to
  contain a K_{k+1}.
hypotheses: arbitrary finite simple graphs; edge additions unrestricted (any
  pair of non-adjacent vertices).
holds-here: PARTIAL — the positivity half transfers (six coordinated edge
  additions can always force a K_5-style jump from a 4-chromatic graph), but
  the unit-distance setting restricts allowed edges to distance-1 pairs and
  spindling adds one edge/identification at a time, so the theorem does not
  directly transfer to unit-distance constructions.
status: asserted-by-source (Kostochka–Nešetřil 2016, proving Bollobás's
  conjecture).
bearing: positivity check and bound for the forced-pair/spindling route: it
  confirms edge-addition CAN force a colour jump in general (so the run's
  direction is not combinatorially impossible), and that a single added edge
  is generically insufficient — accumulation of many forcements is required.
anchor: research/sources/adding-edges-raise-chromatic-number-kostochka-nesetril.md
falsifies: a proof that for unit-distance graphs specifically, adding < 6 unit
  edges to a 4-colourable UDG can never make it non-4-colourable — which the
  theorem does NOT provide (it is silent on the unit-distance restriction),
  and which would close the run's forced-edge direction outright.
```
