"""Verify the degree of the fold cell as a Walsh character / multilinear polynomial.

Canonical floored fold cell:  T(n,d) = XOR_{o subseteq d} h[n-1-d+o].
In the {+-1} basis each h bit x_j = (-1)^{h[j]}, and the XOR over a set S of
positions is the parity character chi_S = prod_{j in S} x_j, whose degree as a
multilinear polynomial is |S|.

S_d = { n-1-d+o : o subseteq d }.  The submasks o of d are DISTINCT numbers
(0..2^{popcount(d)}-1 exhibit one representative per submask), so |S_d| =
2^{popcount(d)}.  The degree of the cell is therefore 2^{popcount(d)}:
the popcount of the INDEX d is the exponent, not the degree.

We count |S_d| for all n,d and report, against the "degree = popcount(d)" claim.
"""

def submasks(d):
    out = []
    o = d
    while True:
        out.append(o)
        if o == 0:
            break
        o = (o - 1) & d
    return out

def popcount(x):
    return bin(x).count("1")

bad = 0
for n in range(4, 16):
    for d in range(2, n):
        S = sorted(n - 1 - d + o for o in submasks(d))
        assert len(S) == len(set(S)), (n, d)  # positions distinct
        deg = len(S)
        expect_claimed = popcount(d)   # what the digest says
        expect_actual = 1 << popcount(d)
        if deg != expect_actual:
            bad += 1
            print("n=%d d=%d deg=%d != 2^popcount=%d" % (n, d, deg, expect_actual))
        if deg == expect_claimed:
            print("n=%d d=%d deg=%d EQUALS popcount (would validate digest)" % (n, d, deg))

print("cells checked; mismatches vs 2^popcount(d):", bad)
# Show the degree is a power of two and reaches ~n.
for n in [8, 16, 32]:
    degs = sorted({len(submasks(d)) for d in range(2, n)})
    print("n=%3d possible cell degrees (powers of two):" % n, degs)
print("MAX cell degree over d in [2,n-1] = 2^popcount(n-1) ~ up to size of the largest submask power <= n-1")
