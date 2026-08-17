"""Singular-certified structure of the n=5 traceless-slice ideal.

Establish (trusted engine Singular, dp order):
  - KRULLDIM (must be 0: V(slice)={0}, as CA_5 requires)
  - the pure a3 (and a2) power in the GB leading monomials (nilpotency)
  - the quotient dimension (Samuel multiplicity) via the standard monomial
    count, using Singular's kbase / vdim.
This settles whether sympy's grevlex GB (which showed NO pure a3 power) was
incomplete -- a load-bearing fact for the mult-map u-resultant route.
"""
import subprocess, tempfile, os
from sympy import symbols, Poly, expand, resultant, binomial, sstr

x = symbols("x")
a1, a2, a3, a4, a5 = symbols("a_1 a_2 a_3 a_4 a_5")
a = [a1, a2, a3, a4, a5]


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


n = 5
f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
R = [expand(resultant(f, hasse(f, i), x).subs(a1, 0)) for i in range(1, n)]


def to_singular(e):
    return sstr(e).replace("a_2", "a2").replace("a_3", "a3") \
        .replace("a_4", "a4").replace("a_5", "a5")


script = f"""
ring R = 0, (a2,a3,a4,a5), dp;
ideal I = {", ".join(to_singular(r) for r in R)};
ideal G = std(I);
"GB_SIZE = " + string(size(G));
"KRULLDIM = " + string(dim(G));
"VDIM (multiplicity) = " + string(vdim(G));
// pure powers among leading monomials
int i; poly lm;
for (i=1; i<=size(G); i++) {{
  lm = lead(G[i]);
  if (leadexp(lm) == vector(4,0)*0 + intvec(0,deg(lm,a3),0,0)) {{
     "LEAD_PURE_a3^" + string(deg(lm,a3));
  }}
}}
for (i=1; i<=size(G); i++) {{
  lm = lead(G[i]);
  if (leadexp(lm) == intvec(deg(lm,a2),0,0,0)) {{
     "LEAD_PURE_a2^" + string(deg(lm,a2));
  }}
}}
"""
fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
with os.fdopen(fd, "w") as fh:
    fh.write(script)
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=600)
    print(proc.stdout)
    if proc.stderr:
        print("STDERR:", proc.stderr[-1500:])
finally:
    os.unlink(path)
