from pathlib import Path
import sympy as sp
ROOT=Path(__file__).parents[1]/'out'

def seq(name):
    out=[]
    for line in (ROOT/name).read_text().splitlines():
        z=line.split()
        if z:
            try: out.append(int(z[-1]))
            except ValueError: pass
    return out

def find_linear_recurrence(a,max_order=12):
    for r in range(1,min(max_order,len(a)-1)+1):
        cs=sp.symbols('c:'+str(r))
        eq=[sp.Eq(a[n],sum(cs[i]*a[n-1-i] for i in range(r))) for n in range(r,len(a))]
        sol=sp.solve(eq,cs,dict=True)
        if sol: return r,sol
    return None

def analyze_sequence(a):
    d=[a[i+1]-a[i] for i in range(len(a)-1)]
    return {'n':len(a),'first':a[:10],'diff_first':d[:20],
            'distinct_diffs':sorted(set(d))}

def main():
    names=['psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','dj_raw.txt','topelitz_defects.txt']
    for name in names:
        a=seq(name)
        print(name, analyze_sequence(a))
        print('linear_recurrence_order<=12',find_linear_recurrence(a))
    # Exact already-known formulas, with explicit first-falsifier scans.
    c=seq('c1_terms.txt'); bad=None
    for k,v in enumerate(c,1):
        e=1+int(sp.floor(sp.Rational(k,2)*(3-sp.sqrt(5))))
        if v!=e: bad=(k,v,e); break
    print('c1_floor_formula_first_bad',bad)
    l=seq('lmin.txt'); fib=[1,1]
    while fib[-1]<=len(l)+10: fib.append(fib[-1]+fib[-2])
    bad=None
    for k,v in enumerate(l,1):
        nxt=next(x for x in fib if x>k)
        if v!=k+nxt-1: bad=(k,v,k+nxt-1); break
    print('lmin_formula_first_bad',bad)
    # Candidate exact regularity: Toeplitz zero defect at Fibonacci-indexed k.
    t=seq('topelitz_defects.txt')
    zeros=[k for k,v in enumerate(t,1) if v==0]
    print('toeplitz_zero_indices_first',zeros[:30])
    print('toeplitz_zero_all_fib_minus1_through_400',all(t[k-1]==0 for k in [1,2,4,7,12,20,33,54,88,143,232] if k<=len(t)))
if __name__=='__main__': main()
