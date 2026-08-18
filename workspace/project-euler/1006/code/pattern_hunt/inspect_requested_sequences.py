"""Exact survey of stored PE1006 sequences; bounded pattern attack only."""
from pathlib import Path
import sympy as sp
from sympy.concrete.guess import guess_generating_function_rational, guess_generating_function
OUT=Path('code/out')

def rows(name):
    ans=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        if z and all(x.lstrip('-').isdigit() for x in z): ans.append([int(x) for x in z])
    return ans

def seq(name,col=1): return [r[col] for r in rows(name) if len(r)>col]
def first_bad(a,p):
    return next(((i+1,x) for i,x in enumerate(a) if not p(i+1,x,a)),None)
def rec(a,order):
    # exact homogeneous constant-coefficient recurrence, solve first available block
    cs=sp.symbols('c:'+str(order))
    eq=[]
    for i in range(order,len(a)):
        eq.append(sp.Eq(a[i],sum(cs[j]*a[i-1-j] for j in range(order))))
    sol=sp.solve(eq,cs, dict=True)
    return sol[0] if sol else None

def bm(a,m):
    # BM over prime modulus, returned complexity
    C=[1];B=[1];L=0;mshift=1;b=1
    for n in range(len(a)):
        d=a[n]%m
        for i in range(1,L+1): d=(d+C[i]*a[n-i])%m
        if d==0:mshift+=1;continue
        T=C[:]
        if sp.gcd(b,m)!=1: return None
        q=d*pow(b,-1,m)%m
        C += [0]*max(0,len(B)+mshift-len(C))
        for j in range(len(B)): C[j+mshift]=(C[j+mshift]-q*B[j])%m
        if 2*L<=n:L=n+1-L;B=T;b=d;mshift=1
        else:mshift+=1
    return L,C

def report(name,a):
    print(f"\n{name}: n={len(a)}")
    print('first=',a[:12])
    for d in range(1,min(12,len(a)//2)+1):
        if rec(a,d): print('exact recurrence order',d,rec(a,d)); break
    else: print('exact recurrence orders 1..12: none')
    for mod in (100,1000,101001001):
        z=bm(a,mod); print('BM modulus',mod,'complexity',None if z is None else z[0])

psi=seq('psi_exact.txt'); c1=seq('c1_terms.txt'); ext=seq('ext_recurrence.txt',4)
for n,a in [('psi_exact',psi),('c1',c1),('ext_final',ext)]: report(n,a)
# Established formula attacks, using exact integer/rational arithmetic.
alpha=(sp.Integer(3)-sp.sqrt(5))/2
print('\nc1 floor formula first falsifier:',first_bad(c1,lambda k,x,a:x==1+int(sp.floor(k*alpha))))
# ext final is v_R-like terminal value; test obvious Fibonacci/block hypotheses through stored range
print('ext final first differences=',[ext[i]-ext[i-1] for i in range(1,15)])
# sequence of pure run words: lengths, decimal values, and first digits
vr=[line.strip() for line in (OUT/'vr_runvals.txt').read_text().splitlines() if line.strip()]
print('\nvr_runvals: n=',len(vr),'lengths first=',[len(x) for x in vr[:15]])
print('vr first=',vr[:8])
print('vr decimal recurrence v[n]=? first falsifier for v_n = concat previous blocks omitted; no scalar claim asserted')
# OEIS-style lookup: local indexed sources only, explicitly report no network lookup.
print('\nOEIS lookup: no local exact match asserted for Psi; Fibonacci word source is A003849 (local source).')
