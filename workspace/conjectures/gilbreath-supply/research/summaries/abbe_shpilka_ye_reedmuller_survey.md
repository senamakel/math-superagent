# Reed–Muller code weight enumerators (Abbe–Shpilka–Ye survey)

Source: Emmanuel Abbe, Amir Shpilka, Min Ye, *Reed–Muller codes: recent progress*,
survey of the weight-enumerator / capacity literature, arXiv:2002.03317.
Full text: `research/sources/abbe_shpilka_ye_reedmuller_survey.full.md`.

## What it establishes

A survey of the weight enumerator of Reed–Muller codes `RM(m,r)` and what it
implies for decoding/capacity. A codeword `f : F₂ᵐ → F₂` of degree ≤ r has
relative weight `wt(f) = E_Z[f(Z)] = P[f=1]` (uniform Z), bias `EZ[(−1)^{f(Z)}]`,
and `A_{m,r}(≤β) = #{f ∈ RM(m,r) : wt(f) ≤ β}`.

The known weight-enumerator bounds (all on the *code itself*, `RM(m,r)`):

- **Kasami–Tokura (1970), [33]:** for r ≥ 3, every codeword with
  `wt(f) < 2.5·2^{−r}` factors as `f = x₁g(x₃..x_m) + x₂h(x₃..x_m) + x₁x₂k(x₃..x_m)`
  (deg g = deg h = r−1, deg k = r−2) up to linear transform — characterising the
  lowest-weight codewords.
- **Theorem 2 (Kaufman–Lovett–Porat):** for constant r, `A_{m,r}(≤(1−ϵ)2^{−ℓ})`
  is `(1/ϵ)^{Θ(r·m^{r−ℓ})}` — asymptotically tight for constant degree.
- **Theorem 3 (Abbe–Shpilka–Wigderson):** for `r < m/4`, `A_{m,r}(≤(1−ϵ)2^{−ℓ})`
  ≤ `(1/ϵ)^{O(ℓ⁴ (m−ℓ ≤ r−ℓ))}`.
- **Theorem 4 (Sberlo–Shpilka):** for any `γ = r/m`, `A_{m,r}(≤2^{−ℓ})
  ≤ 2^{O(m⁴)+17(c_γ ℓ+d_γ)γ^{ℓ−1}(m ≤ r)}`.
- **Theorem 5 (Samorodnitsky):** if C (or C⊥) achieves capacity on the BEC,
  then for `k/n ∈ [1/2 ± R·2ln2]` the weight distribution matches a random code
  up to `2^{o(n)}`; for `k = o(n)` or rate→0 the `2^{o(n)}` term dominates and
  Theorem 4 wins.
- **Theorem 6 (Ben-Eliezer–Hod–Lovett):** for `r ≤ (1−δ)m`, almost all degree-r
  polynomials have weight ≥ some constant below 1/2.
- **Theorem 7 (Sberlo–Shpilka):** concentration of weight near 1/2 for
  `r < m/2 − Ω(√(m log m))`.
- **Capacity results:** RM(m,r) achieves capacity on BEC for r ≤ m/50 and on BSC
  for r ≤ m/70; ML decoding corrects 1/2−o(1) random errors for
  `r < m/2 − Ω(√(m log m))`.

## Bearing on SUPPLY — honest, largely none

The survey is about the **weight enumerator of the RM code itself** — how many
*degree-r polynomials* have a given weight. SUPPLY's object is different: the
weight of the *image* `wt(Φ_n h)` of a **single fixed input string** h under the
fold `Φ_n`. The fold rows are the evaluation vectors of *linear* (degree-1)
functions on submasks; `wt(Φ_n h)` is a co-domain image weight for a fixed h,
not a count over a code. None of the bounds here transfers to a lower bound on
`wt(Φ_n h)` for the prime gap-parity string.

The strongest connection is negative and structural: this literature confirms
(intuitively and then by Selberg–Sberlo–Shpilka) that **low-weight codewords
exist in large structured families and are generically rare** — the same tension
the five closed doors encode. The Kasami–Tokura factorisation is the exact
statement of what low-weight structured inputs look like (degree-1/2 factors),
which is the shape the closed-door witnesses (anti-dyadic, kernel-adjacent) take.
But the survey provides no input hypothesis on h forcing `wt(Φ_n h) ≥ c·n`.

```claim
id: rm-weight-enumerator-bounds
statement: For Reed–Muller codes RM(m,r): lowest-weight codewords factor per Kasami–Tokura
  (wt < 2.5·2^{-r} → x_1g+x_2h+x_1x_2k); A_{m,r}(≤(1-ε)2^{-ℓ}) has tight (constant-r)
  and O(ℓ^4(...)) (r<m/4) bounds; near-weight-1/2 concentration and capacity on BEC/BSC
  hold for r up to O(m/50)–O(m/2 − Ω(√(m log m))). These quantify that in RM code spaces
  low-weight codewords are rare and structured.
hypotheses: RM(m,r) over F_2; relative weight wt, bias, weight enumerator A_{m,r}(≤β);
  capacity senses for BEC/BSC.
holds-here: No — this is the weight distribution of an RM code (counting degree-r
  polynomials), not the image weight wt(Φ_n h) of a single fixed string h under the
  submask-XOR fold. The fold's rows are degree-1 evaluations; the object is co-domain
  image weight for one h, not a code-wide count.
status: proved/surveyed (primary results from [1],[2],[32],[33],[34],[35],[45])
bearing: Structural/negative context: low-weight images are rare and take the factored
  degree-1/2 shape of the five closed-door witnesses. Does not close walsh-spectral-subset-b904
  and supplies no arithmetic input on h forcing wt(Φ_n h) ≥ c·n.
anchor: research/sources/abbe_shpilka_ye_reedmuller_survey.full.md (Def 3; Thms 1-7)
```

## Do not re-read for a supply bound

The weight-enumerator machinery here is for the RM code's own distribution; it is
not a source for `wt(Φ_n h)`. Read it only for the shape of low-weight structured
inputs (Kasami–Tokura factorisation), which reinforces the closed doors rather
than opening a route.
