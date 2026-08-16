#!/usr/bin/env python3
"""Reconcile the three nu2 routes to a single convention and confirm agreement.

The three routes in verify_brute.py differ by exactly ±1, which problem.md
warns about: "an earlier investigation lost a cycle to two conventions
disagreeing by exactly 1 on the degenerate cases." The two conventions:

  - unfloored (brute.py's nu2_matrix): depths d = 1..n-1, no suffix floor.
        This is what reproduces the parent's measurement cache (1976/4000).
  - floored-at-2 (canonical lib.rightdiag.cycle_and_nu2, per problem.md):
        depths d = 2..n-1.

Here I align every route to the SAME convention (floored at 2) so that all
three must agree exactly, and separately report brute.py's unfloored value to
confirm it matches the measurement cache.

Alignment: depth d in [2, n-1], fold cell T(n,d) = XOR over submasks o of d
of h[n-1-d+o], h[0]=0, h[j]=((q_{j+1}-q_j)/2) mod 2 for j>=1.
"""

from brute import nu2_matrix, w as w_brute
from lib.supply_fold import s_sos
import sympy
from sympy.ntheory.generate import primerange, prime


def primes_upto_index(n):
    return list(primerange(0, prime(n) + 1))[:n]


def h_odd(n):
    q = primes_upto_index(n + 1)
    return {j: ((q[j + 1] - q[j]) // 2) % 2 for j in range(1, n)}


def submasks(d):
    out, s = [], d
    while True:
        out.append(s)
        if s == 0:
            break
        s = (s - 1) & d
    return out


def nu2_direct_linear(n):
    """Floored-at-2: count d in [2,n-1] with T(n,d)=1, T via submask XOR of h."""
    h = h_odd(n)
    total = 0
    for d in range(2, n):
        x = 0
        for o in submasks(d):
            idx = n - 1 - d + o
            if 0 <= idx < n and idx in h:
                x ^= h[idx]
        total += x
    return total


def nu2_matrix_floor(n):
    """Literal Pascal matrix product, rows d = 2..n-1 (floored at 2)."""
    q = primes_upto_index(n + 1)
    h = [0] * n
    for j in range(1, n):
        h[j] = ((q[j + 1] - q[j]) // 2) % 2
    wt = 0
    for d in range(2, n):        # depth d; row index d-1 in Phi (d in 2..n-1)
        s = 0
        base = n - d
        for j in range(0, n):
            c = j - base
            if 0 <= c <= d - 1 and (c & (d - 1)) == c:
                s ^= h[j]
        wt += s
    return wt


def nu2_sos_floor(n):
    """SOS submask-zeta route, count of T=1 over d in [2,n-1]."""
    h = [0] * n
    for j, b in h_odd(n).items():
        h[j] = b
    S, ones = s_sos(n, h)
    return ones


def main():
    print("=== aligned to floored-at-2 (d = 2..n-1) ===")
    for n in [20, 50, 100, 200, 400]:
        a = nu2_direct_linear(n)
        b = nu2_matrix_floor(n)
        c = nu2_sos_floor(n)
        print(f"n={n}: direct={a} matrix={b} sos={c}  agree={a==b==c}")
        assert a == b == c, (n, a, b, c)

    print("\n=== brute.py unfloored (d = 1..n-1) vs floored ===")
    for n in [20, 50, 100, 200, 400]:
        u = nu2_matrix(n)            # unfloored, from brute
        f = nu2_matrix_floor(n)
        diff = u - f                 # exactly the d=1 cell, 0 or 1
        print(f"n={n}: brute(unfloored)={u}  floored={f}  diff={diff}  (d=1 cell, 0/1)")


if __name__ == "__main__":
    main()
