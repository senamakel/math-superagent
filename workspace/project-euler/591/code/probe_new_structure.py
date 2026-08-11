"""Fresh probe of structural laws in PE591 data at n=1e13.
Data: results_full_bothsides.txt (d, b, a, |a|).
Tests:
  1. m^2-scaling law (36 pairs): |a_{m^2 d0}| == |a_{d0}| iff m | b_{d0};
     and when equal, b_{m^2 d0} == b_{d0}/m.
  2. Inverse direction: does |a_{m^2 d0}| == |a_{d0}| ever hold when m does NOT
     divide b_{d0}?  (Would falsify the iff.)
  3. |a_d| vs floor/nearest of |b_d|*sqrt(d): find exact c_d = |a_d| - round(|b_d|*sqrt(d)).
  4. Sign pattern of b_d: list d with b>0 vs b<0 and look for structure.
"""
import math

rows = {}
with open("results_full_bothsides.txt") as f:
    for line in f:
        parts = line.split()
        if len(parts) == 4 and parts[0].isdigit():
            d, b, a, aa = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
            rows[d] = (b, a, aa)

nonsq = [d for d in range(2,100) if int(math.isqrt(d))**2 != d]

# ---- Law 1/2: m^2 scaling ----
pairs = []
for d0 in nonsq:
    for m in range(2, 20):
        d1 = m*m*d0
        if d1 < 100 and d1 in rows:
            pairs.append((d0, m, d1))
print("total m^2 pairs within [2,99]:", len(pairs))

viol = 0
eq_when_div = 0
for (d0, m, d1) in pairs:
    b0 = abs(rows[d0][0]); a0 = rows[d0][2]
    b1 = abs(rows[d1][0]); a1 = rows[d1][2]
    divides = (b0 % m == 0)
    equal = (a0 == a1)
    if divides != equal:
        viol += 1
        print("  VIOLATION of iff:", d0, m, d1, "m|b?", divides, "|a| equal?", equal)
    if divides:
        if b1 == b0 // m:
            eq_when_div += 1
        else:
            print("  b-relation fail:", d0, m, d1, b0, b1, b0//m)
print("iff violations:", viol, "| b-divide pairs with b_{d1}=b_{d0}/m:", eq_when_div)

# ---- Law 3: c_d = |a_d| - round(|b_d| sqrt(d)) ----
from collections import Counter
cvals = Counter()
for d in nonsq:
    b, a, aa = rows[d]
    r = round(abs(b)*math.sqrt(d))
    cvals[aa - r] += 1
print("c_d = |a_d| - round(|b| sqrt d) histogram:", dict(sorted(cvals.items())))

# ---- Law 4: sign pattern ----
pos = [d for d in nonsq if rows[d][0] > 0]
neg = [d for d in nonsq if rows[d][0] < 0]
print("num b>0:", len(pos), " num b<0:", len(neg))
print("b>0:", pos)
print("b<0:", neg)
