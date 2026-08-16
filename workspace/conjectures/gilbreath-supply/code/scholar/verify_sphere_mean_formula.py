"""Independent verification of the exact-mean Krawtchouk/parity formula.

Load-bearing formula behind the pass-3 threshold result (claim
threshold-mean-exact-parity-formula / sphere-mean-krawtchouk-exact):

  P_d(w) = (C(n,w) - K_w(2^popcount(d); n)) / (2 C(n,w))
  E_{S_w}[nu2(h)] = sum_{d=2}^{n-1} P_d(w)

where nu2(h) = wt(Phi_n h) counts cells d in [2,n-1] whose submask-XOR parity
is 1, and K_w(m;n) = sum_{j=0}^{min(w,m)} (-1)^j C(m,j) C(n-m, w-j).

We verify against a BRUTE-FORCE direct evaluation: enumerate all weight-w
strings, build the fold cells by subscribing (Lucas: cell d reads the
2^popcount(d) submasks of d), count ones, average. n=3..12, all w.

This is the oracle check the formula's per-n values stand on (method policy
rule 9: brute force on small instances is the oracle).
"""
from math import comb


def popcount(x):
    return bin(x).count("1")


def submask_xor_parity(h, n, d):
    """T(n,d) = XOR of h[n-1-d+o] for o subset of d (floored fold d in [2,n-1])."""
    s = 0
    o = d
    while True:
        s ^= h[n - 1 - d + o]
        if o == 0:
            break
        o = (o - 1) & d
    return s


def formula_mean(n, w):
    total = 0.0
    for d in range(2, n):
        m = 1 << popcount(d)
        # K_w(m;n)
        K = sum(((-1) ** j) * comb(m, j) * comb(n - m, w - j)
                for j in range(0, min(w, m) + 1))
        P_d = (comb(n, w) - K) / (2 * comb(n, w))
        total += P_d
    return total


def brute_mean(n, w):
    total = 0
    count = 0
    # enumerate all weight-w strings of length n
    for h_int in range(1 << n):
        if bin(h_int).count("1") != w:
            continue
        h = [(h_int >> i) & 1 for i in range(n)]
        nu2 = sum(submask_xor_parity(h, n, d) for d in range(2, n))
        total += nu2
        count += 1
    return total / count


fails = 0
for n in range(3, 13):
    for w in range(0, n + 1):
        fm = formula_mean(n, w)
        bm = brute_mean(n, w)
        if abs(fm - bm) > 1e-12:
            fails += 1
            print(f"MISMATCH n={n} w={w} formula={fm} brute={bm}")
print(f"checked n=3..12 all w: fails={fails}")
if fails == 0:
    print("formula == brute force exactly on all small (n,w) -> formula verified")
