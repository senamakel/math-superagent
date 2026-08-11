"""Robust transfer search on R(N,M): does any SHORT exact recurrence relate
R(N,M) to previous rows, with out-of-sample validation? Rank-safe exact solve.
"""
import collections
from fractions import Fraction

R = collections.defaultdict(dict)
for N in range(2,13):
    with open(f'data/level_{N}.txt') as f:
        for line in f:
            p=line.strip().split('|'); M=int(p[1].strip())
            R[N][M]=R[N].get(M,0)+1
with open('code/out/mhist_13_14.txt') as f:
    for line in f:
        line=line.strip()
        if line.startswith('N=') and 'M=' in line:
            lhs,rhs=line.split(': '); tok=lhs.split()
            N=int(tok[0][2:]); M=int(tok[1][2:]); R[N][M]=int(rhs)

import sympy as sp

def solve_minnorm(A, b):
    # minimum-norm least-squares solution over rationals: A^T A c = A^T b
    # handle singular via adding tiny? use sympy: solve AtA c = Atb, if singular
    # use pseudo-inverse via diagonalization (rational).
    AtA = A.T*A; Atb = A.T*b
    # rref approach: augment
    M2 = AtA.row_join(Atb)
    rref, pivots = M2.rref()
    # solve for free variables = 0 (minimal via rref back-substitution)
    n = AtA.shape[0]
    sol = [Fraction(0) for _ in range(n)]
    used=set()
    for piv in pivots:
        if piv < n:
            sol[piv]=rref[piv, n]
            for j in range(piv+1,n):
                if rref[piv,j]!=0:  # free var, set 0
                    pass
    # back-substitute the pivot equation properly
    # simpler: build reduced system from rref rows that are pivot rows
    # We'll do full back substitution in exact fraction
    pivrows=[]; pivcols=[]
    for i,r in enumerate(rref.tolist()):
        # find first nonzero
        first=None
        for j in range(n):
            if r[j]!=0:
                first=j; break
        if first is not None and r[n]!=0 or (first is not None):
            if all(r[j]==0 for j in range(n)):
                if r[n]!=0:
                    return None  # inconsistent
                continue
            pivrows.append(i); pivcols.append(first)
    # back substitute from last pivot upward
    sol=[Fraction(0) for _ in range(n)]
    for rr in reversed(range(len(pivrows))):
        i=pivrows[rr]; pcol=pivcols[rr]
        val=Fraction(rref[i,n])
        for j in range(pcol+1,n):
            val-=rref[i,j]*sol[j]
        sol[pcol]=val/rref[i,pcol]
    return sol

def build(L, dwin, trainN):
    cols=[(j,d) for j in range(1,L+1) for d in dwin]
    nparams=len(cols)
    rows=[]; targets=[]
    for N in trainN:
        for M in sorted(R[N]):
            feat=[R[N-j].get(M+d,0) if (M+d)>=0 else 0 for (j,d) in cols]
            if all(f==0 for f in feat): continue
            rows.append(feat); targets.append(R[N][M])
    return rows,targets,cols

for L, dwin in [(2,[-1,0,1]),(2,[0,1,2]),(2,[-1,0,1,2]),(1,[-1,0,1]),(1,[0,1]),
                (3,[-1,0,1]),(2,[-2,-1,0,1,2])]:
    # train on N=3..13 (11 rows), OOS N=14
    rows,targets,cols=build(L,dwin,range(3,14))
    A=sp.Matrix(rows); b=sp.Matrix(targets)
    sol=solve_minnorm(A,b)
    trainerr=sum(abs(int(round(sum(si*fi for si,fi in zip(sol,row))))-t)
                 for row,t in zip(rows,targets)) if sol else None
    # OOS
    orows,otargets,_=build(L,dwin,[14])
    ooserr=sum(abs(int(round(sum(si*fi for si,fi in zip(sol,row))))-t)
               for row,t in zip(orows,otargets)) if sol else None
    print(f"L={L} dwin={dwin} nparams={len(cols)} nrows={len(rows)} train_err={trainerr} OOS_err={ooserr}")
    if sol and ooserr==0 and trainerr==0:
        print("   OOS+train EXACT:",[str(x) for x in sol])
