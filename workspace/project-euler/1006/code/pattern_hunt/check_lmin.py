"""Check the regularity: minimal prefix length Lmin(k) of the infinite
Fibonacci word that contains all k+1 distinct length-k factors, versus the
closed form floor(k * phi^2) = floor(k * (phi+1)).

Using floating phi even for exact floor could be off by one for large k, so all
integer checks use sqrt5 = isqrt(5 k^2) style exact bounds or the integer
identity floor(phi^2 k) = floor(phi k) + k, with floor(phi k) computed exactly
via isqrt(5 k^2):
    floor(phi k) = floor( k * sqrt(5) / 2 + k/2 )        (phi = (1+sqrt5)/2)
                = (k + floor(k sqrt5))/2   when k sqrt5 has frac < 1 (always even? no)
    Safest: floor(phi k) = floor((k + k*sqrt5)/2); since sqrt5 irrational,
    (k + k sqrt5)/2 is never an integer for k>0, so floor = floor((k + isqrt(5 k^2))/2)
    is exact (isqrt(5 k^2) differs from k sqrt5 by < 1, and the fractional part
    of k sqrt5 is never 0, so the integer part is isqrt; then floor((k + (k sqrt5))/2)
    = floor((k + isqrt(5 k^2))/2) because the leftover (k sqrt5 - isqrt) < 1 and
    (k sqrt5 + k)/2 is not an integer, hence its floor equals that of (k + isqrt)/2).

We compare Lmin(k) == floor(phi^2 k) for every k <= 1000.  Lmin is recomputed
from a long prefix (length >= 3.5 k + 40).
"""

from math import isqrt

phi2_floor = [0, 2, 4, 7, 8, 12, 13, 14, 20, 21, 22, 23, 24, 33, 34, 35, 36,
              37, 38, 39, 40, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
              66, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
              102, 103, 104, 105, 106, 107, 108, 143, 144, 145, 146, 147, 148,
              149]


def floor_phi(k):
    """floor(k * phi) exactly, phi = (1+sqrt(5))/2."""
    return (k + isqrt(5 * k * k)) // 2


def floor_phi2(k):
    """floor(k * phi^2) = floor(k * phi) + k (phi^2 = phi + 1)."""
    return floor_phi(k) + k


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def lmin_seq(word, kmax):
    out = []
    W = word
    n = len(W)
    for k in range(1, kmax + 1):
        s = set()
        found = None
        for i in range(n - k + 1):
            s.add(W[i:i + k])
            if len(s) == k + 1:
                found = i + k
                break
        out.append(found)
    return out


def main():
    # Build one long prefix for all k.
    KMAX = 1000
    L = 4 * KMAX + 60
    W = fib_prefix(L)
    print(f"prefix length {len(W)}")
    lm = lmin_seq(W, KMAX)

    mism = []
    for k in range(1, KMAX + 1):
        want = floor_phi2(k)
        if lm[k - 1] != want:
            mism.append((k, lm[k - 1], want))
    print("mismatches Lmin vs floor(phi^2 k):", len(mism))
    print("first 10 mismatches:", mism[:10])

    # also compare against A344953's first 58 terms (note filed) through k=58
    a344 = phi2_floor[1:]  # indexed by k = note position
    ok28 = all(lm[k - 1] == a344[k - 1] for k in range(1, 29))
    print("matches A344953 note terms through k=28:", ok28)

    # print some Lmin values around the Fibonacci block boundaries
    for k in [1, 2, 3, 4, 5, 7, 8, 12, 13, 20, 21, 33, 34, 54, 55, 88, 89,
              100, 143, 144, 232, 233, 376, 377, 610, 987]:
        print(f"k={k:4d} Lmin={lm[k-1]:4d} phi^2*k floor={floor_phi2(k):4d}")


if __name__ == '__main__':
    main()