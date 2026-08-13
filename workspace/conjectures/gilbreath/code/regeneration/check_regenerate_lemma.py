#!/usr/bin/env python3
"""Verify the regeneration lemma against the REAL Gilbreath rows.

Conventions (task statement):
  row k (1-indexed), A_k = the k-th absolute-difference row of the primes;
  A_k[0] is the leading 1 (always), so positions are 0-based within the row.
  b_k = length of the leading {0,2} block = consecutive entries of row k
        starting at 0-based index 1 that lie in {0,2}  (block_profile).
        Thus the block occupies 0-based indices 1..b_k; the last block value
        is at index b_k and the first non-{0,2} value (the intruder) at b_k+1.
  c_k = intruder      = A_k[b_k+1]   (0-based)
  e_k = edge          = A_k[b_k-1]   (0-based, per explicit index given)
  q_k = A_{k+1}[b_k-1]  (real value of row k+1 at 0-based column b_k-1)

Lemma under test, for every k in 1..999 (998 transitions):
  q_k in {0,2}   IFF   (e_k == 2 and c_k == 4)
and therefore
  b_{k+1} >= b_k IFF   (e_k == 2 and c_k == 4)

Rows generated one at a time (keep previous+current only), numpy int64,
sieve to 20 000 000, depth 1000.  Oracle: first-40 block lengths and second
entries of the REAL rows must match code/out/witnesses.json exactly.
"""
import json, os
import numpy as np
from lib.gilbreath import primes_up_to

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = json.load(open(os.path.join(HERE, "..", "out", "witnesses.json")))
DEPTH = 1000
SIEVE_LIMIT = 20_000_000

# --------------------------------------------------------------------------
# Sieve to 20M and turn into a numpy int64 array.  Sieve cost is
# O(S log log S) time, O(S) bytes.  Row diffusion is O(depth * width).
# --------------------------------------------------------------------------
primes = np.array(primes_up_to(SIEVE_LIMIT), dtype=np.int64)
N0 = len(primes)
print(f"primes > 2 and < {SIEVE_LIMIT}: {N0}")

# block_profile on a numpy row
def block_profile(row):
    length = 0
    for x in row[1:]:
        if x == 0 or x == 2:
            length += 1
        else:
            break
    return length

# --------------------------------------------------------------------------
# Oracle check: first-40 block lengths and second entries vs witnesses.json
# --------------------------------------------------------------------------
w_b = WITNESS["block_profile_first_40"]
w_s = [row["second"] for row in w_b]
w_blk = [row["block"] for row in w_b]

prev = None          # row k   (A_k)
cur = primes.copy()  # row 0 = primes (A_0)
rows_by_idx = {}     # hold rows 0..1 only? we need consecutive; use prev/cur

# We'll store b_k, s_k, and needed entries per k, one pass, keeping prev+cur.
# Step structure: initial cur = A_0; then each iteration produces A_1..A_DEPTH.
# We maintain prev = A_{k-1}, cur = A_k.
# To compute q_k = A_{k+1}[b_k-1] we need three consecutive rows; handle by
# iterating k = 1..999 and using prev(A_{k-1}), cur(A_k), next(A_{k+1}).

# Initialize: advance to A_1.
# A_0 = primes. We need prev = A_0, cur = A_1 at k=1.
def diff_pass(row):
    return np.abs(np.diff(row))

rows = {}
# Generate all rows but store only what we need per k:
#   A_k[b_k-1], A_k[b_k+1], and for next row A_{k+1}[b_k-1].
# Simplest: iterate holding previous row k-1 and current row k; after the
# oracle (which needs A_1..A_40 fully for block_profile), we switch to the
# per-k extractor.  Actually block_profile needs the full row, so do the
# first 40 fully, then continue with wide-row extractor.

# ---- Phase A: rows 1..40 fully (for oracle) ----
gen_cur = primes.copy()
oracle_block = []
oracle_second = []
for k in range(1, 41):
    gen_cur = diff_pass(gen_cur)            # becomes A_k
    oracle_block.append(block_profile(gen_cur))
    oracle_second.append(int(gen_cur[1]))

