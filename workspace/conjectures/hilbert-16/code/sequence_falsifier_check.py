from fractions import Fraction
from math import comb

def counts_from_complement(h):
    c=Fraction(h*h+14*h+8,8)
    return (Fraction(comb(h+4,4))-c)/2

known={4:30,6:97,8:236,10:485,12:890,14:1505}
for h,a in known.items():
    pred=counts_from_complement(h)
    print(h, a, pred, 'PASS' if pred==a else 'FAIL')
print('first falsifier h=16 (d=18), prediction', counts_from_complement(16))
# parity/integrality check for all even h through 100
bad=[]
for h in range(2,101,2):
    if counts_from_complement(h).denominator != 1:
        bad.append(h)
print('nonintegral h <=100:',bad)
