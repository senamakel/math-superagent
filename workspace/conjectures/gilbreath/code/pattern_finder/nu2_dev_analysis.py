#!/usr/bin/env python3
"""Fresh look at the Route B supply object nu2(q_n).

Extract D(n)=2*nu2(n)-n from code/out/nu2_dense.txt and probe for
exploitable structure NOT already recorded in memory:
  - exact max |D(n)| and where it is attained
  - scaling: D(n)/sqrt(n), D(n)/(sqrt(n log n)), running max
  - the strongest linear lower bound supported: min over n of nu2(n)/n
    and the threshold exponent min log(nu2)/log(n)
  - sign of D(n): fraction positive, and whether D ever stays <= 0 (the
    dangerous side for the linear bound) for long runs
  - distribution of D(n) (values are small ints; histogram)
All exact integers read from the file; nothing invented.
"""
import math, collections

def load():
    nu2 = {}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            n, v = line.split()
            nu2[int(n)] = int(v)
    return nu2

D_n= {}
def main():
    nu2 = load()
    n_max = max(nu2)
    print(f"terms: n=1..{n_max}")

    D = {n: 2*nu2[n]-n for n in nu2}
    maxabs = max(D.values(), key=abs)
    maxabs_n = [n for n,v in D.items() if abs(v)==abs(maxabs)]
    max_pos = max(D.values()); min_pos = min(D.values())
    print(f"max |D| = {abs(maxabs)} at n={maxabs_n} (only first few shown)")
    print(f"max D = {max_pos}, min D = {min_pos}")

    # scaling
    worst_ratio = max(abs(v)/math.sqrt(n) for n,v in D.items())
    worst_ratio_n = max(D.items(), key=lambda kv: abs(kv[1])/math.sqrt(kv[0]))
    print(f"max |D|/sqrt(n) = {worst_ratio:.3f} at n={worst_ratio_n[0]}")
    D2 = {n:v for n,v in D.items() if n>=2}
    r2 = max(D2.items(), key=lambda kv: abs(kv[1])/math.sqrt(kv[0]*math.log(kv[0])))
    print(f"max |D|/sqrt(n ln n) = {abs(r2[1])/math.sqrt(r2[0]*math.log(r2[0])):.3f} at n={r2[0]}")

    # exponent (n>=5 so log defined and nu2>0)
    nu2pos = {n:v for n,v in nu2.items() if n>=5 and v>0}
    e = min(nu2pos.items(), key=lambda kv: math.log(kv[1])/math.log(kv[0]))
    print(f"min log(nu2)/log(n) = {math.log(e[1])/math.log(e[0]):.4f} at n={e[0]}")
    ml = min(nu2pos.items(), key=lambda kv: kv[1]/kv[0])
    print(f"min nu2(n)/n (n>=5) = {ml[1]/ml[0]:.4f} at n={ml[0]}")

    # n/2 regression is n/2 -> D = 2nu2 - n; check nu2 ~ n/2 via mean
    # sign structure
    vals = sorted(D.values())
    pos = sum(1 for v in D.values() if v>0); zero=sum(1 for v in D.values() if v==0); neg=sum(1 for v in D.values() if v<0)
    print(f"sign: +{pos} 0:{zero} -{neg}  (total {len(D)})")

    # longest run where D<=0 (dangerous for linear bound: needs 2nu2<n, i.e. below mean)
    # actually dangerous for linear bound is when nu2/n < c, i.e. D(n) < -(1-2c)n
    seq_n = sorted(D)
    cur=0; best=0; bestinfo=None
    for n in seq_n:
        if D[n]<=0: cur+=1
        else:
            if cur>best: best=cur; bestinfo=(n-cur, n-1)
            cur=0
    if cur>best: best=cur; bestinfo=(seq_n[-1]-cur+1, seq_n[-1])
    print(f"longest run of D(n)<=0: {best} terms, ending at n={bestinfo}")

    # longest run where 2*nu2 < n (D<0)
    cur=0; best=0; bestinfo=None
    for n in seq_n:
        if D[n]<0: cur+=1
        else:
            if cur>best: best=cur; bestinfo=(n-cur,n-1)
            cur=0
    if cur>best: best=cur; bestinfo=(seq_n[-1]-cur+1, seq_n[-1])
    print(f"longest run of D(n)<0: {best} terms, ending at n={bestinfo}")

    # when is the linear bound c=0.4 threatened: 2nu2 - n >= (2c-1) n = -0.2 n
    # i.e. D(n) >= -0.2n. Report min of D(n)+0.2n
    minmargin = min(D[n]+0.2*n for n in D)
    minmargin_n = min(D.items(), key=lambda kv: kv[1]+0.2*kv[0])
    print(f"min (D(n)+0.2n) [margin for nu2>=0.4n] = {minmargin} at n={minmargin_n[0]}")

    # distribution near 0 (small integer values)
    c = collections.Counter(v for v in D.values() if abs(v)<=30)
    print("top D values near 0 (>=15 count):")
    for val,cnt in sorted(c.items(), key=lambda x:-x[1])[:15]:
        print(f"  D={val}: {cnt}")

if __name__=="__main__":
    main()
