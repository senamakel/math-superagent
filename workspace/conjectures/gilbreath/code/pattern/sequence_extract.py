#!/usr/bin/env python3
"""Extract the integer sequences that matter from blocks_depth1000.json.

Sequences written to code/out/sequence_dump.txt:
  s_k       : second entry of row k, k=1..1000 (the conjecture object: must stay in {0,2})
  b_k       : leading {0,2} block length (genuine regime k=1..161 only; k>=162 is
              the finite-sieve width artifact)
  regen rows: k with b_{k+1} > b_k (k <= 161)
  stalls    : k with b_{k+1} == b_k
  erosion   : k with b_{k+1} == b_k - 1
  regen gaps: differences between consecutive regen rows  (Rule-90 thread prediction: powers of 2)
  jumps     : b_{k+1} - b_k at regen rows
  erosion run lengths: consecutive erosion rows
  minima    : (k, b_k) local minima of b in genuine regime
  s runs    : run lengths of s=0 and s=2

Also tests the Rule-90 thread's concrete predictions:
  P1: every gap between consecutive regen rows is a power of 2
  P2: regen rows are closer to powers of 2 than a uniform baseline (distance
      to nearest power of 2, compared to all rows 1..161)
  P3: jump sizes are powers of 2  (thread: "block-length differences are powers of 2")

And verifies the empirical exact law: in the genuine regime, every non-regen
transition satisfies b_{k+1} = b_k - 1 exactly (nothing worse), i.e.
b_{k+1} - b_k in {-1} union {>=0}.
"""
import json

D = json.load(open("code/out/blocks_depth1000.json"))
b = D["b"]
s = D["s"]
intr = D["intruder"]
assert len(b) == 1000 and len(s) == 1000 and len(intr) == 1000

GEN = 161  # rows k=1..161 have a real intruder; k>=162 is the width artifact
lines = []
def p(*a):
    lines.append(" ".join(str(x) for x in a))

# ---- s runs ----
s_run0, s_run2 = [], []
cur, ln = s[0], 1
for v in s[1:]:
    if v == cur:
        ln += 1
    else:
        (s_run0 if cur == 0 else s_run2).append(ln)
        cur, ln = v, 1
(s_run0 if cur == 0 else s_run2).append(ln)

# ---- transitions in genuine regime ----
regen, stall, erode = [], [], []
diffs = []
for k in range(GEN - 1):          # transition k -> k+1, k=1..160 (1-based k = idx+1)
    d = b[k + 1] - b[k]
    diffs.append(d)
    if d > 0:
        regen.append(k + 1)
    elif d == 0:
        stall.append(k + 1)
    elif d == -1:
        erode.append(k + 1)
    else:
        assert False, f"unexpected diff {d} at k={k+1}"
# transition 161 -> 162 (row 161 still has an intruder: intr[160] is not None)
assert intr[160] is not None and intr[161] is None
d = b[161] - b[160]
diffs.append(d)
if d > 0: regen.append(161)
elif d == 0: stall.append(161)
elif d == -1: erode.append(161)
else: assert False, f"unexpected diff {d} at k=161"

# ---- erosion runs ----
erun, cur, ln = [], erode[0], 1
for v in erode[1:]:
    if v == cur + 1:
        ln += 1
    else:
        erun.append(ln)
        cur, ln = v, 1
    cur = v
erun.append(ln)

# ---- jumps ----
jumps = [b[k + 1] - b[k] for k in range(GEN - 1) if b[k + 1] > b[k]]

# ---- minima ----
minima = []
for k in range(1, GEN - 1):
    if b[k] <= b[k - 1] and b[k] <= b[k + 1]:
        minima.append((k + 1, b[k]))

p("s (second entries) k=1..200:", s[:200])
p("s run-lengths of 0:", s_run0)
p("s run-lengths of 2:", s_run2)
p("regen rows (b_{k+1}>b_k), genuine k<=161:", regen)
p("count regen:", len(regen))
p("stall rows (b_{k+1}==b_k):", stall, "count:", len(stall))
p("erosion rows count:", len(erode))
p("transition diffs set:", sorted(set(diffs)))
p("regen gaps (consecutive diff, powers of 2?):", [regen[i + 1] - regen[i] for i in range(len(regen) - 1)])
p("jump sizes:", jumps)
p("jump sizes powers of 2?", [j for j in jumps if j & (j - 1) == 0])
p("erosion run lengths:", erun, "max:", max(erun))
p("minima (k, b_k):", minima)
p("minima b-values:", [v for (_, v) in minima])

# ---- Rule-90 prediction tests ----
def nearest_pow2_dist(n):
    lo = 1 << (n.bit_length() - 1)
    hi = lo << 1
    return min(n - lo, hi - n)

gaps = [regen[i + 1] - regen[i] for i in range(len(regen) - 1)]
pw2 = [g for g in gaps if g & (g - 1) == 0]
p("P1 gaps all powers of 2?", len(pw2) == len(gaps), f"({len(pw2)}/{len(gaps)} are powers of 2; non-powers: {[g for g in gaps if not (g & (g-1) == 0)]})")
p("P3 jumps all powers of 2?", len([j for j in jumps if j & (j - 1) == 0]) == len(jumps))

# P2: distance to nearest power of 2 for regen rows vs all rows
all_rows = list(range(1, GEN + 1))
d_regen = [nearest_pow2_dist(r) for r in regen]
d_all = [nearest_pow2_dist(r) for r in all_rows]
import statistics
p("P2 mean dist-to-pow2: regen rows %.3f vs all rows %.3f" % (statistics.mean(d_regen), statistics.mean(d_all)))
p("P2 median dist-to-pow2: regen rows", statistics.median(d_regen), "vs all rows", statistics.median(d_all))
p("P2 regen rows exactly powers of 2:", [r for r in regen if r & (r - 1) == 0])

open("code/out/sequence_dump.txt", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))