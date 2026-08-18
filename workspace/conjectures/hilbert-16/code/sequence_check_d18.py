from math import comb
from fractions import Fraction
# Exact test of the complement conjecture against the newly computed L16 row.
# The next falsifier d=18 is not computed here: its prediction is explicit.
a={4:4,6:30,8:97,10:236,12:485,14:890,16:1505}
for d,v in sorted(a.items()):
 h=d-2
 c=comb(h+4,4)-2*v
 pred=Fraction(h*h+14*h+8,8)
 assert pred.denominator==1
 print(f'd={d} h={h} count={v} complement={c} predicted={pred} match={c==pred}')
assert all(comb(d+2,4)-2*v == (h*h+14*h+8)//8 for d,v in a.items() if (h:=d-2)>=4)
h=16
pred=(comb(h+4,4)-Fraction(h*h+14*h+8,8))/2
print('next falsifier: d=18 h=16 predicted_count=',pred)
