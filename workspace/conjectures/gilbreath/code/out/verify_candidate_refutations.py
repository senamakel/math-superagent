"""Verify, for the research record, the two load-bearing claims used to refute
comparison-order-cellular-automaton:

(1) The local-rule identity: |b-c| > |a-b|  <=>  (a-c)(a+c-2b) < 0   [over all integers]
(2) The scale-invariance kill:  comparison word and convexity word are both
    invariant under positive scaling A -> lambda*A, while the second entry
    A_k(1) scales.  So the symbolic system has no information about |A_k(1)|.
"""
import itertools

# (1) exact identity over a range
bad = 0
for a, b, c in itertools.product(range(-40, 41), repeat=3):
    if (abs(b-c) > abs(a-b)) != ((a-c)*(a+c-2*b) < 0):
        bad += 1
print(f"[1] local-rule identity over a,b,c in [-40,40]: mismatches = {bad}")

# (2) scale invariance of the comparison/convexity word, and second entry scaling
def words(row):
    cmp_ = tuple(1 if row[i+1] >= row[i] else 0 for i in range(len(row)-1))
    cvx  = tuple(1 if row[i] + row[i+2] >= 2*row[i+1] else 0 for i in range(len(row)-2))
    return cmp_, cvx

# even rows of a 2-then-odds triangle: A_k(0)=1, all i>=1 even => positive scaling keeps them even
r  = (1, 2, 0, 4, 6, 2)     # second entry 2  (conjecture-satisfying value)
r2 = (1, 4, 0, 8, 12, 4)    # double: second entry 4 (conjecture-violating value), still all-even
print(f"[2] r  A_k(1)={r[1]}, r2 A_k(1)={r2[1]}")
print(f"[2] words(r) == words(r2)? {words(r) == words(r2)}")
print(f"[2]   r  (cmp,cvx) = {words(r)}")
print(f"[2]   r2 (cmp,cvx) = {words(r2)}")
# homogeneity of the actual operator: T(lambda x) = lambda T(x)
r2next = tuple(abs(r2[i]-r2[i+1]) for i in range(len(r2)-1))
rnext  = tuple(abs(r[i]-r[i+1]) for i in range(len(r)-1))
print(f"[2] absolute-diff operator is homogeneous: 2*T(r) == T(2r)? "
      f"{tuple(2*x for x in rnext) == r2next}")

# (3) for candidate 3: measured event-rate direction
prime_rate = 0.351   # rho_post10, claim conditional-rate-experiment-prime-reference
random_rate = 0.585  # pooled lambda_hat, family-independent
print(f"[3] prime event rate {prime_rate} vs random {random_rate}: "
      f"prime {'>=' if prime_rate >= random_rate else '<'} random => "
      f"needed domination (prime surplus >= random surplus) "
      f"{'HOLDS in the needed direction' if prime_rate >= random_rate else 'FAILS (wrong direction — random dominates prime)'}")
