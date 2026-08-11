# Index — research/L1.0

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0.0.md` | Seal for batch L0.0 (10 notes): relative-speed clocks form the Plackett–Luce exponential race; p(n,L) = Σ_root (distance-ratio)·p(left)·p(right) with additive parity, via independent-subtree treap structure. Wikilinks all 10 originals it compresses. |
| `competing_exponential_clocks_uchicago.md` | Summary of UChicago STAT253/317 (Yibi Huang): min of independent exponentials fires with probability proportional to pooled rate; fixed firing order has probability = product of λ_i/Σλ over survivors; memoryless. |
| `dirichlet_distribution_wikipedia.md` | Summary of Wikipedia "Dirichlet": normalized iid Exp(1) are uniform on the simplex; p(n,L) = uniform-simplex measure of the parity region. |
| `exponential_order_statistics_memoryless_kth.md` | Summary of KTH note (Timo Koski): order-statistic spacings of iid Exp(1) are independent Exps with rates n,n−1,…,1. |
| `inid_exponential_order_statistics_nagaraja.md` | Summary of Nagaraja INID exponential order statistics (via UIC STAT416): Nevzorov/Tikhov antirank law P(next is i)=λ_i/Σλ_survivors; relative speeds W_i=v_i/(t−i)~Exp(t−i) rate=distance. |
| `inverse_exponential_finish_times_wikipedia.md` | Summary of Wikipedia "Inverse distribution": finish time (L−p_j)/v_j is inverse-exponential — finish events are NOT exponential clocks. |
| `laplace_difference_of_exponentials_libretexts.md` | Summary of Siegrist LibreTexts 5.28: difference of two iid Exp(1) is standard Laplace — distribution of the relative speed v_j−v_i. |
| `randomized_search_trees_treaps_seidel_aragon.md` | Summary of Seidel & Aragon "Randomized Search Trees" (Algorithmica 1996): treap root = extremal priority; with iid continuous priorities the two subtrees are independent random treaps — makes p(n,L) a sum of products. |
| `recursive_inversion_models_permutations_meek_meila.md` | Summary of Meek & Meilă NIPS 2014: inversion count additive over the recursion tree; parity = parity(left)·parity(right)·(−1)^cross. |
| `simplex_volume_sections_lasserre.md` | Fold note for Lasserre (Optim. Lett. 2015, L0.1): closed-form Laplace-transform volumes of simplex sections make the parity-region volume an exact rational — last step to the 10-dp target. |
