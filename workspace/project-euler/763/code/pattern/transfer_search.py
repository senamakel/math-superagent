"""Search for an exact transfer recurrence on R(N,M) (configs by max level M),
the 3D analog of the 2D G(k,m) kernel recurrence. Fit on N<=13, test OOS on N=14.
Model: R(N,M) = sum_{j=1..L, m' in window} c[j][m'-M] R(N-j,m').
We use RATIONAL least squares and check exactness on training rows, then OOS.
"""
import collections
from fractions import Fraction
import itertools

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

# Training rows 3..13, test row 14.
def build(L, dwin):
    """features: for each training (N,M), vector of R(N-j, M + d) for j=1..L, d in dwin."""
    rows=[]; targets=[]
    # only consider M present in R[N] (use M range min..max)
    train_Ns = list(range(3, 14))
    minM = min(m for N in train_Ns for m in R[N])
    maxM = max(m for N in train_Ns for m in R[N])
    cols = [(j, d) for j in range(1, L+1) for d in dwin]
    for N in train_Ns:
        for M in sorted(R[N]):
            feat=[]
            for (j, d) in cols:
                Mv = M + d
                if Mv >= 0:
                    feat.append(R[N-j].get(Mv, 0))
                else:
                    feat.append(0)
            if all(f==0 for f in feat):
                continue
            rows.append(feat); targets.append(R[N][M])
    return rows, targets, cols

def solve_exact(rows, targets):
    # solve over rationals by building integer linear system and doing integer gaussian
    # To keep simple: use sympy rational least squares = solve normal equations.
    import sympy as sp
    A = sp.Matrix(rows); b = sp.Matrix(targets)
    # exact least squares: A^T A c = A^T b
    AtA = A.T*A; Atb = A.T*b
    c = AtA.solve(Atb) if AtA.det()!=0 else AtA.LUsolve(Atb)
    return list(c)

def predict(c, rows):
    return [round(sum(ci*fi for ci,fi in zip(c,row))) for row in rows]

for L, dwin in [(2,[-1,0,1]), (3,[-1,0,1]), (2,[-2,-1,0,1,2]), (3,[-1,0,1,2]),
                (4,[-1,0,1]), (3,[-2,-1,0,1,2]), (2,[0,1]), (3,[0,1])]:
    rows, targets, cols = build(L, dwin)
    c = solve_exact(rows, targets)
    pred = predict(c, rows)
    train_err = sum(abs(p-t) for p,t in zip(pred,targets))
    # OOS test on N=14
    oos=[]
    oost=[]
    N=14
    for M in sorted(R[14]):
        feat=[]
        for (j,d) in cols:
            Mv=M+d
            feat.append(R[14-j].get(Mv,0) if Mv>=0 else 0)
        if all(f==0 for f in feat): continue
        oos.append(feat); oost.append(R[14][M])
    opred = predict(c, oos)
    oos_err = sum(abs(p-t) for p,t in zip(opred,oost))
    print(f"L={L} dwin={dwin} nparams={len(cols)} train_err={train_err} OOS(N=14)_err={oos_err}")
    if oos_err==0:
        print("   !!! OOS EXACT: coeffs=", [str(x) for x in c])
