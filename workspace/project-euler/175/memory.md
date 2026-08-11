# Working memory

## Problem

Project Euler 175 (Fractions involving the number of different ways a
number can be expressed as a sum of powers of 2).

Define f(0) = 1. For n >= 1, f(n) = number of ways to write n as a sum of
powers of 2 where no power of 2 occurs more than twice (each 2^k used
0, 1, or 2 times).

Given: f(10)=5; smallest n with f(n)/f(n-1)=13/17 is n=241, whose SBE
(runs of equal bits, MSB first) is 4,3,1.

Target: SBE of the smallest n with f(n)/f(n-1) = 123456789/987654321,
as comma-separated integers with no whitespace.

## Established results

### Verified by brute.py (ran with python3, all checks True)
- f(10) = 5  (matches statement example)
- f(241)/f(240) = 17/13 -> 13/17 exactly (as Fraction), matches example
- first n in 1..245 with ratio 13/17 is n = 241, matches example
- binary of 241 = 11110001, SBE = [4,3,1], matches example

### Empirically derived recurrences (read off table, spot-checked)
- f(2n)   = f(n) + f(n-1)
- f(2n+1) = f(n)
- f(2n-1) = f(n-1)
These match Project Euler 175's classical recursion (to be proven/cited).

## Failed approaches

- First DP attempt updated "1 copy" and "2 copies" of each coin as two
  sequential passes on the live array, which let 1+1 from the second pass
  stack on a coin already used once -> overcounted (f(10) came out 6, not 5).
  Fixed by single-pass bounded transition ndp[j]=dp[j]+dp[j-c]+dp[j-2c]
  computed from the OLD dp. Verified f(10)=5 after fix.

## Open questions

- Prove the recurrences (they match PE175's known recursion).
- Use the recurrences to derive the SBE for ratio 123456789/987654321
  without brute force at full size. (Brute scanning to the bound is
  prohibited; the correct method walks a binary/ratio tree, not the n-line.)
