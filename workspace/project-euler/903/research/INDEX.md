# Index — research

Reference library for PE 903: Q(n)=ΣπΣ_{i=1}^{n!} rank(π^i) mod(1e9+7). memory.md/verify_red.py reduce it to closed forms for A_n,B_n in the gap-affine pair-inversion count f_n(k)=A_n+(k−1)B_n. `L0/` holds full texts (never edited); `L1/` holds one note per source.

## Core mechanism — f_n gap-affine & affine-in-gap is PROVED, two independent routes
- [[conjugacy_class_statistics_body]] (Campion-Loth et al, 2301.00898): per-cycle-type inversion prob Prλ[I_{i,j}=1] is translation-invariant, affine in gap, depends only on n,a_1=#fixed,a_2=#2-cycles (Lemma 4.7); weighted-inversion means depend only on n,a_1,a_2 (Thm 4.8). L0: `conjugacy_class_statistics_body.full.md`.
- [[pinsky_schickentanz_ewens_html]] (Pinsky & Schickentanz, 2510.20654): exact pair-inversion probs under Ewens (uniform=θ=1), unconditioned (Thm 1a, affine in gap) and fixed-point-conditioned (Prop 10a); θ=0 rotation: 1/2+(j−i−1)/[(n−1)(n−2)]. Second independent proof of the A_n,B_n mechanism; concrete summation route. L0: `pinsky_schickentanz_ewens_html.full.md`.
- [[cambie_yan_html]] (Cambie-Yan, 2408.01211): closed forms for expected descents/inversions in π^k for fixed k, n≥2k+1, via divisor functions; confirms [[archer_geary_descents_powers]]. Small-exponent regime only (not the n=1e6 sum). L0: `cambie_yan_html.full.md`.

## Rank/Lehmer structure
- [[lehmer_factorial_norm]] (Zawiślak 2111.03951) & [[factorial_number_system_wiki]]: factoradic (Lehmer) digits give lexicographic rank; digits independent, j-th uniform on {0..j}. Neither addresses powers or the cyclic subgroup {π^i}.

## Supporting / routed
- [[hultman_products_random_permutations]] (1301.0430): irreducible-character method for expected stats on products of class-distributed perms; template, not solution (covers independent products, not {π^i}).
- [[nathanson_fixed_points_powers]] (2206.04021): F(σ^ℓ)=Σ_{k|ℓ}k·C(k), Möbius inversion recovers cycle counts — fixed points of powers determine conjugacy class; cross-check for the a_1,a_2 sums.
- [[leanos_mth_roots_of_permutations]] (1005.1531): exact m-th-root counts by cycle type; NOT directly usable (root counts don't feed the intra-subgroup rank sum).

## Reports & negative lookups
- [[report_literature_ranks_powers]] (current; supersedes [[report_cited_facts]] & [[report_rank_powers]]): closest match is Cambie-Yan; NO source gives a closed form for the rank-sum over a cyclic subgroup (the genuinely novel core); clean negative OEIS lookups — [[oeis_Aseq]] [[oeis_Qseq]] [[oeis_Bdiv]] [[oeis_invpowers]] [[oeis_invpowers2]] all "no results".
