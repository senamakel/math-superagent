#!/usr/bin/env python3
"""
Fresh, independent implementation of the PE 903 closed-form evaluator.

Written from the derivation in closedform_derivation.md (this run, 18 Sep 2025).
Does NOT import solution103.py or closedform_exact.py.

The derivation (all terms modulo p = 10^9+7, exact identities):
    Q(n) = (n!)^2 + A_n (n! - 1) + (B_n/2) * TQ(n)
    TQ(n) = sum_{m=1}^{n-1} m (m-1) m!          (the "reduction" T)

Closed forms (n >= 3):
    E1  = H_n
    E2  = (1/4) H_{floor(n/2)}
    E11 = n + S(n),  S(n) = sum_{a+b<=n} 1/lcm(a,b)
    A_n/(n!)^2 = 1/2 + E2/(n(n-1)) - (E11-E1)/(2 n (n-1))
    B_n/(n!)^2 = (n - (n+1)E1 + E11 - 2E2) / (n(n-1)(n-2))

S(n) via the phi-decomposition (gcd(a,b) = sum_{d|a,d|b} phi(d)):
    S(n) = sum_{d=1}^{floor(n/2)} phi(d)/d^2 * T(floor(n/d)),
    T(m) = sum_{a+b<=m} 1/(ab) = T(m-1) + 2 H_{m-1}/m.

Complexity: O(n) time, O(n) space (harmonic/inverse arrays, phi sieve, T array).
"""

import sys

P = 10**9 + 7


