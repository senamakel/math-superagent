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

## Open questions

- Efficient method for n = 10^6 (n! is astronomically beyond enumeration):
  need a structural/analytic closed form, e.g. via rank = sum of factoradic
  weights, cycle-type / conjugacy-class decomposition, and the sum over i of
  rank(pi^i).  Unresolved.
- Q(10) check against statement (468421536 mod p) still pending — brute is
  infeasible for n=10; needs the efficient method.

## Established results

Record proved steps, verified computations, and source-backed facts.

## Failed approaches

Record attempts that should not be repeated without a new reason.

## Open questions

Record the next unresolved steps.
