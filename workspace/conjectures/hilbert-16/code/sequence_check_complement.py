from math import comb
terms=[4,30,97,236,485,890,1505]
for i,a in enumerate(terms):
 h=2+2*i
 c=comb(h+4,4)-2*a
 pred=(h*h+14*h+8)//8 if h>=4 else None
 print(h,a,comb(h+4,4),c,pred,c==pred if pred is not None else 'exception')
# first falsifier predicted by formula is h=2; next extrapolated h=16 is supplied
assert all(comb((2+2*i)+4,4)-2*a == ((2+2*i)**2+14*(2+2*i)+8)//8 for i,a in enumerate(terms) if i>=1)
print('all h=4..14 pass')
