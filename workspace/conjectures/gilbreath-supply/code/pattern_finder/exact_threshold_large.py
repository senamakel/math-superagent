"""Push the exact first_w (mean nu2/n >= 0.40) to very large n, no sampling.

E[nu2] for uniform weight-w string = sum_{d=2}^{n-1} P_odd(2^pc(d), w, n).
small-w linearization: for w*p small, P_odd ~ w*2^pc(d)/n, giving
E[nu2]/n ~ (w/n^2)*sum 2^pc(d) = w*n^{log2 3 - 2}, first_w ~ n^{2-log2 3} = n^0.415.
But at the parity-nonlinear threshold the exponent is larger. We measure it.
"""
from math import comb, log2

def pc(x): return bin(x).count('1')

# memoized P_odd table for given (w, n, m)
def E_nu2(n, w):
    tot = 0.0
    Cw = [comb(w, k) for k in range(w+1)]
    Cnw = [comb(n-w, k) for k in range(n-w+1)]
    Cn_m = {}
    def cn(m):
        if m not in Cn_m: Cn_m[m] = comb(n, m)
        return Cn_m[m]
    for d in range(2, n):
        m = 2**pc(d)
        lo = max(0, m - (n-w)); hi = min(w, m)
        den = cn(m)
        # sum odd k: C(w,k) C(n-w, m-k)
        s = 0.0
        for k in range(lo, hi+1):
            if k & 1:
                s += Cw[k] * Cnw[m-k]
        tot += s / den
    return tot / n

if __name__ == "__main__":
    n_list = [2**m for m in range(3, 18)]  # 8 .. 131072
    for n in n_list:
        # binary search / linear from 1
        fw = None
        w = 1
        # first_w <= guessed ~ n^0.56, start scan from max(1, int(n**0.4)-2)
        start = max(1, int(n**0.56) - 6)
        for w in range(start, n):
            if E_nu2(n, w) >= 0.40:
                fw = w
                break
        if fw:
            print(f"n={n:7d}  first_w={fw:4d}  w/n={fw/n:.5f}  log2(w)={log2(fw):5.2f}")
        else:
            print(f"n={n:7d}  none")
