# Scratch: H2 three-circle coincidence check (NOT EXECUTED)

This file was written as an analytic scratch check for the
`rigidity-matroid-henneberg-construction` research pass, but was **never run**
(no exec tool available in this run). It is kept as a reproducible sketch of
the intended verification, not as captured output.

## The claim it would verify (analytic, already settled by hand)

An H2 move in the unit-distance setting adds a new vertex w at distance 1 from
three prescribed existing vertices u, v, z. A point at distance 1 from all
three exists **iff** u, v, z are concyclic with circumradius exactly 1 — then w
is the circle's centre. Otherwise no such point exists.

- Two unit circles centred at u, v always co-intersect in up to two points:
  this is the **H1 move**, genuinely free (exact quadratic).
- Three unit circles centred at u, v, z co-intersect only in the circumradius-1
  coincidence: this is the **H2 move**, non-generic.

This is exactly the analytic finding recorded in
`research/approaches/rigidity-matroid-henneberg-construction.md` (caveat 2):
H2 does not eliminate the realizability oracle, it relocates it into a
coincidence query. The sympy code in this file would confirm the three test
cases by symbolic solve; the reasoning above is the step that matters and is
already recorded in the approach file.
