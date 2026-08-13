"""Verify structural facts about the infinite N>=6 family from the sequence tools,
and test the conjecture N(a_i)=6 for all i>=2 (extending the exact-count evidence).

Facts to verify exactly:
1. n_i = F(2i+2)F(2i+3)-1, k_i = F(2i)F(2i+3)-1 (the definition)
2. n_i = F(2i)*F(2i+1)-1  [identity to OEIS A089508, reindexed]
3. order-3 LRR: n_i - 8n_{i-1}+8n_{i-2}-n_{i-3}=0  (homogenized recurrence)
4. first differences n_i - n_{i-1} = F(4i+?): check against A033891/A172968 = F(4i+7)
5. ratio n_{i+1}/n_i -> phi^4
6. NEW: exact N(a_i) for i=5 to test "N=6 for all i>=2" (i=1 is the N=8 anomaly).

Convention: N counts both mirrors + trivial pair. Exact integer arithmetic,
inversion per small k, k <= log2(a).
"""
import math
import gmpy2

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# ---- 1-5: structural facts on n_i, k_i ----
N = 12
ns, ks = [], []
for i in range(1, N+1):
    n = fib(2*i+2)*fib(2*i+3) - 1
    k = fib(2*i)*fib(2*i+3) - 1
    ns.append(n); ks.append(k)

print("=== Fact 1 & 2: closed forms ===")
ok2 = all(ns[i-1] == fib(2*i)*fib(2*i+1)-1 for i in range(1, N+1))
print("n_i == F(2i)F(2i+1)-1 (A089508 identity):", ok2)

print("=== Fact 3: order-3 LRR n_i=8n_{i-1}-8n_{i-2}+n_{i-3} ===")
ok3n = all(ns[i-1] - 8*ns[i-2] + 8*ns[i-3] - ns[i-4] == 0 for i in range(4, N+1))
ok3k = all(ks[i-1] - 8*ks[i-2] + 8*ks[i-3] - ks[i-4] == 0 for i in range(4, N+1))
print("n homog LRR holds i=4..%d:" % N, ok3n)
print("k homog LRR holds i=4..%d:" % N, ok3k)

print("=== Fact 4: first differences of n_i vs Fibonacci ===")
for i in range(1, N):
    d = ns[i] - ns[i-1]
    # check d == F(4i+7)?  A033891 terms: 89,610,4181 at i=1,2,3 -> F(11),F(15),F(19)=F(4i+7)
    print("  i=%d: n diff=%d  F(4i+7)=%d  match=%s" % (i, d, fib(4*i+7), d == fib(4*i+7)))

print("=== Fact 5: ratio n_{i+1}/n_i -> phi^4 ===")
import math as _m
for i in range(1, N-1):
    print("  i=%d: %.6f" % (i, ns[i] / ns[i-1]))

# ---- 6: exact multiplicity to extend the N=6 conjecture ----
print("\n=== Fact 6: exact N(a_i), i=1..5 (both-mirrors + trivial) ===")
def occurrences_half(a, kmax_override=None):
    sol = []
    kfact = 1
    kmax = kmax_override if kmax_override else a.bit_length()
    for k in range(2, kmax + 1):
        kfact *= k
        if math.comb(2*k, k) > a:
            break
        hi = k - 1 + gmpy2.iroot(kfact * a, k)[0] + 1
        while math.comb(hi, k) < a:
            hi <<= 1
        lo = 0
        while lo + 1 < hi:
            mid = (lo + hi) >> 1
            if math.comb(mid, k) <= a:
                lo = mid
            else:
                hi = mid
        if math.comb(lo, k) == a and 2*k <= lo:
            sol.append((lo, k))
    return sol

def N_both(a, sol):
    c = 2
    for (n, k) in sol:
        c += 1 if 2*k == n else 2
    return c

for i in range(1, 6):
    n, k = ns[i-1], ks[i-1]
    a = math.comb(n+1, k+1)
    sol = occurrences_half(a)
    N = N_both(a, sol)
    print("i=%d: a digits=%d  N(a_i)=%d  half-solutions=%s" % (i, len(str(a)), N, sol))
print("Conjecture N(a_i)=6 for i>=2: checked to i=5; i=1 is the N=8 anomaly (a=3003).")
