from math import comb
from fractions import Fraction
from sympy import Matrix

# Exact sequences extracted from completed captures.
counts=[4,30,97,236,485,890]
counts16=[1505]  # independently recorded in sequence_current_patterns.py
seq=counts+counts16
h=[2,4,6,8,10,12,14]
# Complement to full homogeneous degree-h monomial space in 5 variables.
full=[comb(x+4,4) for x in h+[14]]
comp=[full[i]-2*seq[i] for i in range(len(seq))]
print('counts',seq)
print('full',full)
print('complement',comp)
for name,s in [('counts',seq),('complement',comp)]:
    for r in range(1,min(7,len(s))):
        rows=[[s[i-j-1] for j in range(r)] for i in range(r,len(s))]
        rhs=[s[i] for i in range(r,len(s))]
        try:
            sol=Matrix(rows).gauss_jordan_solve(Matrix(rhs))
            print(name,'order',r,'exact_fit',True,'solution',sol)
        except Exception:
            print(name,'order',r,'exact_fit',False)
print('candidate complement formula c=(h^2+14h+8)/8')
for x,c in zip(h+[14],comp):
    f=Fraction(x*x+14*x+8,8)
    print(x,c,f,c==f)
# denominator sequence exact over supplied terms
D=[8,192,18432,1105920,22295347200,37456183296000]
print('denominators',D)
for p in [2,3]:
 vals=[]
 for n in D:
  v=0
  while n%p==0:v+=1;n//=p
  vals.append(v)
 print('valuation',p,vals)
