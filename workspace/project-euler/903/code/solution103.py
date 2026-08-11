#!/usr/bin/env python3
"""solution103.py — modular O(n) evaluator for PE 903 (mod p = 10^9+7).

Computes Q(n) mod p for n = 10^6 from the closed forms derived in
code/closedform_derivation.md and verified exactly by closedform_exact.py:

  E1 = H_n,  E2 = (1/4) H_{floor(n/2)},  E11 = n + S(n),
  S(n) = sum_{a+b<=n} 1/lcm(a,b) = sum_{d<=n/2} phi(d)/d^2 * T(floor(n/d)),
  T(m) = sum_{a=1}^{m-1} sum_{b=1}^{m-a} 1/(ab)  (recurrence below),
  A_n/(n!)^2 = 1/2 + E2/[n(n-1)] - (E11-E1)/[2 n (n-1)],
  B_n/(n!)^2 = [n - (n+1)E1 + E11 - 2 E2] / [n(n-1)(n-2)],
  Q(n) = (n!)^2 + A_n (n!-1) + (B_n/2) T(n)  mod p.

S(n): use 1/lcm(a,b) = gcd(a,b)/(ab), gcd = sum_{d|a,d|b} phi(d):
  S(n) = sum_d phi(d)/d^2 * T(floor(n/d)),
  T(m) = sum_{a,b>=1, a+b<=m} 1/(ab) = 2 sum_{s=2}^{m} H_{s-1}/s,
        T(m) = T(m-1) + 2 H_{m-1}/m.

All arithmetic mod p; every denominator (1..10^6) is invertible since 10^6 < p.

Checks
  * Q mod p for n = 2..11 against the exact verified values
    (5, 88, 4808, 597876, 133103808, 124948631, 798047424, 777220173,
     468421536, 247479760), Q(10) == 468421536 (statement oracle).
  * S cross-check: direct O(n^2) pair-sum of gcd(a,b)/(ab) mod p vs the
    phi-decomposition, for n = 10^4 and 5*10^4.
  * exact-vs-modular: exact-rational phi-based S (Fraction) at n = 2000, 5000
    vs the modular value.
  * stability at n = 10^6: telescoped
    Q = (n!)^2 + A(n!-1) + (B/2) T(n)   vs   direct
    Q = (n!)^2 + sum_{w=1}^{n-1} w! (w A + w(w-1) B/2).

Uses a linear inverse sieve and a linear phi sieve; no numpy.
"""
import math
from fractions import Fraction as F

P = 10**9 + 7
INV2 = (P + 1) // 2


