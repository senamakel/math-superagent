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

- Use the recurrences to derive the SBE for ratio 123456789/987654321
  without brute force at full size. (Brute scanning to the bound is
  prohibited; the correct method walks a binary/ratio tree, not the n-line.)

## Sourced confirmation (research/sources_calkin_wilf_hyperbinary.md)

- f = number of hyperbinary representations = Stern's diatomic series
  A002487 shifted: f(n) = a(n+1). G.f. x*Prod(1+x^(2^k)+x^(2^(k+1))) [Carlitz].
  OEIS: https://oeis.org/A002487
- Recurrences f(2n)=f(n)+f(n-1), f(2n+1)=f(n) are the PE175 form; Calkin & Wilf
  prove b(2n+1)=b(n), b(2n+2)=b(n)+b(n+1), b(0)=1 and identify b with the
  hyperbinary count. https://www2.math.upenn.edu/~wilf/website/recounting.pdf
- r_n = f(n)/f(n-1) is the Calkin-Wilf enumeration of positive rationals:
  root r_1=1/1, r_{2n}=r_n+1, r_{2n+1}=r_n/(r_n+1). Every positive rational
  appears exactly once (Calkin-Wilf Thm 1; already in Stern 1858).
  Verified mechanically: r recurrence holds m=1..199; tree walk over binary
  digits (0->r+1,1->r/(r+1)) matches r_n for n=1..99; solution.py inverse
  peel reproduces bin(n) for all n=2..5000.
- Bijection property: Stern-Brocot/Calkin-Wilf; sources:
  https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree ,
  https://mathworld.wolfram.com/Calkin-WilfTree.html ,
  https://mathworld.wolfram.com/SternsDiatomicSeries.html ,
  https://ems.press/content/serial-article-files/45350 ,
  https://www.jstor.org/stable/10.4169/000298910x496714
