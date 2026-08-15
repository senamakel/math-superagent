#!/usr/bin/env python3
"""
INDEPENDENT from-scratch verification of the Thue-Morse nu2 accounting claim
in research/notes/thue-morse-sublinear-supply-witness.md.

Claim under test:
    nu2(q_n) = #{d <= n : zeta(h)[d] == 1}
             = #{d <= n : d is a power of two}
             = floor(log2 n)+1

Setup (restated from the note):
    h[j] = wt(j) mod 2            (Thue-Morse bit), j >= 0
    q    = 2-then-odds sequence:  q[0]=2, q[1]=3,
           q[j+2]-q[j+1] = 2 if h[j]=1 else 4   (so gap g[j]=q[j+1]-q[j],
           g[0]=1, and for j>=1: g[j]=2 if h[j-1]=1 else 4).
    nu2(n) = number of cells equal to 2 in the maximal {0,2} suffix of the
             right diagonal delta(q_n) = [A_k(n-k)]_k, floored at index 2:
             scan k from n down to 2, cell value A_k(n-k); while the running
             suffix stays within {0,2} count the cells equal to 2; stop at
             the first cell not in {0,2} (or when k drops below 2).

Two independent from-scratch routes:
  (A) Direct integer triangle: build A_0..A_D, read right diagonal for each n.
  (B) Subset-zeta: zeta(h)[d] = XOR_{j submask of d} h[j]; count hits.

No lib.* import; everything reimplemented.
"""

import sys

D = 2000

# ---------- shared primitives (from scratch) ----------

def popcount(x):
    return bin(x).count('1')

def build_h(N):
    # h[j] = wt(j) mod 2 for j = 0..N
    return [popcount(j) & 1 for j in range(N + 1)]

def build_q(D, h):
    """2-then-odds sequence q[0..D] driven by Thue-Morse bits.""" 
    q = [0] * (D + 1)
    q[0] = 2
    q[1] = 3
    # gaps g[j+1] = q[j+2]-q[j+1] = 2 if h[j]==1 else 4
    for j in range(D - 1):
        nxt = q[j + 1] + (2 if h[j] == 1 else 4)
        # q[j+1] starts at q[1]=3 which is set; fill q[j+2]
        pass
    # fill directly: q[k] for k>=2 from gap at k-2
    for k in range(2, D + 1):
        q[k] = q[k - 1] + (2 if h[k - 2] == 1 else 4)
    return q

# ---------- Route A: direct triangle ----------

def build_triangle(D, q):
    """Return list T with T[k] = row A_k (exact ints)."""
    T = [q]
    prev = q
    while len(prev) > 1:
        nxt = [abs(prev[i] - prev[i + 1]) for i in range(len(prev) - 1)]
        T.append(nxt)
        prev = nxt
    return T

def right_diagonal(T, n):
    """[A_k(n-k)]_k for k=0..n."""
    return [T[k][n - k] for k in range(n + 1)]

def nu2_of_diag(diag):
    """Scan k from n-1 down to 2 (the maximal {0,2} suffix of the right
    diagonal, excluding the bottom cell A_n(0) which is the left edge = 1),
    counting cells equal to 2; stop at the first cell not in {0,2} or when
    the k=2 floor is reached.  Matches the run's canonical convention
    (body = diag[:-1], floor at index 2)."""
    # diag[k] = A_k(n-k); indices k=0..n. Scan k = n-1, n-2, ..., 2.
    n = len(diag) - 1
    count = 0
    k = n - 1
    while k >= 2:
        v = diag[k]
        if v not in (0, 2):
            break
        if v == 2:
            count += 1
        k -= 1
    return count

def nu2_all(T, ns):
    """Direct-then read right diagonal, compute nu2 per n (and all n up to
    the max of ns)."""
    maxn = max(ns)
    out = {}
    diag_cache = {}
    # reading the right diagonal of the stored triangle for each n
    for n in range(2, maxn + 1):
        diag = right_diagonal(T, n)
        out[n] = nu2_of_diag(diag)
    return out

# ---------- Route B: subset-zeta ----------

def subset_zeta_all(h, N):
    """Fast subset-zeta transform over F2: z[d] = XOR_{j submask of d} h[j].
    O(N log N) in-place on a copy of h[0..N].  This is the standard
    polynomial DP: for each bit b, z[m] ^= z[m without bit b] where b set."""
    z = list(h[:N + 1])
    b = 1
    while b <= N:
        for d in range(N + 1):
            if d & b:
                z[d] ^= z[d ^ b]
        b <<= 1
    return z

def zeta_count_from(z, n):
    """Z = #{d in 1..n : z[d]==1} given the precomputed zeta array z."""
    return sum(1 for d in range(1, n + 1) if z[d] == 1)

def is_power_of_two(d):
    return d >= 1 and (d & (d - 1)) == 0

def count_powers_of_two(n):
    return sum(1 for d in range(1, n + 1) if is_power_of_two(d))

# ---------- main ----------

