"""Exact no-low-order-recurrence check for H, Phi, A063985 over 300 terms.

For each order d in 1..12: build the (L-d) x (d+1) Toeplitz system whose rows
are (a_i, ..., a_{i+d}); by exact rational elimination (sympy) check whether a
null vector with nonzero last entry exists.  If yes, extract the integer
recurrence and test it against the ENTIRE remaining prefix (n up to 200000):
a candidate that fits the 300-term block but fails anywhere in the tail is not
a recurrence of the sequence.
"""
import numpy as np
from sympy import Matrix, Rational


def main():
    N = 200_000
    L = 300
    H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
    Phi = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)
    A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
    for name, T in (("H", H), ("Phi", Phi), ("A063985", A)):
        found = None
        for d in range(1, 13):
            rows = np.array([T[i:i + d + 1] for i in range(L - d)])
            S = Matrix([[Rational(int(x)) for x in rows[i, :].tolist()]
                        for i in range(rows.shape[0])])
            ns = S.nullspace()
            cand = [v for v in ns if v[d] != 0]
            if cand:
                v = cand[0]
                coeffs = [int(-Rational(v[j]) / v[d]) for j in range(d)]
                tail_ok, first_fail = True, None
                for n in range(d, N):
                    pred = sum(coeffs[j] * T[n - 1 - j] for j in range(d))
                    if pred != T[n]:
                        tail_ok, first_fail = False, n + 1
                        break
                print(f"{name}: order-{d} recurrence fits first {L} terms; "
                      f"tail (up to n={N}): {'OK' if tail_ok else f'FAILS first at n={first_fail}'}")
                found = d
                break
        if found is None:
            print(f"{name}: no constant-coefficient recurrence of order <= 12 "
                  f"fits the first {L} terms (exact rank check)")
    return 0


if __name__ == "__main__":
    main()
