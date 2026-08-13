# Thread: Binary-digit constraint on binomial multiplicities

## Question

Can the binary-submask constraint (k ⊆ n, from Lucas's theorem mod 2) — which every representation (n,k) of an ODD a must satisfy — give a bound on N(a) that is uniform and independent of the Diophantine curve method?

## Why it's different

Every approach so far (genus, Bilu-Tichy, SST/BST, MRSTT, Baker/Matveev, heights) passes through the Diophantine equation C(x,k1)=C(y,k2) and its associated algebraic curve. The uniformity wall for those methods is the ineffectiveness of Siegel/Faltings when the curve's parameters grow. The binary-digit constraint is a combinatorial condition on the PAIRS (n,k) that does NOT involve the curve at all — it's a purely additive (binary digit) condition on the arguments of the binomial coefficient.

The refuted kummer-lucas-p-adic approach tried to bound N(a) by the SIZE of p-adic congruence classes and failed because one class can be exponentially large. This approach is DIFFERENT: it does not bound class size. It asks: given that all representations (n_i,k_i) of a must satisfy k_i ⊆ n_i AND produce the same value a, can there be many such pairs? This is a system of simultaneous constraints, not a class-size estimate.

## Core mechanism

For odd a:
- Lucas's theorem: C(n,k) is odd ⇔ k ⊆ n (bitwise)
- Therefore every (n,k) with C(n,k)=a must have k ⊆ n
- The submask condition means: wherever k has a 1-bit, n must also have a 1-bit
- This forces n ≥ k (trivial from k ⊆ n) and more strongly, n must have "dense" binary expansion relative to k

The plan:
1. For a given odd a and fixed k, the equation C(n,k)=a is a polynomial in n of degree k ⇒ at most k solutions in n (effective, per fixed k).
2. The submask condition couples n and k: if k has popcount w, then n must have at least w ones in its binary expansion, and they must be at the SAME positions as k's ones ⇒ n ≥ 2^{pos(k)} (where pos(k) is the bit pattern of k).
3. For large k, C(n,k) grows fast with n. If a has many representations with large k, the submask condition forces the n_i to be comparable in size, which constrains how many distinct k_i can work.
4. For small k, the effective SST 1995 + Matveev 2000 machinery gives computed bounds on the number of solutions for each fixed pair — and there are only finitely many small-k pairs to check.

The key lemma to prove: if C(n₁,k₁) = C(n₂,k₂) = a with a odd and k₁ < k₂, then either (a) k₂ - k₁ is small (the k's cluster), or (b) the binary-submask condition forces a contradiction. If the k's cluster, we're in the finite-many-pairs regime where SST 1995 gives effective bounds. If they don't cluster, the mechanism proves there CAN BE no second representation.

## First computational step

Enumerate all odd binomial coefficients for n ≤ 2^18, record value multiplicities. This gives the empirical maximum multiplicity in the odd-only triangle up to that bound. Two objectives:
1. If the maximum is ≤ 8, this is numerical evidence consistent with B=8.
2. If any value appears ≥ 9 times, that's a discovery — a new witness.

Cost: ~3.5·10^7 odd entries for n ≤ 2^18. Each C(n,k) computed exactly. Use 128-bit hash for comparison. Parallel across n ranges, 28 CPUs, timeout 540.

## Rest on

- Lucas's theorem (1878): classical, primary sources held
- `kummer-lucas-class-not-logarithmic`: refuted the single-class approach — this thread is different
- `mrstt-interior-theorem`: covers the interior but all witnesses are in the boundary
- `sst-effective-shared-factor`: effective per-pair bounds for SST regime — applies to clustered small-k case
- `matveev-2000-explicit-constants-primary`: the explicit constant supplier

```thread
question: Can the binary-submask constraint alone bound multiplicities in the odd-only
  Pascal triangle, without invoking algebraic geometry or heights?
status: live — adopted from inventor proposal; mechanism distinct from all
  curve-theoretic approaches; first step is computational (odd triangle scan to 2^18)
rests-on: matveev-2000-explicit-constants-primary, sst-effective-shared-factor,
  mrstt-interior-theorem, kummer-lucas-class-not-logarithmic
blocked-by: nothing yet — approach is brand new to the run
next: scan odd binomial coefficients for n <= 2^18, record multiplicities
```

## Literature check (librarian, this pass)

The thread's stated gap — "is the odd-only triangle's *value multiplicity*
studied?" — was searched. Finding: **the base-p/odd-triangle literature counts
how many coefficients are odd (or nonzero mod p^α), not how often one integer
value recurs across rows.** Rowland 2017 (survey now held,
`research/summaries/rowland-binomial-valuations-words.md`) summarizes Kummer,
Lucas, Glaisher 1899 (`2^{popcount(n)}` odd entries per row), Fine 1947, and
Rowland's matrix generalization (exact polynomial for the nonzero-mod-p^α
count) — all sparsity counts, none concerning equal *values* across rows. So the
submask *multiplicity* question remains genuinely unstudied in the surveyed
literature; the thread's premise survives. The matrix theorem supplies a precise,
computable refinement of the sparsity intuition the mechanism relies on.
Implication for the first step: the n<=2^18 odd-triangle scan is not reproducing
known work but probing genuinely open territory, and its maximum-multiplicity
finding (whether any odd value reaches 9) is a new datum. (Lane 2023
arXiv:2309.12942, held, adds only the residue-distribution benchmark: for p=2
the "even distribution" is vacuous, so nothing beyond the total count; the
value-multiplicity gap survives unchanged.)