#!/usr/bin/env python3
"""Direct verification of the collapse lemma's crux: for h periodic of period
2^k, output_c = 0 for ALL c >= 2^k, and non-zero at most at c in 1..2^k-1.
Check over many words, many m, and several k."""
import functools, itertools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def y_seq(h,m):
    N=m-1
    return [reduce(lambda a,b:a^b,(h[N-c+i] for i in submasks(c)),0) for c in range(1,m+1)]

def periodic_h(word,m):
    L=len(word)
    return [int(word[j%L]) for j in range(m)]

def check(word,m):
    """Returns (max_c_with_one, any_violation) where violation = a 1 at c>=2^k."""
    L=len(word)
    k=L.bit_length()-1
    y=y_seq(periodic_h(word,m),m)
    nonzero_positions=[c+1 for c,v in enumerate(y) if v]
    viol=[c for c in range(1,m+1) if y[c-1]==1 and c>=L]
    return max(nonzero_positions) if nonzero_positions else 0, viol

# Exhaustive over all period-2^k words for k=1,2,3 at several m
for k in [1,2,3]:
    L=2**k
    viols=[]
    maxseen=0
    for bits in itertools.product([0,1],repeat=L):
        word=''.join(map(str,bits))
        for m in [60, 200, 601]:
            mx, viol=check(word,m)
            maxseen=max(maxseen,mx)
            if viol:
                viols.append((word,m,viol))
    print(f"k={k} L={L}: searched all words x m in {{60,200,601}} -> violations(c>=2^k nonzero): {len(viols)}; max nonzero c seen = {maxseen} (should be <= {L-1})")
