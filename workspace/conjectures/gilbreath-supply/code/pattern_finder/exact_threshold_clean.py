"""Clean exact first_w (mean nu2/n >= 0.40), scan from w=1 (correct).
Integer rational arithmetic, no float scan-start bug.
For n>=512 compute in log-space but scan from w=1.
Cross-check integer vs logspace on small n.
"""
from math import comb, lgamma, exp, log2

def pc(x): return bin(x).count('1')

def P_odd_int(m, w, n):
    lo = max(0, m - (n - w)); hi = min(w, m); num = 0
    for k in range(lo, hi + 1):
        if k & 1:
            num += comb(w, k) * comb(n - w, m - k)
    return num / comb(n, m)

def E_int(n, w):
    return sum(P_odd_int(2**pc(d), w, n) for d in range(2, n)) / n

def P_odd_lg(m, w, n):
    lo = max(0, m - (n - w)); hi = min(w, m); tot = 0.0
    for k in range(lo, hi + 1):
        if k & 1:
            lg = (lgamma(w+1)-lgamma(k+1)-lgamma(w-k+1)
                  + lgamma(n-w+1)-lgamma(m-k+1)-lgamma((n-w)-(m-k)+1)
                  - lgamma(n+1)+lgamma(m+1)+lgamma(n-m+1))
            tot += exp(lg)
    return tot

def E_lg(n, w):
    return sum(P_odd_lg(2**pc(d), w, n) for d in range(2, n)) / n

if __name__ == "__main__":
    # cross-check
    for n in [64,128,256]:
        for w in [3,8,16,32]:
            e1, e2 = E_int(n,w), E_lg(n,w)
            assert abs(e1-e2)<1e-8, (n,w,e1,e2)
    print("integer == logspace cross-check PASS (n=64,128,256)\n")
    for m in range(3, 17):   # n=8..65536
        n = 2**m
        use_int = n <= 4096
        found = None
        for w in range(1, n):
            E = (E_int if use_int else E_lg)(n, w)
            if E >= 0.40:
                found = w; break
        if found is None:
            print(f"n={n:7d}  NONE"); continue
        print(f"n={n:7d}  first_w={found:4d}  w/n={found/n:.6f}  "
              f"log2(w)={log2(found):6.2f}  log2(w)/log2(n)={log2(found)/log2(n):.4f}")
