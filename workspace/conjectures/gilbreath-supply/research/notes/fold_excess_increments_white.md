# Fold-excess S is near-white (non-random-walk); the collapse witnesses are random walks

```claim
id: fold-excess-increments-white
statement: >
  Let S(n) = (n−2) − 2·ν₂(n) be the signed excess of the floored submask fold.
  The operative discriminator between the density-1-SUPPLY inputs and the
  collapse witnesses is corr(S(n), S(n+1)) — equivalently the vanishing of ALL
  higher-lag increment autocorrelation — NOT the lag-1 increment ACF1(D), which
  is −1/2 fold-generic. Measured (exact): primes corr(S,S⁺¹)=−0.053, iid
  0.018, Σ|ACF(D;k≥2)|=0.08 and 0.15, var(S)/var(D)=0.500 and 0.512 (good,
  white, varS=O(n)); single-1 near-kernel corr=0.956, Σ|ACF k≥2|=3.0,
  varS/varD=158, |S|~1.3n (a near-perfect random walk, collapses). For the
  primes, ACF1(D) settles to −1/2 as N grows (−0.508@1000→−0.5009@40000) and
  var(S)/var(D)→1/2 from below (0.477@2000→0.500@40000).
hypotheses: canonical floored fold ν₂=wt(Φ_n h); S=(n−2)−2ν₂ exact; primes
  n≤40000 from guard-checked JSON; iid/single-1 via exact SOS fold n≤3000.
holds-here: yes (measured; exact integer/ratio arithmetic).
status: measured-not-proved — the infinite-n whiteness of the primes'
  increments is an unproved arithmetic statement about h.
bearing: >
  Nails the mechanism behind the second-moment plateau: density-1 SUPPLY's
  input E[S²]=O(n) holds iff S is a non-random-walk (corr(S,S⁺¹)≈0, white
  increments), which the primes and iid have and every collapse witness lacks.
  Corrects the naive "ACF1=−1/2 is the structure" reading (ACF1 is fold-generic,
  shared by the near-kernel single-1). Consistent with the closed doors: it is a
  property of the OUTPUT S, not a "h is complicated enough" input hypothesis.
  The unconditional proof that the primes' increments stay white is the open
  arithmetic barrier, unchanged.
anchor: code/out/pattern_finder_deliverable.md
```
