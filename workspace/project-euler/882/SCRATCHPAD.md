# Scratchpad — pattern recognition (this branch)

## KEY RESULT: S(n) = ceil(G(n)), G(n) = Σ_{k≤n} k·g(k)

Each single-number bit-deletion subgame is a **canonical Number** g(k):
- One (Left) deletes a 1-bit → g(j) for each option j.
- Zero (Right) deletes a 0-bit → g(j) for each option j.
- g(k) = simplest dyadic strictly between max(Left options) and min(Right options).
- g(0)=0. Verified for k≤4096: never "NOT-A-NUMBER" (always max L < min R).

Board = disjunctive sum → value G(n)=Σ k·g(k). Right-only skip adds −1 per skip,
so Zero (Right) wins iff G(n)−m ≤ 0 ⇒ **S(n)=ceil(G(n))**.

## Reproduces every oracle value
g computed: g(1)=1, g(2)=1/2, g(3)=2, g(4)=1/4, g(5)=3/2, g(6)=1, g(7)=3,
g(8)=1/8, g(9)=5/4, g(10)=3/4, …
S(n)=ceil(G): n=1→1, 2→2, 3→8, 4→9, 5→17, 6→23, 7→44, 8→45, 9→56, 10→64.
Matches given S(2)=2, S(5)=17, S(10)=64 AND brute S(1/2/3/4/5)=1/2/8/9/17.

## Answer at full size
G(10^5) = 517756101446417 / 32768 = 15800662275.5865…
S(10^5) = ceil = **15800662276**.
Two independent code paths (solve_dyadic.py using Fraction, verify_dyadic.py
separate implementation) give identical G and S.

## Exact final value (verified two independent routes)
G(10^5) = 517756101446417 / 32768 = 15800662275.586456…
S(10^5) = ceil(G) = **15800662276**.

## Pattern-run conclusions on the sequences
- S(n) sequence (n=1..60):
  1,2,8,9,17,23,44,45,56,64,91,97,123,151,211,212,231,243,285,293,330,363,443,
  449,487,513,594,622,709,799,954,955,990,1009,1083,1094,1155,1202,1329,1336,
  1393,1429,1548,1581,1693,1808,2020,2026,2087,2124,2252,2278,2384,2492,2712,
  2740,2854,2970,3206,3326,…
  - analyze_sequence: differences never constant → NOT a low-degree polynomial.
  - find_linear_recurrence (order ≤12): NO constant-coefficient linear recurrence
    fits all 30 terms — the sequence is not C-finite.
  - Conclusion: no simple closed recurrence for S(n); the structure that matters
    is the dyadic-CGT rule for g(k), NOT a recurrence of S itself.
- g(k) (single-number dyadic value): g(2^p)=1/2^p, g(2^p+1)=(2^p+1)/2^p,
  g(2^p−1)=p. g is not bit-position additive (weighted least-squares fit leaves
  residual ≈19; the interval max-L/min-R depends on full string structure).
- Up to k=64 all g(k) are dyadic with denominator 2^p, p ≤ 6; up to 1000 the
  denominator exponent of 2 ranges 0..9. Never a NOT-A-NUMBER up to 10^5.

## Structure notes (g(k))
- g(2^p)=1/2^p (powers of two → smallest positive dyadic at birthday p).
- g(2^p −1)=p (Mersenne). g(2^p +1)=(2^{p}+1)/2^p... actually g(2^p+1)= (2^p+1)/2^p? e.g. 3/2,9/8,17/16,33/32 → (2^p+1)/2^p.
- NOT g(2k)=g(k)/2 in general (diverges at k=7,11,15,...).
- No low-degree polynomial / plain linear recurrence found (analyze_sequence).
- The structure that matters is the dyadic CGT rule itself, NOT the S sequence's
  own closed form; G is computable by direct O(N log N) iteration at N=10^5.
