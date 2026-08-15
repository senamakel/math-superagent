#!/usr/bin/env python3
"""Verify the constant-c_r closed form for the P=2^m+1 family.

Conjecture: for odd period P=2^m+1 (m>=1), nu2 is per-residue affine mod
L = 2^(2m)-1 = 2^ord2(P)-1 (ord2(P)=2m), with CONSTANT c_r across all residues
and c_r = 3^m - 1.  Density = (3^m-1)/(2^(2m)-1).

Check c_r constant and == 3^m - 1 for P=5,9,17,33 (and 65 if affordable).
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
from fractions import Fraction

def build_seq(word, n_terms):
    q=[2,3]; per=len(word)
    while len(q)<n_terms:
        bit=word[(len(q)-2)%per]; q.append(q[-1]+(2 if bit else 4))
    return q[:n_terms]

def nu2_map(word, nmax):
    q=build_seq(word,nmax+1); out={}
    for k,dd in enumerate(incremental_diagonals(q)):
        if k>=2: out[k]=cycle_and_nu2(dd)[1]
    return out

def affine_cr(vals,L,nmin,nmax):
    seen={}
    for n in range(nmin,nmax-L+1):
        d=vals[n+L]-vals[n]; r=n%L
        if r in seen and seen[r]!=d: return None
        seen[r]=d
    return seen

def main():
    print("P=2^m+1 family: c_r constant and == 3^m-1?  modulus L=2^(2m)-1")
    print("="*72)
    for m in [2,3,4,5]:
        P=2**m+1; L=2**(2*m)-1
        nmax=min(L*3+300,30000); nmin=L+100
        vals=nu2_map([0]*(P-1)+[1], nmax)
        cr=affine_cr(vals,L,nmin,nmax)
        if cr is None:
            print("P=%d (m=%d) L=%d NOT affine"%(P,m,L)); continue
        cvals=[cr[r] for r in range(L)]
        mn,mx=min(cvals),max(cvals)
        target=3**m-1
        slope=Fraction(sum(cvals),L*L)
        print("P=%2d (2^%d+1) L=%5d c_r const=%s min=%d max=%d target 3^%d-1=%d "
              "slope=%s"%(P,m,L,mn==mx,mn,mx,m,target,slope))

if __name__=="__main__": main()
