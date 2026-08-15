# Projected root lattices and regular-polytope vertex sets as rigid UDGs

```approach
idea: Import rigidity from higher dimension instead of accumulating it inside
      the plane. Take the vertex set of a highly symmetric regular polytope or
      root lattice in R^d (24-cell, 600-cell, 120-cell, the D4/E8 root systems)
      and project it linearly onto a plane R^2 chosen along a symmetry axis
      (Coxeter/Petrie projection). Pairs whose *projected* distance is exactly 1
      become edges. This is a new source of unit-distance graphs — a single
      pre-existing rigid configuration, not a sum/rotation of small 2D gadgets —
      and the projection parameters are the search space.
mechanism: The existing construction engines (Minkowski sums, spindling,
      Henneberg H1/H2 — research/approaches/rigidity-matroid-henneberg-construction.md,
      research/threads/minkowski-rigidity.md) all operate *within* R^2 and
      accumulate rigidity by combining small graphs. This is a change of
      representation: the rigidity is already present in a root system / regular
      polytope in R^d, and the question becomes "which 2D projection preserves
      many of its pairwise distances as unit distances." Concretely, a linear
      projection π: R^d → R^2 is a pair of row vectors (a, b) ∈ (R^d)^2; the
      squared projected distance of a pair (u, v) is the quadratic form
      |π(u−v)|^2 = ⟨u−v, a⟩^2 + ⟨u−v, b⟩^2. Requiring this to equal 1 for a
      chosen set of pairs is a system of polynomial equations in the 2d
      projection parameters — solvable exactly with the run's symbolic field
      arithmetic (coordinates of polytope vertices live in quadratic/cyclotomic
      fields, so projections land in the run's exact fields). The named
      mathematics: root systems and their Coxeter projections, the regular
      4-polytopes (24-cell in R^4 with 24 vertices and 96 edges; 600-cell with
      120 vertices and 720 edges, all edges of a well-defined length), and
      "diameter graphs" / projected unit-distance graphs. Choosing the plane as
      the span of two symmetry axes (e.g. the two large eigenspaces of a Coxeter
      element, the standard Petrie projection) is what makes many distances
      coincide to exactly 1 — a search over *constructions* (symmetry axes and
      scales), not over random point sets, so it respects the no-random-search
      rule.
      SPECULATIVE part, stated as such: whether any projection of these
      polytopes yields a 5-chromatic graph is open; the proposal's certain value
      is a new, dense, rigid family whose chromatic numbers the run's calibrated
      oracle can census and grade (feeding chi_f and the forced-pair SAT test).
      What would falsify: if every projection of every accessible polytope is
      4-colourable and sparser than Moser+Moser, the family contributes no
      forced pair and the line is a construction census only.
status: refuted
killed-by: rescaling-only-killing-consideration-false (the file's own killing
      consideration — "projection only rescales, cannot create new unit
      relationships, never raises chromatic number" — is FALSE: a rank-2 linear
      map is not a homothety, it sends pairs of DIFFERENT source lengths to the
      same planar length. Explicit 24-cell counterexample: difference vectors
      (0,2,0,0) and (0,−1,1,0), source lengths 2 and √2, both project to
      squared norm 4 under rows a=(0,1,3,0), b=(0,0,0,1). Superseded by
      research/approaches/projection-distance-equalization.md, which adopts the
      corrected distance-equalization mechanism.)
precedent: The projection machinery is real and exact: projecting regular
      4-polytopes (24-cell {3,4,3}, 600-cell {3,3,5}, 120-cell {5,3,3}) onto
      planes along symmetry axes is a standard, well-studied operation.
      Chilton, "On the projection of the regular polytope {5,3,3} into a
      regular triacontagon", Canad. Math. Bull. 1964,
      https://doi.org/10.4153/cmb-1964-037-9 — the 120-cell and 600-cell
      project to a regular 30-gon (triacontagon) along the Petrie polygon in
      the plane; the 600-cell's 120 vertices / 720 edges live in Q(√5)
      (quaternionic representation), EXACTLY the field the candidate names.
      Al Ajmi, Koca & Bait Bu Salasel, "Projection of polyhedra onto Coxeter
      planes described with quaternions", SQUJS 19 (2015),
      https://doi.org/10.24200/squjs.vol19iss2pp77-90 — Coxeter plane
      projection method in quaternionic form (binary tetrahedral group = the
      24-cell's 24 vertices; the 600-cell vertex set), projecting to dihedral
      orbits of order 2h. Both confirm the step "all pairwise projected
      distances land in the run's exact quadratic/cyclotomic fields" and
      "the projected edge set is exactly the PP-distance-1 pairs."
      NULL precedent for the chromatic question: no located source applies
      these projections to computing the chromatic number of the projected
      unit-distance graph, and therefore none reports a 5-chromatic projected
      graph. This is honest absence: the mechanism is established, the
      application is novel/unrecorded.
      Killing consideration (structural, before any run): a linear projection
      π:R^d→R^2 only SCALES distances along the two image directions; every
      PP-distance and hence the entire unit-distance graph of the image is
      determined by the original pair distances and the projection plane. So
      the projection cannot create new "unit" relationships beyond stretching
      existing ones to length 1 — it can only rescale, never raise the
      chromatic number of what the full polytope already gives. The Moser
      spindle (7 vertices) is already 4-chromatic and 4-colourable; the run's
      Moser+Moser sums are already 4-colourable with no forced pair. A
      projected 24-cell/600-cell graph's unit-distance edges are a pure
      rescaling of the polytope's mutual distances to length 1 along two
      directions — it cannot require more colours than the corresponding
      planar configuration's chromatic number already is, and no one reports a
      5-chromatic projected graph. The honest claim is a construction census
      plus a forced-pair datum, not a 5-chromatic source.
bearing: A census line, not a bound line. Concretely it can (i) produce a new
      DENSE finite family (24-cell's 24 vertices / 600-cell's 120 vertices
      projected, 96 / 720 candidate unit edges) whose CHEAP, EXACT graphs the
      calibrated oracle can 4-colour and feed the forced-pair SAT harness — a
      genuinely new input into the crux `minkowski-rigidity` / `G-forced-pair-
      exists`, and one the run's Minkowski/spindle engine cannot express; and
      (ii) supply a fresh, independent calibration of the oracle on a rigid
      higher-dimensional source. Its value as a *5-chromatic* source is not
      established anywhere and the scalar-rescale argument makes one unlikely;
      the honest claim is a construction census + forced-pair datum for a new
      rigid family, in exact arithmetic.
first-step: Implement project_polytope(vertices, a, b) in exact arithmetic:
      read the 24-cell (24 vertices in R^4: all permutations of (±1, ±1, 0, 0),
      pairwise distances 0, √2, 2, √8) and the 600-cell vertex set (120 points,
      golden-ratio coordinates in Q(√5)), project along the Petrie/Coxeter plane
      (two symmetry axes) and along a small rational sweep of axis pairs, then
      run unit_graph(points) + chromatic_number(graph, 4) on each projection.
      Report the maximum edge density and chromatic number attained, and feed
      the densest projection to code/forced_pair.py. Expect chi = 4 throughout
      unless projection creates a genuine new 5-chromatic obstruction — which
      the rescale-only argument says it will not.
```
