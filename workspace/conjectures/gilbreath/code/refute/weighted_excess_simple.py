#!/usr/bin/env python3
"""Confirm R-weighted-excess-potential refuted with a SIMPLER counterexample
than the one on record (A=(1,4,12,0)). Independent check.

Claim: no weights w_i>=0 (w_1>0, summable) make
   P_k = sum_i w_i * max(0, A_k(i)-2)
non-increasing under A -> (|A_i - A_{i+1}|).

New counterexample: A = (1, 4, 0)
   d = max(0, A-2) = (0, 2, 0)            P = 2*w2
   child A' = (|1-4|, |4-0|) = (3, 4)
   d' = (1, 2)                            P' = w1 + 2*w2
   monotonicity: w1 + 2*w2 <= 2*w2  ==>  w1 <= 0  (contradicts w1 > 0)
"""
def child(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
def defect(row):
    return [max(0,x-2) for x in row]

A = [1,4,0]
Ap = child(A)
d, dp = defect(A), defect(Ap)
print("A        =", A, " defect d =", d)
print("child A' =", Ap, " defect d'=", dp)
print()
print("P(A)  = w1*0 + w2*2 + w3*0 = 2*w2")
print("P(A') = w1*1 + w2*2        = w1 + 2*w2")
print()
print("P(A') <= P(A) requires w1 + 2*w2 <= 2*w2, i.e. w1 <= 0.")
print("The rung mandates w1 > 0.  CONTRADICTION: every weight choice fails.")
print()
print("CONCLUSION: R-weighted-excess-potential is refuted. This is an")
print("independent, smaller counterexample than the (1,4,12,0) on record.")
