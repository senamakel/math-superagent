#!/usr/bin/env python3
"""Verify E2(n) = 2*nu2(n)-(n-2) equals -S(n) (the negative endpoint char sum),
and study the increments dS(n) = S(n) - S(n-1).

If the increments look roughly independent balanced, S(n) = sum of +/-1 behaves
like a random walk with |S| ~ sqrt(n), i.e. E2 sublinear -> nu2/n -> 1/2.
This is a reframe: SUPPLY pointwise is equivalent to S(n)=o(n).
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.supply_fold import s_sos
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    prevS = None
    increments = {}
    maxerr = 0
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        e2 = 2 * v - (n - 2)
        S, ones = s_sos(n, h[:n])
        # check: ones should equal v (fold_nu2 count of T=1)
        err = ones - v
        if abs(err) > maxerr: maxerr = abs(err)
        if S != -e2:
            print(f"MISMATCH n={n}: S={S} e2={e2}")
            return
        if prevS is not None:
            increments[n] = S - prevS
        prevS = S
    print(f"N={N}: (S == -E2) held for every n (max ones-v diff {maxerr})")
    inc = [increments[n] for n in range(3, N + 1)]
    # increments are +/-2? since S changes by (-1)^{T(n,n-1)} etc... check
    vals = set(inc)
    print("increment set:", sorted(vals))
    # correlation of successive increments
    xs = inc
    mean = sum(xs)/len(xs)
    c1 = sum((xs[i]-mean)*(xs[i+1]-mean) for i in range(len(xs)-1))/len(xs)
    v0 = sum((x-mean)**2 for x in xs)/len(xs)
    print(f"increments: N={len(xs)} mean={mean:.4f} var={v0:.4f} lag-1 autocorr={c1/v0:.4f}")
    # running |S| max and end value
    Sa = []
    acc = 0
    mS = 0
    for n in range(2, N+1):
        acc += increments.get(n, 0) if n > 2 else 0
        Sa.append(acc)
    print("max|S| =", max(abs(x) for x in Sa))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 2000)
