# Shared context

Standing brief for PE 597 (Torpids). What is established, what is dead, what the numbers look like, and where the gap is. Detail behind wikilinks; `research/INDEX.md` lists every source with its URL.

## Model

n boats, starting positions p_j = 40(j−1) (j=1 lowest, downstream), finish line L upstream. Speeds v_j iid Exp(1). Boat j rows at constant v_j until it finishes (when (L−p_j)/v_j elapses) OR bumps the nearest still-rowing boat ahead (then OUT, passed freely; bumped boat keeps rowing and may be re-bumped). New order: i placed above j iff a bump chain i→…→j exists; pairs with no chain keep starting order. p(n,L) = P(new order is an even permutation of starting order). Parity = (# pairs i<j joined by a bump chain) mod 2 = inversion count of the new order. Target: p(13,1800) to 10 dp.

## Established (verified, this run's own)

- **Exact small-n oracle, rational and cross-verified.** The race outcome is piecewise-constant in v, invariant under common scaling; with Exp(1) speeds the normalized vector is uniform on the (n−1)-simplex, so p(n,L) = (n−1)!·(Euclidean volume of even-parity cells). Separators F_j=(L−40j)/v_j (finish) and C_ab=40(b−a)/(v_a−v_b) (catch) give pairwise equalities affine in v → a genuine hyperplane arrangement; parity is constant on open cells (0 inconsistent sign-buckets in 150k samples per config). Implemented exactly in `code/cell_exact.py`+`code/toolkits/arr_enum.py` (+`arr_polytope.py`), cross-checked cell-by-cell by a second independent enumerator `code/arrangement_pn.py`, and by 2–10M-sample MC.

| (n,L) | p(n,L) | basis |
|---|---|---|
| (2,L) | L/(2L−40) closed form | analytic + cell + MC |
| (2,160) | 4/7 | computed |
| (2,400) | 10/19 | computed |
| (2,1800) | 45/89 | computed |
| (3,160) | 56/135 = 0.4148148… | **matches problem example exactly** |
| (3,400) | 542/1377 | computed |
| (3,1800) | 2237/5742 | computed |
| (4,400) | 521/1020 = 0.5107843137… | **matches given 0.5107843137 to 10 dp** |
| (4,1800) | 166802/317985 | computed |

  Extras: 16 more exact p(3,L) (L=120…5000) in `code/out/exact_p3_extra.json`; all re-derived by the second engine + MC. Full table in `code/out/exact_small_n_results.json`.
- **Parity cells are L-independent combinatorially:** n=3 → 32 cells (17 even), n=4 → 1202 (595 even), at every L tested; only volumes depend on L. n=5 → 85 hyperplanes / ~13,750 cells: naive exact vertex solver infeasible → MC only.
- **Bump graph is always a forest** (360k races, n=3,4,5; proved consequences: out-degree ≤ 1, edges strictly index-increasing, no cycles; boat 0 never a target, boat n−1 never bumps; roots are never-bump finishers). Parity = #chain-pairs mod 2. This is the structural reason single-root tree models fail (see below). Details: `structure_report.md` + `code/structure_taxonomy.py`.
- **MC pins p(13,1800) ≈ 0.5002 ± 0.00007** (10M: 0.500380 SE 1.6e-4; 60M pooled: 0.500203 SE 6.5e-5; engine re-checked against both given values). Convergence at L=1800, n=5..8: 0.5320, 0.4870, 0.4916, 0.5058 (SE ~7e-4) — no drift from 0.5. Any true bias ≤ ~3e-4: the 10-dp answer cannot come from MC.

## Refuted — do not rebuild on these (all computed, decisive)

- **w-order hypothesis.** Parity is NOT a function of the rank of w_j = v_j/(L−p_j). Same w-order bucket contains both parities (n=3, L=160: speeds [0.88083,0.60364,0.35634] → odd, [0.72906,0.43938,0.02941] → even). Magnitudes matter. (`verify_hypothesis.py`)
- **Min-heap treap / Cartesian-tree hypothesis.** Tree parity (ancestor pairs of min-w treap) ≠ race parity: fails n=2..6 in the first ~60 trials. Trivial n=2 counterexample: v0<v1, no bump → even, but w0<w1 makes {0,1} treap ancestors → odd. Tree-MC p(3,160)=0.333 vs 0.4148, p(4,400)=0.833 vs 0.5108. (`test_treap.py`)
- **Research-library treap recursion (root = argmin w, p = Σ distance-ratio·p(left)·p(right)·(−1)^cross).** REFUTED on all three levels (`research_recursion_test.py`): (i) value-level exact: p(3,160)=2/3 vs 56/135, p(4,400)=5/6 vs 0.5108 — wrong on the given examples; (ii) per-vector n=2 counterexample [0.89157,0.33049], L=160 (oracle odd, recursion even); (iii) both crux claims fail: decoupling fails 20,177/300,000 and cross=|L||R| fails 152,466/300,000 (holds only ~49%, a coin flip, not a deterministic formula).
  **Root cause:** finish times (L−p_j)/v_j are inverse-exponential, NOT exponential clocks — a bump can be pre-empted by a finish, so left/right subranges do NOT decouple. The library's "exact route" is invalid as stated; an exact method must handle bump-vs-finish chronology over Exp speeds directly (open).

## Sourced library facts that still stand (but do NOT imply the refuted recursion)

- Rate-ratio products for iid/inid Exp clocks; order-statistic spacings of iid Exp(1) are independent Exps with rates n,…,1; memoryless property ([[exponential_order_statistics_memoryless_kth]], [[competing_exponential_clocks_uchicago]], [[inid_exponential_order_statistics_nagaraja]]).
- Relative speed v_j−v_i is Laplace; finish times are inverse-exponential ([[laplace_difference_of_exponentials_libretexts]], [[inverse_exponential_finish_times_wikipedia]]).
- Normalized speeds uniform on the simplex ([[dirichlet_distribution_wikipedia]]); Lasserre closed forms for simplex sections ([[simplex_volume_sections_lasserre]]) — still a valid volume tool if the region is ever enumerated exactly, but its advertised role as "the last step of the recursion" is dead.
- The gap: how the true bump/finish chronology composes across subranges is NOT in the library (claims ledger has no PE597 entry; see below).

## Memory status (checked this cycle)

- `recall_memory` / `relate_memory` / `search_claims` return **no PE597 entries** — durable memory holds only other problems (PE185, PE346). Agents must not expect cross-run memory to answer PE597 questions; this run's durable store is `MEMORY.md` (full record of every refutation + all exact values), with `GOAL.md` (full model restatement + oracle table) and `TASKS.md` (status) beside it. Provisional work lives in `SCRATCHPAD.md`; `recall_scratch` empty.
- Pitfall recorded: uniform-grid sampling v~U(0,1] is NOT the Exp(1) measure and its parity counts converge to 0.5, not to p(n,L) — matching MC to exact values requires true Exp(1) draws.

## Research synthesis of the gap (L2.0 seal + `research/torpids_exact_combinatorics_report.md`)

- A literature survey found **no known polynomial closed recursion** for the finite-finish-line final-order parity — the finish event (inverse-exponential, non-constant hazard) is the entire obstruction, and no standard theory (order statistics, Plackett–Luce, platoon, ballistic aggregation) covers it fully.
- **Pure race (no finish line)** IS classical 1D ballistic aggregation: final bump clusters = segments of the convex minorant of the walk (steps (1,v_j)); cluster-size distribution = cycles of a uniform random permutation (Majumdar–Mallick–Sabhapandit PRE 79 021109, arXiv:0811.0908; convoy leaders = right-to-left record minima, Haghighi-Talab & Wright 1973). This identifies the no-finish object but "local" variant: the convex-minorant block parity does not hand over the finish-line case; it is a warm-up, not the answer.
- **Disagreement (theory vs. run data):** the combinatorics report argues the separating hyperplane set is O(n²) with O(n⁴) arrangement regions, hence "polynomial in principle"; the run's own enumeration shows n=4→1202 cells, n=5→85 hyperplanes/~13,750 cells, i.e. the practical constant explodes and n=13 via naive exact enumeration is dead. Treat the polynomial bound as a ceiling on faces, not a license to enumerate.

## Open

Exact p(13,1800) remains **unsolved**. n≤4 is settled exactly; n=5 exceeds the naive arrangement solver; treap/rank reductions are dead. Required: a reduction whose cost scales with n, not with the arrangement (which grows super-exponentially), handling the bump/finish chronology directly. Never search for published answers/forums (invalidates the run).