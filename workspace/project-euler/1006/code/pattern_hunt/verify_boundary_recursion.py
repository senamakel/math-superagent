"""Verify the exact second-order recursion in n for the boundary subsequence

    Psi_n := Psi( F_{n+2} - 1 )        (windows of the Fibonacci word S_n, length |S_n| = F_{n+2})

derived from the word recursion S_{n+1} = S_n S_{n-1}:

  Psi_{n+1} = 10^{2|S_{n-1}|} * Psi_n
            + 2 * 10^{|S_{n-1}|}   * val(S_{n-1}) * M1(F_{n+2}-1)
            + |S_n|               * val(S_{n-1})^2
            + |S_{n-1}| * 10^{2|S_{n-1}|-2} * val(S_n)^2
            + 2 * 10^{|S_{n-1}|-1} * val(S_n)   * M1(F_{n+1}-1)
            + Psi_{n-1}

with M1(k) = c1(k) * R(k)  (c1(k)=1+floor(k/phi^2), R(k)=repunit of length k,
                            position-balance conjecture, itself verified at these k).

The right-hand side uses only Psi_n, Psi_{n-1}, val(S_n), val(S_{n-1}), and the
Fibonacci lengths; iterating it computes the whole boundary subsequence in O(n)
big-integer steps.

Oracle: exact Psi(F_m - 1) from code/mech/mech_psi.py (mechanical construction,
formulation A == B, itself verified against brute and recorded tables).
"""
from fractions import Fraction
import sys

sys.path.insert(0, "code/mech")
sys.path.insert(0, "code")
from mech_psi import mech_psi  # noqa: E402


def fibs_upto(limit):
    f = [0, 1]
    while f[-1] <= limit:
        f.append(f[-1] + f[-2])
    return f


def fibonacci_word(n):
    """S_0 = "0", S_1 = "01", S_n = S_{n-1} S_{n-2}."""
    words = ["0", "01"]
    for i in range(2, n + 1):
        words.append(words[i - 1] + words[i - 2])
    return words[n]


def val(w):
    return int(w) if w else 0


def c1(k):
    # 1 + floor(k / phi^2), phi^2 = (3 + sqrt5)/2  ->  1/phi^2 = (3 - sqrt5)/2
    # exact integer computation: floor(k * (3 - sqrt5)/2)
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    import math
    phi2 = (3 + math.sqrt(5)) / 2
    return 1 + int(k / phi2)


def repunit(k):
    return (10 ** k - 1) // 9


def M1(k):
    return c1(k) * repunit(k)


def main():
    n_max = 10  # S_10, length F_12 = 144  ->  k = 143

    # Fibonacci lengths: |S_n| = F_{n+2} with F_0=0,F_1=1,F_2=1,F_3=2,...
    F = fibs_upto(200)

    # Oracle boundary values
    print("n  |S_n|  k=F-1          Psi(k) exact")
    oracle = {}
    for n in range(0, n_max + 1):
        k = F[n + 2] - 1
        tA, tB, vA, vB = mech_psi(k)
        assert tA == tB
        oracle[n] = tA
        print(f"{n:2d}  {F[n+2]:4d}  {k:4d}  {tA}")

    # word values
    W = {}
    for n in range(0, n_max + 1):
        W[n] = val(fibonacci_word(n))

    # Recursion:  Psi_{n+1} = ...(Psi_n, Psi_{n-1}, W[n], W[n-1], F...)
    rec = {0: oracle[0], 1: oracle[1]}
    print("\nn  rec(n) == oracle(n)")
    ok_all = True
    for n in range(1, n_max):
        # compute Psi_{n+1} from Psi_n, Psi_{n-1}
        s_prev = F[n + 1]        # |S_{n-1}| = F_{n+1}
        s_cur = F[n + 2]         # |S_n|
        B = W[n - 1]             # val(S_{n-1})
        C = W[n]                 # val(S_n)
        k_n = F[n + 2] - 1       # window length in S_n
        k_nm1 = F[n + 1] - 1     # window length in S_{n-1}
        Psi_next = (
            10 ** (2 * s_prev) * rec[n]
            + 2 * 10 ** s_prev * B * M1(k_n)
            + s_cur * B * B
            + s_prev * 10 ** (2 * s_prev - 2) * C * C
            + 2 * 10 ** (s_prev - 1) * C * M1(k_nm1)
            + rec[n - 1]
        )
        rec[n + 1] = Psi_next
        good = (Psi_next == oracle[n + 1])
        ok_all = ok_all and good
        print(f"{n+1:2d}  {'OK' if good else 'MISMATCH'}  rec={Psi_next}")

    print("\nRECURSION HOLDS for all n = 0..%d: %s" % (n_max, ok_all))


if __name__ == "__main__":
    main()
