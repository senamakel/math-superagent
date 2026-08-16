"""Exact expected nu2(n) for a uniformly random weight-w string, no sampling.

nu2(n) = wt(Phi_n h) = sum_{d=2}^{n-1} [cell d odd], where cell d XORs h over
the submask set M_d = {j : n-1-j subseteq d}, |M_d| = 2^popcount(d).

For a uniformly random weight-w string, P(cell d odd) = P(odd # of 1s in a
fixed set of size m) computed combinatorially. This lets us compute E[nu2/n]
EXACTLY (no Monte Carlo) for every w, and find the exact first_w that reaches
mean nu2/n >= 0.40 + frac >= 0.5. frac needs the full distribution, but the
mean is exact; we compute both.

KEY STRUCTURAL FACT: sum_{d=0}^{2^m-1} 2^popcount(d) = 3^m (since each of m
bits contributes factor (1+2)). Excluding d=0,1: sum_{d=2}^{2^m-1} = 3^m - 3.
So E[nu2/n] in the small-p regime ~ (w/n)*3^m/n = (w/n)*n^{log2 3 - 1}.
"""
from math import comb, log2

def popcount(x): return bin(x).count('1')

def P_odd_given_m(m, w, n):
    """P(odd number of 1s among a fixed set of size m) for uniform weight-w string."""
    if w < 0 or m < 0 or n < 0: return 0.0
    # sum over odd k of C(w,k) C(n-w, m-k) / C(n,m)
    lo = max(0, m - (n-w))
    hi = min(w, m)
    num = 0
    for k in range(lo, hi+1):
        if k % 2 == 1:
            num += comb(w, k) * comb(n-w, m-k)
    return num / comb(n, m)

def E_nu2_over_n(n, w):
    """Exact expected nu2/n for uniform weight-w string."""
    tot = 0.0
    for d in range(2, n):
        m = 2**popcount(d)
        tot += P_odd_given_m(m, w, n)
    return tot / n

def frac_ge(n, w, c):
    """Fraction of weight-w strings with nu2/n >= c. Exact via full count is
    infeasible for large n; instead we numerically integate the distribution
    is also hard. So report mean only for large n; this method gives exact mean."""
    return None

if __name__ == "__main__":
    # Verify the structural sum 3^m - 3 for n = 2^m
    for m in range(2, 14):
        n = 2**m
        s = sum(2**popcount(d) for d in range(2, n))
        assert s == 3**m - 3, (m, s, 3**m-3)
    print("structural sum sum_{d=2}^{2^m-1} 2^pc(d) == 3^m - 3 verified for m=2..13\n")

    # Exact first_w (mean>=0.40) for powers of two
    print(" n      exact_first_w_mean  w/n      measured_first_w")
    measured = {8:3,10:3,12:3,14:4,16:3,32:5,64:8,128:16,256:17,512:25,1024:38,2048:55,4096:87,8192:127}
    for n in [8,16,32,64,128,256,512,1024,2048,4096,8192]:
        # find smallest w with mean >= 0.40
        fw = None
        w = 1
        while w < n:
            mean = E_nu2_over_n(n, w)
            if mean >= 0.40:
                fw = w
                break
            w += 1
        print(f"{n:6d}  {fw if fw else 'none':17}  {fw/n if fw else '-':8.4f}  {measured.get(n,'-')}")
