# Shadow / compression / extremal-set theory on the complement family

```approach
idea: Work in the COMPLEMENT representation: G = {[n]\A : A ∈ F} is
  intersection-closed, and element x is abundant in F ⟺ x is in ≥ |F|/2 of the
  complements' complements... precisely: #F-sets containing x = |F| − #G-sets
  NOT containing x = |F| − (size of the subfamily of G in the hyperplane x∉S).
  So UC reads: some x lies outside ≤ |F|/2 members of G. The named tool is
  extremal-set / shadow theory — Kruskal–Katona, Macaulay, the LYM inequality,
  and Bollobás's theorem — applied to the rank layers of the intersection-closed
  family G (or, dually, the antichain of minimal sets of F). Union/intersection
  closure heavily constrains how many small sets a degree-constrained family can
  contain, and the shadow theorem converts "every degree < |F|/2" into a lower
  bound on |F| that grows past the trivial 2^{n−1} threshold in the regime where
  a minimal counterexample (|F| ≥ 51) is forced to live.
mechanism: This is the pre-entropy combinatorial line made rigorous, but with a
  concrete named engine the run has not used: instead of averaging over a weight
  function (which the CMS linear-average result shows fails), bound the *size of
  the k-shadow / the number of layers* forced by the degree profile. Compression
  (a left-compressed / shifted family with no larger degrees) reduces the search
  to nested/interval-shaped extremal families, which are jointly classified and
  checkable — the near-k-cube extremal profile [2^{k−2}+1 repeated, 1] already
  computed in this run is the boundary case. If every element has degree < |F|/2,
  the degree profile is "flat and below half", and the shadow/LYM bound forces
  either |F| past the trivial threshold (done) or a near-cube structure that
  itself contains an abundant element directly. This is a new representation
  (complement + shadows), distinct from entropy, lattice, and topological.
status: refuted
killed-by: complement-dual-is-known-shadow-bound — the complement (intersection-closed
  dual) is the classical statement of the conjecture (it is in the Bruhn–Schaudt
  survey and every standard source), and the Kruskal–Katona/LYM engine on it is
  not new to this problem: the pre-entropy literature already attacked UC through
  exactly these shadow and averaging techniques. In particular Reimer's theorem
  / the average-size and up-compression method (Balla–Bollobás–Eccles, JCTA 2013;
  the "Union-closed families of sets" paper) and Czédli–Maróti–Schmidt's averaging
  proved the density bound from which UC follows for very large families (|F| ≥
  2^{n−1}·something via {2/3}2^n in Eccles' stability form) — precisely the
  "shadow-forced lower bound on |F|" this approach proposes, and it is already
  known NOT to reach the regime where a counterexample lives (a counterexample
  has |F| < 2^{n−1}, Karpas `karpas-upper-shadow`/Eccles). The linear-average /
  weight-argument engine that actually does the work here is the very one the
  run has documented as failing for the general family (`cms-averaged-frankl-wrong`):
  the CMS averaging result shows pure degree/average profile constraints do NOT
  force abundance in general. So the named machinery is real, its application to
  UC is known and already optimised, and the forcing claim (shadow bound → |F|
  past threshold or near-cube) is the exact direction known to stop short. The
  residual (undocumented) sliver — a genuinely NEW shadow identity for
  intersection-closed families that no one has used — was not found; say plainly:
  no published application of Kruskal–Katona/Macaulay rings specifically to the
  UC abundance problem, beyond the averaging/size results above, was found.
precedent:
  - intersection-closed-dual, (Bruhn–Schaudt, The journey of the union-closed sets conjecture, arXiv:1309.3297 — the complement dual IS the stated intersection-closed form)
  - eccles-stability, (Balla–Bollobás–Eccles / Eccles, JCTA 2013, A stability result; UC for |F| ≥ (2/3)2^n)
  - cms-averaged-frankl-wrong, (Czédli–Maróti–Schmidt, On the scope of averaging for Frankl's conjecture, 2009 — the averaging/density engine fails)
  - karpas-upper-shadow, (Karpas, Two results on union-closed families, arXiv:1708.01434 — a counterexample has |F| < 2^{n−1})
  - reimer-average-size, (Reimer, An Average Set Size Theorem, Cambridge, 2003)
first-step: With the canonical oracle, for every UC family on n ≤ 5 compute the
  complement family G, its rank layers, and the degree profile; test the kernel
  inequality: does "all degrees ≤ |F|/2 − 1" force |F| ≥ 2^{n−1} (the trivial
  regime) OR force near-cube structure? Record the exact families that sit
  below the 2^{n−1} threshold with all degrees < |F|/2 — those are the only
  dangerous ones and their structural classification is the target. Apply the
  three negative controls to the complement/shadow formulation (2^[n] sits
  exactly at |F|=2^{n−1} with all degrees = |F|/2; a non-UC family breaks the
  shadow bound).
```

**Grounding verdict — REFUTED (as a novel route: the representation and its engine are the problem's classical, exhausted line).**

What the reformulation is actually called: this is precisely the *intersection-closed dual* form of Frankl's conjecture (take complements), which the Bruhn–Schaudt survey and every standard reference state as an equivalent conjecture; and the named engine, Kruskal–Katona / LYM / shadows plus up-compression, is the classical pre-entropy toolset of the problem. It is not a representation this run "has not used" so much as the historical starting point.

Hypotheses: Kruskal–Katona and LYM apply to arbitrary set families by rank, so their hypotheses (finite, uniform rank layers) hold here; Macaulay/LYM give sharp bounds on shadow sizes. But — the decisive check — the *forcing step* this approach depends on ("every degree < |F|/2 forces |F| past the trivial threshold, or near-cube structure") is the direction the literature has already optimised and found to stop short: the best such bound (average-size / up-compression, Reimer 2003; Balla–Bollobás–Eccles, JCTA 2013; solved by Eccles' stability form) gives UC only for |F| ≥ (2/3)2^n, while a counterexample must have |F| < 2^{n−1} (Karpas). The gap 2^{n−1} to (2/3)2^n is precisely where a counterexample lives and where the shadow/average engine cannot reach.

Application to this problem: the averaging/weight engine that the shadow approach is built to strengthen is the very mechanism the run has documented as failing in general — `cms-averaged-frankl-wrong` shows the averaged / pure profile constraint does not force abundance for all union-closed families. Since the complement+shadow formulation reduces to *that* engine, the recorded failure applies directly. I found no published application of a genuinely new shadow/Macaulay identity (beyond the size/averaging results above) that forces UC abundance — state plainly: could not find one, so the "new identity" claim in the mechanism is unsupported, not refuted by a named counter-reading.

What it would buy: a re-derivation of known, weaker results. Do not re-propose the shadow/average line as written; any continuation would have to be a genuinely new identity, which was not found.
