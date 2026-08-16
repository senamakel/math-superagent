"""Independent verification: char-p oracle agreement between the canonical
sympy oracle (code/lib/casas_alvero.py) and the naive Euclid/radical oracle
(code/brute.py), on the char-p counterexample family and pure powers.

The two oracles are independent implementations over the same input: the
canonical oracle uses sympy Poly gcd / factor_list over GF(p); the naive
oracle uses hand-rolled Euclid and squarefree-radical recursion over F_p.
Agreement across both is the cross-check that the char-p decision in the
canonical oracle is not measuring the wrong thing.

Checks (all must hold):
  1. x^{p+1} - x^p over GF(p), p = 2,3,5,7:
       is_ca True, is_pure_power False, is_counterexample True   (both oracles)
  2. (x - a)^n over GF(p), p in {2,3,5}, a in {0,1}, n in {2,3,5,7}:
       is_ca True, is_pure_power True                            (both oracles)
"""
import sys
import sympy as sp

sys.path.insert(0, "/workspace/code")
from lib.casas_alvero import is_ca, is_pure_power, is_counterexample, charp_witness
from brute import satisfies_hypothesis, is_pure_power as brute_pure_power

x = sp.symbols("x")
fails = []


def brute_verdict(coeffs_pred, p):
    """brute.py accepts ASCENDING coefficient lists. coeffs_pred is the
    sympy Poly's DESCENDING all_coeffs(); reverse exactly once."""
    asc = list(reversed(coeffs_pred))
    return satisfies_hypothesis(asc, p), brute_pure_power(asc, p)


# --- 1. char-p counterexample family -------------------------------------
print("== 1. char-p family x^{p+1}-x^p over GF(p): counterexample in BOTH oracles ==")
for p in [2, 3, 5, 7]:
    f = charp_witness(p)
    ca = is_ca(f, p)
    pp = is_pure_power(f, p)
    ce = is_counterexample(f, p)
    b_hyp, b_pp = brute_verdict(list(f.all_coeffs()), p)
    b_ce = b_hyp and not b_pp
    ok = (ca and not pp and ce) and (b_hyp and not b_pp and b_ce)
    print(f"  p={p}: canonical ca={ca} pp={pp} ce={ce} | "
          f"brute hyp={b_hyp} pp={b_pp} ce={b_ce} -> {'OK' if ok else 'FAIL'}")
    if not ok:
        fails.append(("charp-poly", p))

# --- 2. pure powers over GF(p) -------------------------------------------
print("== 2. (x-a)^n over GF(p): pure power in BOTH oracles ==")
for p in [2, 3, 5]:
    for a in [0, 1]:
        for n in [2, 3, 5, 7]:
            f = sp.Poly((x - a) ** n, x, domain=sp.GF(p))
            ca = is_ca(f, p)
            pp = is_pure_power(f, p)
            b_hyp, b_pp = brute_verdict(list(f.all_coeffs()), p)
            ok = (ca and pp) and (b_hyp and b_pp)
            if not ok:
                fails.append(("pure-power-GF", p, a, n))
print(f"  checked {2*3*4} triples (p,a,n); failures: {len(fails)}")

print()
if fails:
    print("FAILURES:")
    for f_ in fails:
        print("  -", f_)
    raise SystemExit(1)
print("CHAR-P ORACLE AGREEMENT OK (both oracles agree on every check)")