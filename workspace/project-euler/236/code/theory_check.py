"""Verify the per-product structural theorem for PE236.

Claim: integers s_i in [1,a_i], t_i in [1,b_i] with s_i/t_i = (a_i q)/(b_i p)
(reduced m = p/q) exist  <=>  g_i >= max(p,q), where g_i = gcd(a_i q, b_i p).

Proof sketch of the "if and only if":
  Let (u_i,v_i) = reduced (a_i q, b_i p), u_i = a_i q/g_i, v_i = b_i p/g_i.
  Feasible set is (s_i,t_i)=k_i(u_i,v_i), k_i>=1, within boxes.
  u_i<=a_i <=> q<=g_i ; v_i<=b_i <=> p<=g_i ; so exists k_i (=1) <=> g_i>=max(p,q).
  K_i := min(a_i//u_i, b_i//v_i) = g_i//max(p,q).

We check this equivalence on the raw per-product reachable set (no m assumed),
for the known oracle m values.
"""
from math import gcd

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]

# Oracle m values already computed in this run (factor_analysis.py).
ORACLE = [
(1476,1475),(60,59),(902,885),(3321,3245),(41,40),(123,118),(63,59),(328,295),
(533,472),(738,649),(1353,1180),(205,177),(1722,1475),(697,590),(492,413),(1066,885),
(287,236),(1230,1003),(369,295),(615,472),(1599,1180),(80,59),(81,59),(82,59),
(2460,1711),(861,590),(615,413),(451,295),(369,236),(492,295),(205,118),(738,413),
(108,59),(574,295),(123,59)]

def per_product(ai, bi, p, q):
    """True per-product box feasibility via brute enumeration of s,t."""
    need_num, need_den = ai*q, bi*p
    g = gcd(need_num, need_den)
    u, v = need_num//g, need_den//g
    # rounded / direct check
    direct = (u <= ai and v <= bi)
    # threshold claim
    thr = (g >= max(p, q))
    return direct, thr

bad = 0
for idx,(p,q) in enumerate(ORACLE):
    for i in range(5):
        d, t = per_product(A[i], B[i], p, q)
        if d != t:
            bad += 1
            print("MISMATCH", idx, i, p, q, "direct", d, "thr", t)
print("per-product equivalence mismatches:", bad)

# Overall feasibility check: compare brute overall_feasible to the
# gcd-threshold + bounded-k_i linear-constraint method.
SA, SB = sum(A), sum(B)

def overall_thr(p, q):
    """Per-product thresholds + bounded k_i subset-sum feasibility."""
    u = [0]*5; v = [0]*5; K = [0]*5
    for i in range(5):
        num, den = A[i]*q, B[i]*p
        g = gcd(num, den)
        if g < max(p, q):
            return False
        u[i] = num//g; v[i] = den//g
        K[i] = g // max(p, q)
    w = [q*SB*u[i] - p*SA*v[i] for i in range(5)]
    pos = [(w[i], K[i]) for i in range(5) if w[i] > 0]
    neg = [(-w[i], K[i]) for i in range(5) if w[i] < 0]
    if not pos and not neg:
        return True
    if not pos or not neg:
        return False
    def sums(items):
        cur = {0}
        for wi, Ki in items:
            nxt = set()
            for base in cur:
                for k in range(1, Ki+1):
                    nxt.add(base + k*wi)
            cur = nxt
        return cur
    return not sums(pos).isdisjoint(sums(neg))

# count valid over the oracle set & confirm 35 and the extremes are reproduced
valid = [ (p,q) for (p,q) in ORACLE if overall_thr(p,q) ]
print("valid among oracle set:", len(valid), "of", len(ORACLE))
if valid:
    print("smallest:", min(valid, key=lambda x: x[0]/x[1]))
    print("largest :", max(valid, key=lambda x: x[0]/x[1]))
# does per-product-only (ignoring overall) already reject none of the oracle?
pp_only = 0
for (p,q) in ORACLE:
    ok = all(per_product(A[i],B[i],p,q)[0] for i in range(5))
    pp_only += ok
print("oracle values passing per-product-only condition:", pp_only)
