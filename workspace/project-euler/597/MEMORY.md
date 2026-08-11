# Working memory

## Problem
Torpids (PE-style). n boats, start positions p_j=40j (j=1 lowest), finish at L.
Speeds v_j ~ Exp(1) iid. Constant speed until finish or bump (catch nearest
ROWING boat ahead, then OUT/transparent; bumped boat continues). New order from
bump chains; parity = sign of permutation from starting ascending listing to
new ascending listing. p(n,L) = P(new order is even permutation). Examples:
p(3,160)=56/135≈0.4148; p(4,400)=0.5107843137. Goal: p(13,1800).

## Established results
- `brute.simulate_order` + `parity_of_new_order` faithfully implement the race
  and now reproduce ALL five rows of the n=3,L=160 table (verified: none even,
  B bumps C odd, A bumps B odd, both-bump-C even, chain odd).
- `brute.parity_of_new_order` had a comparator bug (inverted `above` test) that
  shipped in the original run: it reported identity order for every non-trivial
  bump structure, giving MC 1.000000. FIXED (see Failed approaches).

## Failed approaches / dead ends
- Structural hypothesis H: "final parity is a function of the ranking by
  decreasing w_j = v_j/(L-p_j) only." **REFUTED.** With the corrected parity,
  `verify_hypothesis.py` N=200000 reports w-order buckets containing BOTH
  parities: n=3 L=160 has 1 inconsistent order, n=4 (both L) 9, n=5 L=400 66,
  n=5 L=1800 67.
- Concrete counterexample (n=3, L=160), w-order (0,1,2) in both:
    speeds [0.88083,0.60364,0.35634] -> parity 1
    speeds [0.72906,0.43938,0.02941] -> parity 0
  (membership of a w-order bucket carries no parity info).
- Hence the race outcome depends on speed magnitudes, not just their rank
  order: must solve with the true continuous dynamics (exact integration over
  the Exp speeds), not a permutation-only reduction.

## Open questions
- Correct exact method for p(13,1800). The chronology (bump vs finish inter-
  leaving) means events are not merely pairwise-catch comparisons; need an
  exact/analytic route, likely order-statistics/memoryless exponential
  structure. Not yet attacked.

