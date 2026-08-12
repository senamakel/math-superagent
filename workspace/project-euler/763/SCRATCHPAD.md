# Scratchpad

## Extension run (tool-builder)

BFS over distinct configs, fixed-width int bitmask encoding, one level per
step. 28 cores / 30GB available.

Level times (s), bitmask oracle (amoeba_extend.py):
1:0.00 2:0.00 3:0.00 4:0.00 5:0.00 6:0.00 7:0.002 8:0.007 9:0.03 10:0.11
11:0.43 12:1.7 13:6.4 14:26.0

Independent route (amoeba_verify.py) level 14: 37.84s. Both give D(14)=5949063.

Frozenset oracle (brute_extended.py) OOM-killed (exit 137) at N=13->14 step
when frontier reached 5.9M frozensets — expected; D(14) obtained via bitmask.

N=15, N=16 NOT reached: projected frontiers ~20M, ~68M >> 5,000,000 cap and
> 30GB RAM. Run stopped cleanly when level-14 frontier (5,949,063) exceeded the
cap.

Earlier D(N) values: D(0..12) reproduced by both frozenset and bitmask; D(13)
by both frozenset (~200s, MEMORY) and bitmask (6.4s).

## Pattern-finder (this run)

### NEW SOURCED MATCH: histogram-count sequence == OEIS A186085
The sequence of DISTINCT level-histogram counts H(N), N=2..14 =
  1,1,2,3,5,8,13,22,36,60,100,166,277
is EXACTLY OEIS A186085 ("number of 1-dimensional sandpiles with n grains" =
smooth compositions with first/last part 1, |Δparts|<=1).
- oeis_lookup matched it (research/L1.1/oeis_a186085.md).
- Verified H(N)==A186085(N) for N=2..14 against the published table exactly
  (code/pattern/check_a186085_recurrence.py).
