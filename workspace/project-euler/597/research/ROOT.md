# research/ROOT.md — library as a whole

Reference library for PE 597 (Torpids): exact probability that the new boat
order is an even permutation, p(13,1800), to 10 dp.

## What the library establishes
- The race's parity is controlled by **relative-speed clocks**: boat segment
  race times are inverse-exponential, not clocks
  ([[inverse_exponential_finish_times_wikipedia]]); only the *order* of
  relative speeds W_i=v_i/(t−i)~Exp(t−i) acts as clocks, and a pair's relative
  speed is Laplace ([[laplace_difference_of_exponentials_libretexts]]).
- Sequential selection among these clocks is exactly the **Plackett–Luce /
  exponential race** with rate=distance: P(next is i)=λ_i/Σλ and a full
  ranking has probability = product of rate ratios over survivors
  ([[inid_exponential_order_statistics_nagaraja]],
  [[plackett_luce_model_wikipedia]], [[plackett_luce_exponential_race_maddison]]).
- The recursion is a **treap**: min-relative-speed boat is the root, the two
  subranges are independent random treaps, so p(n,L) decouples into
  Σ_roots (distance-ratio weight)·p(left)·p(right)
  ([[randomized_search_trees_treaps_seidel_aragon]]).
- Parity propagates additively: parity = parity(left)·parity(right)·(−1)^cross
  where cross counts flipped pairs across the root
  ([[recursive_inversion_models_permutations_meek_meila]]).
- The normalized Exp speeds are uniform on the simplex
  ([[dirichlet_distribution_wikipedia]]), so p(n,L) is a simplex volume.
- That simplex volume is **closed-form computable**: Lasserre gives
  Laplace-transform volumes of simplex sections Δ∩{a^T x ≤ t} (piecewise
  polynomial in t), so each linear cut of the parity region — and the whole
  region — is an exact rational ([[simplex_volume_sections_lasserre]]).

Together (see the sealed batch [[L0.0]] and its seal [[L1.0]]) these give the
exact, non-exhaustive recursion that the run needs; the exhaustive MC target
≈0.5002±0.00007 needs this exact route to reach 10 dp. The L1.0 batch is now
sealed at [[L1.0]] (read as research/L2.0/L1.0.md): it carries every definition,
theorem, bound and verdict of the ten L1 summaries, plus the Plackett–Luce
content recovered from L0.0, and records the one open gap — finish events are
inverse-exponential (not clocks), so the bump/finish interleaving is the run's
own derivation.

## Known limits
The w-order-only hypothesis is refuted (see MEMORY.md); only exact integration
over the Exp speeds can give the 10-dp answer.
