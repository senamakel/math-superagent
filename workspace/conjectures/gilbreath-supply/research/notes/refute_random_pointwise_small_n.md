# Small-n failure of R-random-pointwise (destroyed runner, finding preserved)

Source: `code/refute/random_pointwise_n4_analysis.md` (deleted in the refute
spray consolidation; this preserves the verified small-n hand computation,
which is NOT superseded and is not reproduced by the single-boundary
consolidated sweep).

Rung `R-random-pointwise` (research/weakened/supply.md): "For h uniform on
F2^n, wt(Phi_n h) >= n/4 with probability 1 - exp(-Omega(n))."

Fold cell at depth d in [2, n-1]:
    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o].

## n = 4 (rows d = 2, 3)
- d=2 (10): submasks {0,2} -> cols {1,3}: c2 = h1^h3
- d=3 (11): submasks {0,1,2,3} -> cols {0,1,2,3}: c3 = h0^h1^h2^h3
- wt = c2 + c3 ; n/4 = 1.
- P(wt < 1) = P(wt = 0) = P(h1=h3 and h0=h2) = 4/16 = 1/4.
- So P(wt < n/4) = 1/4 at n=4, NOT 1 - exp(-Omega(4)).

## n = 5 (rows d = 2,3,4)
- c2=h2^h4, c3=h1^h2^h3^h4, c4=h0^h4. n/4 = 1.25 => need wt >= 2.
- P(wt=0): h0=h2=h4=a, h1=h3=b -> 4 of 32 = 1/8.
- P(wt<=1) is a constant > 0 by symmetry, not exp(-Omega(5)).

## Conclusion
The literal strong exponential form of R-random-pointwise FAILS at small n:
the fraction with wt(Phi_n h) < n/4 is a constant (~1/4, >1/8), not
exponentially small. Whether the asymptotic (> large n) exp(-Omega(n))
concentration holds is genuinely open and needs Phi_n-specific (Lucas/submask)
structure, not bare rank. R-random-pointwise stays open.
