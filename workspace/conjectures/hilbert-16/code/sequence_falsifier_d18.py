from math import comb
# Existing exact counts through d=16; test first falsifier predicted by the complement conjecture.
counts=[4,30,97,236,485,890,1505]
h=[4,6,8,10,12,14,16]
complements=[comb(x+4,4)-2*a for x,a in zip(h,counts)]
print('exact falsifier target: h=16 (d=18)')
print('known complements:', complements)
print('conjectured complement at h=16:', (16*16+14*16+8)//8)
print('conjectured count at d=18:', (comb(20,4)-61)//2)
print('No independently computed L18 count is available; this run cannot test the falsifier.')
