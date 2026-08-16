"""Push exact first_w (mean nu2/n >= 0.40) to very large n in log-space, no sampling.
P_odd(m,w,n) computed in log-space (lgamma) to avoid overflow.
"""
from math import lgamma, exp, log2

def pc(x): return bin(x).count('1')

def P_odd(m, w, n):
    """P(odd # of 1s in a fixed m-subset) for uniform weight-w string, log-space."""
    lo = max(0, m - (n - w)); hi = min(w, m)
    tot = 0.0
    for k in range(lo, hi + 1):
        if k & 1:
            lg = (lgamma(w+1)-lgamma(k+1)-lgamma(w-k+1)
                  + lgamma(n-w+1)-lgamma(m-k+1)-lgamma((n-w)-(m-k)+1)
                  - lgamma(n+1)+lgamma(m+1)+lgamma(n-m+1))
            tot += exp(lg)
    return tot

def E_nu2(n, w):
    tot = 0.0
    for d in range(2, n):
        tot += P_odd(2**pc(d), w, n)
    return tot / n

if __name__ == "__main__":
    # cross-check log-space vs integer on small n
    from math import comb
    def P_odd_int(m, w, n):
        lo=max(0,m-(n-w)); hi=min(w,m); num=0
        for k in range(lo,hi+1):
            if k&1: num+=comb(w,k)*comb(n-w,m-k)
        return num/comb(n,m)
    for n in [32,64,128]:
        for w in [3,8,16]:
            for d in [2,5,8]:
                m=2**pc(d)
                a=P_odd(m,w,n); b=P_odd_int(m,w,n)
                assert abs(a-b)<1e-9, (n,w,d,a,b)
    print("log-space == integer cross-check PASS on n=32..128\n")

    n_list = [2**m for m in range(3, 20)]  # 8 .. 524288
    for n in n_list:
        start = max(1, int(n**0.56) - 8)
        fw = None
        for w in range(start, n):
            if E_nu2(n, w) >= 0.40:
                fw = w; break
        if fw:
            print(f"n={n:8d}  first_w={fw:4d}  w/n={fw/n:.6f}  log2(w)={log2(fw):6.2f}")
        else:
            print(f"n={n:8d}  NONE under w<n")
