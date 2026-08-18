"""Exact audit of previously stored PE1006 sequence artifacts.

This deliberately does not compute Psi at the target bound. It tests only
stored finite sequences for exact low-order recurrences and exact candidate
laws, serving as reproducible evidence for the accompanying report.
"""
from pathlib import Path
import sympy as sp

OUT = Path(__file__).parent

def read_column(name, col):
    result=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        try: result.append(int(z[col]))
        except (ValueError, IndexError): pass
    return result

def first_bad(seq, predicate):
    for i,x in enumerate(seq,1):
        if not predicate(i,x): return (i,x)
    return None

def exact_recurrence(seq, order):
    if len(seq)<=2*order: return None
    cs=sp.symbols('c:'+str(order))
    equations=[sp.Eq(seq[n],sum(cs[j]*seq[n-1-j] for j in range(order)))
               for n in range(order,len(seq))]
    solutions=sp.solve(equations,cs,dict=True)
    return solutions[0] if solutions else None

def main():
    c1=read_column('c1_terms.txt',1)
    lmin=read_column('lmin.txt',1)
    psi=read_column('psi_residues.txt',1)
    toe=read_column('topelitz_defects.txt',-1)
    alpha=(3-sp.sqrt(5))/2
    fib=[0,1]
    while fib[-1] < max(lmin)+2: fib.append(fib[-1]+fib[-2])
    print('c1 floor law first bad:', first_bad(c1,lambda k,x:x==1+sp.floor(k*alpha)))
    print('Lmin formula first bad:', first_bad(lmin,lambda k,x:x==k+next(f for f in fib if f>k)-1))
    print('Toeplitz zero indices:', [k for k,x in enumerate(toe,1) if x==0])
    print('Psi mod100=c1 first bad:', first_bad(psi,lambda k,x:x%100==c1[k-1]%100))
    print('Psi mod1000=c1 first bad:', first_bad(psi,lambda k,x:x%1000==c1[k-1]%1000))
    for name, seq in [('c1',c1),('Lmin',lmin),('Psi residues',psi),('Toeplitz defect',toe)]:
        print(name,'exact recurrence <=12:',[(r,exact_recurrence(seq,r)) for r in range(1,13) if exact_recurrence(seq,r)])

if __name__=='__main__': main()
