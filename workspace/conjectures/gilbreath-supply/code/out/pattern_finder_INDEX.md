# Fold-excess increments white — pattern-finder deliverable and claim

Pattern-finder's final deliverable and the claim that records it. The result:
the fold-excess fluctuation `S(n) = (n−2) − 2·ν₂(n)` is a **non-random-walk**
(corr(S(n),S(n+1)) ≈ 0, white increments with ACF1(D) → −1/2 and all
higher-lag autocorrelation vanishing), so `var(S) = O(n)` — the second-moment
input for density-1 SUPPLY.

The discriminator from the collapse witnesses (single-1, alternating,
Thue-Morse) is corr(S,S⁺¹)≈0 (good) vs ≈1 (bad / random walk, |S|~linear),
NOT ACF1(D)=−1/2 which is fold-generic. Computed exactly over the
guard-checked N=40000 primes JSON plus exact-SOS iid/single-1 comparisons;
all numbers exact integer/ratio arithmetic. The infinite-n whiteness for the
primes is a conjecture to derive (open arithmetic barrier), not a proof.
