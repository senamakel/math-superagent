# Goal

## Problem (Project Euler 591, Best Approximations by Quadratic Integers)

For a non-square positive integer `d`, a *quadratic integer* is a number of the
form `a + b*sqrt(d)` with `a, b` integers.

**BQA_d(x, n)** = the quadratic integer `a + b*sqrt(d)` **closest to x** with
both `|a| <= n` and `|b| <= n`. "Closest" = minimizes `|x - (a + b*sqrt(d))|`.
Ties broken by an unspecified but for our data irrelevant rule (no ties occur
at the argmin in any of our data).

**Integral part** `I_d(a + b*sqrt(d)) = a`.

We need, for `x = pi` and `n = 10^13`, the quantity

    S = sum over all non-square positive integers d < 100 of |I_d(BQA_d(pi, 10^13))|
        = sum_{d non-square, 2<=d<=99} |a_d|

where `a_d + b_d*sqrt(d) = BQA_d(pi, 10^13)`.

## Worked examples (test oracle)

1. `BQA_2(pi, 10) = 6 - 2*sqrt(2)`  => a=6, b=-2, |a|=6
2. `BQA_5(pi, 100) = 26*sqrt(5) - 55` => a=-55, b=26, |a|=55
3. `BQA_7(pi, 10^6) = 560323 - 211781*sqrt(7)` => a=560323, b=-211781, |a|=560323
4. `I_2(BQA_2(pi, 10^13)) = -6188084046055` => a=-6188084046055, |a| = 6188084046055
   (statement also gives the sandwich `4375636191520*sqrt(2) - 6188084046055 < pi
   < 721133315582*sqrt(2) - 1019836515172`, i.e. b = +4375636191520 for the d=2 n=1e13 record)

These four are the correctness oracle for any brute force and any real method.

## Completion criteria

All criteria are now MET; each is backed by an executed program (see memory.md,
solution.md, and the verification scripts).

- [x] Reproduce all 4 worked examples with brute force where feasible (brute.py:
      examples 1-3) and with the real method (solution_bothsides.py and
      solution_ostrowski.py: examples 1-4, including the d=2 n=1e13 oracle).
- [x] Derive and state the governing theory in solution.md
      (Cabanillas Prop 9/10 + Algorithm 3(ii), arXiv:1904.01874; precise
      statement in research/cabanillas_prop9_10_exact_statement.md).
- [x] Implement solution_bothsides.py and solution_ostrowski.py with exact
      integer arithmetic; both reproduce examples 1-4 and agree with brute
      force exactly on all 90 non-square d at n=1e6 (both signs of b) and on
      16 d at n=1e7.
- [x] Reproduce example 4 (the d=2, n=10^13 oracle) with the real method.
- [x] Compute S and verify it by a second INDEPENDENT full-scale route:
      the separately written Ostrowski-numeration solver solution_ostrowski.py,
      run at n=10^13 for all 90 d, produces a result file (results_ostrowski_n13.txt)
      that is byte-identical to results_full_bothsides.txt (diff empty);
      (b, a) match on all 90 d; independent exact re-sums of both files equal S.
- [x] Row-level audit (audit_results.py, touches no solver code): 7 checks pass
      90/90 on results_full_bothsides.txt: non-square d, |a|,|b|<=1e13,
      a == nint(pi - b sqrt(d)), sign(a) == -sign(b), the master |a| identity,
      local minimality in b over a +-10 window, and exact re-sum = S.
- [x] Report the answer, method, and verification.

**Answer: S = 526007984625966.**