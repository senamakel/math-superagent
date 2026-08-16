"""Pin down the two genuine discrepancies (96, 98) between the published open
list (Castryck 2012, eq 6.5) and the m<=7 settled-family coverage, with the
6/7-family bad-prime data from the source (d=6 bad primes include p=2; d=7
smallest non-bad prime is 127).
"""
from sympy import factorint

# Published open (verbatim from castryck2012 eq 6.5): note 98 present, 96 absent.
published_open = [20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66,
                  70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100]

def pp(n):
    f = factorint(n)
    return (list(f)[0], f[list(f)[0]]) if len(f) == 1 else (None, None)

# bad-prime sets (from sources/held lists):
BAD3 = {2}
BAD4 = {3, 5, 7}
BAD5 = {2, 3, 7, 11, 131, 193, 599, 3541, 8009}
BAD6 = {2, 5, 7, 11, 13, 19, 23, 29, 37, 47, 61, 67, 73, 97, 257, 811, 983,
        1069, 1087, 1187, 1487, 1499, 1901, 2287, 3209, 3877, 3881, 4019,
        4943, 5471, 6983, 8699, 9337, 15131, 15823, 20771, 21379, 23993,
        150203, 266587, 547061, 685177, 885061, 1030951, 7783207, 17250187,
        40362599, 9348983563, 70016757407, 2610767527031, 225833117528659,
        7390044713023799, 51313000813080529}
# d=7: 366 bad primes; smallest non-bad (apart from 7) is 127 -> p=2,3 are bad
# for d=7 (2<127, 3<127, and 7 itself index prime).  From the run summary:
# "smallest non-bad prime (apart from p=7) is 127" means 2,3,5,11,... are bad.
BAD7_known_bad = {2, 3, 5, 11}  # sure subset; 7 is the degree's own prime

def cover(n, mfam):
    """Try to write n = m * p^k with m in mfam; return (m, p) or (None, None).""" 
    for m in mfam:
        if n % m == 0:
            q = n // m
            if len(factorint(q)) == 1:
                return m, list(factorint(q))[0]
    return None, None

for n in [96, 98]:
    print(f"=== n={n}  = {factorint(n)} ===")
    print(f"  published open? {n in published_open}")
    # m<=5
    for m in [1, 2, 3, 4, 5]:
        m_, p = cover(n, [m])
        if m_ is not None:
            excl = {1: set(), 2: set(), 3: BAD3, 4: BAD4, 5: BAD5}[m]
            ok = p not in excl
            print(f"  {n} = {m}*{p}^{factorint(n//m)[p]} : p={p} "
                  f"(bad for {m}? {p in excl}) -> covered={ok}")
    # m in {6,7}
    m_, p = cover(n, [6])
    if m_ is not None:
        print(f"  {n} = 6*{p}^{factorint(n//m_)[p]} : p={p} bad for 6? {p in BAD6} -> covered={p not in BAD6}")
    m_, p = cover(n, [7])
    if m_ is not None:
        print(f"  {n} = 7*{p}^{factorint(n//m_)[p]} : p={p} bad for 7? {p in BAD7_known_bad} -> covered={p not in BAD7_known_bad}")
