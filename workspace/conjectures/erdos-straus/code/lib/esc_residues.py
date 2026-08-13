"""Exact mod-840 coverage facts for the Erdos-Straus conjecture.

Computes, from the five classical Mordell-family identities (n = 2 mod 3,
3 mod 4, 2|3 mod 5, 3|5|6 mod 7, 5 mod 8) as stated by Wikipedia / Mordell
(1967), exactly which residue classes r mod 840 are settled, which six
remain open, and per-family residue counts. Asserts the six open classes are
all squares mod 840 and that 1009 is the smallest prime in an open class.
"""
import sympy

MOD = 840
families = {
    "2 mod 3":  lambda r: r % 3 == 2,
    "3 mod 4":  lambda r: r % 4 == 3,
    "2|3 mod 5":lambda r: r % 5 in (2, 3),
    "3|5|6 mod 7": lambda r: r % 7 in (3, 5, 6),
    "5 mod 8":  lambda r: r % 8 == 5,
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

# all six are perfect squares mod 840, and equal to the listed squares outright
squares = {s * s % MOD for s in range(MOD)}
assert all(r in squares for r in open_res)
inside = [r for r in open_res if any(s * s == r for s in range(1, 30))]
print("six open classes are all quadratic residues mod 840; perfect squares among [1,30]^2:", inside)

# smallest prime in an open class
smallest = None
for n in sympy.primerange(2, 5000):
    if n % MOD in open_res:
        smallest = n
        break
print(f"smallest prime n >= 2 in an open class: {smallest}")
assert smallest == 1009, f"expected 1009, got {smallest}"

# symmetry / structure check: open classes all congruent to 1 mod 24 and to 1 mod 3,5,7
print("open classes mod 24:", sorted(r % 24 for r in open_res))
print("open classes mod 3,5,7:", sorted((r % 3, r % 5, r % 7) for r in open_res))