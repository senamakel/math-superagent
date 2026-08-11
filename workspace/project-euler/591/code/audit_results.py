#!/usr/bin/env python3
"""Independent audit of /workspace/results_full_bothsides.txt.

Touches no solver code.  Verifies each of the 90 data rows (d, b, a, |a|)
against the problem statement using mpmath at dps=150 plus exact integers:

  (1) d is non-square in [2,99]
  (2) |a| <= 1e13 and |b| <= 1e13
  (3) a == nint(pi - b*sqrt(d))          (best a for that b)
  (4) sign(a) == -sign(b) or a == 0      (error term drives toward pi)
  (5) master identity in |a|:
        b>0 : |a| == nint(b*sqrt(d) - pi)
        b<0 : |a| == nint(pi + |b|*sqrt(d))
  (6) local minimality in b: for every b' in {b-10..b+10} \ {b} with
        a' = nint(pi - b'*sqrt(d)) clamped to [-1e13,1e13],
        |a+b*sqrt(d)-pi| <= |a'+b'*sqrt(d)-pi|  (no neighbor strictly better)
  (7) exact re-sum of the |a| column equals the S reported in the file.

Also, with the d=2 row, computes a + b*sqrt(2) - pi at dps=150 and checks
|.| <= 1e-13.
"""
import math
from mpmath import mp, mpf, nint, sqrt, pi

mp.dps = 150

LIM = mpf(10)**13

def is_square(d):
    r = math.isqrt(d)
    return r * r == d

rows = []
endsum = None
with open('/workspace/results_full_bothsides.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) == 2 and parts[0] == 'S':
            endsum = int(parts[1])
            continue
        d, b, a, aa = (int(p) for p in parts)
        rows.append((d, b, a, aa))

print(f"rows parsed: {len(rows)}")

def failed(label, i, info):
    print(f"  FAIL {label} row {i}: {info}")

# run all checks, count pass/fail per check (1..7)
counts = {k: [0, 0] for k in range(1, 8)}  # [pass, fail]

for idx, (d, b, a, aa) in enumerate(rows):
    i = idx + 1
    # check 1
    if d in range(2, 100) and not is_square(d):
        counts[1][0] += 1
    else:
        counts[1][1] += 1
        failed(1, i, f"d={d}")
    # check 2
    if abs(a) <= 10**13 and abs(b) <= 10**13:
        counts[2][0] += 1
    else:
        counts[2][1] += 1
        failed(2, i, f"d={d} a={a} b={b}")
    # check 3
    sd = sqrt(mpf(d))
    want_a = int(nint(pi - mpf(b) * sd))
    if a == want_a:
        counts[3][0] += 1
    else:
        counts[3][1] += 1
        failed(3, i, f"d={d} a={a} want={want_a}")
    # check 4
    if a == 0 or (a > 0 and b < 0) or (a < 0 and b > 0):
        counts[4][0] += 1
    else:
        counts[4][1] += 1
        failed(4, i, f"d={d} a={a} b={b}")
    # check 5 master identity
    ok5 = False
    if b > 0:
        ok5 = (aa == int(nint(mpf(b) * sd - pi)))
    elif b < 0:
        ok5 = (aa == int(nint(pi + mpf(-b) * sd)))
    else:
        ok5 = (aa == 0)  # b==0 -> a = nint(pi) ~ 3, |a| handled by check 3
    if ok5:
        counts[5][0] += 1
    else:
        counts[5][1] += 1
        failed(5, i, f"d={d} b={b} aa={aa}")
    # check 6 local minimality
    err = abs(mpf(a) + mpf(b) * sd - pi)
    local_ok = True
    for bp in range(b - 10, b + 11):
        if bp == b:
            continue
        av = int(nint(pi - mpf(bp) * sd))
        av = max(-LIM, min(LIM, av))
        e = abs(mpf(av) + mpf(bp) * sd - pi)
        if e < err:
            local_ok = False
            failed(6, i, f"d={d} better at b'={bp} err'={mp.nstr(e,10)} < err={mp.nstr(err,10)}")
            break
    if local_ok:
        counts[6][0] += 1
    else:
        counts[6][1] += 1

# check 7 exact re-sum
resum = sum(aa for (_, _, _, aa) in rows)
if resum == endsum:
    counts[7][0] += 1
else:
    counts[7][1] += 1
    failed(7, "sum", f"resum={resum} endsum={endsum}")

# d=2 oracle residual
d2 = [r for r in rows if r[0] == 2][0]
_, b2, a2, _ = d2
sd2 = sqrt(mpf(2))
resid = mpf(a2) + mpf(b2) * sd2 - pi
print(f"d=2 oracle residual a + b*sqrt(2) - pi = {mp.nstr(resid, 50)}")
oracle_ok = abs(resid) <= mpf(10)**(-13)
print(f"d=2 oracle |residual| <= 1e-13 : {'PASS' if oracle_ok else 'FAIL'}")

print("\nper-check pass/fail:")
for k in sorted(counts):
    p, fn = counts[k]
    print(f"  check {k}: {p}/{p+fn}")

print(f"final S (exact re-sum): {resum}" if counts[7][0] else "final S: MISMATCH")
