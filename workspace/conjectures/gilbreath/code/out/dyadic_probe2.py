#!/usr/bin/env python3
"""Find the structural pattern of the fold output y_c for h periodic of period
2^k, over the full encoder index range c=1..m. Test:
  - for each period-2^k word, is nu2 (sum of y_c) bounded in m?
  - is y_c itself eventually periodic / eventually zero?
  - decompose y over c: at which c does the support live?
"""
def submasks(c):
    out=[]; i=c
    while True:
        out.append(i); 
        if i==0: break
        i=(i-1)&c
    return out

def y_seq(h, m):
    N=m-1
    return [ reduce(lambda a,b:a^b, (h[N-c+i] for i in submasks(c)), 0) for c in range(1,m+1)]

def periodic_h(word, m):
    L=len(word)
    return [int(word[j%L]) for j in range(m)]

import functools
reduce=functools.reduce

for word in ["01","0011","0110","1010","1111","0000","00001111","11110000","00110011","01010101","10100101"]:
    nu2s=[sum(y_seq(periodic_h(word,m),m)) for m in [40,100,200,400,800,1600]]
    print(f"word {word} period {len(word)}  nu2 at m=40..1600: {nu2s}")

print()
# full y for two interesting words at m=64
for word in ["0110","1010","01010101"]:
    m=64
    y=y_seq(periodic_h(word,m),m)
    ones=[c+1 for c,v in enumerate(y) if v]
    print(word, "ones at c:", ones, " count=",len(ones))
