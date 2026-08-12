# PE346 — Sum of strong repunits below 10^12

## Definition

A **strong repunit** is a positive integer that is a repunit (all digits 1,
length >= 1) in at least two bases b > 1.

Observation: every n > 1 is "11" (length-2 repunit) in base n−1. Hence a
number > 1 is *strong* iff it is a repunit of length >= 3 in some base b > 1,
i.e. equals (b^k − 1)/(b − 1) for some b >= 2, k >= 3.  The number 1 is a
length-1 repunit in every base, so it counts.  (Note 2 is NOT a strong repunit:
it is "10" in base 2 and "2" in every larger base.)

So: strong repunits below N = {1} ∪ { (b^k−1)/(b−1) : b>=2, k>=3, value < N }.

## Method

The value for k=3 is b²+b+1, so a base b is relevant only while b²+b+1 < N,
i.e. b < ~√N.  For each such b we add b³,b⁴,...-based repunits (lengths k=3,4,...)
that stay below N.  Each (b,k) contributes one value; we dedup with a set.

Cost: number of bases ≈ √N (≈ 10^6 for N=10^12), each contributing ~log_b(N)
lengths.  Total ≈ √N·log N — polynomial, well below the bound.

## Result

The sorted list of distinct strong repunits is exactly OEIS A053696 with 1
prepended (verified by matching the exhaustive enumeration in both the OEIS
program and our own brute force).

Sum below 10^12 = **336108797689259276**  (count 1011529).

## Verification

- brute.py reproduces the worked examples: 8 strong repunits {1,7,13,15,21,31,40,43}
  below 50, and sum 15864 below 1000.
- verify.py is a structurally different program (value=val*b+1, iterate length
  per base) that reproduces below-1000 sum 15864, below-10^6, below-10^9 sums,
  and the full 10^12 sum — identical 336108797689259276 and count 1011529.

## Pattern findings

Count per 10^p and sum per 10^p sequences show no low-degree polynomial and no
fixed-order constant-coefficient recurrence (see scratch). The count ~ √N,
dominated by the ~√N relevant bases, with a smaller correction for extra
lengths. No catalogued closed form for the sum; enumeration is the intended
method.
