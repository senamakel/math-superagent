# Scratchpad

## Task (from user)
Write brute.py in /workspace: enumerate all n! permutations in lex order, rank dict
(tuple -> 1-based rank), reproduce rank((2,1,3)) = 3. For each pi, compute pi^i for
i = 1..n! and sum rank(pi^i) mod p; sum over all pi; report Q(n) and Q(n) mod p.
Run n = 2..6 (check Q(2)=5, Q(3)=88, Q(6)=133103808), then n=7, then n=8 only if
it finishes within ~5 min.  Second independent method (brute2.py):
Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau), ord = lcm of cycle lengths,
<pi> = distinct powers.  Verify agreement n=2..6 (will compare 2..7).  Report both.

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

## Verification plan
- brute.py: assert rank((2,1,3))==3, Q(2)==5, Q(3)==88, Q(6)==133103808; save results.json.
- brute2.py: independent code (rebuilds rank dict), assert same examples, load results.json
  and compare with method 1 for each n both reached; print agreement table.