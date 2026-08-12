# Goal

**Problem (Project Euler 346, strong repunits):**

A *repunit* in base b>1 is a number whose base-b representation is all 1's:
R_b(k) = 1 + b + b^2 + ... + b^(k-1) = (b^k − 1)/(b − 1), a string of k ones, k ≥ 1.

A positive integer n is a *strong repunit* if it is a repunit in **at least two**
distinct bases b > 1.

Worked examples (the test oracle):
- Strong repunits below 50: {1, 7, 13, 15, 21, 31, 40, 43}  (8 of them)
- Sum of strong repunits below 1000 = 15864
- **Task**: sum of all strong repunits below 10^12.

Symbols:
- b: base, integer > 1.
- k: number of digits (all ones), k ≥ 1.
- R_b(k) = (b^k − 1)/(b − 1).

Completion criteria:
1. /workspace/brute.py reproduces {1,7,13,15,21,31,40,43} and 15864, and 1.
2. A structural characterization is established (see solution.md).
3. /workspace/solution.py uses an efficient method (cost independent of the 10^12 bound
   aside from ~10^6 length-3 bases), agrees with brute.py on every reachable case,
   and reproduces all examples.
4. Final sum below 10^12 reported and verified by a second independent route.
