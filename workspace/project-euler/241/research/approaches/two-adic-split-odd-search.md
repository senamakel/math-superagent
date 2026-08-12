# 2-adic separation: reduce to odd-number search with explicit v2 tracking

```approach
idea: Analytically factor the 2-adic part: for each a = v2(n) and each k, solve σ(u)/u = T_{a,k} over odd u only, where T_{a,k} = (2k+1)·2^{a-1}/(2^{a+1}-1) and the constraint v2(σ(u)) = a-1 is tracked incrementally
mechanism: Write n = 2^a·u with u odd. The half-integer condition 2σ(n) = (2k+1)n forces v2(σ(u)) = a-1 and the exact rational identity σ(u)/u = (2k+1)·2^{a-1}/(2^{a+1}-1). This is already verified on all 8 known hemiperfects ≤ 3e7 (code/verify_2adic.py). The crucial structural consequence: once a and k are fixed, the target T_{a,k} has an odd denominator D = (2^{a+1}-1) and odd numerator N = (2k+1)·2^{a-1}. Since u is odd, σ(u) is odd (every σ(p^e) for odd p is odd), so all arithmetic stays in odd integers. The search enumerates odd u = ∏ p_i^{e_i} (p_i odd) with two constraints: (1) the multiplicative abundancy condition σ(u)/u = T_{a,k}, and (2) the 2-adic valuation condition ∑ v2(σ(p_i^{e_i})) = a-1. Constraint (2) is a sum over small known values — each odd prime power's σ(p^e) has a known v2 — and can be tracked incrementally during the search. This is genuinely different from the denominator-cancellation DFS: it eliminates the prime 2 from the search space entirely, replaces the rational-residual tracking with two separate constraints (one rational, one 2-adic), and exploits the fact that for each a the target is a fixed rational with known denominator, so the forcing logic simplifies to "denominator D must divide u" and the only primes that can appear are odd primes whose σ-values contribute the needed v2.
status: grounded
first-step: For each a from 1 to 60 and each k from 1 to 5, compute T_{a,k} = (2k+1)·2^{a-1}/(2^{a+1}-1) in lowest terms. For each, if the denominator D exceeds 10^18/2^a, skip (no u can exist). Then implement a DFS over odd primes only, tracking both the rational residual Q = T·u/σ(u) and the accumulated v2(σ(u)). Prune when v2(σ(u)) > a-1 (overshoot) or when the maximum possible additional v2 from remaining prime powers cannot reach a-1. Validate against the brute oracle at small bounds.
precedent: [Amdeberhan–Moll–Sharma–Villamizar, "Arithmetic properties of the sum of divisors", J. Number Theory 223 (2021) 325–349, arXiv:2007.03088](https://www.sciencedirect.com/science/article/abs/pii/S0022314X20303449) — Theorem 1.1 (2-adic valuation of σ depends only on the odd part; per-prime-power formula) and Theorem 1.3 (sharp bound v2(σ(n)) ≤ ⌈log₂ n⌉). Claim ids: ams-2adic-sigma-formula, a242484-equivalence, a159907-sequence-even; corroborated by flammenkamps-tree-search-method (Fred Helenius effective 2-power exponent).
```

## What the literature says

The reformulation is the **2-adic / parity structure of the divisor-sum function**, named
and proved by **Amdeberhan–Moll–Sharma–Villamizar** (J. Number Theory 223 (2021) 325–349;
arXiv:2007.03088). It is not a new idea of this run — it is the classical parity fact that
governs hemiperfect/multiperfect searches, and it is exactly what Flammenkamp's
multiply-perfect tree-search and the run's own verify_2adic.py use.

**Precise statements (from the source):**

- *Theorem 1.1.* ν₂(σ(n)) depends only on the odd part of n. For n = ∏ p_i^{α_i} with p_i
  odd and α_i = ν_{p_i}(n): ν₂(σ(n)) = Σ_i ν₂(σ(p_i^{α_i})), where for odd p and α ≥ 1:
  - if α is even, σ(p^α) is odd, so ν₂(σ(p^α)) = 0;
  - if α is odd, ν₂(σ(p^α)) = ν₂(p+1) + ν₂(α+1) − 1.
- *Theorem 1.3 (sharp bound).* ν₂(σ(n)) ≤ ⌈log₂ n⌉, with equality iff n is a product of
  distinct Mersenne primes.

**Do the hypotheses hold here?** Yes. For PE 241, 2σ(n) = (2k+1)n with n = 2^a·u (u odd)
forces 1 + ν₂(σ(n)) = a, i.e. **ν₂(σ(n)) = a − 1**, and by Theorem 1.1 that valuation is
the sum over the odd prime powers of u of their ν₂(σ(p^α)) = ν₂(p+1)+ν₂(α+1)−1 (α odd) or 0
(α even). This is the run's verified identity σ(u)/u = (2k+1)·2^{a−1}/(2^{a+1}−1). The
claim a159907-sequence-even (all hemiperfects even) is itself an immediate corollary: an
odd half-integer abundancy would force a 2 in the numerics that σ(n)/n must supply, which
odd n cannot.

**Has anyone applied this to the problem family?** Yes — it is the *standard parity gate*
in every tree-search for σ(n)=bn+c numbers. Flammenkamp's multiply-perfect search
(flammenkamps-tree-search-method) tracks exactly this 2-power ("Fred Helenius' effective
exponent": how many further powers of 2 the remaining prime powers must generate). The
Alekseyev 2026 method (Section 3.3 "Case of odd σ") uses the parity of a', b', c' to
detect odd-square or twice-square structure — the same 2-adic idea in the aσ(n)=bn+c
framework. OEIS A242484 (a242484-equivalence) expresses the evenness side.

**What it would buy:** factoring the prime 2 out of the search entirely. For each fixed
(a, k) pair the target T_{a,k} has a fixed odd denominator D = 2^{a+1}−1, so the forcing
("denominator D must divide u") is cleaner and the 2-adic valuation constraint
Σ ν₂(σ(p^e)) = a−1 is a cheaply-tracked incremental sum that prunes long before the
rational residual does. It is a genuine reduction of the search space; it does not by
itself prove completeness (the recursive multiplicity/abundancy still has to be closed by
the DFS or wheel), but it is a provably valid exact restatement.

**Caveat (honest thin spot):** the exact identity σ(u)/u = (2k+1)2^{a−1}/(2^{a+1}−1) is this
run's own derivation, verified on the 8 known small hemiperfects; the *source* proves the
ν₂(σ(p^α)) decomposition and the ν₂(σ(n))=a−1 consequence, which is the load-bearing part.
I found no single paper that presents the "enumerate odd u by (a,k) target" split as a
standalone named algorithm; it is presented in the literature as a constraint piped into
the tree-search, which is exactly how this run uses it.

## Precedent / claim ids
- arXiv:2007.03088 / J. Number Theory 223 (2021) 325–349 (Thm 1.1, 1.3). Claim ams-2adic-sigma-formula.
- flammenkamps-tree-search-method (effective 2-power exponent in MPN search).
- a242484-equivalence; a159907-sequence-even (evenness / antisigma equivalence).
- Section 3.3 of Alekseyev arXiv:2601.17832 (parity/squarish pruning in aσ(n)=bn+c).
