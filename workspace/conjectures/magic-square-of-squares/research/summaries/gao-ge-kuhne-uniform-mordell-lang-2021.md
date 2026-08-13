# Gao–Ge–Kühne, "The Uniform Mordell–Lang Conjecture" (arXiv:2105.15085)

Full text: `research/sources/gao-ge-kuhne-uniform-mordell-lang-2021.full.md`
(arXiv:2105.15085v4, 26 Mar 2026, accepted at Publ. Math. IHÉS; downloaded from the arXiv PDF).

## What it establishes

**Theorem 1.1 (Uniform Mordell–Lang).** For all integers g, d ≥ 0 there exists a
constant c(g, d) > 0 such that: for any abelian variety A of dimension g over an
algebraically closed field F of characteristic 0, any irreducible closed subvariety
X ⊆ A with deg_L X = d, and any subgroup Γ ⊆ A(F) of finite rank ρ, the intersection
X(F) ∩ Γ is covered by at most c(g, d)^(1+ρ) cosets contained in X. Equivalently,
#X°(F) ∩ Γ ≤ c(g, d)^(1+ρ) where X° is the complement of the Ueno locus
(Theorem 1.1′).

**Theorem 1.2 (New Gap Principle) / Theorem 1.3 (Uniform Bogomolov).** For
polarized (A,L) of dimension g and irreducible X generating A with deg_L X ≤ d:
the set of small-height points {P ∈ X°(Q) : ĥ(P) ≤ c1 max{1, h_Fal(A)}} is contained
in a proper Zariski-closed X′ ⊊ X with deg_L X′ < c2. All constants c_i = c_i(g, d).

**The constant is existential, not explicit.** The paper states this directly
(p. 3, after citing Rémond): "An explicit upper bound for the number of cosets was
obtained by Rémond, which additionally depends on the ambient abelian variety A via
its Faltings height... The novelty here is the complete removal of this very
dependence." And: "Before these works, the only uniform results of Mordell-Lang type
were obtained by David and Philippon [DP07, Thm. 1.13] for subvarieties of
self-products of an elliptic curve. It should be also noted that they give a
completely explicit constant in this special case. In this regard, it is interesting
to ask whether the present arguments can yield explicit upper bounds... or if
substantial new ideas are necessary."

## Bearing on the magic-square-of-squares problem

The adopted approach `uniform-height-bound-elliptic-ap` needs a constant C so that
C^(1+r) < 3 to contradict an MSS's three-term AP of doubled-point x-coordinates.
This paper is the "uniform Mordell-Lang" input to Garcia-Fritz–Pasten's Theorem 1.8,
and it confirms at the primary source that:

1. **The GGK constant c(g,d) is not explicit** — so no numerical threshold can be
   extracted from the GGK chain (matching the run's prior belief, now anchored to a
   citation).
2. **David–Philippon [DP07 Thm 1.13] is the unique prior uniform-ML result with a
   completely explicit constant**, and its scope is *subvarieties of self-products of
   an elliptic curve*. This is close to (though not identical with) the MSS AP
   configuration, where the points 2Q_i lie on a single elliptic curve E_c. Whether
   DP07's explicit constant is small enough to beat C^(1+r) < 3 is the natural next
   question — asking it is precisely what this primary source licenses.
3. GGK cite Kühne's equidistribution paper (arXiv:2101.10272) and the survey
   arXiv:2104.03431 as the curve-in-Jacobian stepping stones; both are now in the
   library.

```claim
id: ggk-uniform-mordell-lang-theorem
statement: "Uniform Mordell–Lang (Gao–Ge–Kühne, Thm 1.1): for all g, d ≥ 0 there is
c(g,d) > 0 such that for any abelian variety A of dimension g over an algebraically
closed char-0 field, irreducible closed X ⊆ A of degree d, and finite-rank subgroup
Γ ⊆ A(F), the intersection X(F) ∩ Γ is covered by at most c(g,d)^(1+rk Γ) cosets
contained in X. Constants existential only; the paper leaves open whether explicit
bounds are attainable."
hypotheses: char 0, X irreducible, Γ finite rank, degree taken with respect to an
ample polarization
holds-here: yes (the doubled-point AP of the MSS lies in a rank ≤ rk E(Q) subgroup
of a single elliptic curve; the uniform bound applies but with an unknown constant)
evidence: proved
bearing: anchors the uniform-height-bound-elliptic-ap chain at the primary source;
confirms the incomputable-constant obstruction; points to David–Philippon (explicit
constant, self-products of an elliptic curve) as the one potentially-effective
uniform-ML result relevant to the MSS
anchor: research/summaries/gao-ge-kuhne-uniform-mordell-lang-2021.md
```

```claim
id: dp07-explicit-uniform-ml-elliptic-self-products
statement: "David–Philippon (DP07 Thm 1.13) is, per GGK, the only uniform
Mordell–Lang-type result with a completely explicit constant, and it applies to
subvarieties of self-products of a single elliptic curve; all other uniform ML
results (GGK, DGH, Kühne) have existential constants."
hypotheses: subvariety of E^n, E an elliptic curve; degree and rank data as in DP07
holds-here: yes (the MSS configuration is an AP in x-coordinates of points on ONE
elliptic curve E_c, i.e. a subvariety-type condition of the E^n class — whether it
matches DP07's exact hypotheses needs checking)
evidence: asserted (stated by GGK; DP07 itself not in library)
bearing: the only open lane toward an effective constant for the uniform-height
approach: obtain/read DP07 Thm 1.13 and compute whether its explicit C beats
C^(1+r) < 3 for the MSS doubled-point AP
anchor: research/summaries/gao-ge-kuhne-uniform-mordell-lang-2021.md
```