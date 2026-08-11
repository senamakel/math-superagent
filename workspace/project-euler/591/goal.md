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

- [ ] Reproduce all 4 worked examples with brute force (as far as feasible; #4 is too big for naive scan).
- [ ] Derive and state the governing theory in solution.md.
- [ ] Implement solution.py with exact integer arithmetic, agreeing with brute.py
      on every case brute can reach, and reproducing examples 1-3.
- [ ] Reproduce example 4 (the d=2, n=10^13 oracle) with the real method.
- [ ] Compute S and verify by a second independent route (different method or
      brute-force agreement at the largest reachable n for every d).
- [ ] Report the answer, method, and verification.
