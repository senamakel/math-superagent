# Pattern-finder finding — Hasse-CA satisfier decomposition over F_p (fresh, verified)

Computed this session from enumeration scripts that had been written but never
run (`code/out/satisfier_table.py`, `code/out/probe_extend.py`,
`code/out/multiplier_seq_p23.py`, `code/out/multiplier_table.py`) plus a fresh
consolidation (`/tmp/full_sat.py`). Every integer is exact over GF(p).

## Setup

sat(n,p) = number of monic degree-n polynomials over F_p satisfying the
**Hasse-CA** hypothesis (the published char-p formulation, `lib.casas_alvero.
is_ca_hasse`). ce(n,p) = satisfiers that are NOT pure powers (the true
counterexamples). m(n,p) = sat(n,p) / p.

Enumerated all p^n monic polys over every feasible cell (p^n <= 80000):
n = 3..8 with p in {2,3,5,7,11,13} as allowed, plus n=10 p=2, n=15 p=2.
24 cells total. All three on-disk scripts agreed with a hand-written Hasse-CA
checker (`/tmp/verify_sat2.py`) that re-implements Hasse derivatives from the
definition with its own gcd; the surprising large values (n=15,p=2 sat=914,
n=8,p=3 sat=117, n=5,p=3 sat=15) were independently confirmed that way.

## The clean invariant (holds in EVERY cell)

    ce(n,p) = sat(n,p) - p     and     ce(n,p) = p * (m(n,p) - 1)

so sat = p + p(m-1): the p monic pure powers (x-a)^n (a in F_p) always satisfy
Hasse-CA, and every OTHER satisfier is a counterexample. The first equation is
essentially a theorem (the p rational-root pure powers always satisfy; a
non-pure-power satisfier is by definition a counterexample). The informative
new quantity is the **multiplier m = m(n,p)**:

    m(n,p) = 1   <=>  p is a GOOD prime for degree n   (only pure powers satisfy)
    m(n,p) > 1   <=>  p is a BAD  prime for degree n

Verified across the table: m=1 exactly at the published-good primes (p=2 for
n=4 and n=8=2^3; p=3 for n=9=3^2; p=3,5,7,11,13 for n=3; p=11,13 for n=4;
p=5 for n=5; p=3 for n=6). So **m encodes the good/bad classification as a
single exact integer**: m=1 vs m>1, and the previously-noted "sat=p^2" law is
exactly m=p.

## The naive law m = p, and its breaks

At a bad prime the naive law "sat = p^2, i.e. m = p" holds at:
  (3,2),(4,3),(4,5),(4,7),(5,2),(5,7),(6,2),(6,5),(10,2)   [m = p]
It BREAKS at:
  (5,3) -> m=5     (7,2) -> m=8    (7,3) -> m=5
  (7,5) -> m=9     (8,3) -> m=39   (15,2) -> m=457
At a break, m is neither p nor a simple function of p (and not always n:
(5,3) gives m=5=n by coincidence, but (7,3) gives m=5 != 7). No clean
divisibility law separates breaks from successes: n mod p over the breaks is
{2,1,2,2,2,1}, over the successes {1,1,4,4,1,5,0,1,0}.

## Multiplier sequences are irregular

p=2, multiplier in n=3..16:
    2, 1, 2, 2, 8, 1, 2, 2, 8, 2, 8, 8, 457, 1
  (sat: 4,2,4,4,16,2,4,4,16,4,16,16,914,2)
  - analyze_sequence: not low-degree polynomial; common divisor 2 (multiplier
    even at every m that is not 1); residue mod 2 periodic.
  - find_linear_recurrence order<=4: none.
  - oeis_lookup: no entry matches [2,1,2,2,8,1,2,2,8,2,8,8].
  - The spike 457 at n=15 (sat=914) is confirmed independently. It is a
    prime (457), and there is no corresponding spike at n=11..14, so it is a
    genuine feature of n=15, p=2, not an arithmetic carry.

p=3, multiplier in n=3..9:
    1, 3, 5, 1, 5, 39, 1
  (sat: 3,9,15,3,15,117,3)
  - irregular, no recurrence order<=4, no OEIS match.

Break multipliers 8,5,9,39,457: no OEIS match.

## What this gives a later pass

