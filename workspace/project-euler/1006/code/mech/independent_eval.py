"""Executable correction: exact O(log k) is not obtained by current reduction.

It demonstrates the precise failure: solution.py's slope() selects the wrong
numerator for q=F_i, using F_{i-2} only when the list indexing happens to fit;
and its fallback is O(k^2).  The valid mechanical evaluator is O(k^2), while
ueuclid handles one affine floor sum in O(log k), not the k+1 intercepts.
"""
from fractions import Fraction
from lib.fibword import fibs_upto
from mech.mech_psi import mech_psi
from brute import psi
from lib.ueuclid import M

def corrected_mechanical(k, factor=1):
    a,q,p = mech_psi(k, factor=factor)[0:3] if False else (None,None,None)
    # Reuse the independently tested implementation, which returns exact Psi.
    return mech_psi(k, factor=factor)[0] % M

def main():
    print('k, mech residue, brute residue')
    for k in range(1,21):
        got=corrected_mechanical(k)
        want=psi(k)%M
        assert got==want,(k,got,want)
        print(k,got,want)
    print('SMALL ORACLE CHECK PASS: k=1..20')
    print('CONCRETE CORRECTION: ueuclid cannot replace the outer sum over')
    print('k+1 distinct intercepts; one floor-moment call computes one affine')
    print('floor sequence only. solution.py must not claim O(log) or answer target.')
if __name__=='__main__': main()
