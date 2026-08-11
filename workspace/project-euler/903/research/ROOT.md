# research — what this now establishes

PE 903 reduces exactly (verify_red.py) to Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n),
T(n)=Σ_{m=1}^{n-1}m(m−1)m!, from proved gap-affine pair-inversion counts
f_n(k)=A_n+(k−1)B_n. All sources are routes to A_n,B_n; NONE computes the
rank-sum over the cyclic subgroup {π^i} (the novel core), and OEIS confirms
A_n,B_n,Q(n) are uncatalogued. Library = [[rank_lehmer]] + [[mechanism_pair_inversions]]
(core mechanism, two proofs) + [[order_random_permutation]] (weights) +
[[cycle_type_toolkit]] (summation engine) + small-exponent
[[cambie_yan_descents_inversions_powers]] + [[sack_ulfarsson_refined_inversion_statistics]]
(per-gap inversion machinery) + [[homomesies_permutations]] (framework) +
[[../L0.2/courtois_bard_ault_ppowers_body]] (power-side cycle structure of π^k:
τ(k) fixed points, cycle splitting, fixed-point EGF).
[[legendre_number_system_cyclic_shift]] shares the "rank inside a
cyclic-orbit" shape but for rotation, not powers — related framework only.
See [[report_literature_ranks_powers]] (clean negative) and
[[report_A_n_B_n_closed_forms_sources]] (derivation route).
