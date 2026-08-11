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

Together (see the sealed batch [[L0.0]] and its seal [[L1.1]]) these give the
exact, non-exhaustive recursion that the run needs; the exhaustive MC target
≈0.5002±0.00007 needs this exact route to reach 10 dp. The L0.0 batch is sealed
at [[L1.1]] (read as research/L1.1/L0.0.md): a detailed, self-contained digest
of all ten full texts — every definition, theorem, bound, verdict and the one
open gap (finish events are inverse-exponential, not clocks, so the bump/finish
interleaving is the run's own derivation). The L1.0 batch is sealed at [[L1.0]]
(read as research/L2.0/L1.0.md): it carries the same thesis at the L1-summary
level plus the Plackett–Luce content recovered from L0.0.

## Known limits
The w-order-only hypothesis is refuted (see MEMORY.md); only exact integration
over the Exp speeds can give the 10-dp answer.
**The closed-form recursion claimed above is REFUTED** (see MEMORY.md and
`research_recursion_test.py`): root = argmin W with p = sum of distance-ratio
weight · p(left)·p(right)·(−1)^cross gives p(3,160)=2/3 (truth 56/135) and
p(4,400)=5/6 (truth 0.5107843137); per-vector smallest counterexample
n=2,L=160,speeds=[0.89157,0.33049] (oracle odd, recursion even); the two crux
claims C1 (sub-range decoupling, fails 20177/300000) and C2 (cross=|L||R|, fails
152466/300000) are both false. The treap/sum-of-products route does NOT match
the race: bump vs finish chronology (finish events are inverse-exponential, not
clocks) breaks decoupling and the cross value. An exact route must integrate
the true bump/finish chronology over the Exp speeds.
