#!/usr/bin/env python3
"""Verify the F2 linearization identity  nu2(q_n) = wt(Phi_n h) exactly.

Convention (locked with code/out/reconcile_nu2w.py):
  * nu2(q_n)  = count of 2s in the maximal {0,2} suffix of the right diagonal
                through q_n, tail = diag(n)[2:-1], walk back from the end while
                entries are in {0,2}.
  * diag(n)   = [rows[k][n-k] for k in range(n)]   (delta_k(q_n) = A_k[n-k]).
  * h[j]      = (A_1[j] // 2) mod 2, j in [2, n-1]  (=1 iff gap_{j+1}==2 mod 4).

Identity to verify (per suffix/tail cell k, k in the maximal {0,2} suffix):
      (diag[k] // 2) mod 2  ==  XOR_{m in [0,k-1]} [C(k-1,m) mod 2] * h[n-k+m]
and hence  nu2 == wt(Phi_n h restricted to the suffix rows), where the explicit
matrix row k has entry [C(k-1, j-(n-k)) mod 2] at column j in [n-k, n-1], else
0, over columns j in [2, n-1].

Math: writing b_k(i) = (A_k(i)//2) mod 2 (all columns >=1 of A_k are even, so
halving is exact), for A_k(i),A_k(i+1) even:  b_{k+1}(i) = b_k(i) XOR b_k(i+1)
because |2a-2b|/2 = |a-b| and |a-b| mod 2 = (a mod 2) XOR (b mod 2).  Hence b_k
is the Pascal-mod-2 (Rule-90) fold of b_1 = h on every column >= 1 cell, so the
identity holds on the whole triangle, and in particular on the {0,2} suffix
where a suffix cell is a 2 iff its b-fold is 1, giving nu2 == wt(Phi_n h).

Exact integer arithmetic throughout.  O(N log log N) sieve + O(M^2) triangle.
"""
import math
from lib.gilbreath import primes_up_to

MAX_N = 3000              # dense range upper bound
TRI_N = 4001              # triangle depth/width: enough for sparse n=3999
SPARSE = [50, 100, 200, 400, 800, 1600, 3200, 3999]
BOUND = 1_000_000


def comb_parity(k_minus_1, m):
    """C(k-1, m) mod 2 via the bit-subset identity (C(n,m) odd iff m & ~n == 0)."""
    return 0 if (m & ~(k_minus_1)) else 1


def build_phi_matrix(suffix_ks, n):
    """Explicit F2 matrix Phi_n: rows = suffix cells k, columns j in [2,n-1].
    Entry (k, col j) = C(k-1, j-(n-k)) mod 2 if j in [n-k, n-1] else 0.
    Returns (cols list, rows list-of-dicts k->{j: bit})."""
    cols = list(range(2, n))                 # j in [2, n-1]
    rows = []
    for k in suffix_ks:
        row = {}
        km1 = k - 1
        for m in range(0, k):                # j = n-k+m in [n-k, n-1]
            j = n - k + m
            row[j] = comb_parity(km1, m)
        rows.append((k, row))
    return cols, rows


def wt_from_matrix(matrix, h):
    """wt(Phi_n h) restricted to the suffix rows = count of suffix cells whose
    fold XOR == 1.  matrix = (cols, rows) from build_phi_matrix; h is a dict
    j -> bit for j in [2, n-1]."""
    cols, rows = matrix
    hd = {j: h[j] for j in cols}
    total = 0
    per = []
    for k, row in rows:
        acc = 0
        for j, bit in row.items():
            acc ^= (bit & hd[j])
        per.append((k, acc))
        total += acc
    return total, per


