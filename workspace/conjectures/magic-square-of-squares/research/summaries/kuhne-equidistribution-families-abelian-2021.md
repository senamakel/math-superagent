# Kühne, "Equidistribution in Families of Abelian Varieties and Uniformity" (arXiv:2101.10272)

Full text: `research/sources/kuhne-equidistribution-families-abelian-2021.full.md`
(arXiv:2101.10272, January 2021, PDF).

## What it establishes

**Theorem 2 (uniform Manin–Mumford).** For each g ≥ 2 there is c2(g) ≥ 1 such that
for every smooth proper genus-g curve C over C and every degree-1 divisor D on C,
#(ι_D(C) ∩ Tors(Jac(C))) ≤ c2(g). (Uniformly bounded torsion points on the
Abel–Jacobi image.)

**Theorem 3 (uniform Bogomolov).** For g ≥ 2, n ≥ 3 and an immersion
ι : B_g,n ↪ P^N_Q, there exist c3 = c3(g,n,ι), c4 = c4(g,n,ι) > 0 with the stated
small-height point-set bound for every s in the parameter space.

**Theorem 4 (uniform Mordell–Lang, curve case).** For each g ≥ 2 there is c9(g) > 0
such that for every smooth proper genus-g curve C, every degree-1 divisor D on C, and
every subgroup Γ ⊆ Jac(C)(C) of finite rank ρ, the relevant intersection
(ι_D(C) ∩ Γ-translates) is bounded by c9(g)^(1+ρ) — the digest reads
"C(K) ≤ c10(g)^(1+ρ)" and "C(K) ≤ c11(g,[K:Q])^(1+ρ)".

The paper's method: equidistribution of small points in families (Ullmo–Zhang
strategy) plus the DGH height inequality, applied to non-degenerate subvarieties of
abelian schemes.

## Bearing on the magic-square-of-squares problem

Kühne's Theorem 4 is the direct predecessor of GGK's Uniform Mordell–Lang for curves
embedded in their Jacobians, and is one of the two papers GGK cite as the
curve-in-Jacobian stepping stone (with DGH). Its constants c9(g) are again existential.
For the MSS the object is an elliptic curve (genus 1), so neither Kühne Thm 4 (g ≥ 2)
nor DGH Thm 1.1 applies; the effective lane remains DP07 (self-products of an elliptic
curve) as identified in the GGK summary. Kühne Thm 2 (uniform Manin–Mumford) is a
useful encyclopedic anchor: it completes the trio of uniformity results (MM, Bogomolov,
ML) that the adopted approach's literature rests on.

```claim
id: kuhne-equidistribution-uniform-ml-curves
statement: "Kühne Thm 4: for g ≥ 2 there is c9(g) > 0 such that for any smooth proper
genus-g curve C over a number field, any degree-1 D on C, and any finite-rank
Γ ⊆ Jac(C), #(ι_D(C) ∩ Γ) ≤ c9(g)^(1+ρ). The uniform Manin–Mumford (Thm 2) and
uniform Bogomolov (Thm 3) cases are proved in the same paper via equidistribution of
small points in families of abelian varieties."
hypotheses: genus ≥ 2; number field; Γ finite rank; D degree 1
holds-here: no — the MSS points live on an elliptic curve (genus 1), outside the
g ≥ 2 hypothesis; the genus-1 quantitative/effective case is DP07/Rémond territory
evidence: proved
bearing: encyclopedic completion of the uniform-MM/Bogomolov/ML family feeding the
uniform-height-bound-elliptic-ap approach; confirms again that no effective constant
for the elliptic case sits in the DGH/Kühne/GGK chain
anchor: research/summaries/kuhne-equidistribution-families-abelian-2021.md
```