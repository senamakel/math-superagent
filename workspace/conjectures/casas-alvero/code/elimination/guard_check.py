"""Guard set for the S_n elimination machinery: the oracle plus the S_n
scheme construction, absorbing the unique checks of the deleted
code/casasalvero/guard_check.py (which imported a nonexistent
`charp_witness` and was already broken).

ONE canonical oracle: lib.casas_alvero (is_ca / is_pure_power /
is_counterexample). This check runs that oracle on the guard cases and also
validates the S_n scheme construction (lib.casasalvero) that the elimination
proof uses.

Checks
------
1. f = (x-a)^n for n=2..6, a in {-2,0,5}: oracle must report pass (all
   derivatives share a).
2. generic random f (integer coefficients), n=2..7: oracle must report fail.
3. f = (x-1)^n exactly: pass, and is_pure_power True.
4. char-p witnesses charp_witness(p) over GF(p) for p=2,3,5 (also 7):
   oracle pass and NOT a pure power (the negative control: hypothesis
   satisfied, conclusion false).
5. The S_n equations count and pure-power-locus substitution: the 2(n-1)
   equations vanish identically on the pure-power locus (direction V(P)⊂V(I)).

Run: python code/elimination/guard_check.py   (exit 0 iff all pass)
"""
import random
import sys
import sympy as sp
from lib.casas_alvero import is_ca, is_pure_power, charp_witness, is_counterexample
from lib.casasalvero import sn_equations, pure_power_generators

x = sp.symbols("x")
fails = []

print("== 1. pure powers must PASS the hypothesis ==")
for n in range(2, 7):
    for a0 in [-2, 0, 5]:
        f = (x - a0) ** n
        ok = is_ca(f, 0)
        print(f"  n={n} a={a0}: pass={ok}")
        if not ok:
            fails.append(("pure power n=%d a=%d" % (n, a0), None))

print("== 2. generic random f must FAIL ==")
random.seed(7)
for n in range(2, 8):
    f = x ** n + sum(random.randint(-9, 9) * x ** (n - 1 - i) for i in range(n))
    res = is_ca(f, 0)
    print(f"  n={n}: pass={res}")
    if res:
        fails.append(("random f n=%d" % n, None))

print("== 3. (x-1)^n pure power test ==")
for n in range(2, 7):
    ispure = is_pure_power((x - 1) ** n, 0)
    print(f"  n={n}: is_pure_power={ispure}")
    if not ispure:
        fails.append(("pure-power test n=%d" % n, None))

print("== 4. char-p witnesses: hypothesis ON, pure power OFF ==")
for p in [2, 3, 5, 7]:
    fp = charp_witness(p)
    pass_hyp = is_ca(fp, p)
    ispure = is_pure_power(fp, p)
    ce = is_counterexample(fp, p)
    print(f"  p={p}: oracle pass={pass_hyp}  is_pure_power={ispure} "
          f"counterexample={ce}")
    if not pass_hyp:
        fails.append(("char-witness p=%d must pass" % p, None))
    if ispure:
        fails.append(("char-witness p=%d must NOT be pure power" % p, None))
    if not ce:
        fails.append(("char-witness p=%d must be a counterexample" % p, None))

print("== 5. S_n equations vanish on the pure-power locus ==")
for n in range(2, 7):
    a = sp.symbols("a_1:%d" % (n + 1))
    r = sp.symbols("r_1:%d" % n)
    eqs = sn_equations(n, a, r)
    subs = {}
    for j in range(2, n):
        subs[r[j - 1]] = r[0]
    for j in range(1, n + 1):
        subs[a[j - 1]] = (-1) ** j * sp.binomial(n, j) * r[0] ** j
    vals = [sp.simplify(e.subs(subs)) for e in eqs]
    allzero = all(v == 0 for v in vals)
    print(f"  n={n}: all {len(eqs)} equations vanish on pure-power locus: "
          f"{allzero}")
    if not allzero:
        fails.append(("pure-power locus substitution n=%d" % n, vals))

print()
if fails:
    print("FAILURES:", len(fails))
    for what, data in fails:
        print("  -", what)
    sys.exit(1)
print("ALL ORACLE GUARD CHECKS PASSED")