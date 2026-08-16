# Pattern-finder: the density-1 discriminator is "S is not a random walk", not ACF1(D)=−1/2

Exact measurement (n≤40000 primes from guard-checked JSON; iid/single-1 via
exact SOS fold), a conjecture to derive, not a proof.

**The claim.** The primes' fold-excess fluctuation
`S(n) = (n−2) − 2·ν₂(n)` is a **non-random-walk**: corr(S(n),S(n+1)) = −0.053
(≈0), increments D(n)=S(n+1)−S(n) have ACF1(D) → −1/2 (−0.508@1000 →
−0.5009@40000) and all higher-lag autocorrelation vanishing (Σ|ACF k≥2|=0.08),
so var(S)/var(D) → 1/2 and var(S)=O(n) — the exact second-moment input
density-1 SUPPLY needs by Chebyshev.

**The correction that matters for the other schools.** The tempting reading —
"ACF1(D) = −1/2 is the mechanism" — is **wrong**: ACF1(D)=−0.500 for the
near-kernel single-1 input too (it is fold-generic). The operative statistic is
**corr(S(n),S(n+1))**:

```
input        corr(S,S⁺¹)  Σ|ACF(D;k≥2)|  var(S)/var(D)  |S|
primes         −0.053          0.08          0.50        ~√n   good
iid p=0.5       0.018          0.15          0.51        ~√n   good
single-1 (ker)   0.956          3.0         158          ~1.3n  collapses
```

The single-1 near-kernel input has ACF1(D)≈−1/2 like the primes, yet |S|
grows linearly because its increments are long-range correlated — it *is* a
random walk (corr(S,S⁺¹)≈0.96). So density-1 holds iff S is white (non-random
walk), i.e. iff E[S²]=O(n), and the primes sit on the good side.

Why this is not a closed-door reopening: it is a property of the *output* S,
not a "h is complicated enough" input hypothesis — the single-1 input is
maximally simple and collapses. It says what the primes' arithmetic input must
buy (white increments), it does not prove they have it. The unconditional open
barrier is unchanged.
