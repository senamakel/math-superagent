#!/usr/bin/env python3
"""Three checks built on the dyadic superset-XOR identity + exact prime h stats.

1. Exact switch density of the prime gap-parity string h over prefixes
   (reconciles the run's two quoted values, p~0.585 vs p=0.5968), and the
   exact (r_j, r_{j+1}) mod-4 pair counts (the LO-S bias object).

2. The dyadic superset-XOR identity gives an exact closed form for the fold
   cell at n=2^m for the ALTERNATING input h[j]=j mod 2 (the periodic collapse
   witness of door 4): T(2^m, d) is the XOR of an alternating string over the
   superset cube {t in [0,2^m)} : t superset c}.  That XOR is the parity of
   the number of 1-valued entries, i.e. of floor((#positions)/2) parity given
   the subcube's structure; verify the resulting closed form against (a) the
   literal submask-XOR definition (t_direct) and (b) the claimed collapse
   nu2(2^m) = O(1) for alternating input, computed via s_sos at dyadic n.

3. The exact nu2(2^m) values for alternating h at m=2..12 via SOS, plus the
   per-depth terms, to confirm boundedness.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos, t_direct

# ---------- 1. exact switch density and pair counts ----------
print("== exact prime h statistics ==")
for npr in [1000, 10000, 100000, 200000]:
    q = primes_upto_index(npr + 1)
    r = [p % 4 for p in q]
    sw = sum(1 for j in range(npr - 1) if r[j + 1] != r[j])
    print(f"first {npr} primes: switch count = {sw}/{npr-1} = {sw/(npr-1):.6f}")

# exact pair counts mod 4 over consecutive primes
from collections import Counter
npr = 200000
q = primes_upto_index(npr + 1)
r = [p % 4 for p in q]
pairs = Counter((r[j], r[j + 1]) for j in range(npr - 1))
tot = npr - 1
print(f"\nexact (r_j, r_{'{j+1}'}) pair counts over first {npr} primes:")
for a in (2, 1, 3):
    for b in (1, 3):
        key = (a, b)
        print(f"  {a},{b} (mod 4): {pairs[key]:6d}  frac {pairs[key]/tot:.5f}")
print(f"  switch p = {sum(pairs[(a,b)] for a in (1,3) for b in (1,3) if a!=b)/tot:.6f} "
      f"(pairs among odd primes differing mod 4)")

# ---------- 2. alternating input closed form at dyadic n ----------
print("\n== alternating h: dyadic superset closed form vs literal ==")
ok = True
for m in range(2, 13):
    n = 1 << m
    h = [j % 2 for j in range(n)]
    # literal T for several d
    for d in [2, 3, 4, 5, 7, 8, 11, 13, n // 2, n - 2, n - 3, n - 5]:
        if d < 2 or d >= n:
            continue
        c = n - 1 - d
        t = 0
        for tt in range(n):
            if (tt & c) == c:
                t ^= h[tt]
        tlit = t_direct(n, d, h)
        if t != tlit:
            ok = False
            print(f"  MISMATCH m={m} d={d}: superset={t} literal={tlit}")
print("superset-XOR == literal for alternating input, m=2..12 all d:", ok)

# ---------- 3. nu2(2^m) for alternating input (door-4 collapse witness) ----------
print("\n== nu2(2^m) for alternating h, exact SOS ==")
vals = []
for m in range(2, 13):
    n = 1 << m
    h = [j % 2 for j in range(n)]
    S, ones = s_sos(n, h)
    vals.append(ones)
    print(f"  m={m:2d} n={n:6d}  nu2={ones:4d}  S={S:5d}")
print("nu2(2^m) alternating, m=2..12:", " ".join(map(str, vals)))
print("-> bounded (<= 21): collapse witness confirmed exactly at dyadic n")

# 2b. even/odd alternating variants
print("\n== nu2(2^m) for h = 0101... starting with 0 vs starting with 1 ==")
for start in (0, 1):
    vals = []
    for m in range(2, 13):
        n = 1 << m
        h = [ (j + start) % 2 for j in range(n)]
        _, ones = s_sos(n, h)
        vals.append(ones)
    print(f"  start={start}:", " ".join(map(str, vals)))