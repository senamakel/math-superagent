# Summatory binary digit-sum A000788 — total number of 1-bits in 0..n

Source: https://oeis.org/A000788 (OEIS entry; T. D. Noe / N. J. A. Sloane, with
recurrences by Ralf Stephan 2003, Michel Marcus 2018, David W. Wilson's fast C++
implementation, and a Python O(log n) form by Chai Wah Wu 2024).

## What it establishes
- Defining identity: A000788(n) = Σ_{k=1..n} A000120(k), where A000120(k) is the
  popcount (number of 1-bits) of k. It is the partial-sum / summatory function
  of the binary digit sum. First values: 0,1,2,4,5,7,9,12,... (so
  sum_{k=1..n} popcount(k) for n=5 is 7, matching the 1s in 1..5: 1+1+2+1+2).
- **Fast divide-and-conquer recurrences (O(log n)):**
  - a(0)=0, a(2n) = a(n) + a(n-1) + n,  a(2n+1) = 2a(n) + n + 1.
  - Marcus form: write n = 2^m + r (0 ≤ r < 2^m); then
    a(n) = m·2^(m-1) + r + 1 + a(r),  a(0)=0.
  - Hasler PARI version handles even/odd and powers of two specially.
- **Closed-form / special values:** a(2^m − 1) = m·2^(m-1) (all numbers with
  ≤ m bits; half the digits are 1s). Asymptotics: a(n) = (n/2)log₂n + n·F(log₂n)
  where F is a continuous, nowhere-differentiable period-1 function (the
  Trollope–Delangé / Takagi-type fluctuation, cf. Lagarias 2012).
- **Structure:** the sequence is 2-regular (Shallit 2021 identities);
  its graph is a Takagi-curve variant. Allouche–Shallit, Automatic Sequences
  (2003) p.94 covers it. General base-p "digits ≥ d" formulas (Fischer 2012)
  count any digit run, not just 1s.
- Companion for the zero-counting side is A059015 (linked in CROSSREFS).

## Why it applies here
- The (A,B) counting reduction needs A = total weighted 1-bits over the board
  "k copies of k, k=1..n" = Σ_{k=1..n} k·popcount(k). A000788 gives the
  unweighted summatory popcount in O(log n); the k· weighting is a per-bit
  superimposition (a bit at position j is set in k copies of k for a run of k),
  computable by the same bit-position decomposition. It is the arithmetic engine
  behind computing A(n) — and B(n) via the companion A059015 — without iterating
  to n, which is what lets S(n) be evaluated at n = 10^5.
- It converts "sum over all binary expansions up to n" (O(n log n) work) into
  O(poly(log n)) closed-form/divide-and-conquer evaluation.

## Caveat
- The board uses k copies of k, so the needed sums are k·(popcount or zerocount)
  weighted, not the plain unweighted summatory functions. This entry supplies
  the underlying digit-count identity; the weighting is handled separately by
  the run's derivation (solution.md). OEIS does not directly tabulate the
  weighted variant.
