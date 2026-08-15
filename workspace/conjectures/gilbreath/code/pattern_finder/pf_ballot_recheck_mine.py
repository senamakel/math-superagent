#!/usr/bin/env python3
"""Independent re-check of the Route B crux: pointwise switch-majority.

Crux chain (all definitions 1-indexed primes p_1=2,...):
  gap_k = p_{k+1} - p_k
  h_k   = (gap_k//2) % 2  == 1 iff gap_k = 2 mod 4  (switch bit), k>=2
  w(n)  = sum_{k=3}^{n} h_k                  (n>=2), w(2)=0
  e(n)  = 2*w(n) - (n-2)   excess of switches over non-switches
  R(n)  = # maximal equal-residue runs among p_3..p_{n+1}
  identity: e(n) = 2*R(n) - n  <=>  R(n) >= n/2  <=> mean residue-run len <= 2

Goal: verify e(n)>=0 pointwise over a large N with INDEPENDENT code, and
report the exact minimum / first falsifier position if any.
Also confirm the compressed chain nu2 >= (n-2)/4 beats n^0.525.
"""
import sys, math
from lib.gilbreath import primes_up_to

def main():
    SIEVE = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000_000
    P = primes_up_to(SIEVE)
    print("sieve to %d: %d primes" % (SIEVE, len(P)))
    # need primes up to index N+1
    N = len(P) - 2   # safe window n reads p_{n+1}
    # residues u_k = chi_4(p_k) in {+1 (1 mod4), -1 (3 mod4)}
    # switch bit h_k for gap_k = p_{k+1}-p_k: 1 if gap=2 mod4 i.e. (gap//2)%2
    e = 0
    w = 0
    min_e = (10**30, None)
    viol_first = None
    zero_positions = []
    # walk: step +1 if h_k=1 else -1, for k=3..n
    for k in range(3, N+1):
        g = P[k] - P[k-1]
        hk = (g//2) % 2
        step = 1 if hk == 1 else -1
        w += hk
        e += 2*hk - 1
        if e < min_e[0]:
            min_e = (e, k)
        if e < 0 and viol_first is None:
            viol_first = k
        if e == 0:
            zero_positions.append(k)
    print("window N=%d (primes to index %d = %d)" % (N, N+1, P[N]))
    print("final w=%d  final 2w-(N-2)=%d" % (w, 2*w-(N-2)))
    print("e(n)>=0 for n in [2,%d]: %s" % (N, "YES" if viol_first is None else "NO first-viol=%d" % viol_first))
    print("min e = %d at n=%d" % (min_e[0], min_e[1]))
    print("e==0 positions (first 12):", zero_positions[:12], "count", len(zero_positions))
    # suffix minima to show growth
    for T in (100,1000,10000,100000,1000000):
        # recompute suffix min
        e2=0
        suf=(10**30,None)
        for k in range(3,N+1):
            g=P[k]-P[k-1]; hk=(g//2)%2
            e2+=2*hk-1
            if k>=T and e2<suf[0]:
                suf=(e2,k)
        print("  min e over [%d,N] = %d at n=%d" % (T,suf[0],suf[1]))
    # run-form check over a prefix (identity e=2R-n)
    # verify exact on first 200000 terms
    M = min(N, 200000)
    # runs among p_3..p_{n+1}
    # incremental R: R(n) for sequence p_3..p_{n+1} (length n-1 elements)
    from collections import deque
    # build us[0]=u_3 ...
    R = 1
    prev = P[3-1] % 4
    okR = True
    ecur = 0
    for k in range(3, M+1):
        # extend sequence to p_{k+1}
        # p_{k+1} index = k+1 (1-based)
        v = P[k+1-1] % 4
        if v != prev:
            R += 1
            prev = v
        ecur += 2*((P[k]-P[k-1])//2 % 2) - 1
        if ecur != 2*R - (k):
            okR = False
            print("RUN-ID FAIL at k=%d ecur=%d 2R-k=%d" % (k, ecur, 2*R-k))
            break
    print("identity e(n)=2R(n)-n over k in [2,%d]: %s" % (M, "OK" if okR else "FAIL"))
    # composed supply bound
    print("\ncomposed nu2 >= (n-2)/4 check (uses measured nu2>=w/2 and w>=(n-2)/2 from e>=0):")
    # just show crossover for n^0.525 and n^0.55
    for bet in (0.525, 0.55, 0.6):
        cross = None
        for n in range(23, 1000):
            if (n-2)/4 > n**bet:
                cross = n; break
        print("  (n-2)/4 > n^%.3f first at n=%s" % (bet, cross))

main()
