# Skeleton: finiteness of H_even via Conjecture 29 (second-moment method)

This skeleton closes Conjecture 6 (H_even finite) through **Conjecture 29** —
the proportional mod-16 statement — rather than through the weaker (H1)+(H2)
of Theorem 30. C29 is stronger than (H1) and the run's adopted approach
(`second-moment-character-mod16`) targets it directly, so a decomposition of
C29 itself tells the run what lemmas would suffice and which of them it can
already check.

```skeleton
goal: Conjecture 6 (Maciejewski arXiv:2605.20475) — H_even = {even m : every
  prime divisor of 2^m+1 is 3-Higgs} is finite.
implies: Take any odd prime p with 2p ∈ H_even^prime. By hb-prop4-structural,
  p ∈ P_3. For large p, Lemma C29-omega-lower gives ω(Φ_{4p}(2)) ≥ C·log p
  (or the weaker ω → ∞), so Lemma C29-proportional applies: at least
  c·ω(Φ_{4p}(2)) prime divisors r | Φ_{4p}(2) satisfy r ≡ 1 (mod 16). Each such
  r has v2(r−1) ≥ 4 > 3, so by hb-defs-3higgs-heven, r ∉ P_3, contradicting
  2p ∈ H_even. Thus H_even^prime is bounded, heven-prime-case-reduction gives
  H_even finite. The new part is the decomposition of C29 itself (Lemma
  C29-proportional) into character-orthogonality, first-moment evaluation, and
  second-moment bound — this is what the adopted second-moment approach
  requires.
status: live
rests-on: heven-prime-case-reduction, hb-prop4-structural, bhv-primitive-divisor-theorem,
  aurifeuillean-split, qr-supplementary-2, hb-defs-3higgs-heven
```

## The reduction lemmas (already discharged)

These are the same structural reductions as in the Theorem 30 skeleton; they
are recorded here so the inference is self-contained.

```gap
id: C29-G-prime-case-reduction
lemma: H_even is finite iff H_even^prime = {2p : p odd prime, 2p ∈ H_even} is
  finite, and |H_even| ≤ 4^|H_even^prime|.
status: discharged
discharged-by: heven-prime-case-reduction
```

```gap
id: C29-G-higgs-structure
lemma: If m = 2k ∈ H_even with k odd, then every prime q | k is 3-Higgs with
  v_q(k) ≤ 3. On the prime branch 2p ∈ H_even ⇒ p ∈ P_3.
status: discharged
discharged-by: hb-prop4-structural
```

```gap
id: C29-G-mod16-implication
lemma: For a prime r ≡ 1 (mod 4p), if r ≡ 1 (mod 16) then v2(r−1) ≥ 4 > 3,
  hence r ∉ P_3 (r is not 3-Higgs). This is one-way: the converse is false
  (343081 has v2 = 3 yet is non-3-Higgs).
status: discharged
discharged-by: hb-defs-3higgs-heven, verified empirically through p=61
  (code/out/heven_gauss_61.captured.txt)
```

## The ω-growth lemma (H2-lite)

We need ω → ∞ for the prime branch. This is a weaker form of (H2); it is
subsumed by any of the paper's conjectures (C29 includes it, C23/C24 would
bypass it).

```gap
id: C29-omega-growth
lemma: ω(Φ_{4p}(2)) → ∞ as p → ∞ over odd primes p. (Weaker than (H2); does
  not need the log-p growth rate, only unboundedness on the P_3 subsequence.)
status: open
next: (a) tool_builder: compute ω(Φ_{4p}(2)) for odd primes p up to the
  factorisation frontier (where L_p·M_p still fully factors); verify ω grows
  and does not stall. (b) theorem_prover: the Stewart/Hong radical lower bound
  rad(2^{2p}+1) ≫ 2^{2p}/(non-primitive part) with non-primitive part
  O(log(4p)), combined with every prime divisor r ≥ 4p+1, gives ω ≥
  (2p·log 2 − O(log p))/log(something). Extract the exact ω lower bound from
  hong-stewart-nonprimitive-bound. This is the Stewart-program target the paper
  isolates; a positive answer would give (H2) and hence this lemma
  unconditionally.
```

## The core: decomposing Conjecture 29

Conjecture 29 states: ∃c > 0, p₀ such that ∀p ∈ P_3, p ≥ p₀:
`#{r | Φ_{4p}(2) : r ≡ 1 (mod 16)} ≥ c·ω(Φ_{4p}(2))`.

```gap
id: C29-L1-factorization-structure
lemma: For odd prime p ≠ 5, Φ_{4p}(2) = (2^{2p}+1)/5 = (L_p·M_p)/5 where
  L_p = 2^p − 2^{(p+1)/2} + 1, M_p = 2^p + 2^{(p+1)/2} + 1. Every prime
  divisor r | Φ_{4p}(2) is primitive (ord_r(2) = 4p), hence r ≡ 1 (mod 4p)
  and r mod 16 ∈ {1,5,9,13}. The Gaussian factorization is
  2^{2p}+1 = (2^p+i)(2^p−i) in Z[i].
status: discharged
discharged-by: aurifeuillean-split, bhv-primitive-divisor-theorem, and the
  identity 2^{2p}+1 = Φ_4(2)·Φ_{4p}(2) = 5·Φ_{4p}(2) for p ≠ 5
```

