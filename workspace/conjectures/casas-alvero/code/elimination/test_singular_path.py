"""Corrected successor of code/casasalvero/test_singular_path.py: validates
the exact Singular bridge of the S_n elimination machinery
(lib.casasalvero), which is NOT the oracle and imports from the oracle,
never the reverse.

ONE canonical oracle: lib.casas_alvero decides the CA hypothesis / pure
power. This script validates the elimination machinery (lib.casasalvero)
that feeds the S_n proof, not the hypothesis test itself.

Checks
------
1. _to_singular renders QQ polynomials exactly (compare parse-back by sympy,
   using a regex substitution a(n) -> a_n, r(n) -> r_n that the old naive
   paren-stripping parse-back mangled).
2. Rabinowitsch: a1 in rad(a1^2) over QQ must be YES (rational
   Nullstellensatz; V(a1^2)=V(a1)).
3. Non-membership: a1+1 NOT in rad(a1^2) (a1+1 does not vanish at a1=0).
4. Membership in a radical ideal: a1 in rad(a1, r1) must be YES.
   Both engines (sympy and Singular, when present) must agree.

Run: python code/elimination/test_singular_path.py   (exit 0 iff all pass)
"""
import re
import shutil
import sympy as sp
from lib.casasalvero import _to_singular, rabinowitsch_membership

a1, r1, t = sp.symbols("a_1 r_1 t")
fails = []


def parse_back(s):
    """Map Singular's indexed names back to sympy symbols: a(1)->a_1,
    r(1)->r_1, then parse.  Uses a regex, not paren stripping."""
    s2 = re.sub(r"a\((\d+)\)", r"a_\1", s)
    s2 = re.sub(r"r\((\d+)\)", r"r_\1", s2)
    return sp.sympify(s2, locals={"a_1": a1, "r_1": r1})


print("== 1. _to_singular round-trip ==")
samples = [
    sp.Rational(3, 4) * a1 ** 2 * r1 - sp.Rational(1, 2) * a1 + 7,
    -a1 * r1 ** 3 + sp.Rational(2, 5) * a1 ** 2,
    a1 ** 4 - 3 * a1 ** 2 * r1 + 1,
]
for e in samples:
    s = _to_singular(e)
    back = parse_back(s)
    ok = sp.simplify(back - e) == 0
    print(f"  {e}  ->  {s}   roundtrip={ok}")
    if not ok:
        fails.append(("roundtrip", e, s, back))

print("== 2-4. Rabinowitsch through both engines (ring QQ[a_1,r_1,t]) ==")
J = [a1 ** 2]
engines = ["sympy"] + (["singular"] if shutil.which("Singular") else [])
for engine in engines:
    kw = {"n": 2} if engine == "singular" else {}
    ok1, eng, ord_, dt = rabinowitsch_membership(a1, J, [a1, r1],
                                                 engine=engine, **kw)
    ok2, *_ = rabinowitsch_membership(a1 + 1, J, [a1, r1], engine=engine, **kw)
    ok3, *_ = rabinowitsch_membership(a1, [a1, r1], [a1, r1], engine=engine,
                                      **kw)
    print(f"  [{engine}] a1 in rad(a1^2): {ok1} | "
          f"a1+1 in rad(a1^2): {ok2} | a1 in rad(a1,r1): {ok3}")
    if not (ok1 and not ok2 and ok3):
        fails.append((engine, ok1, ok2, ok3))

print()
if fails:
    print("FAILURES:")
    for f_ in fails:
        print("  -", f_)
    raise SystemExit(1)
print("SINGULAR PATH TESTS PASSED")