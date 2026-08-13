#!/usr/bin/env python3
"""Extract the integer sequences of record from code/out/blocks_depth1000.json
into plain text files for the sequence tools.

Sequences written (one term per line, index j = row k = j+1):
  b.txt          block length (leading {0,2} count), k=1..1000 (tail k>=162 is
                 the finite-width artifact: b = W-k-1)
  b_genuine.txt  same, k=1..161 only (real dynamics)
  s.txt          second entry A_k(1) in {0,2}, k=1..1000
  bits.txt       s/2, k=1..1000 (binary)
  intruder.txt   first value past the block, k=1..161 (None -> empty line)
  diffs.txt      b_{k+1}-b_k, k=1..160 (genuine transitions)
  minima_b.txt   values of b at local minima (from this file: positions where
                 b_k < b_{k-1} and b_k < b_{k+1}, i.e. strict local minima)
  regen_rows.txt row indices k (1-based) with b_{k+1} >= b_k, k=1..161
  jumps.txt      jump sizes b_{k+1}-b_k at regen rows, k=1..161
"""
import json

with open("code/out/blocks_depth1000.json") as f:
    data = json.load(f)

b = data["b"]          # index j -> row k=j+1
s = data["s"]
intruder = data["intruder"]
K = len(b)             # 1000

def dump(name, seq):
    with open(f"code/pattern_finder/{name}", "w") as f:
        for x in seq:
            f.write("" if x is None else str(x))
            f.write("\n")
    print(f"{name}: {len(seq)} terms, first 12 = {[x for x in seq[:12]]}")

dump("b.txt", b)
dump("b_genuine.txt", b[:161])
dump("s.txt", s)
dump("bits.txt", [x // 2 for x in s])
dump("intruder.txt", intruder[:161])
dump("diffs.txt", [b[i + 1] - b[i] for i in range(160)])

# strict local minima in genuine regime (k=2..160, compare neighbours)
mins = []
for i in range(1, 160):
    if b[i] < b[i - 1] and b[i] < b[i + 1]:
        mins.append((i + 1, b[i]))
print("strict local minima (k, b):", mins)
dump("minima_b.txt", [v for _, v in mins])
dump("minima_rows.txt", [k for k, _ in mins])

regen = [i + 1 for i in range(161) if b[i + 1] >= b[i]]
print("regen rows count:", len(regen))
dump("regen_rows.txt", regen)
dump("jumps.txt", [b[i + 1] - b[i] for i in range(161) if b[i + 1] >= b[i]])

# s-run lengths (runs of equal consecutive s)
runs0 = []
runs2 = []
cur = s[0]
cnt = 1
for x in s[1:]:
    if x == cur:
        cnt += 1
    else:
        (runs0 if cur == 0 else runs2).append(cnt)
        cur, cnt = x, 1
(runs0 if cur == 0 else runs2).append(cnt)
print("s runs of 0:", runs0)
print("s runs of 2:", runs2)
dump("s_runs0.txt", runs0)
dump("s_runs2.txt", runs2)