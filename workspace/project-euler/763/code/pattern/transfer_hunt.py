"""Hunt for a row-to-row (transfer) recurrence in R(N,M) of the form
R(N,M) = a*R(N-1,M) + b*R(N-1,M-1) + c*R(N-1,M-2) + ...
The 2D analog (A007902) has exactly such a G(k,m) two-index recurrence, and
it is what would let us compute D(10000) instead of BFS.
Also try R(N,M) = sum over M' of T[M'][M] * R(N-1,M') (fixed transfer matrix).
"""
import collections, numpy as np

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

# Candidate: R(N,M) = c0*R(N-1,M) + c1*R(N-1,M-1) + c2*R(N-1,M-2) (local in index)
print("Test R(N,M) = c0 R(N-1,M) + c1 R(N-1,M-1) + c2 R(N-1,M-2)")
# collect equations
eqs=[]; targets=[]
for N in range(3,15):
    for M in R[N]:
        if N not in R: continue
        if M not in R[N-1] and M-1 not in R[N-1] and M-2 not in R[N-1]:
            pass
        a0=R[N-1].get(M,0); a1=R[N-1].get(M-1,0); a2=R[N-1].get(M-2,0)
        if a0==0 and a1==0 and a2==0: continue
        eqs.append([a0,a1,a2]); targets.append(R[N][M])
A=np.array(eqs,float); b=np.array(targets,float)
c,res,rank,sv=np.linalg.lstsq(A,b,rcond=None)
pred=A@c
print('  coeffs=',c)
print('  residuals sum abs=',np.sum(np.abs(pred-b)))
# too many or few points; check consistency on subset where all three coords exist

# Better: restrict to rows fully present. 
print()
print("Try combos — search small coeff sets over rows where R(N-1,M),R(N-1,M-1),R(N-2,M)...")
# Let's just inspect neighbor structure ratio R(N,M)/R(N-1,M) and R(N,M)/R(N-1,M-1)
print()
print("ratio R(N,M)/R(N-1,M) where both exist:")
for N in range(3,15):
    for M in sorted(R[N]):
        if M in R[N-1] and R[N-1][M]>0:
            print(f'  N={N} M={M}: {R[N][M]}/{R[N-1][M]} = {R[N][M]/R[N-1][M]:.4f}')
