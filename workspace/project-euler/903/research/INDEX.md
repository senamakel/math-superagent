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

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0/gaetz_ryba…` | Dead download (unrelated ML paper) — flagged |
| `L1/[[cambie_yan_descents_inversions_powers]]` | Small-exponent closed forms for lifts |
| `L1/[[homomesies_permutations]]` | Homomesy framework; rank not covered |
| `L1/[[legendre_number_system_cyclic_shift]]` | Rank inside a cyclic-orbit (rotation, not powers) |
| `L1/[[report_literature_ranks_powers]]` | Clean negative on novel core |
| `L1/[[sack_ulfarsson_refined_inversion_statistics]]` | Per-gap k-step inversion distribution |
| `L1/legendre_number_system_cyclic_shift.md` | L1 summary of Legendre arXiv:1007.2870: a number system ranking/unranking permutations inside a cyclic-shift orbit. Shares PE 903's "rank within one map-orbit" shape but the map is one-line word rotation (orbit size n), not the permutation-power subgroup {π^1..π^d} the problem sums over — closest located related-framework source, not a solution to A_n,B_n. |
| `L2/[[cycle_type_toolkit]]` | Cycle-type summation engine for A_n,B_n |
| `L2/[[mechanism_pair_inversions]]*` | **Core**: gap-affine pair-inversion probs (A_n,B_n mechanism) |
| `L2/[[order_random_permutation]]` | ord(π) law → n!/ord(π) weights |
| `L2/[[rank_lehmer]]` | Lehmer/factoradic digits = lex rank |
| `L2/[[report_A_n_B_n_closed_forms_sources]]` | Concrete derivation route to A_n,B_n |
| `L2/[[reports_negatives]]` | OEIS uncatalogued; negative list |
| `verify_*.py` | Oracles: literal rank(π^i) Q(n), Cambie-Yan check |
