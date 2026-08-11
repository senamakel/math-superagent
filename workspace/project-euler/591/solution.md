# Solution: Project Euler 591

## Reduction to inhomogeneous Diophantine approximation

Fix non-square d, s = sqrt(d), n = 10^13. For a target real x = pi, the quadratic
integer closest to pi with |a|,|b| <= n minimizes

    |a + b·s - pi|.

For each fixed integer b the optimal a is a = round(pi - b·s) (nearest integer),
subject to |a| <= n.

Write s = s0 + alpha with s0 = floor(s), alpha = {s} in (0,1). Then
pi - b·s = (pi - b·s0) - b·alpha, and mod 1 the residual is
-(b·alpha - beta) where beta = {pi}. Hence the distance from {b·alpha} to beta
in circular metric:

    dist({b alpha}, beta) = min(|{b alpha}-beta|, |{b alpha}-beta±1|).

So the absolute error equals the circular distance from {b·alpha} to beta.

Feasible b ranges (from |a|<=n):
  b >= 0 : a = round(pi - b s),  a >= -n  =>  b <= (n+pi)/s  =>  B+ = floor((n+pi)/s)
  b <  0 : b = -c,  a = round(pi + c s),  a <= n  =>  c <= (n-pi)/s  =>  B- = floor((n-pi)/s)

The negative-c half is the same routine run against the target {-(pi)} = 1 - beta.

## Core subproblem

> Given irrational alpha in (0,1), target beta in [0,1), bound B: find b in [0,B]
> minimizing the circular distance from {b alpha} to beta.

## Governing theorem (Ostrowski alpha-numeration of the shift)

Cabanillas-Lopez & Labbe, "A variant of Ostrowski numeration", arXiv:1904.01874,
Props 9 & 10, Algorithm 3(ii).

alpha = [0; a1, a2, ...]. Continuants q_{-1}=0, q_0=1, q_k = a_k q_{k-1} + q_{k-2}.
Convergent errors delta_{-1}=1, delta_0=alpha, delta_k = -a_k delta_{k-1}+delta_{k-2}
(positive, decreasing to 0). Greedy alpha-numeration of beta:
  b_k = min(a_k, ceil(beta_{k-1}/delta_{k-1})),  beta_k = b_k delta_{k-1}-beta_{k-1}.

Best-RIGHT candidates (Prop 9): n=0; terminal prefix; and
  n = sum_{i=1}^{2k-1} b_i q_{i-1} + j q_{2k-1},  j in {0,...,b_{2k}-1},  k>=1.
Best-LEFT candidates (Prop 10): terminal prefix; and
  n = sum_{i=1}^{2k} b_i q_{i-1} + j q_{2k},  j in {0,...,b_{2k+1}-1},  k>=0.

The true minimizer over n in [0,B] is a best left OR right alpha-approximation,
so it lies in the union of these candidate sets. Enumerate all candidates with
n <= B, evaluate circular distance, take the minimum.

Why O(log B): for the quadratic irrational alpha the denominators q_k grow
geometrically (q_{k+T} ~ c·theta^k), so only O(log B) levels k are needed.

## Why Pell/unit is not the answer

The optimum solves the inhomogeneous problem (target beta = {pi}), not the
homogeneous |p - q s| one; it is a best left/right alpha-approximation shifted by
the digits of beta, generally not a Pell unit. Confirmed by the given example
BQA_2(pi,10) = 6 - 2 sqrt(2), whose norm 28 != ±1.

## Precision

a,b ~ 1e13..1e14, best gaps ~1e-13 down to arbitrarily small for quadratic
irrationals. Use mpmath with DPS ~ 200 to compare candidates with full
precision; errors computed as a + b*sqrt(d) - pi.

## Algorithm per d

1. alpha = sqrt(d) - floor(sqrt(d)); beta = pi - 3 (fractional part, high precision).
2. Build CF of alpha, q_k, delta_k until q_k > B (B = max(B+,B-)).
3. Alpha-numerate beta: digits b_k.
4. Generate candidate b in [0,B+] (right/left families) -> error via dist to beta;
   best (a,b) with a=round(pi-b*s), a=round reused, record error and a.
5. Repeat with target 1-beta over [0,B-], giving c (and b=-c, a=round(pi+c*s)).
6. Global min over the two; tie-break by smaller error then smaller |a|.
7. |a| contributes to answer.

## Verification (multiple routes)
- Reproduce BQA_2(pi,10)=6-2√2, BQA_5(pi,100)=26√5-55, BQA_7(pi,1e6)=560323-211781√7.
- Cross-check algorithm vs brute.py on many small (d,B,beta) random cases.
- Independent second route: Berthe-Imbert Algorithm 2 (DMTCS 11:1(2009)) best-left
  approximation from convergents + errors; apply to beta and 1-beta; compare final
  summed answer and per-d (a,b).
