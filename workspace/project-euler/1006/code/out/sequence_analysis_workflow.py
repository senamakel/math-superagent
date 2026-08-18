"""Reproducible bounded sequence audit for PE1006 artifacts.

This is a diagnostic, not a solver: it reads stored integer sequences, applies
exact rational recurrence fitting and modular Berlekamp--Massey, and reports
finite-range conjectures/falsifiers.
"""
from pathlib import Path
from fractions import Fraction

M = 101001001

def sequence(name, col=1):
    ans=[]
    for line in (Path('code/out')/name).read_text().splitlines():
        a=line.split()
        if len(a)>col and a[0].lstrip('-').isdigit():
            ans.append(int(a[col]))
    return ans

def first_failure(seq, order):
    if len(seq) <= 2*order: return None
    # Fit exact coefficients using the first order equations.
    from sympy import Matrix, Rational
    A=[]; b=[]
    for n in range(order, 2*order):
        A.append([Rational(seq[n-i-1]) for i in range(order)])
        b.append(Rational(seq[n]))
    try: c=Matrix(A).inv()*Matrix(b)
    except Exception: return ('singular',)
    for n in range(order, len(seq)):
        if sum(c[i]*seq[n-i-1] for i in range(order)) != seq[n]:
            return n+1
    return None

def bm(seq, mod):
    C=[1]; B=[1]; L=0; m=1; b=1
    for n,x in enumerate(seq):
        d=x%mod
        for i in range(1,L+1): d=(d+C[i]*seq[n-i])%mod
        if d==0: m+=1; continue
        T=C[:]; coef=d*pow(b,-1,mod)%mod
        C += [0]*max(0,len(B)+m-len(C))
        for j in range(len(B)): C[j+m]=(C[j+m]-coef*B[j])%mod
        if 2*L<=n: L=n+1-L; B=T; b=d; m=1
        else: m+=1
    return L

for name in ('psi_exact.txt','psi_residues.txt','c1_terms.txt','lmin.txt','dj_raw.txt','ext_recurrence.txt','extrecur_res.txt'):
    s=sequence(name)
    if not s: continue
    print(name, 'n=',len(s), 'first10=',s[:10])
    print(' exact recurrence first failures orders 1..12=', [first_failure(s,o) for o in range(1,13)])
    print(' BM(M)=',bm(s,M))
print('c1 formula is recorded separately; counts/lmin checks are in analyze_existing_sequences.py')
