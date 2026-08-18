# Pattern pass: 6-parameter general-quadratic-focus focal values — exact audit

Ran: `code/sequence_6param_audit.py` (exact recount of on-disk dumps),
`code/sequence_6param_symmetry_probe.py` (exact involution enumeration),
`code/bautin/denom_mechanism_probe.py` (exact rational matrix inverses).
All exact integer/rational arithmetic; no floats. This is the first pattern
pass to examine the 6-parameter family — every prior audit covered only the
5-parameter chart family.

## Family and data provenance

General quadratic focus (linear centre part), six coefficients:

    u' = -v + a1 u^2 + a2 u v + a3 v^2
    v' =  u + b1 u^2 + b2 u v + b3 v^2
    rot(p) = -v p_u + u p_v,  V2 = (u^2+v^2)/2,  gauge c_{d,0} = 0,
    L_d = even-degree radial obstruction (d-th focal value), homogeneous of
    degree h = d-2 in (a1,a2,a3,b1,b2,b3).

Monomial counts a6_d of L_d (exact):
  d=4:  6   (bautin_focal_values.captured.txt, printed inline "monomials: 6")
  d=6: 56   (same capture, "monomials: 56")
  d=8: 220  (same capture, "monomials: 220")
  d=10: 628 (focal_6coeff_L10.txt, recounted by this pass from the raw term list)
  d=12: 1481 (focal_6coeff_L12.txt, recounted by this pass from the raw term list)

## Exact structural facts (all verified by the audit program)

With h = d-2 and dim6(h) = C(h+5,5) (degree-h monomials in 6 variables):

    h    2    4    6    8   10
    a6   6   56  220  628 1481
    dim  21  126  462 1287 3003
    c6 = dim - 2*a6 = 9, 14, 22, 31, 41

- Neither a6 nor c6 is a low-degree polynomial (analyze_sequence: differences
  do not stabilise within the supplied terms).
- No constant-coefficient linear recurrence of order <= 4 fits either
  sequence (find_linear_recurrence, exact).
- OEIS: no match for [6,56,220,628,1481] and no match for [9,14,22,31,41]
  (recorded so nobody searches again).

## Conjecture (exact fit, 4 of 5 terms — NOT established)

    c6(h) = (h^2 + 22 h + 8)/8   for even h >= 4,
    equivalently a6_d = (C(h+5,5) - (h^2+22h+8)/8)/2.

Holds EXACTLY for h = 4, 6, 8, 10 (14, 22, 31, 41); FAILS at h = 2
(actual 9, formula 7). This exactly mirrors the 5-parameter family:
c5(h) = (h^2 + 14 h + 8)/8 holds for h = 4..14 with the same h = 2
exception (actual 7, formula 5). The shared constant term 8 and the shared
h=2-exception pattern are observed over the supplied terms, not derived.

Cross-family identity (exact over all 5 shared h): c6(h) - c5(h) = h, i.e.
the 6-parameter complement is the 5-parameter complement shifted by h.
2 data points (5 -> 6 parameters changing the linear coefficient 14 -> 22)
support no law about parameter count.

## First falsifier (the term that would break the conjecture)

h = 12 (d = 14): formula predicts c6(12) = (144 + 264 + 8)/8 = 52 and
a6_14 = (C(17,5) - 52)/2 = (6188 - 52)/2 = 3068. NOT yet computed: the
6-param recurrence checkpoint (code/out/.focal_6coeff_state.json) stops at
done_through = 12, so degrees 13 and 14 remain. 3068 is the exact value
a_14 must take for the conjecture to survive.

Delegated: tool_builder run (see the run record in the pattern-finder report)
computes L14 via `python code/bautin/focal_counts_6coeff.py --resume
--max-degree 14`, which also yields the ilcm denominator D6_14.

## Denominator identity (exact over 5 computed terms — conjecture)

The ilcm-clearing denominators coincide between the two families:
D_d = 8, 192, 18432, 1105920, 22295347200 for d = 4,6,8,10,12
(5-param from code/out/focal_denoms.captured.txt; 6-param from the
focal_6coeff dumps, recounted). Falsifier: D6_14 =? D5_14 = 37456183296000,
settled by the same delegated run.

## Refutations (exact)

1. Symmetry-support pairing (refuted). If a6 = (dim - c6)/2 came from a
   monomial pairing under a signed-permutation involution sigma on the six
   coefficients, then c6(h) = |Fix_sigma(h)| for one sigma for all h.
   Enumerated ALL 76 permutation involutions on 6 letters (signs do not
   affect monomial fixedness); full match on h = 2,4,6,8,10: NONE; best
   partial match 1/5 (pi = (0,1,3,2,5,4) gives 5,14,30,55,91). The h=4 row
   alone would not refute (14 is attainable), the full 5-row set does.
   Same conclusion as the 5-param probe (there 312 signed involutions, best
   1/7): the complement is not a symmetry-support identity.

2. Rotation-operator-alone denominator mechanism (refuted). Hypothesis: D_d
   is the lcm of denominators of the last row of M_d^{-1}, where M_d is the
   integer system matrix of rot(V_d) + rhs = L_d (u^2+v^2)^{d/2} + gauge,
   identical for both families (rot and the radial term do not see the
   parameters). Exact rational inverse of M_d (dimensions 6x6 .. 14x14):
   last-row lcm = 8, 16, 128, 256, 1024 for d = 4..12 — pure 2-powers,
   while observed D_d = 8, 192, 18432, 1105920, 22295347200 carries 3-, 5-,
   7-adic factors. So D_d is NOT determined by the operator alone: the
   accumulating V-polynomial denominators (the RHS) contribute the odd
   factors and most of the 2-adic growth. The denominator identity, if real,
   needs a mechanism through the shared rhs structure, not the shared
   operator.

## Status

All statements above are exact over the terms supplied. The two conjectures
(6-param complement quadratic; denominator identity) are 4-5 term fits with
no derivation, their falsifier terms delegated. No regularity in this pass
survives beyond what is stated; nothing here is claimed as established.
