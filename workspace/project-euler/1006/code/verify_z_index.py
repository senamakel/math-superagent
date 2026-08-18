"""Small decisive indexing harness for the existing ueuclid primitive.

Claim checked: formulation-B floor moments use weight z^i (i=0..n-1),
therefore ue0, not the 1-indexed ueuclid call with an unchanged intercept.
This is an oracle-only bounded test; it deliberately stops at k=3.
"""
from lib.ueuclid import M, ue0, ueuclid_direct
from mech.mech_psi import mech_psi
from lib.fibword import fibs_upto
from fractions import Fraction


def slope(k):
    f = [0, 1]
    while f[-1] <= k:
        f.append(f[-1] + f[-2])
    q = f[-1]
    p = f[-3]
    return Fraction(p, q), p, q


def floor_sum_ue0(p, q, r, n, z):
    node = ue0(p, q, r, n, z)
    return node.S0, node.S1, node.S2


def direct0(p, q, r, n, z):
    vals = [((p*i+q)//r) for i in range(n)]
    w = [pow(z, i, M) for i in range(n)]
    return tuple(sum(w[i]*vals[i]**e for i in range(n)) % M
                 for e in (0, 1, 2))


def main():
    z = pow(10, -1, M)
    print("z =", z)
    for k in (1, 2, 3):
        a, p, q = slope(k)
        # B's ordinary floor terms are floor((p*i + qcut)/q), i=0..k.
        # Check every cut/intercept directly, then aggregate the actual v's.
        cuts = sorted(((-m*p) % q) for m in range(k+1))
        got = []
        expected = []
        for m in range(k+1):
            qq = (-m*p) % q
            got.append(floor_sum_ue0(p, qq, q, k+1, z))
            expected.append(direct0(p, qq, q, k+1, z))
        print(f"k={k}: all ue0 moments =", got == expected)
        if got != expected:
            raise AssertionError((k, got, expected))
        tA, tB, valsA, valsB = mech_psi(k)
        print(f"k={k}: mech A=B={tA}, values={valsA}")
        assert tA == tB
    print("INDEXING HARNESS PASSED: k=1,2,3; ue0 weights z^0..z^k.")

if __name__ == '__main__':
    main()
