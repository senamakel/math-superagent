from fractions import Fraction
from math import comb

# Exact continuation of the reported complement conjecture for h even >= 4.
def predicted_a(h):
    dim=comb(h+4,4)
    c=Fraction(h*h+14*h+8,8)
    return (dim-c)/2

for h in (4,6,8,10,12,14,16,18,20):
    print(h, predicted_a(h), 'integer=', predicted_a(h).denominator==1)

# Exact denominator sequence recurrence probes from the six reported terms.
D=[8,192,18432,1105920,22295347200,37456183296000]
for i in range(2,len(D)):
    print('ratio',i+1,D[i]//D[i-1], 'exact=', Fraction(D[i],D[i-1]))