- Interpretation: each reachable 3D config's level-histogram (count of cells
  on each level) corresponds bijectively to a smooth composition — the count
  of distinct histograms alone is NOT D(N), but the refinement D(N)=
  sum_histogram (#configs sharing that histogram) is the object; A186085
  counts the histograms, not the weighted D(N). Recorded as a real structural
  link worth deriving.

### OVERFIT CAUTION (reproduced): fitted recurrences on small windows are junk
find_linear_recurrence returned an order-6 constant-coeff recurrence for H,
a(n)=a(n-1)+a(n-2)+a(n-3)-a(n-4)-a(n-6), matching H(2..14) exactly — but it
DIVERGES from published A186085 at n=6 (rec=4 vs 5). Direct confirmation that
a recurrence fit over a finite window carries no predictive power even when it
fits perfectly. Matches the recorded holonomic-negative conclusion. Do NOT
trust any finitely-fitted recurrence to reach D(10000).

### NEGATIVE: Q_k max-level decomposition is INCOMPLETE at even N
The repeated claim "D(N)=sum_k Q_k(N)3^(N-2k-1) reproduces D(N)"
holds only for ODD N (and N<=11). At N=12 it misses 30 configs, at N=14 it
misses 267 (code/pattern/qdecomp_falsify.py). Cause: for even N the column
with max level M=N/2 (offset k=N/2, exponent 2M-N-1 = -1) is excluded by the
"only e>=0" gate, yet those configs exist. The missing count exactly equals
R(N,N/2) for even N (30=R(12,6), 267=R(14,7)). So the Q-column closed forms
are real for the M>(N+1)/2 region, but the summed formula does NOT equal D(N)
as a full identity. First falsified at N=12, not N=15 as previously guessed.

### Confirmations (no change)
- Diagonal R(N,N)=3^(N-1) exact for all N=2..14 (re-verified).
- H(N) growth ~ x1.67/step (A186085's actual growth), distinct from D(N) ~ x3.4.

## This tool-builder task's runs

### Pure naive frozenset BFS oracle (definition check + capacity report)
Program code/brute.py, naive level-by-level frozenset BFS via
lib.amoeba.forward_level, one step per division, stopping when the CURRENT
frontier exceeds 1,000,000 configs (or 500s).
  D(2) = 3        match
  D(10) = 44499   match
  D(0..13) = 1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267
    (all 14 match the reference list; stopped at D(13): frontier 1,749,267 >
    cap, 223 s, peak RSS 2139 MB).
Capacity ceiling in this container: the naive frozenset oracle OOMs (exit 137)
while building the D(14) frontier (~5.9M configs > 2 GiB cgroup cap).  It is
cleanest run with the cap on the current level so it stops BEFORE the huge
step.  D(20)=9204559704 is unreachable by exact BFS: ~9.2e9 configs at level
20 ~ 5-9 TB of RAM, exponentially past this box.  Output:
code/out/brute_fs_oracle_run.txt.

### Oracle re-run (definition check, matches worked examples)
Ran the existing naive oracle `code/brute.py` (canonical `D` from lib/amoeba,
naive frozenset BFS over distinct occupied-cube sets, d=3) at the two sizes
the oracle can reach among the statement's examples:
    D(2) = 3        matches D(2)=3
    D(10) = 44499   matches D(10)=44499
Command: `timeout 60 python code/brute.py` (exit 0, ran in seconds).
D(20)=9204559704 and D(100) last-nine=780166455 are exponentially out of the
naive oracle's reach (state space ~9.2e9), so per the task's instruction the
oracle was not pointed at them — they are definition checks the oracle's job
is not to reach. Reading of the definition is confirmed by both examples.

### Holonomic extrapolation probe (negative)
scratchpad/holonomic_probe.py -> scratchpad/holonomic_probe.txt.  Confirmed
D(2)=3, D(10)=44499 via lib.amoeba.D.  Swept lib.holonomic.fit over
(m=1..5, d=1..3) x (K=11..14), exact rational, checking whether ANY nullspace
solution reproduces ALL held-out points D(K..14).  Result: no recurrence passes;
every fit overfits and breaks on the first out-of-sample term.  P-recursive
extrapolation cannot reach D(10000) — do not re-search.

- Dumped actual configs for N=3 (9 states) and N=4 (30 states), sorted, to
  code/out/configs_n3_n4.txt and stdout (code/amoeba/configs_n3_n4.py); counts
  asserted against D(3)=9, D(4)=30.
- Compact per-level bit encoding (code/amoeba/bfs_more.py, W=level+1) reproduced
  D(0..14) and independently confirmed D(14)=5949063, writing fresh complete
  code/out/d_values_more.txt.
- D(15) is unreachable here: cgroup memory cap is 2 GiB
  (/sys/fs/cgroup/memory.max = 2147483648); the ~5.9M frontier at N=14 nearly
  saturates it, and D(15) ~20M states would need ~12 GiB. The host has 30 GB
  free but the cgroup caps the container, not the host.
- Also removed the stray root brute.py (superseded; replica at code/brute_capped.py).

## Pattern-finder re-verification (this run)

Re-derived the max-level decomposition fresh from data/level_N.txt + 
code/out/mhist_13_14.txt (N=13,14 are OOS, never fit on). All confirmed:

- Diagonal M=N: R(N,N)=3^(N-1) EXACTLY for all N=2..14.
- Q_k(N)=R(N,N-k)/3^(N-2k-1), degree-k poly in N: leading coeff == 1/k!
  confirmed for k=0..4 (k=5 has too few points to fix full degree).
- Closed forms exact over all computed points:
  Q_0=1, Q_1=n-3, Q_2=(n-5)(n+2)/2, Q_3=(n^3-73n+168)/6,
  Q_4=n^4/24+n^3/4-205n^2/24+97n/4+27.
- Then D(N)=sum_{k=0}^{N-2} Q_k(N) 3^(N-2k-1).

NEW NEGATIVE (this run): NO short local transfer recurrence on the R(N,M)
max-level array. Did rank-safe exact rational least-squares over
R(N,M)=sum c_j R(N-j,M+d) for windows (L=1..3, d in various sets incl
[-1,0,1],[-2..2]); trained on N=3..13, tested OOS on N=14. Every candidate
fails: train residuals 119..55103, OOS residuals 823..402630, never exact.
So the 3D analog of the 2D G(k,m) two-index kernel recurrence does NOT exist
in local form. Recorded dead end: do not re-search this.

Growth ratio settled at ~3.4009 as N->14. D(0..14) reconfirmed NOT in OEIS
(oeis_lookup miss again). Prior results (order-7 constant-coeff recurrence =
overfit; NOT holonomic; D2d == A007902 sourced) stand unchanged.

Files: code/pattern/q_decomp_verify.py, q_bivariate.py, transfer_hunt.py,
transfer_search.py, transfer_search2.py (all exploratory; negative transfer
result is the durable finding).

## Naive-oracle confirmation (this tool-builder task)

Run `code/brute.py` (canonical `D` from lib/amoeba, naive frozenset BFS, d=3)
at N=2 and N=10:
    D(2) = 3
    D(10) = 44499
Both match the statement's worked examples. D(20)=9204559704 and the D(100)
last-nine example are out of reach for the naive oracle (state space ~9.2e9 /
exponential), so by instruction they were not attempted — the oracle's job is
to pin down the definition, which the two reachable examples do. Root
code/brute.py and code/amoeba/brute.py are now identical except a trailing
blank line and both import the same canonical D.

## C1 conjecture test (origin-connected == reachable?)

Program code/test_c1.py.  C1 FALSE in 2D and 3D.  Origin-connected sets are
positive directed animals; counts by size match A005773 in 2D
(1,2,5,13,35,96,267,750,2123,6046,17303,49721,143365), not the amoeba D_2D.
3D counts 1,3,12,52,237,1113,5339,26011,128247,638346 — always above D(N).
m=11 in 3D (~6.4M sets) OOM-killed in this container (2 GiB cap).  Generator
verified by subset oracle (verify_c1_subsets.py).  Details in
code/out/c1_test_results.md.

## Naive-oracle confirmation (this tool-builder task)

Run `code/brute.py` (canonical `D` from lib/amoeba, naive frozenset BFS, d=3)
at N=2 and N=10:
    D(2) = 3
    D(10) = 44499
Both match the statement's worked examples. D(20)=9204559704 and the D(100)
last-nine example are out of reach for the naive oracle (state space ~9.2e9 /
exponential), so by instruction they were not attempted — the oracle's job is
to pin down the definition, which the two reachable examples do. Root
code/brute.py and code/amoeba/brute.py are now identical except a trailing
blank line and both import the same canonical D.

## NEW (this run): EXACT closed form for the histogram-refinement of D(N)

The open refinement question — "how many configurations realize each distinct
level-histogram" — is now answered EXACTLY over the whole computable range.

For a reachable config's level-histogram h = (a_0=0, a_1, ..., a_M=3) counting
cells per level k=x+y+z (M = max level), let n_k = #{interior levels with
exactly k cells}.  Then the number of configs realizing h is

    mult(h) = 2^(2 n_4) * 3^(n_1 + n_2 + n_3 - 1)        if no level has 6 cells
           = 10 * 2^(2 n_4) * 3^(n_1 + n_2 + n_3 - 2)    if some level has 6 cells

Verified EXACTLY on all 694 histograms, in-sample N=2..12 (data dumps) AND
out-of-sample N=13,14 (computed fresh via bitmask BFS, D(13)=1749267,
D(14)=5949063, 443 histograms): zero exceptions.
- code/pattern/final_mult_verify.py (rule), oos_mult_closedform2.py (OOS),
  verify_mult_closedform.py, check_4power.py, mult_structure.py, scan_6_7.py.
- Fresh N=13,14 mult data: code/out/per_hist_mult_13_14.txt.

Consequences:
- D(N) = sum over smooth compositions (OEIS A186085) of the above weight.
  This answers the inventor's open "count configs per histogram" refinement:
  the multiplicity is a closed product depending only on the multiset of the
  histogram's interior level-counts (not their arrangement), times 3^(n1+n2+n3-1).
- The 2-power ties to n_4 (levels with 4 cells): a level with 4 cells forces
  2^(2)=4 configs per...; multiplicities are 3-smooth (2^a·3^b) EXCEPT the
  single family containing a 6-level together with a 7-level, where a factor
  of 10 appears: 30 (N=12), 90 (N=13), 120/270 (N=14). All other 8
  six-containing histograms have a 7 but NO 6 immediately preceding... actually
  the 6-level ALWAYS immediately precedes the 7-level (substring "6 7"), so
  the no-six rule misses them only when a 6-level is present. Characterized:
  first exception at the "0 1 3 6 7 5 3" histogram (N=12), pred 9 vs 30.
- NOTE this still does NOT reach D(10000): the number of histograms H(N)=A186085
  grows ~x1.67^N (huge at N=10000), so the weighted-sum still enumerates an
  enormous space. But it collapses the configuration refinement to a closed
  product, which is the piece the 2D-G(k,m)-style DP would need.

## Pattern-finder (PE763) — max-level decomposition, OOS strength

Fresh sympy-exact re-confirmation (code/pattern/q_columns_fresh.py,
q_fresh_verify.py) rebuilt the full Q_k table from data + mhist_13_14.txt:
- Q_k(N) = R(N,N-k)/3^(N-2k-1) is EXACTLY a degree-k polynomial for k=0..4,
  now checked with N=13,14 as out-of-sample (finite differences vanish at
  level k).
- Leading coefficient of Q_k == 1/k! for k=0..4 (k=1:1, k=2:1/2, k=3:1/6,
  k=4:1/24).
- Q_2 column == OEIS A055999 (n(n+7)/2) sourcing the Q_2=(N-5)(N+2)/2 closed
  form. Q_3,Q_4,Q_5 columns not in OEIS (misses recorded).
- D(N)=sum_k Q_k(N)3^(N-2k-1) reproduces D(N) exactly N=2..10; k>=5 columns
  contribute from N=11. First falsifier for k>=5: N=15 (unreachable by BFS).

## Organizer pass (this run)

Reconciled every folder's INDEX.md with what is on disk after the writing run:
- Described previously-undescribed files in code/inventor (check_eriksson_fig3,
  _run_all, _run_fig3, probe_failures, probe_live, probe_a2_fails,
  probe_parent_present, probe_refined_collapse, probe_reverse_moves,
  trace_collapse, diagnose_B, diagnose_B2, decomp_probe, structure_probe,
  definitive_check), code/pattern (a186085, bottom_probe, triangle_build,
  transfer_hunt, transfer_search2), code/amoeba (amoeba_extend,
  distinct_hist_count).
- Filled the missing research/ rows for L1.1 (a186085, a383891, a392317),
  L1.0 (a055999, a074171, a134227) and L2.0 (L1.0.md) in their LEAF indexes.
  Note: describe_file routes research descriptions to the top-level
  research/INDEX.md, which the researcher role continuously regenerates; the
  persistent home for these rows is the leaf index, so write there.
- Research top-level INDEX.md is owned/rewritten by the researcher role (it was
  observed shrinking to only CLAIMS/THREADS during this pass) — not touched,
  as it is being actively maintained by that role.
- The code/inventor folder is being actively written by the run's inventor role
  (new probe programs appeared mid-pass: probe_a2_fails, diagnosis, traces).
  All current files are described; a refresh at the very end may show more.
- The `.full.md` source texts under research/L0.0/ are intentionally never
  indexed (their digests in L2.0 are the index rows) — refresh confirms this.
- No file's content was changed; only index rows were added/corrected.

