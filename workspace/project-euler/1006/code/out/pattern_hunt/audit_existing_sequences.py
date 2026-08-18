from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).parents[1]
FILES=['psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','dj_raw.txt','dj_mod.txt','counts.txt','vr_runvals.txt','vr_rungaps.txt','ext_recurrence.txt','extrecur_res.txt']

def nums(p):
    out=[]
    for line in (ROOT/p).read_text().splitlines():
        for tok in line.replace(',',' ').split():
            try: out.append(int(tok))
            except ValueError: pass
    return out

def first_bad(seq, pred):
    for i,x in enumerate(seq):
        if not pred(i,x): return i+1,x
    return None

def fibs(n):
    a,b=0,1; z=[]
    while len(z)<n:
        z.append(a); a,b=b,a+b
    return z

def linear(seq, order, coeff_bound=10):
    if len(seq)<=order: return None
    # solve first order equations over rationals; validate all supplied terms
    import sympy as sp
    cs=sp.symbols('c:'+str(order))
    eq=[sp.Eq(seq[i],sum(cs[j]*seq[i-1-j] for j in range(order))) for i in range(order,len(seq))]
    sol=sp.solve(eq,cs, dict=True)
    for s in sol:
        if all(seq[i]==sum(s.get(cs[j], cs[j])*seq[i-1-j] for j in range(order)) for i in range(order,len(seq))): return tuple(s.get(c,c) for c in cs)
    return None

for fn in FILES:
    try: s=nums(fn)
    except FileNotFoundError: continue
    print(f'[{fn}] count={len(s)} prefix={s[:12]}')
    if len(s)>1:
        d=[s[i]-s[i-1] for i in range(1,len(s))]
        print('  diff prefix=',d[:12], 'constant-diff=', first_bad(d, lambda i,x:x==d[0]))
    print('  fib-index equality=', [ (i+1,s[i]) for i in range(min(len(s),30)) if i<len(fibs(30)) and s[i]==fibs(30)[i] ][:8])
    for r in range(1,6):
        c=linear(s,r)
        if c is not None: print('  exact linear recurrence order',r,c)
    if fn=='c1_terms.txt':
        # c1 increments are Sturmian binary; test Fibonacci block constancy of sums
        for q in [2,3,5,8,13,21,34]:
            if q<len(s): print('  block',q,'sums',[sum(s[i:i+q]) for i in range(0,min(len(s),q*5),q)])
