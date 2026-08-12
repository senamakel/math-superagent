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

## This tool-builder task's runs

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
