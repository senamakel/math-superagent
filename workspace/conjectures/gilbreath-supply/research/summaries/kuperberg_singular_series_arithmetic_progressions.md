# Summary — Sums of singular series along arithmetic progressions and with smooth weights

Author: Vivian Kuperberg.
Source: arXiv:2301.06095 [math.NT], Jan 2023.
Source URL: https://arxiv.org/pdf/2301.06095
Full text: `research/sources/kuperberg_singular_series_arithmetic_progressions.full.md`

## What this source establishes

Studies constrained sums of the Hardy–Littlewood singular series S(H) = ∏_p (1−ν_H(p)/p)/(1−1/p)^k,
and of the "fully subtracted" sums S₀(H) = Σ_{J⊂H}(−1)^{|H\J|}S(J) (which kill the main term so
lower-order contributions become visible), where the sets H are constrained either to arithmetic
progressions mod r or by smooth weights.

**Background it builds on (and cites correctly).** Montgomery–Soundararajan (2004) [7] showed
Σ_{H⊂[1,h],|H|=k} S₀(H) = μ_k(−h log h + A)^{k/2} + O(h^{k/2−1/(7k)+ε}), μ_k = 1·3·…·(k−1) for k even,
0 for k odd, A = 2−γ₀−log 2π. This was the engine behind the Gaussian/Poissonian fluctuation
results. The present paper develops the analog when H is restricted to residue classes mod r or by
smooth weights — precisely the objects in LOS's heuristic for consecutive-prime pair bias.

**Direct LOS connection.** LOS conjecture that π(x;q,(a,b)) (consecutive primes p ≡ a, next ≡ b mod q)
∼ (1/q)∫ α(y)ε_q(a,b)(q/φ(q) log y)² D(a,b;y) dy, where D(a,b;y) is a sum over h ≡ b−a mod q of
co-subsets weighted by S₀,q(A∪T). LOS estimated D by a weighted version of R₂(h;r,c₁,c₂). **This paper
generalises to R_k(h;r,c₁,…,c_k) for all k** — necessary for LOS's error terms.

**Main results.**
- **Theorem 1.1**: For the related quantity V_k(q,h;r,c₁,…,cₖ) (qi restricted to divide a secondary
  modulus q) the leading term is a sum over perfect matchings σ ∈ B_k of ∏_{(i,j)∈σ} V₂(q,h;r,cᵢ,cⱼ),
  with error O_{r,k}(h^{k/2−1/(7k)}(q/φ(q))^{2k+k/2}). Only even k have nonzero matching terms (B_k = ∅
  for k odd).
- **Theorem 1.2**: R_k(h;r,c₁,…,cₖ) is governed by **incidences among the cᵢ mod r** — the pairing of
  indices whose residue classes coincide. Concretely, if #̃B(c₁,…,cₖ) counts the pairings of the cᵢ with
  every pair equal, then
  > R_k(h;r,c₁,…,cₖ) = #̃B(c₁,…,cₖ)(−hφ(r)/r · log h + C₀(r)h)^{k/2} + O_{r,k}(h^{k/2}(log h)^{k/2−1}),
  and in general R_k ≪_{r,k} h^{k/2}(log h)^{k/2}. The main term's value depends on the precise
  arrangement of the cᵢ (not just their counts). When all cᵢ are congruent mod r it recovers
  Montgomery–Soundararajan Thm 2 with #̃B = μ_k.
- The smooth-weight version (10)–(13): the leading term is again a sum over perfect matchings, each
  (i,j) ∈ σ contributing an interaction of f_i, f_j via their Fourier transforms/Poisson summation.

## Why it matters for SUPPLY / the reopened question

This makes the **higher-order (K≥2)** bias structure of consecutive-prime residue patterns rigorous
through singular-series sums along arithmetic progressions. The reopened question asks exactly whether
a functional of the fold sensitive to correlation order 1 < K ≲ n/2 can be controlled by an arithmetic
input strictly weaker than pointwise mod-4 switch density. This paper is the arithmetic-side machinery
for just such higher-order inputs: R_k(h;r,c₁,…,cₖ) gives the size of k-fold residue-constrained sums,
with the leading term governed by the *incidence/pairing* pattern of the residue classes mod r — a
genuinely K≥2 structure (not the K=1 switch density, which is about immediate equal-vs-differing pairs).

**Cautions (interpretive, not claims).** The statements are averages over many primes / over h and
moduli; SUPPLY needs a fixed-prefix statement. The transfer from these averaged singular-series sums to
wt(Φ_n h) for the fixed gap-parity string is not made in this source. Kuperberg's results are about the
*singular series side* (where all residues are admissible); the fold reads binary-submask structure, so
the bridge to Φ is the run's own open step.

## Evidence class

Proved theorems (fixed k, h → ∞, explicit errors). Bearing on SUPPLY is interpretive.

```claim
id: kuperberg-singular-series-along-arithmetic-progressions
statement: The k-fold sums R_k(h;r,c_1,...,c_k) of subtracted singular series over sets in fixed residue
  classes mod r have leading term governed by the incidences (pairings with equal residue) among the c_i
  mod r: R_k = #B~(c_1,...,c_k)(-h phi(r)/r log h + C_0(r)h)^{k/2} + O(h^{k/2}(log h)^{k/2-1}); and R_k
  ≪ h^{k/2}(log h)^{k/2} in general. Generalises Montgomery-Soundararajan (all c_i congruent reduces to
  their Thm 2); extends the LOS consecutive-prime bias heuristic from pairs (R_2) to all orders k.
hypotheses: Hardy-Littlewood k-tuples framework; fixed k, r, residue classes; h → oo; q squarefree (r,q)=1.
holds-here: provides the arithmetic machinery for K>=2 residue-constrained inputs beyond the K=1 switch
  term; the bridge to the fixed-prefix fold wt(Phi_n h) is NOT made by this source (averages over h/r only).
status: proved (Kuperberg 2023, arXiv:2301.06095).
bearing: candidate arithmetic input for GOAL priority 2 — higher-order (K>=2) residue structure, rigorous,
  strictly beyond the K=1 switch term; but transfer from averaged singular-series sums to the fixed
  gap-parity prefix is open and is the run's own step.
anchor: arXiv:2301.06095, Thms 1.1, 1.2, eqs (4)-(13), Introduction LOS connection.
```
