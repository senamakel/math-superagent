"""Exact structure of the infinite multiplicity->=6 family (Singmaster's conjecture).

Family (Lind/Singmaster/Tovey; established-review.md claim infinite-family-6):
    C(n+1, k+1) = C(n, k+2)   with
    n_i = F_{2i+2} F_{2i+3} - 1
    k_i = F_{2i}   F_{2i+3} - 1
    a_i = C(n_i + 1, k_i + 1)          (i = 1, 2, ...)
a_1 = 3003, a_2 = 61218182743304701891431482520 (OEIS A090162 / A003015).

Derived here (from the classical identity F_a F_b = (L_{a+b} - (-1)^b L_{a-b})/5):
    F_{2i+2} F_{2i+3} = (L_{4i+5} - 1)/5   =>  n_i = (L_{4i+5} - 6)/5   =>  u_i := 5 n_i + 6 = L_{4i+5}
    F_{2i}   F_{2i+3} = (L_{4i+3} - 4)/5   =>  k_i = (L_{4i+3} - 9)/5   =>  v_i := 5 k_i + 9 = L_{4i+3}
The sequences L_{4i+5} and L_{4i+3} each satisfy x_i = 7 x_{i-1} - x_{i-2} (roots phi^4, psi^4;
phi^4 + psi^4 = L_4 = 7, (phi psi)^4 = 1). Hence, exactly:
    n_i = 7 n_{i-1} - n_{i-2} + 6
    k_i = 7 k_{i-1} - k_{i-2} + 9
Both recurrences are verified below against direct Fibonacci computation.

Convention: N(a) counts BOTH mirrored occurrences and includes the trivial pair
C(a,1)=C(a,a-1), matching code/out/witnesses.json. Exact N(a_i) is computed for
i = 1..4 by inverting C(n,k)=a per k (k <= log2(a), binary search in n bounded by
n <= k-1+(k! a)^{1/k}, from C(n,k) >= (n-k+1)^k/k!). i = 5,6 get only the small-k
partial scan (k <= 200) and the triangular check 8a+1 square.

All exact integer arithmetic. gmpy2 for iroot/is_square, math.comb for binomials.
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
    if n == 0: return a
    for _ in range(1, n):
        a, b = b, a + b
    return b

NMAX = 8
print("=== Family parameters, i = 1..%d ===" % NMAX)
print("%2s %22s %22s %4s %4s %8s %28s" % ("i", "n_i", "k_i", "okC", "okRec", "u_i=5n+6", "v_i=5k+9"))
ns, ks, us, vs, As = [], [], [], [], []
for i in range(1, NMAX + 1):
    n = fib(2*i + 2) * fib(2*i + 3) - 1
    k = fib(2*i) * fib(2*i + 3) - 1
    a = math.comb(n + 1, k + 1)
    lhs = math.comb(n + 1, k + 1)
    rhs = math.comb(n, k + 2)
    ns.append(n); ks.append(k); As.append(a)
    u = 5 * n + 6; v = 5 * k + 9
    us.append(u); vs.append(v)
    # direct checks of the two derived identities and of the recurrence
    okC = (lhs == rhs) and (u == lucas(4*i + 5)) and (v == lucas(4*i + 3))
    okRec = True
    if i >= 3:
        okRec = (n == 7*ns[-2] - ns[-3] + 6) and (k == 7*ks[-2] - ks[-3] + 9)
    print("%2d %22d %22d %5s %6s %9d %11d" % (i, n, k, okC, okRec, u, v))
    assert okC and okRec, (i, n, k)

print("\nAll i=1..%d: C(n+1,k+1)==C(n,k+2), u_i==L_{4i+5}, v_i==L_{4i+3}, recurrences n,k hold." % NMAX)
print("Lucas-identity derivation CONFIRMED against direct Fibonacci/Lucas computation.")

print("\n=== Family values a_i, digit counts, growth ===")
print("%2s %38s %10s %8s %10s" % ("i", "a_i", "digits", "bits", "d_i/d_{i-1}"))
prev = None
for i, a in enumerate(As, start=1):
    d = len(str(a))
    bits = a.bit_length()
    ratio = (d / prev) if prev else float('nan')
    print("%2d %38d %10d %8d %10.4f%s" % (i, a, d, bits, ratio,
          "   <- 3003" if i == 1 else ""))
    prev = d
print("(d_i/d_{i-1}) -> phi^4 ~= 6.854 asymptotically: log10 a_i ~ c*(phi^4)^i. Linear-recurrent? "
      "No: log a_i grows exponentially, impossible for a sum of exponentials. See tool output below.")

def occurrences_half(a, kmax_override=None):
    """All (n,k) with 2<=k<=n/2 and C(n,k)=a, exact. k <= log2(a) suffices since
    C(2k,k) >= 2^k. Binary search in n per k, upper bound n <= k-1+(k!a)^{1/k}.
    Returns list of (n,k)."""
    sol = []
    kfact = 1
    kmax = kmax_override if kmax_override else a.bit_length()
    for k in range(2, kmax + 1):
        kfact *= k
        if math.comb(2*k, k) > a:
            break                      # larger k: C(2k,k) only grows
        hi = k - 1 + gmpy2.iroot(kfact * a, k)[0] + 1
        while math.comb(hi, k) < a:    # safety doubling (should never trigger)
            hi <<= 1
        lo = 0
        while lo + 1 < hi:             # largest n with C(n,k) <= a
            mid = (lo + hi) >> 1
            if math.comb(mid, k) <= a:
                lo = mid
            else:
                hi = mid
        if math.comb(lo, k) == a and 2*k <= lo:
            sol.append((lo, k))
    return sol

def N_both(a, sol):
    """both-mirrors + trivial-pair count from half-triangle solutions."""
    c = 2  # (a,1) and (a,a-1), distinct since a > 1
    for (n, k) in sol:
        c += 1 if 2*k == n else 2
    return c

print("\n=== Exact N(a_i), i = 1..4 (both-mirrors + trivial convention) ===")
for i in range(1, 5):
    t0 = time.time()
    a = As[i-1]
    sol = occurrences_half(a)
    N = N_both(a, sol)
    print("i=%d: a=%-30s N=%d  half-solutions=%s  (%.1fs, k<=%d scanned)"
          % (i, str(a), N, sol, time.time() - t0, a.bit_length()))
    # triangular check: C(x,2)=a iff 8a+1 square
    sq = gmpy2.iroot(8*a + 1, 2)[1]
    if sq:
        x = (gmpy2.isqrt(8*a + 1) + 1) // 2
        print("     8a+1 IS a square: C(%d,2) = a (additional occurrence)" % x)

print("\n=== i = 5, 6: triangular check (k=2) and partial small-k scan (k <= 200) ===")
for i in (5, 6):
    a = As[i-1]
    sq = gmpy2.iroot(8*a + 1, 2)[1]
    if sq:
        x = (gmpy2.isqrt(8*a + 1) + 1) // 2
        print("i=%d: 8a+1 IS a square: C(%s,2) = a" % (i, x))
    else:
        print("i=%d: 8a+1 is NOT a square -> no C(x,2)=a occurrence" % i)
    t0 = time.time()
    sol = occurrences_half(a, kmax_override=200)
    Nlo = N_both(a, sol)
    print("     partial (k<=200): N(a) >= %d, half-solutions found=%s (%.1fs)"
          % (Nlo, sol, time.time() - t0))
    print("     NOTE: k up to log2(a) ~ %d not scanned; exact N(a_%d) NOT established here." % (a.bit_length(), i))

print("\n=== sanity: N(3003) == 8, matching witnesses.json ===")
assert N_both(3003, occurrences_half(3003)) == 8
print("OK")
print("\nAll done.")