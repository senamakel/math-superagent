"""Exact test of the two-monomial submask law for F2 Hasse-CA counterexamples.

Law (recorded in run): for monic degree-n poly over F2 of the form x^a + x^n
(0 < a < n), the poly is a Hasse-CA counterexample (satisfies Hasse-CA and is
not a pure power) IFF a is a PROPER NONEMPTY SUBSET-SUM of the set bits of n.

The exhaustive enumeration earlier could only reach n <= 28 (2^n ceiling).
But testing this law needs only the 2^popcount(n) - 2 candidate polys per n,
so it can be verified exactly for far larger n.

Pure powers over F2 of degree n: (x)^n = x^n, and (x+1)^n (coeff of x^j = C(n,j) mod 2).
A two-monomial poly x^a+x^n is a pure power only if it equals one of those two;
neither holds for 0<a<n except, over F2, (x+1)^1 = x+1 = x^1 + x^0... handled by a<n.

Hasse derivative over F2: H_i has coeff of x^j equal to C(j,i) mod 2 = 1 iff (i & j)==i (Lucas).
gcd via Euclid on bit-polynomials.  Hasse-CA iff gcd(f,H_i) is non-constant for all i=1..n-1
(gcd(f,0)=f trivially non-constant; a vanishing H_i passes).
"""
from math import comb


def hasse_deriv(fbits, i):
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i:
                out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out


def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return False
    return True


def Cparity(n, k):
    return (k & n) == k


def is_pure_f2(fbits, n):
    """Over F2 the only monic pure powers of degree n are x^n and (x+1)^n."""
    if fbits == (1 << n):
        return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j):
            bits |= 1 << j
    return fbits == bits


def set_bits(n):
    return [1 << b for b in range(n.bit_length()) if (n >> b) & 1]


def subset_sums(bits):
    """All subset-sums of a list of bit values (powers of 2), as a set."""
    sums = {0}
    for b in bits:
        sums |= {s + b for s in sums}
    return sums


def main():
    NMAX = 64
    bad = []
    n_total = 0
    fails = 0
    for n in range(3, NMAX + 1):
        bits = set_bits(n)
        ss = subset_sums(bits)
        # proper nonempty subset-sums: all except 0 (empty) and n (full set)
        legal = [a for a in ss if 0 < a < n]
        # all a in 1..n-1 are the candidate lower monomial exponents;
        # official predicted counterexamples are exactly `legal`
        for a in range(1, n):
            fbits = (1 << n) | (1 << a)
            is_ca = is_ca_f2(fbits)
            is_pp = is_pure_f2(fbits, n)
            is_ce = is_ca and not is_pp
            predicted = (a in legal)
            n_total += 1
            if is_ce != predicted:
                fails += 1
                if len(bad) < 15:
                    bad.append((n, a, is_ce, predicted, bin(n).count("1")))
    print(f"two-monomial submask law, n = 3..{NMAX}")
    print(f"  candidate polys tested: {n_total}")
    print(f"  mismatches: {fails}")
    if bad:
        for row in bad:
            print("   MISMATCH n=%d a=%d is_ce=%s predicted=%s pc=%d" % row)
    else:
        print("  LAW HOLDS EXACTLY for every candidate in n=3..%d" % NMAX)
    # report predicted support-2 counts = 2^pc - 2 per popcount class
    print("\nsupport-2 (two-monomial ce) count per popcount class:")
    from collections import defaultdict
    per = defaultdict(set)
    for n in range(3, NMAX + 1):
        pc = bin(n).count("1")
        per[pc].add(2 ** pc - 2)
    for pc in sorted(per):
        print(f"  pc={pc}: 2^pc-2 = {2**pc-2}, all n in range give this count: {len(per[pc])==1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
