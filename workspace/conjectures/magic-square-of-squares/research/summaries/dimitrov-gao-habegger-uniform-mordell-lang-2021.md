# Dimitrov–Gao–Habegger, "Uniformity in Mordell–Lang for curves" (Ann. Math. 194 (2021), 237–298)

Full text: `research/sources/dimitrov-gao-habegger-uniform-mordell-lang-2021.full.md`
(arXiv:2001.10276v3, 31 Mar 2021 — the published Annals version).

## What it establishes

**Theorem 1.1.** Let g ≥ 2, d ≥ 1 be integers. There exists a constant c = c(g, d) ≥ 1
such that: if C is a smooth curve of genus g over a number field F with [F : Q] ≤ d,
then #C(F) ≤ c^(1+ρ), where ρ is the Mordell–Weil rank of the Jacobian Jac(C)(F).
(Answers Mazur's question affirmatively.)

**Theorem 1.2 / Corollary 1.3 (curve-in-Jacobian, height threshold).** Let g ≥ 2.
There exist c1 = c1(g, ι) ≥ 0 and c2 = c2(g, ι) ≥ 1 such that for a smooth genus-g
curve C over Q, P0 ∈ C(Q), and Γ ⊆ Jac(C)(Q) of finite rank ρ: if the modular height
h(ι([Jac(C)])) ≥ c1, then #(C(Q) − P0) ∩ Γ ≤ c2^(1+ρ). The torsion analogue
#(C(Q) − P0) ∩ Jac(C)(Q)_tors ≤ c2 holds uniformly in C.

**Theorem 1.6 (height inequality).** For a non-degenerate closed irreducible X ⊆ A
dominating S, ĥ_A(P) ≥ c1 h(π(P)) − c2 for all P in a Zariski-open dense U ⊆ X.
This is the key new ingredient (also DGH Thm 1.6 / B.1, cited by GGK as the height
inequality used in the uniform Mordell–Lang proof).

**Constants.** As in GGK, the c(g, d) are existential via Vojta's approach (counting
arguments, Betti map, height inequality); no explicit dependence on g, d is stated.
The paper does not compute any of its constants.

## Bearing on the magic-square-of-squares problem

DGH Theorem 1.2/Corollary 1.3 is the curve-in-Jacobian uniform Mordell–Lang statement
that both Kühne's equidistribution paper and GGK's higher-dimensional version build on,
and it is what Garcia-Fritz–Pasten Theorem 1.2/1.8 uses as the "height-uniform Mordell"
input. For the MSS: the four doubled points 2Q_i live in E_c(Q) (an elliptic curve,
genus 1), so DGH's genus-g ≥ 2 theorem does **not** apply directly — the relevant
curve-in-Jacobian statement for genus 1 is the classical Rémond/DP07 quantitative one
(for self-products of an elliptic curve) or the elliptic-curve case of GGK. This
distinction matters for the `uniform-height-bound-elliptic-ap` thread: it is exactly
why the DP07 explicit-constant route (see GGK summary) is the only lane to an
effective bound that could reach C^(1+r) < 3.

```claim
id: dgh-uniform-mordell-lang-curves
statement: "Dimitrov–Gao–Habegger, Thm 1.1: for g ≥ 2, d ≥ 1 there is c = c(g,d) ≥ 1
such that any smooth genus-g curve C over a number field F with [F:Q] ≤ d satisfies
#C(F) ≤ c^(1+ρ) with ρ = rk Jac(C)(F). Thm 1.2: if the modular height of Jac(C) is
≥ c1(g,ι), then #(C(Q)−P0) ∩ Γ ≤ c2^(1+ρ) for any finite-rank Γ ⊆ Jac(C)(Q). Both
constants existential."
hypotheses: genus ≥ 2; smooth proper; number field of degree ≤ d; Γ finite rank
holds-here: no — the MSS points lie on an elliptic curve (genus 1), so DGH Thm 1.1
does not apply directly; the genus-1 case is handled by GGK/DP07/Rémond quantitative
theory instead
evidence: proved
bearing: anchors the 'height-uniform Mordell' input at the primary source and pins
down exactly why it does not apply to E_c; forces the effective lane through DP07
(genus 1 / E^n) rather than through DGH
anchor: research/summaries/dimitrov-gao-habegger-uniform-mordell-lang-2021.md
```

```claim
id: dgh-height-inequality-nondegenerate
statement: "DGH Thm 1.6: for a non-degenerate closed irreducible X ⊆ A dominating S
(with A → S satisfying their hypothesis), ĥ_A(P) ≥ c1 h(π(P)) − c2 for all P in a
Zariski-open dense U ⊆ X. This is the height inequality GGK cite ([DGH21, Thm 1.6
and B.1]) to control large points in the uniform Mordell–Lang proof."
hypotheses: non-degenerate subvariety of an abelian scheme; base S; heights as in
the paper
holds-here: yes (technical ingredient, no direct MSS statement)
evidence: proved
bearing: the structural heart of the uniformity results; its constant is also
existential, so nothing explicit flows from it for the MSS
anchor: research/summaries/dimitrov-gao-habegger-uniform-mordell-lang-2021.md
```