def main():
    ns = [2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 100, 200, 500, 1000, 2000]

    print("D =", D)

    # h bits for the gaps: need h[0..D-2]
    h = build_h(D)
    print("h[0..15] =", h[:16])

    q = build_q(D, h)
    print("q[0..11] =", q[:12])

    # ---- Route A ----
    print("\n=== Route A: direct integer triangle (from scratch) ===")
    T = build_triangle(D, q)
    # rows built up to the single-cell row; confirm we reached depth D
    print("triangle has rows k=0..%d (row lengths: start %d -> end %d)"
          % (len(T) - 1, len(T[0]), len(T[-1])))

    nu2A = nu2_all(T, ns)

    # sanity: hand-computed right diagonals / nu2 for tiny n
    # n=2: A_2(0)=3 not in {0,2} -> nu2=0
    # n=3: A_3(0)=1 -> 0
    # n=4: bottom A_4(0) -> check
    print("hand-nu2 check: nu2(2)=%d nu2(3)=%d nu2(4)=%d"
          % (nu2A[2], nu2A[3], nu2A[4]))

    # ---- Route B ----
    print("\n=== Route B: subset-zeta (from scratch) ===")
    zeta_arr = subset_zeta_all(h, D)
    Zs = {}
    pws = {}
    for n in ns:
        Zs[n] = zeta_count_from(zeta_arr, n)
        pws[n] = count_powers_of_two(n)

    # ---- comparison ----
    print("\n=== Comparison ===")
    print("%-6s %-8s %-8s %-8s | %-6s %-6s" %
          ("n", "nu2_A", "Z", "#pw2", "nu2==Z", "nu2==#pw2"))
    first_AZ = None
    first_Ap = None
    for n in ns:
        a = nu2A[n]; z = Zs[n]; p = pws[n]
        ok1 = (a == z); ok2 = (a == p)
        if not ok1 and first_AZ is None:
            first_AZ = n
        if not ok2 and first_Ap is None:
            first_Ap = n
        print("%-6d %-8d %-8d %-8d | %-6s %-6s"
              % (n, a, z, p, "OK" if ok1 else "NO", "OK" if ok2 else "NO"))

    print("\nfirst n where nu2_A != Z          :", first_AZ)
    print("first n where nu2_A != #pw2       :", first_Ap)

    # full scan over n=2..D for first failures
    f1 = None; f2 = None
    for n in range(2, D + 1):
        if f1 is None and nu2A[n] != zeta_count_from(zeta_arr, n):
            f1 = n
        if f2 is None and nu2A[n] != count_powers_of_two(n):
            f2 = n
    print("first n in 2..D where nu2_A != Z   :", f1,
          "(nu2=%d, Z=%d)" % (nu2A[f1] if f1 else None,
                              zeta_count_from(zeta_arr, f1) if f1 else None))
    print("first n in 2..D where nu2_A != #pw2:", f2,
          "(nu2=%d, #pw2=%d)" % (nu2A[f2] if f2 else None,
                                 count_powers_of_two(f2) if f2 else None))

    # Any equality anywhere?
    any_eq_Z = [n for n in range(2, D + 1)
                if nu2A[n] == zeta_count_from(zeta_arr, n)]
    any_eq_p = [n for n in range(2, D + 1) if nu2A[n] == count_powers_of_two(n)]
    print("n in 2..D with nu2_A == Z    (count %d): first few %s"
          % (len(any_eq_Z), any_eq_Z[:15]))
    print("n in 2..D with nu2_A == #pw2 (count %d): first few %s"
          % (len(any_eq_p), any_eq_p[:15]))
    print("max nu2_A over n in 2..%d: %d" % (D, max(nu2A.values())))

    # ---- n=100 detail: tail of right diagonal and zeta over same indices ----
    print("\n=== n=100 detail ===")
    n = 100
    diag = right_diagonal(T, n)
    print("right diagonal delta(q_%d), last 15 cells (k=%d..%d) = A_k(n-k):" %
          (n, n - 14, n))
    for k in range(max(2, n - 14), n + 1):
        zk = zeta_arr[k]
        print("  k=%3d  A_k(%3d)=%3d   zeta(h)[%d]=%d" %
              (k, n - k, diag[k], k, zk))
    print("nu2_A(%d) = %d" % (n, nu2A[n]))
    print("Z(%d)     = %d" % (n, zeta_count_from(zeta_arr, n)))
    print("#pw2(%d)  = %d" % (n, count_powers_of_two(n)))

    # ---- conclusion ----
    ident_holds = (first_AZ is None)
    ident2_holds = (first_Ap is None)
    print("\n=== VERDICT ===")
    print("nu2_A == Z        :", "HOLDS at all sampled n" if ident_holds
          else "REFUTED (first failure at n=%d)" % first_AZ)
    print("nu2_A == #pw2     :", "HOLDS at all sampled n" if ident2_holds
          else "REFUTED (first failure at n=%d)" % first_Ap)
    return 0

if __name__ == "__main__":
    sys.exit(main())
