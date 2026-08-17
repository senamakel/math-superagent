# Librarian cycle — closing staircase-convexity-unsourced

Scope: this cycle pursued exactly the one named source-gap tied to the live
allowable-sequence/extremal-structure thread (`staircase-convexity-unsourced`),
per the standing directive to gather only against a stated gap.

## What was acquired

1. **Gärtner, ETH *Computational Geometry* course notes (2012)**
   - `research/sources/gaertner-eth-computational-geometry-convex-hull-characterization-2012.full.md`
   - source URL: https://ti.inf.ethz.ch/ew/Lehre/CG13/lecture/cg-2012.pdf
   - Prop 3.17: *p is extremal for P ⇔ there is a directed line g through p with
     P∖{p} to the left of g* — the supporting-line/hull-vertex characterization.
   - Closure: the surviving "extreme-in-projection ⟺ hull vertex" criterion of the
     allowable-sequence thread is now literature-sourced, not machine-confirmed-
     but-unsourced. Claim `hull-vertex-extreme-in-projection-sourced` filed and in
     derived/CLAIMS.md.

2. **Cardinal & Santos, "Sweeps, Polytopes, Oriented Matroids, and Allowable
   Graphs of Permutations", Combinatorica 44 (2024) 63–123 (open access)**
   - `research/sources/cardinal-santos-sweeps-polytopes-oriented-matroids-allowable-graphs-2023.full.md`
   - source URL: https://link.springer.com/article/10.1007/s00493-023-00062-3
   - Framework only: confirms the 2D allowable sequence is the rank-2 sweep
     oriented matroid; generalizes to higher dimension. Does NOT carry the exact
     constant. Recorded as context/vocabulary, not load-bearing.

## Requests state

All three requests (balko-valtr-attack-baa4, open-access-full-1e6e,
full-text-faithful-b96b) are answered by held primary full texts whose claim
blocks carry `answers:` fields. No open request remains to gather against.

## What is NOT new, and why nothing else was fetched

- The library already covers 1935 + 1961 primaries, Morris–Soltan and Tóth–Valtr
  surveys, all published upper bounds, SAT attacks (Balko–Valtr/Scheucher/Dumitru/
  Koshelev–Koshka), Aichholzer order-type enumeration, CC systems, signotopes,
  empty-hexagon, higher dimensions, Duque integer realization, saturation,
  split/decomposable sets, and the allowable-sequence framework.
- The whole-ES upper bound is open; the run must not drift into asymptotics,
  the monotone-subsequence theorem, or adjacent problems.
- Per steer 12 and the directive, gathering is admissible only against a stated
  gap; no further gap is stated in derived/REQUESTS.md. This cycle therefore
  added the one gap's closure and stopped.

## Housekeeping notes for the team

- `remember_memory` store is currently DOWN (3 failures, health-report timeout).
  The verified closure is durable in the summary note + claim ledger instead;
  it should be pushed to Cognee memory when the store recovers.
- The claimed `hull-vertex-extreme-in-projection-sourced` is classified
  "asserted by the source" by the runtime (status: sourced); the *machine*
  verification of the EPS property on es_construct is separately recorded in the
  existing thread/claim history. Both facts together are what close the gap.
