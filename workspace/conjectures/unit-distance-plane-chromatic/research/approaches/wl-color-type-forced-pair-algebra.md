# WL colour-type algebra for forced pairs

```approach
idea: Replace the per-pair SAT search for "forced monochromatic pairs" (the crux
`G-forced-pair-exists`) with the algebraic closure operator of the
Weisfeiler-Leman / colour-refinement hierarchy, equivalently the
(strong) k-consistency hierarchy of the k-colouring CSP and the pebble game.
For fixed k this refinement computes, in polynomial time, the coarsest stable
partition of V×V by "colour type": the set of ordered colour pairs (i,j) that
u,v can receive in some k-colouring. A pair is forced-equal iff its type
contains only diagonal pairs; forced-distinct iff only off-diagonal pairs.
status: refuted
killed-by: filter-not-a-bound-line (Cai-Furer-Immerman: no fixed WL dimension
  decides k-colourability, so the refinement can miss forced pairs and can never
  replace the complete SAT scan; at the run's sizes that scan already costs 0.1 s,
  so the pre-filter buys nothing; its one distinctive capability — the level-5
  forced-pair query toward chi >= 6 — is moot until the run holds a 5-chromatic
  base graph, which it does not. Not refuted as mathematics; closed as the adopted
  line because it produces no bound and its value is conditional on inputs the run
  lacks.)
first-step: Implement `wl_type(points, k)` over the exact field Q(sqrt3,sqrt11,sqrt33):
build the coloured complete graph on the Moser spindle and Moser+Moser, where each
pair carries its exact squared-distance label d=|u-v|^2 (edge iff d=1), run the
2-dimensional colour-type refinement to a fixpoint, and calibrate against the
run's complete SAT forced-pair scan (must reproduce: no forced pair in the spindle
or in Moser+Moser; and must certify the diamond's forced-equal tips at k=3). Then
run it ahead of `code/forced_pair.py` on every new construction.
mechanism: The run's one measured obstruction is that the spindle and one
Minkowski sum have no pair forced equal in every 4-colouring, and the only way it
knows this is one SAT call per candidate pair (256 queries on Moser+Moser). A
forced pair is exactly a "colour type" query, and colour-type refinement answers
ALL pairs at once as a sound over-approximation: seed the type of (u,v) by the
distance-graded relation (edge/non-edge plus the exact squared distance as a
colour label), then repeatedly refine so that whenever two pairs (u,v),(u',v')
cannot be distinguished by any combination of a common neighbour's type, they
are merged. This is a change of representation — the geometry is read only
through the distance-graded relation structure, i.e. a coloured complete graph,
not through coordinates — and it is the natural home of the forced-pair notion
rather than an ad hoc search. The refinement is sound but, by
Cai-Furer-Immerman, incomplete for k-colourability in general, so the exactness
gap is closed by a single SAT call on the boundary pairs the refinement flags;
the point is that most pairs are eliminated algebraically before any SAT. It
also degrades gracefully to the level-5 question (forced pairs in 5-colourings,
the resource needed to spindle up to chi>=6), which the current harness cannot
ask at all without a 5-colouring oracle.
precedent:
  - Weisfeiler-Leman / colour refinement: K. Weisfeiler & A. Leman, 1968; the
    k-WL hierarchy refines colourings of k-tuples to a stable (coherent)
    configuration. Sound, polynomial for fixed k. (Kiefer, "Power and limits of
    the Weisfeiler-Leman algorithm", RWTH thesis.)
  - Incompleteness: Cai, Fürer & Immerman, "An optimal lower bound on the number
    of variables for graph identification", Combinatorica 12 (1992) — no fixed k-WL
    decides all graphs (and equivalently no fixed k-consistency decides all
    colouring CSPs). Exactly the gap the candidate closes with SAT on boundary pairs.
  - CSP equivalence: Feder–Vardi, Kolaitis–Vardi; Atserias–Bulatov–Dalmau "On the
    power of k-consistency"; Berkholz "Lower bounds for existential pebble games
    and k-consistency tests" LMCS 9:4 (2013). k-consistency = sound polynomial
    test, complete iff the template's core has bounded treewidth (colouring does not).
  - claim sat-k-colourability-encoding (the exact SAT oracle this approach reuses
    for its boundary pairs); claim minkowski-sum-unit-distance-condition and
    sharp-nbhd-local (the geometry enters only through the distance-graded
    complete graph these certify).
grounded-by: wl-kconsistency-is-sound-polytime-incomplete
```

