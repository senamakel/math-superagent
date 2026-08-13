#!/usr/bin/env python3
"""Analysis of the genuine (infinite-row) block-length sequence b(k):
growth structure, regen events, and the exact invariant candidates.

Reads code/out/genuine_sequences.json (written by extract_genuine.py).
Prints exact facts only. No floats except where stated.
"""
import json
from collections import Counter

with open("code/out/genuine_sequences.json") as f:
    g = json.load(f)
b = g["b"]
s = g["s"]
bits = g["bits"]
ig = g["intruder"]
diffs = g["diffs"]
runs = g["runs"]
K = len(b)

print(f"genuine rows k=1..{K}")

# 1. growth: log2 ratios at regen jumps; doubling time between local minima
print("\n-- growth structure --")
# local minima of b (dips before regen jumps)
lmin = [(k + 1, b[k]) for k in range(K) if (k == 0 or b[k] < b[k - 1]) and (k == K - 1 or b[k] <= b[k + 1])]
print("local minima (k, b):", lmin)

# consecutive regen events: k where diff > 0 (strict growth, absorbing a long run)
jumps = [(k + 1, d) for k, d in enumerate(diffs) if d > 0]
print("strict regen jumps (k+1, size):", jumps)
print("num strict regen:", len(jumps), " max:", max(d for _, d in jumps))

# 2. bit structure of s: runs
print("\n-- s (second entry) runs --")
sruns = []
cur, clen = bits[0], 1
for x in bits[1:]:
    if x == cur:
        clen += 1
    else:
        sruns.append((cur, clen))
        cur, clen = x, 1
sruns.append((cur, clen))
print("s/2 runs:", sruns)
print("run lengths by value:", {v: [t[1] for t in sruns if t[0] == v] for v in (0, 1)})

# 3. invariant candidates, checked EXACTLY over all genuine rows
print("\n-- invariant checks over k=1..%d --" % K)
# (a) s in {0,2} (that's the conjecture itself, holds by construction of file)
print("s all in {0,2}:", all(x in (0, 2) for x in s))
# (b) intruder all even, in [4, 14], all 0 or 2 mod 4
intr = [x for x in ig if x is not None]
print("intruders: min %d max %d n=%d" % (min(intr), max(intr), len(intr)))
print("intruder value counts:", sorted(Counter(intr).items()))
print("intruder mod4:", sorted(Counter(x % 4 for x in intr).items()))
print("all intruders in (0,2) mod 4:", all(x % 4 in (0, 2) for x in intr))
# (c) erosion runs: y0 in [4,14]; check L vs (y0-4)/2 constraint: run needs
#     (y0-4)/2  x==2 steps to reach y=4, then one more x==2 to regen, so
#     L-1 >= (y0-4)/2 + 1  ->  L >= (y0-4)/2 + 2  is necessary. Also total
#     length L >= (y0-4)/2 + 1 + (x==0 steps allowed).
viol = [(r0, L, y0) for (r0, L, y0, _) in runs if L < (y0 - 4) // 2 + 2]
print("runs violating necessary bound L >= (y0-4)/2+2:", viol if viol else "none")
# (d) min b over genuine stays >= 7 for k>=2  (regen before exhaustion is
#     numerically observed; b never even gets close to small)
print("min b over k>=2:", min(b[1:]), "at k=", b[1:].index(min(b[1:])) + 2)
# (e) does b(k+1) >= b(k)-1 always (erosion bound)?  -- theorem, check anyway
print("erosion bound b(k+1) >= b(k)-1:", min(diffs) >= -1)

# 4. regen structure: what does the state (x_last, y) look like at each row?
#    x_last not in the JSON; recompute from rows is a separate exact run.
#    Here: report diff==-1 vs >=0 distribution and the b-values at regen rows
print("\n-- transition stats --")
print("transitions: total %d, diff==-1: %d, diff==0: %d, diff>0: %d" % (
    len(diffs), sum(1 for d in diffs if d == -1), sum(1 for d in diffs if d == 0),
    sum(1 for d in diffs if d > 0)))
print("b right before each regen (k, b):",
      [(k + 1, b[k]) for k, d in enumerate(diffs) if d >= 0])

# 5. doubling: growth between successive local minima (k, b)
print("\n-- growth between minima --")
prev = None
for (k, v) in lmin:
    if prev:
        dk = k - prev[0]
        ratio = v / prev[1] if prev[1] else float("inf")
        print(f"  k:{prev[0]}->{k}: b {prev[1]} -> {v}, rows {dk}, ratio {ratio:.3f}, "
              f"doubling every {dk / ((v / prev[1]).bit_length() - 1) if v > prev[1] else float('inf'):.2f} rows")
    prev = (k, v)