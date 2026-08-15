"""Verify the core technical claims of the three proposed approaches.

Candidate 1 (comparison-order-cellular-automaton):
  (a) the exact identity |b-c| > |a-b|  <=>  (a-c)(a+c-2b) < 0  for all integer triples
  (b) the scale-invariance kill: two rows differing by an overall positive scale
      have IDENTICAL comparison+convexity words but different A_k(1) magnitudes.
      => the orientation system cannot force A_k(1) in {0,2}.
"""
import itertools

# --- (a) verify the local-rule identity exactly over a range ---
bad = 0
for a, b, c in itertools.product(range(-30, 31), repeat=3):
    lhs = abs(b-c) > abs(a-b)
    rhs = (a-c)*(a+c-2*b) < 0
    if lhs != rhs:
        bad += 1
print(f"[C1 identity] total triples checked, mismatches = {bad}")

# --- (b) scale-invariance kill ---
def words(row):
    # comparison bit [row[i+1] >= row[i]] and convexity bit [row[i]+row[i+2] >= 2*row[i+1]]
    cmp_ = [1 if row[i+1] >= row[i] else 0 for i in range(len(row)-1)]
    cvx = [1 if row[i] + row[i+2] >= 2*row[i+1] else 0 for i in range(len(row)-2)]
    return tuple(cmp_), tuple(cvx)

r = [1, 2, 0, 4, 6, 2]      # second entry = 2  (in {0,2})
scaled = [3*x for x in r]    # second entry = 6  (NOT in {0,2})
print(f"[C1 scale] row A_k(1)={r[1]}, scaled A_k(1)={scaled[1]}")
print(f"[C1 scale] words equal? {words(r) == words(scaled)}  (cmp,cvx) r={words(r)} scaled={words(scaled)}")

# also verify the same for entries that stay nonnegative (rows of a Gilbreath triangle are nonneg)
r2 = [1, 2, 0, 2, 4, 2, 6]  # all even >=0 after position 0, second entry 2
s2 = [2*x for x in r2]       # second entry 4, still a valid even row
print(f"[C1 scale2] A_k(1) {r2[1]} vs {s2[1]}; words equal? {words(r2) == words(s2)}")

# --- Candidate 3 direction test: which process has the larger event surplus ---
# From the run's own measured event rates (conditional-rate-experiment):
#   prime lambda_post10 ~ 0.351; random-class pooled lambda ~ 0.585
# Higher event rate  =>  larger recharge surplus S_k. We need PRIME >= RANDOM for
# the coupling transfer; measured PRIME < RANDOM.
prime_rate, random_rate = 0.351, 0.585
print(f"[C3 direction] prime event rate {prime_rate} vs random {random_rate}: "
      f"prime{' >' if prime_rate > random_rate else ' <'} random => "
      f"needed direction for transfer (prime dominates random) {'HOLDS' if prime_rate > random_rate else 'FAILS'}")
