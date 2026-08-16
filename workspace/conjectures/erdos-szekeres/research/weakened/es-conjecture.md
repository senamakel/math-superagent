# Erdős–Szekeres conjecture — ladder of weakened versions

```ladder
goal: For every n >= 4, every set of 2^(n-2)+1 points in general position in the
      plane contains n points in convex position (the upper-bound direction of the
      Erdős–Szekeres conjecture ES(n) = 2^(n-2)+1). General position = no three
      collinear; "n points in convex position" = they are the vertex set of their
      own convex hull, not necessarily consecutive on the hull of the whole set.
difficulties: unbounded n, zero slack, arbitrary order type, stability/uniqueness, search intractability, realizability gap
status: open
```

```rung
id: R-oracle-small-n
statement: Reproduce the exact values ES(3)=3, ES(4)=5, ES(5)=9, ES(6)=17 with this
      run's own tools: an exact integer/rational orientation oracle deciding general
      position and reporting the largest convex subset, validated by hand against
      ES(4)=5 and ES(5)=9; exhaustive enumeration over Aichholzer order types
      (realizable, n <= 10) where applicable; and for n = 6 a SAT encoding that first
      reproduces the 16-point negative (a 16-point general-position set with no convex
      6-gon) before any UNSAT is trusted.
off: unbounded n, search intractability, realizability gap
stance: open
merge: The oracle and encoder, once reproducing the known answers, are frozen. To
      climb to R-one-interior, keep the exact constant 2^(n-2)+1 but take it to all
      n under the hypothesis "at most one interior point"; the move is a hull-count
      argument — the hull of a (2^(n-2)+1)-point set with <= 1 interior point has at
      least 2^(n-2) >= n vertices, and those already form a convex n-gon.
```

```rung
id: R-one-interior
statement: For every n >= 4, every set of 2^(n-2)+1 points in general position with at
      most one interior point (a point strictly inside the convex hull of the set)
      contains n points in convex position.
off: arbitrary order type, stability/uniqueness
stance: open
merge: Admit k interior points. The hull then has 2^(n-2)+1-k vertices, so the
      trivial hull argument dies exactly when k > 2^(n-2)+1-n; from there the first
      move is to bound, for each interior point, how many hull vertices it can remove
      from the usable convex n-gon, and to induct on k.
```

```rung
id: R-k-interior
statement: For every n >= 4 and every fixed k >= 0, every set of 2^(n-2)+1 points in
      general position with at most k interior points contains n points in convex
      position. (True and trivial for k <= 2^(n-2)+1-n; the content is the regime
      where the hull has fewer than n vertices and interior structure matters.)
off: arbitrary order type, stability/uniqueness
stance: open
merge: Lifting the interior-point bound entirely means handling sets whose hull is
      small but whose interior is deep — exactly an onion of nested convex layers.
      The move is an onion-peeling induction that counts how many layers a set is
      forced to have before a convex n-gon appears; that is the entry into R-h-layers.
```

```rung
id: R-h-layers
statement: For every n >= 4 and every fixed h >= 1, every set of 2^(n-2)+1 points in
      general position whose onion (convex-layer / repeated-hull) depth is at most h
      contains n points in convex position.
off: arbitrary order type, stability/uniqueness
stance: open
merge: Dropping the layer bound is exactly admitting the Erdős–Szekeres 1960
      construction, whose recursive union of n-1 blocks has depth growing with n and
      no convex n-gon at 2^(n-2) points. The first move is to show any extremal
      (2^(n-2)-point, convex-n-gon-free) set has layer depth at least some function
      g(n), and then to check whether depth < g(n) already forces the convex n-gon —
      that is where "arbitrary order type" turns back on in full.
```

```rung
id: R-es7-computational
statement: ES(7) <= 33: no set of 33 points in general position lacks a convex 7-gon.
      Established by a SAT/CP-SAT encoding of the orientation variables with the
      signature/transitivity axioms, whose encoder has first been made to reproduce
      ES(5)=9 and the 16-point negative for n=6; the search is over realizable order
      types (or exact rational coordinates) with a stated symmetry reduction and an
      argued isomorph-rejection method, and an empty result rules out exactly the
      33-point counterexample.
off: unbounded n, realizability gap
stance: open
merge: Going from ES(7) to all n requires turning the finite certificate into a
      uniform argument. The move is to extract from the n=7 proof a structural lemma
      (a forced subconfiguration or a counting invariant) that generalizes to n, then
      induct — this is precisely the step where "zero slack" and "stability/uniqueness"
      turn back on, and it is the hardest merge on the ladder.
```

```rung
id: R-factor-two
statement: For every n >= 4, every set of 2^(n-1)+1 points in general position contains
      n points in convex position — i.e. ES(n) <= 2^(n-1)+1, the conjecture with the
      exact constant relaxed by a factor of two. This does not imply the conjecture;
      it is a fixed-constant bound strictly stronger than any published 2^(n+o(n))
      form once it holds for all n.
off: zero slack
stance: open
merge: To remove the factor two, the argument must stop paying for the two halves of
      the cups-and-caps decomposition independently (the binomial pays C(2n-4,n-2)
      ~ 4^n, the conjecture needs no factor at all). The first move is to locate, in
      whichever counting argument yields 2^(n-1), the single place the factor of two
      enters and show that a set attaining it must already contain a convex n-gon.
```

```rung
id: R-extremal-structure
statement: Any set S of 2^(n-2) points in general position with no convex n-gon has
      convex hull of size at most n-1, hence at least 2^(n-2)-(n-1) interior points;
      in particular every such extremal set has nonempty interior for n >= 5. The open
      part: how the interior points must be distributed — e.g. whether the two
      outermost layers must come close to the block sizes of the Erdős–Szekeres
      construction, and which subconfigurations S is forced to avoid. (A structural
      constraint on a hypothetical extremal set, not an assertion of the bound.)
off: zero slack
stance: open
merge: Turning a structural constraint into the bound is exactly the
      stability/uniqueness step: show the Erdős–Szekeres construction is the
      essentially unique extremal set and any deviation from it already forces a
      convex n-gon. The first move is to take the hull-size bound and ask whether the
      hull plus second layer together avoid a convex n-gon only if they match the two
      outermost blocks of the construction.
```

```rung
id: R-conjecture
statement: For every n >= 4, every set of 2^(n-2)+1 points in general position
      contains n points in convex position — the full Erdős–Szekeres conjecture.
off: 
stance: open
merge: This is the goal itself; the ladder is exhausted exactly when every rung above
      is settled and each merge has been carried through to here.
```
