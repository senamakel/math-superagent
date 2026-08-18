"""PE1006: attack the OEIS A019587 match for d_j.

d_j = (S1(s_j+1) - S1(s_j)) / 10^{s_j} over V-runs j = 1..1145 (computed above).

OEIS A019587(j) = #{ i : 0 < i <= j and 0 < {phi*i} <= {phi*j} }, phi = golden ratio.

Conjecture under attack: d_j == A019587(j) for all j.

The first falsifying j would be the first j where they differ.  We compute
A019587(j) by its *exact* definition via high-precision Decimal comparison of
fractional parts {phi*i}.  Since phi is irrational and i <= 1145, the distance
from phi*i to the nearest integer is >= 1/(2*phi*1145 + 2) ~ 2.8e-4 — far larger
than the 60-digit precision error, so the fractional-part ordering is exact.

Verification over all 1145 terms, printing the first mismatch.
"""
from decimal import Decimal, getcontext

# load d_j
d = []
for line in open('code/out/dj_raw.txt'):
    j, val = line.split()
    d.append(int(val))
N = len(d)
print("loaded d_j count:", N)

getcontext().prec = 80
phi = (Decimal(1) + Decimal(5).sqrt()) / 2

def frac_cmp(i, j):
    """Return True if 0 < {phi*i} <= {phi*j}."""
    fi = (Decimal(i) * phi) % 1
    fj = (Decimal(j) * phi) % 1
    return fi > 0 and fi <= fj

def a019587(n):
    return sum(1 for i in range(1, n + 1) if frac_cmp(i, n))

firstbad = None
for j in range(1, N + 1):
    aj = a019587(j)
    if aj != d[j - 1]:
        firstbad = (j, d[j - 1], aj)
        break

print("d_j == A019587(j) for j = 1..%d:" % N, "VERIFIED (no mismatch)" if firstbad is None else "MISMATCH " + str(firstbad))

# also verify the complement relation a(n)+A194733(n)=n quickly? skip; just report count
