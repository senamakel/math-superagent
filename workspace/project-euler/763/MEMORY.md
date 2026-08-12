# Working memory

## Problem
3D amoeba. Amoeba at (x,y,z) divides into three amoebas at (x+1,y,z),
(x,y+1,z),(x,y,z+1) iff those three cubes are all empty; parent disappears.
Start: one amoeba at (0,0,0). After N divisions there are 2N+1 amoebas.
D(N) = number of distinct reachable sets of occupied cubes after exactly N
divisions, counted once even if reachable multiple ways.

## Established results (two independent BFS routes)
D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063.
D(14)=5949063 verified by THREE independent implementations. D(2)=3, D(10)=44499
match the statement's worked examples. Hard ceiling: 2 GiB cgroup cap, exact BFS
stops at N=14 (~5.9M states); D(15) unreachable by any exact BFS here.

## Claim verification sweep (this run: full computable range)

Re-ran check_recurrence.py (N<=7), definitive_check.py (N0..12), and two new
lean bitmask probes (check_a1a2_bitmask.py -> N=14, check_a12_lean_large.py ->
N=13) to settle the top-cap structural claims over the WHOLE computable range.

- A1 (max level holds EXACTLY 3 cells): HOLDS for every reachable config,
  N=1..14 (A1bad=0 at every N).
- A2_tri (those 3 = {p+e1,p+e2,p+e3} of a single parent p at M-1): HOLDS,
  N=1..14 (A2tri_bad=0 at every N).  Verified directly on the 5.9M-config
  N=14 frontier.
- A2_empty (that parent p is absent from the config): FAILS from N=4.
  A2empty_bad = 3,9,39,126,453,1521,5241,17766,60630,206010,701262 for
  N=4..14.  The empty-parent triangle requirement is too strong: the top-3 IS
  a full child-triangle, but the parent cell is sometimes re-occupied.
- A3 (deterministic empty-parent cap-collapse to origin in N steps): FAILS
  from N=5 (3,18,93,405,1668,6525,24816,92214,337272 bad for N=5..12).  Only
  checked to N=12 (the per-config iterative collapse is too heavy on the
  N=13/14 frontier for the 600 s budget).
- B (D(N+1) == sum_C f(C), f=#dividable cells): FAILS from N=3.  The forward
  map (C,p)->child is NOT injective (diagnose_B finds collisions), so summing
  f over all configs overcounts distinct children.  sum_f vs D(N+1): N=3
  33 vs 30, N=4 126 vs 99, N=5 483 vs 336, N=6 1836 vs 1134, N=7 6924 vs 3855,
  N=8 25875 vs 13086, N=9 95994 vs 44499, N=10 353691 vs 151263, N=11 1295751
  vs 514419, N=12 4722687 vs 1749267, N=13 17137029 vs 5949063.

NET: A1 and A2_tri (top-3 is always the full child-triangle of ONE parent,
equivalently the same-if-stronger "every top triad has a unique parent") hold
over the whole computable range; the REFINED collapse/pivot must allow a
PRESENT parent, not require an empty one.  The determinism that makes
"configs <-> reverse-collapse sequences <-> ternary trees" a bijection is the
weak spot: B's collision count shows distinct children are produced from
multiple (C,p).  This is the seam a two-index voidance/folded-polyominoid DP
(2D G(k,m) lift) must repair; a plain D(N+1)=sum f(C) step is refuted.

## Sourced structural backbone (Eriksson "Pebblings", EJC 2 (1995) #R7)
- The 3D PE763 amoeba is exactly Eriksson/Vaderlind's n=3 pebbling game
  (a cell -> 3 children one unit out along +e1,+e2,+e3, all targets empty).
- **n>=3**: there is a bijection between reachable positions, voidance sets,
  and folded polyominoids (Eriksson Thm 9), and **no node is ever played
  twice** (Prop 24), so positions = voidance sets = folded polyominoids.
- 2D analogue = chessboard pebbling (CGMO AMM 102 (1995)) = OEIS A007902,
  governed by the two-index DP G(k,m); no small one-index closed form.

## Inventor's NEW structural observation (the collapse lever)

**Top-cap structure (hand-verified on config dumps, to be confirmed by
code/inventor/check_recurrence.py):**
- CLAIM A1: every reachable N-config (N>=1) has EXACTLY 3 cells on its max
  level M (all level histograms end in "3": "0 2 3", "0 2 2 3", "0 1 5 3", ...).
- CLAIM A2: those 3 top cells are the complete forward-child triangle
  {p+e1,p+e2,p+e3} of a single EMPTY parent p at level M-1.
- CLAIM A3: cap-merging (replace those 3 by p) gives a reachable (N-1)
  config; repeating reaches {origin} DETERMINISTICALLY.
Consequence: configs <-> reverse-collapse sequences <-> full ternary
collapse trees <-> voidance sets (Eriksson Prop 20/Thm 9).

**Consequence recurrence (CLAIM B):** f(C) = #{cells p in C none of whose
p+ei is in C} (dividable cells).  Then
        D(N+1) = sum_{C in conf(N)} f(C)
provided the map (C,p) -> child config is injective (which CLAIM A3 gives).
This is the forward DP step; it reproduces D exactly if the collapse bijection
holds.  Verified only by hand on small configs so far; see check script.

## The gap to D(10000)
CLAIM B's sum still ranges over all reachable configs (enumerates the space),
so it does NOT by itself reach N=10000.  The real reduction must come from the
**voidance-set / folded-polyominoid** counting (Eriksson Thm 9): count, for
each N, the voidance sets of the collapse that produce an N-division config.
Eriksson Fig.3 column n=3 gives folded-polyominoid counts f(k,3)=
1,3,12,57,300,1680,9900,... (k=0..6) but D(N) is NOT f(k,3); the PE763 "position
with 2N+1 cells" count is a refinement (level/weight constraints).  Proposing
a two-index DP (3D analogue of the 2D G(k,m)) as the concrete next target;
falsifier: must reproduce D(14) and then D(20)=9204559704, D(100) last
nine=780166455.  NOT yet derived; this is the open seam.

