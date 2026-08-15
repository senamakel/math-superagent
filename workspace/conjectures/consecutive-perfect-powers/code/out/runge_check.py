"""Verify the Runge-condition claims for y^q = x^p - 1 and the sharpness example.

Runge's condition (Walsh 1992, Acta Arith 62:2): the equation F=0 has finitely many
integer solutions via Runge's method iff at least one of C1-C4 FAILS. If all four hold,
the method is inapplicable (single conjugate Puiseux class at infinity).

For F = x^p - y^q - 1 with degrees m=p in x, n=q in y:
  (C1) a_{i,n}=0 and a_{m,j}=0 for all nonzero i,j
  (C2) a_{ij}=0 whenever n*i + m*j > n*m
  (C3) sum of monomials with n*i+m*j = n*m is a constant multiple of a power
       of an irreducible polynomial
  (C4) the algebraic function y(x) has only one conjugate Puiseux class

We check C1,C2,C3 for several (p,q). We also check the file's sharpness case:
integer solutions of x^2 - y^2 = 1 (claimed "infinitely many").
"""

from sympy import factor, symbols

x, y = symbols("x y")

def runge_condition(p, q):
    """Return dict of which of C1,C2,C3 hold. C4 (single conjugacy class)
    holds for gcd(p,q)=1 superelliptic since x^{p/q} generates Q(x^{1/q})."""
    m, n = p, q
    # only monomials present in F = x^p - y^q - 1
    terms = {(p,0): 1, (0,q): -1, (0,0): -1}
    # C1: coefficient of x^i y^q (i>0) and x^p y^j (j>0) are zero
    c1 = True
    for i in range(1, p+1):
        if terms.get((i,q), 0) != 0: c1 = False
    for j in range(1, q+1):
        if terms.get((p,j), 0) != 0: c1 = False
    # C2: no term with n*i+m*j > n*m
    c2 = True
    for (i,j),c in terms.items():
        if n*i + m*j > n*m: c2 = False
    # C3: restriction to the line n*i+m*j=n*m
    line_sum = 0
    for (i,j),c in terms.items():
        if n*i + m*j == n*m:
            line_sum += c * x**i * y**j
    # is line_sum a power of an irreducible (with constant multiple)?
    fac = factor(line_sum)
    # count how many distinct irreducible factors (squarefree)? check squarefree
    sq = line_sum
    import sympy
    c3 = True
    f = sympy.factor(line_sum)
    # f is "constant * product of irreducibles"; it is a power of a single
    # irreducible iff it has exactly one irreducible factor (up to constant)
    from sympy import Poly, gcd, diff
    # squarefree iff gcd(f, f') is a unit/constant
    g = gcd(line_sum, diff(line_sum, x))
    sqfree = g == 1 or (g.is_constant() and int(sympy.factor(line_sum).subs(x,0)) != 0)
    # number of distinct irreducible factors
    fac_dict = {}
    try:
        fac_dict = sympy.factor_list(line_sum)[1]
    except Exception:
        fac_dict = []
    c3 = len([k for k,_ in fac_dict]) <= 1
    return dict(C1=c1, C2=c2, C3=c3, C4=True,
                line_restriction=str(line_sum), factor=str(fac),
                n_irreducible_factors=len([k for k,_ in fac_dict if not k.is_number]))

print("=== Runge Determine for F = x^p - y^q - 1 ===")
for (p,q) in [(3,5),(5,3),(2,3),(3,2),(3,7),(5,7)]:
    r = runge_condition(p,q)
    all4 = all(r[k] for k in ["C1","C2","C3","C4"])
    r["all_four_hold"] = all4
    r["runge_applies"] = not all4
    print(f"p={p}, q={q}: {r}")

print()
print("=== Sharpness case: integer solutions of x^2 - y^2 = 1 ===")
sols = []
for X in range(-20,21):
    for Y in range(-20,21):
        if X*X - Y*Y == 1:
            sols.append((X,Y))
print("integer solutions x^2-y^2=1:", sols)
print("count:", len(sols))

print()
print("=== Contrast: Pell x^2 - D y^2 = 1, D=2 (the actual infinite case) ===")
sols2 = []
for X in range(0,20):
    for Y in range(0,20):
        if X*X - 2*Y*Y == 1:
            sols2.append((X,Y))
print("small solutions x^2-2y^2=1:", sols2, "(known to be infinite)")
