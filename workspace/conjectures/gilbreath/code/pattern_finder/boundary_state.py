#!/usr/bin/env python3
"""Extract the exact boundary-automaton state per row, using the real rows.

For k = 1..161 (live regime) with block length b_k, define
    w_k = A_k[b_k-2], i_k = A_k[b_k-1], e_k = A_k[b_k]   (last three {0,2} entries)
    c_k = A_k[b_k+1]                                     (intruder, even >= 4)

Claims to check exactly against the record:
  L1. regen (b_{k+1} >= b_k)  <=>  (e_k == 2 and c_k == 4)          [established]
  L2. on erosion (b_{k+1} == b_k - 1):  c_{k+1} == c_k - e_k        [intruder never up]
  L3. on erosion:  e_{k+1} == i_k XOR e_k,  i_{k+1} == w_k XOR i_k  [trailing shove]
  L4. (0,0) pairs (i_k == e_k == 0) never occur                     [no "00" block end]
  L5. c_k <= 14 in live regime; c always even.
Also dump the sequences:
  e_bits.txt  (e_k/2), t_bits.txt (A_k[2]/2), s_bits.txt (A_k[1]/2),
  c.txt       intruder, run lengths of erosion, regen gaps.
Oracle first: numpy int64 rows must reproduce witnesses.json rows A_1..A_5 first 12.
"""
import json
import numpy as np
from lib.gilbreath import primes_up_to

# ---- oracle check first ----
EXPECTED = {1: [1,2,2,4,2,4,2,4,6,2,6,4], 2: [1,0,2,2,2,2,2,2,4,4,2,2],
            3: [1,2,0,0,0,0,0,2,0,2,0,0], 4: [1,2,0,0,0,0,2,2,2,2,0,0],
            5: [1,2,0,0,0,2,0,0,0,2,0,2]}
primes = np.array(primes_up_to(200), dtype=np.int64)
row = primes.copy()
for k in range(1, 6):
    row = np.abs(np.diff(row))
    assert row[:12].tolist() == EXPECTED[k], f"oracle mismatch at k={k}"
print("numpy int64 oracle: rows A_1..A_5 first 12 match problem.md exactly")

# ---- full regeneration to depth 162 (live regime k=1..161) ----
LIMIT = 20_000_000
primes = np.array(primes_up_to(LIMIT), dtype=np.int64)
print("primes:", len(primes))
rows = [primes]
r = primes
for k in range(1, 163):
    r = np.abs(np.diff(r))
    rows.append(r)

# compare b with the record
with open("code/out/blocks_depth1000.json") as f:
    rec = json.load(f)
b_rec = rec["b"][:161]
intr_rec = rec["intruder"][:161]

def block_len(row):
    n = 0
    for x in row[1:]:
        if x == 0 or x == 2:
            n += 1
        else:
            break
    return n

s_bits, t_bits, e_bits, w_bits, i_bits, c_vals, b_vals = [], [], [], [], [], [], []
bad_b = []
for k in range(1, 162):
    rowk = rows[k]
    bk = block_len(rowk)
    b_vals.append(bk)
    if bk != b_rec[k - 1]:
        bad_b.append((k, bk, b_rec[k - 1]))
    c_vals.append(int(rowk[bk + 1]))
    e_bits.append(int(rowk[bk]) // 2)
    i_bits.append(int(rowk[bk - 1]) // 2)
    w_bits.append(int(rowk[bk - 2]) // 2)
    s_bits.append(int(rowk[1]) // 2)
    t_bits.append(int(rowk[2]) // 2)

print("b mismatches vs record:", bad_b if bad_b else "none")
print("c mismatches vs record:",
      [ (k, c_vals[k-1], intr_rec[k-1]) for k in range(1,162) if c_vals[k-1] != intr_rec[k-1] ] or "none")

# ---- verify the laws ----
n_reg = n_ero = 0
fail_L1, fail_L2, fail_L3a, fail_L3b, zero00 = [], [], [], [], []
erosion_run = None
runs = []
for k in range(1, 161):
    e, i, w, c = e_bits[k-1]*2, i_bits[k-1]*2, w_bits[k-1]*2, c_vals[k-1]
    e1 = b_vals[k]   # b_{k+1}
    regen = e1 >= b_vals[k-1]
    if regen != (e == 2 and c == 4):
        fail_L1.append(k)
    if regen:
        n_reg += 1
        if erosion_run is not None:
            runs.append(erosion_run)
            erosion_run = None
    else:
        n_ero += 1
        # erosion: c_{k+1} == c_k - e_k
        if c_vals[k] != c - e:
            fail_L2.append((k, c_vals[k], c, e))
        # e_{k+1} == |i - e| (XOR since both in {0,2})
        if e_bits[k] != (i_bits[k-1] ^ e_bits[k-1]):
            fail_L3a.append((k, e_bits[k], i_bits[k-1], e_bits[k-1]))
        # i_{k+1} == |w - i|
        if i_bits[k] != (w_bits[k-1] ^ i_bits[k-1]):
            fail_L3b.append((k, i_bits[k], w_bits[k-1], i_bits[k-1]))
        erosion_run = erosion_run + 1 if erosion_run is not None else 1
if erosion_run is not None:
    runs.append(erosion_run)
for k in range(1, 162):
    if i_bits[k-1] == 0 and e_bits[k-1] == 0:
        zero00.append(k)

print(f"regen rows: {n_reg}, erosion rows: {n_ero}")
print("L1 failures:", fail_L1 or "none")
print("L2 (c drain) failures:", fail_L2 or "none")
print("L3a (e shove) failures:", fail_L3a or "none")
print("L3b (i shove) failures:", fail_L3b or "none")
print("rows with (i,e)=(0,0):", zero00 or "none")
print("erosion runs:", runs, "max:", max(runs) if runs else 0)

# run starts: intruder value at first row of each run
starts = []
idx = 0
for L in runs:
    starts.append((idx + 1, c_vals[idx], b_vals[idx]))  # k of run start, c at start
    idx += L + 1  # skip run + the regen row
print("erosion run starts (k, c_at_start, b_at_start):", starts)

def dump(name, seq):
    with open(f"code/pattern_finder/{name}", "w") as f:
        for x in seq:
            f.write(str(x) + "\n")

dump("e_bits.txt", e_bits)
dump("i_bits.txt", i_bits)
dump("w_bits.txt", w_bits)
dump("s_bits.txt", s_bits)
dump("t_bits.txt", t_bits)
dump("c.txt", c_vals)
dump("b_genuine2.txt", b_vals)
print("wrote sequences")