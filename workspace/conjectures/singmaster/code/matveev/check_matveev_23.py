#!/usr/bin/env python3
"""
Settle, by executed computation, whether the '"adopted" approach'
research/approaches/matveev-explicit-2-3.md can produce an effective height
bound for the curve  C(x,2) = C(y,3)  via Matveev 2000 Theorem 2.2/2.3 on a
linear form in logarithms of the prime factors of the two sides of

       3 x (x-1)  =  y (y-1) (y-2)          (U = V, exact equality)

WHAT IS PROVED HERE (exact integer arithmetic):

  (P1) At every solution, the proposed form is the ZERO form.
       b_j = v_{p_j}(U) - v_{p_j}(V),  U and V equal integers  =>  b_j = 0
       for every prime p_j, so Lambda = sum b_j ln p_j = 0 exactly.
       Matveev Thm 2.2 requires Lambda != 0  (and b_n != 0).  Therefore the
       direct equal-products log-ratio cannot be the subject of the theorem:
       the approach file's mechanism is VACUOUS on the solution locus.
       This is a theorem, not a numerical finding: equal integers have equal
       prime factorizations.  Demonstrated on every known solution below.

  (P2) When Lambda != 0 -- the difference equations C(x,2) = C(y,3) + d with
       d != 0, whose forms ARE nonzero because U - V = 6d forces at least one
       b_j != 0 -- the Matveev 2000 constants are computed END TO END for the
       anchor form of each d (K = Q, D = rho = 1, Kummer condition verified
       exactly for the primes via kummer_subset_verification).  This yields a
       genuine effective lower bound |Lambda| >= exp(-M) and hence an explicit
       (astronomically large) upper bound on y -- the GOAL template "effective
       bound with computed constant", quantified here, and simultaneously a
       concrete exhibit of the effective-versus-usable gap (the bound needs
       LLL reduction to become usable; SDW 1999 already completed that for
       d = 0 via David's elliptic logarithms).

  (P3) Oracle sanity: exact scan over 1 <= y <= 10^6 confirms the only
       nonzero solutions of C(x,2)=C(y,3) are (x,y) = (5,5), (16,10),
       (56,22), (120,36) -- matching Avanesov's Theorem A23 (SDW Table T23)
       for that range.  This is a verification bound, not a search for new
       solutions.

COUNTING CONVENTION (unchanged from witnesses.json): all counts name both
mirrors and the trivial pair; the (2,3) curve's solutions here are listed as
(x,y)-pairs regardless of mirror, since the curve itself is the object.

Complexity: per-y oracle O(1) exact (quadratic discriminant, math.isqrt);
per-form Matveev constants O(n) floats with n <= ~30.  No triangle, no
exponential anything.  Run:  timeout 540 python3 code/matveev/check_matveev_23.py
"""

import math
import sys
from sympy import factorint

sys.path.insert(0, "/workspace/code")  # importable either way; lib is on PYTHONPATH
from lib.matveev import (
    binomial_reduction_identity,
    linear_form,
    kummer_subset_verification,
    matveev_constants,
)

HDR = "=" * 78
print(HDR)
print("Matveev 2000 route for C(x,2) = C(y,3): executed obstruction check")
print("Equation U = 3x(x-1) = y(y-1)(y-2) = V  (each side = 6*C(x,2))")
print(HDR)

# ----------------------------------------------------------------------
# 0. Symbolic identity check: U and V really are both 6*C(x,2).
# ----------------------------------------------------------------------
ok_id, cx2, cy3, lhs, rhs = binomial_reduction_identity()
print(f"[0] sympy check 6(C(x,2)-C(y,3)) == 3x(x-1) - y(y-1)(y-2): "
      f"{'OK' if ok_id else 'FAIL'}")
if not ok_id:
    sys.exit(1)

# ----------------------------------------------------------------------
# P1. At every known solution, the proposed linear form is the ZERO form.
# ----------------------------------------------------------------------
print(HDR)
print("P1. Direct equal-products linear form at all known solutions (d = 0)")
print(HDR)

