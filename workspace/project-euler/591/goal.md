# Goal

## Problem (Project Euler 591, Best Approximations by Quadratic Integers)

For a non-square positive integer `d`, a *quadratic integer* is a number of the
form `a + b*sqrt(d)` with `a, b` integers.

**BQA_d(x, n)** = the quadratic integer `a + b*sqrt(d)` **closest to x** with
both `|a| <= n` and `|b| <= n`. "Closest" = minimizes `|x - (a + b*sqrt(d))|`.
Ties broken by an unspecified but for our data irrelevant rule.

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

These four are the correctness oracle for any brute force and any real method.

## Completion criteria

- [x] Reproduce all 4 worked examples, brute force where feasible and the real method for #4
      (brute.py reproduced examples 1-3; solution_bothsides.py reproduced all four, with
      I_2(BQA_2(pi,1e13)) = -6188084046055).
- [x] Derive and state the governing theory in solution.md
      (Cabanillas Prop 9/10 + Algorithm 3(ii), arXiv:1904.01874; precise statement in
      research/cabanillas_prop9_10_exact_statement.md).
- [x] Implement solution_bothsides.py with exact integer arithmetic, agreeing with brute force
      on every case brute can reach (exact (b,a) match on 16 d at n=1e7 and all 90 d at n=1e6,
      both signs) and reproducing examples 1-3.
- [x] Reproduce example 4 (the d=2, n=10^13 oracle) with the real method.
- [x] Compute S and verify by a second independent route
      (brute force at largest reachable n — exact agreement at n=1e7; independent exact-int
      re-sum of results_full_bothsides.txt).
- [x] Report the answer, method, and verification (this report).

Answer: **S = 526007984625966**.
