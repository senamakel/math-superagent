# Goal

Solve Project Euler 175: find the Shortened Binary Expansion (SBE) of the smallest
integer n such that f(n)/f(n-1) = 123456789/987654321.

## Definitions

- f(0) = 1.
- For n >= 1, f(n) = number of ways to write n as a sum of powers of 2 in which
  no power of 2 occurs more than twice.
- SBE of n = run-length encoding of the binary expansion of n, read from the
  most-significant bit to the least-significant bit, i.e. the lengths of the
  maximal runs of consecutive equal bits (first run is a run of 1s, then 0s,
  then 1s, ...), given as comma-separated integers with no whitespace.

## Test oracle (from the statement)

1. f(10) = 5 (5 explicitly listed ways).
2. The smallest n for which f(n)/f(n-1) = 13/17 is n = 241.
   Binary of 241 = 11110001 -> SBE = 4,3,1.

## Completion criteria / evidence

- brute.py reproduces both oracle examples.
- solution.py (efficient greedy / Euclid-style method) reproduces both oracle
  examples and agrees with brute.py on every ratio brute.py can reach.
- solution.py computes the SBE for 123456789/987654321.
- The full answer is verified by a second, independent route (forward
  reconstruction of the exact ratio from the run lengths, plus cross-checks),
  and the verification result reported.

## Saved files

- goal.md, memory.md, solution.md, scratchpad.md
- brute.py (naive oracle), solution.py (efficient method), any verification script