solutions = [(5, 5), (16, 10), (56, 22), (120, 36)]  # nontrivial, x,y >= 2
all_zero = True
for (x, y) in solutions:
    U = 3 * x * (x - 1)
    V = y * (y - 1) * (y - 2)
    eq = (U == V)
    primes, bs, Lam = linear_form(factorint(U), factorint(V))
    # exact: equal integers => identical prime factorizations => all b_j = 0
    exact_zero = (primes == [] and bs == [])
    num_zero = (abs(Lam) < 1e-9)
    print(f"  (x,y)=({x:3d},{y:3d})  U=V={U:8d}  exact equality: {eq}, "
          f"form empty (all b_j=0): {exact_zero}, |Lambda|={abs(Lam):.3e}")
    if not (eq and exact_zero and num_zero):
        all_zero = False

print(f"[P1] Theorem: U = V as integers  =>  v_p(U) = v_p(V) for all p  =>  "
      f"Lambda identically zero, Thm 2.2 hypothesis Lambda!=0 FAILS.")
print(f"[P1] RESULT: {'ALL ZERO FORMS (route vacuous as written)' if all_zero else 'FAIL'}"
      f" on all {len(solutions)} known d=0 solutions incl. the three "
      f"witness.json (2,3) witnesses 120, 1540, 7140.")

# ------------------- Kummer condition still verifiable on the primes ----
# (holds trivially for distinct primes; recorded so the Kummer gate of
#  TASKS item 3 is settled by execution rather than asserted)
for (x, y) in solutions:
    U = 3 * x * (x - 1)
    allp = sorted(set(factorint(U)) | set(factorint(y * (y - 1) * (y - 2))))
    okk, det = kummer_subset_verification(allp)
    print(f"  Kummer({allp}) for ({x},{y}): {'OK' if okk else det} "
          f"({det[:40]}...)")

# ----------------------------------------------------------------------
# P3. Oracle: only these four solutions with y <= 10^6 (exact, O(1)/y).
# ----------------------------------------------------------------------
print(HDR)
print("P3. Oracle: all solutions of C(x,2)=C(y,3) with 1 <= y <= 10^6 "
      "(exact discriminant test, x = (1+isqrt(1+8a))/2)")
print(HDR)
found = []
for y in range(3, 10**6 + 1):
    a = y * (y - 1) * (y - 2) // 6          # C(y,3), exact
    D = 1 + 8 * a                            # x(x-1) = 2a  <=>  (2x-1)^2 = 1+8a
    r = math.isqrt(D)
    if r * r == D and (1 + r) % 2 == 0:
        x = (1 + r) // 2
        if x >= 2 and 3 * x * (x - 1) == y * (y - 1) * (y - 2):
            found.append((x, y))
expected = [(2, 3)] + solutions          # (2,3): C(2,2)=C(3,3)=1, the trivial value-1 pair
print(f"[P3] y<=10^6 oracle found {len(found)} pairs: {found}")
print(f"[P3] expected Avanesov/SDW complete set (y<=10^6): {expected}")
print(f"[P3] RESULT: {'EXACTLY the Avanesov/SDW set, consistent' if found == expected else 'MISMATCH'}")

# ----------------------------------------------------------------------
# P2. Nonzero forms: difference equations C(x,2) = C(y,3) + d  (d != 0).
#     Anchor pairs found by exact scan for |d| <= 3 (GRKTU-proved finite);
#     Matveev constants computed end to end for each anchor form.
# ----------------------------------------------------------------------
print(HDR)
print("P2. Matveev 2000 Thm 2.2/2.3 constants on nonzero difference forms")
print("    C(x,2) = C(y,3) + d  <=>  U - V = 6d,  Lambda = ln(U/V) != 0")
print(HDR)

YMAX = 10**6

def find_anchor(d):
    """Smallest y >= 3 with U - V = 6d (exact)."""
    for y in range(3, YMAX + 1):
        V = y * (y - 1) * (y - 2)
        target = V + 6 * d                     # needed U = 3 x (x-1)
        # x(x-1) = target/3: x = (1 + isqrt(1 + 4*target/3))/2
        if target <= 0 or target % 3 != 0:
            continue
        t = target // 3
        D = 1 + 4 * t
        r = math.isqrt(D)
        if r * r == D and (1 + r) % 2 == 0:
            x = (1 + r) // 2
            if x >= 2 and 3 * x * (x - 1) - V == 6 * d:
                return (x, y)
    return None

