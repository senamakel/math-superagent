#!/usr/bin/env python3
"""Verify the small-column rows of the run's computed genus table for
C(x,k1)=C(y,k2) against the LITERATURE genus formula for superelliptic curves
y^m = f(x), f squarefree of degree d:

    g = ((d-2)(m-1) + m - gcd(m,d)) / 2

(Sutherland, Open Book Series 4 (2020) eq. (1); Wikipedia "Superelliptic
curve", Genus section.)

The relevant birational models (from code/out/genus_closed_forms.md and the
genus table capture):
  * pair {2,n}: C(y,2)=C(x,n)  <=>  y(y-1) = 2 C(x,n)  <=>  (2y-1)^2 = 1+8C(x,n)
        hyperelliptic, m=2, d=n  ->  g = floor((n-1)/2)
  * pair {3,n}: C(y,3)=C(x,n)  <=>  Y^3 - Y = 6 C(x,n),  Y = y-1
        cyclic trigonal, m=3, d=n  ->  g = n-1 (3 ∤ n), n-2 (3 | n)
  * pair {4,n}: 2:1 cover of the hyperelliptic curve w^2 = 1+24 C(x,n);
        NOT a direct superelliptic cover, formula does not apply (reported).

Empirical test: formula vs the recorded table values genus(2,n) for n=3..12
and genus(3,n) for n=4..24 from code/out/genus_table.captured.txt.
"""
import math

def genus_superelliptic(m, d):
    return ((d - 2) * (m - 1) + m - math.gcd(m, d)) // 2

def closed_2n(n):   return (n - 1) // 2
def closed_3n(n):   return n - 1 if n % 3 else n - 2

recorded_2n = {3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:4, 10:4, 11:5, 12:5}
recorded_3n = {4:3, 5:4, 6:4, 7:6, 8:7, 9:7, 10:9, 11:10, 12:10,
               13:12, 14:13, 15:13, 16:15, 17:16, 18:16, 19:18, 20:19,
               21:19, 22:21, 23:22, 24:22}
recorded_4n = {5:6, 6:7, 7:9, 8:9, 9:12, 10:13, 11:15, 12:15}

print("== {2,n} pair: hyperelliptic (m=2, d=n);  literature vs claimed vs recorded ==")
bad2 = []
for n in sorted(recorded_2n):
    lit, claim, rec = genus_superelliptic(2, n), closed_2n(n), recorded_2n[n]
    mark = "OK" if lit == claim == rec else "MISMATCH"
    if lit != rec: bad2.append(n)
    print(f"  n={n:2d}: lit={lit:2d} claim={claim:2d} recorded={rec:2d}  {mark}")

print()
print("== {3,n} pair: cyclic trigonal (m=3, d=n);  literature vs claimed vs recorded ==")
bad3 = []
for n in sorted(recorded_3n):
    lit, claim, rec = genus_superelliptic(3, n), closed_3n(n), recorded_3n[n]
    mark = "OK" if lit == claim == rec else "MISMATCH"
    if lit != rec: bad3.append(n)
    print(f"  n={n:2d}: lit={lit:2d} claim={claim:2d} recorded={rec:2d}  {mark}")

print()
print("== {4,n} pair: NOT a direct superelliptic cover (2:1 cover of w^2=1+24C(x,n)) ==")
print("  Literature formula for the *base* hyperelliptic w^2=1+24C(x,n) (m=2,d=n):")
print("  n : base genus | recorded {4,n} genus")
for n in sorted(recorded_4n):
    print(f"  {n:2d}:      {genus_superelliptic(2,n):2d}      |      {recorded_4n[n]:2d}")

print()
total_bad = len(bad2) + len(bad3)
if total_bad == 0:
    print("RESULT: ALL literature-formula cross-checks PASS for {2,n} and {3,n}")
    print("  -> the Sutherland/Wikipedia superelliptic genus formula reproduces")
    print("     the run's independently computed small-column genus rows,")
    print("     giving the small-column closed forms a citable primary anchor.")
else:
    print(f"RESULT: {total_bad} mismatches: {bad2} ({len(bad2)} in row 2), {bad3} ({len(bad3)} in row 3)")