## NEW NEGATIVE (this run): P-recursive extrapolation is dead

Benchmarked lib.holonomic.fit over every (m=1..5, d=1..3) and K=11..14, exact
rational arithmetic, and checked whether ANY nullspace solution reproduces ALL
held-out points D(K..14) (scratchpad/holonomic_probe.py ->
scratchpad/holonomic_probe.txt).  RESULT: ZERO recurrences out of the whole
sweep reproduce every held-out point.  Each fitted recurrence (e.g. extrapolating
from K=14 does hit D(13)=1749267 trivially since it is in-sample) breaks on the
very next out-of-sample term.  These are overfits: any finite initial window of
an arbitrary sequence admits a P-recursive interpolation of high enough order,
so a low-order fit that matches D(0..13) or D(0..14) carries no predictive
power.  Conclusion recorded: D(N) is NOT P-recursive of low order on the
observed window, and no recurrence fit here is a viable route to D(10000).
Do NOT re-run this search.

## NEW FINDINGS (this run, pattern-finder)

### CORRECTION — the Q_k max-level decomposition does NOT equal D(N) for even N
Prior notes claimed "D(N)=sum_k Q_k(N)3^(N-2k-1) reproduces D(N) exactly
N=2..10 (and holds)." That is INCOMPLETE: it holds only for odd N (and N<=11).
At N=12 it misses 30 configs, at N=14 it misses 267
(code/pattern/qdecomp_falsify.py). Cause: for even N, the column with max level
M=N/2 (offset k=N/2, exponent 2M-N-1 = -1) is excluded by the e>=0 gate, yet
such configs exist (R(12,6)=30, R(14,7)=267). The per-column Q_k polynomial
closed forms remain exact for M>(N+1)/2 (verified OOS at N=13,14 for those
columns); only the summed-IDENTITY reading is false. First falsifier of the sum
formula: N=12, NOT N=15 as previously guessed. The diagonal R(N,N)=3^(N-1)
(confirmed all N=2..14) is unaffected.

### NEW SOURCED MATCH — histogram-count H(N) == OEIS A186085 (sandpiles)
The count H(N) of DISTINCT level-histograms over reachable N-configs,
N=2..14 = 1,1,2,3,5,8,13,22,36,60,100,166,277, equals OEIS A186085
("number of 1D sandpiles with n grains" = smooth compositions with first/last
part 1, |consecutive Δ|<=1) exactly (oeis_lookup + verify program
code/pattern/check_a186085_recurrence.py). H(N)≠D(N) — H counts histogram
shapes, D counts configurations — but it identifies the "shape space" of the
3D amoeba as the smooth-composition family. Strongest new structural lead;
deriving how many configs realize each histogram is the open refinement.

### OVERFIT CONFIRMED AGAIN
find_linear_recurrence returned an order-6 const-coeff recurrence fitting H(2..14)
perfectly, but it diverges from published A186085 at n=6. Direct proof that a
finite-window recurrence fit is not predictive even when it fits exactly.

## Files
- code/inventor/check_recurrence.py — tool_builder target verifying CLAIM A
  (top-cap deterministic collapse) and CLAIM B (D(N+1)=sum f(C)) on BFS
  configs N<=7.
- code/brute.py — this run's pure naive frozenset BFS oracle for PE763
  (level-by-level via lib.amoeba.forward_level, prints D(N)/elapsed/frontier
  each level, stops at a frontier cap of 1,000,000 or 500s). Output in
  code/out/brute_fs_oracle_run.txt.

## Naive frozenset oracle run (this tool-builder task)

Ran the pure exact BFS (code/brute.py) to pin down the definition against the
statement's examples and report how far naive BFS reaches in THIS container:
- D(2)=3 and D(10)=44499 both asserted in-run and matched (same oracle gold
  values as the whole run's D(0..14)).
- Exhaustive frozenset BFS reaches D(0..13)=
  1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267; all fourteen
  values match the reference list exactly. Run then stops gracefully (cap
  reason: frontier 1,749,267 > 1,000,000 at level 13, elapsed 223 s, peak RSS
  2139 MB).
- The OOM ceiling: the frozenset oracle cannot even build the D(14) frontier
  (5,949,063 configs) here — a single forward step that big exceeds the 2 GiB
  cgroup memory.max (killed with exit 137 when the cap was left at 5e6; the
  fix is to cap the CURRENT level, i.e. stop before the huge step).  D(14) is
  reachable only via the compact bitmask oracle (code/amoeba/bfs_more.py ->
  d_values_more.txt), which is NOT this brute.py.
- Task (3) confirmed: D(20)=9204559704 is unreachable by exact BFS.  Level
  20 holds ~9.2e9 distinct configs (state space ~9.2e9); at ~0.5-1 KB per
  frozenset that is ~5-9 TB of RAM, and the 5.9M-config N=14 frontier (the
  nearest one strictly less than that) already needs ~4-6 GB here.  Far past
  any feasible time (exponential) or memory budget in this container.
- code/inventor/probe_topcap.py, probe_reachable.py — empirical probes.
- code/pattern/check_a186085_recurrence.py, qdecomp_falsify.py, mdist2.py,
  full_triangle_dump.py, pn_poly.py — this run's pattern-finder probes
  (A186085 histogram match; even-N Q-decomposition falsification).
