"""Refuter checker: compare finite rational mechanical approximants on small k.
Theory: Sturmian factor sets are slope-stable for sufficiently good convergents;
this checks the stated finite construction, not the full target evaluator.
"""
from fractions import Fraction
from mech.mech_psi import mech_psi

def direct(k, p, q):
    a=Fraction(p,q)
    pts=sorted((Fraction(-m*p,q)) % 1 for m in range(k+1))
    vals=[]
    for i,lo in enumerate(pts):
        hi=pts[(i+1)%(k+1)] + (1 if i==k else 0)
        x=(lo+hi)/2
        fl=[(x+j*a).numerator//(x+j*a).denominator for j in range(k+1)]
        vals.append(sum((fl[j+1]-fl[j])*10**(k-1-j) for j in range(k)))
    return sorted(vals)

def main():
    # convergents to 1/phi^2: F_n/F_{n+2}; include boundary near-equal cases
    F=[0,1]
    for _ in range(20): F.append(F[-1]+F[-2])
    fails=[]
    for k in range(1,51):
        reference=sorted(mech_psi(k,q=F[12])[2])
        for n in range(5,15):
            p,q=F[n],F[n+2]
            got=direct(k,p,q)
            if got != reference: fails.append((k,n,p,q))
    print('approximant comparisons:', 50*10, 'failures:',len(fails))
    if fails: print('first failure:',fails[0])
    # exact edge: q not greater than k can create duplicate orbit points; report it
    for k in range(1,8):
        p,q=1,2
        try:
            got=direct(k,p,q)
            print('boundary k',k,'q=2 distinct-values',len(set(got)),'count',len(got))
        except Exception as e: print('boundary exception',k,repr(e))
if __name__=='__main__': main()
