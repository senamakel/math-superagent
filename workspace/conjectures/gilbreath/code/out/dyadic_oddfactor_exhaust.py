#!/usr/bin/env python3
"""Odd-factor half, exhaustive on small periods: for EVERY word of period P
(with odd part), does nu2 grow or stay bounded? Classify words by nu2 at
large m. Also verify the constant words (000,111 for P=3) collapse."""
import itertools, functools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def nu2_stable(word, m):
    h=[int(word[j%len(word)]) for j in range(m)]
    w=0
    for c in range(1,m):
        s=0
        for i in submasks(c):
            s ^= h[m-1-c+i]
        w+=s
    return w

def period_pwords(P):
    return [''.join(map(str,b)) for b in itertools.product([0,1],repeat=P)]

print("P=3 (odd part 3): all 8 words, nu2 at m=500 and m=3000")
for w in period_pwords(3):
    a=nu2_stable(w,500); b=nu2_stable(w,3000)
    print(f"  {w}: m=500 {a}, m=3000 {b}, {'COLLAPSE' if b<15 else 'grow'}")

print("P=5: all 32 words")
for w in period_pwords(5):
    b=nu2_stable(w,3000)
    flag='COLLAPSE' if b<15 else 'grow'
    print(f"  {w}: m=3000 {b} {flag}")
