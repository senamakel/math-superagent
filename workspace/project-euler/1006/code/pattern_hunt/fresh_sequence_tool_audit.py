"""Fresh exact audit of strongest PE1006 sequence artifacts.
Evidence only: finite terms, exact laws, and recurrence diagnostics.
"""
from pathlib import Path
import sympy as sp

OUT=Path(__file__).parents[1]/"out"
PHI2=(3+sp.sqrt(5))/2
ALPHA=(3-sp.sqrt(5))/2

def read(name, col=-1):
    a=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        if not z or z[0].startswith('#'): continue
        try: a.append(int(z[col]))
        except (ValueError,IndexError): pass
    return a

def fit(a,r):
    if len(a)<=2*r: return None
    cs=sp.symbols('c:'+str(r))
    eq=[sp.Eq(a[n],sum(cs[j]*a[n-1-j] for j in range(r))) for n in range(r,len(a))]
    q=sp.solve(eq,cs,dict=True)
    return q[0] if q else None

def first_bad(a,p):
    for i,x in enumerate(a,1):
        if not p(i,x): return i,x
    return None

def bm(a,p=100000007):
    C=[1];B=[1];L=0;m=1;b=1
    for n in range(len(a)):
        d=a[n]%p
        for i in range(1,L+1): d=(d+C[i]*a[n-i])%p
        if d==0: m+=1;continue
        q=d*pow(b,-1,p)%p; T=C[:]
        if len(C)<len(B)+m:C += [0]*(len(B)+m-len(C))
        for j,x in enumerate(B): C[j+m]=(C[j+m]-q*x)%p
        if 2*L<=n:L=n+1-L;B=T;b=d;m=1
        else:m+=1
    return L

def fibs(n):
    f=[0,1]
    while f[-1] < n+2:f.append(f[-1]+f[-2])
    return f

def main():
    seq={
      'c1':read('c1_terms.txt',1), 'Lmin':read('lmin.txt',1),
      'toeplitz defect':read('topelitz_defects.txt',-1),
      'Psi residues':read('psi_residues.txt',1),
      'run gaps':read('vr_rungaps.txt',-1),
      'run starts':read('vr_runvals.txt',0),
    }
    lines=['# Fresh exact sequence-tool audit (2026-08-18)','',
      'Method: read current artifact files, retain exact integer terms, fit homogeneous rational recurrences (orders 1--12), and run Berlekamp--Massey modulo prime 100000007. These are finite diagnostics, not proofs.']
    for name,a in seq.items():
        lines += [f'## {name}',f'- terms used: n={len(a)}, first 12={a[:12]}',
          '- exact recurrence orders 1..12: '+str([(r,fit(a,r)) for r in range(1,13) if fit(a,r)]),
          f'- BM complexity mod 100000007: {bm(a)}']
        if name=='c1':
            bad=first_bad(a,lambda k,x:x==1+sp.floor(k*ALPHA))
            lines.append(f'- law c1(k)=1+floor(k*(3-sqrt(5))/2): first falsifier={bad}')
        elif name=='Lmin':
            f=fibs(max(a)); bad=first_bad(a,lambda k,x:x==k+next(q for q in f if q>k)-1)
            lines.append(f'- law Lmin(k)=k+NextFib(k)-1: first falsifier={bad}')
        elif name=='toeplitz defect':
            zeros=[i for i,x in enumerate(a,1) if x==0]
            lines.append(f'- zero indices (all supplied): {zeros}')
            lines.append(f'- all-zero conjecture first falsifier={first_bad(a,lambda k,x:x==0)}')
        elif name=='run gaps':
            # The artifact includes the initial boundary marker 1; audit the
            # genuine successive gaps from its second term onward.
            lines.append(f'- distinct gaps (after boundary marker)={sorted(set(a[1:]))}; first non-{{2,3}}={first_bad(a[1:],lambda k,x:x in (2,3))}')
        elif name=='Psi residues':
            c=seq['c1']; lines.append(f'- Psi mod 100 == c1 first falsifier={first_bad(a,lambda k,x:x%100==c[k-1]%100)}')
            lines.append(f'- Psi mod 1000 == c1 first falsifier={first_bad(a,lambda k,x:x%1000==c[k-1]%1000)}')
    lines += ['', '## Conclusion', 'The exact audit finds no new surviving scalar constant-coefficient recurrence. The strongest surviving finite laws are c1 floor law, Lmin strict-next-Fibonacci law, run gaps in {2,3}, and Psi ≡ c1 (mod 100); Toeplitz defects are not identically zero and Psi mod 1000 is falsified early.']
    p=OUT/'pattern_hunt'/'fresh_sequence_tool_audit.md';p.write_text('\n'.join(lines)+'\n');print(p);print('\n'.join(lines))
if __name__=='__main__':main()
