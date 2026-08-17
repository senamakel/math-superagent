# Pattern-finder analysis: sequence structure in the ES construction data

Role round: pattern-recognition on the run's computed data (`es_construct`,
the verified 2^{n-2}-point no-convex-n-gon set). Exact tools only.

## The one clean, checked sequence: full-transversal count = A001142

The number of full transversals (exactly one point from each block T_0..T_{n-2})
of `es_construct` equals the product of the block sizes,

    T(n)  :=  prod_{i=0}^{n-2} C(n-2, i)  =  OEIS A001142(n-2)

   n=4: 2,  n=5: 9,  n=6: 96,  n=7: 2500,  n=8: 162000,  n=9: 26471025.

The equality is not a "fit": it holds because **every** full transversal lies in
convex position.  Verified exactly (`lib.es_geom.in_convex_position`,
Fraction arithmetic) for ALL transversals at n=4..9 — including the full
26,470,125 at n=9, with zero non-convex.  Structural cause: the outer hull of
`es_construct` is one point per block in block order (Conjecture A, PASS at
n=5,6,7), so any transversal is seen hull-extreme in order and is convex.
Status: checked (out-of-sample n=8, n=9 survived a deliberate break attempt).

## Sequence that is NOT in OEIS and shows no closed form — a real miss

The distinct (n-1)-convex-subset counts,

   n=4: 4,  n=5: 38,  n=6: 802,  n=7: 39648

are not catalogued (OEIS lookup: no match) and over four terms show no
polynomial/low-order recurrence (the order-2 recurrences the tool fits are
arbitrary rationals over 4 points — meaningless).  C(128,7) ~ 10^12 makes n=8
infeasible, so this sequence stops at four terms with no derivable regularity.
Recorded so nobody re-searches.

## Structural regularities confirmed exactly on the maximal-convex patterns

- The full-transversal diagonal (1,1,...,1) has count prod C(n-2,i): 9/96 at
  n=5/6 — consistent with transversal-convexity (above).
- The block-index pattern-count distribution is **reversal-symmetric**: the
  count of a pattern equals the count of its reversal i -> (n-2)-i.  PASS at
  n=5,6 (every pair).  This is the reflection symmetry of the construction.

## Non-regularities (recorded so nobody re-derives them)

- gsplit valid-split counts [6,4,2,0] at n=4..7: the constant-difference
  fit is a small-domain artifact, not structure.  The genuine fact is the
  scoped 4/2/0 decay at n=5/6/7 (template only).
- The convex-layer (onion) profiles [3,1],[4,4],[5,5,3,3],[6,6,6,5,6,3] are a
  placement artifact of the radial arc, not the binomial block structure
  (established elsewhere; Conjecture C layer-extremality PASSes n=5,6,7).

## Conjecture worth deriving

**Transversal-convexity / A001142.** That every full transversal is convex is a
conjecture (exact evidence n=4..9, structural expectation from Conjecture A).
First falsifier: a non-convex transversal at any n.  It would follow from a
stronger, placement-invariant statement: any set on a strictly-convex arc with
one strictly-convex subcopy per block has all transversals convex — i.e. the
property is structural to the ES template, not to these coordinates.  Whether
it extends to ALL no-convex-n-gon sets (an upper-bound-leaning direction) is
open and is exactly the kind of claim that would bear on GOAL item 4.
