from math import comb
from fractions import Fraction
from sympy import Matrix
# Exact terms already computed by mono_counts.py and captured on disk.
a=[4,30,97,236,485,890,1505]
d=[4,6,8,10,12,14,16]
h=[x-2 for x in d]
c=[comb(t+4,4)-2*x for t,x in zip(h,a)]
print('terms a',a)
print('terms c',c)
# Verify proposed complement formula on every supplied term.
for t,x,y in zip(h,c,a):
    f=Fraction(t*t+14*t+8,8)
    print(t, 'c',x, 'formula',f, 'PASS',x==f)
# Exact recurrence search, orders 1..6, for both sequences.
def fits(seq,r):
    rows=[]; rhs=[]
    for i in range(r,len(seq)):
        rows.append([seq[i-j-1] for j in range(r)])
        rhs.append(seq[i])
    try:
        sol=Matrix(rows).gauss_jordan_solve(Matrix(rhs))
        return True,sol
    except ValueError:
        return False,None
for name,seq in [('a',a),('c',c)]:
    for r in range(1,7):
        ok,sol=fits(seq,r)
        print(name,'recurrence_order',r,'fits',ok)
for t in [16,18,20]:
    cc=Fraction(t*t+14*t+8,8)
    aa=(comb(t+4,4)-cc)/2
    print('falsifier candidate h',t,'predicted c',cc,'predicted a',aa)
