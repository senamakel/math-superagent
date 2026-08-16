# Yoshida 2011 — Information storage capacity of discrete spin systems (fractal / Sierpinski codes)

**Source:** Beni Yoshida, *Information storage capacity of discrete spin systems*,
Annals of Physics 338 (2013) 134–166. arXiv:1111.3275v3 (dated 2012-12-24). URL: https://arxiv.org/pdf/1111.3275
Full text: `research/sources/yoshida_information_storage_fractal_codes.full.md`
DOI: 10.1016/j.aop.2013.07.009

*This file replaces the auto-generated structural digest. It is a faithful summary of what the
source establishes, filed by the librarian; whether these lemmas suffice for the SUPPLY fold is a
theorem question for the scholar, not a claim made here.*

## What the paper is

A physics/coding-theory paper constructing *fractal codes* — linear error-correcting codes whose
generator matrices are the Pascal triangle reduced modulo p (i.e. the Sierpinski-gasket structure),
realised as ground spaces of gapped frustration-free local Hamiltonians. Its technical core is a set
of exact weight lemmas for the mod-p Pascal (Sierpinski) matrix. These are the mathematical content
relevant to this run's fold Φ (Pascal mod 2 / Rule 90), held by the open request
`walsh-spectral-subset-b904`.

## The load-bearing lemmas (for p=2 this is precisely the Rule-90 / Pascal-mod-2 fold geometry)

The matrix **B** is the mod-p Pascal matrix of size L×L, L = p^m. Its rows are the *principal vectors*
B(t), t = 0, …, L−1. Every vector v ∈ F_p^L decomposes uniquely as v = Σ_t c(t) B(t) with c(t) ∈ F_p
(the rows are independent; Eq. (21)).

**Lemma 2 (Inequality on principal vectors).** Let v = Σ_t c(t) B(t) and let t_min be the smallest t
with c(t) ≠ 0. Then
```
W(v) ≥ W(B(t_min))
```
where W(·) is the number of non-zero entries. That is: the weight of a linear combination of Pascal
rows is bounded below by the weight of its leading (smallest-index) contributing row — a lower bound
depending only on the fold's row structure, **not** on the coefficients c(t) being "complicated".
The p=2 proof uses the self-similar (Sierpinski) structure: adding any row B(t) with t > t_min never
decreases the weight of the partial sum (the first-half/last-half-recovery argument). For p>2 the
proof is in Appendix B.

**Relationship to the fold.** In the SUPPLY setting, wt(Φ_n h) is the weight of a linear combination
of the fold's rows (downsets M_d ≅ ↓d under the reflection x ↦ n−1−x, claim
`downset-row-intersection-meet-formula`), which is the image of h under Pascal-mod-2 geometry. Yoshida's
Lemma 2 is the closest published statement to the request's "Walsh/subset-sum lower bound on wt(Φ_n x)
valid for inputs not complicated in the five refuted senses": it lower-bounds the image weight in terms of
the leading row alone. **Caveat (must be priced, not assumed):** the bound is `W(B(t_min))`, the weight
of a *single* row of the Pascal matrix, which is generally a power of 2 and can be small (B(0) has weight
1). Whether the fold's specific row set forces `W(B(t_min)) ≥ c·n` for the primes' h is NOT established by
this lemma and remains the open theorem. This lemma is a *structural input* to that question, not its answer.

## Other results in the paper

- The *raw-vector* weight lower bound (Lemma 6 area) and principal-matrix inequalities (Lemma 5) are the
  multi-dimensional analogues.
- Theorem 1 / Corollary 1 / Theorem 2: the fractal (Hausdorff) dimension of the code distance of these
  codes equals the Sierpinski fractal dimension log(p(p+1)/2)/log p; the code distance d scales
  polynomially in L, and the codes asymptotically saturate the local-code storage bound k·d^{1/D} ≤ O(n).
- Lemma 1: Lucas-type product formula for the entries `_tC_r` mod p (the Submask/Lucas structure that also
  governs the fold's binomial entries, cf. `mestrovic_lucas_theorem_survey`).
- Lemma 7 (inverse matrix), Lemma 8 (generation by modified rule), Lemma 9–11: structural identities for
  principal matrices / transpose decompositions.

## Why it was filed (relevance to the run)

The open request `walsh-spectral-subset-b904` asks for exactly this: a weight lower bound on images of a
Pascal-mod-2 (submask) linear map valid without "h is complicated" hypotheses. **This is a genuine published
source for that bound's structural engine (Lemma 2).** The two prior librarian passes recorded "no source on
`walsh-spectral-subset-b904` exists" — that blanket statement is now shown to be too strong: a relevant weight
lemma for exactly this matrix family exists. Whether it *suffices* for SUPPLY (linear supply for the primes'
h) is the separate theorem question; this source is the input to pricing it.

## Download provenance (correction of a wrong download)

The first fetch by inferred arXiv ID `1304.6104` returned an unrelated exoplanets paper (Kevin Heng).
The correct ID was confirmed via the arXiv API title query on 2026-08-16: **arXiv:1111.3275**. The wrong
download is recorded in `research/sources/DELETED_wrong_arxiv_yoshida.md` so nobody guesses the ID again.
