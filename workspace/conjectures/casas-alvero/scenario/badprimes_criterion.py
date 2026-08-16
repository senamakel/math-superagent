"""Bad primes by the sufficient criterion p | C(d,i)-1 (Schaub-Spivakovsky
`bad-prime-criterion`): if p is prime and p divides (d choose i) - 1 for some
1<=i<=d-1, then CA_{d,p} is FALSE (p is bad for degree d).

Compute this for d up to 8.  For d<=7 compare against the published bad-prime
lists to calibrate how informative (lower-bound) the criterion is.  For d=8
this gives an exact partial list of bad primes.
"""
from sympy import binomial, factorint, primerange

def criterion_bad_primes(d):
    bad = set()
    for i in range(1, d):
        v = binomial(d, i) - 1
        for p in factorint(v):
            bad.add(p)
    return sorted(bad)

published = {
    3: [2],
    4: [3, 5, 7],
    5: [2, 3, 7, 11, 131, 193, 599, 3541, 8009],
    6: [2,5,7,11,13,19,23,29,37,47,61,67,73,97,257,811,983,1069,1087,1187,
        1487,1499,1901,2287,3209,3877,3881,4019,4943,5471,6983,8699,9337,
        15131,15823,20771,21379,23993,150203,266587,547061,685177,885061,
        1030951,7783207,17250187,40362599,9348983563,70016757407,
        2610767527031,225833117528659,7390044713023799,51313000813080529],
}
# d=7: 366 bad primes, we only know the count and extremes (smallest non-bad
#       apart from 7 is 127; largest is a 135-digit number) - not the full list.

print("d | #criterion | criterion primes (subset of true bad primes)")
for d in range(3, 9):
    crit = criterion_bad_primes(d)
    print(f"{d} | {len(crit):2d} | {crit}")

print("\nCalibration against published lists (d<=6):")
for d in [3, 4, 5, 6]:
    crit = set(criterion_bad_primes(d))
    pub = set(published[d])
    print(f"  d={d}: criterion={sorted(crit)}; "
          f"published has {len(pub)} bad primes; "
          f"criterion subset of published? {crit <= pub}; "
          f"captured {len(crit & pub)}/{len(pub)}")
