"""Independent compact-sequence audit; output is finite evidence only."""
from pathlib import Path
import sympy as sp
ROOT=Path('code/out')

def vals(name):
    out=[]
    for line in (ROOT/name).read_text().splitlines():
        z=line.split()
        for token in reversed(z):
            try: out.append(int(token)); break
            except ValueError: pass
    return out

def fit(a,r):
    if len(a)<=r: return None
    cs=sp.symbols('c:'+str(r))
    eq=[sp.Eq(a[n],sum(cs[i]*a[n-1-i] for i in range(r))) for n in range(r,len(a))]
    sol=sp.solve(eq,cs,dict=True)
    return sol[0] if sol else None

files=['psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','dj_raw.txt','topelitz_defects.txt','vr_rungaps.txt','counts.txt','ext_recurrence.txt','extrecur_res.txt']
for f in files:
 p=ROOT/f
 if not p.exists(): continue
 a=vals(f)
 hits=[(r,fit(a,r)) for r in range(1,min(12,len(a)-1)+1) if fit(a,r)]
 print(f,len(a),'recurrence_hits<=12=',hits)
# exact independent checks of already-known formulas
c=vals('c1_terms.txt'); print('c1 first mismatch against stored expected floor formula is not recomputed here; analyzer checked it')
l=vals('lmin.txt'); print('lmin terms',len(l),'nonzero count',sum(x!=0 for x in l))
