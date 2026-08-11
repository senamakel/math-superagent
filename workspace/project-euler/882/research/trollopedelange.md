# Digital sums and functional equations — Girgensohn (2011), primary proof of the Trollope–Delange structure for both ones and zeros

Source: R. Girgensohn, "Digital sums and functional equations", INTEGERS 11 (2011), #A54.
https://emis.muni.cz/journals/INTEGERS/papers/l54/l54.pdf
Full text stored at `research/trollopedelange.full.md`. This primary paper gives a new, elementary
proof of the Trollope–Delange formula and derives explicit analogues for the number of **zeros** as well.

## What it establishes

Let s(j) = number of 1-bits of j (A000120 / popcount), S(n) = Σ_{j=0}^{n-1} s(j) (the summatory
1-bit count; A000788 is the same sum). For s^(0)(j) = number of 0-bits (no leading zeros) and its
summatory S^(0)_1(n), with p(n) = the largest power of 2 ≤ n and x = (n − p(n))/p(n) ∈ [0,1):

- **Trollope–Delange formula (ones), exact:**
  (1/n)·S(n) = (1/2)log₂n + (1/2)F̃(log₂n), with the 1-periodic F̃ built from Takagi's
  function; equivalently (35)  S(n) = (n/2)log₂p(n) + p(n)·F(x) where F is the continuous
  solution of a pair of functional equations of type (10),(11). Equivalently S(p) = (1/2)p·log₂p
  at powers of two, and the whole sequence is determined by the identities
  S(2n) = 2S(n) + n,  S(n+p(n)) = S(n) + S(p(n)) + p(n),  S(n+2p(n)) = S(n) + S(2p(n)) + n.
- **Same structure for zeros (Trollope–Delange analogue, (99)):**
  (1/n)·S^(0)_1(n) = (1/2)log₂n − 1 − (1/2)log₂(x+1) + F^(0)_1(x)/(x+1), with F^(0)_1(x) = x + (1/2)T(x).
- **Key method (the actual reason this is efficient):** the entire summatory sequence is fixed by
  its values at powers of two (the "stepping stones") plus a single continuous 1-periodic
  fluctuation function; the paper gives explicit formulas for the power sums Σ s(j)^k too
  (Theorem 2, formula (73)) and their zero-count analogues (98).

## Why it applies here

The (A,B) minimax DP runs on A(n) = Σ_{k=1..n} k·popcount(k) and B(n) = Σ_{k=1..n} k·zerocount(k).
Those are the k·-**weighted** ranges of the unweighted summatory functions this paper treats. The
paper is the primary, locally-held evidence that the *unweighted* one- and zero-count summatory
functions each have an exact Trollope–Delange representation (main term + continuous periodic
fluctuation), and — decisively — that they are determined by the O(log n) divide-and-conquer
identities (22)–(24) (and their zero analogues), i.e. computable in polylog time. Combined with
the run's per-bit k·-weighting decomposition (and the weighted-moment structure in weightedmom.md),
this warrants S(n) evaluation at n = 10^5 without iterating to n.

## Caveats
- This is for the UNWEIGHTED Σ popcount and Σ zerocount. The k·-weighted A(n), B(n) are the run's
  own bit-position decomposition; the paper supplies the underlying unweighted engine and its
  polylog recurrences, not the k·-weighted sums directly (OEIS A000788/A059015 give the matching
  unweighted recurrences; cf. bitcount.md, zerocount.md).
- Formula (99) uses s^(0)(0) := −1 (a normalisation so S^(0)(2n;t) mirrors the ones-case); the
  convention is documented in the paper but must be accounted for if formula (99) is quoted
  numerically.
