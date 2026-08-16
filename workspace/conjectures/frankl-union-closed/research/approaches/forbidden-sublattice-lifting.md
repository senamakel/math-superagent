# Birkhoff forbidden-sublattice (N₅/M₃) lifting of the abundant element

```approach
idea: In Poonen's lattice form, the only gap between the settled distributive
  case and general finite lattices is non-distributivity, and Birkhoff's theorem
  says non-distributivity is *locally witnessed*: a finite lattice is
  distributive iff it contains no sublattice isomorphic to the pentagon N₅ or
  the diamond M₃. Both N₅ and M₃ themselves satisfy UC in Poonen's form. For
  N₅ the only join-irreducible with |↑j| ≤ 5/2 is the top 1̂ (vacuous; see the
  verdict below — the inventor's claimed abundant join-irreducible b with
  |↑b|=2 does not exist); M₃ has each atom a,b,c with |↑a| = 2 ≤ 5/2. So try to
  *lift* the abundant join-irreducible of a forbidden sublattice to the whole
  lattice: show a minimal counterexample cannot contain a convex N₅/M₃ copy
  whose abundant join-irreducible fails to lift, then bootstrap.
mechanism: A minimal counterexample L (every join-irreducible j has
  |↑_L j| > |L|/2) is non-distributive, hence contains an N₅ or M₃ sublattice.
  In any such copy the "local" abundant element j₀ has |↑_copy j₀| ≤ |copy|/2.
  The filter ↑_L j₀ is obtained from ↑_copy j₀ by adding elements of L outside
  the copy; the lift fails exactly when those added elements push |↑_L j₀|
  above |L|/2. So either (a) the lift succeeds and L is not a counterexample —
  contradiction — or (b) every N₅/M₃ copy sits in L so "smashed" that its
  abundant join-irreducible gains many new upper elements. Classify the
  obstruction in case (b): it forces the abundant join-irreducible to be
  dominated by a specific large filter, and one can then either propagate the
  obstruction along a maximal chain or show it terminates at a second forbidden
  sublattice whose lift *does* succeed. This is a lifting/forbidden-sublattice
  argument, the same shape as the classical proofs for distributive, modular
  and geometric lattices, but driven by Birkhoff's N₅/M₃ dichotomy instead of
  by semimodularity.
status: refuted
killed-by: n5-lift-claim-false-as-stated — the inventor's kernel claim "N₅ has the join-irreducible b with |↑b| = 2 ≤ 5/2" is wrong for any labelling of the (unique) pentagon. Hand-verified (script code/out/n5_m3_joinirreducible_check.py written for tool_builder confirmation; both standard labellings agree; claim n5-m3-joinirreducible-filters): N₅ = (0<a<c<1, 0<b<c<1, a∥b) has join-irreducibles {a, b, 1} with principal-filter sizes |[a)|=3, |[b)|=3, |[1)|=1. The only join-irreducible with filter ≤ 5/2 is the TOP 1 (filter size 1, vacuous). The element c with |[c)|=2 is join-reducible (c=a∨b), not join-irreducible, so the "local abundant join-irreducible b of the N₅ copy" does not exist — the pentagon's own abundant join-irreducible is 1̂, whose filter is the whole copy, and lifting that is trivial/meaningless. M₃'s kernel is CORRECT (verified: each atom has filter {atom,1} of size 2 ≤ 5/2), so a restarted lift program could begin from M₃ or from a different abundant join-irreducible relative to the containing lattice — but the approach AS STATED, lifting the N₅ copy's b, is refuted on evidence. Precedent (Birkhoff N₅/M₃ dichotomy, and the settled distributive/modular/semimodular classes): all solid and supportive — non-distributive ⟺ contains N₅ or M₃ (Birkhoff/Dedekind), modular ⟺ no N₅ (Dedekind), and Frankl proven for modular (Abe–Nakano), lower semimodular (Reinhold), breadth≤2 (Joshi–Waphare), planar/semimodular (Czédli–Schmidt). No published "forbidden-sublattice lifting of an abundant join-irreducible" for UC was found (searched N₅/M₃ lifting join-irreducible union-closed; the related lattice-minimal-counterexample work, Bouchard arXiv:2503.00277, derives necessary conditions but does no N₅/M₃ lift).
precedent: n5_false_local (hand-verified, script code/out/n5_m3_joinirreducible_check.py); birkhoff-dichotomy (Medina–al. categorical characterization, Dedekind/Birkhoff, https://hdl.handle.net/10893/4916); abe-nakano-modular (https://research/summaries/abefrankl-abe-nakano-modular-1998.md); reinhold-lower-semimodular (https://research/summaries/reinhold-lower-semimodular-2000.md); joshiwaphare-breadth2 (https://research/summaries/joshi-waphare-semimodular-2019.md); czedli-schmidt-planar (https://research/summaries/czedli-schmidt-semimodular-planar-2008.md); bouchard-minimal (https://doi.org/10.48550/arxiv.2503.00277).
first-step: With the canonical oracle, enumerate the smallest lattices where the
  abundance minimum is tight or where UC is least comfortable (n ≤ 6 families),
  locate every convex N₅/M₃ sublattice, and test the lift claim: is there a
  case where the local abundant join-irreducible has |↑_L j₀| > |L|/2? Report
  the exact set of added upper elements — that is the obstruction this line must
  classify.
```

## Speculation, marked

That the lift always succeeds or forces a terminating propagation is my
speculation and is the open hinge. The non-speculative kernel is: (i) Birkhoff's
forbidden-sublattice characterization of distributivity, (ii) the explicit
abundant join-irreducibles of N₅ and M₃, and (iii) the exact "added upper
elements" obstruction, all of which are checkable with the oracle at small
size. Whether the obstruction can be classified is unknown and is what research
should probe (this is distinct from the refuted interval-doubling line, which
was about Day's construction and bounded lattices, not about N₅/M₃ copies).
