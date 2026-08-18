"""Fresh exact sequence-tool audit of supplied PE1006 artifacts.
Outputs finite evidence only; no full-size Psi computation.
"""
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).parents[1] / "out"
M = 101001001

def vals(name, column=-1):
    out=[]
    for line in (ROOT/name).read_text().splitlines():
        z=line.split()
        if not z or z[0].startswith('#'): continue
        try: out.append(int(z[column]))
        except (ValueError, IndexError): pass
    return out

def recurrence(seq, r):
    if len(seq) <= 2*r: return None
    c=sp.symbols('c:'+str(r))
    eq=[sp.Eq(seq[n],sum(c[j]*seq[n-1-j] for j in range(r)))
        for n in range(r,len(seq))]
    sols=sp.solve(eq,c,dict=True)
    return sols[0] if sols else None

def bm_prime(seq, p):
    # Diagnostic BM over prime p only; M is composite, so use prime 100000007.
    C=[1]; B=[1]; L=0; m=1; b=1
    for n in range(len(seq)):
        d=seq[n]%p
        for i in range(1,L+1): d=(d+C[i]*seq[n-i])%p
        if not d: m+=1; continue
        inv=pow(b,-1,p); T=C[:]
        if len(C)<len(B)+m: C += [0]*(len(B)+m-len(C))
        q=d*inv%p
        for j,x in enumerate(B): C[j+m]=(C[j+m]-q*x)%p
        if 2*L<=n: L=n+1-L; B=T; b=d; m=1
        else: m+=1
    return L

def first_bad(seq, pred):
    for i,x in enumerate(seq,1):
        if not pred(i,x): return (i,x)
    return None

def main():
    data={
      'psi_exact': vals('psi_exact.txt',0),
      'psi_res': vals('psi_residues.txt',1),
      'c1': vals('c1_terms.txt',1),
      'lmin': vals('lmin.txt',1),
      'dj': vals('dj_raw.txt',1),
      'toeplitz': vals('topelitz_defects.txt',-1),
    }
    for name,s in data.items():
        print(name, 'n=',len(s), 'prefix=',s[:10])
        print(' exact_rec<=12=', next(((r,recurrence(s,r)) for r in range(1,13) if recurrence(s,r)), None))
        print(' BM mod 100000007=',bm_prime(s,100000007))
        if name=='c1':
            a=(3-sp.sqrt(5))/2
            print(' c1 floor law first_bad=',first_bad(s,lambda k,x:x==1+sp.floor(k*a)))
        if name=='lmin':
            fib=[0,1]
            while fib[-1] < max(s)+2: fib.append(fib[-1]+fib[-2])
            print(' lmin formula first_bad=',first_bad(s,lambda k,x:x+k==k+next(f for f in fib if f>k)-1+k))
        if name=='dj':
            print(' dj adjacent Fibonacci first_bad=',first_bad(s,lambda k,x:k<3 or x==s[k-2]+s[k-3]))
        if name=='toeplitz':
            print(' zero_indices=',[k for k,x in enumerate(s,1) if x==0])
            print(' zero_everywhere first_bad=',first_bad(s,lambda k,x:x==0))
    psi=data['psi_res']; c1=data['c1']
    print('psi mod100=c1 first_bad=',first_bad(psi,lambda k,x:x%100==c1[k-1]%100))
    print('psi mod1000=c1 first_bad=',first_bad(psi,lambda k,x:x%1000==c1[k-1]%1000))

if __name__=='__main__': main()
