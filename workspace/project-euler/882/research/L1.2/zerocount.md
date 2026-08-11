# Summatory binary zero-count A059015 — total number of 0-bits in 0..n

Source: https://oeis.org/A059015 (OEIS entry; Patrick De Geest, with recurrences
by Ralf Stephan 2003, Hieronymus Fischer 2012, and an O(log n) Python form by
Chai Wah Wu 2023/2024).

## What it establishes
- Defining identity: A059015(n) = Σ_{k=0..n} A023416(k), where A023416(k) is the
  number of 0-bits in the binary expansion of k (no leading zeros). First
  values: 1,1,2,2,4,5,6,6,9,11,13,... So Σ_{k=1..n} zerocount(k) for n=5 is
  0+1+0+2+1 = 4 (A059015(5) − 1 = 5−1). Offset: A059015(0)=1 counts the single
  "0" string.
- **Fast recurrences (O(log n)):** a(n) = b(n)+1 with b(2n)=b(n)+b(n-1)+n and
  b(2n+1)=2b(n)+n (Ralf Stephan). Special value: total zero digits over all
  numbers with ≤ m places is a(2^m −1) = 2 + (m−2)·2^(m-1).
- **Key identity linking the two sides:** A059015(n) = A083652(n) − A000788(n),
  i.e. (total number of binary digits over 0..n) minus (total 1-bits) equals the
  total 0-bits. Also Chai Wah Wu: A059015(n) = 2 + (n+1)(m − popcount-sum) − 2^m
  where m = bit_length(n+1), plus the A000788 subtractive term — a direct closed
  form through the 1-bit summatory function.
- **Structure:** partial sums of A023416; graph is another Takagi-curve variant
  (Lagarias 2012); general base-p "digits ≤ d" formulas given (Fischer 2012).

## Why it applies here
- The counting reduction needs B = total weighted 0-bits over "k copies of k,
  k=1..n" = Σ_{k=1..n} k·zerocount(k). A059015 gives the unweighted summatory
  zero-count in O(log n); the k· weighting is the same per-bit superimposition
  as for A. It is the exact complement of A000788, so together they supply
  A(n) and B(n) — the two integers the (A,B) minimax DP is run on — at n = 10^5
  without iterating.

## Caveat
- Same as A000788: the board's k copies of k requires the k·-weighted sums, not
  the plain summatory values; this entry supplies the underlying digit-count
  identity and the weighting is the run's own derivation.
