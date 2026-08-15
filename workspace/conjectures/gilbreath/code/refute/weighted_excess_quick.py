#!/usr/bin/env python3
import subprocess, sys
sys.path.insert(0, "/workspace/code")
from lib.gilbreath import diff_block

A  = [0, 4, 0]
Ap = diff_block(A)
parent = [4, 4, 8]
print("A        =", A, "  diff =", Ap)
print("parent   =", parent, "  diff(parent) =", diff_block(parent), "== A:", diff_block(parent)==A)

# defects
def defect(row): return [max(0,x-2) for x in row]
dA, dAp = defect(A), defect(Ap)
print("defect(A)  =", dA, " -> P(A)  = 2*w2")
print("defect(A') =", dAp, " -> P(A') = 2*w1 + 2*w2")
print("P(A')-P(A) = 2w1 ; non-increase requires w1<=0, contradicts w1>0")
