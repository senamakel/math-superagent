# Working memory

## Problem

Q(n) = sum over all permutations pi of {1..n} of [ sum_{i=1}^{n!} rank(pi^i) ],
where rank(pi) is the 1-based position of pi in the lexicographically sorted
list of all n! permutations (one-line notation, e.g. rank(2,1,3)=3), and pi^i is
the i-th iterate with (pi^{k+1})(j) = pi(pi^k(j)), pi^0 = identity.
Need Q(10^6) mod (10^9+7); statement gives Q(2)=5, Q(3)=88, Q(6)=133103808,
Q(10) ≡ 468421536 (mod 10^9+7).

## Established results

Verified by brute.py (literal double sum) AND brute2.py (independent period
formula), all run 18 Sep 2025 (UTC), exact integers then reduced mod p:

| n | Q(n) | Q(n) mod (10^9+7) | method1 time | method2 time |
|---|---|---|---|---|
| 2 | 5 | 5 | <0.01s | <0.01s |
| 3 | 88 | 88 | <0.01s | <0.01s |
| 4 | 4808 | 4808 | <0.01s | <0.01s |
| 5 | 597876 | 597876 | 0.00s | 0.00s |
| 6 | 133103808 | 133103808 | 0.13s | 0.00s |
| 7 | 47124948960 | 124948631 | 7.17s | 0.02s |
| 8 | 24768798220800 | 798047424 | not reached (est. 8.7 min > budget) | 0.16s |

- Oracle checks: rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808 — all pass.
- Cross-validation: methods exactly agree for n=2..7 (Q values identical, not
  just congruent mod p).  Note: for n≤5 Q(n) < p so mod is trivially equal.
- Structural fact behind brute2 (proved inline): pi^i is periodic with period
  d = ord(pi) = lcm of cycle lengths.  Every cycle length divides n!, hence
  d | n!, so among i = 1..n! each distinct power appears exactly n!/d times;
  sum_i rank(pi^i) = (n!/d) * sum_{tau in <pi>} rank(tau).
- Time/space: method 1 is O((n!)^2) tuple compositions + O(n!) rank dict (ran
  for n ≤ 7, 5040^2 = 25.4M steps in 7.2s); method 2 is O((n!) * avg d) + O(n!)
  (much faster, reached n=8 in 0.16s).  Both are exact-integer arithmetic.

## Failed approaches

(none yet)

## gaps.py — T(j,m) translation invariance & arithmetic form (18 Sep 2025)

T(j,m) = #{(pi,i): 0<=i<n!, (pi^i)(m) < (pi^i)(j)}, computed for n=2..9 with
the period formula T(j,m) = sum_pi (n!/ord(pi)) * #{tau in <pi>: tau(m)<tau(j)}
with exact Fractions (no literal n!-power iteration).

Verified: literal double-count oracle agrees for n=2,3 (in-script), n=4,5
(separate oracle).  Translation invariance T(j,j+k) independent of j holds for
ALL j in every n (checked exhaustively).  f_n(k)=T(1,1+k) is exactly
ARITHMETIC (constant 2nd difference = 0) for every n>=3, with values:

| n | f_n(k) = A_n + (k-1) B_n | A_n = f(1) | B_n (step) |
|---|---|---|---|
| 2 | [1] (trivial) | 1 | - |
| 3 | 10,11 | 10 | +1 |
| 4 | 184,184,184 | 184 | 0 |
| 5 | 5052,4944,4836,4728 | 5052 | -108 |
| 6 | 191232,187632,184032,180432,176832 | 191232 | -3600 |
| 7 | 9851040,9642240,9433440,9224640,9015840,8807040 | 9851040 | -208800 |
| 8 | 650626560,638208000,625789440,613370880,600952320,588533760,576115200 | 650626560 | -12418560 |
| 9 | 54052427520,53119825920,52187224320,51254622720,50322021120,49389419520,48456817920,47524216320 | 54052427520 | -932601600 |

Conjecture (structure): f_n(k) = A_n + (k-1) B_n is arithmetic in the gap k for
all n; B_n<=0 for n>=5.  Sequence A_n: 1,10,184,5052,191232,9851040,...
(no obvious closed form derived yet).

## Open questions

- Efficient method for n = 10^6 (n! is astronomically beyond enumeration):
  need a structural/analytic closed form, e.g. via rank = sum of factoradic
  weights, cycle-type / conjugacy-class decomposition, and the sum over i of
  rank(pi^i).  Unresolved.
- Q(10) check against statement (468421536 mod p) still pending — brute is
  infeasible for n=10; needs the efficient method.

## Structural finding from explore.py (n = 2..7, exact integers, 18 Sep 2025)

Definitions (0-indexed one-line permutation of {0..n-1}):
  a_j(tau) = #{ m>j : tau[m] < tau[j] }   (Lehmer coefficient)
  M_j      = sum_pi sum_{i=0}^{n!-1} a_j(pi^i)
  N(j,m)   = #{(pi,i) : 0<=i<n!, (pi^i)[m] < (pi^i)[j]}

Verified on every n=2..7:  M_j = sum_{m>j} N[j][m]  (linearity; identity is
exact, not asymptotic).

KEY PATTERN: N(j,m) depends ONLY on the gap k = m-j (translation invariance),
i.e. N(j,m) = f(k).  So M_j = sum_{k=1}^{n-1-j} f(k)  is a suffix sum of the
gap function f(k).  Hence M_j is NOT constant in j; it decreases with j.

Observed f(k) = N(j, j+k):
  n=2: f(1)=1
  n=3: f(1)=10,  f(2)=11
  n=4: f(1)=f(2)=f(3)=184
  n=5: f(1..4)=5052,4944,4836,4728  (arithmetic, step -108)
  n=6: f(1..5)=191232,187632,184032,180432,176832  (arithmetic, step -3600)
  n=7: f(1..6)=9851040,9642240,9433440,9224640,9015840,8807040 (step -208800)

M_j vectors (j=0..n-1):
  n=2: [1,0]
  n=3: [21,10,0]
  n=4: [552,368,184,0]
  n=5: [19560,14832,9996,5052,0]
  n=6: [920160,743328,562896,378864,191232,0]
  n=7: [55974240,47167200,38151360,28926720,19493280,9851040,0]

So the per-position Lehmer contributions are translation-invariant in pairwise
form, and M_j is the suffix sum of f(k).  To get Q(n) we need sum_j (n-j)! M_j
then + (n!)^2 (rank = 1 + sum_j a_j (n-j)! over powers; the +1 per power term
sums to n!·n! = (n!)^2).  Next step: derive a closed form for f(k).

CORRECT factoradic weight (verified by exact Q reconstruction for n=2..7):
  rank(tau) = 1 + sum_{j=0}^{n-2} a_j(tau) * (n-1-j)!   [weight is (n-1-j)!, NOT (n-j)!]
  Q(n) = (n!)^2 + sum_{j=0}^{n-2} (n-1-j)! * M_j
Cross-check: with M_j from explore.py and this formula, Q matches all of
Q(2..7)={5,88,4808,597876,133103808,47124948960} exactly (done 18 Sep 2025).
This is an independent second route to the M_j tables' correctness.

## Established results

Record proved steps, verified computations, and source-backed facts.

## Failed approaches

Record attempts that should not be repeated without a new reason.

## Open questions

Record the next unresolved steps.
