#!/usr/bin/env python3
"""Prove F1 (10^k-1, 10^k) by decimal identity.
 A_k = 10^k-1: (10^k-1)^2 = 10^{2k}-2*10^k+1 = (10^k-2)*10^k + 1
   digits = str(10^k-2) + "0"*(k-1) + "1";  blocks [10^k-2, 0..0, 1],
   sum = (10^k-2)+1 = 10^k-1 (>=3 blocks).
 B_k = 10^k: seconds = str("1"+k zeros) + k zeros; blocks [10^k, 0..0], sum=10^k.
Both S-roots for all k>=2."""
def concat_ok(vals, m):
    concat = "".join(str(v) for v in vals)
    return concat == str(m*m) and sum(vals) == m
okA = okB = True
for k in range(2, 61):
    mA = 10**k - 1
    valsA = [10**k - 2] + [0]*(k-1) + [1]
    okA = okA and concat_ok(valsA, mA)
    mB = 10**k
    valsB = [10**k] + [0]*k
    okB = okB and concat_ok(valsB, mB)
print(f"A (10^k-1): blocks [10^k-2, 0*(k-1), 1] all k>=2 -> {okA}")
print(f"B (10^k)  : blocks [10^k, 0*k]               all k>=2 -> {okB}")
print(f"F1 family both members S-roots for all k>=2: {okA and okB}")
for k in (2,3,4):
    va=[10**k-2]+[0]*(k-1)+[1]; vb=[10**k]+[0]*k
    print(f"  k={k}: A {'+'.join(map(str,va))} concat_ok={concat_ok(va,10**k-1)} | "
          f"B {'+'.join(map(str,vb))} concat_ok={concat_ok(vb,10**k)}")