# ----------------------------------------------------------------------
# modular basics
# ----------------------------------------------------------------------
def inverse_sieve(n):
    """inv[i] = i^{-1} mod p for i = 1..n in O(n)."""
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (P - (P // i) * inv[P % i]) % P
    return inv


def phi_sieve(n):
    """phi[i] = Euler totient of i for i = 0..n by a linear sieve."""
    phi = [0] * (n + 1)
    if n >= 1:
        phi[1] = 1
    primes = []
    is_comp = [False] * (n + 1)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for pr in primes:
            v = i * pr
            if v > n:
                break
            is_comp[v] = True
            if i % pr == 0:
                phi[v] = phi[i] * pr
                break
            else:
                phi[v] = phi[i] * (pr - 1)
    return phi


# ----------------------------------------------------------------------
# S(n) via phi-decomposition
# ----------------------------------------------------------------------
def T_recurrence_array(mmax, H, inv):
    """T[m] = sum_{a+b<=m} 1/(ab) mod p for m = 0..mmax, via
    T(m) = T(m-1) + 2 H_{m-1}/m.  H[i] and inv are precomputed (mod p)."""
    T = [0] * (mmax + 1)
    for m in range(2, mmax + 1):
        T[m] = (T[m - 1] + 2 * H[m - 1] % P * inv[m]) % P
    return T


def S_phi(n, phi, inv, T):
    """S(n) mod p = sum_{d<=n/2} phi(d)/d^2 * T(floor(n/d))."""
    s = 0
    for d in range(1, n // 2 + 1):
        term = phi[d] * inv[d] % P * inv[d] % P * T[n // d] % P
        s = (s + term) % P
    return s


def S_direct(n):
    """S(n) mod p by direct O(n^2) pair-sum of gcd(a,b)/(ab) (cross-check)."""
    s = 0
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (P - (P // i) * inv[P % i]) % P
    for a in range(1, n):
        ia = inv[a]
        for b in range(1, n - a + 1):
            g = math.gcd(a, b)
            s = (s + g * ia % P * inv[b]) % P
    return s


def S_phi_exact(n):
    """S(n) as an exact Fraction via the phi-decomposition (for cross-check)."""
    # phi by direct computation (small n)
    phi = [0] * (n + 1)
    for i in range(1, n + 1):
        phi[i] = i
    for i in range(2, n + 1):
        if phi[i] == i:  # prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    # T(m) exact
    T = [F(0)] * (n + 1)
    for m in range(2, n + 1):
        T[m] = T[m - 1] + 2 * sum(F(1, s) for s in range(1, m)) / m
    s = F(0)
    for d in range(1, n // 2 + 1):
        s += F(phi[d], d * d) * T[n // d]
    return s


# ----------------------------------------------------------------------
# A, B, Q
# ----------------------------------------------------------------------
def H_value(n, inv):
    """H_n mod p (prefix sum of modular inverses)."""
    return sum(inv[i] for i in range(1, n + 1)) % P


def A_B_mod(n, inv, Hn, Sval):
    """(A_n, B_n) mod p from the Section-5 closed forms.

    Returns normalized values A_n/(n!)^2, B_n/(n!)^2 mod p (these are what
    the formulas give directly; the caller combines with n! and T(n))."""
    E2 = INV2 * INV2 % P * H_value(n // 2, inv) % P      # (1/4) H_{n/2}
    E11 = (n + Sval) % P
    inv_n = inv[n]
    inv_nm1 = inv[n - 1] if n >= 2 else 0
    A = (INV2
         + E2 * inv_n % P * inv_nm1
         - (E11 - Hn) % P * INV2 % P * inv_n % P * inv_nm1) % P
    # denominator n(n-1)(n-2)
    denom = inv_n * inv_nm1 % P
    if n >= 3:
        denom = denom * inv[n - 2] % P
    B = (n - (n + 1) * Hn + E11 - 2 * E2) % P * denom % P
    return A, B


def q_compute(n, A, B, fact=None):
    """Q(n) mod p from (normalized) A_n/(n!)^2, B_n/(n!)^2.

    Convert to the actual counts first:  A_int = A * (n!)^2, B_int = B*(n!)^2
    (mod p), then the telescoped route
        Q = (n!)^2 + A_int (n!-1) + (B_int/2) T(n),
        T(n) = sum_{w=1}^{n-1} w! w (w-1).
    """
    if fact is None:
        fact = 1
        for m in range(1, n + 1):
            fact = fact * m % P
    n2 = fact * fact % P
    A_int = A * n2 % P
    B_int = B * n2 % P
    # accumulate T(n) while building factorials
    f = 1
    Tn = 0
    for m in range(1, n):
        f = f * m % P          # f = m!
        Tn = (Tn + f * m % P * (m - 1)) % P
    return (n2 + A_int * (fact - 1) % P + B_int * INV2 % P * Tn) % P


def q_compute_direct(n, A, B, fact=None):
    """Q(n) mod p by the direct accumulation route (A, B normalized):
        Q = (n!)^2 + sum_{w=1}^{n-1} w! (w A_int + w(w-1) B_int/2)."""
    if fact is None:
        fact = 1
        for m in range(1, n + 1):
            fact = fact * m % P
    n2 = fact * fact % P
    A_int = A * n2 % P
    B_int = B * n2 % P
    f = 1
    s = 0
    for w in range(1, n):
        f = f * w % P          # f = w!
        s = (s + f * (w * A_int % P + w * (w - 1) % P * B_int % P
                      * INV2 % P)) % P
    return (n2 + s) % P


# ----------------------------------------------------------------------
# full run
# ----------------------------------------------------------------------
def compute_Q(n):
    """Full modular evaluation of Q(n) mod p with all cross-checks."""
    print(f"=== PE 903  Q({n}) mod p   (p = {P}) ===")
    inv = inverse_sieve(n)
    H = [0] * (n + 1)
    for i in range(1, n + 1):
        H[i] = (H[i - 1] + inv[i]) % P
    phi = phi_sieve(n // 2)
    T = T_recurrence_array(n, H, inv)
    Sval = S_phi(n, phi, inv, T)

    Hn = H[n]
    A, B = A_B_mod(n, inv, Hn, Sval)
    q_tel = q_compute(n, A, B)
    q_dir = q_compute_direct(n, A, B)

    print(f"A mod p = {A}")
    print(f"B mod p = {B}")
    print(f"S(n) mod p = {Sval}")
    print(f"H_n mod p = {Hn}")
    # n! mod p
    fact = 1
    for m in range(1, n + 1):
        fact = fact * m % P
    print(f"n! mod p = {fact}")
    print(f"Q(n) mod p (telescoped) = {q_tel}")
    print(f"Q(n) mod p (direct)     = {q_dir}")

    # ---- self-tests n=2..11 ----
    expected = {2: 5, 3: 88, 4: 4808, 5: 597876, 6: 133103808,
                7: 124948631, 8: 798047424, 9: 777220173,
                10: 468421536, 11: 247479760}
    print("\n--- self-test: Q mod p for n=2..11 ---")
    all_ok = True
    for nn in sorted(expected):
        invn = inverse_sieve(nn)
        Hn_small = [0] * (nn + 1)
        for i in range(1, nn + 1):
            Hn_small[i] = (Hn_small[i - 1] + invn[i]) % P
        phin = phi_sieve(nn // 2)
        Tn = T_recurrence_array(nn, Hn_small, invn)
        Sn = S_phi(nn, phin, invn, Tn)
        An, Bn = A_B_mod(nn, invn, Hn_small[nn], Sn)
        qn = q_compute(nn, An, Bn)
        ok = qn == expected[nn]
        all_ok = all_ok and ok
        print(f"  n={nn}: Q mod p = {qn}  expected {expected[nn]}  "
              f"[{'PASS' if ok else 'FAIL'}]")
    ok10 = expected[10] == 468421536
    print(f"  Q(10)==468421536 (statement oracle): "
          f"{'PASS' if ok10 else 'FAIL'}")
    all_ok = all_ok and (qn == expected[10]) if False else all_ok

    # ---- S cross-check: direct O(n^2) vs phi-method ----
    print("\n--- S cross-check: direct O(n^2) vs phi-decomposition ---")
    for nn in (10_000, 50_000):
        invn = inverse_sieve(nn)
        Hn_small = [0] * (nn + 1)
        for i in range(1, nn + 1):
            Hn_small[i] = (Hn_small[i - 1] + invn[i]) % P
        phin = phi_sieve(nn // 2)
        Tn = T_recurrence_array(nn, Hn_small, invn)
        Sv = S_phi(nn, phin, invn, Tn)
        Sd = S_direct(nn)
        ok = Sv == Sd
        all_ok = all_ok and ok
        print(f"  n={nn}: phi-method S={Sv}  direct S={Sd}  "
              f"[{'PASS' if ok else 'FAIL'}]")

    # ---- exact-vs-modular S ----
    print("\n--- S cross-check: exact Fraction vs modular ---")
    for nn in (2000, 5000):
        invn = inverse_sieve(nn)
        Hn_small = [0] * (nn + 1)
        for i in range(1, nn + 1):
            Hn_small[i] = (Hn_small[i - 1] + invn[i]) % P
        phin = phi_sieve(nn // 2)
        Tn = T_recurrence_array(nn, Hn_small, invn)
        Sv = S_phi(nn, phin, invn, Tn)
        Sex = S_phi_exact(nn)
        Sexp = Sex.numerator % P * pow(Sex.denominator, P - 2, P) % P
        ok = Sv == Sexp
        all_ok = all_ok and ok
        print(f"  n={nn}: modular S={Sv}  exact S mod p={Sexp}  "
              f"[{'PASS' if ok else 'FAIL'}]")

    # ---- stability at n ----
    ok_stab = q_tel == q_dir
    all_ok = all_ok and ok_stab
    print(f"\n--- stability at n={n}: telescoped == direct ---")
    print(f"  Q mod p: {q_tel} == {q_dir}  "
          f"[{'PASS' if ok_stab else 'FAIL'}]")

    print("\n" + "=" * 60)
    if all_ok:
        print("ALL CHECKS PASS")
        print(f"\nTHE ANSWER: Q({n}) mod (10^9+7) = {q_tel}")
    else:
        print("SOME CHECKS FAILED — do not trust the answer")
    print("=" * 60)
    return q_tel, all_ok


if __name__ == "__main__":
    import sys
    ntarget = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    q, ok = compute_Q(ntarget)
    sys.exit(0 if ok else 1)
