#!/usr/bin/env python3
"""Pin the exact recursion of the Mersenne c_r/2 arrays (verified data, k=2..10).

Observations from verified output:
  * tail of P_k = P_{k-1} with only the SECOND entry incremented by 1.
  * first half of P_k ends in [2,2].
  Hypothesis to test: P_k is generated from P_{k-1} by a doubling rule.

Verified arrays (c_r/2), hardcoded from the confirmation run:
"""
import itertools

P = {
 2:[1,1,1],
 3:[1,3,2,2,1,2,1],
 4:[1,7,4,4,2,4,2,2,1,4,2,2,1,2,1],
 5:[1,15,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
}

# Test 1: tail recursion  P_k = P_{k-1} with only entry[1] += 1
for k in [3,4,5]:
    Pk=P[k]; Pkm=P[k-1]
    tail=Pk[2**(k-1):]
    # expect tail == Pkm with tail[1]+=1? Pkm has length 2^(k-1)-1, same as tail
    expected=list(Pkm); 
    # difference: compare
    diff=[(i,a,b) for i,(a,b) in enumerate(zip(tail,expected)) if a!=b]
    print(f"k={k} tail-as-P_{k-1} diffs: {diff}")

# Test 2: first-half recursion. len(Pk first half)=2^(k-1).
for k in [3,4,5]:
    h=P[k][:2**(k-1)]
    # hypothesis: h = P_{k-1} with each entry doubled, then boundary adjust
    Pkm=P[k-1]; hd=[2*x for x in Pkm]
    # h has len 2^(k-1), hd has len 2^(k-1)-1. Compare h[:-1] vs hd
    diff=[(i,a,b) for i,(a,b) in enumerate(zip(h[:-1],hd)) if a!=b]
    print(f"k={k} first-half[:-1] vs 2*P_{k-1} diffs: {diff}")

# Test 3: what is the last element relation? h[-1] vs Pkm[-1]
for k in [3,4,5]:
    h=P[k][:2**(k-1)]
    print(f"k={k} h[-1]={h[-1]} h[-2]={h[-2]}")
