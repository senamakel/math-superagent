# Erdős–Szekeres conjecture — ladder of weakened versions

```ladder
goal: For every n >= 4, every set of 2^(n-2)+1 points in general position in the
      plane contains n points in convex position (the upper-bound direction of the
      Erdős–Szekeres conjecture ES(n) = 2^(n-2)+1). General position = no three
      collinear; "n points in convex position" = they are the vertex set of their
      own convex hull, not necessarily consecutive on the hull of the whole set.
difficulties: unbounded n, zero slack, arbitrary order type, stability/uniqueness, search intractability, realizability gap, adversarial extremal set
status: open
```

The ladder below is ordered weakest first (bottom of the ladder = top of the
file after this header). A `settled` stance means the run has already
established the statement — by machine (the run's own exact oracle) or by source
(a theorem in the library). A settled-rung reason names which claim or source
establishes it, so a reader can check. Rungs are listed weakest first to climb.

Two structural facts discipline this ladder. Both say: **the interior-count and
layer-depth axes are content-free except in the deep, small-hull regime** —
i.e. except where a set is shaped like the Erdős–Szekeres extremal construction.

1. *Interior-count collapse.* With at most k interior points a set of N=2^(n-2)+1
   points has at least N-k hull vertices, and any n hull vertices of a
   general-position set are in convex position. So the hull alone forces a convex
   n-gon for the whole range k <= 2^(n-2)+1-n. R-one-interior (k=1) and the easy
   tail of R-k-interior are therefore theorems, not content; the interior axis
   only engages where the hull has fewer than n vertices.
2. *Layer-depth collapse.* Every onion (convex) layer is itself a set in convex
   position, so a set of layer depth h whose largest layer has >= n points already
   contains a convex n-gon. The largest layer is at least N/h, so depth h is
   trivial while h <= 2^(n-2)/n. The layer axis only engages when the layers are
   all small, i.e. when the set is many-layered and deep.

Both facts point the same way: the difficulty that actually bites is not "a few
interior points" or "few layers" — it is the *recursive deep structure* of a set
whose hull is small and whose interior is a nested onion, which is precisely the
Erdős–Szekeres 1960 construction and its affine relatives. Structure (which a set
avoids, how the layers interlock) carries the weight, not depth or interior count.

```rung
id: R-speedrun-exact-small-n
statement: ES(3)=3, ES(4)=5, ES(5)=9, ES(6)=17. The run's own exact-arithmetic
      oracle (lib/es_geom, integer/rational determinants, never float) decides
      general position and reports the largest convex subset and the cup/cap
      spectrum, and the verified es_construct 2^(n-2)-point lower-bound set is
      confirmed to have largest convex subset n-1 at n=4,5,6 (no convex n-gon)
      and no convex 7-gon at n=7.
off: unbounded n, arbitrary order type, stability/uniqueness, search intractability, adversarial extremal set, realizability gap
stance: settled
merge: This rung is the frozen oracle (GOAL criterion 3), verified by
      build-oracle / disambiguate-es-lower-set; the exact constants are the
      library claim es-exact-values (proved). Climbing past it keeps the exact
      constant 2^(n-2)+1 and takes n to all integers, switching "unbounded n"
      back on first. The cheap first step up is a hull count: a set of 2^(n-2)+1
      points with <= 1 interior point has >= 2^(n-2) >= n hull vertices, which
      already give a convex n-gon — this is the collapse of Fact 1 and is the
      next rung.
```

```rung
id: R-one-interior
statement: For every n >= 4, every set of 2^(n-2)+1 points in general position with
      at most one interior point (a point strictly inside the convex hull of the set)
      contains n points in convex position.
off: arbitrary order type, stability/uniqueness, adversarial extremal set
stance: settled
merge: SETTLED AS TRIVIAL, not content. A set with at most one interior point has at
      least 2^(n-2) >= n hull vertices (equality only at n=4), and any n hull
      vertices of a general-position set are in convex position, so the statement is
      true with margin. The refuter proved it both by this one-line hand argument
      (tightest case n=4 is ES(4)=5, itself a proved library claim) and by machine:
      an n=4 TPTP fragment over the full Knuth CC axioms returned SZS Theorem (no
      countermodel even abstractly); the only "refuted" diagnostic was the weak
      axioms-1-3 fragment admitting a non-realizable abstract chirotope at n=5 —
      confirming the realizability gap, not this rung. Evidence:
      research/weakened/R-one-interior-refutation-report.md. The interior axis does
      not begin to matter until k >= 2, i.e. R-k-interior with the hull below n
      vertices.
```

```rung
id: R-k-interior
statement: For every n >= 4 and every fixed k >= 0, every set of 2^(n-2)+1 points in
      general position with at most k interior points contains n points in convex
      position. Content only in the regime where the hull has fewer than n vertices;
      the whole range k <= 2^(n-2)+1-n is settled by the hull alone (Fact 1).
off: arbitrary order type, stability/uniqueness
stance: open
merge: The hull argument (Fact 1) settles everything up to k = 2^(n-2)+1-n. The only
      content is k large enough that the hull drops below n vertices while the set
      still has 2^(n-2)+1 points — at n=5 the first such case is k >= 5 (9 points,
      <= 4 hull vertices, 5 interior). That is not really "a bounded number of
      interior points" anymore; it is a set whose hull is small and whose interior
      is deep. The next step is to enumerate those first small regimes exactly
      (n=4, hull>=3; n=5, k>=5) as machine targets, then climb toward the deep
      interior by switching "adversarial extremal set" back on — interior points
      are where the recursion of the ES construction lives.
```

```rung
id: R-h-layers
statement: For every n >= 4 and every fixed h >= 1, every set of 2^(n-2)+1 points in
      general position whose onion (convex-layer / repeated-hull) depth is at most h
      contains n points in convex position. Content only for h large (deep sets);
      h <= 2^(n-2)/n is settled by Fact 2.
off: arbitrary order type, stability/uniqueness, adversarial extremal set
stance: open
merge: Every onion layer is convex (Fact 2), so the largest layer of an h-layered
      set has >= 2^(n-2)/h points and gives a convex n-gon whenever that is >= n.
      The content is the deep regime h > 2^(n-2)/n — exactly where a set is built
      like the Erdős–Szekeres construction (n-1 nested blocks, depth growing with
      n, no convex n-gon at 2^(n-2) points). The first move: show any extremal
      2^(n-2)-point convex-n-gon-free set has depth at least some function g(n),
      and check whether depth < g(n) already forces the n-gon. This is where
      "arbitrary order type" turns back on in full, and where the checked claim
      es-construct-layer-extremality (each onion layer of the extremal template is
      itself maximally convex) becomes the tool.
```

```rung
id: R-4set-supersaturation
statement: Every ordinary n-avoiding set S of 2^(n-2) points in general position (no
      convex n-gon) contains a minimum number NNC(N) of non-convex 4-subsets, and
      the Erdős–Szekeres construction es_construct attains (or is within a stated
      factor of) this minimum. Because a set is in convex position iff every one of
      its 4-subsets is (the 4-point criterion, library claim es35-four-criterion),
      every n-subset of an n-avoiding S contains at least one non-convex 4-subset,
      forcing the covering bound NNC(N) * C(N-4,n-4) >= C(N,n). The weakened target
      is the *supersaturation* direction: how much above this automatic minimum NNC
      must be, as a structural constraint on n-avoiding sets, with the known
      construction as the extremal candidate.
off: unbounded n, zero slack, stability/uniqueness, adversarial extremal set
stance: open
merge: This rung is attackable today with the exact oracle (lib.es_geom): count
      NNC(N) exactly on es_construct at n=5,6,7 (N=8,16,32) and test the covering
      bound and its sharpness, then lift to the Karolyi–Toth twin and Aichholzer
      order types — the second family is what makes it a statement about n-avoiding
      sets rather than one placement. It is the head-of-queue task
      con4-supersat-nnc-count. It does not imply the bound (it is a structural
      lower bound on a density, not a pigeonhole over sets); climbing to the next
      difficulty — "zero slack" — means turning the forced large NNC into a forcing
      of the convex n-gon itself, which is the missing step every counting argument
      in this problem shares.
```

```rung
id: R-split-k-gon
statement: For every n >= 4, every set of 2^(n-2)+1 points in general position
      contains a "split n-gon" (the Baek–Balko vertex-2-coloring notion), and
      2^(n-2)+1 is exactly the threshold: some 2^(n-2)-point set has no split n-gon.
off: zero slack, stability/uniqueness, adversarial extremal set
stance: settled
merge: This is the Baek–Balko theorem (claim baek-balko-split: ESsplit(k)=2^{k-2}+1
      proved exactly for every k >= 2; evidence: proved per the SoCG 2025 summary,
      with the abstract analogue over all 2-colorings of ordered K^3_N also exact).
      It shows the exact constant survives under a relaxed "convex" notion, strong
      evidence the 2^(n-2)+1 candidate is right and that the difficulty lives
      specifically in convex-position versus split condition. Turning "zero slack"
      back on is precisely the convex-vs-split gap. No proof text is yet held (only
      the SoCG summary), so treat as load-bearing but re-verify against the full
      document before building a merge on it.
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
merge: To remove the factor two, an argument must stop paying for the two halves of
      the cups-and-caps decomposition independently (the binomial pays ~4^n, the
      conjecture needs no factor). First move: locate in whichever counting
      argument yields 2^(n-1) the single place the factor of two enters and show a
      set attaining it must already contain a convex n-gon. Caution: R-split-k-gon
      is settled, so a counting bound must be sharpened against a set that avoids a
      convex n-gon but still contains split n-gons — the extra slack is real, not
      an artefact.
```

```rung
id: R-es7-computational
statement: ES(7) <= 33: no set of 33 points in general position lacks a convex 7-gon.
      Established by a SAT/CP-SAT encoding of the orientation variables with the
      signature/transitivity axioms, whose encoder has first been made to reproduce
      ES(5)=9 and the 16-point negative for n=6; search over realizable order types
      (or exact rational coordinates) with a stated symmetry reduction and an argued
      isomorph-rejection method; an empty result rules out exactly the 33-point
      counterexample.
off: unbounded n, realizability gap
stance: open
merge: Going from ES(7) to all n requires turning the finite certificate into a
      uniform argument: extract from the n=7 proof a structural lemma (a forced
      subconfiguration or a counting invariant) that generalizes to n, then
      induct — the step where "zero slack" and "stability/uniqueness" turn back on,
      the hardest merge on the ladder. Not yet begun: the run's own SAT encoder has
      not yet reproduced the k=6 cap (task es-nogon-k6-rung is open), so this rung
      is not attackable until that reproduction exists. Note the run already has
      machine evidence that a universal search is out of reach (order-type counts
      at 32 points are astronomical), and that the abstract all-colorings analogue
      FAILS at k=7 (balko-valtr-refutes-PS assertion: red-blue colorings of K^3_33
      with no 7-gon), so the search must be over realizable/pseudolinear colorings,
      not all abstract chirotopes.
```

```rung
id: R-decomposable
statement: For every n >= 4, every decomposable set of 2^(n-2)+1 points in general
      position contains n points in convex position, where a decomposable set is one
      built recursively from the ES construction's block structure (Baek–Balko
      definition).
off: arbitrary order type, stability/uniqueness, adversarial extremal set
stance: settled
merge: This is the Baek–Balko decomposable theorem (claim baek-balko-decomposable:
      the conjecture holds for decomposable sets; evidence: asserted per summary,
      full proofs not yet held — JCTA 2026, DOI 10.1016/j.jcta.2026.106195). It
      settles the conjecture on exactly the recursive-block class the search space
      most resembles. The open gap is "arbitrary order type" outside this class —
      where the ES construction itself sits and where every structural rung above
      lands. Until the full text is held, verify the precise definition of
      "decomposable" before treating the merge as safe.
```

```rung
id: R-extremal-structure
statement: Any set S of 2^(n-2) points in general position with no convex n-gon has
      convex hull of size at most n-1, hence at least 2^(n-2)-(n-1) interior points;
      in particular every such extremal set has nonempty interior for n >= 5. The
      open part: how the interior points must be distributed — e.g. whether the two
      outermost layers must come close to the block sizes of the Erdős–Szekeres
      construction, and which subconfigurations S is forced to avoid. (A structural
      constraint on a hypothetical extremal set, not an assertion of the bound.)
off: zero slack
stance: open
merge: Turning a structural constraint into the bound is the stability/uniqueness
      step: show the Erdős–Szekeres construction is the essentially unique extremal
      set and any deviation already forces a convex n-gon. First move: take the
      hull-size bound (hull <= n-1 so a convex n-gon cannot be read off the hull
      alone — this is the one place the interior/layer axes genuinely engage, Fact 1)
      and ask whether the hull plus second layer together avoid a convex n-gon only
      if they match the two outermost blocks of the construction. The run's checked
      claims (es-construct-layer-extremality, es-construct-block-tightness,
      layer-profile-outer-hull-one-per-block) pin down these outer structures on the
      confirmed template; the task is to lift them off the placement.
```

```rung
id: R-conjecture
statement: For every n >= 4, every set of 2^(n-2)+1 points in general position
      contains n points in convex position — the full Erdős–Szekeres conjecture.
off: 
stance: open
merge: This is the goal itself; the ladder is exhausted exactly when every rung above
      is settled and each merge carried through to here.
```