ok_b = (oracle_block == w_blk)
ok_s = (oracle_second == w_s)
print(f"oracle first-40 block lengths match witnesses.json : {ok_b}")
print(f"oracle first-40 second entries match witnesses.json : {ok_s}")
if not (ok_b and ok_s):
    print("MISMATCH with oracle; aborting.")
    raise SystemExit(1)
print("oracle PASS (first 40 rows block lengths + second entries == witnesses.json)")

# ---- Phase B: full pass k=1..999 across all rows ----
# prev = A_{k-1}, cur = A_k.  Start by bringing cur to A_40 (we already have
# it as gen_cur after the loop above).
A = gen_cur               # this is A_40
prev = None               # we will set prev for k=41.. by tracking
# We only actually need, for each k: b_k, A_k[b_k-1], A_k[b_k+1], A_{k+1}[b_k-1].
# Rebuild from scratch holding three consecutive rows to avoid index juggling:
# keep r_{k-1}, r_k, and compute r_{k+1} on the fly.

# Start fresh at k=1: r0 = primes, r1 = A_1 = diff_pass(primes).
r0 = primes.copy()
r1 = diff_pass(r0)

fake_violations = 0
pair_dist = {}
q_dist = {}
id_checks = {"q_equals_abs_e_minus_c": 0, "q_not_equals_abs_e_minus_c": 0}
regen_fail = 0
edge_is_last_block_val_fail = 0

# We need b_{k+1} for the "b_{k+1} >= b_k" half; b comes from row k+1 profile,
# but we can compute b_{k+1} directly from r_{k+1}.  Keep last b too.
prev_b = None
for k in range(1, 1000):
    r2 = diff_pass(r1)   # r2 = A_{k+1}
    b_k = block_profile(r1)
    e_k = int(r1[b_k - 1])
    c_k = int(r1[b_k + 1])
    q_k = int(r2[b_k - 1])
    # real last block value is at index b_k
    real_last = int(r1[b_k])
    if real_last != e_k:
        edge_is_last_block_val_fail += 1
    # identity q_k = |e_k - c_k|?  (task states this; check truth)
    if q_k == abs(e_k - c_k):
        id_checks["q_equals_abs_e_minus_c"] += 1
    else:
        id_checks["q_not_equals_abs_e_minus_c"] += 1
    q_dist[q_k] = q_dist.get(q_k, 0) + 1
    pair = (e_k, c_k)
    pair_dist[pair] = pair_dist.get(pair, 0) + 1

    lemma_lhs = (q_k in (0, 2))
    lemma_rhs = (e_k == 2 and c_k == 4)
    if lemma_lhs != lemma_rhs:
        fake_violations += 1
        print(f"  [IFF FAIL] k={k} b={b_k} e={e_k} c={c_k} q={q_k} "
              f"q_in{{0,2}}={lemma_lhs} rhs={lemma_rhs}")

    # b_{k+1} >= b_k iff (e_k==2 and c_k==4)
    b_next = block_profile(r2)
    reg_lhs = (b_next >= b_k)
    if reg_lhs != lemma_rhs:
        regen_fail += 1
        print(f"  [REGEN FAIL] k={k} b={b_k}->{b_next} e={e_k} c={c_k}")

    r0 = r1
    r1 = r2

print("\n================ RESULTS ================")
print(f"transitions checked (k=1..999): 998")
print(f"[IFF] count where 'q_k in {{0,2}} iff (e==2 and c==4)' FAILS : {fake_violations}")
print(f"[REGEN] count where 'b_{{k+1}} >= b_k iff (e==2 and c==4)' FAILS : {regen_fail}")
print(f"[EDGE] count where e_k != true last-block-value (A_k[b_k]): {edge_is_last_block_val_fail}")
print(f"[ID] count where q_k == |e_k - c_k|  : {id_checks['q_equals_abs_e_minus_c']} "
      f"(of 998)")
print(f"[ID] count where q_k != |e_k - c_k|  : {id_checks['q_not_equals_abs_e_minus_c']}")
print(f"distribution of q_k = A_{{k+1}}[b_k-1] values: {dict(sorted(q_dist.items()))}")
print("distribution of (e_k, c_k) pairs over 998 transitions:")
for pair, cnt in sorted(pair_dist.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"    (e={pair[0]}, c={pair[1]}): {cnt}")
