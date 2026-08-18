#!/usr/bin/env python3
"""Naive oracle for PE1006; exponential in k, used only at k=3,10."""
def fibword(k):
    a,b='0','01'
    while len(b)<k:
        a,b=b,b+a
    return b

def factors(k):
    w=fibword(k)
    # enlarge until factor set stabilizes; for these anchors S_10 is enough
    a,b='0','01'
    seen=set()
    while True:
        w=a
        seen |= {w[i:i+k] for i in range(max(0,len(w)-k+1))}
        if len(seen)==k+1 and len(w)>=k: return seen
        a,b=b,b+a

def psi(k,m=None):
    s=sum(int(x)**2 for x in (int(t) for t in factors(k)))
    return s if m is None else s%m

if __name__=='__main__':
    for k in (3,10): print(k, sorted(factors(k)), psi(k), psi(k,101001001))
