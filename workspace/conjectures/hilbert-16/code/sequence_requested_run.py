from math import comb
from fractions import Fraction
import sympy as sp

# Recompute the two relevant artifact sequences from definitions/formulas.
# S_k is the sourced lower-bound family formula in research/sequence-s-k-findings.md.
def S(k):
    return Fraction(4**(k-1)*(6*k-13),6) + Fraction(2*k-1,3)

s = [S(k) for k in range(1,25)]
print('S_k k=1..24:', s)
print('S_k integer indices:', [k for k,x in enumerate(s,1) if x.denominator==1])
print('S recurrence residuals:', [s[i+4]-10*s[i+3]+33*s[i+2]-40*s[i+1]+16*s[i] for i in range(len(s)-4)])

# Exact monomial-count data available in code/out/mono_counts.captured.txt.
a = [4,30,97,236,485,890]
h = [2,4,6,8,10,12]
ambient = [comb(x+4,4) for x in h]
comp = [ambient[i]-a[i] for i in range(len(a))]
print('Bautin monomial counts A_h:', a)
print('ambient dimensions:', ambient)
print('complements:', comp)
print('complement first differences:', [comp[i+1]-comp[i] for i in range(len(comp)-1)])
print('complement second differences:', [comp[i+2]-2*comp[i+1]+comp[i] for i in range(len(comp)-2)])
# exact polynomial interpolation check, deliberately label as conjectural if it fits.
x=sp.symbols('x')
poly=sp.interpolate(list(zip(h,comp)),x)
print('interpolating polynomial:', sp.factor(poly))
print('polynomial residuals:', [sp.expand(poly.subs(x,z)-y) for z,y in zip(h,comp)])
# recurrence search over supplied terms only
for r in range(1,4):
    cs=sp.symbols('c:'+str(r))
    eq=[sp.Eq(a[i],sum(cs[j]*a[i-j-1] for j in range(r))) for i in range(r,len(a))]
    print('A recurrence order',r,sp.solve(eq,cs,dict=True))
