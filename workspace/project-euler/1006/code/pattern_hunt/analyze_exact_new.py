"""Exact sequence recurrence hunt; output is finite computational evidence only."""
from pathlib import Path
from fractions import Fraction
import sympy as sp

ROOT=Path(__file__).parents[1]/'out'

def rows(path):
    out=[]
    for line in (ROOT/path).read_text().splitlines():
        t=line.strip()
        if not t or t.startswith('#'): continue
        try:
            z=t.split()
            # Most files are one-column; for tabular reports use the final
            # numeric column, not the row index or binary word.
            out.append(int(z[-1]) if len(z)>1 else int(z[0]))
        except ValueError: pass
    return out

def bm_mod(a,m):
    # Sympy BM over a prime field only; report unusable composite inversions.
    C=[1]; B=[1]; L=0; b=1; shift=1
    for n in range(len(a)):
        d=a[n]%m
        for i in range(1,L+1): d=(d+C[i]*a[n-i])%m
        if d==0: shift+=1; continue
        g=sp.gcd(d,m)
        if g!=1: return ('nonunit',n,int(d),int(g))
        coef=d*pow(int(b),-1,m)%m
        T=C[:]
        if len(C)<len(B)+shift: C += [0]*(len(B)+shift-len(C))
        for j,x in enumerate(B): C[j+shift]=(C[j+shift]-coef*x)%m
        if 2*L<=n:
            L=n+1-L; B=T; b=d; shift=1
        else: shift+=1
    return ('ok',L,C)

def exact_recurrences(a,maxord=12):
    ans=[]
    for r in range(1,min(maxord,len(a)-1)+1):
        # solve first overdetermined equations exactly
        cs=sp.symbols('c:'+str(r))
        eq=[sp.Eq(a[n],sum(cs[i]*a[n-1-i] for i in range(r))) for n in range(r,len(a))]
        sol=sp.solve(eq,cs, dict=True)
        if sol: ans.append((r,sol))
    return ans

def report(name,a):
    print(f'{name}: n={len(a)} first={a[:8]}')
    print(' exact homogeneous recurrences <=12:',exact_recurrences(a))
    print(' BM mod M:',bm_mod(a,101001001))
    for mod in (2,5,10,100,1000): print(' BM mod',mod,':',bm_mod(a,mod))

for fn in ['psi_exact.txt','psi_residues.txt','c1_terms.txt','dj_raw.txt','ext_recurrence.txt','extrecur_res.txt','lmin.txt','counts.txt']:
    p=ROOT/fn
    if p.exists(): report(fn,rows(Path(fn)))
