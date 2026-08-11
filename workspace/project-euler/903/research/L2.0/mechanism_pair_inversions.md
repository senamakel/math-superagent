# Fold: gap-affine pair-inversion mechanism (PROVED core)

The mechanism behind f_n(k)=A_n+(k−1)B_n — the pair-inversion count over [[../../L1/conjugacy_class_statistics_body.md|both routes]] — is established two independent ways, plus a small-exponent confirmation. No source in this fold computes the rank-sum over {π^i} itself (that stays novel/open); each proves only the per-pair inversion probability.

- [[conjugacy_class_statistics_body]] (Campion-Loth 2301.00898): per-cycle-type inversion prob Prλ[I_{i,j}=1] is translation-invariant, affine in gap, depends only on n, a_1=#fixed, a_2=#2-cycles (Lemma 4.7); weighted-inversion means depend only on n,a_1,a_2 (Thm 4.8). L0 `conjugacy_class_statistics_body.full.md`.
- [[pinsky_schickentanz_ewens_html]] (2510.20654): exact pair-inversion probs under Ewens (uniform θ=1), unconditioned (Thm 1a, affine in gap) and fixed-point-conditioned (Prop 10a); θ=0 rotation: 1/2+(j−i−1)/[(n−1)(n−2)]. L0 `pinsky_schickentanz_ewens_html.full.md`.
- [[pinsky_inversion_fixed_points]] (Pinsky, EJC P2.36): exact finite-n expected-inversion formula conditioned on exactly k fixed points; derangement k=0: n(n−1)/4+n/6+1/12+o(1). Gives the concrete summation route: average per-gap inversion prob over the fixed-point-count distribution of a uniform permutation. L0 `pinsky_inversion_fixed_points.full.md`.
- [[cambie_yan_html]] (2408.01211) + [[archer_geary_descents_powers]]: closed forms for E[des/inv(π^k)] for fixed k, n≥2k+1, via divisor functions; per-exponent gap-affine counts explain f_n linearity, but only cover exponents k≤(n−1)/2 (large-exponent regime is the open step). L0 `cambie_yan_html.full.md`, `archer_geary_descents_powers.full.md`.

<!-- brief -->
Proved: per-gap pair-inversion probability is translation-invariant and affine in the gap, depending only on n and fixed/2-cycle counts; two independent proofs + small-exponent closed forms. Open: the rank-sum over the cyclic subgroup {π^i} and the large-exponent regime behind the full A_n,B_n.
