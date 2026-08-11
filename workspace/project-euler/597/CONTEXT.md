# Shared context

Standing brief: what the `research/` library establishes for PE 597 (Torpids). Detail lives in the fold notes behind wikilinks; `research/INDEX.md` lists every source with its URL.

## Model

Speeds v_j are iid Exp(1). Boat j rows at v_j until it finishes (at L) or bumps the nearest rowing boat ahead (then OUT, passed freely; bumped boat keeps rowing). New-order parity = (# pairs i<j with a bump chain i→…→j) mod 2. Target: p(13,1800).

## Established (sources)

- **Rate-ratio products.** Order-statistic spacings of iid Exp(1) are independent Exps with rates n,…,1 ([[exponential_order_statistics_memoryless_kth]]); for independent Exps with rates λ_i, P(i fires first)=λ_i/Σλ and a specific firing order has probability = product of rate ratios over survivors ([[competing_exponential_clocks_uchicago]]). For inid exponentials the successive order statistics are the Nevzorov/Tikhov antirank sequence: P(next is i)=λ_i/Σ_survivors λ ([[inid_exponential_order_statistics_nagaraja]]).
- **The clocks are relative speeds.** W_i = v_i/(t−i) ~ Exp(t−i), rate = *distance* t−i, so "slowest relative to target t" is chosen with probability proportional to its distance; recursing on the two subranges makes p(n,L) a sum of products of distance ratios — the exact-integration route memory.md demands (parity depends on speed magnitudes, not just rank order). Finish times are NOT clocks: (L−p_j)/v_j is inverse-exponential ([[inverse_exponential_finish_times_wikipedia]]); a pair's relative speed v_j−v_i is standard Laplace ([[laplace_difference_of_exponentials_libretexts]]). Normalized speeds are uniform on the simplex, so p(n,L) is a simplex volume of the parity region ([[dirichlet_distribution_wikipedia]]).
- **Subrange recursion is a treap.** Root = boat slowest relative to t; left/right subtrees are the treaps of the adjacent ranges. With i.i.d. continuous priorities (here the Exp speeds) the two subtrees are independent random treaps, so p(n,L) = Σ_root (distance-ratio weight)·p(left)·p(right), no cross-range coupling ([[randomized_search_trees_treaps_seidel_aragon]]).
- **Parity accumulates additively over the recursion.** Inversions in a permutation built by recursive merges arise only inside each node's left/right subranges + the cross pairs flipped at that node; total inversion distance = Σ_node (per-node cross inversions), and the two child subranges otherwise decouple ([[recursive_inversion_models_permutations_meek_meila]]). So with root r of range [a,b], parity([a,b]) = parity([a,r−1])·parity([r+1,b])·(−1)^{cross}, where cross = # pairs (i in left, j in right) whose relative order flips at r — combined with the treap's sum-of-products form this gives the exact recursion for the parity mass.
- **Closed-form simplex sections (make the exact integral computable).** p(n,L) is the uniform-simplex volume of the parity region, a finite union of sub-simplices cut by linear inequalities a^T x ⋛ c. Lasserre gives closed-form Laplace-transform volumes of a simplex section Δ∩{a^T x ≤ t} (piecewise polynomial of degree n in t), so each cut — hence the whole parity region — is an exact rational rather than numeric quadrature or enumeration ([[simplex_volume_sections_lasserre]]). This is the missing last step that turns the recursion into a finite exact computation for the 10-dp target.

## Known limits

- w-order hypothesis (parity from rank of w_j = v_j/(L−p_j) alone) REFUTED (memory.md): magnitudes matter; exact integration required.
- MC pins p(13,1800) ≈ 0.5002 ± 0.00007 (60M samples): any true bias ≤ ~3e-4; the 10-dp answer needs the exact recursion, not MC.

## Contradictions / gaps

None between sources and the model.