from fractions import Fraction
from math import comb
from sympy import Matrix

# Exact sequences already produced by the investigation's captures.
a=[4,30,97,236,485,890,1505]
h=[2,4,6,8,10,12,14]
full=[comb(x+4,4) for x in h]
c=[full[i]-2*a[i] for i in range(len(a))]
print('a=',a)
print('c=',c)
print('full=',full)
for name,s in [('a',a),('c',c)]:
    print(name,'first differences=',[s[i+1]-s[i] for i in range(len(s)-1)])
    for r in range(1,7):
        M=Matrix([[s[i-j-1] for j in range(r)] for i in range(r,len(s))])
        b=Matrix(s[r:])
        try:
            sol=M.gauss_jordan_solve(b)[0]
            print(name,'recurrence_order',r,'exact_fit=True','coefficients=',list(sol))
        except Exception:
            print(name,'recurrence_order',r,'exact_fit=False')
print('candidate c=(h^2+14h+8)/8')
for x,y in zip(h,c):
    f=Fraction(x*x+14*x+8,8)
    print(x,y,f,y==f)
