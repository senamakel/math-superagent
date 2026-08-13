#!/usr/bin/env python3
"""Verify the sub-progression identity families found by search_subprogression.py
and quantify how much of the open class n ≡ 1 (mod 840) they cover.

Each family has form n = a*k + b with a = 840*M, b ≡ 1 (mod 840), so it is a
sub-progression of the open class r=1.  For a family (a,b), n=840*K+1 falls in
it iff 840K+1 ≡ b (mod a), i.e. K ≡ (b-1)/840 (mod M), density 1/M within r=1.

We re-verify every family as a symbolic identity in k AND at sampled integer k,
then compute the union of residue classes (K mod M) covered per modulus, and the
density of coverage of r=1 by the union over all families found.

The families are copied verbatim from code/out/subprogression.captured.txt.
"""
from fractions import Fraction
from sympy import Symbol, simplify

k = Symbol('k')

# (a, b, x, y, z) with x,y,z as sympy expressions in k
FAMILIES = [
    (9240, 4201, 27720*k + 12603, 3*(840*k + 382)*(9240*k + 4201), 2520*k + 1146),
    (9240, 5881, 27720*k + 17643, 3*(2520*k + 1604)*(9240*k + 5881), 2520*k + 1604),
    (9240, 8401, 27720*k + 25203, (840*k + 764)*(9240*k + 8401), 2520*k + 2292),
    (10920, 5881, 109200*k + 58810, 10*(1400*k + 754)*(10920*k + 5881), 2800*k + 1508),
    (10920, 7561, 109200*k + 75610, 2*(280*k + 194)*(10920*k + 7561), 2800*k + 1940),
    (10920, 9241, 109200*k + 92410, 5*(280*k + 237)*(10920*k + 9241), 2800*k + 2370),
    (10920, 10081, 109200*k + 100810, 10*(560*k + 517)*(10920*k + 10081), 2800*k + 2585),
    (14280, 3361, (217/17 if False else 0), 0, 0),  # placeholder removed below
]

# Manual: 14280 family from 14b/15a with products; simpler to verify symbolically
# using its own expressions.  Add explicitly:
FAMILIES = [
    (9240, 4201, 27720*k + 12603, 3*(840*k + 382)*(9240*k + 4201), 2520*k + 1146),
    (9240, 5881, 27720*k + 17643, 3*(2520*k + 1604)*(9240*k + 5881), 2520*k + 1604),
    (9240, 8401, 27720*k + 25203, (840*k + 764)*(9240*k + 8401), 2520*k + 2292),
    (10920, 5881, 109200*k + 58810, 10*(1400*k + 754)*(10920*k + 5881), 2800*k + 1508),
    (10920, 7561, 109200*k + 75610, 2*(280*k + 194)*(10920*k + 7561), 2800*k + 1940),
    (10920, 9241, 109200*k + 92410, 5*(280*k + 237)*(10920*k + 9241), 2800*k + 2370),
    (10920, 10081, 109200*k + 100810, 10*(560*k + 517)*(10920*k + 10081), 2800*k + 2585),
    # 14b family a=14280 b=3361 (from captured: x=(21k+5)(485520k+114274),
    # y=(21k+5)(71400k+16805), z=3570k+850)  -- verify symbolically:
    (14280, 3361, (21*k + 5)*(485520*k + 114274),
     (21*k + 5)*(71400*k + 16805), 3570*k + 850),
    # 15a family a=14280 b=3361 (x=124950k+29410, y=3675k+865, z=(735k+173)(485520k+114274))
    (14280, 3361, 124950*k + 29410, 3675*k + 865, (735*k + 173)*(485520*k + 114274)),
]


def check_family(a, b, x, y, z):
    n = a * k + b
    diff = simplify(4 / n - (1 / x + 1 / y + 1 / z))
    # Also check at sampled integer k by exact Fraction arithmetic
    numeric_ok = True
    for kk in range(0, 12):
        def ev(e):
            return int(simplify(e.subs(k, kk)))
        xx, yy, zz, nn = ev(x), ev(y), ev(z), a * kk + b
        if xx <= 0 or yy <= 0 or zz <= 0:
            numeric_ok = False
            break
        if Fraction(1, xx) + Fraction(1, yy) + Fraction(1, zz) != Fraction(4, nn):
            numeric_ok = False
            break
    return diff == 0, numeric_ok


def main():
    print("Symbolic + numeric verification of every sub-progression family")
    r1_covered_residues = {}   # modulus M -> set of residues c (K ≡ c mod M)
    print("-" * 78)
    for (a, b, x, y, z) in FAMILIES:
        sym_ok, num_ok = check_family(a, b, x, y, z)
        M = a // 840
        res = (b - 1) // 840   # K ≡ res (mod M)
        r = b % 840
        r1_covered_residues.setdefault(M, set()).add(res)
        print(f"a={a:6} b={b:6} M={M:3}  covers n≡1 mod840 with K≡{res} mod{M} "
              f"| sym={sym_ok} num={num_ok}")

    print("-" * 78)
    print("Coverage of open class n=840K+1 - union over all families")
    # Density = sum over distinct (M,res) of 1/M, overlapping handled by CRT union.
    # Union over moduli: compute directly by sampling large K.
    N = 2000000
    covered = 0
    for K in range(N):
        n = 840 * K + 1
        hit = False
        for (a, b, x, y, z) in FAMILIES:
            if n >= b and (n - b) % a == 0:
                hit = True
                break
        if hit:
            covered += 1
    print(f"Sample K in [0,{N}): {covered}/{N} covered = {covered/N:.6f} "
          "of the class n≡1 mod 840")
    best_density = max(1.0 / (a // 840) for (a, b, *_ ) in FAMILIES)
    print(f"Best single-family density (largest modulus M):  1/{min(a//840 for (a,b,*_) in FAMILIES)} "
          f"= {best_density:.6f}")


if __name__ == '__main__':
    main()
