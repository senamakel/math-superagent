"""Samuel multiplicity of the CA traceless-slice scheme at small degrees,
computed by the trusted engine Singular (dp order, std GB, vdim).

Claim under test:  |QQ[a_2..a_n]/I_n| = n^{n-2}   (n=3: ? , n=4: 16=4^2,
n=5: 125=5^3).  Also test the Samuel/Valabrega-Valla identity
    length == prod_i ord_0(R_i) / prod_j w(a_j),  w(a_j)=j,
which confirms the associated graded is CM (complete intersection in gr).
If it holds at n=5 this is the mult-map certificate extended past the lex
wall: 0-dim quotient (dim 0, multiplicity computable via multiplication map).
"""
import subprocess, tempfile, os
from sympy import symbols, Poly, expand, resultant, binomial, sstr

x = symbols("x")


def hasse(f, i):
    p = Poly(expand(f), x)
    c = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(binomial(j, i) * cc * x ** (j - i)
               for j, cc in c.items() if j >= i)


def slice_resultants(n):
    a = symbols(f"a_1:{n+1}")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    return [expand(resultant(f, hasse(f, i), x).subs(a[0], 0)) for i in range(1, n)]


def to_singular(e, n):
    s = sstr(e)
    for j in range(2, n + 1):
        s = s.replace(f"a_{j}", f"a{j}")
    return s


def singular(n):
    R = slice_resultants(n)
    vars_ = ",".join(f"a{j}" for j in range(2, n + 1))
    script = f"""
ring R = 0, ({vars_}), dp;
ideal I = {", ".join(to_singular(r, n) for r in R)};
ideal G = std(I);
"KRULLDIM = " + string(dim(G));
"VDIM = " + string(vdim(G));
"GB_SIZE = " + string(size(G));
"""
    fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
    with os.fdopen(fd, "w") as fh:
        fh.write(script)
    out = ""
    try:
        proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                              text=True, timeout=900)
        out = proc.stdout
    finally:
        os.unlink(path)
    return out


for n in (3, 4, 5):
    print(f"===== n={n} traceless slice (Singular dp, trusted) =====")
    print(singular(n))
    print(f"  expected n^(n-2) = {n ** (n - 2)}")
