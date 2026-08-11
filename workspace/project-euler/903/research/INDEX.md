# Index — research

<!-- brief -->
PE 903 reduces exactly (verify_red.py) to Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n),
T(n)=Σ_{m=1}^{n-1}m(m−1)m!, from proved gap-affine pair-inversion counts
f_n(k)=A_n+(k−1)B_n. All sources are routes to A_n,B_n; NONE computes the
rank-sum over the cyclic subgroup {π^i} (the novel core), and OEIS confirms
A_n,B_n,Q(n) are uncatalogued. Library = [[rank_lehmer]] + [[mechanism_pair_inversions]]
(core mechanism, two proofs) + [[order_random_permutation]] (weights) +
[[cycle_type_toolkit]] (summation engine) + small-exponent
[[cambie_yan_descents_inversions_powers]] + [[sack_ulfarsson_refined_inversion_statistics]]
(per-gap inversion machinery) + [[homomesies_permutations]] (framework).
[[legendre_number_system_cyclic_shift]] shares the "rank inside a
cyclic-orbit" shape but for rotation, not powers — related framework only.
See [[report_literature_ranks_powers]] (clean negative) and
[[report_A_n_B_n_closed_forms_sources]] (derivation route).
<!-- /brief -->

The way in: start in **`L2/`** (the curated core-mechanism and synthesis notes),
then **`L1/`** (one short summary file per source), then **`L0/`** (raw fetches / full
texts, read only when the L1 summary is not enough). The two per-folder index files
below this one list and describe every file in each.

| Folder / File | Purpose |
| --- | --- |
| `L2/` → INDEX.md | Curated synthesis: `mechanism_pair_inversions.md` (PROVED per-gap affine mechanism, two proofs), `rank_lehmer.md` (rank model), `order_random_permutation.md` (n!/ord weights), `cycle_type_toolkit.md` (summation engine), `report_A_n_B_n_closed_forms_sources.md` (step-by-step derivation route to A_n,B_n), `reports_negatives.md` (clean negative on the cyclic-subgroup rank-sum) |
| `L1/` → INDEX.md | One short summary per source: Cambie-Yan (small-exponent powers), Campion-Loth (per-class gap-affine), Pinsky-Schickentanz & Pinsky (Ewens / fixed-point inversion), Sack-Úlfarsson (per-gap Eulerian machinery), Ford (cycle-type toolkit), Hultman, Leaños, Nathanson, Legendre (cyclic-orbit rank), homomesy framework, Stong (average order), OEIS negative lookups, literature reports |
| `L0/` → INDEX.md | Raw fetches and `.full.md` full texts (one companion per L1 summary); includes flagged dead downloads (Gaetz-Ryba mislabel, Pinsky derangement marker). Read the L1 summary first, open full only when needed |
| `verify_cambie_yan.py` | Verification script: checks Cambie-Yan (2408.01211) Thms 1.1/1.2 expected-descents/inversions formulas vs direct enumeration n=3..7, checks the f_n(k) gap-affinity from extend_f.json, and re-measures per-gap pair-inversion probabilities under the random-power law n=5..7 |
| `verify_facts.py` | Verification oracle: literal rank(pi^i) double-sum Q(n) for reachable n, plus the rank-statistics check sum of all 1-based ranks = n!(n!+1)/2; reproduces rank(2,1,3)=3, Q(2)=5, Q(3)=88 |
