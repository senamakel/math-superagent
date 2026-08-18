from math import comb
from fractions import Fraction
counts=[4,30,97,236,485,890,1505]
h=[2,4,6,8,10,12,14]
full=[comb(x+4,4) for x in h]
comp=[full[i]-2*counts[i] for i in range(len(h))]
print('counts',counts)
print('complement',comp)
for name,s in [('counts',counts),('complement',comp)]:
    row=s[:]
    print(name,'differences')
    for k in range(1,len(s)):
        row=[row[i+1]-row[i] for i in range(len(row)-1)]
        print(k,row)
for x,c in zip(h,comp):
    f=Fraction(x*x+14*x+8,8)
    print('formula',x,c,f,c==f)
x=16
cf=Fraction(x*x+14*x+8,8)
print('next_prediction',x,cf,(comb(x+4,4)-cf)/2)
