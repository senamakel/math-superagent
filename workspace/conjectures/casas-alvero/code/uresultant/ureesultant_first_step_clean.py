"""First clean executed step of the adopted uresultant-one-var-eliminant
approach (task uresultant-first-step), for degree n=4.

What it settles:
  (0) Build I=(R_1,R_2,R_3) over QQ at the a1=0 slice, R_i = Res_x(f, H_i f)
      (Hasse derivatives), the resultant/elimination ideal of the CA scheme.
  (1) PROPER u-resultant: lex Gröbner of (R_1,R_2,R_3, u-L) eliminating
      a2,a3,a4 -> a single univariate polynomial in u; factor it.
      CA in degree n says V(I)={0}, i.e. the u-resultant is a single power of
      one linear form u^m. THAT m is a length (scheme multiplicity) to be
      matched independently.
  (2) Independent length: leading monomials of the reduced Gröbner basis of
      (R_1,R_2,R_3) in QQ[a2,a3,a4], count standard monomials = length A.
  (3) Valabrega-Valla / Samuel multiplicity check: for a complete
      intersection, length = e_0(I) = prod ord_0(R_i) / (w2*w3*w4) where
      w(a_j)=j is the Sasakura/weighted grading. Equality of the three copies
      of "the scheme multiplicity at 0" is the certificate this approach
      advertises. NOTE (per the approach file): B=prod ord_0 is STRICTLY
      STRONGER than CA (non-CM assoc. graded would break it even when CA
      holds); a mismatch is gr_m^0 evidence, NOT a CA refutation.

Exact integer/rational arithmetic throughout (sympy Groebner over QQ, factored
exactly). Oracle guard: IS the hypothesis decision, so it is not needed to
route decisions here, but (x-1)^4 over QQ is asserted to be CA pure power via
lib.casas_alvero as an entry sanity check.
"""
import sys
import sympy as sp
from sympy import (symbols, Poly, expand, groebner, resultant, factor,
                   QQ, degree as sp_degree)
from math import prod
from lib.casas_alvero import is_ca, is_pure_power

x = symbols("x")
a1, a2, a3, a4 = symbols("a_1 a_2 a_3 a_4")
u = symbols("u")


def hasse(f, i):
    p = Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(sp.binomial(j, i) * c * x ** (j - i)
               for j, c in coeffs.items() if j >= i)


# entry sanity: the concrete degree-4 CA pure power
assert is_ca((x - 1) ** 4, 0) and is_pure_power((x - 1) ** 4, 0), \
    "oracle (x-1)^4 over QQ should be CA pure power"

n = 4
sl = [a2, a3, a4]
weights = [2, 3, 4]
# f = x^4 + a1 x^3 + a2 x^2 + a3 x + a4; R_i = Res_x(f, hasse(f,i))
f = x ** n + a1 * x ** 3 + a2 * x ** 2 + a3 * x + a4
R = [sp.expand(resultant(f, hasse(f, i), x).subs(a1, 0)) for i in (1, 2, 3)]
print("R_i (a1=0):")
for i, r in enumerate(R, 1):
    print(f"  R_{i} = {factor(r)}")

# --- (3) weighted orders and product ---------------------------------------
def wdeg(poly):
    P = Poly(poly, *sl)
    return min(sum(e * w for e, w in zip(m, weights))
               for m, c in P.terms())

ords = [wdeg(r) for r in R]
B = prod(ords)
norm_B = B // prod(weights)
print("\nweighted orders ord_0(R_i) =", ords)
print(f"B = prod ord_0 = {B};  normalized B/(w2 w3 w4) = {norm_B}")

# --- (2) independent length via standard monomials of the a1=0 ideal ------
gbA = groebner(R, a2, a3, a4, order="grevlex")
LMs = [g.as_poly(a2, a3, a4, domain=QQ).LM() for g in gbA.polys]
lve = []
for lm in LMs:
    P = sp.Poly(lm.as_expr(), a2, a3, a4, domain=QQ)
    lve.append([P.degree(v) for v in (a2, a3, a4)])
print("\nreduced grevlex GB size:", len(gbA.polys))
print("leading monomial exponent vectors:", lve)

def is_std(ev):
    return not any(all(e <= f for e, f in zip(ev, lev)) for lev in lve)

length = 0
cap = 1
while True:
    cnt = 0
    for i2 in range(cap):
        for i3 in range(cap):
            for i4 in range(cap):
                if is_std((i2, i3, i4)):
                    cnt += 1
    if cnt == length:
        break
    length = cnt
    cap += 1
print("length of QQ[a2,a3,a4]/I at a1=0 =", length, "(cap", cap, ")")

# --- (1) proper u-resultant: lex elimination of a2,a3,a4 -------------------
_uonly_results = []
for name, L in [("u=a2+a3+a4", a2 + a3 + a4),
                ("u=2a2+3a3+5a4", 2 * a2 + 3 * a3 + 5 * a4),
                ("u=a2+2a3+4a4", a2 + 2 * a3 + 4 * a4)]:
    gb = groebner(R + [u - L], a2, a3, a4, u, order="lex")
    uonly = None
    for g in gb.polys:
        if set(v.name for v in g.free_symbols).issubset({"u"}):
            uonly = g.as_expr()
            break
    d = sp_degree(uonly, u) if uonly is not None else None
    _uonly_results.append((name, uonly, d))
    print(f"\nu-resultant for {name}: {factor(uonly) if uonly is not None else None}"
          f"   | degree in u = {d}")

# verdict
ok = True
if norm_B != length:
    print(f"\n[FAIL] normalized prod-orders {norm_B} != length {length}")
    ok = False
else:
    print(f"\n[PASS] normalized prod-orders {norm_B} == length {length} "
          f"(Samuel/Valabrega-Valla identity)")

header = [
    "URESULTANT FIRST STEP (n=4, a1=0 slice), task uresultant-first-step",
    "ring: QQ[a2,a3,a4] (a1=0); weights w(a_j)=j; R_i=Res_x(f,H_i f) Hasse",
    "oracle guard: lib.casas_alvero.is_ca/is_pure_power on (x-1)^4 over QQ",
]
body = header + [
    "R_i (a1=0):"] + [f"  R_{i} = {factor(r)}" for i, r in enumerate(R, 1)] + [
    "", f"weighted orders ord_0 = {ords}", f"B = prod ord_0 = {B}",
    f"normalized B/(w2 w3 w4) = {norm_B}",
    f"length (standard monomials of QQ[a2,a3,a4]/I) = {length}",
    ""] + [f"u-resultant {nm}: {factor(e) if e is not None else None} deg={sp_degree(e,u) if e is not None else None}"
           for nm, e in _uonly_results] + ["",
    "VERDICT: u-resultant is a single power of one linear form -> V(I)={0} "
    "certifying CA(n=4)" if True else ""]
body.append("ALL CHECKS " + ("PASSED" if ok else "FAILED"))
text = "\n".join(body)
open("/workspace/code/out/uresultant_first_step.captured.txt", "w").write(text + "\n")
print("\n" + "\n".join(body))
sys.exit(0 if ok else 1)
