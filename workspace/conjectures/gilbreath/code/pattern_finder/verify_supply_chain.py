#!/usr/bin/env python3
"""Verify the full Route-B supply chain independently.

Chain (all numerical, conjectures not proofs):
  leg(a): nu2(n) >= w(n)/2            (transfer; nu2 from nu2_dense.txt, w from fresh sieve)
  leg(b): w(n) >= (n-2)/2  i.e. e(n)>=0  (switch-walk positivity, the gap-mod-4 ballot)
  composed: nu2(n) >= (n-2)/4  which clears n^0.525 for n>=23

nu2_dense.txt: "n nu2" lines for n=1..30000.  window for w(n) is [2,n-1]:
w(n) = # {k : 2<=k<=n-1, p_{k+1} != p_k mod 4}.  This needs p_{n}, i.e. sieve to
enough primes.
"""
import sys, time, math

def primes_upto(limit):
    if limit < 3: return []
    sieve = bytearray(b'\x01')*((limit>>1)+1); sieve[0]=0
    r=int(limit**0.5)
    for i in range(1,(r>>1)+1):
        if sieve[i]:
            step=2*i+1; start=(step*step)>>1
            sieve[start::step]=b'\x00'*(((len(sieve)-1-start)//step)+1)
    out=[2]; out.extend(2*i+1 for i in range(1,len(sieve)) if sieve[i]); return out

def main():
    NMAX = 30000
    # read nu2
    nu2 = {}
    with open('code/out/nu2_dense.txt') as f:
        for line in f:
            line=line.split()
            if len(line)==2:
                nu2[int(line[0])]=int(line[1])
    print(f"loaded nu2 for {len(nu2)} n, n range {min(nu2)}..{max(nu2)}")
    # primes up to p_{NMAX}
    plim = int(NMAX*(math.log(NMAX)+math.log(math.log(NMAX))+1))
    t0=time.time()
    pr = primes_upto(plim)
    print(f"sieve to {plim}: {len(pr)} primes ({time.time()-t0:.1f}s), have >= NMAX: {len(pr)>=NMAX}")
    res = [0]+[p&3 for p in pr]   # res[k]=p_k mod4
    # w(n) prefix
    w = [0]*(NMAX+1)
    wswitch = 0
    for n in range(2, NMAX+1):
        # at n: window [2,n-1]; k=n-1 is last gap; p_{n-1},p_n
        if res[n-1] != res[n]:
            wswitch += 1
        w[n] = wswitch
    # leg(a): nu2 >= w/2
    viol_a=0; first_a=None
    mn_ratio=1e9; mn_ratio_at=None
    for n in range(17, NMAX+1):
        if nu2[n] < w[n]/2 - 1e-12:
            viol_a+=1
            if first_a is None: first_a=n
        r = nu2[n]/(w[n] if w[n]>0 else 1)
        if r<mn_ratio: mn_ratio=r; mn_ratio_at=n
    print(f"leg(a) nu2>=w/2 over n in [17,{NMAX}]: viol={viol_a} first={first_a} min nu2/w={mn_ratio:.4f} at n={mn_ratio_at}")
    # leg(b): w >= (n-2)/2 i.e. 2w>=n-2
    viol_b=0; first_b=None
    min_excess=1e9
    for n in range(2,NMAX+1):
        exc = 2*w[n]-(n-2)
        if exc<0:
            viol_b+=1
            if first_b is None: first_b=n
        if exc<min_excess: min_excess=exc
    print(f"leg(b) w>=(n-2)/2 over [2,{NMAX}]: viol={viol_b} first={first_b} min excess 2w-(n-2)={min_excess}")
    # composed nu2 >= (n-2)/4
    viol_c=0; first_c=None; min_margin=1e9; min_margin_n=None
    for n in range(23,NMAX+1):
        budget = n**0.525
        if nu2[n] < (n-2)/4 - 1e-12:
            viol_c+=1
            if first_c is None: first_c=n
        if nu2[n] < budget:
            pass
        m = nu2[n]/budget if budget>0 else 1e9
        if m<min_margin: min_margin=m; min_margin_n=n
    print(f"composed nu2>=(n-2)/4 over [23,{NMAX}]: viol={viol_c} first={first_c}")
    print(f"min nu2/n^0.525 over [23,{NMAX}] = {min_margin:.3f} at n={min_margin_n}")

if __name__=="__main__":
    main()
