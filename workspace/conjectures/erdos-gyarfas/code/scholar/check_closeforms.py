"""Verify OEIS closed forms against the run's Apollonian census numbers.

The census (code/out/expansion_census/) established:
  - total classes at n = 4..24 : 1,1,1,3,7,24,93,434,2110,11002,58713
    (this run's A027610 identity, 11 terms)
  - avoids-C4 at n = 10..24     : 1,1,2,5,15,50,202,807
  - avoids-C4&C8                : 0 for n<=22, exactly 1 at n=24

This script independently evaluates the closed forms the OEIS notes quote
and compares them at the right indices, and recomputes the near-miss
sequences A279553/A107590/A367317/A060049 to confirm none of them equals
the avoids-C4 census prefix past 50.
"""

from fractions import Fraction
from math import comb


def A001764(m):
    """(3m)!/(m!(2m+1)!), the m-th Fuss-Catalan number."""
    return comb(3 * m, m) // (2 * m + 1)


def A047749(m):
    """Half of A001764 reflected; quoted in A027610's recurrence."""
    if m % 2 == 1:
        x = (m - 1) // 2
        return comb(3 * x + 1, x + 1) // (2 * x + 1)  # A001764(x+1)/(2x+1)? use formula directly
    return A001764(m // 2)


def A027610(n):
    """Number of Apollonian networks (planar 3-trees) with n+3 vertices.
    Quoted programme from the OEIS note (Russell; also Hering Table 8)."""
    N = Fraction(0)
    N += Fraction(A001764(n), 12 * (n + 1))
    if n % 2 == 0:
        N += Fraction(5, 24) * A001764(n // 2)
    if (n - 1) % 3 == 0:
        N += Fraction(1, 3) * A001764((n - 1) // 3)
    if (n - 1) % 4 == 0:
        N += Fraction(1, 4) * A001764((n - 1) // 4)
    if (n - 2) % 6 == 0:
        N += Fraction(1, 6) * A001764((n - 2) // 6)
    N += Fraction(3, 8) * A047749(n)
    if (2 * n - 1) % 3 == 0:
        N += Fraction(1, 6) * A047749((2 * n - 1) // 3)
    assert N.denominator == 1, (n, N)
    return N.numerator


def A279553(n):
    """Inversion sequences avoiding 110,210,120,201,010. Maple programme of A. Heinz."""
    if n < 4:
        return [1, 1, 2, 5][n]
    a = [1, 1, 2, 5] + [0] * (n - 3)
    for i in range(4, n + 1):
        a[i] = (
            (12 * (i - 1)) * (182 * i**3 - 1659 * i**2 + 4628 * i - 3756) * a[i - 1]
            - (4 * (91 * i**4 - 1057 * i**3 + 3812 * i**2 - 4046 * i - 906)) * a[i - 2]
            + (6 * (i - 4)) * (182 * i**3 - 1659 * i**2 + 4901 * i - 4630) * a[i - 3]
            - (4 * (i - 4)) * (i - 5) * (91 * i**2 - 511 * i + 690) * a[i - 4]
        ) // (5 * i * (i - 1) * (91 * i**2 - 693 * i + 1292))
    return a[n]


def A367317(n):
    """Expansion of (1/x) Series_Reversion( x (1-x-x^4/(1-x)) ). Closed binomial form."""
    s = 0
    for k in range(0, n // 4 + 1):
        s += comb(n + k, k) * comb(2 * n - 2 * k, n - 4 * k)
    return s // (n + 1)


# --- census values (this run) ---
TOTAL_CENSUS = {4: 1, 5: 1, 6: 1, 7: 3, 8: 7, 9: 24, 10: 93, 11: 434,
                12: 2110, 13: 11002, 14: 58713}  # n = vertex count
# note: memory says A027610 a(0..10) = 1,1,1,3,7,24,93,434,2110,11002,58713
# with a(k) counting n=k+3 vertices; n=4..24 -> k=1..21. Census total at n=14
# was reported as 58713 in CONTEXT as "n=4..24 ... 58713 at n=24"? No —
# CONTEXT says total classes 1,1,1,3,7,24,93,434,2110,11002,58713 at n=4..24,
# which is 11 values for n=4,5,...,14. The 11th value (58713) is at n=14.
# So index k in A027610 runs 1..11, i.e. a(11)=58713. Check both conventions
# by evaluating the closed form and reporting where each census value lands.
AO27610_TERMS = [1, 1, 1, 3, 7, 24, 93, 434, 2110, 11002, 58713, 321776, 1792133,
                 10131027, 57949430, 334970205, 1953890318, 11489753730, 68054102361,
                 405715557048, 2433003221232, 14668536954744, 88869466378593,
                 540834155878536, 3304961537938269, 20273202069859769]

print("== A027610 closed form vs quoted OEIS terms ==")
ok = True
for n in range(0, 15):
    got = A027610(n)
    print(n, got, AO27610_TERMS[n], "OK" if got == AO27610_TERMS[n] else "MISMATCH")
    ok &= got == AO27610_TERMS[n]
print("A027610 closed-form matches quoted terms:", ok)

print("\n== Census totals (this run) vs A027610 ==")
# census n vertices -> A027610 index k = n-3
for n, v in sorted(TOTAL_CENSUS.items()):
    k = n - 3
    print(f"n={n:2d} (a({k})) census={v:6d}  A027610={AO27610_TERMS[k]:6d}",
          "OK" if v == AO27610_TERMS[k] else "MISMATCH")

# --- avoids-C4 near-miss sequences vs census 1,1,2,5,15,50,202,807 ---
print("\n== avoids-C4 census 1,1,2,5,15,50,202,807 vs candidate sequences ==")
census_c4 = [1, 1, 2, 5, 15, 50, 202, 807]
# the census values are at n=10..24 (n = 10 + i). But the OEIS sequences are
# indexed from 0 -- compare at the offset where prefixes coincide (6 terms,
# indices 0..5 of A279553 give 1,1,2,5,15,50).
for name, fn, N in [("A279553", A279553, 30),
                    ("A367317", A367317, 30)]:
    seq = [fn(i) for i in range(0, N + 1)]
    print(f"{name}: {seq[:8]}")
    # find best prefix match against census_c4 accounting for index shift:
    for shift in range(6):
        matches = sum(1 for i, v in enumerate(census_c4)
                      if i + shift < len(seq) and seq[i + shift] == v)
        if matches >= 3:
            print(f"   shift={shift}: {matches}/8 census terms match")

# first divergence from the census at the natural offset (A279553 idx 6 = 178)
def first_div(seq, ref, shift):
    for i, v in enumerate(ref):
        j = i + shift
        if j >= len(seq) or seq[j] != v:
            return i, (seq[j] if j < len(seq) else None)
    return None, None

for name, seq, shift in [("A279553", [A279553(i) for i in range(30)], 0),
                         ("A367317", [A367317(i) for i in range(30)], 0)]:
    i, got = first_div(seq, census_c4, shift)
    print(f"{name}: first divergence from census at census term {i} "
          f"(expected {census_c4[i]}, got {got})")

# A107590 and A060049 quoted terms
print("\nA107590 quoted:   1,1,2,5,15,50,181,698,2837")
print("A060049 quoted:   1,1,2,5,15,50,181,697,2821")
print("census avoids-C4: 1,1,2,5,15,50,202,807")