import sympy as sp
m = sp.symbols('m')
funcs = {
 2: m/(2*m-1),
 3: (7*m**2-17*m+12)/(18*m**2-45*m+27),
 4: (19*m**3-119*m**2+244*m-162)/(36*m**3-216*m**2+423*m-270),
}
print("Pole sets (m where denominator=0):")
for n in (2,3,4):
    _,den=sp.fraction(sp.cancel(funcs[n]))
    print(f"  n={n}: roots={[complex(r) for r in sp.solve(den,m)]}")

print("\nLimit values as fractions:", [sp.limit(funcs[n],m,sp.oo) for n in (2,3,4)])
print("Largest pole for each n: ", [max(abs(complex(r)) for r in sp.solve(sp.fraction(sp.cancel(funcs[n]))[1],m)) for n in (2,3,4)])
print("\nfixed m=45 evaluation:")
for n in (2,3,4):
    print(f"  p({n},1800) = {sp.nsimplify(sp.cancel(funcs[n].subs(m,45)))} =", float(sp.cancel(funcs[n].subs(m,45))))
print("Known actuals: p(2,1800)=45/89, p(3,1800)=2237/5742, p(4,1800)=166802/317985")
