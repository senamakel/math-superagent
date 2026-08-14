"""Digit-complement (mirror) structure, corrected derivation.

Let C = M-1 = 9999999999 (10 nines).  The involution x -> C-x on [0, M-1]
flips every digit: digit_i(C-x) = 9 - digit_i(x).  So digit-(9-d) in x
<-> digit-d in C-x.  Hence

    f_{9-d}(C - n)  =  (# digit-d in the strings of [n, C])            (bijection)
                    =  M - f_d(n) + z_d(n)

because total digit-d occurrences over all 10-digit strings is 10*10^9 = M
and [0, C] = [0, n-1] u {n} u [n+1, C], with f_d(n) = f_d(n-1) + z_d(n).
[In the first run the script asserted this with z_{9-d}; the failure rate
113098/160000 showed the z was wrong, and z_d(n) is what makes 9971736172
work: f_7(9971736172) = M - f_2(28263827) + 3 = 9971736176, which is
f_7(9971736170) + 3 + 3 along the B_7 members.]

Consequence for fixed points:  f_d(n) = n  =>  f_{9-d}(C-n) = M - n + z_d(n).

Data claims tested exactly over the complete solution lists:
  (A) identity above, 160000 random samples, d = 1..8;
  (B) the set mirror claim: for which d does
        B_{9-d} \ {0}  ==  { M - b - z_d(b) : b in B_d, b != 0 }   exactly?
      (d=2 predicted exact; d=1 predicted to fail: |B_1|=84, |B_8|=43;
       d=3 predicted to fail on set despite matching counts 12=12;
       d=4 impossible: B_5 = {0} while B_4 has 11 nonzero seeds.)
  (C) gap sequences of B_2 and B_7: gaps of B_2 are period-4
      (p1 p2 p3 p4 p1 p2); B_7's gaps are the same four magnitudes with
      residue corrections from z (6736173 -> 6736170 etc.).
"""
import sys, os, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

M = 10**10
C = M - 1
sols = {d: [int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
        for d in range(1, 10)}
B = {d: [n for n in sols[d] if n < M] for d in range(1, 10)}
zd = lambda n, d: str(n).count(str(d))

print("== (A) corrected identity  f_{9-d}(C-n) = M - f_d(n) + z_d(n), d=1..8 ==")
random.seed(156)
bad = []
for d in range(1, 9):
    e = 9 - d
    for _ in range(20000):
        n = random.randrange(0, M)
        lhs = f_place_value(C - n, e)
        rhs = M - f_place_value(n, d) + zd(n, d)
        if lhs != rhs:
            bad.append((d, n, lhs, rhs))
            if len(bad) > 5:
                break
    if len(bad) > 5:
        break
print(f"  160000 samples: failures = {len(bad)} (first: {bad[:5]})")
assert not bad

print("\n== (B) mirror set claim, all pairs (d, 9-d) ==")
for d in range(1, 9):
    e = 9 - d
    if e == 0:
        continue
    pred = sorted({0} | {M - b - zd(b, d) for b in B[d] if b != 0})
    ok = (pred == B[e])
    print(f"  d={d} -> e={e}: |B_d|={len(B[d])} |B_e|={len(B[e])}  mirror-exact={ok}")
    if not ok:
        inter = len(set(pred) & set(B[e]))
        print(f"        overlap={inter}, diffs-in-pred={sorted(set(pred) ^ set(B[e]))[:6]}")

print("\n== (B2) exact check of the mechanism for which it holds: ==")
for d in [1, 2, 3, 4]:
    e = 9 - d
    pred = sorted({0} | {M - b - zd(b, d) for b in B[d] if b != 0})
    tag = "OK " if pred == B[e] else "FAIL"
    print(f"  d={d}: {tag}")

print("\n== (C) gap sequences ==")
for d in [2, 7]:
    gaps = [B[d][i + 1] - B[d][i] for i in range(len(B[d]) - 1)]
    print(f"  B_{d} gaps = {gaps}")
g2 = [B[2][i+1] - B[2][i] for i in range(len(B[2]) - 1)]
print(f"  B_2 gaps period-4 (first two repeat as last two): "
      f"{g2[0] == g2[4] and g2[1] == g2[5]}")
g7 = [B[7][i+1] - B[7][i] for i in range(len(B[7]) - 1)]
same = sorted(g2) == sorted(abs(x) for x in g7[1:])
print(f"  B_7 gaps (from position 1) are B_2's four magnitudes: {same}")

print("\n== (D) per-seed mirror table for d=2 ==")
for b in B[2]:
    n = M - b - zd(b, 2)
    f7 = f_place_value(n, 7)
    print(f"  b={b:>10} z2={zd(b,2)}  n*={n:>12}  f_7(n*)={f7:>12}  fixed={f7 == n}")