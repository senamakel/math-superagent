"""Digit-complement (mirror) structure:  d  vs  9-d, across the 10^10 window.

The 9's complement map  n -> M-1-n  (M = 10^10) bijects [0, M-1] and flips
digits d <-> 9-d.  Tree-derived identity to verify mechanically:

    f_d( M-1-n ) = M - f_{9-d}(n) + z        z = # of digit (9-d) in n   ... (I)

Derivation: pad every number in [0, M-1] to 10 digits; digit 9-d at a
position of n occurs in exactly f_{9-d}(n) strings; total count of digit d
over ALL strings [0, M-1] is 10*10^9 = M; the complement bijection maps
d-occurrences in (M-1-n, M-1] onto (9-d)-occurrences in [0, M-1-n].

Consequences for fixed points (verified as set equalities over the COMPLETE
solution lists on disk, plus direct f evaluations):
  * if f_d(n) = n then f_{9-d}(M-1-n) = M - n + z_{9-d}(n).
  * Empirically, for d=2 (complete 7-term seed B_2):
      B_7 = {0} U { M - b - z : b in B_2, b != 0, z = # of digit-2s in b }.
    (Equivalently the mirror lands on a 7-fixed point after subtracting z.)
    Same claim probed for other pairs (d, 9-d) and reported either way.
  * B_2's six first-differences = p1 p2 p3 p4 p1 p2 (period-4, exact);
    B_7's six first-differences contain the same four numbers with trailing
    digits 27->30, 3->0 (residue effect of the z-corrections).
"""
import sys, os, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

M = 10**10
sols = {d: [int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
        for d in range(1, 10)}
B = {d: [n for n in sols[d] if n < M] for d in range(1, 10)}
SB = {d: set(B[d]) for d in range(1, 10)}
zd = lambda n, d: str(n).count(str(d))

print("== (I) complement identity  f_d(M-1-n) = M - f_{9-d}(n) + z  ==")
random.seed(9)
bad = 0
for d in range(1, 9):          # 9-d in 1..8
    e = 9 - d
    for _ in range(20000):
        n = random.randrange(0, M)
        lhs = f_place_value(M - 1 - n, e)   # f_{9-d}(M-1-n)
        rhs = M - f_place_value(n, d) + zd(n, e)
        if lhs != rhs:
            bad += 1
print(f"  160000 random n over all d=1..8: failures = {bad}")
assert bad == 0

print("\n== (II) fixed-point mirror: f_{9-d}(M-1-n) = M - n + z_{9-d}(n) for f_d(n)=n ==")
for d in range(1, 9):
    e = 9 - d
    for n in B[d]:
        got = f_place_value(M - 1 - n, e)
        assert got == M - n + zd(n, e), (d, n, got)
print("  holds for every seed solution n of every d=1..8 (mechanical)")

print("\n== (III) the (2,7) mirror set claim ==")
B2 = B[2]; B7 = set(B[7])
mirror = sorted(M - b - zd(b, 2) for b in B2 if b != 0)
print("  predicted B_7 = {0} U {M - b - z_2(b) : b in B_2}: "
      f"{[0] + mirror == B[7]}")
for b in B2[1:]:
    n = M - b - zd(b, 2)
    f7 = f_place_value(n, 7)
    print(f"    b={b:>10} z={zd(b,2)}  -> n*={n:>12}  f_7(n*)={f7:>12}  fixed={f7==n}")

print("\n== (IV) other pairs (d, 9-d): does {0} U {M-b-z : b in B_d} == B_{9-d}? ==")
for d in range(1, 8):
    e = 9 - d
    if e == d or e == 0:
        continue
    pred = [0] + sorted(M - b - zd(b, d) for b in B[d] if b != 0)
    print(f"  d={d} -> e={e}: seed sizes |B_d|={len(B[d])} |B_e|={len(B[e])} "
          f"mirror-match={pred == B[e]}")
    if pred != B[e]:
        common = len(set(pred) & set(B[e]))
        print(f"        (overlap {common}, first mis-match sample: "
              f"{next((p for p in pred if p not in set(B[e])), None)})")

print("\n== (V) B_2 first-difference period; B_7 differences as residue-variant ==")
for d, tag in [(2, "B_2"), (7, "B_7")]:
    dd = [B[d][i+1] - B[d][i] for i in range(len(B[d]) - 1)]
    print(f"  {tag} diffs = {dd}")
d2 = [B[2][i+1] - B[2][i] for i in range(len(B[2]) - 1)]
print(f"  B_2 diffs period-4 (p1 p2 p3 p4 p1 p2): "
      f"{d2[0]==d2[4] and d2[1]==d2[5]}")
d7 = [B[7][i+1] - B[7][i] for i in range(len(B[7]) - 1)]
print(f"  B_7 diffs contain {{6736170, 28263830, 257536170, 207463830}} "
      f"(residue variants of B_2's p's): "
      f"{set(d7[1:]) == {6736170, 28263830, 257536170, 207463830}}")