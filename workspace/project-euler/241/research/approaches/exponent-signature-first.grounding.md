# Grounding: is exponent-signature-first a genuinely new direction?

Checked against the literature. **Answer: no — the direction is already published,
and for this problem it does not beat the run's denominator-cancellation DFS.**

## (1) Published work enumerating by exponent-signature first

**Yes, and the decisive precedent is the paper this run already holds.**

**Goto & Shibata, "All numbers whose positive divisors have integral harmonic
mean up to 300", Math. Comp. 73 (2004), 475–491** — Section 3, *General
algorithm*, is literally the signature-first search. For a fixed target c the
search has three steps:

> (1) List the possibilities of ω(n), the number of distinct primes dividing n.
> (2) For each value of ω(n), list the possibilities of the *types of
> exponents* in the factorization of n.
> (3) For each type of exponents, list the possibilities of primes dividing n.

Then it checks H(n)=c on the surviving finite candidates. Step (2) is the
exponent-signature enumeration; Step (3) is the prime-assignment search; and the
bounds on both come from the *same* monotonicity this approach relies on —
§3.3 establishes
`1 < S(q^e) < S(q^f) < S(p^e) < S(p^f) < 2` for p<q, e<f (S=σ/n), and Lemma 4.2
is `H(p^e q^f) > H(p^f q^e)` for e<f, p<q — the exponent-sorting lemma
`code/maxab.py` re-derives. Goto–Shibata's target family is *harmonic numbers*
(H(n)=nτ(n)/σ(n) integral), a sibling ratio, not the hemiperfect abundancy; but
the *algorithmic shape* is unmistakably the one proposed here. So the idea is
not new.

The harmonic-number branch of the literature continues it (Cohen–Sorli harmonic
seeds; Cohen–Sorli "Odd harmonic numbers exceed 10^24", Math. Comp. 2010 — a
tree-based component/exponent enumeration of the same shape). Nothing found
applies signature-first specifically to half-integer abundancy (hemiperfects);
there the established method is instead the **interleaved** tree-search over
prime powers — Flammenkamp's exhaustive MPN tree-search and Alekseyev's
(arXiv:2601.17832) lpf-based RES tree with analytic prime-wheel pruning — which
is exactly the run's denominator-cancellation DFS. So transplanting
signature-first to hemiperfects does not add a method the run lacks; it
re-describes a harmonic-number technique onto a target whose own literature
uses the interleaved tree-search the run already implements.

## (2) The sorting lemma (fixed prime set, nonincreasing exponents on smallest
primes maximizes abundancy) used to prune a signature-first search

The lemma is **standard and appears in multiple independent literatures**:

- **Goto–Shibata §3.3 / Lemma 4.2** use it directly to prune the exponent-type
  step (their §3.2 example bounds H(n) from below by H(2^{e1}·3^{e2}···q_r^{er})
  on the smallest primes — precisely min_n(E)).
- **Colossally abundant / superabundant theory** (Alaoglu–Erdős 1944; the
  Caveney–Nicolas–Sondow / Nazardonyavi–Yakubovich expositions) is built on it:
  the extremal shape of σ(n)/n has nonincreasing exponents k2≥k3≥k5≥… on the
  primes in order, with p_{min} exponents constrained by product bounds. This is
  the same "sort exponents down onto the smallest primes" fact maxab.py proves,
  used to bound the extremal abundancy shapes.
- The product-bound count of such shapes (min_n(E)=∏p_i^{e_i}≤X) is the same
  structural quantity Goto–Shibata's Table 1 / §3.1 bound by ω(n).

So yes — the sorting lemma has been used to prune signature/shape searches in
exactly this way, in harmonic-number enumeration and in CA/SA extremal analysis.
It is not new and not unpublished.

## (3) A known bound on the number of feasible exponent signatures below 10^18

No *published closed-form count* for the specific integer 10^18 was found, and
I could not execute a count in this environment, so the exact number is
**unverified here**. But the finiteness and smallness of the set is standard:
e1 ≤ log_2(10^18) ≈ 59, and the product constraint ∏p_i^{e_i} ≤ 10^18 caps r
(since r ≤ log_2(10^18)). This is the same "few thousand shapes" claim maxab.py
relies on. Goto–Shibata (§3.1, Table 1) bound ω(n) the same way for the
harmonic case. The count is a structural parameter (a bounded partition count),
not an answer-space enumeration, so it is consistent with the method policy —
but *no source states the numeric value at 10^18 specifically*, and the run
should compute it if it wishes to quote it.

## Verdict

- **Precedent exists**: Goto–Shibata (2004) §3 is signature-first enumeration
  for harmonic numbers, with the same monotonicity and sorting lemma.
- **Not novel for hemiperfect/multiperfect σ-equations**: for that family the
  published standard is the interleaved tree-search (Flammenkamp; Alekseyev
  2026), which the run's denominator-cancellation DFS already implements. The
  signature-first route is the harmonic-number method transplanted to a sibling
  ratio; it does not beat the run's DFS and is not required to solve PE241.
- **Sorting lemma**: standard (Goto–Shibata; CA/SA theory), already used to
  prune shape searches.
- **Signature count at 10^18**: finite and small by standard argument; numeric
  value not sourced and not computed here.

Status: **grounded** (the method is a real, published technique — not refuted)
but with the decisive caveat that it is **not genuinely new** and offers no
advantage over the run's existing method. Recorded so nobody proposes it again
as a new direction.
