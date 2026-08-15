#!/usr/bin/env python3
"""Exact (1-zeta_p)-adic valuation of x - zeta_p in Z[zeta_p], odd prime p.

Basis: {1, zeta, ..., zeta^{p-2}} with 1 + zeta + ... + zeta^{p-1} = 0, so
zeta^{p-1} = -(1 + zeta + ... + zeta^{p-2}).

Division rule (lambda = 1 - zeta):  alpha = sum_{j=0}^{p-2} a_j zeta^j is
divisible by lambda iff S = sum a_j == 0 (mod p); the quotient has
    b_j = (a_0 + ... + a_j) - (j+1) * S/p .   (*)
The valuation is the number of times we may divide by lambda.

Derivation of (*): writing alpha = (1-zeta)*sum b_j zeta^j and using
zeta^{p-1} = -(1+...+zeta^{p-2}) gives a_j = b_j - b_{j-1} + b_{p-2} for
j=1..p-2, a_0 = b_0 + b_{p-2}; solving with c = b_{p-2} yields
b_j = (a_0+...+a_j) - (j+1)c and S = p c.  Verified numerically below by
re-multiplying the quotient by (1-zeta).
"""

from math import isqrt


def odd_primes_upto(n):
    """All odd primes <= n."""
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = b"\x00" * len(sieve[i * i :: i])
    return [p for p in range(n + 1) if sieve[p] and p != 2]


def _times_one_minus_zeta(g, p):
    """Coefficients of (1-zeta)*g in the {1,...,zeta^{p-2}} basis.

    From zeta^{p-1} = -(1+...+zeta^{p-2}):
        zeta^0 coeff: g_0 + g_{p-2}
        zeta^j coeff: g_j - g_{j-1} + g_{p-2}.
    Used only to check that quotient * (1-zeta) == original.
    """
    c = g[-1]
    res = [g[0] + c]
    for j in range(1, p - 1):
        res.append(g[j] - g[j - 1] + c)
    return res


def v_lambda(coeffs, p, check_roundtrip=True):
    """(1-zeta_p)-adic valuation of alpha = sum coeffs[j] zeta^j (j=0..p-2).

    Iterative division by lambda = 1-zeta.  Returns the number of lambda
    factors dividing alpha.  coeffs is a length-(p-1) list of Python ints.
    O(p * v) time, O(p) space where v is the returned valuation.
    """
    a = list(coeffs)
    steps = 0
    while True:
        S = sum(a)
        if S % p != 0:
            return steps
        Sp = S // p
        run = 0
        b = []
        for j in range(p - 1):
            run += a[j]
            b.append(run - (j + 1) * Sp)
        if check_roundtrip:
            # quotient * lambda must reproduce the original coefficients
            if _times_one_minus_zeta(b, p) != a:
                raise AssertionError("division roundtrip failed")
        a = b
        steps += 1


def x_minus_zeta(x, p):
    """Coefficients of x - zeta_p in the {1,...,zeta^{p-2}} basis."""
    coeffs = [0] * (p - 1)
    coeffs[0] += x
    coeffs[1] -= 1
    return coeffs


def v_p(n, p):
    """p-adic valuation of integer n by exact division."""
    if n == 0:
        # 0 is divisible by every power of p: valuation is infinite.
        raise ValueError("v_p(0, p) is infinite; excluded from the identity check")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def main():
    primes = odd_primes_upto(61)
    XMAX = 200

    # Check 1: v_lambda(x-zeta) == 1  <=>  p | (x-1)
    failures1 = []
    exemplars1 = []
    for p in primes:
        for x in range(1, XMAX + 1):
            v = v_lambda(x_minus_zeta(x, p), p)
            cond = ((x - 1) % p == 0)
            want = 1 if cond else 0
            if v != want:
                failures1.append((p, x, v, want))
            if len(exemplars1) < 6:
                exemplars1.append((p, x, v, want))
    status1 = "PASS" if not failures1 else "FAIL"

    # Check 2: exact-integer v_p(x^p - 1) == v_p(x-1) + [p | (x-1)]
    failures2 = []
    exemplars2 = []
    for p in primes:
        for x in range(2, XMAX + 1):  # x=1 gives x^p-1=0, valuation infinite on both sides
            lhs = v_p(x ** p - 1, p)
            rhs = v_p(x - 1, p) + (1 if (x - 1) % p == 0 else 0)
            if lhs != rhs:
                failures2.append((p, x, lhs, rhs))
            if len(exemplars2) < 6:
                exemplars2.append((p, x, lhs, rhs))
    status2 = "PASS" if not failures2 else "FAIL"

    print(f"== v_lambda(x-zeta)==1 iff p|(x-1), p in {primes}, x in 1..{XMAX} ==")
    print(f"RESULT: {status1}  ({len(failures1)} failures)")
    print("exemplar rows (p, x, v_lambda, expected):")
    for row in exemplars1:
        print("   ", row)
    if failures1:
        print("first failures:")
        for row in failures1[:10]:
            print("   ", row)

    print()
    print("== exact v_p(x^p-1) == v_p(x-1) + [p|(x-1)] ==")
    print(f"RESULT: {status2}  ({len(failures2)} failures)")
    print("exemplar rows (p, x, LHS, RHS):")
    for row in exemplars2:
        print("   ", row)
    if failures2:
        print("first failures:")
        for row in failures2[:10]:
            print("   ", row)

    overall = "PASS" if (status1 == "PASS" and status2 == "PASS") else "FAIL"
    print()
    print(f"OVERALL: {overall}")


if __name__ == "__main__":
    main()
