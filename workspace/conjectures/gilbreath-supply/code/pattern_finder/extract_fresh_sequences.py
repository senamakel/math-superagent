#!/usr/bin/env python3
"""Extract fresh exact sequences from the canonical nu2 JSON that have not
been through the sequence tools:

  (A) dyadic  nu2(2^k)          k = 2..15
  (B) near-dyadic nu2(2^k + 1), nu2(2^k - 1)
  (C) record-low positions of nu2(n)/n on n in [50, 40000] (running min
      updates) and the record values as exact fractions; likewise record
      highs of S(n)/n where S(n) = (n-2) - 2*nu2(n).
  (D) exact sets {n : nu2(n) <= k} for k = 1..15, their sizes and maxima.

Guards re-verified: nu2(53)=18, nu2(64)=27, nu2(4000)=1975, nu2(40000)=20081.
Convention d in [2, n-1] (the operative floored range). All arithmetic exact;
the fractions nu2(n)/n and S(n)/n are printed as floats ONLY for display, the
record comparison uses exact integer cross-multiplication.
"""
import json

d = json.load(open('/workspace/code/out/nu2_primes_xor_40000.json'))
assert d[53] == 18 and d[64] == 27 and d[4000] == 1975 and d[40000] == 20081, \
    "guards failed"
assert len(d) == 40001
N = 40000

def nu2(n):
    assert 0 <= n <= N
    return d[n]

def S(n):
    return (n - 2) - 2 * nu2(n)

out = []
out.append("guards: nu2(53)=18 nu2(64)=27 nu2(4000)=1975 nu2(40000)=20081  (all pass)")
out.append("convention: floored d in [2, n-1]; json d[i] = nu2(i)")

# ---- (A) dyadic and near-dyadic ----
out.append("\n== (A) dyadic and near-dyadic subsequences (exact) ==")
for k in range(2, 16):
    p = 1 << k
    out.append(f"k={k:2d} 2^k={p:6d}  nu2(2^k)={nu2(p):5d}  "
               f"nu2(2^k+1)={nu2(p+1):5d}  nu2(2^k-1)={nu2(p-1):5d}  "
               f"S(2^k)={S(p):6d}  nu2(2^k)/2^k={nu2(p)/p:.6f}")
dyadic = [nu2(1 << k) for k in range(2, 16)]
dyadic_p1 = [nu2((1 << k) + 1) for k in range(2, 16)]
dyadic_m1 = [nu2((1 << k) - 1) for k in range(2, 16)]
out.append("nu2(2^k)   k=2..15: " + " ".join(map(str, dyadic)))
out.append("nu2(2^k+1) k=2..15: " + " ".join(map(str, dyadic_p1)))
out.append("nu2(2^k-1) k=2..15: " + " ".join(map(str, dyadic_m1)))

# ---- (C) record lows of nu2(n)/n and record highs of S(n)/n on [50, N] ----
# record low: n where nu2(n)/n < all previous (exact cross-multiplication)
out.append("\n== (C) record extremes of nu2(n)/n over n in [50, 40000] ==")
record_low_pos, record_low_val = [], []
cur_num, cur_den = nu2(50), 50
for n in range(50, N + 1):
    num, den = nu2(n), n
    if num * cur_den < cur_num * den:          # new strict record low
        record_low_pos.append(n)
        record_low_val.append(num / den)
        cur_num, cur_den = num, den
out.append("record-low positions: " + " ".join(map(str, record_low_pos)))
out.append(f"count={len(record_low_pos)}")
out.append("record-low values (nu2/n): " + " ".join(f"{v:.6f}" for v in record_low_val))
out.append("record-low nu2 values: " + " ".join(str(nu2(n)) for n in record_low_pos))
if len(record_low_pos) > 1:
    gaps = [record_low_pos[i + 1] - record_low_pos[i] for i in range(len(record_low_pos) - 1)]
    out.append("gaps between record-low positions: " + " ".join(map(str, gaps)))
    out.append("gap ratios (r_{i+1}/r_i of consecutive record values 1/2 - nu2/n): "
               + " ".join(
                   f"{(0.5 - record_low_val[i + 1])/(0.5 - record_low_val[i]):.4f}"
                   for i in range(len(record_low_val) - 1)))

# record high of S(n)/n (S sums n-2 terms in {+-1}; S(n)/n up to 1)
out.append("\n== (C2) record highs of S(n)/n over n in [50, 40000] (exact) ==")
rec_hi_pos, rec_hi_val = [], []
curS, curD = S(50), 50
for n in range(50, N + 1):
    s = S(n)
    if s * curD > curS * n:                     # new record high of S/n
        rec_hi_pos.append(n)
        rec_hi_val.append(s / n)
        curS, curD = s, n
out.append("record-high S/n positions: " + " ".join(map(str, rec_hi_pos)))
out.append(f"count={len(rec_hi_pos)}")
out.append("record-high S/n values: " + " ".join(f"{v:.6f}" for v in rec_hi_val))
out.append("record-high S values: " + " ".join(str(S(n)) for n in rec_hi_pos))
if len(rec_hi_pos) > 1:
    gaps = [rec_hi_pos[i + 1] - rec_hi_pos[i] for i in range(len(rec_hi_pos) - 1)]
    out.append("gaps: " + " ".join(map(str, gaps)))

# ---- (D) small-nu2 sets ----
out.append("\n== (D) exact sets {n in [2,40000] : nu2(n) <= k}, k = 1..15 ==")
for k in range(1, 16):
    members = [n for n in range(2, N + 1) if nu2(n) <= k]
    out.append(f"k={k:2d}: size={len(members):3d} max={max(members):6d}  "
               f"members={members[:26]}{'...' if len(members) > 26 else ''}" if members
               else f"k={k:2d}: empty")

# record-low positions table with (n, nu2, S, nu2/n, S/n)
out.append("\n== record-low detail (n, nu2(n), S(n), nu2/n, S/n) ==")
for n in record_low_pos:
    out.append(f"  n={n:6d}  nu2={nu2(n):5d}  S={S(n):6d}  "
               f"nu2/n={nu2(n)/n:.6f}  S/n={S(n)/n:.6f}")

print("\n".join(out))