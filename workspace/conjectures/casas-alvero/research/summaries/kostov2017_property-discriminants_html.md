# Kostov — "A property of discriminants" (arXiv:1701.02912; Vietnam J. Math. 47 (2019) 287–296) — full-text record

Full text held at `research/sources/kostov2017_property-discriminants_html.full.md` (arXiv HTML v1, fetched this cycle).
Source URL: https://arxiv.org/html/1701.02912v1.

This is the same paper as `research/summaries/kostov2017_property-discriminants.md` — that file is the canonical summary. This file exists because the download created a per-source digest here; its content is superseded by the canonical summary, which states:

**Main theorem (Theorem 4).** For the monic generic P = x^n + a_1 x^{n−1} + … + a_n, n ≥ 4, with discriminant R = Res(P, P′, x), the repeated discriminant D̃_k = Res(R, ∂R/∂a_k, a_k) factors as

D̃_k = c_k (a_n)^{d(n,k)} M_k² T_k³,  d(n,k) = min(1, n−k) + max(0, n−k−2),

with c_k ∈ ℚ*, M_k, T_k ∈ ℂ[a^≤k] irreducible with integer coefficients, where {M_k = 0} and {T_k = 0} are the projections of the Maxwell stratum (two double roots) and the triple-root stratum Σ of {R = 0}. R is quasi-homogeneous with weight(a_j) = j; degree n in a_j (j ≤ n−1), degree n−1 in a_n. Examples: n=3 (only T_k cubes, no M_k), n=4 (explicit M_a,…,T_d; M_b = a²d − c² is the Whitney umbrella).

**Bearing on this run:** same resultant family as the run's R_i = Res(f, H_i f); the quasi-homogeneous weight(a_j) = j is exactly the run's weighted scaling; the square factor M_k² = 0 means "P and P′ share two distinct roots" — the natural stratification of the CA shared-root conditions. Char 0 (ℂ[a]) only, no char-p content.

**Scholar judgement (does not materially help):** Kostov's repeated discriminant D̃_k = Res(R, ∂R/∂a_k, a_k) is the discriminant of the *single* discriminant R against its partial derivative — i.e. it detects when two *double* roots collide (Maxwell stratum) — not the CA resultant family R_i = Res(f, H_i f) against Hasse derivatives. The only overlap with this run's needs is the quasi-homogeneous weight(a_j) = j, which the run already holds primary from Graf von Bothmer et al 2007 (line ~87: "the equation Res_X(P,P_i) is homogeneous of weighted degree d(d-i), giving weight j to a_j"). Kostov is char-0-only and adds no CA-specific or char-p content. Read it once for the weighted-scheme/stratification vocabulary; do not plan work on it.

**File cleanup:** `research/sources/kostov2020_higher-order-discriminants.full.md` is a mislabeled duplicate holding the 1701.02912 abstract page — do not cite it for the 2020 paper (that is `kostov2020_highorder-discriminants.full.md`, arXiv:1702.08216, held in full).
