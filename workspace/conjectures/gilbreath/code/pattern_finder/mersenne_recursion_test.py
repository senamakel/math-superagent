#!/usr/bin/env python3
"""Find the exact recursion of the Mersenne per-residue constants c_r/2 array.

Observed: P_k (length 2^k-1) has its second half equal to P_{k-1}, e.g.
P15[8:15] == P7, P31[16:31] == P15.  Test this and try to get the first-half
recursion.  This would give a complete closed form for the whole c_r structure.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2

def build_seq(word, n_terms):
    q=[2,3]; per=len(word)
    while len(q)<n_terms:
        bit=word[(len(q)-2)%per]; q.append(q[-1]+(2 if bit else 4))
    return q[:n_terms]

def nu2_seq(word,nmax):
    q=build_seq(word,nmax+1); out={}
    for k,dd in enumerate(incremental_diagonals(q)):
        if k>=2: out[k]=cycle_and_nu2(dd)[1]
    return out

def get_P(k):
    P=2**k-1; nmax=min(P*4+300,12000); nmin=P+150
    vals=nu2_seq([0]*(P-1)+[1],nmax)
    seen={}
    for n in range(nmin,nmax-P+1):
        d=vals[n+P]-vals[n]; r=n%P
        if r in seen and seen[r]!=d: raise RuntimeError(f"not affine k={k}")
        seen[r]=d
    return [seen[r]//2 for r in range(P)]

arrays={}
for k in range(2,11):
    arrays[k]=get_P(k)

# check second-half recursion P_k[2^(k-1):] == P_{k-1}
print("second-half recursion (P_k[2^(k-1):] == P_{k-1}):")
for k in range(3,11):
    P=2**k-1; half=2**(k-1)
    ok = arrays[k][half:]==arrays[k-1]
    print(f"  k={k}: {ok}")
    if not ok:
        print("   P_k tail:", arrays[k][half:])
        print("   P_{k-1}:", arrays[k-1])

# check first half relation to P_{k-1}: maybe first-half = 2*P_{k-1} with boundary?
print()
print("first half P_k[0:2^(k-1)] :")
for k in range(3,8):
    P=2**k-1; half=2**(k-1)
    print(f"  k={k} first half len {half}:", arrays[k][:half])
print("P_3:", arrays[3])
print("P_2:", arrays[2])
