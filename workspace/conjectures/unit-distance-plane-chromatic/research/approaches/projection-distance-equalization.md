# Projection as distance equalization — a genuinely new UDG construction

```approach
idea: Treat the linear projection of a rigid higher-dimensional point set (a
      root system or regular-polytope vertex set in R^d) onto a plane not as a
      "rescaling" but as a *distance-equalization* machine. The squared
      projected distance of a pair (u,v) is the rank-2 quadratic form
      Q_π(u−v) = (a·(u−v))² + (b·(u−v))², where a,b ∈ R^d are the projection
      rows. Requiring Q_π(u−v) = 1 for a chosen set of pairs is a system of
      quadratic equations in the 2d projection parameters — and, because Q_π
      depends on the *direction* of u−v as well as its length, it maps pairs of
      DIFFERENT source lengths to the SAME planar length. The projected
      unit-distance graph is therefore genuinely new: it contains unit edges
      between pairs whose distances in the source set differ, which no rescaling
      of the source graph can produce. The projection parameters are the search
      space, and every edge condition is an exact polynomial equation.
mechanism: All existing construction engines (Minkowski sums, spindling,
      Henneberg H1/H2 — research/approaches/rigidity-matroid-henneberg-construction.md,
      research/threads/minkowski-rigidity.md) build rigidity *inside* R^2 by
      combining small graphs. This is a change of representation: the rigidity
      is pre-existing in a single symmetric configuration (the 24-cell has 24
      vertices / 96 edges / 1152 symmetries; the 600-cell has 120 vertices /
      720 edges / 14400 symmetries), and the only freedom is the rank-2 linear
      projection — 2d parameters, down to ~2d−4 essential after quotienting by
      image rotation and scale. The named mathematics: root systems, the regular
      4-polytopes, and their Coxeter/Petrie projections.
      SPECULATIVE part, stated as such: whether any projection yields a
      5-chromatic graph or a 4-colouring-forced pair (the crux
      `G-forced-pair-exists`) is open — no located source reports one. The
      certain value is a new supply of dense, rigid, exactly-certifiable planar
      UDGs to feed the forced-pair harness and the census, which the run's
      Minkowski/spindle engine cannot express. Falsifies the line's value: if
      every swept projection is 4-colourable with no forced pair and sparser
      than Moser+Moser, the family is a census datum only.
status: adopted
precedent: Projecting regular 4-polytopes (24-cell {3,4,3}, 600-cell {3,3,5},
      120-cell {5,3,3}) onto planes along symmetry axes is standard and exact:
      Chilton, "On the projection of the regular polytope {5,3,3} into a
      regular triacontagon", Canad. Math. Bull. 1964,
      https://doi.org/10.4153/cmb-1964-037-9 — the 600-cell projects to a
      regular 30-gon along the Petrie polygon; Al Ajmi, Koca & Bait Bu Salasel,
      "Projection of polyhedra onto Coxeter planes described with quaternions",
      SQUJS 19 (2015), https://doi.org/10.24200/squjs.vol19iss2pp77-90 — the
      24-cell vertex set is the binary tetrahedral group, the 600-cell the unit
      icosians, both in exact quadratic fields (24-cell integer, 600-cell in
      Q(√5)). The distance-equalization mechanism is elementary linear algebra
      and is CONCRETELY exhibited: 24-cell pairs with difference vectors
      (0,2,0,0) and (0,−1,1,0) have squared source lengths 4 and 2 respectively,
      yet under projection rows a=(0,1,3,0), b=(0,0,0,1) both give Q_π = 4
      exactly (2²+0 and (3−1)²+0). Two distinct 4D lengths equalize to one
      planar length — a rank-2 map is not a homothety. This OVERTURNS the
      "rescaling only, cannot create new unit relationships" killing
      consideration recorded in
      research/approaches/projected-root-lattice-constructions.md (which is
      why that file is superseded, not kept as the adopted line). NULL precedent
      for the chromatic question: no located source computes chi of these
      projected UDGs, and none reports a 5-chromatic projected graph — honest
      absence, the application is novel/unrecorded.
bearing: The lower-bound crux `G-forced-pair-exists` is blocked by a shortage of
      richer base graphs (spindle and Moser+Moser exhausted, no forced pair).
      This line supplies a genuinely new, dense, rigid family — a single
      24-cell/600-cell projection can carry far more unit edges per vertex than
      a Minkowski sum of small gadgets, with every edge certified exactly over
      Q or Q(√5) — and it feeds the same complete forced-pair SAT harness
      (code/forced_pair.py) plus the census. Its chromatic outcomes are
      machine-checkable in both directions: a 4-colouring witness when 4-
      colourable, a complete UNSAT certificate otherwise.
first-step: >
  (1) code/lib/polytope_sets.py: the 24-cell as all 24 permutations of
      (±1,±1,0,0) (exact integers) and the 600-cell's 120 vertices in Q(√5)
      (standard unit-icosian representation), each stored as exact tuples.
  (2) project(S, a, b) with rows a,b ∈ R^d, kept exact (sympy).
  (3) MACHINE-VERIFY the equalization counterexample before anything else:
      rows a=(0,1,3,0), b=(0,0,0,1) must give Q_π(0,2,0,0) = Q_π(0,−1,1,0) = 4
      symbolically, no floats. This is the datum that justifies the whole line;
      if it does not reproduce, the line is dead at the first step.
  (4) Sweep the Petrie/Coxeter projections and a rational one-parameter family
      of generic planes; for each, normalise the densest coincidence class to
      unit length, run unit_graph(points) + chromatic_number(graph,4) +
      code/forced_pair.py. Report edge density, chromatic number, and forced
      pairs per projection; feed any forced-pair candidate into the spindle
      skeleton, and grade the graphs with the Nullstellensatz forced-pair
      certificate (research/approaches/nullstellensatz-colouring-certificate.md)
      as the independent re-check.
```

## Why this over the other two candidates

- **Nullstellensatz certificate** is correct and complete (NulLA) but is a
  *re-verifier*, not a search line: at the run's sizes it does not beat SAT, and
  its deliverable is idle until the run holds a non-4-colourable graph. It does
  not supply the richer base graphs the crux needs.
- **Cut-and-project Meyer 6-colouring** is the superclass of the already
  adopted-and-blocked flat-torus line and inherits its continuum-margin gap
  wholesale; its value is conditional on settling that step first, on the
  unstructured upper-bound side away from the live crux.

The projection line attacks the actual obstruction (a new source of dense rigid
base graphs for the forced-pair harness) with a mechanism the run has never
used, and the correction to the "rescaling only" claim is itself a result worth
owning.

## Attack surface — what breaks this line

- The equalization counterexample must reproduce symbolically (first step 3).
  If it does not, the whole line is dead at the first step.
- A projection cannot equalize *every* pair arbitrarily: some target edge sets
  are not realizable as projections of a fixed source set (e.g. K4, which is
  not a planar UDG). The honest search is a sweep over projection parameters,
  not a claim that any graph is reachable.
- The rescaling objection is not entirely empty — along a single symmetry
  direction distances do just scale. The point is that a *rank-2* map has two
  directions to trade off, and that is what creates new coincidences; a
  rank-1 (axis-aligned) projection genuinely only rescales and is not the
  mechanism.
