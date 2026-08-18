"""Extend the Fibonacci-boundary subsequence Psi(F_{n+1} - 1) far beyond the
stored residue table (which stops at k=400).

At k = |q_n| - 1 = F_{n+1} - 1 the k+1 distinct length-k factors are exactly
the cyclic windows of the standard word q_n (|q_n| = F_{n+1}, q_1='0',
q_2='01', q_{n+1}=q_n q_{n-1}).  We verify this identity at every boundary
point and compute Psi(k) mod M = 101001001 by the verified mechanical
construction (code/mech/mech_psi.py, A==B) for n = 2..18 (k up to F_19-1 =
4180), which is far beyond the stored 400.

Outputs code/out/boundary_psi_modM.txt (k, Psi mod M) and
code/out/boundary_psi_exact.txt (k, Psi exact), plus stdout verification.
"""
import sys

sys.path.insert(0, "code/mech")
sys.path.insert(0, "code")
from mech_psi import mech_psi  # noqa: E402

sys.set_int_max_str_digits(20000)
M = 101001001


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def std_word(n):
    if n == 1:
        return "0"
    if n == 2:
        return "01"
    return std_word(n - 1) + std_word(n - 2)


def val(w):
    return int(w) if w else 0


def cyclic_window_sum_sq(w):
    L = len(w)
    total = 0
    for s in range(L):
        cyc = w[s:] + w[:s]
        total += val(cyc[: L - 1]) ** 2
    return total


def main():
    rows = []
    print("n   |q_n|   k=|q_n|-1      Psi mod M       identity")
    for n in range(2, 19):
        q = std_word(n)
        k = len(q) - 1
        tA, tB, vA, vB = mech_psi(k)
        assert tA == tB
        cw = cyclic_window_sum_sq(q)
        ident = (cw == tA)
        rows.append((k, tA % M, tA))
        print(f"{n:2d}  {len(q):4d}   {k:6d}   {tA % M:9d}   {ident}")
        if not ident:
            print("  identity FAILED; stop")
            return
    with open("code/out/boundary_psi_modM.txt", "w") as fh:
        for k, r, _ in rows:
            fh.write(f"{k} {r}\n")
    with open("code/out/boundary_psi_exact.txt", "w") as fh:
        for k, _, ex in rows:
            fh.write(f"{k} {ex}\n")
    print("\nwrote code/out/boundary_psi_modM.txt and code/out/boundary_psi_exact.txt")


if __name__ == "__main__":
    main()
