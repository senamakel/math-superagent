"""Samuel identity + multiplicity closed form at n=6, and n=7 boundary.

Verified so far: n=3,4,5,6 all give multiplicity = n^(n-2) exactly
(3=3^1, 16=4^2, 125=5^3, 1296=6^4).  Here: (1) confirm the Samuel
identity at n=6 (ords=[n(n-i)], prod/ n! ), (2) run n=7 to find the
boundary of the pattern AND of Singular's computation.
"""
import subprocess, tempfile, os, time
from sympy import (symbols, Poly, expand, resultant, binomial, sstr,
                   QQ as sympy_QQ, prod as sprod)

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


def weighted_order(poly, n):
    a = symbols(f"a_1:{n+1}")
    sl = list(a[1:])
    W = list(range(2, n + 1))
    P = Poly(poly, *sl, domain=sympy_QQ)
    return min(sum(e * w for e, w in zip(m, W)) for m, c in P.terms())


def to_singular(e, n):
    s = sstr(e)
    for j in range(2, n + 1):
        s = s.replace(f"a_{j}", f"a{j}")
    return s


# (1) Samuel identity at n=6 using the n^(n-2) length (from Singular vdim)
n = 6
R = slice_resultants(n)
ords = [weighted_order(r, n) for r in R]
W = list(range(2, n + 1))
print(f"n=6 ords={ords}, expected [n(n-i)] = {[n*(n-i) for i in range(1,n)]}")
print(f"n=6 Samuel RHS = {sprod(ords)}/{sprod(W)} = {sprod(ords)/sprod(W)}")
print(f"n=6 n^(n-2) = {n**(n-2)}")
print(f"n=6 ords match n(n-i): {ords == [n*(n-i) for i in range(1,n)]}")

# (2) n=7 boundary
n = 7
t0 = time.time()
R7 = slice_resultants(n)
print(f"\nn=7: constructed {n-1} resultants in {time.time()-t0:.1f}s")
vars_ = ",".join(f"a{j}" for j in range(2, n + 1))
script = f"""
ring R = 0, ({vars_}), dp;
ideal I = {", ".join(to_singular(r, n) for r in R7)};
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
        print("STDERR:", proc.stderr[-1200:])
    print(f"(Singular n=7 took {time.time()-t0:.1f}s)")
except subprocess.TimeoutExpired:
    print(f"n=7 SINGULAR TIMED OUT after {time.time()-t0:.1f}s (1800s cap) "
          "= measured boundary")
finally:
    os.unlink(path)
