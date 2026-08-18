from __future__ import annotations
from pathlib import Path
from fractions import Fraction
import re

ROOT=Path(__file__).resolve().parents[1]/'out'
FILES=['c1_terms.txt','counts.txt','lmin.txt','psi_exact.txt','psi_residues.txt','ext_recurrence.txt','extrecur_res.txt','dj_raw.txt','dj_mod.txt','topelitz_defects.txt','vr_rungaps.txt','r_runs_wythoff.txt']

def rows(path):
    out=[]
    for line in (ROOT/path).read_text().splitlines():
        nums=re.findall(r'-?\d+',line)
        if nums:
            out.append(tuple(map(int,nums)))
    return out

def vals(path):
    rs=rows(path)
    # All compact sequence artifacts are index/value rows; retain last field.
    return [r[-1] for r in rs if len(r)>=2]

def rec(seq, order):
    if len(seq)<=2*order: return False
    # exact rational solve using first equations, then check every term
    import sympy as sp
    cs=sp.symbols('c:'+str(order))
    eq=[]
    for n in range(order,len(seq)):
        eq.append(sp.Eq(seq[n],sum(cs[j]*seq[n-1-j] for j in range(order))))
    sol=sp.solve(eq[:order],cs, dict=True)
    if not sol: return False
    s=sol[0]
    if any(c not in s for c in cs): return False
    return all(sp.Rational(seq[n])==sum(s[cs[j]]*seq[n-1-j] for j in range(order)) for n in range(order,len(seq)))

def first_bad(pred, seq):
    for i,(a,b) in enumerate(zip(seq,pred),1):
        if a!=b:return i,a,b
    return None

def main():
    print('schema audit')
    for f in FILES:
        p=ROOT/f
        if not p.exists(): continue
        v=vals(f)
        print(f, 'terms=',len(v), 'prefix=',v[:8])
        good=[o for o in range(1,13) if rec(v,o)]
        print('  exact homogeneous recurrence orders <=12:',good or 'none')
    c=vals('c1_terms.txt'); counts=vals('counts.txt'); lm=vals('lmin.txt')
    # c1 slope law using exact quadratic irrational comparison: floor(k*(3-sqrt5)/2)
    import math
    bad=[]
    for k,a in enumerate(c,1):
        x=k*(3-math.sqrt(5))/2
        if a != 1+math.floor(x): bad.append((k,a,1+math.floor(x)))
    print('c1 slope first bad:',bad[:1] or 'none through '+str(len(c)))
    print('count=k+1 first bad:',first_bad([k+1 for k in range(1,len(counts)+1)],counts))
    # exact Fibonacci next law
    fib=[1,2]
    while fib[-1]<=max(lm)+10000:fib.append(fib[-1]+fib[-2])
    pred=[]
    for k in range(1,len(lm)+1):
        nxt=next(x for x in fib if x>k)
        pred.append(k+nxt-1)
    print('Lmin law first bad:',first_bad(pred,lm))
    # supplied run gaps and starts, exact integer square root of 5 comparison
    rr=rows('r_runs_wythoff.txt')
    starts=[r[0] for r in rr if len(r)>=2]
    bad=[]
    for j,s in enumerate(starts,1):
        # floor(j phi^2)=floor(j*(3+sqrt5)/2), integer-safe
        q=(3*j+math.isqrt(5*j*j))//2
        if s!=q: bad.append((j,s,q));break
    print('Wythoff starts first bad:',bad[:1] or 'none through '+str(len(starts)))

if __name__=='__main__': main()
