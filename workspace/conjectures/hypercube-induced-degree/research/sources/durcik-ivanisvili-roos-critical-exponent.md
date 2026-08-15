# Durcik–Ivanisvili–Roos, "Sharp isoperimetric inequalities on the Hamming cube near the critical exponent" (arXiv:2407.12674)

Source URL: https://arxiv.org/abs/2407.12674
Authors: Polona Durcik, Paata Ivanisvili, Joris Roos. 2024.

## What this source establishes

For β ≥ β0 = 0.50057 and A ⊆ {0,1}^n with |A| ≤ 1/2:

    E[h_A^β] ≥ |A|·(log2(1/|A|))^β

(equality for subcubes), improving the earlier threshold log2(3/2) ≈ 0.585.
Also: E[h_A^β] ≥ max(J(|A|), (1−|A|)(log2(1/(1−|A|)))^β) for |A| ≥ 1/2.
Auxiliary result: for β=1/2, essentially sharp for small sets. Proof is
computer-assisted (Bellman function + interval arithmetic). Supports the
Kahn–Park conjecture; yields sharp Poincaré-type inequalities for Boolean
functions near L1.

## Why it is here

Companion to Beltrán et al. and again an **average** E[h_A^β] bound. The β=1/2
critical-regime result is the natural interpolation between vertex boundary
(β=0) and edge boundary (β=1). All still average quantities. Nothing here
bounds the maximum internal degree of a single subset of size 2^{n-1}+1.

## Claim block

```claim
id: durcik-ivanisvili-roos-critical-exponent
statement: For β ≥ 0.50057 and |A| ≤ 1/2, E[h_A^β] ≥ |A|(log2(1/|A|))^β, with
  equality for subcubes (and an analogous bound for |A| ≥ 1/2).
hypotheses: uniform measure, β ≥ β0.
holds-here: holds, but average-type. Equality case is a subcube (size a power of
  2), so the bound for size 2^{n-1}+1 is not equality-typed and gives no max
  internal-degree conclusion.
status: asserted-by-source.
bearing: confirms → at any β ≥ 0.5 the sharp cube isoperimetric inequality
  bounds an average outer boundary; no translation to max internal degree
  D(S). Supports the obstruction.
anchor: durcik-ivanisvili-roos-2024
```
