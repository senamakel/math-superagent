from fractions import Fraction
from math import comb

# Data already produced by exact Bautin recurrence computations.
A = [4, 30, 97, 236, 485, 890, 1505]
D = [8, 192, 18432, 1105920, 22295347200, 37456183296000]
H = [d - 2 for d in range(4, 18, 2)]
C = [comb(h + 4, 4) - 2*a for h, a in zip(H, A)]
print('exact sequence audit; source: existing captures code/out/mono_counts.captured.txt and focal_denoms.captured.txt')
print('A=', A)
print('H=', H)
print('C=', C)
print('C first differences=', [C[i+1]-C[i] for i in range(len(C)-1)])
print('C second differences=', [C[i+2]-2*C[i+1]+C[i] for i in range(len(C)-2)])
print('quadratic candidate C=(h^2+14h+8)/8:')
for h,c in zip(H,C):
    p=Fraction(h*h+14*h+8,8)
    print(h,c,p,c==p)
print('first omitted test d=18 (h=16), candidate count=', (comb(20,4)-Fraction(16*16+14*16+8,8))/2)
print('denominator D=', D)
for p in (2,3):
    vals=[]
    for q in D:
        x=q; v=0
        while x%p==0: x//=p; v+=1
        vals.append(v)
    print('v',p,'=',vals)
