# On the number of m-th roots of permutations — source note

Source: Leaños, Moreno, Rivera-Martínez, arXiv:1005.1531v4 (2011), PDF → markdown.

## Objects and definitions
σ ∈ S_n of cycle type a = (a_1,…,a_n) (a_ℓ = # cycles of length ℓ). An **m-th
root** of σ is τ ∈ S_n with τ^m = σ. Wilf's number ((ℓ,m)) := ∏_{p|ℓ} p^{ν_p(m)}
(part of m supported on primes of ℓ).

## Statements (with locations)
- **Theorem 3** (Wilf / Knopfmacher–Warlimont, existence criterion), §3:
  σ has an m-th root iff for every ℓ, a_ℓ is divisible by ((ℓ,m)). So for a
  prime p this says cycles whose length is a multiple of p must come in batches
  of p.
- **Theorem 1** (explicit count), §1/§4: the number r^(m)(a) of m-th roots of σ
  is
    ∏_{ℓ: a_ℓ≠0} a_ℓ! · Σ_{ε∈E_m(ℓ,a_ℓ)} ∏_i ℓ^{(g_i−1)ε_i}/(g_i^{ε_i} ε_i!)
  where G_m(ℓ,a) = {g∈N : g≤a_ℓ, gcd(gℓ,m)=g}, g=(g_1..g_k) its ascending order,
  and E_m(ℓ,a) = {ε∈N_0^k : Σ g_i ε_i = a_ℓ}. (r=0 iff some E_m is empty.)
- **Theorem 2** (EGF), §1/§4.2: the coefficient of t_1^{a_1}⋯t_n^{a_n}/(a_1!⋯a_n!)
  in exp( Σ_ℓ Σ_{g∈G_m(ℓ)} (ℓ^{g−1}/g) t_ℓ^g ) is the m-th-root count of type a.
- **Proposition 9**, §5: for m=p^r a prime power, the probability p_m(n) that a
  random n-permutation admits an m-th root is constant on each block
  n = jp, jp+1, …, jp+p−1.

## Relevance to this run
This is the primary source for fact (2) of `report_cited_facts.md` (existence
criterion Theorem 3 and explicit count Theorem 1). It is confirmatory and
accurate as far as it goes.

## What it does NOT settle
Q(n) is NOT a count of m-th roots — it sums rank over iterates of each single
permutation (cyclic subgroups). Theorem 1 counts preimages τ of σ under the
power map τ↦τ^m; it gives no identity for Σ_{τ∈⟨π⟩} rank(τ).

One reformulation it does suggest (a deduction, NOT stated in the paper): writing
Q(n) = Σ_τ rank(τ)·N(τ), where N(τ)=#{(π,i): 1≤i≤n!, π^i=τ} = Σ_{i=1}^{n!} R_i(type(τ))
with R_i = i-th-root count of that cycle type (root counts are conjugation-invariant,
so constant per type). This is type-structured but does not beat enumeration: the
number of cycle types is the partition number p(10^6) ≫ astronomically large, and
the inner sum is over n! values of i. So it does not reach Q(10^6). The
report's hint that G_m sets "govern which powers share an exponent" is a
speculation of the report, not a claim of this paper.

## Verdict
Confirms fact (2); does NOT advance the efficient-method subtask.

## Contradictions
None with memory.md. m-th-root counts play no role in the reduction to cyclic
subgroups already in memory.md — consistent, not conflicting.
