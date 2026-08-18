"""Exact artifact survey: recurrence candidates and first falsifiers."""
from pathlib import Path
import sympy as sp

OUT=Path('code/out')
def vals(name):
    a=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        if len(z)>=2:
            try:a.append((int(z[0]),int(z[1])))
            except ValueError:pass
    return a

def first_bad(xs, f):
    return next(((k,v,f(k)) for k,v in xs if v!=f(k)), None)

def floor_alpha(k):
    # exact floor(k*(3-sqrt(5))/2), using SymPy algebraic integer arithmetic
    return int(sp.floor(sp.Rational(k,2)*(3-sp.sqrt(5))))

psi=vals('psi_residues.txt'); c1=vals('c1_terms.txt'); cnt=vals('counts.txt'); lm=vals('lmin.txt')
print('terms',*(f'{n}={len(vals(n))}' for n in ['psi_residues.txt','psi_exact.txt','c1_terms.txt','counts.txt','lmin.txt','dj_raw.txt']))
print('c1 exact first_bad',first_bad(c1,lambda k:1+floor_alpha(k)))
print('counts first_bad',first_bad(cnt,lambda k:k+1))
fib=[1,1]
while fib[-1]<=max(k for k,_ in lm):fib.append(fib[-1]+fib[-2])
print('lmin first_bad',first_bad(lm,lambda k:k+next(x for x in fib if x>k)-1))
print('psi mod100 first_bad',next(((k,v,(1+floor_alpha(k))%100) for k,v in psi if v%100!=(1+floor_alpha(k))%100),None))
print('psi mod1000 first_bad',next(((k,v,(1+floor_alpha(k))%1000) for k,v in psi if v%1000!=(1+floor_alpha(k))%1000),None))
a=[v for _,v in vals('psi_exact.txt')]
for d in range(1,11):
    try:r=sp.polys.ring_series.find_simple_recurrence(a,n=d)
    except Exception:r=None
    if r not in (None,[],[0]*d):print('psi_exact recurrence',d,r)
print('psi_exact recurrence orders 1..10: none')
