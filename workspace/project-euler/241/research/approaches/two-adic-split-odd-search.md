# 2-adic separation: reduce to odd-number search with explicit v2 tracking

```approach
idea: Analytically factor the 2-adic part: for each a = v2(n) and each k, solve σ(u)/u = T_{a,k} over odd u only, where T_{a,k} = (2k+1)·2^{a-1}/(2^{a+1}-1) and the constraint v2(σ(u)) = a-1 is tracked incrementally
mechanism: Write n = 2^a·u with u odd. The half-integer condition 2σ(n) = (2k+1)n forces v2(σ(u)) = a-1 and the exact rational identity σ(u)/u = (2k+1)·2^{a-1}/(2^{a+1}-1). This is already verified on all 8 known hemiperfects ≤ 3e7 (code/verify_2adic.py). The crucial structural consequence: once a and k are fixed, the target T_{a,k} has an odd denominator D = (2^{a+1}-1) and odd numerator N = (2k+1)·2^{a-1}. Since u is odd, σ(u) is odd (every σ(p^e) for odd p is odd), so all arithmetic stays in odd integers. The search enumerates odd u = ∏ p_i^{e_i} (p_i odd) with two constraints: (1) the multiplicative abundancy condition σ(u)/u = T_{a,k}, and (2) the 2-adic valuation condition ∑ v2(σ(p_i^{e_i})) = a-1. Constraint (2) is a sum over small known values — each odd prime power's σ(p^e) has a known v2 — and can be tracked incrementally during the search. This is genuinely different from the denominator-cancellation DFS: it eliminates the prime 2 from the search space entirely, replaces the rational-residual tracking with two separate constraints (one rational, one 2-adic), and exploits the fact that for each a the target is a fixed rational with known denominator, so the forcing logic simplifies to "denominator D must divide u" and the only primes that can appear are odd primes whose σ-values contribute the needed v2.
status: grounded (correct and literature-backed, but NOT a genuinely new direction)

## Verdict (checked against the literature)

The identity σ(u)/u = T_{a,k} is **correct and independently settled in the literature**, but the approach is **not novel** and its distinctive second constraint is **redundant**.

- T_{a,k} = (2k+1)·2^{a-1}/(2^{a+1}-1) with 2^{a+1}-1 = σ(2^a) is just the abundancy-multiplicativity split σ(n)/n = [σ(2^a)/2^a]·[σ(u)/u] = (2k+1)/2 solved for σ(u)/u. Confirmed on the 8 known hemiperfects by code/verify_2adic.py.
- The v2-of-odd-prime-powers formula used as constraint (2) is published **verbatim** as Theorem 1.1 of Amdeberhan–Moll–Sharma–Villamizar, J. Number Theory 223 (2021) 325–349 (arXiv:2007.03088): v2(σ(p^α)) = 0 if α even, = v2(p+1)+v2(α+1)−1 if odd. Claim `ams-2adic-sigma-formula`. So constraint (2)'s content is published.
- The D | u forcing fact is claim `property22-denominator-divides` (Holdener–Stanton).

### Answer to the three questions

**(1) No published theorem bounds a = v2(n) for hemiperfects.** The bound used is elementary, derived here from the approach's own denominator constraint: σ(u)/u = N/D (lowest terms) with D | u and u ≤ LIMIT/2^a, so 2^a·D_reduced ≤ 10^18. Since gcd(2k+1, 2^{a+1}-1) ≤ 11 for k=1..5, D_reduced ≈ 2^{a+1}/1 and **a ≲ 30 for all reachable (a,k) below 10^18 — not the 60 the first-step wrote**. The empirical 2-exponents in A088912/Michon–Marcus hpn tables (a=1,3,4,?,11,23 for 3/2..13/2) grow with k; no theorem caps them. The a-bound is a self-derived gap-filler, not a literature result.

**(2) The "separate v2-tracking" is redundant, so no such published split exists as a distinct algorithm.** Cross-multiply σ(u)(2^{a+1}-1) = (2k+1)2^{a-1}u and take v2: since 2^{a+1}-1, 2k+1, u are all odd, v2(σ(u)) = a−1 immediately. **Constraint (2) is a theorem-consequence of constraint (1) — there is one constraint, not two.** The reduction to a per-(a,k) odd-u search is exactly the standard denominator-cancellation DFS (cirosantilli PE241; Ross Millikan math.SE) with the first prime's exponent fixed — the prime 2 is just a tree node whose depth is a. No published named algorithm splits hemiperfects this way, precisely because it is not a separate mechanism.

**(3) Flammenkamp's effective exponent does subsume the 2-adic mechanism.** For multiply perfect numbers, Helenius's effective exponent (wwwhomes.uni-bielefeld.de/achim/mpn.html): because p−1=1 at p=2, 2^k carries σ(2^k)=2^{k+1}-1 whose prime factors may generate further 2-powers, reducing the two-power deficit the rest of n must supply. The hemiperfect 2^{a+1}-1 | u is the same phenomenon (companion odd factor of the 2-power supplied by the odd part). Flammenkamp states it structurally, not as T_{a,k}, so it is the concept-precedent, not a literal hemiperfect formula (claim `flammenkamps-tree-search-method`).

### Bottom line
Grounded and correct, but **not novel**: it is the standard forced-denominator DFS re-derived with a,k explicit and the prime 2 hoisted out; v2(σ(u))=a−1 is redundant (follows from the rational target); the a-range should be ~1..30 (elementary D|u bound), not 1..60. For the PE 241 answer it adds nothing hemiperfect_dfs.py does not already do per-target; treat as alternative bookkeeping of the same tree, not a separate direction. Any improvement-over-DFS claim rests on the redundant v2 cut and should not be relied on.

precedent:
- https://www.sciencedirect.com/science/article/abs/pii/S0022314X20303449 (AMSV, JNT 223 (2021) 325-349; arXiv:2007.03088) — Thm 1.1 v2(σ) over odd prime powers; claim `ams-2adic-sigma-formula`, anchor research/summaries/amd_2adic_sigma.md
- http://wwwhomes.uni-bielefeld.de/achim/mpn.html (Flammenkamp/Helenius) — effective-exponent analysis, mechanism precedent (MPN twin); claim `flammenkamps-tree-search-method`
- https://arxiv.org/abs/2601.17832 (Alekseyev) — general RES tree over all of n; no odd-split, shows full-n tree is already efficient
- https://raw.githubusercontent.com/cirosantilli/project-euler-solutions/master/solvers/241.md — standard PE241 solver this approach reformulates; research/summaries/pe241_technique.md
- Holdener–Stanton, JIS 10 (2007) 07.9.6 — property22-denominator-divides (D | u)

killed-by: none (approach correct); the *novelty* claim is refuted — (2) follows from (1), and the split is the standard DFS with 2 fixed.

first-step (revised): For each a from 1 to 30 (elementary D|u bound replaces 60) and k from 1 to 5, reduce T_{a,k}; if 2^a·den > 10^18 skip. DFS over odd primes vs the single rational constraint σ(u)/u = T_{a,k} (drop the v2 cut as redundant: it is automatic). Validate against the brute oracle.
```