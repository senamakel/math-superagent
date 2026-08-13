"""Exact multiplicities of the infinite N>=6 family (Singmaster's conjecture).

Family (Lind/Singmaster/Tovey): C(n+1, k+1) = C(n, k+2) with
    n_i = F_{2i+2} F_{2i+3} - 1
    k_i = F_{2i}   F_{2i+3} - 1
    a_i = C(n_i + 1, k_i + 1)          (i = 1, 2, ...)
a_1 = 3003 (N=8), a_2 = 61218182743304701891431482520 (OEIS A090162).

The n_i, k_i are small (n_12 ~ 5e8); only a_i grows (by a factor ~phi^4 ~ 6.85
in digits per step), so computing a_i = math.comb(n+1, k+1) directly becomes the
bottleneck. Scope discipline: compute exact multiplicities for i = 1..4, verify
the recurrences to i = 12 (cheap: n_i, k_i are small), and verify the identity
C(n+1,k+1)=C(n,k+2) to i = 7 by direct comb (a_7 ~ 3M digits, ~acceptable one
time). i >= 8 a_i is a multi-gigabyte integer, so the identity there is verified
via the small-size equivalent identity instead:
    C(n+1,k+1)==C(n,k+2)  <=>  (n+1)(k+2) == (n-k)(n-k-1) ... (scaled)
which is NOT used; instead i>=8 identity is left unchecked and stated so.

Convention: N(a) counts BOTH mirrored occurrences AND the trivial pair
C(a,1)=C(a,a-1), matching code/out/witnesses.json. Exact N(a_i) computed for
i=1..4 by inverting C(n,k)=a per k (k <= log2(a), binary search in n, upper
bound n <= k-1 + floor((k! a)^(1/k)) + 1).

All exact integer arithmetic. gmpy2 for iroot, math.comb for binomials.
"""
import math
import gmpy2
import time

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def lucas(n):
    a, b = 2, 1
    if n == 0:
        return a
    for _ in range(1, n):
        a, b = b, a + b
    return b

NMAX_REC = 12   # recurrences verified to i = 12 (n_i, k_i small; cheap)
NMAX_ID = 7     # identity C(n+1,k+1)=C(n,k+2) verified by direct comb to i = 7
NMAX_EXACT = 4  # exact N(a_i) computed for i = 1..4

print("=== Family parameters i = 1..%d : recurrences and Lucas identities ===" % NMAX_REC)
print("%2s %20s %20s %6s %6s" % ("i", "n_i", "k_i", "okRec", "okLucas"))
ns, ks = [], []
for i in range(1, NMAX_REC + 1):
    n = fib(2*i + 2) * fib(2*i + 3) - 1
    k = fib(2*i) * fib(2*i + 3) - 1
    ns.append(n); ks.append(k)
    u = 5 * n + 6; v = 5 * k + 9
    okLucas = (u == lucas(4*i + 5)) and (v == lucas(4*i + 3))
    okRec = True
    if i >= 3:
        okRec = (n == 7*ns[-2] - ns[-3] + 6) and (k == 7*ks[-2] - ks[-3] + 9)
    print("%2d %20d %20d %6s %6s" % (i, n, k, okRec, okLucas))
    assert okRec and okLucas, (i, n, k)
print("recurrences n_i=7n_{i-1}-n_{i-2}+6, k_i=7k_{i-1}-k_{i-2}+9 and Lucas"
      " identities hold for i=1..%d.\n" % NMAX_REC)

print("=== Identity C(n+1,k+1)=C(n,k+2), i = 1..%d (direct comb) ===" % NMAX_ID)
for i in range(1, NMAX_ID + 1):
    n, k = ns[i-1], ks[i-1]
    t0 = time.time()
    lhs = math.comb(n + 1, k + 1)
    rhs = math.comb(n, k + 2)
    dt = time.time() - t0
    print("i=%d: n=%d k=%d  C(n+1,k+1)==C(n,k+2): %s  a_i digits=%d  (%.1fs)"
          % (i, n, k, lhs == rhs, len(str(lhs)) if lhs else 0, dt))
    assert lhs == rhs, (i, n, k)
print("identity holds i=1..%d.\n" % NMAX_ID)

print("=== Exact N(a_i), i = 1..%d (both-mirrors + trivial convention) ===" % NMAX_EXACT)
def occurrences_half(a, kmax_override=None):
    """All (n,k) with 2<=k<=n/2 and C(n,k)=a, exact. k <= log2(a) suffices.
    Binary search in n per k; hi = k-1 + floor((k! a)^(1/k)) + 1."""
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
    c = 2  # (a,1) and (a,a-1), distinct since a > 1
    for (n, k) in sol:
        c += 1 if 2*k == n else 2
    return c

family_vals = {}
family_N = {}
for i in range(1, NMAX_EXACT + 1):
    n, k = ns[i-1], ks[i-1]
    a = math.comb(n + 1, k + 1)
    family_vals[i] = a
    t0 = time.time()
    sol = occurrences_half(a)
    N = N_both(a, sol)
    family_N[i] = N
    print("i=%d: a_i digits=%d  N(a_i)=%d  half-solutions=%s  (%.1fs, k<=%d scanned)"
          % (i, len(str(a)), N, sol, time.time() - t0, a.bit_length()))
    assert N >= 6, (i, N)

print("\nSanity: exact N(3003) via same oracle (expect 8, matches witnesses.json).")
assert N_both(3003, occurrences_half(3003)) == 8
print("N(3003)=8 OK.")
print("\nRESULT: infinite-family members i=1..%d each have N(a_i)>=6 "
      "(both-mirrors + trivial convention). Exact multiplicities:"
      % NMAX_EXACT)
for i in range(1, NMAX_EXACT + 1):
    print("   i=%d: N(a_i)=%d" % (i, family_N[i]))
print("\nAll done.")