## Cartesian-tree (min-heap treap) hypothesis: REFUTED
- Conjecture tested in test_treap.py: with priority w_i = v_i/(L-40i), the
  bump-chain pairs should equal the ancestor/descendant pairs of the min-w
  Cartesian tree, giving parity = (# such pairs) mod 2.
- RESULT: fails instantly. n=2..6, L in {160,400,1800}, 20k trials per (n,L):
  30 mismatches after ~62 trials. Tree-MC p(3,160)=0.333 (given 0.4148),
  p(4,400)=0.833 (given 0.5108), p(13,1800)=0.536 — the treap parity is a
  different random variable entirely.
- Trivial n=2 counterexample: v=[0.13269,0.56728], L=160. v0<v1 so boat0 can
  never catch boat1 -> no bump -> even parity (oracle=0, bumps=[]). But w0=0.0008
  < w1=0.0047 so boat0 is the treap root and the pair {0,1} counts as an
  ancestor/descendant pair -> tree predicts odd. The treap's ancestor relation is
  NOT the bumper-chronology reachability: bumping is about the CARETAKER between
  boats (relative speed and distances), a genuinely different structure than
  treap-ancestry by time-to-finish-rate.
- n=3 case oracle=0 tree=1 with bumps [(1,2),(0,2)] (2-root treap): the treap
  counts {0,1,2} triple chains wrongly; race reachability gives only 1->2,0->2
  (2 chain-pairs, even), while the treap with root 2,left-subtree 0->1 claims
  {0,1} is an ancestor pair too -> odd. Treap ancestry over-counts non-adjacent
  index relations that the bump chronology never realizes.
- Takeaway: treap/tree structures built on w_i = speed/distance do NOT encode the
  race parity. The race parity depends on pairwise relative speeds and the
  actual chronological order, not on a single scalar priority ordering.

## Research-library recursion (L1.1/L0.0, CONTEXT.md): REFUTED
The claimed "exact non-exhaustive recursion" — root = argmin W_i=v_i/(L-40i),
p([a,b]) = sum over root of (distance-ratio weight)·p(left)·p(right)·(-1)^cross,
parity propagates as parity(left)·parity(right)·(−1)^cross — is WRONG. Tested
decisively in research_recursion_test.py (all three parts):
1. VALUE-LEVEL (exact Fractions): the closed-form with cross=|L||R| gives
   p(3,160)=2/3 (truth 4/15+4/27=56/135≈0.4148) and p(4,400)=5/6
   (truth 0.5107843137). Wrong in the very given examples. (The recursion value
   is L-independent: it equals the uniform-treap value ~2/3 or 5/6 regardless
   of L, whereas the truth depends heavily on L.) cross=0 gives p=1 always.
2. PER-VECTOR: smallest counterexample n=2, L=160, speeds=[0.89157,0.33049]:
   oracle parity=1 (odd; boat0 bumps boat1 since v0>v1 and catches at 71.3 m
   before the 160 m finish), recursion (root=argmin W, cross=|L||R|) says 0.
   A full n=3 example speeds=[0.63879,0.16263,0.10432] also mismatches (11).
3. CRUX CLAIMS (the recursion requires both):
   C1  DECOUPLING: sub-race parity on slice [0..r-1] == restriction parity of
       the full permutation -> FAILS (20177/300000), even with the LEFT slice.
   C2  cross = |left|*|right| -> FAILS (152466/300000). cross is NOT a
       deterministic |L||R| flip.
   Root cause: the finish events are inverse-exponential (non-constant hazard),
   not exponential clocks, so a bump can be pre-empted by a finish; the
   left/right subranges do NOT decouple and the treap cross value is wrong.
   Also n=2 value-level fails: recursion says p(2,L)=1.0 for all L, truth is
   p(2,160)≈0.571, p(2,400)≈0.526, p(2,1800)≈0.505 (MC). This is the cleanest
   single refutation: the recursion misses that a 2-boat race is not always a
   bump (the slower/equal-speed finish case keeps identity order).
   => The library's closed-form route is NOT valid. An exact route must handle
   the bump-vs-finish chronology over the Exp speeds directly (open).

## Oralce edge-loss bug: FOUND and FIXED (see scratchpad)
- `brute.simulate_order` recorded only the LAST bumper of each boat
  (`bumped_by[k]=j`) and rebuilt `above` by following that single `out_of`
  chain. A bumped boat keeps rowing and can be bumped again; the earlier edge
  was silently dropped, so `above` lost transitive-chain edges in ~40% of
  random cases (against a full-reachability reference).
- IMPACT: the lost edges never changed the reconstructed total order or parity
  in 2M random trials (order_diff=0, par_diff=0), because every lost
  intermediate edge had a direct replacement, and the inversion count was
  preserved. So the probability measure was UNCHANGED by the bug — but the
  data structure was wrong-by-construction. Fixed brute.py to record every
  bump edge and compute `above` by full graph reachability.
- After the fix, `brute.simulate_order` is byte-identical to
  `simulate_order_nobug` (full reachability) on 500k random trials, and the
  worked-example values are reproduced: MC p(3,160)~0.415, MC p(4,400)~0.512.
- Correct parity identity confirmed: parity = (# pairs i<j with a bump chain
  i -> ... -> j) mod 2, i.e. the inversion count of the permutation. 1M-trial
  check vs full reachability: 0 mismatches.

## Ballpark target (MC, n=13, L=1800, fixed engine)
- p(13,1800) ~ 0.500 (100k: 0.500470; 200k: 0.499400; 300k: 0.499027;
  1.2M: 0.500880). Expect the exact answer near 0.500, consistent with the
  parity being asymptotically a fair coin as n grows.

## Exact p(3,L) arrangement validation table (all cross-verified)
- Anchor values (first 12, from exact_p3_data.py) were re-derived exactly by
  code/exact_p3_extra.py via the arrangement enumeration and all matched:
  160→56/135, 240→2/5, 320→36/91, 400→542/1377, 480→272/693, 640→1532/3915,
  800→824/2109, 1000→1981/5076, 1200→1934/4959, 1400→444/1139,
  1600→10532/27027, 1800→2237/5742 (all 32 cells).
- Extra L values computed exactly (ncells listed), saved to
  code/out/exact_p3_extra.json:
  L=120: 4/9 (27 cells), L=200: 17/42 (32), L=280: 118/297 (32),
  L=360: 71/180 (32), L=440: 112/285 (32), L=520: 487/1242 (32),
  L=560: 382/975 (32), L=720: 658/1683 (32), L=900: 4231/10836 (32),
  L=1100: 6451/16536 (32), L=1400: 444/1139 (32, = anchor),
  L=2000: 5554/14259 (32), L=2400: 896/2301 (32), L=3000: 6352/16317 (32),
  L=4000: 68312/175527 (32), L=5000: 5959/15314 (32).
- Verification: every one of the 16 extras independently reproduced by the
  second enumerator (toolkits/arr_enum + p_cell_exact.py); MC 400k at
  L=120/900/5000 within 1 SE (0.4439 vs 4/9=0.4444, 0.3906 vs 4231/10836,
  0.3897 vs 5959/15314). The n=3 arrangement method is a validated oracle.

## Sanity checks (2024 result)
- Fixed a latent Python bug in `exact_race.simulate_order_exact`: candidates
  were compared as tuples (`c < best[0]`) which threw `TypeError` for Fraction
  times. Corrected to compare `c[0] < best[0]`.
- `check_counterexample.py` (grid v_j=k/M uniform, M=8,16,32,64) validates the
  counterexample pair and the parity engine's internal consistency:
      ce1 [0.88083,0.60364,0.35634] -> parity 1 (float and exact agree)
      ce2 [0.72906,0.43938,0.02941] -> parity 0 (float and exact agree)
    i.e. opposite parities in the same w-order bucket, as expected.
- The grid even-count itself does NOT converge to 56/135 (it goes to 0.5):
      M=8  even=258/512 =0.5039
      M=16 even=2060/4096=0.5029
      M=32 even=16408/32768=0.5007
      M=64 even=131184/262144=0.500427
  This is a SAMPLING-MEASURE artifact, not a parity bug: the uniform grid
  v~U(0,1] is not the Exp(1) measure of the true model. Proper Exp(1) MC
  (verify_hypothesis.py N=200000) gives p(3,160)=0.415145 against exact
  56/135=0.414815, confirming the parity engine is correct and the grid
  premise in the check script was wrong.

## High-precision MC (high_precision_mc.py, parallel, exact binomial SE)
- Engine sanity re-check: p(3,160)=0.414045 (SE~0.0008, exact 56/135=0.414815),
  p(4,400)=0.5122225 (SE~0.0008, given 0.510784). Both agree with the given
  values within MC error -> engine is the right target.
- p(13,1800): N=10M even=5003798 p=0.500380 SE=0.000158
              N=60M even=30012151 p=0.500203 SE=0.000065  (60M pooled, ~333s, 28 procs)
  i.e. p(13,1800) is 0.5002 +/- 0.00007: indistinguishable from 0.5 up to the
  ~60M-sample resolution; any true bias is <= ~0.0003 in magnitude.
- Convergence toward 0.5 with n (L=1800), a few hundred k samples each:
    n=5 p=0.531964 SE=0.000706
    n=6 p=0.486980 SE=0.000707
    n=7 p=0.491648 SE=0.000707
    n=8 p=0.505779 SE=0.000559
  (values cluster near 0.5 with no growing or monotone deviation; SE ~0.0007)
- Bottom line: high-precision MC pins p(13,1800) extremely close to 0.5
  (0.5002 +/- 0.00007). Final 10-dp answer needs the exact method, not MC,
  since distinguishing a tiny true bias from exactly 0.5 would need >100M
  samples.

## EXACT small-n oracle (cell_exact.py / toolkits/arr_enum.py) — RESULT

Deliverable from the tool-builder exact-integration task. The race outcome is
a deterministic piecewise-constant function of the speed vector, invariant
under common scaling; with Exp(1) speeds the normalized vector is uniform on
the (n-1)-simplex (Dirichlet(1,..,1)), so p(n,L) = (n-1)!(Euclidean volume of
even-parity cells). The outcome's separating set is a genuine straight-line
hyperplane arrangement on the simplex (candidate event times are
const/(linear): F_j=(L-40j)/v_j and C_ab=40(b-a)/(v_a-v_b), so pairwise
time-equalities — and v_a=v_b — are affine). Parity is constant on open cells
(verified: 0 inconsistent sign-buckets per 150k samples, every (n,L)).

### Exact values (rational), verified by two independent routes + MC
| (n,L) | p(n,L) exact | float |
|---|---|---|
| (2,160) | 4/7 | 0.5714285714 |
| (2,400) | 10/19 | 0.5263157895 |
| (2,1800) | 45/89 | 0.5056179775 |
| (3,160) | 56/135 | 0.4148148148 |
| (3,400) | 542/1377 | 0.3936092956 |
| (3,1800) | 2237/5742 | 0.3895855103 |
| (4,400) | 521/1020 | 0.5107843137 |
| (4,1800) | 166802/317985 | 0.5245593346 |

p(2,L) closed form: boat0 bumps boat1 iff v1/v0 < (L-40)/L, so
P(bump)=(L-40)/(2L-40), p(2,L)=P(no bump)=L/(2L-40). Matches cell enumeration
and MC. (My first analytic attempt gave P(bump); p is the complement.)

### Anchor verification
- p(3,160) = 56/135 EXACT — matches the problem's worked example precisely
  (2*(28/135) with Dirichlet density 2).
- p(4,400) = 521/1020 = 0.5107843137254902 — the problem's given value
  0.5107843137 to all 10 dp. Matched exactly.
- Cross-checked against the independent solver arrangement_pn.py and its data
  tables (exact_p3_data.py, exact_p4_data.py): identical rationals at every
  shared L (3:160,240,320,400,480,640,800,1000,1200,1400,1600,1800;
  4:160,240,320,400,800,1000,1200,1400,1600,1800).
- MC at 2-10M samples per config: all within 1-3 SE of the exact values.

### Parity-cell counts (arrangement tractability)
| n | cells | even | odd |
|---|---|---|---|
| 2 | 3 | 2 | 1 |
| 3 | 32 | 17 | 15 |
| 4 | 1202 | 595 | 607 |

The cell count is L-INDEPENDENT for n=3 (32) and n=4 (1202) at every L
tested (160..5000); only the cell shapes/volumes depend on L. This means the
combinatorial complexity is fixed per n by the arrangement's combinatorial
type, and L only moves the parity of a fixed set of cells.

### n=5 status
The n=5 arrangement has 85 hyperplanes in the 4-simplex; sampling found
13,750 distinct nonempty cells in 200k draws. A full exact sum with the naive
per-cell vertex solver is not tractable in reasonable time (each leaf needs
an O(choose(m,4)) Fraction vertex solve; m grows with cuts). Delivered as MC:
p(5,1800) = 0.53273 +/- 0.00029 (3M samples). See TASKS for the arrangement
speedup (vertex caching, plane pruning, incremental cutting) left as open work.

### n=5,6,13 MC comparison (brute engine, for context)
p(4,1800) 0.5246, p(5,1800) 0.5327, p(6,1800) ~0.487 (earlier), p(13,1800)
~0.5002 = target. Small-n exact values are the testbed, not the deliverable.

## Structural taxonomy (structure_taxonomy.py -> structure_report.md)
Verified examples + bump-graph taxonomy over 60k MC trials per (n,L), n=3,4,5,
L in {160,1800} (360k total races), using the reference brute engine:
- n=3,L=160 five-row table: all parities reproduced; exact rational sums
  all-five=1 (partition) and even-rows=56/135 = p(3,160). MC p(4,400)=0.5115
  +/- 0.0008 (given 0.510784).
- CENTRAL: the bump directed graph is ALWAYS a FOREST — every boat out-deg <= 1,
  every edge strictly index-increasing, zero cycles, across all 360k trials.
  Deterministic consequences (proved): boat 0 is never a target, boat n-1 never
  bumps (confirmed P=0 over 100k trials); components are in-arborescences
  rooted at never-bump finishers; max chain length reaches n-1 (0->1->...->n-1).
- In-degree is unbounded: a bumped boat keeps rowing and can be re-bumped by
  several lower boats; targets concentrate on the highest boats (boat n-1
  bumped prob ~0.45-0.49).
- Chains/roots are NOT consecutive: the set of boats bumping a target need not
  be a consecutive lower block; above[] can skip intermediate boats (a boat
  passes boats already OUT). Bumper-set non-consecutive ~1-3% at n=5/6.
- Distinct edge structures reached grow with n: 5 (n=3), 14 (n=4), 14-42 (n=5);
  edge-set and above-reachability representations agree in count (bijective on
  observed data).
- Multiple disjoint forest components per race (independent index intervals),
  parity = product of component parities = #chain-pairs mod 2. This is the
  structural reason single-scalar treap hypotheses fail: bumping is a
  chronological forest-of-chains process, not a one-root Cartesian tree.
