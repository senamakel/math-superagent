# Sieve upper bound on the structured progression {4pk+1 : k in S_3^(≤3)}

```approach
idea: Attack Conjecture 24 (the divisor log-mass bound) directly, by running an
  upper-bound sieve on the structured progression of admissible primitive
  divisors r = 4pk+1 with k ∈ S_3^{(≤3)}, and converting Ford's power-saving
  thinness of the 3-Higgs semigroup into an explicit δ > 0 in
  Σ_{admissible r} log r ≤ (2 log 2 − δ) p.
mechanism: Φ_{4p}(2) = (2^{2p}+1)/5, so every prime r | Φ_{4p}(2) is primitive
  with ord_r(2) = 4p and r ≡ 1 (mod 4p); the non-primitive part of 2^{2p}+1 is
  O(log(4p)) (Hong, catalogued), so the primitive divisors must carry log-mass
  2p log 2 − O(log p). A primitive divisor is "admissible" (i.e. could still be
  3-Higgs) exactly when (r−1)/4p = k ∈ S_3^{(≤3)}; any other primitive divisor is
  non-3-Higgs and already closes 2p ∈ H_even. Conjecture 24 is the statement that
  the admissible set cannot carry all of this log-mass. The sieve route: the
  admissible r lie in the union over k ∈ S_3^{(≤3)} of the arithmetic
  progressions r ≡ 1 (mod 4pk). Brun–Titchmarsh gives
  #{r ≤ X : r ≡ 1 mod 4pk} ≤ 2X/(φ(4pk) log(X/4pk)), so summing over the
  semigroup,

      #{admissible r ≤ X} ≤ (2X/log X) · Σ_{k ∈ S_3^{(≤3)}, k ≤ X/4p} 1/φ(4pk).

  The inner sum is controlled by Ford's thinness of downward-closed prime sets:
  the counting function of S_3^{(≤3)} is ≪ Y^{1−η} for an absolute η > 0 (the
  paper's own Theorem 21 input). A power-saving count on k transfers, through
  Brun–Titchmarsh, to a power-saving count on admissible r, and then the
  log-mass identity Σ log r = ∫ log t dN(t) yields a genuine deficit
  δ = 2 log 2 · η' > 0. This is a *divisor-level* upper bound (congruence
  r ≡ 1 mod 4p on the prime support of one fixed integer), not a Chebotarev
  density over a range of primes — which is exactly the distinction the paper's
  §5.3 draws, and exactly why the closed density/rarity arguments do not reach
  here. Named machinery: Brun–Titchmarsh inequality, the Selberg/large sieve for
  primes in arithmetic progressions, and Ford's thinness theorem (already in the
  library as `ford-thinness-downward-closed-primes`).
status: proposed
first-step: (1) Recompute the exact thinness exponent η of S_3^{(≤3)} by direct
  enumeration for k up to 10^8 (independent of the paper), confirming the
  ≪ Y^{1−η} power saving. (2) State the resulting upper bound on
  #{admissible r ≤ X} with explicit constants and identify the level of
  distribution of the APs r ≡ 1 mod 4pk that Brun–Titchmarsh requires. (3) Derive
  the δ in C24 as a function of η, and check whether the constants leave δ > 0.
```

## Notes for the research check

- **Distinct from the closed density/rarity arguments**: the closed ones
  (`stewart-size-elimination`, `heven-thinness-not-finiteness`) confused
  thinness with boundedness and used *global* counting of H. This one produces a
  *log-mass deficit* on the admissible divisor set via a power-saving *count*
  transferred through an explicit congruence `r ≡ 1 mod 4pk`, which is the exact
  shape of Conjecture 24. It targets δ, not "smallness".
- **Falsifier**: if the semigroup count `Σ 1/φ(4pk)` over `k ∈ S_3^{(≤3)}` does
  *not* carry a power saving (only a logarithmic/reciprocal-mass one), the
  Brun–Titchmarsh transfer produces no δ and the approach gives nothing new.
- **Cost**: everything here is a *counting* estimate; no factorization of
  `2^{2p}+1` beyond the trivial `(2^{2p}+1)/5` is required. That is the point:
  it bounds the admissible divisors without finding them.
- Speculative level: low-medium (standard sieve, but the semigroup-restricted AP
  count is a real open sub-problem — possibly at the boundary of
  Bombieri–Vinogradov; research should check whether "primes of the form
  `mk+1` with `k` in a multiplicative semigroup" has existing bounds).
