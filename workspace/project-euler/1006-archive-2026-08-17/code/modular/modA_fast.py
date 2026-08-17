"""TASK A (fast, prime case): modular structure of M=101001001.

Established in this run: M is prime (trial division to sqrt(M)=10049),
M-1 = 2^3 * 3 * 5^3 * 131 * 257, and 5 is a quadratic residue mod M
(legendre_symbol(5,M)=1).

Because 5 is a quadratic residue mod prime M, the Pisano period pi(M) divides
M-1 (a classical result: the Fibonacci period mod p divides p-1 when 5 is a
QR mod p, and p+... when 5 is a QNR). We verify the divisibility and find the
exact period by the standard divisor-reduction:

  ord_10(M): starts at phi(M)=M-1, divides out prime-power factors of phi(M)
             while 10^d == 1 mod M still holds. (Cheap: pow with exponents
             that are divisors of phi(M).)
  pi(M):     starts at a known multiple (M-1), divides out prime factors while
             F_d = 0 and F_{d+1} = 1 mod M still holds. Here we use matrix
             exponentiation / fast doubling of Fibonacci mod M, costing
             O(log d) multiplications per candidate d.

All exact integer arithmetic.
"""

import math
import sympy
from sympy.ntheory import legendre_symbol

MOD = 101001001


def factor_int(n):
    return {int(p): int(e) for p, e in sympy.factorint(n).items()}


def fib_pair_mod(m, n):
    """(F_n mod m, F_{n+1} mod m) by matrix fast-doubling."""
    if n == 0:
        return (0, 1)
    a, b = fib_pair_mod(m, n >> 1)  # a=F_k, b=F_{k+1}, k=n//2
    c = a * ((2 * b - a) % m) % m          # F_{2k}
    d = (a * a + b * b) % m                # F_{2k+1}
    if n & 1:
        return (d, (c + d) % m)
    return (c, d)


def fib_mod(m, n):
    return fib_pair_mod(m, n)[0]


def ordinal_10(M):
    """Multiplicative order of 10 mod prime M."""
    phi = M - 1
    d = phi
    for p, e in factor_int(phi).items():
        for _ in range(e):
            if pow(10, d // p, M) == 1:
                d //= p
    return d


def pisano_period_prime(M):
    """Pisano period mod prime M, using that it divides M-1 (5 is QR)."""
    # start from M-1
    d = M - 1
    # check that M-1 really is a period
    assert fib_mod(M, d) == 0 and fib_mod(M, d + 1) == 1, "M-1 not a period?!"
    for p, e in factor_int(M - 1).items():
        for _ in range(e):
            if fib_mod(M, d // p) == 0 and fib_mod(M, d // p + 1) == 1:
                d //= p
    return d


def main():
    M = MOD
    out = []
    isprime = sympy.isprime(M)
    out.append(f"M = {M}")
    out.append(f"isprime(M) = {isprime}")
    out.append(f"M-1 = {M-1} = " + " * ".join(f"{p}^{e}" for p, e in sorted(factor_int(M-1).items())))
    out.append(f"legendre_symbol(5, M) = {legendre_symbol(5, M)}  (=> pi(M) divides M-1)")

    out.append("")
    o10 = ordinal_10(M)
    out.append(f"ord_10(M) = {o10}")
    out.append(f"  check 10^{o10} mod M == 1 : {pow(10, o10, M) == 1}")
    out.append(f"  (divides M-1={M-1}: {(M-1) % o10 == 0})")

    out.append("")
    piM = pisano_period_prime(M)
    out.append(f"Pisano period pi(M) = {piM}")
    # verify
    ok = (fib_mod(M, piM) == 0 and fib_mod(M, piM + 1) == 1)
    out.append(f"  check F_{piM} mod M == 0 and F_{piM+1} mod M == 1 : {ok}")
    out.append(f"  (divides M-1={M-1}: {(M-1) % piM == 0})")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_A.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
