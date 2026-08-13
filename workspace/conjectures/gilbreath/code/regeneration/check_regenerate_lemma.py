#!/usr/bin/env python3
"""Verify the regeneration lemma against the REAL Gilbreath absolute-difference
rows of the primes, and report the indexing correction needed to make it true.

Conventions (0-based within each row; A_k[0] is the leading 1 for all k):
  A_0 = primes ; A_{k+1}[j] = |A_k[j] - A_k[j+1]|   (row width shrinks by 1)
  b_k   = block_profile(row k): the number j>=1 of leading entries of row k
          that lie in {0,2}.  Block occupies 0-based indices 1..b_k.
  row width of A_k = (num_primes - 1) - (k - 1) = num_primes - k.

The task's literal reading used e_k=A_k[b_k-1], c_k=A_k[b_k+1],
q_k=A_{k+1}[b_k-1].  Because A_{k+1}[j] = |A_k[j]-A_k[j+1]|, the diff partner
of the intruder c_k=A_k[b_k+1] is A_k[b_k], NOT A_k[b_k-1].  So the correct
("true-end") reading is e_k=A_k[b_k], c_k=A_k[b_k+1], q_k=A_{k+1}[b_k], and
q_k == |e_k - c_k| identically.  Both readings are checked below.

Lemma (corrected): for every k with an intruder (b_k+1 < width),
  q_k in {0,2}  IFF  (e_k==2 and c_k==4)
and therefore  b_{k+1} >= b_k  IFF  (e_k==2 and c_k==4).

Rows generated one at a time (three consecutive rows held), numpy int64,
sieve to 20 000 000, depth 1000.  Oracle: first-40 block lengths and second
entries must match code/out/witnesses.json exactly.
"""
import json, os
import numpy as np
from lib.gilbreath import primes_up_to

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = json.load(open(os.path.join(HERE, "..", "out", "witnesses.json")))
SIEVE_LIMIT = 20_000_000
DEPTH = 1000

primes = np.array(primes_up_to(SIEVE_LIMIT), dtype=np.int64)
N0 = len(primes)
print(f"primes in (2, {SIEVE_LIMIT}): {N0}")

def block_profile(row):
    n = 0
    for x in row[1:]:
        if x == 0 or x == 2:
            n += 1
        else:
            break
    return n

# ---------------- Oracle: first-40 rows vs witnesses.json ----------------
w40 = WITNESS["block_profile_first_40"]
want_blk = [r["block"] for r in w40]
want_sec = [r["second"] for r in w40]
got_blk, got_sec = [], []
cur = primes.copy()
for k in range(1, 41):
    cur = np.abs(np.diff(cur))
    got_blk.append(block_profile(cur))
    got_sec.append(int(cur[1]))
ok_b = got_blk == want_blk
ok_s = got_sec == want_sec
print(f"oracle first-40 block lengths match witnesses.json : {ok_b}")
print(f"oracle first-40 second entries match witnesses.json : {ok_s}")
if not (ok_b and ok_s):
    print("ORACLE MISMATCH -- aborting, results untrustworthy.")
    raise SystemExit(1)
print("oracle PASS\n")

# ---------------- Full pass over all 999 transitions ----------------
r0 = primes.copy()
r1 = np.abs(np.diff(r0))          # A_1

resA = {"checked": 0, "iff_fail": 0, "id_mismatch": 0, "regen_fail": 0, "hold": 0}
resB = {"checked": 0, "iff_fail": 0, "id_mismatch": 0, "regen_fail": 0, "hold": 0}
pair_dist = {}     # (e,c) pairs, corrected indexing, meaningful range
q_dist = {}
first_failA = None
no_intruder = 0
no_intruder_regen = 0
all_regen = 0
for k in range(1, 1000):
    r2 = np.abs(np.diff(r1))      # A_{k+1}
    b = block_profile(r1)
    width = len(r1)
    bnext = block_profile(r2)
    if bnext >= b:
        all_regen += 1
    if b + 1 >= width:            # no intruder: block runs to end of row
        no_intruder += 1
        if bnext >= b:
            no_intruder_regen += 1
        r0, r1 = r1, r2
        continue
    c = int(r1[b + 1])            # intruder
    # variant A (literal task)
    eA = int(r1[b - 1]); qA = int(r2[b - 1])
    resA["checked"] += 1
    if qA != abs(eA - c):
        resA["id_mismatch"] += 1
    lhsA = (qA in (0, 2)); rhsA = (eA == 2 and c == 4)
    if lhsA != rhsA:
        resA["iff_fail"] += 1
        if first_failA is None:
            first_failA = (k, b, eA, c, qA)
    if (block_profile(r2) >= b) != rhsA:
        resA["regen_fail"] += 1
    if lhsA and rhsA:
        resA["hold"] += 1
    # variant B (corrected: true end of block)
    eB = int(r1[b]); qB = int(r2[b])
    resB["checked"] += 1
    if qB != abs(eB - c):
        resB["id_mismatch"] += 1
    lhsB = (qB in (0, 2)); rhsB = (eB == 2 and c == 4)
    if lhsB != rhsB:
        resB["iff_fail"] += 1
    if (block_profile(r2) >= b) != rhsB:
        resB["regen_fail"] += 1
    if lhsB and rhsB:
        resB["hold"] += 1
    pair = (eB, c)
    pair_dist[pair] = pair_dist.get(pair, 0) + 1
    q_dist[qB] = q_dist.get(qB, 0) + 1
    r0, r1 = r1, r2

print("=" * 64)
print("VARIANT A -- literal task reading  (e=A_k[b_k-1], q=A_{k+1}[b_k-1])")
print("=" * 64)
print(f"  transitions with an intruder:  {resA['checked']}")
print(f"  q == |e-c|  mismatches:        {resA['id_mismatch']}")
print(f"  IFF failures (q in {{0,2}} iff e==2&c==4): {resA['iff_fail']}")
print(f"  REGEN failures (b_next>=b iff e==2&c==4): {resA['regen_fail']}")
print(f"  first failure example:          {first_failA}")
print()
print("=" * 64)
print("VARIANT B -- corrected reading     (e=A_k[b_k], q=A_{k+1}[b_k])")
print("=" * 64)
print(f"  transitions with an intruder:  {resB['checked']}")
print(f"  q == |e-c|  mismatches:        {resB['id_mismatch']}")
print(f"  IFF failures (q in {{0,2}} iff e==2&c==4): {resB['iff_fail']}")
print(f"  REGEN failures (b_next>=b iff e==2&c==4): {resB['regen_fail']}")
print(f"  transitions where e==2&c==4 (regeneration events): {resB['hold']}")
print()
print("distribution of q_k = A_{k+1}[b_k]  (corrected), over meaningful rows:")
print("   " + ", ".join(f"q={q}:{n}" for q, n in sorted(q_dist.items())))
print("distribution of (e_k, c_k) pairs (corrected) over meaningful rows:")
for pair, n in sorted(pair_dist.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"   (e={pair[0]}, c={pair[1]}): {n}")

print()
print("full-998-transition check of 'b_{k+1} >= b_k  iff  (e==2 and c==4)':")
print(f"  transitions with no intruder (whole row in {{0,2}}): {no_intruder}")
print(f"    among them with b_{{k+1}} >= b_k: {no_intruder_regen} "
      f"(0 required for the iff to hold across all 998)")
print(f"  total regeneration events (b_{{k+1}} >= b_k) over all 998: {all_regen}")
print(f"  regeneration events at meaningful rows with e==2&c==4: {resB['hold']}")
print(f"  remaninder (must be 0): {all_regen - resB['hold']}")