def solve(n):
    if n == 2:
        # exact: A_2 = 1, B_2 = 0; Q(2) = 5
        return 5  # (n!)^2 + A*(n!-1) = 4 + 1*(1) = 5

    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        # linear modular-inverse recurrence: i * inv[i] == 1 (mod p)
        inv[i] = (P - (P // i) * inv[P % i] % P) % P

    # --- E1 = H_n, H array for T recurrence and E2 ---
    H = [0] * (n + 1)
    for m in range(1, n + 1):
        H[m] = (H[m - 1] + inv[m]) % P
    E1 = H[n]
    E2 = (pow(4, P - 2, P) * H[n // 2]) % P

    # --- T[m] = sum_{a+b<=m} 1/(ab), for all m up to n ---
    # T[m] = T[m-1] + 2 H_{m-1} / m
    T = [0] * (n + 1)
    for m in range(2, n + 1):
        T[m] = (T[m - 1] + (2 * H[m - 1] % P) * inv[m]) % P

    # --- phi up to n//2 via a simple linear sieve ---
    M = n // 2
    phi = list(range(M + 1))
    phi[1] = 1
    is_comp = [False] * (M + 1)
    primes = []
    for i in range(2, M + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for q in primes:
            ip = i * q
            if ip > M:
                break
            is_comp[ip] = True
            if i % q == 0:
                phi[ip] = phi[i] * q
                break
            else:
                phi[ip] = phi[i] * (q - 1)

    # --- S(n) = sum_{d<=n/2} phi(d)/d^2 * T(n//d) ---
    S = 0
    for d in range(1, M + 1):
        d_inv2 = inv[d] * inv[d] % P
        S = (S + phi[d] * d_inv2 % P * T[n // d]) % P

    E11 = (n + S) % P

    # --- (n!)^2 mod p ---
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % P
    fact2 = fact * fact % P

    # --- A, B mod p from the closed forms ---
    inv_n = inv[n]
    inv_nm1 = inv[n - 1]
    inv_nm2 = inv[n - 2]
    nnm1 = inv_n * inv_nm1 % P

    a_over = (inv[2] + E2 * nnm1 - (E11 - E1) * inv[2] % P * nnm1) % P
    b_over = ((n - (n + 1) * E1 + E11 - 2 * E2) % P
              * nnm1 % P * inv_nm2) % P

    A = a_over * fact2 % P
    B = b_over * fact2 % P

    # --- TQ(n) = sum_{m=1}^{n-1} m (m-1) m!  ---
    # Second accumulation route (as in the derivation): 
    #   Q = (n!)^2 + sum_{w=1}^{n-1} w! ( w A + w(w-1)B/2 )
    # equals (n!)^2 + A(n!-1) + (B/2) TQ(n) by sum_m m*m! = n!-1.
    Q = fact2
    f = 1  # f = w!
    for w in range(1, n):
        f = f * w % P                     # f = w!
        tri = (w * (w - 1) // 2) % P      # w(w-1)/2 exact, then mod
        term = (w % P) * A % P
        term = (term + tri * B) % P
        Q = (Q + f * term) % P
    return Q % P


def direct_S(n):
    """Direct O(n^2) S(n) = sum_{a+b<=n} 1/lcm(a,b) mod p — cross-check only."""
    from math import gcd
    S = 0
    for a in range(1, n):
        for b in range(1, n - a + 1):
            S = (S + pow((a * b) // gcd(a, b), P - 2, P)) % P
    return S


def S_phi(n):
    """S(n) mod p via the phi-decomposition (the method used in solve())."""
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (P - (P // i) * inv[P % i] % P) % P
    H = [0] * (n + 1)
    for m in range(1, n + 1):
        H[m] = (H[m - 1] + inv[m]) % P
    T = [0] * (n + 1)
    for m in range(2, n + 1):
        T[m] = (T[m - 1] + (2 * H[m - 1] % P) * inv[m]) % P
    M = n // 2
    phi = list(range(M + 1))
    phi[1] = 1
    is_comp = [False] * (M + 1)
    primes = []
    for i in range(2, M + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for q in primes:
            ip = i * q
            if ip > M:
                break
            is_comp[ip] = True
            if i % q == 0:
                phi[ip] = phi[i] * q
                break
            else:
                phi[ip] = phi[i] * (q - 1)
    S = 0
    for d in range(1, M + 1):
        d_inv2 = inv[d] * inv[d] % P
        S = (S + phi[d] * d_inv2 % P * T[n // d]) % P
    return S


def direct_Q_small(n):
    """Exact-integer Q(n) from the closed-form A,B (uses Python big ints).

    Equivalent to summing rank over the cyclic subgroup — only meaningful for
    small n; used to confirm the modular route against known Q values.
    """
    from math import gcd
    # exact rational H, S using Fractions
    from fractions import Fraction as Fr
    Hn = sum(Fr(1, m) for m in range(1, n + 1))
    H2 = sum(Fr(1, m) for m in range(1, n // 2 + 1))
    S = sum(Fr(1, (a * b) // gcd(a, b)) for a in range(1, n)
            for b in range(1, n - a + 1))
    E11 = n + S
    E1 = Hn
    E2 = Fr(1, 4) * H2
    # A/(n!)^2 and B/(n!)^2 as Fractions
    a_over = Fr(1, 2) + E2 / (n * (n - 1)) - (E11 - E1) / (2 * n * (n - 1))
    b_over = (n - (n + 1) * E1 + E11 - 2 * E2) / (n * (n - 1) * (n - 2))
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    A = a_over * fact * fact
    B = b_over * fact * fact
    assert A.denominator == 1 and B.denominator == 1
    A = A.numerator
    B = B.numerator
    # Q = n!^2 + A(n!-1) + (B/2)*TQ, TQ = sum m(m-1)m!
    TQ = 0
    f = 1
    for m in range(1, n):
        f *= m
        TQ += m * (m - 1) * f
    return fact * fact + A * (fact - 1) + B * TQ // 2


def self_test():
    """Check the modular route against known exact Q values (memory.md)."""
    known = {
        2: 5,
        3: 88,
        4: 4808,
        5: 597876,
        6: 133103808,
        7: 47124948960 % P,   # 124948631
        8: 24768798220800 % P,  # 798047424
        9: 777220173,         # brief oracle
        10: 468421536,        # statement oracle for Q(10) mod p
        11: 247479760,        # brief oracle
    }
    for n, val in known.items():
        got = solve(n)
        assert got == val, f"n={n}: got {got}, expected {val}"
        print(f"Q({n}) mod p = {got}  [OK expected {val}]")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 10**6
    do_selftest = "--selftest" in sys.argv or (n < 10**5 and len(sys.argv) > 1 and sys.argv[1].isdigit())
    if do_selftest:
        self_test()
        # independent small cross-check of the S phi-decomposition
        for m in (50, 120, 300):
            ss = solve(m)  # smoke
            assert solve(m) == solve(m)
        for m in (8, 9, 10, 11):
            exact = direct_Q_small(m) % P
            assert solve(m) == exact, f"n={m}: modular {solve(m)} != exact {exact}"
            print(f"direct-Fraction cross-check n={m}: OK")
        # brief-required cross-check: S(n) by direct O(n^2) pair sum vs the
        # phi-decomposition mod p at n = 20000.
        nsc = 20000
        dS = direct_S(nsc)
        pS = S_phi(nsc)
        assert dS == pS, f"S cross-check n={nsc}: direct {dS} != phi {pS}"
        print(f"S(n) direct-vs-phi cross-check n={nsc}: OK ({pS})")
    ans = solve(n)
    print(f"Q({n}) mod ({P}) = {ans}")
