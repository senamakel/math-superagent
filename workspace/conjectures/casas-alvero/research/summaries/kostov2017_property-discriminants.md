# Kostov — "A property of discriminants" (arXiv:1701.02912; Vietnam J. Math. 47 (2019) 287–296)

Full text held at `research/sources/kostov2017_property-discriminants_html.full.md` (arXiv HTML v1, 40410 bytes).
Source URL: https://arxiv.org/html/1701.02912v1.

## What the paper establishes

For the monic generic family P = x^n + a_1 x^{n−1} + … + a_n, n ≥ 4, with discriminant R := Res(P, P′, x) ∈ ℂ[a], a = (a_1,…,a_n):

**Theorem 4 (main).** Regarded as a polynomial in a_k, the repeated discriminant
D̃_k := Res(R, ∂R/∂a_k, a_k) factors as
D̃_k = c_k (a_n)^{d(n,k)} M_k² T_k³,  d(n,k) := min(1, n−k) + max(0, n−k−2),
with c_k ∈ ℚ*, and M_k, T_k ∈ ℂ[a^≤k] (a^≤k = a with a_k deleted) irreducible with integer coefficients. The zero sets {M_k = 0} and {T_k = 0} are the projections into the a^≤k-space of the closures of the strata of {R = 0} where P has respectively **two double roots** (the Maxwell stratum M̃) or a **triple root** (Σ).

**Structure facts (Section 1).** R is quasi-homogeneous with weight(a_j) = j; degree n in each a_j (j ≤ n−1), degree n−1 in a_n; {R=0} = {P has a multiple root}; Σ and M̃ are irreducible (explicit parametrizations: z_2 = z_3 = z_1 for Σ; z_2 = z_1, z_4 = z_3 for M̃). Example 2 (n=3): D̃_a = −64c(b³−27c²)³, D̃_b = −64c(a³−27c)³, D̃_c = −432(−3b+a²)³ — only the cubes of T_k and powers of a_n appear (no M_k since M̃ doesn't exist for n<4). Example 3 (n=4): explicit irreducible M_a,…,T_d; e.g. M_b = a²d − c² defines the Whitney umbrella.

**Lemma 1 (from [5], Prop 7):** D̃_k = (a_n)^{d(n,k)} D̃^0_k where D̃^0_k is not divisible by any a_i.

## Relationship to the run's problem

- This is the **same resultant family** the run's scheme method uses (R_i = Res(f, H_i f) is D̃-type with the ordinary derivative), and the quasi-homogeneous weight(a_j) = j is exactly the run's weighted scaling (x ↦ λx, a_j ↦ λ^j a_j). The paper gives an independent, fully-worked structural analysis of these discriminants over ℂ[a]: irreducibility, quasi-homogeneity, and the **geometric meaning of the square factor M_k² = 0 as "P and P′ share two distinct roots"**.
- For CA the direct relevance: a CA polynomial is one where every (P, P^(m)) shares a root; the M_k/T_k stratification is the natural refinement (share *two* roots / triple root). The run's resultants Res(f, H_i f) for the highest indices i = d−2, d−1 reduce to discriminants of the near-derivative polynomials P_{m,k} (compare the Schaub–Spivakovsky Theorem 5 trailing-index result, held in full). Kostov's T_k = Res(P_k, P_k′, x) with P_k = P − xP′/(n−k) is structurally the same "derivative minus projection" combination the run's pinned-centroid / Gauss–Lucas arguments use.
- Caveat: char 0 (ℂ[a]) only, ordinary derivatives; no char-p content, so it does not speak to the run's bad-prime break.

## Status

Sourced/asserted — read the abstract, Section 1, Theorem 4, Examples 2–3 and the lemmas' statements; the full proofs in Section 3 were not independently re-verified by this run. The n=4 explicit factors are checkable with sympy (the run's oracle machinery) if needed.

## File cleanup note

The file `research/sources/kostov2020_higher-order-discriminants.full.md` (6191 bytes) is a **mislabeled duplicate** — it holds the arXiv abstract landing page of THIS 2017 paper (1701.02912), not the 2020 higher-order discriminants paper (which is `kostov2020_highorder-discriminants.full.md`, arXiv:1702.08216, held in full). Both files coexist; the 2017 full text is now the `_html` file above, so the mislabeled abstract-page duplicate adds nothing and should be ignored or removed.
