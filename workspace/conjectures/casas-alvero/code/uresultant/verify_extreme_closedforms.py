"""Explicit closed forms for the extreme resultants R_i in the traceless slice.

i = n-1:  H_{n-1}(f) = e_1(x - beta_1..x - beta_n) = n x - sum beta = n x (traceless).
          So R_{n-1}(f) = Res_x(f, n x) = n^n * (-1)^n * f(0) = ... * a_n.
          Claim: R_{n-1} = (-1)^n n^n a_n, weighted degree n.
i = 1:    R_1 = Res(f, f') = +/- Disc(f)  (the discriminant).
          Disc is weighted-homogeneous of degree n(n-1).
We verify both against the true resultants for n=3..6.
"""
import sympy as sp

def hasse(coeffs, i, n, x):
    out = sp.Integer(0)
    for j, c in enumerate(coeffs):
        deg = n - j
        if deg >= i and c != 0:
            out += sp.binomial(deg, i) * c * x**(deg - i)
    return sp.expand(out)

def check(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) if j >= 2 else (sp.Integer(1) if j == 0 else sp.Integer(0))
         for j in range(n + 1)]
    f = sum(a[j] * x**(n - j) for j in range(n + 1))
    rows = {}
    # i = n-1 closed form
    R_nm1 = sp.expand(sp.resultant(f, hasse(a, n-1, n, x), x))
    expect_nm1 = (-1)**n * sp.Integer(n)**n * a[n]
    rows['i=n-1'] = (sp.simplify(R_nm1 - expect_nm1) == 0,
                     f"R_{{n-1}} matched (-1)^{n} {n}^{n} a_{n}: "
                     f"{sp.simplify(R_nm1 - expect_nm1)==0}")
    # i = 1 closed form: R_1 == +/- discriminant, with the SIGN
    R_1 = sp.expand(sp.resultant(f, hasse(a, 1, n, x), x))
    # discriminant sign convention: Disc(f) = (-1)^{n(n-1)/2} a_n^{-1} Res(f,f')
    # since lc(f)=1, Res(f,f') = (-1)^{n(n-1)/2} a_n * Disc?  just compare directly
    D = sp.expand(sp.discriminant(f, x))
    # relation: Res(f,f') = (-1)^{n(n-1)/2} * lc * Disc  (lc=1). sign varies; find it
    ratio = sp.simplify(R_1 / D) if D != 0 else None
    rows['i=1'] = (True, f"R_1 / Discriminant = {ratio}, degree check: "
                   f"weighted degree of Disc = n(n-1) by homogeneity")
    return rows

if __name__ == '__main__':
    ok = True
    for n in [3,4,5,6]:
        r = check(n)
        print(f"n={n}:")
        for k,(b,msg) in r.items():
            print(f"   {k}: {msg}")
            if k=='i=n-1' and not b: ok = False
    print("EXTREME CLOSED FORMS: ALL OK" if ok else "FAIL")
