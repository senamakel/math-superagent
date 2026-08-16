# Analysis of Boolean Functions — Ryan O'Donnell (2021 revision)

Source: arXiv:2105.10386 (also the 2014 book); full text at
`research/sources/odonnell-analysis-of-boolean-functions-full.pdf.full.md` →
[[odonnell-analysis-of-boolean-functions-full.pdf.full]]

## What it establishes (the facts this problem uses)

- **Thm 1.1 / 1.5.** Every `f : {−1,1}^n → R` has a unique multilinear expansion, and
  the `2^n` parity (Walsh) functions `χ_S(x) = (−1)^{Σ_{i∈S} x_i}` form an
  orthonormal basis (Fourier/Walsh basis) of the space of such functions.
- **Fact 1.6.** `χ_S(x)·χ_T(x) = χ_{S△T}(x)` — characters multiply by symmetric
  difference.
- **Prop 1.8 / 1.9.** Fourier coefficient `f̂(S) = ⟨f, χ_S⟩`; for Boolean-valued `f`,
  Parseval: `Σ_S f̂(S)² = E[f²] = 1`.
- **Fact 2.14 / 2.29.** Influence = boundary-edge fraction; the edges of the Hamming
  cube.

## Bearing on this problem

This fixes the **setting**: `S(n,h)² = Σ_{d,d'} (−1)^{XOR over M_d △ M_{d'} of h}` is
a sum of `(n−2)²` Walsh characters `χ_{M_d △ M_{d'}}(h)`. The collapse question is
precisely whether that index multiset `{M_d △ M_{d'}}` is dominated by short-range
sets (unions of few adjacent runs), which would make every second-moment functional of
`w(h)` a function of the short-range correlations of `h` alone. Fact 1.6 (multiplication
= symmetric difference) is the exact operation generating the index set.

## Claim blocks

```claim
id: odonnell-walsh-character-basis
statement: The functions χ_S(x) = (−1)^{Σ_{i∈S} x_i} for S ⊆ [n] form an orthonormal
  basis of {−1,1}^n → R, with χ_S χ_T = χ_{S△T} and Parseval Σ_S f̂(S)² = E[f²].
hypotheses: f : {−1,1}^n → R
holds-here: yes
status: proved
bearing: the S² expansion is a weighted sum of Walsh characters indexed by
  M_d △ M_{d'}; the index multiset governs whether S² factors through short-range
  correlations only (the collapse).
anchor: research/sources/odonnell-analysis-of-boolean-functions-full.pdf.full.md
```

## What it does not settle

O'Donnell does not describe the specific multiset `{M_d △ M_{d'}}` for these
down-sets; it only provides the language (Walsh basis, Parseval, Fourier
coefficients) in which that description is made.
