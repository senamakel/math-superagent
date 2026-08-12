import sympy as sp

m = sp.symbols('m')
funcs = {
 2: m/(2*m-1),
 3: (7*m**2-17*m+12)/(18*m**2-45*m+27),
 4: (19*m**3-119*m**2+244*m-162)/(36*m**3-216*m**2+423*m-270),
}

print("Leading (limit) pairs num,den per n:")
lnum=[]; lden=[]
for n in (2,3,4):
    num,den = sp.fraction(sp.cancel(funcs[n]))
    ln = sp.Poly(num,m).LC(); ld = sp.Poly(den,m).LC()
    lnum.append(ln); lden.append(ld)
    print(n, ln, ld, sp.Rational(ln,ld))

print("leading numerators:", lnum, " leading denominators:", lden)

# coefficient sequences of numerator (degree n-1), list from highest to lowest
print("\nNumerator coeffs (high->low):")
for n in (2,3,4):
    num,_=sp.fraction(sp.cancel(funcs[n]))
    print(n, [int(c) for c in sp.Poly(num,m).all_coeffs()])

print("\nDenominator coeffs (high->low):")
for n in (2,3,4):
    _,den=sp.fraction(sp.cancel(funcs[n]))
    print(n, [int(c) for c in sp.Poly(den,m).all_coeffs()])

# constant terms (evaluate at m=0, i.e. L=0) as potential sequence
print("\nConstant terms num/den (m=0):")
for n in (2,3,4):
    num,den=sp.fraction(sp.cancel(funcs[n]))
    print(n, sp.Poly(num,m).TC(), sp.Poly(den,m).TC())
