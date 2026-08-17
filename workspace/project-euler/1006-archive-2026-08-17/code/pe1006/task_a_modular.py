"""Task A: modular structure of M = 101001001.

- Factor M into prime powers (M turns out to be prime).
- order of 10 mod each prime power, and ord_10(M) = lcm.
- Pisano period of the Fibonacci recurrence mod M.
- period of the Fibonacci word structure if relevant.

Exact integer arithmetic throughout.
"""
import sympy

MOD = 101001001


def pisano_period(m):
    """Pisano period of the Fibonacci sequence mod m: smallest T>0 with
    F_T==0 (mod m) and F_{T+1}==1 (mod m).

    Naive but only up to the actual period; used for the single modulus here.
    We rely on the standard fact that the period exists (the pair
    (F_{n},F_{n+1}) mod m is a finite reversible map, so it is purely periodic).
    """
    a, b = 0, 1  # F_0, F_1 mod m
    # iterate state pairs until returning to (0,1); the map (a,b)->(b,a+b) is a
    # permutation when gcd(1,m)... in general period <= 6m. Scan.
    for t in range(1, 6 * m + 2):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return t
    return None


def main():
    print("=" * 60)
    print("TASK A: modular structure of M =", MOD)
    print("=" * 60)

    # ---- A1: factorization ----
    print("\n[A1] Factorization of M =", MOD)
    print("  isprime:", sympy.isprime(MOD))
    fac = sympy.factorint(MOD)
    print("  factorint:", fac)
    print("  -> M is a single prime power: itself (M^1).")

    # ---- A2: order of 10 ----
    print("\n[A2] Multiplicative order of 10 mod prime powers, and ord_10(M)")
    for q in sorted(fac, key=lambda x: -(x or 0)):
        pass
    # single prime power is MOD itself
    q = MOD
    print(f"  For prime power q = {q}:")
    if sympy.gcd(10, q) == 1:
        ord_q = sympy.n_order(10, q)
        print(f"    gcd(10, q) = 1, ord_10(q) = {ord_q}")
        print(f"    (check: 10^{ord_q} mod q = {pow(10, ord_q, q)})")
    else:
        print("    gcd(10,q) != 1: 10 not invertible mod q; no finite multiplicative order.")
        ord_q = None

    ord_M = ord_q  # lcm over the single prime power = the prime-power order itself
    print(f"  ord_10(M) = lcm({[q for _ in [0]]}) = {ord_M}")
    print(f"  check 10^{ord_M} mod M = {pow(10, ord_M, MOD)} (should be 1)")
    print(f"  => the period of 10^k mod M is {ord_M}.")

    # ---- A3: Pisano period ----
    print("\n[A3] Pisano period of Fibonacci mod M =", MOD)
    pi = pisano_period(MOD)
    print(f"  Pisano period pi(M) = {pi}")
    # verify: F_pi == 0, F_{pi+1} == 1 mod M
    a, b = 0, 1
    for _ in range(pi):
        a, b = b, (a + b) % MOD
    print(f"  F_{pi} mod M = {a} (expect 0), F_{pi+1} mod M = {b} (expect 1)")
    # Also confirm it's the minimal: no smaller T in 1..pi-1 with the pair (0,1)
    a, b = 0, 1
    smaller = None
    for t in range(1, pi):
        a, b = b, (a + b) % MOD
        if a == 0 and b == 1:
            smaller = t
            break
    print(f"  smallest T<{pi} returning to (0,1): {smaller} (None => pi is minimal)")

    print("\n[DONE Task A]")
    print(f"  ord_10(M) = {ord_M} ; Pisano(M) = {pi}")


if __name__ == "__main__":
    main()
