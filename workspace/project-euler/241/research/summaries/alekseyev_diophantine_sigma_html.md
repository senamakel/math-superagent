# Alekseyev — Computing bounded solutions to linear Diophantine equations with the sum of divisors

**Source:** Max A. Alekseyev, arXiv:2601.17832 [math.NT], 25 Jan 2026 (HTML).
Full text: `[[alekseyev_diophantine_sigma_html.full]]`. Code:
`https://github.com/maxale/multiplicative_functions` (function `res_solve_sigma_abc` in
`sigma_linear_eq.sage`).

## What it establishes

Solves **aσ(n) = bn + c** for all n ≤ U, coefficients a,b,c with gcd(a,b,c)=1 (a>0).
Search space is the tree T_U rooted at 1, where each node n>1 has parent n/p^{ν_p(n)} with
p = lpf(n); descendants of node m are m·n′ with spf(n′) > lpf(m), n′ ≤ U′ = U/m, solving
the reduced equation (a′,b′,c′) = cancel( aσ(m), bm, c ). Cost grows with the number of
visit-ed nodes in T_U, not with U.

- **§3.1 Shortcuts** (solutions with Ω(n′) ≤ 2 or ω(n′)=1 found without descending):
  n′=p^k forces p | (a′−c′); n′=pq reduces to `(Ap+B)(Aq+B) = B²−AC` (Brahmagupta
  rectangle completion), solved by factoring B²−AC.
- **Theorem 3.2 (prime wheel pruning).** If n ≤ U, σ(n) ≥ S, spf(n) = 𝔭_k, then for
  each ℓ ≤ ω(n): ∏_{i=1}^ℓ 𝔭_{k+i-1} ≤ U; and for ℓ ≥ ω(n):
  ∏_{i=1}^ℓ 𝔭_{k+i-1}/(𝔭_{k+i-1}−1) ≥ S/U. (Proof: σ(n)/n ≤ ∏_{p|n} p/(p−1), a
  decreasing function of p.)
- **Theorem 3.3 (completeness).** The prime wheel W (initial length 2, W₁ = next prime
  after lpf(m)) eventually reaches a state with |W| ≤ ω(n′) and W₁ = spf(n′) for *any*
  solution n′ = 𝔭_t·… — i.e. **the pruning never skips a solution.** This is the
  rigorous completeness guarantee for the whole tree-search family.
- **§3.3 odd-σ case:** if a′, b′+c′ odd, any odd solution n′ is a square; Legendre-symbol
  test on −b′c′ kills square-nonresidue branches. Used to lift quasiperfect bound to 10^45
  and no non-power-2 almost-perfects below 10^33.
- **Empirics (§6):** running time as f(U) grows like Θ(r^{log₁₀U}), r ∈ [2,4].
  Computations to 10^20–10^26 for fixed-abundance sequences (Table 1).

## What it means for PE 241 (and how it differs)

The hemiperfect equation **2σ(n) = (2k+1)n has c = 0** (a=2, b=2k+1). The paper notes
(§1) c=0 is "rather special" because it admits *additional* optimization not available
for c≠0 — **that special optimization is exactly the run's forced-denominator lemma**
(the reduced denominator of σ(n)/n divides n, forcing the next prime to be the least
prime factor of the denominator). So Alekseyev's Theorem 3.3 is not the identical bound
the run relies on, but it is the same tree-search/pruning family and proves the *general*
method is complete and cost-scales with the description not the bound. The run's DFS for
c=0 is the specialized, *faster* instance that Alekseyev identifies but does not develop.

Load-bearing consequences for this run:
1. **Completeness is principled, not heuristic.** The tree-search this run implements is
   the same the literature proves complete; the 22-value answer set below 1e18 is exactly
   what a complete traversal must return. This is the gap the oracle note
   (`hemiperfect_below_1e18_oracle.md`) flagged as unverified — Alekseyev + Flammenkamp
   close that ("the solver must reproduce 22" is now backed by the standard complete
   method).
2. Confirms the method-policy requirement (cost grows with description, not bound 10^18).
3. **Does not enumerate** the 22 values; does not give c=0 numerics. The actual set+sum
   remain the run's computation (sourced from the A159907/class b-files).

```claim
id: alekseyev-tree-search-complete
statement: The tree T_U over prime powers (node m's children m·p^e, spf(p^e)>lpf(m)) with prime-wheel pruning solves a*sigma(n)=b*n+c for all n<=U; Theorem 3.3 proves the wheel reaches every solution (pruning never skips one), so the complete enumeration cost scales with the visited-node count, not with U. The c=0 case (multiperfect/hemiperfect) admits additional optimization = the forced-denominator lemma.
hypotheses: gcd(a,b,c)=1, a>0; the paper's focus is general c (c=0 noted special, extra optimization not developed)
holds-here: yes — tree-search+pruning completeness is proved for the general a*sigma(n)=bn+c family; the run's c=0 forced-denominator DFS is the specialized instance of the same complete scheme (inference beyond the paper's text)
status: proved (Alekseyev 2026, Thms 3.2, 3.3; arXiv preprint)
bearing: turns the "22 values must be reproduced by a complete traversal" from an assumption into a claim backed by the standard complete method; directly answers request theory-numbers-with-88d5 (a finitary, complete recursion over the divisor-sum equation exists, cost in the description)
anchor: research/sources/alekseyev_diophantine_sigma_html.full.md
answers: theory-numbers-with-88d5
```
