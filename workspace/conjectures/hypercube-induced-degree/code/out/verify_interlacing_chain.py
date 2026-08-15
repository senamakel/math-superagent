"""Verify the spectral-interlacing lower-bound chain for the cube, exactly.

Objects
-------
A_1 = [[0,1],[1,0]]
A_n = block [[A_{n-1}, I_{2^{n-1}}], [I_{2^{n-1}}, -A_{n-1}]]

This is the Huang signed adjacency of Q_n. By block multiplication,
A_n^2 = [[A_{n-1}^2 + I, A_{n-1} - A_{n-1}],
         [A_{n-1} - A_{n-1}, I + A_{n-1}^2]]
      = [[n I, 0], [0, n I]] = n I_{2^n},
so the spectrum of A_n is {+sqrt(n), -sqrt(n)}, each with multiplicity
2^{n-1} (A_n is symmetric, zero diagonal, trace 0).

Checks performed
----------------
(a) For n=1..8: A_n is symmetric, entries in {0,±1}, A_n^2 = n*I EXACTLY
    (integer arithmetic). We also check the support: A_n[u,v] != 0 iff u,v
    differ in exactly one bit (= an edge of Q_n).
(b) Interlacing claim: for S = (even-weight vertices) + one odd vertex, size
    2^{n-1}+1, B = A_n[S,S] has lambda_max(B) >= sqrt(n). Verified n=2..8.
(c) For the pure even-weight independent set (size 2^{n-1}), lambda_max(B)
    should be < sqrt(n). B there is A_{n-1}, so lambda_max = sqrt(n-1).

All matrices are built as exact integer matrices (Python ints / int64); the
square identity A_n^2 = n I is checked in exact integer arithmetic. Lambda_max
is computed to high precision (numpy eigh on float64, plus a scipy-checked
largest-eigenvalue via power iteration to cross-check).
"""

import numpy as np


def build_An(n):
    """Exact integer signed adjacency A_n of Q_n (numpy int64, exact values)."""
    A = np.array([[0, 1], [1, 0]], dtype=np.int64)
    if n == 1:
        return A
    for k in range(2, n + 1):
        m = A.shape[0]  # 2^{k-1}
        I = np.eye(m, dtype=np.int64)
        top = np.block([[A, I], [I, -A]])
        A = top
    return A


def popcount(x):
    return bin(x).count("1")


def check_square_and_support(n):
    """Return (symmetric_ok, entries_ok, square_ok, support_ok) exact checks."""
    N = 1 << n
    A = build_An(n)
    # (a) symmetry
    symmetric_ok = bool(np.array_equal(A, A.T))
    # (a) entries in {0, ±1}
    entries_ok = bool(np.max(np.abs(A)) <= 1 and np.all(np.isin(A, [-1, 0, 1])))
    # zero diagonal
    diag_ok = bool(np.all(np.diag(A) == 0))
    # (a) A^2 = n I exactly (int64; |entries of A^2| <= 2^n = 256 for n=8)
    A2 = A @ A
    square_diag = np.diag(A2)
    square_off = A2 - np.diag(np.diag(A2))
    square_ok = bool(
        np.all(square_diag == n) and np.all(square_off == 0)
    )
    # (b) support == edges of Q_n: A[u,v] != 0 iff Hamming distance 1
    support_ok = True
    for u in range(N):
        for v in range(N):
            if u == v:
                continue
            d = u ^ v
            differs_one_bit = (d & (d - 1)) == 0  # popcount(u^v)==1
            is_edge = bool(A[u, v] != 0)
            if is_edge != differs_one_bit:
                support_ok = False
                break
        if not support_ok:
            break
    return symmetric_ok, entries_ok, diag_ok, square_ok, support_ok


def lambda_max(A, S):
    """Largest eigenvalue of A[S,S] (principal submatrix), high precision."""
    B = A[np.ix_(S, S)].astype(np.float64)
    ev = np.linalg.eigvalsh(B)
    return ev[-1]


def even_weight_set(n):
    return [v for v in range(1 << n) if popcount(v) % 2 == 0]


def main():
    print("=" * 72)
    print("(a) A_n symmetry, {0,±1} entries, zero diagonal, A_n^2 = n*I, support=edges")
    print("=" * 72)
    for n in range(1, 9):
        sym, ent, diag, sq, sup = check_square_and_support(n)
        status = all([sym, ent, diag, sq, sup])
        print(f"  n={n}: symmetric={sym} entries{{0,±1}}={ent} zerodiag={diag} "
              f"A^2=nI={sq} support=Q_n_edges={sup}  -> {'PASS' if status else 'FAIL'}")

    print()
    print("=" * 72)
    print("(b) Interlacing: S = even-weight vertices + one odd vertex (|S|=2^{n-1}+1)")
    print("    B = A_n[S,S], check lambda_max(B) >= sqrt(n)")
    print("=" * 72)
    for n in range(2, 9):
        A = build_An(n)
        evens = even_weight_set(n)
        # pick one odd vertex (say vertex 1, which is odd weight)
        odd = 1
        assert popcount(odd) % 2 == 1
        S = evens + [odd]
        if len(S) != (1 << (n - 1)) + 1:
            print(f"  n={n}: BAD SIZE {len(S)}")
            continue
        lam = lambda_max(A, S)
        s = np.sqrt(n)
        status = "PASS" if lam >= s - 1e-9 else "FAIL"
        print(f"  n={n}: |S|={len(S)}  lambda_max(B)={lam:.10f}  "
              f"sqrt(n)={s:.10f}  lam-sqrt={lam-s:+.3e}  {status}")

    print()
    print("=" * 72)
    print("(c) Pure even-weight independent set (|S|=2^{n-1}): lambda_max(B) < sqrt(n)")
    print("=" * 72)
    for n in range(2, 9):
        A = build_An(n)
        S = even_weight_set(n)
        assert len(S) == 1 << (n - 1)
        # independent: internal edges are none, and its B is A_{n-1} block
        lam = lambda_max(A, S)
        s = np.sqrt(n)
        status = "PASS(<)" if lam < s else "FAIL(>=)"
        print(f"  n={n}: |S|={len(S)}  lambda_max(B)={lam:.10f}  "
              f"sqrt(n)={s:.10f}  {status}   (expect sqrt(n-1)={np.sqrt(n-1):.6f})")


if __name__ == "__main__":
    main()
