# Odd-factor dyadic density — decisive measurement (Directive 62/64)

## What was run

1. `code/out/dyadic_oddfactor_density.py` — the target script (had no capture).
   Ran it, EXIT_CODE=0, captured to `code/out/dyadic_oddfactor_density.captured.txt`.
   It uses the **fold-weight** proxy (`nu2_stable`) and samples only n=400 and
   n=2000 for random words per odd-factor period. It does NOT measure the
   infimum the directive asks for, and its "nu2(2000)=0" readings for some
   period-3 and period-5 random words are fold-weight artifacts, not the true
   suffix count.

2. `code/out/dyadic_oddfactor_inf_new2.py` (new) — the real infimum measurement
   with the **canonical, anchored** `cycle_and_nu2` convention (suffix starts at
   index >= 2; the quantity that reproduces nu2=2048 at n=3999 for the primes,
   and that feeds Granville Lemma 5.4's budget). Incremental right-diagonal
   recurrence, O(N^2) diffs, O(N) memory, parallel over the four periods via
   multiprocessing. Captured to `code/out/dyadic_oddfactor_inf_new2.captured.txt`.

## The number (CONFIRMED over n in [100,20000] only; tail-1 word per period)

INFIMUM of nu2(n)/n (true/anchored convention), and the late-window read:
the global infimum is always attained in the small-n startup regime (n ~ 100-114),
and the infimum over [10000,20000] stays bounded well away from 0 for every P.

| P | word | global inf@n | inf[1000,N]@n | inf[10000,N]@n | late new low (n>N/3)? |
|---|------|--------------|---------------|----------------|----------------------|
| 3 | 001 | 0.647059 @102 | 0.664671 @1002 | 0.666467 @10002 | NO |
| 5 | 00001 | 0.508772 @114 | 0.530572 @1014 | 0.533054 @10014 | NO |
| 7 | 0000001 | 0.266667 @105 | 0.283716 @1001 | 0.285514 @10003 | NO |
| 9 | 000000001 | 0.359223 @103 | 0.407301 @1041 | 0.412139 @10050 | NO |

Reading: for the tail-1 word of each period, the infimum SETTLES early at a
positive value and does NOT keep decaying toward 0 out to n=20000. So on these
words a uniform positive c with nu2 >= c*n is plausible over the measured range.

## Decisive negative (the real falsifier): all odd-period WORDS at period 3,5,7

The odd-factor converse claims nu2 >= c(P)*n for EVERY word of a given odd
minimal period. Enumerating ALL primitive words of periods 3,5,7 and computing
the TRUE nu2 at n=2000 and n=12000:

- P=3 (6 primitive words): smallest nu2(12000) = 7998 (word 001 / 110). None bounded.
- P=5 (30 words): smallest nu2(12000) = 6398. None bounded.
- P=7 (126 words): smallest nu2(12000) = 3428 (word 0000100 etc). None bounded.

So NO odd-period word of period 3, 5, or 7 has bounded true nu2 at n up to
12000. The "nu2=O(1) on some odd-period word" scare from the fold-weight proxy
is NOT reproduced with the true suffix count. The odd-factor converse is NOT
refuted by any small-odd-period word.

## Oscillation with binary structure

The prior reflection (P=7 reads [0.284, 0.5712, 0.2856, 0.8571]) is visible in
the ratio's n-dependence: the true-nu2 infimum settles to ~0.2855 for P=7 at
n~10000, but single-n ratios still swing (e.g. near powers of two the fold
weight / nu2 ratio can double). In aggregate over [10000,20000] the infimum is
stable; the oscillation is a per-n fluctuation, not a decay toward 0.

## Independent verification

- Three routes agree cell-for-cell at every sampled point: (A) my incremental
  right-diagonal sweep, (B) my full-triangle brute force (literal rows), and
  (C) the canonical `lib.rightdiag.cycle_and_nu2`. Verified at n in
  {300,511,1000,2047,4093} for each P, and at n in {200,400,511,600,700} for
  all-words points. Also matched the recorded stage-1/periodic-extend values
  (P=15: 104,104,158; P=14: 56).

## Conclusion

CONFIRMED over n in [100,20000] (tail-1 words): inf nu2(n)/n is bounded below
by a positive constant per odd factor P; NO late-plateau decay to 0 in range.
CONFIRMED over n<=12000 (all primitive words of period 3,5,7): every odd-period
word has true nu2 growing ~linearly, none bounded. Numerical evidence only —
the odd-factor converse remains CONJECTURED, but nothing here refutes it and
the supply-usefulness on the periodic family is not killed by a plateau.

Note: periodic test words only; the primes are aperiodic. This measures whether
the odd-factor dichotomy is supply-useful on the periodic family, not
Gilbreath itself.
