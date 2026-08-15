#!/usr/bin/env python3
"""Independent cross-check of the primitive-divisor claim for a sample of
(p, x): directly compute the multiplicative order of x mod the candidate
primitive divisor r, and confirm it is exactly p (so r ≡ 1 mod p and r is
primitive).  Also cross-check the mirror direction Phi_q(-y) = U_q(y-1,-y)
on small y.

This is a SECOND, independent route to the same value as the library helper:
the driver asserted order = p from (r | Phi_p(x) and r ∤ x-1); here we compute
the order directly by repeated multiplication mod r.  Exact integers only.
"""
from lib.lucas_prim import (primitive_prime_divisor,
                            primitive_prime_divisor_mirror)


def order_mod(a, r):
    """Multiplicative order of a mod r (r prime, gcd(a,r)=1), by direct
    repeated powering.  Returns the smallest k>=1 with a^k ≡ 1 (mod r)."""
    a %= r
    val = 1
    k = 0
    seen = set()
    while True:
        val = (val * a) % r
        k += 1
        if val == 1:
            return k


def cross_check_direct():
    XMAX = {3: 40, 5: 25, 7: 20, 11: 12, 13: 10}
    checked = 0
    bad = []
    for p in [3, 5, 7, 11, 13]:
        for x in range(2, XMAX[p] + 1):
            r, _ = primitive_prime_divisor(p, x)
            ord_r = order_mod(x, r)
            checked += 1
            if ord_r != p:
                bad.append((p, x, r, ord_r))
    return checked, bad


def cross_check_mirror():
    # Phi_q(-y) = (y^q+1)/(y+1); a primitive divisor s has (-y)^q ≡ 1 (mod s),
    # (-y)^k ≢ 1 for k<q, i.e. order of (-y) mod s exactly q.
    # Expect near-total existence but with small exceptions (e.g. q=3,y=2:
    # Phi_3(-2)=3, order of -2 mod 3 is 1 -> no primitive divisor).
    cases = []
    exceptions = []
    for q in [3, 5, 7]:
        for y in range(1, 30):
            s, _ = primitive_prime_divisor_mirror(q, y)
            if s is None:
                exceptions.append((q, y))
                continue
            o = order_mod(-y, s)
            if o != q:
                return False, f"order mismatch q={q} y={y} s={s} order={o}"
            cases.append((q, y, s, o))
    return True, (len(cases), exceptions)


if __name__ == "__main__":
    checked, bad = cross_check_direct()
    print("Direct-order cross-check of primitive divisor r | Phi_p(x):")
    print(f"  (p,x) checked: {checked}; order(x mod r) != p failures: {len(bad)}")
    print("  RESULT:", "PASS" if not bad else f"FAIL {bad}")

    print()
    ok, info = cross_check_mirror()
    if ok:
        n, ex = info
        print("Mirror primitive divisor Phi_q(-y) direct-order cross-check:")
        print(f"  cases with primitive divisor: {n}; exceptions (q,y) where "
              f"none exists: {ex}")
        print("  all primitive divisors have order(-y) = q -> RESULT: PASS")
    else:
        print("  mirror FAIL:", info)
