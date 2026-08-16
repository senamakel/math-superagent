# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `ErdosGyarfas_Statement.lean` | Formal statement of the Erdős–Gyárfás conjecture (δ≥3 ⟹ a cycle of length 2^k, k≥2); stated with `sorry`, open conjecture. |
| `LemmaA_chord_deletion.lean` | Formal statement of Lemma A (chord deletion preserving 2-connectivity and min-degree≥2) with IsTwoConnected definition; proof `sorry` (depends on Dirac's minimal-2-connected theorem, not in Mathlib). |
| `LemmaB_cycle_lengths_transfer.lean` | Formal statement of Lemma B (cycle lengths of G = those of G−e union the lengths of simple a–b paths in G−e plus one) with CycleLengths definition; proof `sorry`. |
| `LemmaB_cycle_splits_to_path.lean` | Hard direction of Lemma B, stated with sorry: a cycle of G using edge e=s(a,b) splits at that edge into a simple a–b path of G.deleteEdges {s(a,b)} of length one less; plus the inclusion CycleLengths G ⊆ C(G−e) ∪ path-lengths-plus-one. |
| `LemmaB_path_plus_chord_is_cycle.lean` | Proved easy direction of Lemma B: a simple a–b path P in G.deleteEdges {s(a,b)} closed by the chord e = ab gives a cycle of G of length |P|+1. Kernel-checked, no sorry. |
| `Lemma_b_single.lean` | Broken draft: cycle from a single neighbour at position i; does not compile, 1 sorry. Informal claim with 1≤i is false; correct hypothesis is 2≤i. |
| `Lemma_b_single_fixed.lean` | Newer draft with hypothesis 2≤i; does not compile (coercion of subpathPos blocks the lemmas). |
| `Lemma_b_single_neighbor.lean` | Broken draft: subpathPos_not_mem_start; does not compile, 2 sorries. |
| `LongestPathLemma_b1.lean` | **Proved**: every neighbour of the start vertex of a longest path lies on the path. Kernel-checked, no sorry. |
| `LongestPathLemma_b2.lean` | Broken draft: cycle from two neighbours at positions 1≤ia<ib; does not compile, 1 sorry. |
| `LongestPathLemma_b2_fixed.lean` | Newer draft of the two-neighbours cycle lemma (cycle_from_two_neighbors with hypothesis 1≤ia<ib). Does not compile: subpathPos_getVert is scoped with `where` and invisible at its use site, Walk.append_assoc does not match the cons-form IsCycle goal, length goal unsolved. Contains a detailed comment planning the isCycle_append disjointness route. 0 sorries but no complete proof. |
| `Subpath.lean` | Broken draft: shared subpathPos positional lemmas; does not compile (getVert application, mem_tail/isPath_def unknown). |
| `Subpath_positional.lean` | Broken draft: subpathPos lemmas with `where`-scoped helper; does not compile (unknown subpathPos_getVert). |
| `Test_subpath.lean` | Scratch test of subpathPos + length; compiles, no #print axioms. |
| `Test_subpath2.lean` | Scratch test of subpathPos + isPath; compiles, no #print axioms. |
| `VERIFICATION_REPORT.md` | Per-file verification report of the whole code/lean tree: compiles/sorry/axioms for every file, precise status of the two load-bearing lemmas (Lemma A stated+sorry; Lemma B easy direction proved, hard direction sorry), which statement of the conjecture is formalised, and what remains unproved. |
