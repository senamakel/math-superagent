#!/usr/bin/env python3
"""Prove F2 family (10^k-10, 10^k-9) by exact decimal identity:
 A_k = 10^k-10:  (10^k-10)^2 = concat(10^k-20, 0*(k-3), 10, 0); blocks sum = 10^k-10
 B_k = 10^k-9 :  (10^k-9)^2  = concat(10^k-18, 0*(k-2), 8, 1 ); blocks sum = 10^k-9
Verify every k. If both members verified for all k>=3, F2 is a proven infinite family.
Derivations:
 (10^k-10)^2 = 10^{2k}-2*10^{k+1}+100: first k digits = 10^k-20, last k digits = 00..00100
 (10^k-9)^2  = 10^{2k}-18*10^k+81  : first k digits = 10^k-18, last k digits = 00..0081
"""
def check(k, vals, m):
    concat = "".join(str(v) for v in vals)
    return (concat == str(m*m), sum(vals) == m, concat)

okA = okB = True
for k in range(3, 81):
    mA = 10**k - 10
    valsA = [10**k - 20] + [0]*(k-3) + [10, 0]
    cA = check(k, valsA, mA)[0] and check(k, valsA, mA)[1]
    okA = okA and cA
    mB = 10**k - 9
    valsB = [10**k - 18] + [0]*(k-2) + [8, 1]
    cB = check(k, valsB, mB)[0] and check(k, valsB, mB)[1]
    okB = okB and cB
print(f"A (10^k-10): identity holds for all k in 3..80 -> {okA}")
print(f"B (10^k-9 ): identity holds for all k in 3..80 -> {okB}")
print(f"F2 family proven for all k>=3 (both members S-roots): {okA and okB}")
for k in (3,4,5):
    print(f"  k={k}")
    mA=10**k-10; mB=10**k-9
    va=[10**k-20]+[0]*(k-3)+[10,0]
    vb=[10**k-18]+[0]*(k-2)+[8,1]
    print(f"    A: {'+'.join(map(str,va))} -> {'+'+str(mA)} concat_ok={check(k,va,mA)[0]}")
    print(f"    B: {'+'.join(map(str,vb))} -> {'+'+str(mB)} concat_ok={check(k,vb,mB)[0]}")
