#!/usr/bin/env python3
"""Verify exact-empirical laws in the genuine regime (k=1..161) of blocks_depth1000.

Law 1 (intruder transition law): c_k = A_k[b_k+1] always in {4,6,8,10,12,14};
  - if c_k >= 6 then c_{k+1} in {c_k, c_k - 2} (never up, never down by more than 2)
  - if c_k == 4 then c_{k+1} in {4,6,8,10,12,14} (never down, never odd)
  over all 160 live transitions.

Law 2 (up-jumps from 4 coincide with regeneration): rows where c_{k+1} > c_k
  are exactly regeneration rows (b_{k+1} >= b_k), and rows where c_{k+1} < c_k
  are exactly erosion rows (b_{k+1} == b_k - 1).

Law 3 (no odd intruders ever): c_k even for all k in live regime.

Also: distribution statistics of s_k (second entries, 1000 rows).
"""
import json

D = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = D["b"], D["s"], D["intruder"]
c = intr[:161]
assert len(c) == 161

# ---- Law 1 ----
vals = set(c)
print("Law 1: c values observed:", sorted(vals), "| any odd?", any(v % 2 for v in c))
fail1 = []
down_ok = up_ok = stay = up = down = 0
for k in range(160):
    ck, cn = c[k], c[k + 1]
    if ck >= 6:
        if cn == ck:
            stay += 1
        elif cn == ck - 2:
            down_ok += 1
        else:
            fail1.append((k + 1, ck, cn))
    elif ck == 4:
        if cn == 4:
            stay += 1
        elif cn in (6, 8, 10, 12, 14):
            up += 1
        else:
            fail1.append((k + 1, ck, cn))
    else:
        fail1.append((k + 1, ck, cn))
print("Law 1 failures:", fail1 if fail1 else "NONE (160/160)")
print("  from c>=6: stay %d, drop-2 %d; from c=4: stay %d, up %d" % (stay, down_ok, stay2 := 0, up))
# recompute a bit more carefully
stay61 = stay
stay4 = sum(1 for k in range(160) if c[k] == 4 and c[k + 1] == 4)
print("  exact: from c>=6 stay %d drop-2 %d; from c=4 stay %d up %d "
      % (sum(1 for k in range(160) if c[k] >= 6 and c[k+1] == c[k]),
         sum(1 for k in range(160) if c[k] >= 6 and c[k+1] == c[k]-2),
         stay4, up))

# ---- Law 2 ----
up_rows = [k + 1 for k in range(160) if c[k + 1] > c[k]]
down_rows = [k + 1 for k in range(160) if c[k + 1] < c[k]]
regen_rows = [k + 1 for k in range(160) if b[k + 1] >= b[k]]
erode_rows = [k + 1 for k in range(160) if b[k + 1] < b[k]]
print("Law 2: c-up rows == regen rows?", set(up_rows) == set(regen_rows))
print("  c-up rows:", up_rows)
print("  regen rows:", regen_rows)
print("  symmetric diff:", sorted(set(up_rows) ^ set(regen_rows)))
print("  c-down rows == erode rows?", set(down_rows) == set(erode_rows),
      "| sym diff:", sorted(set(down_rows) ^ set(erode_rows)))
print("Law 3 (c even always):", all(v % 2 == 0 for v in c))

# ---- s stats ----
print("s: zeros", s.count(0), "twos", s.count(2), "len", len(s))
print("s first 161 as bits:", [1 if v == 2 else 0 for v in s])