"""Extend the Samuel-multiplicity closed-form test to n=6.

Claim under test: |QQ[a_2..a_n]/I_n| = n^(n-2).  Verified n=3,4,5 exactly
(215-221 capture).  A bigger run (n=6) answers one question the smaller
ones could not: does the closed form continue past the n=5 lex wall, or
does the scheme change structure there?  If n=6 gives 6^4=1296 (or any
power), the tree-count identification is reinforced; a different value
marks where the pattern breaks.
"""
import subprocess, tempfile, os, time
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


n = 6
t0 = time.time()
R = slice_resultants(n)
print(f"n=6: constructed {n-1} resultants in {time.time()-t0:.1f}s")
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
t0 = time.time()
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=1800)
    print(proc.stdout)
    if proc.stderr:
        print("STDERR:", proc.stderr[-1500:])
    print(f"(Singular took {time.time()-t0:.1f}s)")
except subprocess.TimeoutExpired:
    print(f"n=6 SINGULAR TIMED OUT after {time.time()-t0:.1f}s (1800s cap); "
          "this is the measured boundary of the multiplicity route")
finally:
    os.unlink(path)
