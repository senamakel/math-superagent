# Arithmetic properties of the sum of divisors

**Source:** Tewodros Amdeberhan, Victor H. Moll, Vaishavi Sharma, Diego Villamizar,
"Arithmetic properties of the sum of divisors", arXiv:2007.03088 [math.NT],
submitted 6 Jul 2020; published as J. Number Theory 223 (2021) 325–349,
doi:10.1016/j.jnt.2020.11.014.
Full text: `research/sources/amd_2adic_sigma.full.md`.

## What it establishes

For σ(n) = sum of divisors of n and ν_p(m) the exponent of the prime p in m:

- **Theorem 1.1 (2-adic formula).** ν₂(σ(n)) depends only on the *odd part* of n.
  Writing n = ∏ p_i^{α_i} with p_i odd and α_i = ν_{p_i}(n), the sum-of-divisors
  function over the prime power factors satisfies
  ν₂(σ(n)) = Σ_i ν₂(σ(p_i^{α_i})), where for odd p and α ≥ 1:
  - if α is even, σ(p^α) is odd, so ν₂(σ(p^α)) = 0;
  - if α is odd, ν₂(σ(p^α)) = ν₂(p + 1) + ν₂(α + 1) − 1.
- **Theorem 1.3 (sharp bound).** ν₂(σ(n)) ≤ ⌈log₂ n⌉ for all n, with equality
  if and only if n is a product of distinct Mersenne primes.
- **Theorem 1.4 (odd primes).** For an odd prime p, ν_p(σ(n)) ≤ ⌈log_p n⌉ under
  stated conditions, with equality related to solutions of the Ljunggren–Nagell
  Diophantine equation (q^{k+1}−1)/(q−1) = p^s.

## Why it matters for PE 241

The governing 2-adic structure used by the solver is exactly the content of
Theorem 1.1. For n = 2^a·u with u odd, half-integer abundancy
2σ(n) = (2k+1)n forces 1 + ν₂(σ(n)) = a, i.e. ν₂(σ(n)) = a − 1
(verified computationally for the 8 known small hemiperfects in
`code/verify_2adic.py`). That ν₂(σ(n)) is a function of the odd part u alone —
with each odd prime power contributing ν₂(σ(p^α)) = ν₂(p+1)+ν₂(α+1)−1 when α is
odd and 0 when α is even — is precisely what makes the exponent of 2 in n
determined by the odd part, and is what the denominator-cancellation DFS uses to
fix the 2-power in each target search. This source is the named theorem behind
the 2-adic reduction; it does not by itself enumerate the solutions (that is the
role of Alekseyev's aσ(n)=bn+c machinery).

```claim
id: ams-2adic-sigma-formula
statement: For n = 2^a·u with u odd, v2(sigma(2^a·u)) = v2(sigma(u)), and for odd primes p with alpha = v_p(u), v2(sigma(p^alpha)) = 0 if alpha even, and = v2(p+1)+v2(alpha+1)-1 if alpha odd; hence v2(sigma(n)) depends only on the odd part of n. Sharp bound v2(sigma(n)) <= ceil(log2 n), equality iff n is a product of distinct Mersenne primes.
hypotheses: sigma multiplicative; p odd prime; alpha >= 1
holds-here: yes — PE 241's half-integer condition 2sigma(n)=(2k+1)n forces v2(sigma(n)) = v2(n)-1, and the formula decomposes that constraint over the odd prime powers of n
status: proved in Amdeberhan–Moll–Sharma–Villamizar (Thms 1.1, 1.3); journal-verified article J. Number Theory 223 (2021) 325–349
bearing: grounds the 2-adic reduction the DFS solver relies on (v2(sigma(u))=a-1); confirms code/verify_2adic.py's computed pattern in the literature
anchor: research/summaries/amd_2adic_sigma.md
```