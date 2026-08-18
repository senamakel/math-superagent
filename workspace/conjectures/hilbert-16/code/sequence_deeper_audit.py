from fractions import Fraction
from math import comb
from sympy import Matrix

a=[4,30,97,236,485,890,1505]
d=[4,6,8,10,12,14,16]
D=[8,192,18432,1105920,22295347200,37456183296000]
hs=[x-2 for x in d]
print('a=',a)
print('complement=',[comb(h+4,4)-2*x for h,x in zip(hs,a)])
for h,x in zip(hs,a):
    pred=(comb(h+4,4)-Fraction(h*h+14*h+8,8))/2
    print('formula',h,'actual',x,'pred',pred,'PASS',pred==x)
for r in range(1,4):
    rows=[]; rhs=[]
    for i in range(r,len(a)):
        rows.append([a[i-j-1] for j in range(r)])
        rhs.append(a[i])
    M=Matrix(rows); b=Matrix(rhs)
    try:
        sol=M.gauss_jordan_solve(b)
        ok=True
    except ValueError:
        sol=None; ok=False
    print('a recurrence order',r,'fits',ok,'solution',sol)
for q in D:
    x=q; v2=v3=0
    while x%2==0:v2+=1;x//=2
    while x%3==0:v3+=1;x//=3
    print('D',q,'v2',v2,'v3',v3,'oddpart',x)
for h in (16,18,20):
    c=Fraction(h*h+14*h+8,8)
    print('predicted',h,'c',c,'a', (comb(h+4,4)-c)/2)
