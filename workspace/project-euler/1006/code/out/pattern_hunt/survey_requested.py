from pathlib import Path
from fractions import Fraction
import math

D=Path('code/out')
def rows(name):
    out=[]
    for line in (D/name).read_text().splitlines():
        p=line.split()
        if len(p)>=2:
            try: out.append((int(p[0]),int(p[1])))
            except: pass
    return out

def first_bad(pred, xs):
    return next(((x,y) for x,y in xs if not pred(x,y)),None)

def linrec(xs, order, start=0):
    # exact solve on first window, test remainder; coefficients rational
    import sympy as s
    ys=[y for _,y in xs]
    cs=s.symbols('c:'+str(order))
    eq=[s.Eq(ys[i],sum(cs[j]*ys[i-1-j] for j in range(order))) for i in range(order,len(ys))]
    sol=s.solve(eq[:max(order,1)],cs, dict=True)
    if not sol:return None
    c=[sol[0][z] for z in cs]
    bad=next((i for i in range(order,len(ys)) if ys[i]!=sum(c[j]*ys[i-1-j] for j in range(order))),None)
    return c,bad

for name in ['psi_exact.txt','psi_residues.txt','c1_terms.txt','ext_recurrence.txt','dj_raw.txt','counts.txt']:
    xs=rows(name); print(name,'rows',len(xs),'first',xs[:5],'last',xs[-3:])
    if name=='c1_terms.txt':
        # exact floor(k/phi^2) = floor(k*(3-sqrt5)/2), compare via integer sqrt
        bad=[]
        for k,v in xs:
            # floor(k*(3-sqrt5)/2), exact comparison using Decimal-free square test
            # use high precision only for survey, report no claim beyond tested range
            import decimal
            decimal.getcontext().prec=50
            q=(decimal.Decimal(3)-decimal.Decimal(5).sqrt())/2
            if v != 1+int(decimal.Decimal(k)*q): bad.append((k,v))
        print(' c1_formula_bad',bad[:1])
    if name=='counts.txt': print(' count_bad',[(k,v) for k,v in xs if v!=k+1][:3])
    for r in range(1,min(8,len(xs)//2)):
        z=linrec(xs,r)
        if z and z[1] is None:
            print(' exact_linear_recurrence_order',r,'coeff',z[0]); break
        elif z: print(' first_fit_order',r,'coeff',z[0],'first_falsifier_index',xs[z[1]][0])
