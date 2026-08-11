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

## Structure notes (g(k))
- g(2^p)=1/2^p (powers of two → smallest positive dyadic at birthday p).
- g(2^p −1)=p (Mersenne). g(2^p +1)=(2^{p}+1)/2^p... actually g(2^p+1)= (2^p+1)/2^p? e.g. 3/2,9/8,17/16,33/32 → (2^p+1)/2^p.
- NOT g(2k)=g(k)/2 in general (diverges at k=7,11,15,...).
- No low-degree polynomial / plain linear recurrence found (analyze_sequence).
- The structure that matters is the dyadic CGT rule itself, NOT the S sequence's
  own closed form; G is computable by direct O(N log N) iteration at N=10^5.