## Literature verdict

The reformulation is **real, correctly named, and its correctness
description is accurate.** The k-dimensional WL / colour-type refinement (equivalently
the k-consistency hierarchy of the k-colouring CSP) is: (a) sound — any pair it
certifies forced-equal is genuinely forced; (b) polynomial-time for fixed k; (c)
irreducibly **incomplete** for colouring in general (Cai–Fürer–Immerman: no fixed
k decides all; for CSPs k-consistency is complete exactly for templates whose core
has treewidth at most k, and colouring does not have bounded treewidth).

So the candidate's own two-step design — polynomial sound refinement, then a
single SAT call on the boundary pairs it flags — is exactly the correct way to
use k-consistency, and matches standard CSP practice (prune with local
consistency, then search). Its claim that this degrades gracefully to the
5-colouring / χ≥6 question is also correct: the dimension k in k-WL is not tied
to the number of colours, so the same refinement runs at C=5 where the run has
no complete 5-colouring oracle.

**Where the value is genuinely in doubt (say it plainly):** for the run's
*current* graphs the direct complete SAT scan is already nearly free — the
captured run (`code/out/forced_pair.captured.txt`) tests all 256 Moser+Moser
pairs at k=4 in 0.1 s. A polynomial pre-filter cannot beat that at this size,
and its incompleteness means it can *miss* forced pairs that the complete SAT
scan finds, so it must never replace the SAT oracle. The approach's advantage is
therefore only (a) cheaper pre-filtering over many *future* candidate base
graphs, and (b) the level-5 query the current harness cannot ask. Both are real
but neither is a theorem this run can currently claim. Honest status: grounded
as sound; its *value* is an open empirical question.

## Decision — grounded, with the incomplete/cost caveat recorded

The literature **supports** this as a legitimate, non-redundant line: correctly
named (WL / k-consistency), mechanism described accurately, and genuinely a
*different representation* from the run's one-SAT-call-per-pair scan (one
refinement answers all pairs, and reaches a level the colouring oracle cannot).
It does not re-propose a closed line.

Two caveats bound the claim. (1) **Incompleteness is the point of no return** —
the refinement is provably not complete for k-colouring (CFI), so it is a filter,
never a substitute; any "no forced pair" it reports is conditional. (2) **At
current graph sizes it buys little** over the 0.1 s SAT scan. Give it the
calibration it asks for (must reproduce the diamond's forced-equal tips at k=3
and no forced pairs in the spindle), then treat its real test as the level-5
question and the many-graph pre-filtering case — not the four graphs already
settled.

## Convergence decision — refuted (deferred as a line)

Closed in favour of the fractional-chromatic line. Not refuted as mathematics —
WL / k-consistency is sound and polynomial — but refuted as the run's next
adopted line: (i) CFI incompleteness means it can miss forced pairs and can
never replace the complete SAT scan, so any "no forced pair" it reports is
conditional and must still be confirmed by SAT; (ii) at the run's current sizes
the complete scan already costs 0.1 s, so the pre-filter buys nothing there;
(iii) its one distinctive capability, the level-5 forced-pair query toward
chi >= 6, is moot until the run holds a 5-chromatic base graph, which it does
not. Keep it on the shelf: it becomes the right tool the moment the run holds a
5-chromatic base and wants forced pairs in 5-colourings.
