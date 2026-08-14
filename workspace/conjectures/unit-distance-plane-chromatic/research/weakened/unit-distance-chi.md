# Ladder: chromatic number of the unit-distance graph on R^2

Scope note, so the dials below are read correctly.

- `exactness-trap` is **never** switched off in any rung. Adjacency is `|x-y| = 1`
  exactly, and a rung that relaxes it to a tolerance becomes a proximity-graph
  problem whose results do not transfer (a spurious edge can only raise the
  apparent chromatic number — the trap in `problem.md`). Exact algebraic
  coordinates are on in every rung, including the bottom one, because the bottom
  rung exists precisely to prove the exact path works.
- `infinite-target` is dialed off by the De Bruijn–Erdős reduction (a proved
  input needing a choice principle): `chi(G) >= 5` is equivalent to the
  existence of a finite unit-distance graph with `chi >= 5`. So the real
  obstacle is the *space of finite candidates*, not the infinite vertex set.

Stances reflect the claims ledger at the time of writing: `research/CLAIMS.md`
records nothing yet, so no rung here is settled by this run and every rung is
`open` until a forward attempt closes it.

```ladder
goal: determine chi(G) for the unit-distance graph G on R^2 (all points of the plane, edges iff |x - y| = 1 exactly); close the standing gap 4 <= chi(G) <= 7 in either direction.
difficulties: infinite-target, continuum-search, exactness-trap, rigidity-deficit, exponential-test, colouring-construction
status: open
```

```rung
id: R-moser-calibration
statement: Determine the chromatic number of the 7-vertex Moser spindle from problem.md in exact arithmetic: symbolically certify all 11 of its unit edges (|x - y|^2 = 1 over the exact coordinate field), and prove by a complete colouring test that chi = 4 (a 4-colouring exists, no 3-colouring exists).
off: infinite-target, continuum-search, exponential-test, rigidity-deficit, colouring-construction
stance: open
merge: Turn infinite-target back on by applying De Bruijn–Erdős (record the choice hypothesis it needs) to lift the verified finite chi = 4 to chi(G) >= 4. First move: state the compactness theorem and check its hypotheses against G.
```

```rung
id: R-standing-bounds
statement: Machine-verify the standing interval 4 <= chi(G) <= 7: the De Bruijn–Erdős lift of the verified Moser spindle gives the lower bound, and a hexagonal tiling gives the upper bound with side length, separation margin, and exact minimum/maximum distance between same-coloured hexagons computed rather than asserted.
off: continuum-search, exponential-test, rigidity-deficit, colouring-construction
stance: open
merge: Turn continuum-search back on: fix a structured construction family (Minkowski sums A+B and spindles of small exact unit-distance graphs over quadratic fields) and census its chromatic numbers. First move: the theorem characterising exactly which pairs in A+B land at unit distance.
```

```rung
id: R-construction-census-small
statement: For a fixed, explicitly bounded family of structured constructions (Minkowski sums and spindles whose coordinates live in a fixed exact field such as Q(sqrt(3))), compute chi of every member with the complete oracle, keeping the family small enough that every complete k-colouring test terminates; report the maximum chi reached and the vertex count at which it occurs.
off: exponential-test, rigidity-deficit, colouring-construction
stance: open
merge: Turn exponential-test back on by scaling the census to the boundary where the complete oracle stops finishing. First move: grow the family and record the largest n at which the k-colouring test completed, with the encoding and time noted — this boundary is the first datum for the size-bound rung.
```

```rung
id: R-size-bound
statement: Theorem: every unit-distance graph on at most N vertices is 4-colourable, for the largest N this run can establish, by a structural argument (a vertex of degree <= 3 can always be removed and recoloured, so a minimal 5-chromatic graph has minimum degree >= 4, and its vertex-neighbourhoods lie on a unit circle with chord-1 edges at 60 degrees) combined with complete verification of any boundary cases the argument leaves open.
off: rigidity-deficit, colouring-construction
stance: open
merge: Turn rigidity-deficit back on: stop proving 4-colourability and start asking what the engine must do to force 5. First move: a theorem on what spindling does to the chromatic number and which rotated Minkowski sums create the extra unit-distance coincidences.
```

```rung
id: R-lower-bound-closed
statement: Close the lower bound within the exact pipeline: exhibit a unit-distance graph that is not 4-colourable (exact coordinates, every edge symbolically certified, non-4-colourability by a complete method with independent re-verification), or prove that every unit-distance graph is 4-colourable.
off: colouring-construction
stance: open
merge: Turn colouring-construction back on — the last difficulty. The upper bound 7 -> 6 needs a genuinely new colouring scheme, not a search. First move: name the candidate class of colourings (periodic, tile-based) and compute the separation margin a 6-colouring would have to achieve.
```
