# Cut-and-project (Meyer) sets for a non-periodic 6-colouring

```approach
idea: Attack the upper bound χ ≤ 6 with a class of colourings strictly larger
      than the lattice-periodic ones: colour the plane via a cut-and-project
      (model/Meyer) set M ⊂ R^2, whose colouring rule lives on a *finite window*
      in internal space rather than on a flat torus. Periodic lattices are the
      special case; a Meyer set with a genuinely aperiodic (but
      finite-window-defined) colouring is a search object the flat-torus line
      cannot express.
mechanism: A cut-and-project set is M = { π_∥(x) : x ∈ L, π_⊥(x) ∈ W }, where
      L ⊂ R^4 is a lattice, π_∥ the projection onto physical R^2, π_⊥ onto
      internal R^2, and W ⊂ R^2 a bounded "window." The distance between two
      points of M is determined by their internal coordinates (the "star-map"
      rigidity), so the unit-distance relation — and hence the constraint that
      two points receive distinct colours — can be checked *exactly* in the
      finite internal space, not the continuum. Concretely, colouring M by
      "cell colour = colour of the point in M nearest its cell centre"
      (the run's existing thickening/margin lemma, reused from
      flat-torus-periodic-6col) reduces "6-colour the plane from M" to: find a
      6-colouring of the *finite* window partition such that every same-colour
      pair of window cells has physical distance strictly bounded away from 1.
      The window is a finite object (a convex polygon subdivided by the
      lattice's internal structure), so the search is finite and the margin is
      computed exactly. The named mathematics: the cut-and-project method,
      Meyer sets / model sets, substitution tilings (Penrose is a 5-fold
      example), and aperiodic order. This is a genuine generalisation of the
      adopted flat-torus line: a periodic lattice is the cut-and-project set
      with a single-point window, so the torus search is the window={pt} corner;
      a non-trivial window is a strictly richer family, and the board's recorded
      bug/dead-end on the torus line is exactly a reason to widen the class.
      SPECULATIVE part, stated as such: whether a non-periodic Meyer colouring
      can beat 7 colours at all, and whether the discrete set M is dense enough
      that its colouring extends to the whole continuum with positive margin, are
      both open — the proposal's certain value is a well-defined finite search
      object for the unstructured upper-bound side, plus a machine-checkable
      negative datum ("no Meyer-set 6-colouring with margin > 0") if the search
      exhausts a stated window class.
status: refuted
killed-by: inherits-torus-continuum-gap (the continuum-extension/margin step
      that bug-blocked flat-torus-periodic-6col is inherited wholesale —
      colouring the countable Meyer set does not colour R^2, and the
      thickening/margin lemma needs the bound on every cell; value is
      conditional on settling that step first, and the line is the superclass
      of the already-adopted-and-blocked torus line rather than independent of
      it. The run's live crux is on the lower-bound construction side. Closed
      in favour of projection-distance-equalization.)
precedent: The cut-and-project / model set mechanism is fully established in
      aperiodic order: a CPS is a lattice L ⊂ R^(d1+d2), physical space R^d1,
      internal space R^d2, window W ⊂ R^d2, with model set
      M = { π_∥(x) : x ∈ L, π_⊥(x) ∈ W }; every model set is a Meyer set, and
      a relatively dense set is a Meyer set iff it is contained in a model
      set. Standard treatments: Moody (the term "model set"), and e.g.
      Iizuka–Akama–Akazawa, "Asymmetries of cut-and-project sets and related
      tilings", IIS 2009, https://doi.org/10.4036/iis.2009.99 — defines CPS
      with physical/internal spaces, window relatively compact with non-empty
      interior, and notes model sets are Meyer sets; the n-gonal (n=5,8,10,12)
      quasilattices are exactly the 2D cut-and-project sets the candidate
      names (Penrose 5-fold, Ammann–Beenker 8-fold); LRDL + Moody + Baake
      give the general CPS/model-set framework and window-rigidity of
      distances (the star-map rigidity the candidate's exactness rests on).
      (The canonical reference texts are not retrievable through this
      network boundary — recorded in FRONTIER.md — but the framework is
      confirmed by the technique-level sources above and is standard.)
      Structural relation to the adopted flat-torus line is correct: a
      single-point window degenerates to a periodic lattice colouring, so the
      Meyer family strictly contains the periodic family, exactly as claimed.
      NULL precedent: no located source colours the WHOLE plane from a
      nontrivial model-set window, and none resolves whether a Meyer/aperiodic
      6-colouring exists — that is precisely the open question, and its
      resolution would move the upper bound, so its absence is the honest
      state of the art, not a gap in the search.
      Killing consideration (structural, not found-but-absent): (i) the open
      problem is whether 6 colours can colour ANY one set of dense points —
      the current record uses a periodic lattice and reaches only 7; nothing
      in the cut-and-project formalism supplies a 6-colouring, it merely widens
      the search class. (ii) The candidate inherits the flat-torus line's
      continuum gap wholesale: colouring the countable Meyer set M does NOT
      colour R^2; the thickening/margin lemma (colour radius-ρ cells by a
      nearest M-point's colour, require same-colour centre distance > 1+2ρ)
      needs M relatively dense AND the margin to hold for EVERY cell — the
      exact gap that recorded the flat-torus line as bug-blocked. (iii) By
      de Bruijn–Erdős it suffices to find a finite forbidden configuration to
      show chi>6, but a cut-and-project set is Delone (relatively dense +
      uniformly discrete), so its finite excerpts look arbitrarily dense and
      the "window cell" approximation of the margin is the whole difficulty.
bearing: A sound, strictly-wider search class on the UNSTRUCTURED upper-bound
      side — the side where any 6-colouring (periodic or not) is an open,
      high-value result and would be a machine-checked deliverable directly.
      Its concrete deliverables are (i) a 6-colouring with positive margin from
      a Meyer/window scheme (would be a major result), or (ii) a negative
      no-Meyer-set-6-colouring-within-a-stated-window-class datum (a census
      fact about the search, quotable). It is NOT independent of the adopted
      flat-torus line — it is its superclass — so it does not de-risk the
      blocked torus line; if the torus approach cannot extend to the
      continuum, the Meyer variant faces the same gap. Value is therefore
      conditional on solving (or bounding) the continuum-margin step first.
first-step: Build code/lib/meyer_set.py: for the 5-fold (Penrose) and 8-fold
      (Ammann–Beenker) cut-and-project schemes with a square/decagon window W,
      enumerate the window's sub-cells (projections of lattice points landing
      in W), compute each pair's physical squared distance as an exact
      quadratic form in the projection parameters, and SAT-test for a 6-colouring
      of the resulting finite conflict graph with the margin condition
      |u−v|^2 > (1+2ρ)^2 for same-colour cells. Calibrate on the known
      hexagonal-lattice 7-colouring (must reproduce 7, not 6, for the A2 lattice
      window={pt}), then sweep window sizes/rotations at k = 6. The step that
      must come first and is the real blocker: settle the continuum-extension
      (margin) step that bug-blocked the flat-torus line, because the Meyer
      generalisation inherits it.
```
