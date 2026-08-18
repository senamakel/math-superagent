"""Second-route verification of audit conclusions using direct parsing and integer checks."""
from pathlib import Path
from math import isqrt

OUT=Path(__file__).resolve().parents[1]/'out'

def table(name):
    ans=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        if len(z)>=2:
            try: ans.append((int(z[0]),int(z[1])))
            except ValueError: pass
    return ans

def floor_alpha(k):
    # alpha=(3-sqrt(5))/2; floor((3k-k sqrt5)/2).
    # ceil(k sqrt5) is obtained exactly by checking integer square bounds.
    q=isqrt(5*k*k)
    ceil_q=q if q*q==5*k*k else q+1
    # Since 3k-k sqrt5 is nonintegral for k>0, floor((3k-k sqrt5)/2)
    # equals floor((3k-ceil(k sqrt5))/2), with parity handled directly.
    return (3*k-ceil_q)//2

def first_bad(rows, f):
    for k,v in rows:
        e=f(k)
        if v!=e:return (k,v,e)
    return None

def main():
    c=table('c1_terms.txt'); l=table('lmin.txt'); counts=table('counts.txt')
    print('counts k+1:', first_bad(counts,lambda k:k+1))
    print('c1 floor law:', first_bad(c,lambda k:1+floor_alpha(k)))
    fib=[1,2]
    while fib[-1]<=max(k for k,_ in l):fib.append(fib[-1]+fib[-2])
    print('Lmin law:', first_bad(l,lambda k:k+next(x for x in fib if x>k)-1))
    p=table('psi_residues.txt'); cm=dict(c)
    print('Psi mod100=c1 first:',next(((k,v,cm[k]) for k,v in p if v%100!=cm[k]%100),None))
    print('Psi mod1000=c1 first:',next(((k,v,cm[k]) for k,v in p if v%1000!=cm[k]%1000),None))
    s=table('s1_exact.txt'); r=table('vR_exact.txt'); rd=dict(r)
    # direct cross relation candidate S1(k)=V(R_k) is checked at k=2 and fails at k=3.
    print('S1=VR first:',next(((k,v,rd[k]) for k,v in s if v!=rd[k]),None))
    d=table('dj_raw.txt')
    print('dj Fibonacci additive first:',next(((k,v,d[k-2][1]+d[k-3][1]) for k,v in d if k>=3 and v!=d[k-2][1]+d[k-3][1]),None))

if __name__=='__main__':main()