```gap
id: C29-L2-character-orthogonality
lemma: Let N_a = #{r | Φ_{4p}(2) : r ≡ a (mod 16)} for a ∈ {1,5,9,13}. Then
  N_1 = (1/4)(ω + S_1 + S_2 + S_3) where S_j = Σ_{r|Φ} χ_j(r) for the three
  nontrivial characters of the cyclic group {1,5,9,13} ≅ C₄. Moreover
  Σ_χ |S_χ|² = 4·Σ_a N_a² − ω² (Parseval), and C29 is equivalent to the
  existence of ε > 0 such that Σ_{χ≠1} S_χ ≥ −(1−4c)ω for large p.
status: open
next: theorem_prover: this is elementary character theory (orthogonality of
  Dirichlet characters on a finite abelian group). The task is to formalise the
  equivalence: C29 (N_1 ≥ c·ω) ⇔ the character sums are not too negative.
  The three nontrivial characters are χ₁(r) = i^{(r−1)/4} (quartic),
  χ₂(r) = (−1)^{(r−1)/4} = (2/r) (quadratic Legendre symbol, since r ≡ 1 mod 4
  and r ≡ ±1 mod 8 determines the symbol), and χ₃ = χ₁·χ₂. The reduction is
  deterministic; the "open" part is pinning down the exact constants.
```

```gap
id: C29-L3-first-moment-quartic
lemma: For the quartic character χ₁(r) = (2/r)_₄ (the quartic residue symbol
  in Z[i]), the product identity holds: ∏_{r|Φ_{4p}(2)} (2/r)_₄ =
  (2/Φ_{4p}(2))_₄, where the right side is evaluated in Z[i] via
  Φ_{4p}(2) = (2^p+i)(2^p−i)/5. The pointwise equivalence (2/r)_₄ = 1 ⇔
  r ≡ 1 (mod 16) and (2/r)_₄ = −1 ⇔ r ≡ 9 (mod 16) is verified for all
  primitive divisors through p = 61. The product evaluation depends only on
  p mod 16 and can be tabulated.
status: open (pointwise equivalence discharged; product evaluation open)
discharged-by (pointwise): code/out/heven_gauss_61.captured.txt (71 primitive
  divisors, C5 pass)
next: (a) symbolic_math: compute the closed-form evaluation of
  (2/(2^p+i))_₄ in Z[i] as a function of p mod 16, using qr-supplementary-2
  and qr-main-law; tabulate the possible values. (b) tool_builder: verify the
  product identity numerically on the known divisors for p ≤ 61 by computing
  both sides independently. (c) theorem_prover: the multiplicativity of the
  quartic character gives the product identity exactly when the Gaussian
  factorisation of Φ_{4p}(2) is squarefree — verify this condition holds
  (primitive divisors are distinct, and 5 is the only possible repeated factor
  at p=5).
```

```gap
id: C29-L4-second-moment-bound
lemma: There exists δ < 1 such that for all sufficiently large p ∈ P_3,
  the quadratic character sum S₂ = Σ_{r|Φ} (2/r) satisfies |S₂| ≤ δ·ω. Since
  (2/r) = +1 for r ≡ 1,9 (mod 16) and −1 for r ≡ 5,13 (mod 16), this says the
  divisors are not overwhelmingly concentrated in the {5,13} classes where the
  quartic character cannot separate 5 from 13. Combined with the first-moment
  evaluation of S₁ (Lemma C29-L3), this yields N_1 ≥ (1−δ)ω/4 via
  C29-L2, establishing C29 with c = (1−δ)/4.
status: open
next: (a) tool_builder: compute N₁,N₅,N₉,N₁₃ for all p ≤ 61 from the existing
  divisor table (code/out/heven_gauss_61.captured.txt), and on the H_even slice
  {3,5,13,23,31,41,61} compute the ratio N₁/ω explicitly — the decisive
  empirical question is whether N₁/ω stays ≥ c uniformly or collapses toward 0
  on the H_even slice. (b) theorem_prover: the Aurifeuillean split
  L_p·M_p = 2^{2p}+1 induces a partition of the divisors; the quadratic
  character (2/r) = (−1)^{(r²−1)/8} relates to whether r splits in
  Q(√2)/Q. Can the product ∏_{r|L_p} (2/r) and ∏_{r|M_p} (2/r) be evaluated
  independently from the Aurifeuillean norm form? If so, a bias in one factor
  would give the variance bound. The falsifier is systematic bias into r ≡ 9
  (mod 16), which would survive this check and refute C29.
```

## Summary of gaps

| Gap | What it is | Status |
|-----|-----------|--------|
| C29-G-prime-case-reduction | Prime-case reduction | discharged |
| C29-G-higgs-structure | Higgs-cubefree structure of H_even | discharged |
| C29-G-mod16-implication | r ≡ 1 mod 16 ⇒ r ∉ P₃ | discharged |
| C29-L1-factorization-structure | Φ_{4p}(2) = (L_p·M_p)/5, primitive divisors | discharged |
| C29-omega-growth | ω(Φ_{4p}(2)) → ∞ | open |
| C29-L2-character-orthogonality | Orthogonality ⇒ N₁ = (ω + ΣS_χ)/4 | open |
| C29-L3-first-moment-quartic | Product identity for (2/r)_₄ | open |
| C29-L4-second-moment-bound | Variance bound ⇒ N₁ ≥ c·ω | open |

Of the four open gaps, C29-L2 is elementary (character orthogonality on a
4-element group — a theorem_prover can close it), C29-L3 is the quartic
product identity (symbolic_math + theorem_prover), and C29-L4 is the genuine
analytic difficulty. C29-omega-growth is shared with the (H2) route but in
weaker form.

The **first gap to attack** is C29-L2 (character orthogonality reduction):
it is the cheapest to close, it makes the structure of the other gaps precise,
and until it is formalised the relationship between C29-L3 and C29-L4 is only
heuristic.