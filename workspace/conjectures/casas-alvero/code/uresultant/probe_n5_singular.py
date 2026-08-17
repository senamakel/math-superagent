"""Independent dimension check of the n=5 traceless-slice ideal in Singular.

sympy's grevlex GB gave no pure a3 power -> would mean quotient not 0-dim,
CONTRADICTING CA_5 (settled true, V(slice)={0}).  Singular is the trusted
engine; compute std(GB) and the Krull dimension.  If Singular says dim 0
with a pure a3 power, sympy's GB is incomplete.
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
"NRPOLOGS = " + string(nrpolys(G));
"KRULLDIM = " + string(dim(G));
// check for a pure a3 power in the quotient: find k with a3^k in rad
// --- enumerate leading monomials to see if any pure a3^e appears
int i;
for (i=1; i<=size(G); i++) {{
  poly lm = lead(G[i]);
  if (lm == a3^deg(lm,a3)) {{ "PURE_A3_LM exponent = " + string(deg(lm,a3)); }}
}}
"GB_SIZE = " + string(size(G));
"""
fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
with os.fdopen(fd, "w") as fh:
    fh.write(script)
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=600)
    print(proc.stdout)
    if proc.stderr:
        print("STDERR:", proc.stderr[-2000:])
finally:
    os.unlink(path)
