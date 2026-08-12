# Method (theory)

## Governing fact

A repunit in base b with k digits is R_b(k) = 1 + b + b^2 + ... + b^(k-1) = (b^k − 1)/(b − 1).

**Key observation:** every integer n ≥ 3 is a repunit of length 2 in base n−1,
since R_{n−1}(2) = 1 + (n−1) = n. Distinct n give distinct bases, and for n ≥ 3
the base n−1 > 1. So every n ≥ 3 is automatically a repunit in one base (n−1).

Therefore **a positive integer n is a strong repunit (repunit in ≥2 distinct
bases > 1) iff n is a repunit of length ≥ 3 in some base, or n = 1.**
(Length-1 repunits are n=1 = "1" in every base; 1 is strong. Length-2 handles
the second base for everything already length-≥3, and 1.)

Hence:
```
answer(N) = 1 + sum of all distinct values R_b(k) < N with k ≥ 3, b ≥ 2.
```

## Why the bound does not defeat us

Cost grows with the **description size** (log of the bound), not the bound:
- length-3 repunits: b^2 + b + 1 < 10^12  ⇒  b < 10^6  (≈ 10^6 bases)
- length-4: b^3 + b^2 + b + 1 < 10^12  ⇒  b < 10^4  (≈ 10^4 bases)
- length-5: b < 10^3 ; length-6: b < 10^2 ... etc.

Total work ≈ 10^6 (sum over the few lengths is negligible). This is a length of
the answer in the "number of bases up to sqrt of bound" — a genuine structural
reduction, not enumeration of the 10^12 candidate integers.

## Hand check against the worked examples

Length-3 repunits below 50: b=2→7, 3→13, 4→21, 5→31, 6→43.
Length-4: b=2→15, 3→40.
Distinct values with length ≥ 3 below 50: {7,13,21,31,43,15,40}. Plus 1.
Set = {1,7,13,15,21,31,40,43}. Exactly the 8 stated. ✓

Below 1000: sum = 1 + (length≥3 values) = 15864 (verified numerically by brute).
