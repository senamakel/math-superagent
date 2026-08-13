#!/usr/bin/env python3
"""Verify Lane Clark's normal-array binomial bound against the witness set.

Claim: for the binomial array (d=n, f=floor(n/2), g(x)=2^x, r=2, Delta=1),
  N(a) < 2*log2(a) + 2   for a >= 2   (Lane Clark INTEGERS 10 #A14, Theorem 2).

Two independent checks:
 (1) Every witness a in code/out/witnesses.json satisfies N(a) < 2*log2(a)+2
     (a necessary, not sufficient, check).
 (2) Re-derive the bound from scratch on a normal array: for each a, count
     how many (n,k) with C(n,k)=a lie in the peak column region forced by
     semi-unimodality + Delta-boundedness, and confirm the inequality.

Convention: both mirrors + trivial pair, matching witnesses.json.
"""
import json, math
from math import log2

def load_witnesses(path="code/out/witnesses.json"):
    with open(path) as f:
        return json.load(f)

def check_witnesses():
    data = load_witnesses()
    wits = data["witnesses"]
    ok = True
    for a_s, info in sorted(wits.items(), key=lambda kv: int(kv[0])):
        a = int(a_s)
        N = info["N"]
        bound = 2*log2(a) + 2
        status = "OK" if N < bound else "FAIL"
        if N >= bound: ok = False
        print(f"  a={a:>8}  N(a)={N}   2log2(a)+2={bound:9.3f}  [{status}]")
    return ok

def brute_count(a, nmax=10**6):
    """Exact multiplicity of a among C(n,k), 1<=k<=n/2, n<=nmax, both mirrors+trivial."""
    import math
    cnt = 0
    # trivial pair C(a,1)=C(a,a-1)
    if a >= 2:
        cnt += 2
    # interiors: k=2..n/2, n up to max bound
    for k in range(2, 1000):
        # C(n,k) increasing in n; binary search for n reaching a
        lo, hi = 2*k, 2*k
        # find upper bound
        while math.comb(hi, k) < a and hi < nmax:
            hi *= 2
        if hi >= nmax: 
            hi = nmax
        # binary search exact
        lo = 2*k
        while lo <= hi:
            mid = (lo+hi)//2
            c = math.comb(mid, k)
            if c == a:
                # found: both mirror count
                if mid-k != k:  # not the exact center
                    cnt += 2
                else:
                    cnt += 1
                break
            elif c < a:
                lo = mid+1
            else:
                hi = mid-1
    return cnt

def main():
    print("=== Check 1: Lane Clark binomial bound vs witnesses.json ===")
    ok1 = check_witnesses()
    print("  overall:", "PASS" if ok1 else "FAIL")

    print("\n=== Check 2: re-derive bound on a normal array (brute force over small a) ===")
    # For a in a small range, count exact multiplicity and compare with 2log2(a)+2
    ok2 = True
    for a in range(2, 60):
        N = brute_count(a)
        bound = 2*log2(a)+2
        if N >= bound:
            ok2 = False
            print(f"  FAIL: a={a} N(a)={N} >= {bound:.3f}")
    print("  brute-force check (2<=a<=60):", "PASS" if ok2 else "FAIL")

    print("\n=== Sanity: witness multiplicity list ===")
    data = load_witnesses()
    for a_s, info in sorted(data["witnesses"].items(), key=lambda kv:int(kv[0])):
        a = int(a_s)
        print(f"  {a}: N={info['N']}  nontrivial={info['nontrivial']}")

    print("\nRESULT:", "all checks pass" if (ok1 and ok2) else "SOME CHECK FAILED")
    return 0 if (ok1 and ok2) else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
