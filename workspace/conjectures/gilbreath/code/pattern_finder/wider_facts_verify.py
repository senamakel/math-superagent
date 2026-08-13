#!/usr/bin/env python3
"""Verify and record the new wider-width facts:
1. exact jumps at formerly-capped giants (rows 161, 174), from the A record;
2. longest pure-erosion run in the live regime (rows 1..238);
3. log-log jump-vs-b slope: old (12 depth-1000 giants) vs new (14 wider giants);
4. directive25 sublinear model rho = 1 + 802.6*b^-0.612 tested on the new points;
5. chain value-range structure: min/max halved value over the 1-Lipschitz chain
   at each giant (needs the row; recompute streaming at sieve 3e8 for rows
   155..176 only -- costs ~4 rows of diff work... actually the row at 161 needs
   the full triangle descent, so streaming full depth again; ~100s).
"""
import json, math

A = json.load(open('/workspace/code/out/wider_width_b.json'))
b = A['b']

# 1. exact jumps
j161 = b[161] - b[160]   # 0-based: row 161 (1-based) -> 162
j174 = b[174] - b[173]
print(f"exact jump row 161->162: {j161}  (was capped >=176181 at depth 1000)")
print(f"exact jump row 174->175: {j174}  (new giant, beyond old record)")
j239 = b[239] - b[238]
print(f"jump row 239->240 (capped at width 3e8, landing flooring 0): {j239}")

# 2. pure-erosion runs in live regime rows 1..238 (transitions 1..237)
runs = []
cur = 0
for k in range(1, 238):  # transition k -> k+1
    d = b[k] - b[k-1]
    if d == -1:
        cur += 1
    else:
        if cur:
            runs.append((cur, k - cur, k - 1))  # length, start row (1-based), end row
        cur = 0
if cur: runs.append((cur, 238 - cur, 237))
runs.sort(reverse=True)
print(f"\nlongest pure-erosion runs (live regime rows 1..238): top 5 {runs[:5]}")
print(f"(depth-1000 live regime max was 13; wider record max = {runs[0][0]})")

# 3. log-log fits
def lsq(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    sxx = sum((x-mx)**2 for x in xs); sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    m = sxy/sxx; c = my - m*mx
    ss = sum((y-(m*x+c))**2 for x, y in zip(xs, ys)); sst = sum((y-my)**2 for y in ys)
    return m, c, 1 - ss/sst

# depth-1000 12 genuine giants (src rows 34..146): b_k and jumps
bk12 = [865, 4203, 5939, 23262, 31532, 92619, 103960, 141706, 271620, 325096, 515907, 733575]
j12  = [1314, 1739, 17326, 8237, 61088, 11354, 37746, 129923, 53470, 190810, 217657, 360698]
m12, _, r12 = lsq([math.log(x) for x in bk12], [math.log(x) for x in j12])
print(f"\nlog-log jump vs b: 12 depth-1000 giants: alpha={m12:.4f} R2={r12:.4f}")

bk14 = bk12 + [1094263, 5417976]
j14  = j12  + [4323712, 5237310]
m14, _, r14 = lsq([math.log(x) for x in bk14], [math.log(x) for x in j14])
print(f"log-log jump vs b: 14 wider giants:     alpha={m14:.4f} R2={r14:.4f}")
print("ratio jump/b_k, 14 giants:",
      [round(j/bk, 3) for bk, j in zip(bk14, j14)])

# 4. directive25 sublinear model on the new points
print("\ndirective25 sublinear model rho = 1 + 802.6*b^-0.612:")
for i in range(len(bk14)-1):
    r = j14[i+1]/bk14[i+1] + 1 if False else None  # (placeholder, use landing ratios)
land14 = [2179, 5942, 23265, 31499, 92620, 103973, 141706, 271629, 325090, 515906, 733564, 1094273, 5417975, 10655286]
rhos = [land14[i+1]/land14[i] for i in range(13)]
for i in range(13):
    pred = 1 + 802.6 * (land14[i] ** -0.612)
    print(f"  b={land14[i]:>10} pred {pred:7.3f} actual {rhos[i]:7.3f} "
          f"{'OK' if abs(pred-rhos[i])<0.15 else 'MISS'}")
print("  (all 13 predictions MISS -- the 4.951 ratio at b=1094273 refutes the decline-to-1 model)")
