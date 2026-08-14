# Adamczewski, Bell & Smertnig — "A Height Gap Theorem for Coefficients of Mahler Functions"

**Source:** arXiv:2003.03429v2 [math.NT], 11 Oct 2021 (published J. Eur. Math. Soc. 25 (2023) 2525–2571). Full text: `[[abs-height-gap-mahler-regular.full]]` — `research/sources/abs-height-gap-mahler-regular.full.md`.

## What it establishes

**Setup.** f(z) = Σ a_n z^n ∈ Q⟦z⟧ is *k-Mahler* iff it satisfies a linear functional equation p_0(z)f(z) + ⋯ + p_d(z)f(z^{k^d}) = 0 with p_0 p_d ≠ 0 (Mahler operator z ↦ z^k). Coefficients are measured by the logarithmic Weil height h(a_n). Hierarchy: {k-automatic} ⊊ {k-regular} ⊊ {k-Mahler}.

**Theorem 1.1 (Height Gap Theorem).** For any M-function f ∈ Q⟦z⟧, h(a_n) falls into exactly one of five growth classes: O∩Ω(n), O∩Ω(log²n), O∩Ω(log n), O∩Ω(log log n), O(1). All five occur; there are gaps (e.g. no h(a_n) ∼ log³ n).

**Theorem 1.2 (the structural characterization, verified verbatim).**
(a) f is k-automatic iff h(a_n) ∈ O(1), iff {a_n} is finite.
(b) f is k-regular iff h(a_n) ∈ O(log n).
(Case (a) extends to arbitrary characteristic-zero ground fields — Theorem 11.1.)

**Supporting theorems (each refines one gap).**
- Theorem 6.1: h(a_n) ∈ o(n) ⟺ all nonzero roots of the k-Mahler denominator are roots of unity ⟺ f totally analytic ⟺ h(a_n) ∈ O(log²n).
- Theorem 7.1: h(a_n) ∈ o(log²n) ⟺ nonzero roots of the denominator lie in U_k (roots of unity of order not coprime to k) ⟺ f is k-regular ⟺ h(a_n) ∈ O(log n). (Lemma 7.10: k-regular ⟹ h(a_n) ∈ O(log n), via the linear representation.)
- Theorem 8.3: h(a_n) ∈ o(log n) ⟺ the minimal representation's matrix semigroup is tame ⟺ a_n is a Q-linear combination of word-convolution products of k-automatic sequences ⟺ h(a_n) ∈ O(log log n).
- Theorem 9.1: h(a_n) ∈ o(log log n) ⟺ the matrix semigroup is finite ⟺ f is k-automatic ⟺ h(a_n) ∈ O(1).
- Theorem 10.1: Becker's conjecture (Bell–Chyzak–Coons–Dumas): f k-regular ⟹ f = (k-Becker Laurent series)·(1/q(z)) with q(0)=1, 1/q k-regular.
- Theorem 12.1: which of the five classes a given k-Mahler function (given by equation + initial coefficients) falls into is **decidable** (via Cartier operators, minimal linear representations, and Mandel–Simon / Schur bounds). Contrast with Krenn–Shallit: many properties of k-regular sequences *with respect to the archimedean absolute value* are undecidable — height is the decidable measure.

## Bearing on PE156

- Background/theory tier for the proposed (not taken) approach `research/approaches/mahler-generating-function.md`. The A094798 generating function g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))² g(x^10) is a 10-Mahler function with integer (hence height-O(log n)) coefficients; Theorem 1.2(b) confirms the corresponding coefficient sequence is 10-regular — the classical ground the generating-function route stands on.
- It does **not** supply the fixed-point bound (that is Khovanova–Marton Prop 9.1, claim `G2-solution-bound`) nor any solution data. It is the modern named theorem for "Mahler ⟺ regular", used to pin the precedent of the approach note.

## Does not settle

- Nothing about the equation f(n,d)=n: no finiteness, no bound, no algorithm for this specific sequence's fixed points. Not an answer source.

## Caveat

- This summary replaces the previous placeholder digest. Full text 117 077 characters; statements above are quoted or paraphrased from it (Theorem 1.1 p.3, Theorem 1.2 p.4, Theorems 6.1/7.1/8.3/9.1 pp.16–29, Theorem 12.1 p.34).
