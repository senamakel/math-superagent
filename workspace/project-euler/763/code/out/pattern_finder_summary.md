# Pattern-recognition summary for PE763

## What was found, and its status

### SOURCED — d=2 analog == OEIS A007902 (pebbling configurations)
The 2D amoeba (cell at (x,y) splits into (x+1,y),(x,y+1) if both empty)
has D_2(N) = A007902(N+1). Exact for N=0..21 (computed by exact BFS and
cross-checked by a frozenset oracle). Asymptotic D_2 ~ 0.1227 * 2.3216^N
(Knessl). A007902 has NO simple one-index recurrence — only a two-index DP
(G(k,m)). This is the model for what to expect in 3D: no closed form, a real
transfer procedure needed. Filed at research/L1.0/oeis_a007902.md.

### NEW SOURCED MATCH — distinct HISTOGRAM count == OEIS A186085 (sandpiles)
The count H(N) of distinct level-histograms over reachable N-configs,
N=2..14 = 1,1,2,3,5,8,13,22,36,60,100,166,277, is EXACTLY OEIS A186085
("1-dimensional sandpiles with n grains" = smooth compositions with first/last
part 1, |consecutive difference|<=1). Verified H(N)==A186085(N) on N=2..14
against the published table (code/pattern/check_a186085_recurrence.py) and by
oeis_lookup. This is a genuine structural link: the reachable 3D configurations
cluster by level-histogram, and the histograms are in bijection with smooth
compositions. It does NOT give D(N) (H(N)≠D(N); D counts configurations, not
histograms), but it tells the run the histogram-indexing family — the
"shape space" of the amoeba — is the sandpile family, worth deriving how many
configs realize each histogram.

### CORRECTION (NEGATIVE, breaks a prior claim): Q_k decomposition is FALSE for even N
The repeated claim "D(N)=sum_k Q_k(N) 3^(N-2k-1) reproduces D(N)", where
Q_k(N)=R(N,N-k)/3^(N-2k-1) (R = count of max-level-M configs, k=N-M), holds
ONLY for odd N (and N<=11). It FAILS at even N: N=12 misses 30, N=14 misses 267
(code/pattern/qdecomp_falsify.py). Cause: for even N the column with max level
M=N/2 (offset k=N/2) has exponent 2M-N-1 = -1, is excluded by the e>=0 gate,
yet such configs exist (R(12,6)=30, R(14,7)=267). So:
- The Q_k polynomial closed forms ARE exact for each column in the region
  M>(N+1)/2 (verified OOS at N=13,14 for those columns).
- But D(N) is NOT that closed-form sum as a full identity. First falsifier of
  the summed formula is N=12, NOT N=15 as previously guessed.

### CONFIRMED (no change)
- Diagonal R(N,N)=3^(N-1) exact for all N=2..14.
- Order-7 const-coeff recurrence on D(0..14) is an overfit (not reproducible).

### OVERFIT CAUTION (reproduced)
find_linear_recurrence handed back an order-6 constant-coeff recurrence for H
that fits H(2..14) perfectly but DIVERGES from published A186085 at n=6. Direct
proof that perfect finite-window fits carry no predictive power. Reinforces the
holonomic-negative conclusion. Any recurrence used to reach D(10000) must be
derived, not fitted.

## Where this leaves the solver
Still no closed form for D(N), and now a corrected understanding: the max-level
decomposition is exact per-column but the summed formula needs the M=N/2
(empty-least-offset) terms at even N. The A186085 (sandpile) match is the
strongest NEW structural lead to hand the inventor: the histogram/shape space
is the smooth-composition family, and the run needs to count configs per
histogram.

## First falsifiers (to break each claim)
- Q_k column polynomials: extend a column to a fresh N and compare.
- D(N)=Q-sum formula: ANY even N>11 (already broken at N=12,14).
- H(N)==A186085: H(15) vs A186085(15)=461 (needs histogram count at N=15).
- D_2 == A007902: D_2(22) vs A007902(23)=31775756.

## Files
- Analysis: code/pattern/*.py (see code/pattern/INDEX.md)
- code/pattern/check_a186085_recurrence.py, qdecomp_falsify.py, mdist2.py,
  full_triangle_dump.py, pn_poly.py (this run's new probes)
- SCRATCHPAD.md (findings recorded)
- research/L1.1/oeis_a186085.md (sourced d=2 sandpile match)
