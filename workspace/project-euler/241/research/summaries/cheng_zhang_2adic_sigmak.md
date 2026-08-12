# On the 2-adic valuation of σ_k(n) — Cheng & Zhang (2026)

**Source:** Kaimin Cheng, Ke Zhang, "On the 2-adic valuation of σ_k(n)",
arXiv:2603.11979 [math.NT], 12 Mar 2026. 8 pages.
Full text: `research/sources/cheng_zhang_2adic_sigmak.full.md`.

## What it establishes

For σ_k(n) = Σ_{d|n} d^k and ν_p(m) the exponent of p in m:

- **Theorem 1.1 (explicit 2-adic formula).** For n = 2^a·Π p_i^{α_i} with p_i
  distinct odd primes,
  ν₂(σ_k(n)) = Σ_{i: α_i odd} (ν₂(α_i+1) + ν₂(p_i^k + 1) − 1).
  In particular ν₂(σ_k(2^a)) = 0 (Lemma 2.1), so **ν₂(σ_k(n)) depends only on
  the odd part of n** (Lemma 2.2).
- **k odd:** ν₂(σ_k(n)) = ν₂(σ(n)) for all n (Prop. 3.1 — the same AMSV
  formula), and ν₂(σ_k(n)) ≤ ⌈log₂ n⌉ with equality iff n is a product of
  distinct Mersenne primes (Thm 3.2).
- **k even:** ν₂(σ_k(n)) = Σ_{α_i odd} ν₂(α_i+1) ≤ ⌊log₂ n⌋, with equality iff
  n = 3 (Thm 3.5).

## What it adds to this library

1. **Independent, peer-review-track corroboration of the governing 2-adic
   constraint.** PE 241's condition σ(n)/n = (k+1/2) — i.e. 2σ(n) = (2k+1)n —
   is the k=1 (odd) case, and k=1 is exactly AMSV's theorem. This paper proves
   the same formula from the LTE lemma with full proofs, so the claim
   `ams-2adic-sigma-formula` now has two independent published derivations.
2. **History of the hypothesis-removal chain** (from its introduction): AMSV
   (2020/21) proved the odd-prime bounds only conditionally; Zhao & Chen
   (Front. Math. 20 (2025) 795–827) removed the conditions, proving
   ν_p(σ(n)) ≤ ⌈log_p n⌉ for every odd prime p and n ≥ 2 and determining all
   equality cases for p < 10^5; Zhao (Bull. Austral. Math. Soc., 2026,
   doi:10.1017/S000497272510083X) proved ν_p(σ_k(n)) ≤ ⌈k log_p n⌉. These are
   the named results the run's 2-adic reduction stands on, beyond the
   encyclopedic tier.
3. Confirms the AMSV journal reference as J. Number Theory 223 (2021) 325–349
   (matching `research/summaries/amd_2adic_sigma.md`).

## What it does NOT do

It is a valuation bound/formula paper: it does not enumerate hemiperfect
numbers, does not mention hemiperfect numbers at all, and gives no bound on
how many n ≤ 10^18 have σ(n)/n half-integer. That is the role of the
Alekseyev aσ(n)=bn+c machinery and the A088912 reachability data, already in
the library. This paper only cements the 2-adic structural fact the DFS uses
to fix the exponent of 2 in each target search.

```claim
id: cheng-zhang-2adic-sigmak
statement: For n = 2^a * prod p_i^{alpha_i} (p_i distinct odd primes), v2(sigma_k(n)) = sum_{i: alpha_i odd}(v2(alpha_i+1) + v2(p_i^k+1) - 1); the k odd case reduces to v2(sigma_k(n)) = v2(sigma(n)) (the AMSV formula) with v2(sigma_k(n)) <= ceil(log2 n), equality iff n is a product of distinct Mersenne primes. In particular v2(sigma_k(2^a)) = 0, so v2(sigma_k(n)) depends only on the odd part of n.
hypotheses: k >= 1 integer, n >= 2; sigma_k multiplicative; LTE lemma applies to the geometric-sum quotient
holds-here: yes — k=1 is the PE241 case: 2*sigma(n) = (2k+1)n forces v2(sigma(u)) = a-1 where u is the odd part, exactly the content of the theorem (and of claim ams-2adic-sigma-formula, which this independently corroborates)
status: proved in Cheng–Zhang 2026 (arXiv:2603.11979), Thms 1.1, 2.4, 3.2; independent derivation of the AMSV formula
bearing: second independent published derivation of the 2-adic structure the denominator-cancellation DFS relies on; confirms the AMSV citation details and maps the Zhao–Chen/Zhao hypothesis-removal chain
anchor: research/summaries/cheng_zhang_2adic_sigmak.md
answers: theory-numbers-with-88d5
```