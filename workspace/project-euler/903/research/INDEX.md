# Index — research

<!-- brief -->
Reference library for PE 903: Q(n)=ΣπΣ_{i=1}^{n!} rank(π^i) mod(1e9+7). memory.md/verify_red.py reduce it to closed forms for A_n,B_n in the gap-affine pair-inversion count f_n(k)=A_n+(k−1)B_n. `L0/` holds full texts (never edited); `L1/` holds one note per source.

CORE MECHANISM PROVED, two independent routes: per-cycle-type inversion prob is translation-invariant and affine in the gap, depending only on n, a_1=#fixed, a_2=#2-cycles ([[conjugacy_class_statistics_body]] Lemma 4.7 / Thm 4.8); exact identically, under Ewens uniform, with fixed-point-conditioning ([[pinsky_schickentanz_ewens_html]] Thm 1a, Prop 10a). NEW this cycle: [[pinsky_inversion_fixed_points]] gives the EXACT finite-n per-pair inversion probability conditioned on exactly k fixed points — the concrete fixed-point-conditioned summation route to A_n, B_n, closing the gap between the two proved mechanisms.

Rank/Lehmer structure: [[lehmer_factorial_norm]] & [[factorial_number_system_wiki]] — factoradic digits give lexicographic rank.

Closed forms for descents/inversions of π^k (fixed k) via divisor functions: [[cambie_yan_html]] (confirms [[archer_geary_descents_powers]]); small-exponent regime only.

Supporting: [[hultman_products_random_permutations]] (character method, independent products only); [[nathanson_fixed_points_powers]] (fixed points of powers ↔ class); [[leanos_mth_roots_of_permutations]] (root counts, not usable).

Negative: [[report_literature_ranks_powers]] — no source gives a closed form for the rank-sum over a cyclic subgroup (the novel core); OEIS probes [[oeis_Aseq]][[oeis_Qseq]][[oeis_Bdiv]][[oeis_invpowers]][[oeis_invpowers2]] all "no results".
<!-- /brief -->

## File table
| File | Purpose |
| --- | --- |
| `L1/archer_geary_descents_powers.md` | A&G 2406.09369; provenance of CY descent-in-powers line |
| `L1/cambie_yan_html.md` | Cambie-Yan 2408.01211; closed forms for descents/inversions in π^k |
| `L1/conjugacy_class_statistics_body.md` | Campion-Loth et al 2301.00898; per-cycle-type inversion probs |
| `L1/factorial_number_system_wiki.md` | factoradic/Lehmer code → lexicographic rank |
| `L1/hultman_products_random_permutations.md` | 1301.0430; character method for product stats |
| `L1/leanos_mth_roots_of_permutations.md` | 1005.1531; m-th-root counts by cycle type |
| `L1/lehmer_factorial_norm.md` | Zawiślak 2111.03951; factoradic digits |
| `L1/nathanson_fixed_points_powers.md` | 2206.04021; fixed points of powers ↔ class |
| `L1/oeis_*.md` | negative OEIS lookups (no results) |
| `L1/pinsky_inversion_fixed_points.md` | Pinsky EJC P2.36 (10.37236/14250): exact finite-n fixed-point-conditioned per-pair inversion prob |
| `L1/pinsky_schickentanz_ewens_html.md` | P&S 2510.20654; Ewens inversion probs (affine in gap) |
| `L1/pinsky_schickentanz_ewens_inversions.md` | P&S inversion-statistic paper |
| `L1/report_literature_ranks_powers.md` | current negative report (supersedes report_cited_facts, report_rank_powers) |
| `L0/*.full.md` | full texts (never edited) |
| `verify_cambie_yan.py` `verify_facts.py` | verification scripts |
