# Approach: Mordell-Weil sieve on the Robertson curve

```approach
idea: On the single Robertson curve E: y² = x(x²−c²) for a fixed centre
  c = e², use local information mod many primes (the Mordell-Weil sieve of
  Bruin–Stoll) to prove that no linear combination of the MW generators
  E(Q) can yield THREE doubled points with x-coordinates in arithmetic
  progression.  Difference from the refuted 2-Selmer approach: it works with
  actual rational points on a single curve as the sieve object, not with the
  2-Selmer data of four linked curves.

status: grounds-as-method / doubts-as-cycle; NOT refuted as a technique, but
  with a decisive cycle-level obstruction and an open first-step feasibility.

precedent (the sieve is a real, published method):
  - N. Bruin & M. Stoll, "The Mordell–Weil sieve: proving non-existence of
    rational points on curves", LMS J. Comput. Math. 13 (2010) 272-306
    (arXiv:math/0601104).  The sieve proves/decides existence of rational
    points on a FIXED curve by combining the global Mordell-Weil group (an
    explicit generator set of J(Q)) with local data (residue images at chosen
    primes), showing the cotational lattice image in the product of local
    groups is empty.
  - Applications as a finishing tool: "Quadratic Chabauty for modular curves"
    (Compositio Math. 2023) and others use the MWS to cut p-adic Chabauty
    residue discs down to the true rational points — the sieve is routinely
    the decisive last step in rational-point computations on fixed curves.
  - The Robertson reduction itself: Bremner, Acta Arith. 88 (1999) 289-297 /
    Robertson, Math. Mag. 69 (1996): MSS ⇔ three points of 2E(Q) on
    E: y²=x(x²−c²) with x-coordinates in AP.  Source:
    research/sources/bremner-on-squares-of-squares-1999.full.md.

feasibility (the decisive obstruction — method-vs-problem mismatch):
  The Mordell-Weil sieve is a per-curve tool: it certifies rational points on
  ONE fixed curve, given explicit generators of that curve's MW group.  The
  MSS problem is a FAMILY of curves parameterised by c = e², with the centre
  unbounded (Morgenstern/Buell: centre > 25×10²⁴ for the hourglass; the
  run's phi work: millions of e ≤ 10⁷ admit four AP-differences).  To use the
  sieve here you would have to:
    (i) compute an exact MW generator set for E: y²=x(x²−c²) for EVERY
        candidate c up to an astronomical bound, via 2-descent/mwrank, and
    (ii) run the sieve for each — a cost that scales with the BOUND (≥ 10²⁵),
        not with the size of the problem's description.  This violates the
        run's method rule ("if the cost grows with the bound in the
        statement, it is the wrong method"): it is a per-instance exhaustion
        over an unbounded family, albeit each instance is decided exactly.
  Worse, the G-B half of the work goes the WRONG way.  Garcia-Fritz–Pastén
  and Bremner's rank conjecture (this run's adopted
  uniform-height-bound-elliptic-ap approach; research/sources/
  garcia-fritz-pasten-bremner-uniformity-2026.full.md) state: a LONG AP of
  x-coordinates of rational points forces the rank of E(Q) to be LARGE.  The
  MW sieve is exactly the tool that degrades as rank grows (the cotational
  lattice image covers a larger and larger subspace of the product of local
  groups, so the empty-intersection obstruction gets exponentially harder to
  demonstrate).  So the regime where the MSS configuration would live (large
  rank) is precisely the regime where the sieve is least effective.
  Concretely this run computed (robertson_reduction_check.txt) that
  Bremner's witness curve E: y²=x³−19209960000x has RANK 2 (mwrank and Sage
  2-descent agree; full MW basis found).  Even at rank 2 the sieve would
  only be deciding whether THIS c admits three doubled points in AP — a
  single instance — and Bremner already searched rational points in AP on
  E(Q) directly and found the structure.  There is no published application
  of the MW sieve to the MSS problem, and the reason is the family-vs-curve
  and rank-vs-sieve mismatches.

  On the witness specifically, the three AP x-coordinates (139129, 180625,
  222121) are NOT three points of 2E(Q): only the first two are (the third,
  X=222121, has X and X+c non-squares; robertson_reduction_check.txt).  So
  even the best-known 7-square witness is one doubled point short — the
  sieve would have to rule out the third membership, i.e. show that the
  quartic (t²+c²)²−4X t(t²−c²) has NO rational root for X=222121.  That
  quartic has no rational root (computed: t⁴−888484t³+... has no rational
  root), which the sieve could certify, but certifying it for ONE X on ONE
  curve is a point-computation, not a sieve over a family — and doing it for
  every c to 10²⁵ is the exhaustion the method forbids.

first-step (feasible, and the honest place the approach stops): choose a
  specific candidate centre c (e.g. Bremner's c = 138600, or a c with many
  two-square representations), run mwrank to get the exact MW basis of
  E: y²=x³−c²x, and run Bruin–Stoll's MWSieve for the three-point-AP-in-2E
  condition.  This is a legitimate per-curve result: it proves for THAT c
  that no three doubled points lie in AP.  It cannot scale to the family, so
  as a proof of global non-existence it is a cycle of per-instance results
  indexed by an unbounded bound, which this run does not count as a proof.
```

## Why this is different from the refuted 2-Selmer approach

The 2-Selmer approach (`simultaneous-congruent-numbers-2selmer`, refuted) was
killed because its four-curve Selmer data is *subsumed* by Bremner II's K3
(Néron-Severi + singular fibres already compute it).  The MW sieve is not
subsumed: it works with actual rational points and a real generator set, and
as a *method* it is sound and published (Bruin–Stoll).  The objection here is
different and twofold: (a) it is per-curve while the problem is an unbounded
family — the cost scales with the bound; (b) the rank-growth direction of the
Garcia-Fritz–Pastén/Bremner result is exactly the regime where the sieve loses
power.  Neither is a refutation of the *technique*; together they refute the
*use of the technique as a proof of global MSS non-existence*.

## Outcome

- Published for MSS? No — no source applies the MW sieve (or any sieve) to the
  3×3 MSS elliptic-curve formulation.
- Known obstruction? Two: (1) family-vs-fixed-curve scope (cost scales with
  centre bound 10²⁵+); (2) large-rank regime degrading the sieve, per the
  Garcia-Fritz–Pastén/Bremner rank conjecture.  Both are structural, not
  computational footguns.
- First-step feasibility? Feasible and worth doing FOR ONE FIXED c as a
  checkable per-curve theorem (start with Bremner's c=138600, exact MW basis
  already known: rank 2, generators (-88200,·),(315000,·)).  It will never be
  a global proof.
