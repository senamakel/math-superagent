"""Extend the verified Samuel-multiplicity closed form |QQ[a_2..a_n]/I_n| = n^(n-2)
for the CA traceless-slice scheme from n=6 to n=7 (and n=8 if feasible).

Modeled on code/uresultant/extend_n6_capture.py. Two independent exact routes,
cross-checked:
  (A) Singular (trusted engine, dp order, std GB, vdim) -> exact length;
  (B) Samuel/Valabrega-Valla identity from each R_i's lowest weighted degree:
      length == prod_i ord_0(R_i) / prod_{j=2}^{n} w(a_j), w(a_j)=j,
      ord_0(R_i) = n(n-i) expected => prod_{i=1}^{n-1} n(n-i) / n! = n^(n-2).

Canonical oracle guard: lib.casas_alvero is_ca / is_pure_power on (x-1)^n over QQ.

Singular non-termination within the wall cap is recorded as the measured
boundary exactly, not retried.

Usage: python extend_n7_capture.py [n]
Writes code/out/uresultant_n7.captured.txt (or _n8). Exit 0 iff no FAIL.
"""
import subprocess, tempfile, os, time, sys
from sympy import symbols, Poly, expand, resultant, binomial, sstr, prod as sprod
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


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    wall0 = time.time()

    # (1) oracle guard
    rec(f"oracle: (x-1)^{n} over QQ is_ca", is_ca((x - 1) ** n, 0))
    rec(f"oracle: (x-1)^{n} over QQ is_pure_power", is_pure_power((x - 1) ** n, 0))

    # (2) construct resultants on the traceless slice
    t0 = time.time()
    R = slice_resultants(n)
    t_construct = time.time() - t0
    rec(f"n={n} R_i (a1=0) construction", True,
        f"{t_construct:.1f}s; term-ops={[r.count_ops() for r in R]}")

    # (3) Samuel identity (route B)
    t0 = time.time()
    try:
        ords = [weighted_order(r, n) for r in R]
        t_ord = time.time() - t0
        W = list(range(2, n + 1))
        samuel = sprod(ords) / sprod(W)
        expected_ords = [n * (n - i) for i in range(1, n)]
        rec(f"n={n} Samuel identity: ord_0(R_i) = n(n-i)", ords == expected_ords,
            f"ords={ords}, expected={expected_ords}  ({t_ord:.1f}s)")
        rec(f"n={n} Samuel: length == prod ord_0 / prod w",
            samuel == n ** (n - 2),
            f"prod ords/prod(2..{n}) = {sprod(ords)}/{sprod(W)} = {samuel} "
            f"vs n^(n-2)={n}^{n-2}={n**(n-2)}")
    except Exception as e:
        rec(f"n={n} Samuel identity (weighted-order route)", False,
            f"raised {type(e).__name__}: {e}")
        samuel = None

    # (4) Singular vdim, route A
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

    WALL_CAP = 3000
    t0 = time.time()
    vdim = None
    kdim = "N/A"
    sing_ok = False
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
        sing_ok = vdim == n ** (n - 2)
        rec(f"n={n} Singular: KRULLDIM=0, VDIM=n^(n-2)={n**(n-2)}",
            sing_ok,
            f"Singular took {t_sing:.1f}s; KRULLDIM={kdim}, VDIM={vdim}, "
            f"expected {n**(n-2)}")
        if proc.stderr:
            print("STDERR:", proc.stderr[-1200:])
    except subprocess.TimeoutExpired:
        t_sing = time.time() - t0
        msg = (f"n={n} SINGULAR did not finish within {WALL_CAP}s wall "
               f"({t_sing:.1f}s) -- MEASURED BOUNDARY of the multiplicity route at n={n}")
        rec(f"n={n} Singular vdim", False, msg)
        rec("(boundary recorded; do NOT silently retry)", True,
            "the wall cap was hit exactly")
    except Exception as e:
        t_sing = time.time() - t0
        rec(f"n={n} Singular vdim", False, f"raised {type(e).__name__}: {e}")
    finally:
        os.unlink(path)

    wall_total = time.time() - wall0
    nworkers = 1
    header = [
        f"URESULTANT-n{n}: CA traceless-slice Samuel-multiplicity extension (EXACT)",
        f"program: code/uresultant/extend_n7_capture.py; oracle: lib.casas_alvero.is_ca/is_pure_power on (x-1)^{n} over QQ (char 0)",
        f"ring: QQ[a2..a{n}] (a1=0 traceless slice); R_i=Res_x(f,H_i f) Hasse; weights w(a_j)=j",
        f"exact range: n={n} (n-1={n-1} vars), Samuel identity n={n}; worker count = {nworkers} "
        f"(not over-split); wall clock = {wall_total:.1f}s (Singular {t_sing:.1f}s, "
        f"construct {t_construct:.1f}s)",
    ]
    footer = ["ALL CHECKS " + ("PASSED" if not FAIL else "FAILED")]
    out = "\n".join(header + [""] + PASS + [""] + footer) + "\n"

    both_ok = (vdim == n ** (n - 2)) and (samuel == n ** (n - 2))
    if both_ok:
        out += (f"\nClosed form n^(n-2) CONTINUES at n={n}: "
                f"|Q[a2..a{n}]/I_{n}| = {n**(n-2)} = {n}^{n-2}, from two "
                f"independent exact routes (Singular vdim + Samuel identity).\n")
    else:
        closed = n ** (n - 2)
        out += (f"\nClosed form at n={n}: Singular VDIM={vdim} (expected {closed}), "
                f"Samuel length={samuel} (expected {closed}). "
                f"{'BOTH ROUTES AGREE' if (vdim is not None and samuel is not None and vdim==samuel==closed) else 'see PASS/FAIL lines.'}\n")

    fname = f"/workspace/code/out/uresultant_n{n}.captured.txt"
    _tmp = f"/workspace/code/out/.uresultant_n{n}.captured.tmp"
    with open(_tmp, "w") as fh:
        fh.write(out)
    os.replace(_tmp, fname)
    print(f"\n--- capture {fname} written ({len(out)} bytes) ---")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
