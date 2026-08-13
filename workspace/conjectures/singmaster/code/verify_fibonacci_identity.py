"""Verify Singmaster's infinite family C(n+1,m+1)=C(n,m+2) with N>=6.

Singmaster 1975 (Fibonacci Quart. 13(4), 295-298) gives solutions to
    C(n+1, k+1) = C(n, k+2)
via  n+1 = F_{2j+2} F_{2j+3},  k+1 = F_{2j} F_{2j+3} + 1
where F_0=0, F_1=1.

Equivalently in MRSTT Remark 1.4's notation (m there = k here):
    n = F_{2j+2} F_{2j+3} - 1,   m = F_{2j} F_{2j+3} - 1
solves  C(n+1, m+1) = C(n, m+2).

We check: identity holds, and the common value occurs >= 6 times
(2 interior + 2 mirrors + value=a as C(a,1) and its mirror = 6).
"""
from math import comb

F = [0, 1]
for _ in range(60):
    F.append(F[-1] + F[-2])

def occurrences(a):
    """count (n,k) with 1<=k<=n-1, C(n,k)=a, k<=n/2 convention-free: count all."""
    cnt = 0
    # n must satisfy C(n,1)=a => n=a; and k <= log2(a) since C(2k,k)>=2^k
    k = 1
    while True:
        lo, hi = k, a + 1
        # find n with C(n,k)=a if any (binary search); C monotone in n for n>=k
        while lo <= hi:
            mid = (lo + hi) // 2
            c = comb(mid, k)
            if c == a:
                cnt += 1
                n_found = mid
                break
            elif c < a:
                lo = mid + 1
            else:
                hi = mid - 1
        k += 1
        if k > 63:            # safety bound well past log2(a) needs
            break
        if comb(2 * k, k) > a and k > 2:
            break
    return cnt

print("=== Fibonacci family identity ===")
for j in range(1, 7):
    # MRSTT notation
    n = F[2*j+2] * F[2*j+3] - 1
    m = F[2*j]   * F[2*j+3] - 1
    lhs = comb(n + 1, m + 1)
    rhs = comb(n, m + 2)
    a = lhs
    occ = occurrences(a)
    print(f"j={j}: n+1={n+1} m+1={m+1} | C(n+1,m+1)=C(n,m+2): "
          f"{lhs==rhs}  value={a}  N(a)={occ}")

print("\n=== 3003 check (expect 8 by MRSTT (1.2) counting both halves) ===")
print("MRSTT (1.2):", [(3003,1),(78,2),(15,5),(14,6),(14,8),(15,10),(78,76),(3003,3002)])
print("computed occurrences(3003):", occurrences(3003))

print("\n=== Singmaster 1975 list of the seven nontrivial repetitions ===")
print("120, 210, 1540, 7140, 11628, 24310, 3003")
for v in [120, 210, 1540, 7140, 11628, 24310, 3003]:
    print(v, "N =", occurrences(v))
