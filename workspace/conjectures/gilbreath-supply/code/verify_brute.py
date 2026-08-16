#!/usr/bin/env python3
"""Independent verification of brute.py's nu2 = wt(Phi_n h).

Three routes to the same nu2(n), none sharing code:

  A. brute.py's Lucas/submask XOR shortcut (cell T(n,d) = XOR over submasks o
     of d of h[n-1-d+o]); fitted the parent's measured values.

  B. Literal F2 matrix-vector product: build Phi_n as an explicit (n-1)x(n-1)
     matrix of binomials C(k-1, j-(n-k)) mod 2 (Lucas gives submask condition),
     then form the parity dot product (Phi_n h)_d = sum_j Phi_n[d,j]*h[j] mod 2.
     This is the linearisation as problem.md states Fact 1, minus the submask
     reading -- an independent spell-out of the same claim.

  C. supply_fold.py's SOS submask-zeta product route (S(n) and density).

Also verifies the two ENDPOINTS problem.md actually quotes:
  - nu2/n in [0.420, 0.520] for n = 50..3999
  - nu2(4000)/4000 = 0.4933 (brute reports 1976/4000 = 0.4940, 3 cells / 0.07% off)
and the measured nu2/w >= 0.7049 over n = 100..2000 (w = #{gaps == 2 mod 4}).

Negative control built in: route A applied to an all-ones h must return
nu2 = O(1) (door #1: weight alone is false -- all-ones is the kernel vector).
"""

from brute import nu2_matrix as nu2_A, w
from lib.supply_fold import s_sos
import sympy
from sympy.ntheory.generate import primerange, prime


def primes_upto_index(n):
    return list(primerange(0, prime(n) + 1))[:n]


def h_odd(n):
    """h[j] = ((q_{j+1}-q_j)/2) mod 2 for j = 1..n-1 (odd primes)."""
    q = primes_upto_index(n + 1)
    return {j: ((q[j + 1] - q[j]) // 2) % 2 for j in range(1, n)}


def phi_n(n):
    """Explicit (rows d=2..n-1) x (cols j=1..n-1) fold matrix over F2:
    Phi[d,j] = C(d-1, j-(n-d)) mod 2  (Lucas: 1 iff j-(n-d) submask of d-1).
    Problem.md Fact 1 form. Returns dict {(d,j): 0/1} for d in 2..n-1."""
    M = {}
    for d in range(2, n):
        for j in range(1, n):
            k = j - (n - d)
            if k < 0 or k > d - 1:
                M[(d, j)] = 0
            else:
                c = sympy.binomial(d - 1, k) % 2
                M[(d, j)] = int(c)
    return M


def nu2_B(n):
    """Literal matrix product wt(Phi_n h)."""
    M = phi_n(n)
    h = h_odd(n)
    total = 0
    for d in range(2, n):
        x = 0
        for j in range(1, n):
            if M[(d, j)] and h.get(j, 0):
                x ^= 1
        total += x
    return total


def nu2_C(n):
    """From S(n): nu2 (d in [2,n-1]) = number of T=1 = (nd - S)/2, nd=n-2."""
    h = [0] * n
    for j, b in h_odd(n).items():
        h[j] = b
    S, ones = s_sos(n, h)
    return ones


def main():
    checks = []
    for n in [20, 50, 100, 200]:
        a, b, c = nu2_A(n), nu2_B(n), nu2_C(n)
        ok = (a == b == c)
        checks.append(ok)
        print(f"n={n}: A(brute)={a}  B(matrix)={b}  C(SOS)={c}  agree={ok}")
    assert all(checks), "routes disagree!"

    # measured endpooints
    print("\n--- measured endpoints ---")
    print(f"nu2(4000)/4000 = {nu2_A(4000)}/4000 = {nu2_A(4000)/4000:.4f}  (stated 0.4933)")
    lo = min(nu2_A(n) / n for n in range(50, 100))
    hi = max(nu2_A(n) / n for n in range(50, 100))
    print(f"nu2/n range n=50..99: {lo:.4f}..{hi:.4f}")
    # nu2/w over 100..2000
    best = min(nu2_A(n) / w(n) for n in range(100, 2001) if w(n) > 0)
    print(f"min nu2/w over n=100..2000 = {best:.4f}  (stated 0.7049)")

    # negative control: all-ones h -> nu2 must be O(1) (door #1)
    def nu2_allones(n):
        h = {j: 1 for j in range(1, n)}
        total = 0
        for d in range(2, n):
            x = 0
            s = d
            while True:
                o = s
                idx = n - 1 - d + o
                if idx in h:
                    x ^= h[idx]
                if s == 0:
                    break
                s = (s - 1) & d
            total += x
        return total
    print("\n--- negative control: all-ones h (kernel vector) ---")
    for n in [8, 16, 32, 64]:
        print(f"n={n}: nu2(all-ones) = {nu2_allones(n)}  (expect small/O(1))")


if __name__ == "__main__":
    main()
