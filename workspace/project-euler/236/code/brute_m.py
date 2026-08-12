"""Brute-force oracle for PE236: find all valid m values.

Per product i: t_i/b_i = m * s_i/a_i  =>  a_i t_i = m b_i s_i
m must be achievable for all five products; then overall constraint couples them.
"""
from math import gcd

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A); SB = sum(B)

def achievable(ai, bi):
    S = set()
    for s in range(1, ai + 1):
        for t in range(1, bi + 1):
            num = ai * t
            den = bi * s
            g = gcd(num, den)
            S.add((num // g, den // g))
    return S

def overall_feasible(p, q):
    # m = p/q reduced; s_i/t_i = c_i/d_i reduced, with s_i=k_i c_i, t_i=k_i d_i
    c = [0]*5; d = [0]*5; K = [0]*5
    for i in range(5):
        num = A[i]*q
        den = B[i]*p
        g = gcd(num, den)
        ci = num//g; di = den//g
        c[i] = ci; d[i] = di
        K[i] = min(A[i]//ci, B[i]//di)
        if K[i] < 1:
            return False
    # overall: (sum s)/(sum a) = m (sum t)/(sum b)
    # sum k_i c_i / SA = (p/q) * sum k_i d_i / SB
    # q*SB*sum k_i c_i = p*SA*sum k_i d_i
    w = [q*SB*c[i] - p*SA*d[i] for i in range(5)]  # sum k_i w_i = 0
    pos = [(w[i], K[i]) for i in range(5) if w[i] > 0]
    neg = [(-w[i], K[i]) for i in range(5) if w[i] < 0]
    if not pos and not neg:
        return True  # all w=0 -> any k works
    if not pos or not neg:
        return False
    def totals(items):
        cur = {0}
        for wi, Ki in items:
            nxt = set()
            for base in cur:
                for k in range(1, Ki+1):
                    nxt.add(base + k*wi)
            cur = nxt
        return cur
    sp = totals(pos)
    sn = totals(neg)
    return not sp.isdisjoint(sn)

def main():
    sets = [achievable(A[i], B[i]) for i in range(5)]
    for i, S in enumerate(sets):
        print(f"product {i}: achievable size {len(S)}")
    inter = set.intersection(*sets)
    print("per-product achievable m count:", len(inter))
    results = []
    for (num, den) in inter:
        g = gcd(num, den)
        p, q = num//g, den//g
        if p <= q:
            continue  # m>1
        if overall_feasible(p, q):
            results.append((p, q))
    results.sort(key=lambda x: x[0]/x[1])
    print("total valid m:", len(results))
    for p, q in results:
        print(f"{p}/{q}  = {p/q:.6f}")
    if results:
        print("SMALLEST", results[0][0], "/", results[0][1])
        print("LARGEST ", results[-1][0], "/", results[-1][1])

main()
