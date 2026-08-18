from pathlib import Path
import re
import sympy as sp
from sympy.concrete.guess import guess_generating_function_rational, guess

ROOT=Path('/workspace/code/out')
files=['psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','dj_raw.txt','dj_mod.txt','r_runs_wythoff.txt','vr_runvals.txt','vr_rungaps.txt','counts.txt','s1_res.txt','vR_res.txt']

def nums(p):
    return [int(x) for x in re.findall(r'-?\d+', (ROOT/p).read_text())]
def linrec(a,maxord=20):
    for d in range(1,min(maxord,len(a)//2)+1):
        # solve recurrence a[n]=sum c_i a[n-i]
        cs=sp.symbols('c:'+str(d))
        eq=[sp.Eq(a[n],sum(cs[i]*a[n-1-i] for i in range(d))) for n in range(d,len(a))]
        sol=sp.solve(eq,cs, dict=True)
        if sol:
            s=sol[0]
            if all(a[n]==sum(s[cs[i]]*a[n-1-i] for i in range(d)) for n in range(d,len(a))): return d,[s[x] for x in cs]
    return None
for f in files:
    a=nums(f)
    if not a: continue
    print(f,'n=',len(a),'head=',a[:12])
    print('diff head=',[a[i+1]-a[i] for i in range(min(10,len(a)-1))])
    print('rec=',linrec(a))
    for mod in [2,3,5,10,100]:
        b=[x%mod for x in a]
        # periodicity
        found=None
        for p in range(1,min(500,len(b)//2)+1):
            if all(b[i]==b[i-p] for i in range(p,len(b))): found=p;break
        if found: print('period mod',mod,found)