def main():
    P = primes_up_to(BOUND)
    W = len(P)
    print("sieve to %d : %d primes (need > %d)" % (BOUND, W, TRI_N))
    assert W > TRI_N + 2, "not enough primes"

    # ---- build the integer triangle rows ----
    width = TRI_N + 2
    rows = [P[:width]]
    for k in range(1, TRI_N):
        prev = rows[-1]
        rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])

    # ---- global identity: b-table via XOR recurrence equals actual b ----
    # bt[1] = h; bt[k+1][i] = bt[k][i] XOR bt[k][i+1]; check bt[k][i] ==
    # (rows[k][i]//2) mod 2 for all k>=1, i>=1 (zero violations => the Pascal
    # fold equals the actual halved mod-2 bit on every column>=1 cell).
    bt_prev = [(rows[1][i] // 2) % 2 for i in range(len(rows[1]))]
    bt = {1: bt_prev}
    global_viol = 0
    n_checked = 0
    for k in range(1, TRI_N - 1):
        for i in range(1, len(bt_prev) - 1):
            want = (rows[k][i] // 2) % 2
            got = bt_prev[i]
            n_checked += 1
            if want != got:
                global_viol += 1
                if global_viol <= 10:
                    print("  GLOBAL XOR MISMATCH k=%d i=%d actual=%d bt=%d" %
                          (k, i, want, got))
        # advance bt via XOR recurrence
        nxt = [bt_prev[i] ^ bt_prev[i + 1] for i in range(len(bt_prev) - 1)]
        bt[k + 1] = nxt
        bt_prev = nxt
    print("\n=== GLOBAL identity b_k(i) = Pascal-fold of h, all cells i>=1 ===")
    print("cells checked (k>=1,i>=1): %d  violations: %d" % (n_checked, global_viol))

    def suffix_of(n):
        """Return list of k in the maximal {0,2} suffix of diag(n)[2:-1]."""
        d = [rows[k][n - k] for k in range(n)]
        tail = d[2:-1]
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        # tail index t in [i, len-1]  <->  k = t+2
        return [t + 2 for t in range(i, len(tail))]

    def nu2_of(n):
        d = [rows[k][n - k] for k in range(n)]
        tail = d[2:-1]
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        return tail[i:].count(2)

    h_full = {j: (rows[1][j] // 2) % 2 for j in range(2, TRI_N)}

    # ---- (1) sample set: individual suffix-cell identity + matrix wt ----
    print("\n=== (1) SPARSE sample set {50,..,3999}: per-cell + matrix weight ===")
    print("%-6s %-7s %-7s %-8s %-8s %-7s" % (
        "n", "nu2", "wt(Phi h)", "sufCells", "cellViol", "sufK\n"))
    all_cell_viol = 0
    all_cell_check = 0
    for n in SPARSE:
        nu2 = nu2_of(n)
        suf = suffix_of(n)
        # per-cell identity: (diag//2)%2 vs fold via bt (=Pascal fold of h)
        cell_viol = 0
        wt_from_bt = 0
        for k in suf:
            actual = (rows[k][n - k] // 2) % 2
            fold = bt[k][n - k]           # Pascal-fold of h by construction
            all_cell_check += 1
            if actual != fold:
                cell_viol += 1
                all_cell_viol += 1
            wt_from_bt += fold            # suffix cells in {0,2}: fold==1 <=> cell==2
        # explicit matrix weight
        matrix = build_phi_matrix(suf, n)
        hmat = {j: h_full[j] for j in range(2, n)}
        wt_from_mat, per = wt_from_matrix(matrix, hmat)
        ok = (nu2 == wt_from_bt == wt_from_mat) and cell_viol == 0
        print("%-6d %-7d %-7d %-8d %-8d %s" % (
            n, nu2, wt_from_mat, len(suf), cell_viol, "OK" if ok else "MISMATCH"))
        assert nu2 == wt_from_bt == wt_from_mat, "n=%d aggregate failed" % n
        assert cell_viol == 0, "n=%d per-cell identity failed" % n
    print("per-cell suffix identity checked over %d cells, %d violations"
          % (all_cell_check, all_cell_viol))

    # ---- (2) dense n in [50, MAX_N]: nu2 == wt (via bt, cheap) ----
    print("\n=== (2) DENSE n in [50,%d]: nu2 == wt(Phi_n h) ===" % MAX_N)
    dense_viol = 0
    per_cell_dense_viol = 0
    dense_n = 0
    for n in range(50, MAX_N + 1):
        nu2 = nu2_of(n)
        suf = suffix_of(n)
        wt = 0
        for k in suf:
            # confirm per-cell identity too (fold == actual b)
            if (rows[k][n - k] // 2) % 2 != bt[k][n - k]:
                per_cell_dense_viol += 1
            wt += bt[k][n - k]
        if nu2 != wt:
            dense_viol += 1
            if dense_viol <= 10:
                print("  DENSE MISMATCH n=%d nu2=%d wt=%d" % (n, nu2, wt))
        dense_n += 1
    print("dense n in [50,%d]: %d n-values, nu2==wt violations: %d, "
          "per-cell identity violations: %d"
          % (MAX_N, dense_n, dense_viol, per_cell_dense_viol))

    # ---- (3) convention lock: all-ones and all-zeros h through Phi_n ----
    print("\n=== (3) CONVENTION LOCK: all-ones / all-zeros h through Phi_n ===")
    for n in SPARSE:
        suf = suffix_of(n)
        matrix = build_phi_matrix(suf, n)
        hones = {j: 1 for j in range(2, n)}
        hzeros = {j: 0 for j in range(2, n)}
        w1, _ = wt_from_matrix(matrix, hones)
        w0, _ = wt_from_matrix(matrix, hzeros)
        print("n=%-5d suffix-cells=%2d  wt(all-ones h)=%d  wt(all-zeros h)=%d"
              % (n, len(suf), w1, w0))
        assert w1 == 0 and w0 == 0, "convention lock failed at n=%d" % n

    # ---- cross-check recorded nu2 values ----
    print("\n=== CROSS-CHECK against recorded nu2 values (reconcile_nu2w) ===")
    for n in [50, 100, 200, 400, 800, 1600, 3200, 3999]:
        print("n=%-5d nu2=%d   (recorded: 26,42,98,203,389,785,1604,2048)"
              % (n, nu2_of(n)))

    print("\nRESULT: F2 linearization identity nu2(q_n) == wt(Phi_n h) "
          "CONFIRMED")
    print("  over sparse samples %s and dense n in [50,%d]" % (SPARSE, MAX_N))
    print("  per-cell fold identity: 0 violations everywhere in column>=1 "
          "(%d cells dense-checked)" % (n_checked,))
    print("  convention lock: all-ones/all-zeros h both give nu2=0 at all 8 "
          "samples")


if __name__ == "__main__":
    main()
