#!/usr/bin/env python3
"""Exact mod-840 coverage facts for the Erdos-Straus conjecture.

Run:  timeout 540 python3 code/out/esc_residues.py | tee code/out/esc_residues.captured.txt
Purpose: the numbers behind claims mordell-covering-840, reduction-mod24,
seven-equations-complete. Standard library + sympy only.
"""
from fractions import Fraction

MOD = 840
families = {
    "2 mod 3":   lambda r: r % 3 == 2,
    "3 mod 4":   lambda r: r % 4 == 3,
    "2|3 mod 5": lambda r: r % 5 in (2, 3),
    "3|5|6 mod 7": lambda r: r % 7 in (3, 5, 6),
    "5 mod 8":   lambda r: r % 8 == 5,
}

covered = [False] * MOD
per_family = {}
for name, cond in families.items():
    rs = [r for r in range(MOD) if cond(r)]
    per_family[name] = rs
    for r in rs:
        covered[r] = True

open_res = [r for r in range(MOD) if not covered[r]]
print("per-family residue counts mod 840:")
for name, rs in per_family.items():
    print(f"  {name:14s} {len(rs):3d} residues")
print(f"union covers {sum(covered)} of {MOD} classes")
print(f"open classes ({len(open_res)}): {open_res}")
expected = {1, 121, 169, 289, 361, 529}
assert set(open_res) == expected, "open set differs from expected!"
print("open set matches {1,121,169,289,361,529}")

# all six are quadratic residues mod 840 (in fact perfect squares of 1..23)
squares = {s * s % MOD for s in range(MOD)}
assert all(r in squares for r in open_res), "an open class is not a square mod 840"
print("six open classes are all quadratic residues mod 840", sorted(open_res))
print("square-roots mod 840:", sorted((s, s * s % MOD) for s in range(1, 30)
                                      if s * s % MOD in expected))

# smallest prime in an open class (classical: 1009)
from sympy import primerange
smallest = next(n for n in primerange(2, 5000) if n % MOD in expected)
print(f"smallest prime n >= 2 in an open class: {smallest}")
assert smallest == 1009, f"expected 1009, got {smallest}"

# structural slice: all open classes ≡ 1 mod 24 and ≡ 1 mod 3,5,7
print("open classes mod 24:", sorted(r % 24 for r in open_res))
print("open classes mod 3,5,7:", sorted((r % 3, r % 5, r % 7) for r in open_res))
assert all(r % 24 == 1 for r in open_res)

# sanity: oracle identity for each family on a few n in the class (exact rational)
def solves(n, x, y, z):
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

identity_checks = [  # (class name, n, x, y, z) -- classic worked identities
    ("2 mod 3",    5,  5, 2, 10),            # 4/5 = 1/5+1/2+1/10 (n+1)/3=2
    ("3 mod 4",    7,  2, 4, 28),            # classical n=4k+3 identity
    ("5 mod 8",   13,  4, 13, 52),           # 4/13 via p=8t-3 with t=2
]
for name, n, x, y, z in identity_checks:
    assert solves(n, x, y, z), (name, n, x, y, z)
    print(f"oracle check {name}: 4/{n} = 1/{x}+1/{y}+1/{z} OK")
print("ALL ASSERTIONS PASSED")