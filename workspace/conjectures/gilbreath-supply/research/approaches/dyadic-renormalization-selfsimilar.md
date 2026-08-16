# The fold is self-similar under dyadic renormalization — a fixed-point identity S = Σ_g Fold(τ_g)

```approach
idea: >
  The fold is self-similar under dyadic renormalization. For each scale
  g = ν₂(d+1), the run telescope collapses depth d to an XOR over the
  renormalized switch sequence τ_g(j) = [q_j ≢ q_{j+2^g} mod 4] =
  [χ(q_j) ≠ χ(q_{j+2^g})], read at coarsened positions 2^g·t with t ranging
  over the submask down-set of d' = ⌊d/2^g⌋. Hence the scale-g stratum of
  S(n) = Σ_d (−1)^{T(n,d)} is, up to a shift, the SAME fold applied to τ_g at
  coarser resolution. With ν₂(n) = (n−2−S(n))/2, SUPPLY becomes a fixed-point
  (renormalization-group) identity S(n) = Σ_g Fold(τ_g)(window), and the
  conjecture is the statement that the renormalization operator preserves
  linear fold weight.

mechanism: >
  Change of representation: from "one character sum" to "one summand per dyadic
  scale, each the same object at coarser scale" — a renormalization-group /
  self-similarity statement, not a concentration inequality and not a block
  recursion. Two predecessors are distinguished precisely: (a) the refuted
  dyadic-martingale route tried to bound each scale with Azuma/Burkholder
  (impossible for a deterministic string); (b) the refuted pascal-cascade route
  tried a 2×2 block recursion on the anti-diagonal slice Φ_n (the slice does not
  carry it). Here NO concentration and NO block recursion is claimed. The
  identity is EXACT and uses only the run decomposition of ↓d (G-run-telescope,
  standard): for g = ν₂(d+1) the down-set ↓d is a union of 2^{pc(d)−g} runs of
  length 2^g, the run starts are 2^g·t for t ⊆ d' with d' = ⌊d/2^g⌋, and
  telescoping over one run gives a single switch indicator of the residue string
  at distance 2^g. Therefore

      T(n,d) = ⊕_{t ⊆ d'} τ_g(n−1−d + 2^g·t),   τ_g(j) = [s_j ≠ s_{j+2^g}],
      s_j = χ(q_j) = (−1/q_j).

  So the scale-g stratum S_g(n) = Σ_{d:ν₂(d+1)=g} (−1)^{T(n,d)} is exactly the
  zeta/fold transform of the renormalized string τ_g on the coarsened window, and
  S(n) = Σ_g S_g(n). The load-bearing new fact is the RENORMALIZED INPUT: τ_g is
  the gap-parity string of the SAME residue sequence s read at distance 2^g, so
  the problem is self-similar — the fold applied to the distance-2^g switches.
  A bootstrap then asks for the weakest statement about τ_g under which
  Fold(τ_g) has linear weight; because the scales enter ADDITIVELY, the needed
  input is an average over g of the fold-weight of τ_g, strictly weaker than any
  single g (in particular weaker than the g=0 adjacent switch density).
  Speculative half: whether Σ_g Fold(τ_g) can be bounded below by a bootstrap
  without pointwise control of any τ_g — this is exactly what must be priced.
  Hand-checked on d=2 (g=0, d'=2, two singleton runs), d=3 (g=2, d'=0, one run
  of length 4), d=5 (g=1, d'=2, runs {0,1},{4,5}) and d=6 (g=0, d'=6, four
  singletons).

first-step: >
  tool_builder, exact F₂/integer arithmetic only, no number theory beyond the
  real residue string r_j = q_j mod 4: (1) machine-verify
  T(n,d) = ⊕_{t ⊆ d'} τ_g(n−1−d + 2^g·t) with g = ν₂(d+1), d' = ⌊d/2^g⌋,
  against brute submask-XOR for n ≤ 200 and ALL d ∈ [2,n−1], on the real prime
  string and on random {1,3} controls; (2) print the per-scale partial sums
  S_g(n) and verify Σ_g S_g(n) = S(n); (3) for each g compute τ_g and confirm
  S_g(n) equals Fold(τ_g) on the coarsened window. Falsifier: if S_g(n) is not
  the fold of τ_g, the RG route is dead. If it holds, the bootstrap question is
  isolated and ready for a theorem pass.
status: refuted
killed-by: >
  The proposed machinery is a renormalization in NAME only, and the exact
  identity it rests on already reduces to the parity barrier at the coarsest
  scale. Two independent defects, either alone fatal.
  (1) There is no fixed-point / scale-invariance equation to bootstrap. The
  identity S(n) = Σ_g Fold(τ_g) decomposes S(n) additively over scales, but each
  scale-g stratum S_g(n) = Σ_{d:ν₂(d+1)=g} (−1)^{T(n,d)} is the fold of τ_g at
  the ORIGINAL resolution (τ_g is read at the SAME positions j = q_j mod 4, only
  at separation 2^g), not a coarser copy of itself. A renormalization-group
  bootstrap converts a fixed point of a renormalization operator into a global
  statement; here there is no RG operator mapping scale-g to scale-g+1, so
  "average over g of Fold(τ_g)" is not a consequence of any scale self-similarity,
  it is just an average of different objects. The route's own speculative half
  admits this: a lower bound on the SUM from a lower bound on the AVERAGE over g
  needs each Fold(τ_g) to be comparable, which is exactly what the absence of an
  RG equation fails to give. (2) The weakest input that would make any single
  τ_g's fold large is the switch correlation at separation 2^g, and for g=0 that
  is the adjacent switch correlation — the named open parity barrier
  (research/CLAIMS.md abgs-p1-wide-open, lau-nonconstant-pattern-open,
  ash_beltis_gross_sinnott_prime_residues §9 "cannot be treated using
  L-functions"). So the "strictly weaker than g=0" hope is exactly the claim
  that a bound on the average over g forces something on the g=0 term without
  pointwise control, and no RG identity supplies it. The exact decomposition is
  a correct lemma but it relabels the adopted dyadic-gap-character-correlation
  route (whose priced input IS the switch correlation τ_g); it is not a
  distinct engine. Refuted as a standalone route; the identity is kept as a
  lemma.
precedent: >
  The exact identity is already established inside this workspace (claim
  g-run-telescope-verified: the digital down-set ↓d of d ≤ 2^14 partitions into
  2^{popcount(d)−g} runs of length 2^g, each [m·2^g,(m+1)·2^g−1], and the fold
  telescopes over a run to the switch τ_g(j) = [r_{pos+j} ≠ r_{pos+j+2^g}];
  machine-verified on the real prime-residue string and 6 random controls).
  So the load-bearing identity is not new. What the literature does NOT supply
  is any fixed-point/self-similarity operator on this anti-diagonal slice or on
  the prime residue string: the only rule-90 / Pascal-mod-2 self-similarity
  that exists (Cardell–Fúster-Sabater, 10.1155/2019/2108014, binomial sequences /
  2-regular generators of the diagonals; Fine a₂(n)=2^popcount(n), Rowland
  arXiv:1001.1783, row weights; Hofer mod2-Pascal LU, claim
  hofer-mod2-pascal-thue-morse-structure; Bacher, claim bacher-pascal-det-mod2)
  lives on BLOCKS / rows / triangular regions, not on the anti-diagonal slice
  Φ_n or on scalar sums folded over a prime string — see the refutation of
  pascal-cascade-block-recursion, which is the same structural point. No source
  applies a renormalization-group identity to a deterministic fold of a prime
  residue string; the RG/self-similar CA literature (Edlund–Nilsson Jacobi,
  10.1007/s10955-010-9974-z) treats probabilistic CA dynamics, not deterministic
  character sums, and its fixed points are unrelated.
```

## Distinctness (not a restatement)

- Not `dyadic-martingale-azuma`: no filtration, no probability, no Azuma/Burkholder — the per-scale objects are combined by an exact algebraic identity, not bounded by concentration.
- Not `pascal-cascade-block-recursion`: no 2×2 block recursion on Φ_n; the self-similarity here lives in the run structure of ↓d (which the slice DOES respect), not in anti-diagonal blocks.
- Not `dyadic-gap-character-correlation` (adopted): that route keeps the single character sum S(n) and prices its correlations; this route decomposes S(n) into a sum of the same fold applied to renormalized inputs, turning the pricing question into a fixed-point/bootstrap question.
