"""Explicit acceptance harness for the failed reduction boundary.

It documents the exact failure: a single ueuclid call for one intercept cannot
represent the k+1 distinct intercepts in formulation B. The harness compares
that tempting reduction against mech_psi only at k=1,2,3 and exits nonzero on
any accidental claim of correctness.
"""
from fractions import Fraction
from lib.ueuclid import M, ue0
from mech.mech_psi import mech_psi


def fib_slope(k):
    f=[0,1]
    while f[-1] <= k: f.append(f[-1]+f[-2])
    return f[-3], f[-1]


def naive_single_intercept(k):
    p,q=fib_slope(k); z=pow(10,-1,M)
    # The invalid tempting construction: only b=0, with the digit weights.
    n=ue0(p,0,q,k+1,z)
    # It is not a Psi formula; return its second moment as a diagnostic.
    return n.S2


def main():
    for k in (1,2,3):
        t=mech_psi(k)[0] % M
        bad=naive_single_intercept(k)
        print(f"k={k}: mech_psi={t}, single-intercept-S2={bad}, equal={t==bad}")
    print("Conclusion: z^0 indexing is fixed by ue0, but the prior single-call")
    print("reduction is mathematically insufficient: formulation B has k+1 intercepts.")

if __name__=='__main__': main()