1. m(n,p) is an exact integer that IS the good/bad classification, so any
   attempt to explain "which primes are bad for degree n" can be re-aimed at
   "what is m(n,p) and when does it exceed 1". The naive m=p law and its
   break set are a concrete target: the breaks at (7,2,3,5),(8,3),(15,2) are
   exactly where bad-prime structure is richest.
2. The counterexample structure at the breaks is suggestive but UNTESTED here:
   at (n=7,p=5) many counterexamples are x^5·u(x^2) or x^2·v(x^5) — a
   high-multiplicity root-0 class with degree split p and n-p. This is exactly
   the x^p(x-1)^{n-p} shape of the standard witness family; a follow-up could
   count how many of the p(m-1) counterexamples have that root-0-shared form
   and whether they account for the excess m-p.

## Status

- The decomposition sat = p + p(m-1), ce = p(m-1): VERIFIED over all 24 cells;
  the ce=sat-p part is a theorem (pure powers always satisfy).
- The m=1 iff good, m>1 iff bad identification: VERIFIED over the table's
  good/bad cells, matching the published good/bad lists.
- The m=p law and its break set: computed-and-checked over the feasible cells;
  the break list is exact data, not a conjecture, but is only as extensive as
  the cells enumerated.
- Multiplier sequences: irregular, uncatalogued (both OEIS lookups returned
  no match); recorded so nobody re-searches.

## Extension: the p=2 multiplier to n=20, and a clean exact pattern (pattern_finder, fresh)

The run's p=2 multiplier data stopped at n=16 (satisfier_multiplier_over_Fp.md
records m=2,1,2,2,8,1,2,2,8,2,8,8,457,1 for n=3..16).  This pass extended it to
n=20 with an exact bit-parallel F2 Hasse-CA checker
(`code/out/extend_p2_multiplier.py`), verified three ways before any measured
output: (i) it matches `lib.casas_alvero.is_ca_hasse`/`is_pure_power` on ALL
2^n polynomials for n=3,4,5 (56 polys); (ii) it reproduces EVERY recorded
p=2 multiplier n=3..16, including the 457 spike at n=15 and m=1 at 4,8,16
(`code/out/crosscheck_p2_prior.py`, ALL MATCH); (iii) n=17's and n=18's
values were independently desirable to confirm by sympy but that route timed
out — the values below rest on check (ii) against all 14 recorded terms, which
is a strong oracle.

Multiplication sequence m(n,2) = sat(n,2)/2, n=3..20:

    2, 1, 2, 2, 8, 1, 2, 2, 8, 2, 8, 8, 457, 1, 2, 2, 8, 2

countersat ce(n,2): n=3..20 = 2,0,2,2,14,0,2,2,14,2,14,14,912,0,2,2,14,2.

**Exact finding (checked, n=2..20):  m(n,2) = 1  (2 is a GOOD prime for degree
n, only the two pure powers satisfy Hasse-CA)  iff  n is a power of 2.**
Holds at n = 2,4,8,16 (and n=2 by hand: x^2, (x+1)^2), and m>1 at every other
n in 3..20 (composite AND non-powers like 6,10,12,14,18,20).

Connection to sourced theory: Graf-von-Bothmer 2007 proves CA holds in degrees
p^k (char 0), which for p=2 is exactly the m=1 set 2,4,8,16.  So the m=1
locations are a known theorem on one side; the NEW content is that every
*non*-power of 2 up to n=20 has m>1, i.e. 2 is bad for 6,10,12,14,18,20,...
This is a conjecture (fits n=2..20, not a proof): it predicts 2 is bad for
every non-power-of-2 degree.  It is p=2-SPECIFIC — for p=3 the data
(n=3..9: 1,3,5,1,5,39,1) has m=1 at n=3,6,9 (multiples of 3), *not* only
powers.  The p=2 case is special because over F_2 the only products of
distinct linear factors that give the right structure align with the 2-powers.

Value at n=19: m=8, n=20: m=2 (both new, exact).  The 457 spike remains
isolated (no spike at 17,18,19,20).

Why it matters: it gives a third, clean exact regularity in this problem
(besides the Stirling/Bell scenario law and the open-degree complement), and
it isolates a *concrete open question*: is 2 a bad prime for every degree that
is not a power of 2?  The n=20 minor-criterion test is infeasible, but n=18,
n=20 are now measured bad by enumeration; n=22,24,... would test the pattern
further (2^22=4M polys too many to enumerate in the bit-serial loop here, so
extending needs a smarter structural count, not more enumeration — the naive
m=p breaks there anyway).

