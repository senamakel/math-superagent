from math import comb
from fractions import Fraction
from itertools import combinations

def diffs(a):
    out=[]
    while a:
        out.append(a); a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return out

def rec_fit(a,r):
    # solve exact linear system for c0..c(r-1), a[n]=sum c_j*a[n-1-j]
    import sympy as s
    cs=s.symbols('c:'+str(r)); eq=[]
    for n in range(r,len(a)):
        eq.append(s.Eq(a[n],sum(cs[j]*a[n-1-j] for j in range(r))))
    sol=s.solve(eq,cs, dict=True)
    return sol

A=[4,30,97,236,485,890,1505]
H=[4,6,8,10,12,14,16]
C=[comb(h+4,4)-2*a for h,a in zip(H,A)]
print('sequence audit: exact integer Bautin monomial counts and complements')
print('A=',A); print('H=',H); print('C=',C)
print('C first differences=',[d for d in diffs(C)[1]])
print('C second differences=',diffs(C)[2])
for r in range(1,7): print('recurrence order',r,'solutions',rec_fit(A,r))
print('quadratic conjecture C=(h^2+14h+8)/8 on h=4..14:', all(C[i]==(H[i]**2+14*H[i]+8)//8 for i in range(6)))
print('exception h=2: predicted', (2**2+14*2+8)//8, 'versus observed 7')
print('h=16 predicted C=',(16**2+14*16+8)//8,'A=',(comb(20,4)-61)//2)
