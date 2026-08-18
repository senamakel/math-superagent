"""Small exact refuter for decimal/floor-sum indexing and slope stability.

The bounded loops are oracle-only: k<=80 and small rational slopes.  The
proposed full method must not use this enumeration.
"""
from fractions import Fraction
from lib.ueuclid import M, ue0
from mech.mech_psi import mech_psi, slope_for


def direct_moment(p, q, r, n, z):
    vals = [(p*i+q)//r for i in range(n)]
    return tuple(sum(pow(z, i, M)*v**h for i, v in enumerate(vals)) % M
                 for h in (0, 1, 2))


def test_ue0():
    for p in range(1, 20):
        for q in range(0, 20):
            for r in range(1, 20):
                for n in range(0, 25):
                    z = 10
                    got = ue0(p,q,r,n,z)
                    want = direct_moment(p,q,r,n,z)
                    du = 0 if n == 0 else (p*(n-1)+q)//r
                    if (got.S0, got.S1, got.S2, got.dU) != (*want, du):
                        return (p,q,r,n,got,want,du)
    return None


def words_from_fraction(k, p, q, variant="correct"):
    a = Fraction(p,q)
    pts = sorted((Fraction(-m*p,q)) % 1 for m in range(k+1))
    out=[]
    for i, lo in enumerate(pts):
        hi=pts[(i+1)%(k+1)] + (1 if i==k else 0)
        x=(lo+hi)/2
        f=[(x+j*a).numerator//(x+j*a).denominator for j in range(k+1)]
        if variant == "correct":
            v=sum((f[j+1]-f[j])*10**(k-1-j) for j in range(k))
        elif variant == "left-weight":
            v=sum((f[j+1]-f[j])*10**(k-j) for j in range(k))
        elif variant == "right-weight":
            v=sum((f[j+1]-f[j])*10**(k-2-j) for j in range(k))
        out.append(v)
    return sorted(out)


def main():
    print("ue0 exhaustive small grid:", test_ue0())
    if test_ue0() is not None:
        raise SystemExit(1)
    bad=[]
    for k in range(1,81):
        base=mech_psi(k)[0]
        for factor in (1,2,5,10):
            a,q,p=slope_for(k,factor)
            tA,tB,va,vb=mech_psi(k,q=q)
            if tA != base or tA != tB or va != vb:
                bad.append((k,factor,q,"approximant",base,tA,tB,va==vb))
                break
            if words_from_fraction(k,p,q) != va:
                bad.append((k,factor,q,"correct-index"))
                break
    print("slope/decimal checks k<=80:", "PASS" if not bad else bad[:1])
    # Deliberately wrong decimal exponent: find the smallest witness.
    witness=None
    for k in range(1,10):
        a,q,p=slope_for(k,1)
        good=words_from_fraction(k,p,q,"correct")
        wrong=words_from_fraction(k,p,q,"left-weight")
        if good != wrong:
            witness=(k,q,good,wrong)
            break
    print("smallest wrong decimal-weight witness:", witness)
    if bad:
        raise SystemExit(1)
