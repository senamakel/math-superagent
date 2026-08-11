# Pattern-recognition summary for PE763

## What was found, and its status

### SOURCED — d=2 analog == OEIS A007902 (pebbling configurations)
The 2D amoeba (cell at (x,y) splits into (x+1,y),(x,y+1) if both empty)
has D_2(N) = A007902(N+1). Exact for N=0..21 (computed by exact BFS and
cross-checked by a frozenset oracle). Asymptotic D_2 ~ 0.1227 * 2.3216^N
(Knessl). A007902 has NO simple one-index recurrence — only a two-index DP
(G(k,m)). This is the model for what to expect in 3D: no closed form, a real
transfer procedure needed. Filed at research/L1.0/oeis_a007902.md.

### CONFIRMED (exact, survived out-of-sample) — max-level decomposition
N(N,M) = # distinct reachable configs after N divisions with max level M.
For offset k=N-M: N(N,N-k) = Q_k(N) * 3^(N-2k-1), Q_k a degree-k polynomial.
Closed forms Q_0=1, Q_1=N-3, Q_2=(N-5)(N+2)/2, Q_3=(N^3-73N+168)/6,
Q_4=N^4/24+N^3/4-205N^2/24+97N/4+27. Verified at FRESH N=13,14 (not in the
fit data), so it survives the break attempt; still a conjecture past N=14.
D(N) = sum_{k=0}^{N-2} Q_k(N) 3^(N-2k-1).

### NEGATIVE results (dead ends, recorded so nobody repeats them)
- Order-7 constant-coefficient linear recurrence over D(0..14): OVERFIT,
  fails integrality at n=18, can't hit the statement's D(20). 
- D(0..14) not in OEIS.
- D(N) not small-order holonomic (P-recursive): all order/degree fits either
  pole or go non-integer immediately.

## Where this leaves the solver
No closed form. The forward/BFS enumeration is memory-capped well below D(15).
The path forward is a transfer/DP on the structure that produced the
max-level columns — the 3D generalization of the d=2 A007902 G(k,m) DP. That
is the seam between these structural facts and the efficient method the run
needs; handed to inventor/orchestrator.

## First falsifiers (to break each claim)
- Q_k columns / D(N)=sum: N=15 (needs M histogram at N=15, not BFS-computable
  here). Compute D(15) some other way and compare.
- 3^(N-1) diagonal: N=15.
- D_2 == A007902: D_2(22) vs A007902(23)=31775756.

## Files
- Analysis: code/pattern/*.py (see code/pattern/INDEX.md)
- SCRATCHPAD_pattern.md (this run's notes)
- data/level_N.txt (N=2..12 config features), code/out/mhist_13_14.txt
  (fresh M-histograms), research/L1.0/oeis_a007902.md (sourced d=2).
