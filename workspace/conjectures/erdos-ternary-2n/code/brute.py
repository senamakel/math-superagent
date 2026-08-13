#!/usr/bin/env python3
"""Naive oracle for the Erdos ternary conjecture on powers of two.

Exact integer arithmetic only. Obviously correct, deliberately not fast: it
exists to pin down what the statement means, checked against the worked
examples in problem.md (n = 0, 2, 8).

Objects:
    digit_free(m)   -- True iff the base-3 expansion of m avoids the digit 2.
    ternary(m)      -- base-3 representation of m as a string ("1_3"-style value).
    sieve(k)        -- the residue-class sieve A_k:
        A_k = { r mod 2*3^(k-1) : the low k ternary digits of (2^r mod 3^k)
               all lie in {0,1} }.
        Computed modulo 3**k via pow() so 2^n is never materialised.

The falsification oracle: every claimed obstruction must let r = n survive
for n in (0, 2, 8). sieve() reports which residue classes of r the three
witnesses occupy and whether those classes survive.
"""


def ternary(m):
    """Base-3 digits of m as a string; exact, no floats."""
    if m == 0:
        return "0"
    digits = []
    n = m
    while n > 0:
        n, d = divmod(n, 3)
        digits.append(str(d))
    return "".join(reversed(digits))


def digit_free(m):
    """True iff the base-3 expansion of m avoids the digit 2."""
    return "2" not in ternary(m)


def low_k_digits_free(x, k):
    """True iff the low k ternary digits of x all lie in {0, 1}.

    x is taken as already reduced mod 3**k (a plain integer 0 <= x < 3**k).
    """
    for _ in range(k):
        x, d = divmod(x, 3)
        if d == 2:
            return False
    return True


def sieve(k):
    """Return the ordered list of A_k (residue classes r mod 2*3^(k-1))."""
    mod = 3 ** k          # work modulo 3^k
    period = 2 * (3 ** (k - 1))  # order of 2 mod 3^k -> r reduces mod this
    out = []
    for r in range(period):
        x = pow(2, r, mod)          # 2^r mod 3^k, modular only
        if low_k_digits_free(x, k):
            out.append(r)
    return out


def main():
    print("=== digit_free on worked examples ===")
    # The three exceptions; all must be digit-2-free.
    for n in (0, 2, 8):
        m = 2 ** n
        print(f"  n={n}: 2^n={m:>5} ternary={ternary(m):>8} digit_free={digit_free(m)}")

    # A value known to contain a 2: 2^1=2="2_3", 2^3=8="22_3".
    for m in (2, 8, 2 ** 5):
        print(f"  m={m:>5} ternary={ternary(m):>8} digit_free={digit_free(m)}")

    print()
    print("=== sieve(k) with the three witnesses' residue classes ===")
    for k in range(1, 7):
        ak = sieve(k)
        # residue class of n=0: r=0. n=2: 2 mod period. n=8: 8 mod period.
        period = 2 * (3 ** (k - 1))
        survivors = set(ak)
        rows = []
        for n in (0, 2, 8):
            r = n % period
            rows.append(f"n={n}->r={r}: {'SURVIVES' if r in survivors else 'dies'}")
        print(f"  k={k}: |A_k|={len(ak):>4}  period={period:>4}  " + " | ".join(rows))

    print()
    print("=== |A_k| for k=1..8 (naive sieve, the experiment of problem.md) ===")
    for k in range(1, 9):
        ak = sieve(k)
        print(f"  k={k}: |A_k|={len(ak):>5}")


if __name__ == "__main__":
    main()
