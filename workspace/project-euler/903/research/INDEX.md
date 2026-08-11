# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0/gaetz_ryba_stable_chars_permutation_patterns.full.full.md` | Full text of the erroneous fetch (arXiv:2107.10110, a zeroth-order-optimization ML paper) — unrelated to permutation combinatorics. Dead download; see L1 flag. |
| `L0/homomesies_permutations_arxiv.md` | Raw summary of the arXiv abstract page for Elder–Lafrenière–McNicholas–Striker–Welch, "Homomesies on permutations" (2206.13409): 128 homomesy instances on S_n under Lehmer-code rotation, etc. Full text companion is homomesies_permutations_arxiv.full.md (abstract only; PDF not captured). Only a route toward the run's open core (averaging rank over the cyclic subgroup {pi^i}), not the solution — map here is Lehmer-code rotation, not permutation power, and rank is not among the homomesic statistics. Curated summary: L1/homomesies_permutations.md |
| `L0/pinsky_inversion_derangements.arxiv.md` | _(undescribed)_ |
| `L0/sack_ulfarsson_refined_inversion_pdf.md` | _(undescribed)_ |
| `L0/sack_ulfarsson_refined_inversion_statistics.md` | Raw summary of the same Sack & Úlfarsson paper (arXiv:1106.1995v2) as sack_ulfarsson_refined_inversion_pdf.md — k-step inversion distribution (Thm 4.4), ninvsum identities (Thm 2.5, Cor 2.6), zone-crossing vector encoding (Prop 3.3, Lemma 3.4, Thm 3.8), (k1,k2)-step inversions (Prop 4.6/4.8). Parallel/duplicate superceded by the pdf.md summary; covered by the curated L1/sack_ulfarsson_refined_inversion_statistics.md |
| `L1/archer_geary_descents_powers.md` | _(undescribed)_ |
| `L1/cambie_yan_descents_inversions_powers.md` | _(undescribed)_ |
| `L1/cambie_yan_html.md` | _(undescribed)_ |
| `L1/conjugacy_class_statistics.md` | _(undescribed)_ |
| `L1/conjugacy_class_statistics_body.md` | _(undescribed)_ |
| `L1/factorial_number_system_wiki.md` | _(undescribed)_ |
| `L1/ford_cycle_type_toolkit.md` | _(undescribed)_ |
| `L1/homomesies_permutations.md` | Summary of Elder et al (2206.13409): homomesy — statistic average constant on each orbit of a map; Lehmer-code rotation orbits all size lcm(1..n), 45 inversion stats homomesic (Thm 4.7/4.8); conceptual framework for averaging rank over the cyclic subgroup {π^i}, rank itself not covered |
| `L1/hultman_products_random_permutations.md` | _(undescribed)_ |
| `L1/leanos_mth_roots_of_permutations.md` | _(undescribed)_ |
| `L1/lehmer_factorial_norm.md` | _(undescribed)_ |
| `L1/nathanson_fixed_points_powers.md` | _(undescribed)_ |
| `L1/oeis_Aseq.md` | _(undescribed)_ |
| `L1/oeis_Bdiv.md` | _(undescribed)_ |
| `L1/oeis_Qseq.md` | _(undescribed)_ |
| `L1/oeis_invpowers.md` | _(undescribed)_ |
| `L1/oeis_invpowers2.md` | _(undescribed)_ |
| `L1/pinsky_inversion_fixed_points.md` | _(undescribed)_ |
| `L1/pinsky_schickentanz_ewens_html.md` | _(undescribed)_ |
| `L1/pinsky_schickentanz_ewens_inversions.md` | _(undescribed)_ |
| `L1/report_cited_facts.md` | _(undescribed)_ |
| `L1/report_literature_ranks_powers.md` | _(undescribed)_ |
| `L1/report_rank_powers.md` | _(undescribed)_ |
| `L1/sack_ulfarsson_refined_inversion_statistics.md` | L1 summary of Sack & Úlfarsson, arXiv:1106.1995, refined (k-step) inversion statistics: H_{n,k} distribution via Eulerian polynomials (Thm 4.4), ninvsum/zone-crossing machinery — direct analytic handle on the gap function f_n(k); treats only the single permutation π, not the cyclic subgroup {π^i} PE 903 sums over |
| `L1/stong_average_order_permutation.md` | _(undescribed)_ |
| `L2/cycle_type_toolkit.md` | _(undescribed)_ |
| `L2/mechanism_pair_inversions.md` | _(undescribed)_ |
| `L2/order_random_permutation.md` | _(undescribed)_ |
| `L2/rank_lehmer.md` | _(undescribed)_ |
| `L2/report_A_n_B_n_closed_forms_sources.md` | Synthesis note (12KB) answering which located sources give (a) per-gap pair-inversion probabilities affine in the gap (Campion-Loth Lemma 4.7 + Thm 4.8, Pinsky-Schickentanz Thm 1a/Prop 10a), (b) concrete summation routes to A_n,B_n via cycle-type calculus (Ford), and (c) an Eulerian-polynomial closed form for per-gap k-step inversion counts (Sack-Ulfarsson Thm 4.4). Records the clean-negative finding: no source computes the rank-sum over the cyclic subgroup {pi^i} (the novel core), and describes the step-by-step route to derive A_n,B_n. The concrete "how to compute Q(10^6)" synthesis for the open problem. |
| `L2/reports_negatives.md` | _(undescribed)_ |
| `verify_cambie_yan.py` | Verification script: checks Cambie-Yan (2408.01211) Thms 1.1/1.2 expected-descents/inversions formulas vs direct enumeration n=3..7; checks the f_n(k) gap-affinity from extend_f.json; and re-measures per-gap pair-inversion probabilities under the random-power law n=5..7 |
| `verify_facts.py` | Verification oracle: literal rank(pi^i) double-sum Q(n) for reachable n, plus the rank-statistics check sum of all 1-based ranks = n!(n!+1)/2; reproduces rank(2,1,3)=3, Q(2)=5, Q(3)=88 |
