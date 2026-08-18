from fractions import Fraction
from math import comb
from sympy import Integer, Rational, Matrix

def fit_poly(xs, ys, deg):
    M=Matrix([[Integer(x)**j for j in range(deg+1)] for x in xs])
    b=Matrix(ys)
    try:
        sol=M[:deg+1,:].inv()*b[:deg+1,:]
    except Exception: return None
    return sol if all(sum(sol[j]*Integer(x)**j for j in range(deg+1))==y for x,y in zip(xs,ys)) else None

def recurrence(terms, order):
    # solve exact recurrence t_i=sum c_j t_{i-j-1}, using first order equations
    M=[]; b=[]
    for i in range(order,len(terms)):
        M.append([Integer(terms[i-j-1]) for j in range(order)])
        b.append(Integer(terms[i]))
    A=Matrix(M); B=Matrix(b)
    sol= next(iter(A.gauss_jordan_solve(B)), None) if A.rows==A.cols else None
    if sol is None: return None
    c=list(sol)
    return c if all(Integer(terms[i])==sum(c[j]*Integer(terms[i-j-1]) for j in range(order)) for i in range(order,len(terms))) else None

# newly available monomial count through d=16
A=[4,30,97,236,485,890,1505]
h=[2,4,6,8,10,12,14]
C=[comb(x+4,4)-2*y for x,y in zip(h,A)]
print('A',A)
print('C',C)
for deg in range(0,6): print('C polynomial degree',deg,fit_poly(h,C,deg))
for r in range(1,5): print('A recurrence order',r,recurrence(A,r))
# denominators, now exact d=4..14 only; separate d16 unavailable
D=[8,192,18432,1105920,22295347200,37456183296000]
print('D',D)
for p in [2,3,5,7]:
 def val(n):
  k=0
  while n%p==0: k+=1;n//=p
  return k
 print('v',p,[val(x) for x in D])
# exact proposed complement formula on all supplied rows
print('quadratic complement residuals', [8*c-(x*x+14*x+8) for x,c in zip(h,C)])
