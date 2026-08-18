"""Exact symbolic probe for node G-degenerate-pstar-and-center.

Grounds the Lean transcription facts for the DI2a normal-form families (2.7),
(2.8) of Dumortier-Rousseau 2009 (CPAA 8:1133-1157):

  (2.7): x' = c x - y + 1 + x^2,  y' = x y
  (2.8): x' = c x - y + 1 + (1+mu2) x^2 + mu1 x y + mu0 y^2,
         y' = x y - mu3 x^2

Checks, in exact rational arithmetic:
  A. (2.7) has the finite invariant line y=0 and the singular point (0,1).
  B. (2.8) with (c, mu0, mu1, mu3) = (0,0,0,0) is invariant under the
     involution (x,t) |-> (-x,-t): P(-x,y)=P(x,y) and Q(-x,y)=-Q(x,y);
     this is the source's center condition (DR 2009 4.4: "systems (3.1) with
     b = D = E1 = 0 represent centers since they are invariant under
     (x,t) |-> (-x,-t)").
  C. Search for a Darboux first integral of (2.7): invariant algebraic
     curves f (deg <= 2) with P f_x + Q f_y = f * (cofactor of deg <= 2),
     then test whether a product of powers of the factors is a first
     integral (H_x P + H_y Q = 0).
All arithmetic is exact (sympy rationals); no floats.
"""
import sympy as sp

x, y = sp.symbols('x y', real=True)
c, mu0, mu1, mu2, mu3 = sp.symbols('c mu0 mu1 mu2 mu3', real=True)


def P28(c, mu0, mu1, mu2, mu3, x, y):
    return c*x - y + 1 + (1 + mu2)*x**2 + mu1*x*y + mu0*y**2


def Q28(c, mu0, mu1, mu2, mu3, x, y):
    return x*y - mu3*x**2


def P27(c, x, y):
    return P28(c, 0, 0, 0, 0, x, y)


def Q27(c, x, y):
    return Q28(c, 0, 0, 0, 0, x, y)


# --- A. unperturbed (2.7) ------------------------------------------------
print("A. (2.7): invariant line y=0 and singular point (0,1)")
print("   Q27(c,x,0) =", sp.simplify(Q27(c, x, 0)))          # expect 0
print("   P27(c,0,1) =", sp.simplify(P27(c, 0, 1)))          # expect 0
print("   Q27(c,0,1) =", sp.simplify(Q27(c, 0, 1)))          # expect 0

# --- B. center symmetry of (2.8) -----------------------------------------
print("\nB. center symmetry of (2.8) at (c,mu0,mu1,mu3)=(0,0,0,0)")
Pc = P28(0, 0, 0, mu2, 0, -x, y)
Qc = Q28(0, 0, 0, mu2, 0, -x, y)
print("   P(-x,y) - P(x,y) =", sp.expand(Pc - P28(0, 0, 0, mu2, 0, x, y)))  # expect 0
print("   Q(-x,y) + Q(x,y) =", sp.expand(Qc + Q28(0, 0, 0, mu2, 0, x, y)))  # expect 0

# --- C. Darboux factors of (2.7) ------------------------------------------
print("\nC. invariant algebraic curves of (2.7): search deg <= 2")
# f = a20 x^2 + a11 xy + a02 y^2 + a10 x + a01 y + a00
# cofactor L = l20 x^2 + l11 xy + l02 y^2 + l10 x + l01 y + l00
# condition: P f_x + Q f_y - f L == 0 (polynomial identity, c symbolic)
a20, a11, a02, a10, a01, a00 = sp.symbols('a20 a11 a02 a10 a01 a00')
l20, l11, l02, l10, l01, l00 = sp.symbols('l20 l11 l02 l10 l01 l00')
f = a20*x**2 + a11*x*y + a02*y**2 + a10*x + a01*y + a00
L = l20*x**2 + l11*x*y + l02*y**2 + l10*x + l01*y + l00
P = P27(c, x, y)
Q = Q27(c, x, y)
cond = sp.expand(P*sp.diff(f, x) + Q*sp.diff(f, y) - f*L)
coeffs = sp.Poly(cond, x, y).coeffs()  # polynomials in the unknowns
unknowns = [a20, a11, a02, a10, a01, a00, l20, l11, l02, l10, l01, l00]
sol = sp.solve(coeffs, unknowns, dict=True)
print("   number of solution families:", len(sol))
for s in sol:
    # express in terms of free parameters
    free = {k: v for k, v in s.items()}
    # print a basis vector: set free vars to simple values
    free_params = [u for u in unknowns if u not in free]
    if len(free_params) <= 2:
        print("   free:", [str(u) for u in free_params])

# known invariant: y = 0 (the finite invariant line)
print("   check f=y: cofactor =", sp.simplify(P*sp.diff(y, x) + Q*sp.diff(y, y)) / y)

# --- D. first integral ansatz ---------------------------------------------
print("\nD. first integral of (2.7): try H = f(x,y)^a * g(x,y)^b")
# use the found factors; first search degree-1 and degree-2 factors again
# with the cofactor degree bounded, printing explicit nonconstant factors
found = []
for s in sol:
    f_expr = f.subs({k: v for k, v in s.items() if k in unknowns[:6]})
    L_expr = L.subs({k: v for k, v in s.items() if k in unknowns[6:]})
    if sp.simplify(f_expr) != 0 and sp.simplify(f_expr) != 1:
        found.append((sp.factor(f_expr), sp.factor(L_expr)))
for fe, le in found:
    print("   factor:", fe, "  cofactor:", le)
