<!-- brief -->
PE 903 reduces exactly (verify_red.py) to Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n),
T(n)=Σ_{m=1}^{n-1}m(m−1)m!, from proved gap-affine pair-inversion counts
f_n(k)=A_n+(k−1)B_n. All sources are routes to A_n,B_n; NONE computes the
rank-sum over the cyclic subgroup {π^i} (the novel core), and OEIS confirms
A_n,B_n,Q(n) are uncatalogued. Library = [[rank_lehmer]] + [[mechanism_pair_inversions]]
(core mechanism, two proofs) + [[order_random_permutation]] (weights) +
[[cycle_type_toolkit]] (summation engine) + small-exponent
[[cambie_yan_descents_inversions_powers]] + [[sack_ulfarsson_refined_inversion_statistics]]
(per-gap inversion machinery) + [[homomesies_permutations]] (framework, does
not close core). See [[report_literature_ranks_powers]] (clean negative) and
[[report_A_n_B_n_closed_forms_sources]] (concrete derivation route).
<!-- /brief -->

| File | Purpose |
| --- | --- |
| L2/[[rank_lehmer]] | Lehmer/factoradic digits = lex rank |
| L2/[[mechanism_pair_inversions]]* | **Core**: gap-affine pair-inversion probs (A_n,B_n mechanism) |
| L2/[[order_random_permutation]] | ord(π) law → n!/ord(π) weights |
| L2/[[cycle_type_toolkit]] | Cycle-type summation engine for A_n,B_n |
| L1/[[cambie_yan_descents_inversions_powers]] | Small-exponent closed forms for lifts |
| L1/[[sack_ulfarsson_refined_inversion_statistics]] | Per-gap k-step inversion distribution |
| L1/[[homomesies_permutations]] | Homomesy framework; rank not covered |
| L1/[[report_literature_ranks_powers]] | Clean negative on novel core |
| L2/[[report_A_n_B_n_closed_forms_sources]] | Concrete derivation route to A_n,B_n |
| L2/[[reports_negatives]] | OEIS uncatalogued; negative list |
| L0/gaetz_ryba… | Dead download (unrelated ML paper) — flagged |
| verify_*.py | Oracles: literal rank(π^i) Q(n), Cambie-Yan check |
