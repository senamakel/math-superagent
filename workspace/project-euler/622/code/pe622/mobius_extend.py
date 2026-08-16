#!/usr/bin/env python3
"""Falsification test of the PE622 Möbius-inversion identities past k=60.

The existing record is machine-verified for k=1..60 (and the identity is
provable via Möbius inversion).  To push the conjecture further we compare,
for each sampled k > 60:

  C_mob(k)  = sum_{d|k} mu(k/d)*(tau(2^d-1) - 1)
  S_mob(k)  = sum_{d|k} mu(k/d)*(sigma(2^d-1) - 1)

against a DIRECT divisor enumeration over divisors m of 2^k - 1 with
ord_m(2) = k (m > 1).  Any disagreement is a falsification of the identity.

The direct enumeration is the oracle; it is kept feasible by choosing k whose
2^k - 1 has a manageable divisor count.
"""
import sympy


def mobius_C_S(k):
    C = sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k))
    return C, S


def direct_C_S(k):
    N = 2**k - 1
    good = [m for m in sympy.divisors(N) if m > 1 and sympy.n_order(2, m) == k]
    return len(good), sum(good)


def main():
    # sample k > 60, spread, keeping divisor counts of 2^k-1 feasible
    ks = [61, 62, 64, 66, 68, 70, 72, 75, 76, 78, 80, 84, 90, 96, 100,
          102, 108, 120, 61*2]
    # drop if divisor enumeration of 2^k-1 would blow up (guard below)
    checked = 0
    for k in ks:
        N = 2**k - 1
        n_div = sympy.divisor_count(N)
        if n_div > 200000:
            print(f"k={k}: skip direct (2^{k}-1 has {n_div} divisors)")
            continue
        Cm, Sm = mobius_C_S(k)
        Cd, Sd = direct_C_S(k)
        ok = (Cm == Cd) and (Sm == Sd)
        Cm, Cd, Sm, Sd = int(Cm), int(Cd), int(Sm), int(Sd)
        print(f"k={k:3d}  C_mob={Cm:6d} C_dir={Cd:6d}  S_mob={Sm} S_dir={Sd}  "
              f"{'OK' if ok else '*** FALSIFIED ***'}")
        checked += 1
        if not ok:
            print("\nFALSIFIED — identity fails past k=60!")
            return
    print(f"\nAll {checked} sampled k>60 agree with the Möbius identity (direct oracle). "
          f"Identity survives extension well past k=60.")


if __name__ == "__main__":
    main()