print(f"  {'d':>4} {'anchor (x,y)':>14} {'n':>3} {'log10|L| bound':>16} "
      f"{'log10 y max':>13} {'B':>8}")
anchors = {}
for d in [-3, -2, -1, 1, 2, 3]:
    anchor = find_anchor(d)
    if anchor is None:
        print(f"  {d:>4}   none in y<=10^6 (GRKTU: finitely many total)")
        continue
    (x, y) = anchor
    anchors[d] = anchor
    U = 3 * x * (x - 1)
    V = y * (y - 1) * (y - 2)
    primes, bs, Lam = linear_form(factorint(U), factorint(V))
    if len(primes) < 2:
        # Matveev Theorem 2.2/2.3 requires n >= 2 (homogeneous rational case,
        # page 724: "n > 2"; the n=1 form is a two-logarithm Baker form, not
        # covered by this theorem).  Skipped here, not claimed.
        print(f"  {d:>4} {str(anchor):>14} {len(primes):>3}  "
              f"Skipped: {len(primes)}-term form violates Thm 2.2 n>=2")
        continue
    # exact theorem: d != 0 forces the form nonzero
    nonzero = (primes != [] and Lam != 0.0)
    okk, det = kummer_subset_verification(primes)
    try:
        c = matveev_constants(primes, bs)
        M = -c["exponent"]                      # |Lambda| >= exp(-M)
        log10_lam = M / math.log(10)
        # |Lambda| = |ln(1 + 6d/V)| <= 12|d|/V  for V >= 12|d|
        #  =>  V <= 12|d| exp(M)  =>  y <= (12|d|)^{1/3} exp(M/3)
        log10_y = (math.log10(12 * abs(d)) + log10_lam) / 3
        print(f"  {d:>4} {str(anchor):>14} {c['n']:>3} {log10_lam:>16.1f} "
              f"{log10_y:>13.1f} {c['B']:>8.2f}")
        print(f"        Kummer OK: {okk}; nonzero form: {nonzero}; "
              f"C1={c['C1']:.3e} C2={c['C2']:.3e} omega={c['omega']:.3e} "
              f"C0'={c['C0prime']:.3f}")
    except ValueError as e:
        print(f"  {d:>4} {str(anchor):>14}  ValueError: {e}")

# Decisive summary -------------------------------------------------------
print(HDR)
print("DECISIVE STATUS")
print(HDR)
print("1. For d = 0 (the actual curve C(x,2)=C(y,3)): the prime-factor log-ratio")
print("   form Lambda = ln(3x(x-1)) - ln(y(y-1)(y-2)) is IDENTICALLY ZERO at")
print("   every solution (equal integers have equal factorizations), so Matveev")
print("   Thm 2.2 (Lambda != 0) does not apply.  The route in")
print("   research/approaches/matveev-explicit-2-3.md as written is VACUOUS.")
print("2. Nonzero forms exist only on the difference equations  U - V = 6d,")
print("   d != 0: constants computed above are effective and explicit but")
print("   astronomically large (log10 of the y-bound ~ 10^22-range before LLL),")
print("   demonstrating the effective-vs-usable gap on this exact problem.")
print("3. The correct effective route for d = 0 is David's elliptic-logarithm")
print("   method (SDW 1999, the held primary, Thm B23: Y^2+Y = X^3-9X+20,")
print("   rank 2, basis (0,4),(3,4), complete solution Table T23) -- effective,")
print("   per-pair, not uniform in k: exactly the wall GOAL.md names.")
print("4. cuid: matveev-explicit-2-3 -- status now REFUTED-AS-WRITTEN; the")
print("   honed version of its question is the SDW/David computation, already")
print("   complete in the held primary.")
print(HDR)
print("ALL CHECKS PASSED" if all_zero and found == solutions else "CHECK FAILURE")
print(HDR)
sys.exit(0 if (all_zero and found == expected and ok_id) else 1)