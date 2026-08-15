# Ladder: chromatic number of the unit-distance graph on R^2

Scope notes, so the dials below are read correctly.

- `exactness-trap` is **never** switched off in any rung. Adjacency is
  `|x - y| = 1` exactly, and a rung that relaxes it to a tolerance becomes a
  proximity-graph problem whose results do not transfer — a spurious edge can
  only raise the apparent chromatic number (the trap in `problem.md`). Exact
  algebraic coordinates are on in every rung, including the bottom one, because
  the bottom rung exists precisely to prove the exact path works.
- `infinite-target` is handled by the De Bruijn–Erdős reduction
  (`chi(G) = sup{ chi(H) : H finite subgraph }`, a proved input needing a
  compactness/choice principle): raising the lower bound is equivalent to
  finding a finite unit-distance graph of the required chromatic number. The
  real obstacle is the *space of finite candidates*, not the infinite vertex
  set.
- The bottom rung is **settled** by this run (four independent routes, captured
  in `code/out/calibrate_moser.captured.txt`, `brute_calibration.txt`,
  `sat_count_check.captured.txt`, `sat_calibration.captured.txt`,
  `verify_calibration_independent.captured.txt`). Everything above it is open
  or failed as marked.

```ladder
goal: determine chi(G) for the unit-distance graph G on R^2 (vertices: all points of the plane, edges iff |x - y| = 1 exactly); close the standing gap 4 <= chi(G) <= 7 in either direction.
difficulties: infinite-target, continuum-search, sparsity-random, rigidity-deficit, exponential-test, exactness-trap, upper-novelty
status: open
```

```rung
id: R-moser-calibration
statement: Reproduce the calibration pair in exact arithmetic: the 7-vertex Moser spindle from problem.md (two unit rhombi sharing a vertex, rotated by cos = 5/6, sin = sqrt(11)/6 so the far tips Q,Q' are at distance 1) has all 11 claimed unit edges certified |x-y|^2 = 1 symbolically over Q(sqrt3, sqrt11, sqrt33), and a complete k-colouring test reports chi = 4 (a 4-colouring witness exists, k = 3 is UNSAT).
off: infinite-target, continuum-search, sparsity-random, rigidity-deficit, exponential-test, upper-novelty
stance: settled
established-by: code/out/calibrate_moser.captured.txt (11 edges certified exactly, no spurious/missed edge on a full 21-pair scan; k=4 SAT with witness [0,1,2,0,1,2,3], k=3 UNSAT); code/out/brute_calibration.txt; code/out/sat_count_check.captured.txt (brute-force and SAT colouring counts agree exactly for k=1..5); code/out/sat_calibration.captured.txt and code/out/verify_calibration_independent.captured.txt (independent Cadical153/Minisat22 + numeric/symbolic rebuild)
merge: Oracle pair exists and is trusted (11 edges certified exactly, no spurious/missed edge on a full 21-pair scan; k=4 SAT with witness, k=3 UNSAT; brute-force and SAT colouring counts agree for k=1..5). Turn infinite-target back on via De Bruijn–Erdős to lift chi(Moser)=4 to chi(G) >= 4 — first move: state the compactness/choice hypothesis and check it against G.
```

```rung
id: R-standing-bounds
statement: Machine-verify the standing interval 4 <= chi(G) <= 7: the De Bruijn–Erdős lift of the settled Moser spindle (with its choice hypothesis stated and checked) gives the lower bound, and a hexagonal tiling gives the upper bound with side length, colour count 7, and exact minimum/maximum distance between same-coloured hexagons computed rather than asserted.
off: continuum-search, sparsity-random, rigidity-deficit, exponential-test, upper-novelty
stance: open
merge: The lower-bound half is already settled (Moser chi = 4 verified; the De Bruijn–Erdős lift is recorded as asserted-by-source in research/CLAIMS.md, not yet checked here). The upper-bound half is open: the hexagon exploration in commands.log is scratch, not a computed separation margin. First move: for side length s = 1/2 - eps, compute the exact same-colour hexagon separation and certify every hexagon has diameter < 1 while same-coloured hexagons are > 1 apart.
```

```rung
id: R-forced-pair-base
statement: Find a 4-chromatic unit-distance graph containing a pair (u,v) with |u-v| >= 1/2 that is monochromatic in every 4-colouring — the spindling crux that would let a forced-pair spindling accumulate rigidity toward chi >= 5.
off: infinite-target, continuum-search, sparsity-random, upper-novelty
stance: failed
failed-by: complete forced-pair SAT scan (code/out/forced_pair.captured.txt) found no forced pair — Moser spindle (10 pairs) and Moser+Moser (256 pairs) are both 4-colourable with no monochromatic-forced pair, so the spindle route's crux is not witnessed by these graphs
merge: A forced pair, if one exists, needs a strictly richer/denser base; feed rotation-coincidence Minkowski sums or spindlings of a seed that is itself forced through the same complete per-pair SAT test.
```

```rung
id: R-construction-census-small
statement: For a fixed, explicitly bounded family of structured constructions (Minkowski sums A+B and spindles whose coordinates live in a fixed exact field such as Q(sqrt3, sqrt11)), compute chi of every member with the complete oracle, keeping the family small enough that every k-colouring test terminates; report the maximum chi reached, the vertex count at which it occurs, and the size at which the test stops finishing.
off: infinite-target, continuum-search, sparsity-random, exponential-test, upper-novelty
stance: open
merge: Turn exponential-test back on by scaling the census to the boundary where the complete oracle stops finishing. First move: grow the family and record the largest n at which the k-colouring test completed, with encoding and time noted — that boundary is the first datum for the size-bound rung.
```

```rung
id: R-size-bound
statement: Theorem: every unit-distance graph on at most N vertices is 4-colourable, for the largest N this run can establish, by a structural argument — a minimal 5-chromatic graph has minimum degree >= 4, and each vertex's neighbours lie on a unit circle with pairwise chord-1 edges at 60 degrees — combined with complete verification of any boundary cases the argument leaves open.
off: infinite-target, continuum-search, sparsity-random, upper-novelty
stance: open
merge: Turn rigidity-deficit back on: stop proving 4-colourability and start asking what a construction must supply to force 5. First move: a theorem on what spindling does to the chromatic number, and which rotated Minkowski sums create the extra unit-distance coincidences.
```

```rung
id: R-lower-bound-closed
statement: Close the lower bound within the exact pipeline: exhibit a unit-distance graph that is not 4-colourable (exact coordinates, every edge symbolically certified, non-4-colourability by a complete method with independent re-verification), or prove that every unit-distance graph is 4-colourable.
off: upper-novelty
stance: open
merge: Turn upper-novelty back on — the last difficulty. The upper bound 7 -> 6 needs a genuinely new colouring scheme, not a search. First move: name the candidate class of colourings (periodic, tile-based) and compute the separation margin a 6-colouring would have to achieve.
```
