"""Independent check of the new k2=6 entries by Sage's own genus routine
(Curve.genus), the second engine that agreed on the original grid.
Checks n=13,16,18 (residues 1,4,0 mod 6) against Singular's values
30,37,40."""
import time
import math

def CB(k):
    poly = [0.0] * (k + 1)
    # build prod_{i=0}^{k-1} (z - i) exactly as a list of ints
    coeffs = [1]
    for i in range(k):
        new = [0] * (len(coeffs) + 1)
        for d, c in enumerate(coeffs):
            new[d + 1] += c
            new[d] += -i * c
        coeffs = new
    fac = math.factorial(k)
    return [c // fac for c in coeffs]

for n, expected in [(13, 30), (16, 37), (18, 40)]:
    t0 = time.time()
    R = PolynomialRing(QQ, 'x,y')
    x, y = R.gens()
    c6 = CB(6)
    cn = CB(n)
    F = sum(c6[d] * x**d for d in range(len(c6))) - sum(cn[d] * y**d for d in range(len(cn)))
    C = Curve(F)
    g = C.genus()
    print(f"k2=6 n={n}: sage genus={g} (singular said {expected}) "
          f"{'MATCH' if g == expected else 'MISMATCH'}  {time.time()-t0:.1f}s")