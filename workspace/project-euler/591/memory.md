# Working memory

## Problem
PE 591: for each non-square integer d with 1<=d<100, find BQA_d(pi, 10^13) =
the quadratic integer a + b*sqrt(d) (|a|<=n, |b|<=n, n=10^13) minimizing
|a + b*sqrt(d) - pi|. I_d(...) = a. Answer = sum of |a_d| over 90 non-square d.

## Established results
- Brute-force oracle /workspace/brute.py reproduces all 3 worked examples:
  BQA_2(pi,10)=6-2√2 (a=6,b=-2); BQA_5(pi,100)=26√5-55 (a=-55,b=26);
  BQA_7(pi,1e6)=560323-211781√7. PASS.
- /workspace/verify_big.py confirms (60-digit mpmath) that for d=2,n=1e13,
  a=-6188084046055,b=4375636191520 gives |a+b√2-pi| = 4.293e-15 < 1e-13. PASS.
  (matches the statement's double inequality lower bound exactly).

## Core subproblem and governing theory
For fixed b, best a = round(pi - b*s), s=√d. So error = circular distance
dist({b·α}, β) where α = {√d} = s - floor(s), β = {π}. Negative b handled by
the same routine with target β' = {-π} = 1 - β.
Feasible ranges: b>=0 -> B+ = floor((n+pi)/s); b<0 (b=-c) -> B- = floor((n-pi)/s).

Theory (Cabanillas-Lopez & Labbe arXiv:1904.01874, Props 9 & 10, Alg 3(ii)):
Ostrowski alpha-numeration of beta. CF of alpha: q_{-1}=0,q_0=1,q_k=a_k q_{k-1}+q_{k-2};
deltas delta_{-1}=1, delta_0=alpha, delta_k = -a_k delta_{k-1}+delta_{k-2} (>0, down to 0).
Greedy digits b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1})), beta_k = b_k delta_{k-1}-beta_{k-1}.
Best-RIGHT candidates (Prop 9): n=0; terminal prefix; and
  n = sum_{i=1..2k-1} b_i q_{i-1} + j q_{2k-1}, j in {0..b_{2k}-1}, k>=1.
Best-LEFT candidates (Prop 10): terminal prefix; and
  n = sum_{i=1..2k} b_i q_{i-1} + j q_{2k}, j in {0..b_{2k+1}-1}, k>=0.
Global min over [0,B] is min of these candidate distances (filtered to <=B).
Complexity O(log B) since q_k grows geometrically for quadratic alpha.

Independent second route: Berthe & Imbert (DMTCS 11:1(2009)) Algorithm 2, best
left alpha-approximations from convergents (p_n/q_n), errors f_n=|q_n alpha-p_n|;
apply to beta and to 1-beta to cover both sides.

Why NOT Pell: optimum solves inhomogeneous problem with shift beta; not a Pell unit
(example 6-2√2 has norm 28 != ±1).

## Precision
n=1e13, values ~1e14, best gap ~1e-13..1e-15. Need >~30 significant digits;
use mpmath with DPS ~ 80 to resolve the winner safely.

## Failed approaches
(none yet)

## Open questions
- Must tune candidate enumeration level count (q_k up to > Bound).
- Confirm tie-break rule with statement/brute (min error, then smaller |a|).
