# Goal

Solve Project Euler problem 175.

## Problem restatement (with symbols)

Define:
- `f(0) = 1`.
- For `n >= 1`, `f(n)` = number of ways to write `n` as a sum of
  powers of 2 where no power of 2 occurs more than twice.
  (Each `2^k` may be used 0, 1, or 2 times.)

Worked examples given in the statement (test oracle):
1. `f(10) = 5`; the five ways are:
   10, 8+2, 8+1+1, 4+4+2, 4+2+2+1+1, 4+4+1+1.
2. The smallest `n` with `f(n)/f(n-1) = 13/17` is `n = 241`,
   whose binary expansion is `11110001`. Its "Shortened Binary
   Expansion" (runs of equal bits, most-significant first) is `4,3,1`
   (4 ones, 3 zeroes, 1 one).

Target: find the Shortened Binary Expansion of the smallest `n` for which
`f(n)/f(n-1) = 123456789/987654321`. Report as comma-separated integers,
no whitespace.

## Completion criteria
1. brute.py computes f(n) correctly (validated against f(10)=5 and the
   n=241 example) and derives the governing recursion empirically.
2. Governing theory identified and recorded in memory.md.
3. solution.py implements an efficient (poly in log of bound) exact
   algorithm, agrees with brute.py on all reachable cases, and reproduces
   the n=241 example.
4. Final SBE verified by a second independent route.
