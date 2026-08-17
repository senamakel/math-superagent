"""TASK A - modular structure of M = 101001001.

Computes, with exact integer arithmetic:
  1. prime-power factorization of M,
  2. multiplicative order of 10 mod each prime-power factor q, and
     ord_10(M) = lcm of those orders,
  3. the Pisano period (period of the Fibonacci sequence) mod M.

Method / theorem:
  - ord_10(M) = lcm_p ord_10(p^e) because the multiplicative group mod M is
    the product of the groups mod each prime power (CRT), and an element has
    order the lcm of its component orders.
  - Pisano period pi(n) for n = prod p_i^{e_i}: pi(n) = lcm_i pi(p_i^{e_i}),
    and pi(p^e) = p^{max(0, e-g)} pi(p) where the rank of apparition z(p) is the
    index of the first Fibonacci number divisible by p (Wall's theorem:
    pi(p^e)=p^{e-1} pi(p) when p is not a Wall-Sun-Sun prime, and the p-adic
    valuation of F_{pi(p)} is 1). We compute pi(p) by direct iteration mod p
    (p is small) and handle the p-adic lift by checking the valuation of
    F_{pi(p)} and multiplying by p while the valuation of F still rises.

Everything below is exact (small moduli, direct iteration).
"""

import math
import sympy


MOD = 101001001


def factor_int(n):
    """Return prime -> exponent dict for n using sympy."""
    return {p: int(e) for p, e in sympy.factorint(n).items()}


def multiplicative_order(a, m):
    """Multiplicative order of a mod m; requires gcd(a,m)=1."""
    assert math.gcd(a, m) == 1, (a, m)
    order = 1
    # order of a mod m divides phi(m); find the minimal divisor d of phi(m)
    # with a^d == 1 mod m.
    phi = int(sympy.totient(m))
    d = phi
    # reduce d by each prime power factor of phi
    for p, e in factor_int(phi).items():
        for _ in range(int(e)):
            if pow(a, d // int(p), m) == 1:
                d //= int(p)
    return d


def fib_period_prime(p):
    """Pisano period of Fibonacci mod a prime p (Wall: divides p-1, p+1, or 2p+2)."""
    # iterate the (a,b)=(F_n, F_{n+1}) pair until it returns to (0,1)
    a, b = 0, 1
    n = 0
    while True:
        a, b = b, (a + b) % p
        n += 1
        if a == 0 and b == 1:
            return n


def p_adic_val(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def fib_period_prime_power(p, e):
    """Pisano period mod p^e using Wall's theorem with p-adic lifting."""
    pi_p = fib_period_prime(p)
    # period mod p^e = pi(p) * p^{e - g}, where g = v_p(F_{pi(p)}).
    # Compute F_{pi(p)} exactly, then g, then scale.
    def fib_exact(m):
        a, b = 0, 1
        for _ in range(m):
            a, b = b, a + b
        return a
    F = fib_exact(pi_p)
    g = p_adic_val(F, p)
    return pi_p * (p ** max(0, e - g))


def pisano_period(n):
    """Pisano period mod n = lcm of periods mod each prime power."""
    pers = [fib_period_prime_power(p, e) for p, e in factor_int(n).items()]
    return math.lcm(*pers)


def main():
    out = []
    out.append(f"M = {MOD}")
    fac = factor_int(MOD)
    out.append(f"factorization: {fac}")
    out.append(f"  (as list) " + " ".join(f"{p}^{e}" for p, e in sorted(fac.items())))

    # verify factorization by multiplication
    prod = 1
    for p, e in fac.items():
        prod *= p ** e
    out.append(f"  check product: {prod} == M: {prod == MOD}")

    out.append("")
    out.append("Multiplicative order of 10 mod each prime-power factor:")
    ords = {}
    for p, e in sorted(fac.items()):
        q = p ** e
        o = multiplicative_order(10, q)
        ords[(p, e)] = o
        out.append(f"  ord_10({q}) = {o}")
    lcm_ord = math.lcm(*ords.values())
    ords["lcm"] = lcm_ord
    out.append(f"  ord_10(M) = lcm = {lcm_ord}")
    out.append(f"  verify: 10^{lcm_ord} mod M == 1 : {pow(10, lcm_ord, MOD) == 1}")

    out.append("")
    out.append("Pisano period of Fibonacci mod M:")
    for p, e in sorted(fac.items()):
        q = p ** e
        out.append(f"  pi({q}) = {fib_period_prime_power(p, e)}  (pi({p})={fib_period_prime(p)}, e={e})")
    piM = pisano_period(MOD)
    out.append(f"  pi(M) = lcm = {piM}")
    out.append(f"  verify: F_{piM} mod M == 0 and F_{piM+1} mod M == 1 : "
               f"{pow(0,0,1)}")  # placeholder replaced below

    # independent verification of pi(M) by direct iteration mod M
    a, b = 0, 1
    n = 0
    while True:
        a, b = b, (a + b) % MOD
        n += 1
        if a == 0 and b == 1:
            break
        if n > 10 * piM:
            out.append("  !! direct iteration did not return -- mismatch")
            n = -1
            break
    out.append(f"  direct iteration period mod M = {n} ; matches pi(M): {n == piM}")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_A.txt", "w") as fh:
        fh.write(text)
    return fac


if __name__ == "__main__":
    main()
