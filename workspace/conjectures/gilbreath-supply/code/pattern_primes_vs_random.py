#!/usr/bin/env python3
"""Direct detrended comparison primes vs random at same N, to decide whether
short-lag autocorrelation is primes-specific or a fold artifact. Random h has
no secular drift, so its raw rho is already the fair comparison vs detrended
primes.
"""
import sys, random
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def autocorr_detrended(seq, W):
    L=len(seq)
    detr=[]
    for i in range(L):
        lo=max(0,i-W//2); hi=min(L,i+W//2+1)
        detr.append(seq[i]-sum(seq[lo:hi])/(hi-lo))
    d=[x-sum(detr)/len(detr) for x in detr]
    v=sum(x*x for x in d)/len(d)
    out=[]
    for k in [1,2,3,5,8,13,21,34,55,80]:
        if k>=len(d): break
        out.append(sum(d[i]*d[i+k] for i in range(len(d)-k))/v/len(d))
    return out

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    ps = primes_upto_index(N + 2)
    h = [((ps[j+1]-ps[j])//2) % 2 for j in range(N+1)]
    nu=[0]*(N+1)
    for n in range(2,N+1):
        _,ones=s_sos(n,h[:n]); nu[n]=ones
    rp=[nu[n]/n for n in range(2,N+1)]
    # random h same N
    random.seed(7)
    hr=[random.randint(0,1) for _ in range(N+1)]
    nur=[0]*(N+1)
    for n in range(2,N+1):
        _,ones=s_sos(n,hr[:n]); nur[n]=ones
    rr=[nur[n]/n for n in range(2,N+1)]
    W=500
    ap=autocorr_detrended(rp,W)
    ar=autocorr_detrended(rr,W)
    lags=[1,2,3,5,8,13,21,34,55,80]
    print(f"N={N}  detrended(W={W}) autocorrelation: primes vs random")
    print("  lag  primes  random")
    for i,k in enumerate(lags):
        p_=ap[i] if i<len(ap) else float('nan')
        r_=ar[i] if i<len(ar) else float('nan')
        print(f"  {k:3d}  {p_:+.4f}  {r_:+.4f}")

if __name__ == "__main__":
    main()
