# Scratchpad

## Tool-builder oracle run (oracle subtask, current)
Reused existing code/brute.py (naive literal double sum) on the worked-example
sizes only.  `python code/brute.py 2 3 6` -> exit 0, all oracles OK:
  rank(2,1,3)=3   Q(2)=5   Q(3)=88   Q(6)=133103808
<0.15s total (n=6: 518400 power-steps).  Wrote code/results.json.  Reading of
the definition is thereby pinned; size bound 10^6 is left to the derivation.

Same run re-executed (this session) -> identical output; brute2.py (independent
period-formula oracle) also run at n=2,3,6 -> exact agreement on all three and
cross-check vs method 1 all True.  results.json / results2.json regenerated.

## Task (from user)
Write brute.py in /workspace: enumerate all n! permutations in lex order, rank dict
(tuple -> 1-based rank), reproduce rank((2,1,3)) = 3. For each pi, compute pi^i for
i = 1..n! and sum rank(pi^i) mod p; sum over all pi; report Q(n) and Q(n) mod p.
Run n = 2..6 (check Q(2)=5, Q(3)=88, Q(6)=133103808), then n=7, then n=8 only if
it finishes within ~5 min.  Second independent method (brute2.py):
Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau), ord = lcm of cycle lengths,
<pi> = distinct powers.  Verify agreement n=2..6 (will compare 2..7).  Report both.

## DONE — task12.py (chain oracle + A/B/tables, 18 Sep 2025)
Chain verified: Q(n)=(n!)^2+A(n!-1)+(B/2)T with A=f(0), B=f(1)-f(0) from
out/extend_f.json via solution.q_from_ab:
  n=10: Q mod p = 468421536 == statement oracle  [OK]
  n=6:  133103808 == brute value               [OK]
  n=8:  798047424 == brute value               [OK]
So the whole reduction + extend_f.json n=10 row reproduces the statement's
Q(10) mod p.  Full A_n/B_n/c_n table and prime factorizations printed
(the c_n=(|B|/(n-1)!) integer only for n>=6: 30,290,2464,23130,235080,2728368).

## DONE — task3.py (n=12/13 wall, method2 reuse), 18 Sep 2025
f_n_method2 (verify_f_method2.py) enumerates all n! perms → wall ~ n! * const.
Measured n=10 at 24.6s → extrapolate n=11 ~4.5min, n=12 ~54min, n=13 ~12h.
No faster cycle-type method is written, so n=12/13 SKIPPED (would exceed the
few-minute budget).  Report wall instead.

## Current sub-task (extend_f.py)
Compute f_n(k) = #{(pi,i): 0<=i<n!, (pi^i)(k) < (pi^i)(0)} for n=2..11,
0-based, period formula, row j=0 only, exact ints, no mod.  Save to
extend_f.json as {n: [f(1),...,f(n-1)]}.  Print each row with first/second
differences (all-zero 2nd diff => exactly arithmetic).  Gate at ~280 s per n.
DONE: n=2..11 all computed (n=11 334.8s), every row exactly arithmetic,
n=10,11 verified independently by verify_f_method2.py (cycle-type decomp).

## Method-1 cost model
n=7: 5040 perms x 5040 powers = 25.4M tuple builds (len 7) + dict lookups -> seconds.
n=8: 40320^2 = 1.63e9 -> ~64x n=7; gate on t7*64*(8/7) <= 290 s, hard budget 300 s.

## Method-2 justification
Sequence pi^i is periodic with period d = ord(pi); d | lcm(1..n) | n!, so every
distinct power appears exactly n!/d times among i = 1..n!.  Hence
sum_i rank(pi^i) = (n!/d) * sum_{tau in <pi>} rank(tau).  Exact integer, then mod p.

## Power semantics check
(pi^k)(j) = pi(pi^{k-1}(j)); 0-based: new[j-1] = pi[old[j-1]-1], i.e.
cur_next = tuple(pi[v-1] for v in cur).  Sanity: pi=(2,1) -> (1,2)=id after 2 steps.
Q(2)=5 by hand: id contributes 2*1, (2,1) contributes (2/2)*(2+1)=3.  Total 5. OK.

## Verified results (both methods agree exactly for n=2..7; method 2 only for n=8)
| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| Q(n) | 5 | 88 | 4808 | 597876 | 133103808 | 47124948960 | 24768798220800 |
| Q(n) mod p | 5 | 88 | 4808 | 597876 | 133103808 | 124948631 | 798047424 |

Timings: method 1 (literal): n=6 0.13s, n=7 7.18s; n=8 skipped (est. 8.8 min).
Method 2 (period formula): n=7 0.02s, n=8 0.16s.

## explore.py (18 Sep 2025) -- run, saved to explore.out.txt

Task: for n=2..7 compute M_j = sum_pi sum_{i=0}^{n!-1} a_j(pi^i) with
a_j(tau)=#{m>j: tau[m]<tau[j]}, and N(j,m)=#{(pi,i):0<=i<n!,(pi^i)[m]<(pi^i)[j]}.
Output tables in explore.out.txt.  Exact integers.

Findings (see memory.md): N(j,m) depends only on gap m-j -> M_j is a suffix
sum of gap function f(k).  M_j not constant; decreases with j.  Verified
M_j == sum_{m>j} N[j][m] for all n=2..7.