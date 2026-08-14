#!/usr/bin/env python3
"""Verify the library's check values for PE 351: H(5), H(10), H(1000) and
the H(10^8) arithmetic, from the claim blocks in
research/notes/pe351-governing-theory.md.  Exact integer arithmetic only."""
import sys

def phi_sieve(n):
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:            # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi

def Phi(n):
    return sum(phi_sieve(n))

def H_formula(n, Phi_n):
    # H(n) = 6 * (C(n+1,2) - Phi(n)) = 3n(n+1) - 6*Phi(n)
    return 3 * n * (n + 1) - 6 * Phi_n

def main():
    # statement oracles
    oracles = {5: 30, 10: 138, 1000: 1177848}
    ok = True
    for n, want in sorted(oracles.items()):
        p = Phi(n)
        h = H_formula(n, p)
        status = "OK" if h == want else "FAIL"
        if h != want:
            ok = False
        print(f"H({n}) = {h}  (want {want})  [{status}]  Phi({n}) = {p}")
    # library's verification values: Phi(10^k), k=0..8 (OEIS A064018)
    want_phi = {0: 1, 1: 32, 2: 3044, 3: 304192, 4: 30397486, 5: 3039650754,
                6: 303963552392, 7: 30396356427242, 8: 3039635516365908}
    print("\nSummatory totient Phi(10^k) vs OEIS A064018:")
    for k, want in sorted(want_phi.items()):
        n = 10 ** k
        p = Phi(n)
        status = "OK" if p == want else "FAIL"
        if p != want:
            ok = False
        print(f"Phi(10^{k}) = {p}  (want {want})  [{status}]")
    # the final arithmetic: H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8)
    # with the catalogued Phi(10^8) -- this is the check anchor, not the
    # program's answer; the program must reproduce it.
    n = 10 ** 8
    p8 = want_phi[8]
    h8 = H_formula(n, p8)
    print(f"\nH(10^8) via catalogued Phi(10^8) = {h8}")
    print(f"digits: {len(str(h8))}")
    print("\nALL OK" if ok else "\nMISMATCHES PRESENT")

if __name__ == "__main__":
    sys.exit(main())
