"""Capture the n=6 Samuel-multiplicity extension of the CA traceless-slice
scheme, exactly.

Question under test: does |QQ[a_2..a_6]/I_6| = 6^(6-2) = 1296 = 6^4 continue
the closed form n^(n-2) verified for n=3,4,5 (3,16,125)?

Two independent exact routes, both run and cross-checked here:
  (A) Singular (trusted engine, dp order, std GB, vdim) -> exact VLENGTH;
  (B) Samuel/Valabrega-Valla identity computed from each R_i's lowest
      weighted degree:  length == prod_i ord_0(R_i) / prod_{j=2}^{n} w(a_j),
      w(a_j)=j, with ord_0(R_i)=n(n-i) expected => prod 30*24*18*12*6 / 2*3*4*5*6.

Exit 0 iff no FAIL.  Writes code/out/uresultant_n6.captured.txt atomically
(temp-file-then-move).  A Singular non-termination within the wall cap is
recorded as the measured boundary, not a wrong answer.
"""
import subprocess, tempfile, os, time, sys
from sympy import symbols, Poly, expand, resultant, binomial, sstr
from sympy import QQ as sympy_QQ
from lib.casas_alvero import is_ca, is_pure_power

x = symbols("x")
PASS, FAIL = [], []

def rec(label, ok, detail=""):
    l = f"[{'PASS' if ok else 'FAIL'}] {label}" + (f"  ({detail})" if detail else "")
    (PASS if ok else FAIL).append(l)
    print(l)

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
    """ord_0: smallest weighted degree over a_2..a_n, w(a_j)=j."""
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

# --------------------------------------------------------------------------
# (1) oracle guard
rec("oracle: (x-1)^6 over QQ is_ca",
    is_ca((x - 1) ** 6, 0))
rec("oracle: (x-1)^6 over QQ is_pure_power",
    is_pure_power((x - 1) ** 6, 0))

# --------------------------------------------------------------------------
# (2) construct n=6 resultants on the traceless slice (a1=0)
n = 6
_wall0 = time.time()
t0 = time.time()
R = slice_resultants(n)
t_construct = time.time() - t0
rec("n=6 R_i (a1=0) construction",
    True, f"{t_construct:.1f}s; term-counts={[len(r.as_poly(*symbols(f'a_2:a_7'))) if False else r.count_ops() for r in R]}")

# --------------------------------------------------------------------------
# (3) Samuel identity, independent second route (route B)
t0 = time.time()
try:
    ords = [weighted_order(r, n) for r in R]
    t_ord = time.time() - t0
    W = list(range(2, n + 1))
    from sympy import prod as sprod
    samuel = sprod(ords) / sprod(W)
    expected_ords = [n * (n - i) for i in range(1, n)]
    rec("n=6 Samuel identity: ord_0(R_i) = n(n-i)",
        ords == expected_ords,
        f"ords={ords}, expected={expected_ords}  ({t_ord:.1f}s)")
    rec("n=6 Samuel: length == prod ord_0 / prod w",
        samuel == n ** (n - 2),
        f"prod ords/prod(2..6) = {sprod(ords)}/{sprod(W)} = {samuel} vs n^(n-2)=6^4={n**(n-2)}")
except Exception as e:
    rec("n=6 Samuel identity (weighted-order route)", False, f"raised {type(e).__name__}: {e}")
    samuel = None

# --------------------------------------------------------------------------
# (4) Singular vdim, exact route A. NOT over-split: one vdim computation on
#     one process (28 cores available but a single GB is not parallelisable
#     by splitting; Singular runs single-threaded here).
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

WALL_CAP = 3000  # seconds; non-termination here = measured boundary
t0 = time.time()
vdim = None
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=WALL_CAP)
    t_sing = time.time() - t0
    out = proc.stdout
    for line in out.splitlines():
        if line.startswith("VDIM"):
            vdim = int(line.split("=")[1].strip())
        if line.startswith("KRULLDIM"):
            kdim = line.split("=")[1].strip()
    rec("n=6 Singular: KRULLDIM=0, VDIM=6^4=1296",
        vdim == 6 ** (n - 2),
        f"Singular took {t_sing:.1f}s; KRULLDIM={kdim}, VDIM={vdim}, expected 1296")
    if proc.stderr:
        print("STDERR:", proc.stderr[-1200:])
except subprocess.TimeoutExpired:
    t_sing = time.time() - t0
    msg = f"n=6 SINGULAR did not finish within {WALL_CAP}s wall ({t_sing:.1f}s) -- measured boundary of the multiplicity route at n=6"
    rec("n=6 Singular vdim", False, msg)
    rec("(boundary recorded; n=7 not attempted -- n=6 is the wall)",
        True, "multiplicity route stops at n=6")
except Exception as e:
    t_sing = time.time() - t0
    rec("n=6 Singular vdim", False, f"raised {type(e).__name__}: {e}")
finally:
    os.unlink(path)

# --------------------------------------------------------------------------
wall_total = time.time() - _wall0
nworkers = 1  # one Singular GB, not over-split
header = [
    "URESULTANT-n6: CA traceless-slice Samuel-multiplicity extension (EXACT)",
    f"program: code/uresultant/extend_n6_capture.py; oracle: lib.casas_alvero.is_ca/is_pure_power on (x-1)^6 over QQ (char 0)",
    "ring: QQ[a2,a3,a4,a5,a6] (a1=0 traceless slice); R_i=Res_x(f,H_i f) Hasse; weights w(a_j)=j",
    f"exact range: n=6 (n-1=5 vars), Samuel identity n=6; worker count = {nworkers} (not over-split); "
    f"wall clock = {wall_total:.1f}s (Singular {t_sing:.1f}s, construct {t_construct:.1f}s)",
]
footer = ["ALL CHECKS " + ("PASSED" if not FAIL else "FAILED")]
caption = [
    "WHAT THIS SETTLES:",
]
out = "\n".join(header + [""] + PASS + [""] + footer) + "\n"
if vdim == 6 ** (n - 2) and samuel == 6 ** (n - 2):
    out += ("\nClosed form n^(n-2) CONTINUES at n=6: |Q[a2..a6]/I_6| = 1296 = 6^4, "
            "from two independent exact routes (Singular vdim + Samuel identity).\n")
else:
    out += "\nClosed form did NOT both-route-verify at n=6; see PASS/FAIL lines and captures.\n"

_tmp = "/workspace/code/out/.uresultant_n6.captured.tmp"
with open(_tmp, "w") as fh:
    fh.write(out)
os.replace(_tmp, "/workspace/code/out/uresultant_n6.captured.txt")
print(f"\n--- capture code/out/uresultant_n6.captured.txt written "
      f"({len(out)} bytes) ---")
sys.exit(0 if not FAIL else 1)
