# Goal

## Problem (Project Euler 156, from /workspace/problem.md)

Write the natural numbers consecutively in base 10, starting from zero:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ...

**Definition.** For a digit d ∈ {0,...,9} and an integer n ≥ 0, let
`f(n,d)` = total number of occurrences of the digit `d` in the base-10
writings of all integers 0, 1, ..., n, counting one occurrence per digit
position (no leading zeros; the number 0 contributes its single digit '0').

**Equation.** Solve `f(n,d) = n` for each d ∈ {1,...,9}.

**Notation.** `s(d)` = sum of all solutions n of f(n,d)=n (each solution
counted once per digit d it satisfies; if n solves the equation for several d,
it is counted in each s(d)).

**Answer required:** Σ_{d=1}^{9} s(d).

## Oracle (worked examples from the statement — must be reproduced by brute.py)

- f(n,1) for n=0..12: 0,1,1,1,1,1,1,1,1,1,2,4,5.
- f(n,1) never equals 3 for any n.
- First three solutions of f(n,1)=n: n=0, 1, 199981.
- s(1) = 22786974071.
- For every d ≠ 0, n=0 is a solution of f(n,d)=n.

## Completion criteria

1. brute.py (naive per-number counting) reproduces every oracle target above.
2. solution.py (efficient method, exact integer arithmetic) agrees with
   brute.py on every case brute.py can reach, and reproduces the oracle.
3. solution.py computes Σ s(d) at full size.
4. The final number is verified by a second independent route (a
   differently-structured program, or brute-force agreement at the largest
   reachable size), and the verification is reported.