#!/usr/bin/env python3
"""Generate nu2(2^k) for larger k to test whether the suspected 5th-order
recurrence generalizes (attack the over-fit). Uses numpy for the DP.
"""
import numpy as np
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok=True; r=isqrt(cand)
        for p in ps:
            if p>r: break
            if cand%p==0: ok=False; break
        if ok: ps.append(cand)
        cand+=2
    return ps

def main():
    import sys
    K=int(sys.argv[1]) if len(sys.argv)>1 else 15   # up to 2^K
    N=1<<K
    ps=primes_upto_index(N+3)
    h=np.array([((ps[j+1]-ps[j])//2)%2 for j in range(N+2)], dtype=np.int8)
    # DP over d
    # rows[d] needed at base n-1-d. We keep V(d,base) as numpy arrays.
    # memory: sum over d of (N-d) ~ N^2/2 int8 = 2^(2K-1) bytes: 2^29 ~ 500MB at K=15. too big.
    # Instead process: we only read diagonal cells rows[d][n-1-d] for n varying.
    # Use the recurrence without storing all rows: store rows incrementally, discard
    # but the diagonal read needs rows[d] at specific base for all d up to n.
    # We'll store rows but as int8 arrays; bound by available memory.
    # For K=14, N=16384, sum_(d) (N-d) ~ N^2/2 =1.34e8 bytes=134MB int8. OK.
    # For K=15,N=32768 -> 5.4e8 bytes=537MB. borderline.
    # Use uint8 (XOR same as add mod 2).
    import resource
    rows=[None]*N
    rows[0]=h[:N].astype(np.uint8)
    # build
    for d in range(1,N):
        m=1
        while (m<<1)<=d: m<<=1
        d1=d-m
        r1=rows[d1]
        L=N-1-d
        new=np.zeros(L+1, dtype=np.uint8)
        np.bitwise_xor(r1[:L+1], r1[m:m+L+1], out=new)
        rows[d]=new
    # diagonal: nu2(n)=sum_{d=2}^{n-1} rows[d][n-1-d]
    # print dyadic values
    print("k  n=2^k   nu2(2^k)   nu2/n")
    res={}
    for k in range(1,K+1):
        n=1<<k
        if n<2: continue
        s=0
        for d in range(2,n):
            s+=int(rows[d][n-1-d])
        res[k]=s
        print(f"{k:3d} {n:8d} {s:10d}  {s/n:.4f}")
    # test the 5th-order recurrence on dyadic values
    seq=[res[k] for k in sorted(res)]
    print("\nDyadic seq nu2(2^k), k=1..%d:"%K)
    print(seq)
    if len(seq)>=8:
        # recurrence a(n)=c1 a(n-1)+...+c5 a(n-5) from first 10 terms (k index)
        # predict next using coefficients
        # c = (398171,131238,546101,167275,-1212641)/276121
        c=[398171/276121, 131238/276121, 546101/276121, 167275/276121, -1212641/276121]
        # predict terms beyond index 9 (0-based k=1..)
        nterms_with= len(seq)
        # predict for each position idx (0-based in seq) using prev 5, start idx 5
        print("\nRecurrence prediction vs actual (attack):")
        for i in range(5, nterms_with):
            pred=sum(c[j]*seq[i-1-j] for j in range(5))
            print(f"  seq[{i}] (k={i+1}): actual={seq[i]} pred={pred:.3f} diff={seq[i]-pred:.3f}")

if __name__=="__main__":
    main()
