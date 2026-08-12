import json, sympy as sp

m = sp.symbols('m')

# Established rational functions in m = L/40
P2 = m/(2*m-1)
P3 = (7*m**2-17*m+12)/(18*m**2-45*m+27)
P4 = (19*m**3-119*m**2+244*m-162)/(36*m**3-216*m**2+423*m-270)

funcs = {2:P2, 3:P3, 4:P4}

# exact data
p3 = json.load(open('code/out/exact_p3_extra.json'))
p4 = json.load(open('code/out/exact_p4_extra.json'))
# also known anchors
extra = {3:{**{int(L): v['p'] for L,v in p3.items()},
              160:'56/135',400:'542/1377',1800:'2237/5742'},
         4:{**{int(L): v['p'] for L,v in p4.items()},
              400:'521/1020',1800:'166802/317985'}}

for n in (3,4):
    P = funcs[n]
    bad=0; good=0
    for Lstr, frac in extra[n].items():
        L=int(Lstr)
        pred = sp.simplify(P.subs(m, sp.Rational(L,40)))
        want = sp.Rational(frac)
        if pred==want: good+=1
        else:
            bad+=1
            print(f"  n={n} L={L}: pred={pred} want={want}")
    print(f"n={n}: {good} match, {bad} mismatch")

print("\n=== Denominator factorization ===")
for n in (2,3,4):
    num, den = sp.fraction(sp.cancel(funcs[n]))
    print(f"n={n}: num={sp.expand(num)}")
    print(f"      den={sp.expand(den)} = {sp.factor(den)}")

# large-L limits
for n in (2,3,4):
    print(f"limit n={n}: {sp.limit(funcs[n], m, sp.oo)}")

# leading coefficient pairs
for n in (2,3,4):
    num,den = sp.fraction(sp.cancel(funcs[n]))
    print(f"n={n} leading (num,den): {(sp.Poly(num,m).LC(), sp.Poly(den,m).LC())}")
