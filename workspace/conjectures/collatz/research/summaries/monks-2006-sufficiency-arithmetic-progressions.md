# Monks 2006 — The sufficiency of arithmetic progressions for the 3x+1 conjecture

<!-- source: https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf (author's final version; published Proc. Amer. Math. Soc. 134 (2006), 2861-2872, DOI 10.1090/S0002-9939-06-08567-4) -->

**Kenneth M. Monks, 2006. Full text held (author's Rev4 PDF, 1035 lines).**

## What it establishes

T(x) = (3x+1)/2 if x odd, x/2 if x even. x,y **merge** if their T-orbits
intersect (an equivalence relation). S ⊆ Z⁺ is **sufficient** if it meets every
merge-equivalence class. Since the 3x+1 Conjecture holds iff every positive
integer merges with 1, proving the conjecture on any sufficient set proves it
everywhere.

- **Theorem 1.1**: Every arithmetic progression A + BN (A ≥ 0, B ≠ 0) is
  sufficient. Answering Andaloro's question (are 1+2^nℕ sufficient for all
  n? — Andaloro had n ≤ 4): yes, every nonconstant progression works.
- **Corollary 1.2 / 1.3**: every arithmetic progression is sufficient for the
  Divergent Orbits Conjecture and for the Nontrivial Cycles Conjecture — so
  each of the three conjectures needs only to be proved on any one arithmetic
  progression.
- Also: every negative arithmetic progression is sufficient for T on Z⁻; a
  progression ∪ negative progression ∪ {0} is sufficient for T on Z.

Method (the part a future reduction argument needs): back-tracing functions
(Wirsching's machinery). For s = (s₀,…,s_k) ∈ ℕ^{k+1}, v_s = T₀^{−s₀}∘T₁^{−1}∘…∘T₁^{−1}∘T₀^{−s_k}
with v_s(x) = c(s)x − r(s), c(s) = 2^{||s||}/3^{l(s)}; s admissible for x
if v_s(x) ∈ Z⁺, then T^{||s||}(v_s(x)) = x. The proof works mod b with
(b, 6) = 1, where T₀, T₁ induce permutations x ↦ 2^n 3^m x + k of Z_b
(Lemma 3.1: the group generated is exactly this set — via Misiurewicz–Rodrigues).
Lemma 2.7 (after Bernstein): for every n, odd τ, a ∈ Z there is an increasing
sequence t_1 < … < t_h < n with Σ 2^{t_i} τ^i ≡_{2^n} a. Sufficiency of
A + BN then follows by constructing, for any x, an admissible vector with
v_s(x) ∈ A + BN.

## Why it matters for this run

This is the primary that Ansari 2025's "merge sufficient" notion builds on
(Ansari ref [7]), and it is the load-bearing structural fact of the
sufficiency/verification-sieve arm: **proving the conjecture on a single
arithmetic progression would prove all of it**, and likewise for the
divergence and non-trivial-cycle sub-conjectures. Any attempt that proves a
restricted class must be compared against this: proving it on a progression is
NOT weaker in structure than proving it everywhere.

```claim
id: monks-ap-sufficient
statement: Every nonconstant arithmetic progression A + BN (A, B ≥ 0, B ≠ 0) is a sufficient set for the accelerated Collatz map T on Z⁺: the T-orbit of every positive integer intersects the T-orbit of some element of A + BN.
hypotheses: T(x) = (3x+1)/2 if x odd, x/2 if x even; sufficiency in the merge sense (orbits intersect).
holds-here: true — the actual 3n+1 map in accelerated form.
evidence: proved in source (Monks 2006, Theorem 1.1), read in full text.
status: proved (in source; not yet Lean-formalised here)
falsifies: a positive integer whose T-orbit avoids every element of some progression A + BN (checkable for small x by orbit computation).
```

```claim
id: monks-ap-sufficient-for-subconjectures
statement: Every arithmetic progression is sufficient for the Divergent Orbits Conjecture and for the Nontrivial Cycles Conjecture: if no element of a progression A + BN has an unbounded orbit (resp. an orbit containing a nontrivial cycle), then no positive integer does.
hypotheses: same map; a divergent orbit = unbounded T-orbit; nontrivial cycle = T^k(x) = x for k > 1 other than the trivial {1,2} cycle.
holds-here: true.
evidence: proved in source (Monks 2006, Corollaries 1.2, 1.3), read in full text.
status: proved (in source)
falsifies: a divergent orbit or nontrivial cycle avoiding a progression, with the progression's elements all convergent/cycle-free (finite check against known verification bound).
```
