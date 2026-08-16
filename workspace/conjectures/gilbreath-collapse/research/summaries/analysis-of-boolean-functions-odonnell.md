# Analysis of Boolean Functions — Ryan O'Donnell

Source: https://arxiv.org/pdf/2105.10386 (arXiv:2105.10386, DOI https://doi.org/10.48550/arXiv.2105.10386); also https://arxiv.org/html/2105.10386v1

## What it establishes

The standard graduate textbook on Fourier analysis of Boolean functions `f: {0,1}ⁿ → ℝ`.
The relevant machinery, for a function `f` on the Boolean cube with Fourier–Walsh
expansion `f = Σ_{S⊆[n]} f̂(S)·χ_S` where `χ_S(x) = (−1)^{Σ_{i∈S} x_i}`:

- Orthogonality `E[χ_S χ_T] = δ_{S,T}`; Plancherel `E[f²] = Σ_S f̂(S)²`;
  Parseval.
- The expectation of a Walsh character over a coordinate-aligned set, and how XOR of
  index sets corresponds to products of characters: `χ_{S△T} = χ_S·χ_T`.
- Correlation / low-degree influences: the notion that a second-moment functional of a
  function factors through its low-degree (pairwise) Fourier coefficients precisely when
  its Walsh support is concentrated on small sets.

## Bearing on this problem

This is the *setting* in which the collapse question lives. The problem's
`S(n,h)² = Σ_{d,d'} (−1)^{XOR over M_d △ M_{d'} of h}` is exactly a sum of Walsh
characters `χ_{M_d △ M_{d'}}(h)`. The COLLAPSE conjecture is the statement that every
second-moment functional of `w(h)` factors through the short-range (degree-≤2) Fourier
coefficients of `h`. The textbook's Fourier vocabulary — Walsh characters indexed by
subsets, XOR of index sets, concentration of the Fourier support on small sets — is the
precise language in which the multiset `{M_d △ M_{d'}}` of Walsh indices (priority 1)
answers the question. If that multiset is dominated by small sets, Parseval/Plancherel
makes the collapse a Fourier-machinery statement; if not, the machinery gives the
breakdown.
