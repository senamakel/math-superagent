#!/usr/bin/env python3
"""verify_new_source_identities.py — mechanically check the identities found
in the newly added sources (librarian cycle, 2026-08-13).

Each check runs BOTH routes:
  (a) symbolic: 4/n(k) - 1/x(k) - 1/y(k) - 1/z(k) simplifies to exactly 0
      (sympy, rational functions of the parameter),
  (b) numeric/exact: solves(n, x, y, z) from code/oracle.py on concrete
      integers, including the open-class examples cited in the sources.

Claims verified here (all were asserted-by-source before this run):
  1. OEIS A139665 / Detlefs identities:
       4/(11n-3) = 1/(3n) + 1/(3(11n-3)) + 1/(n(11n-3))
       4/(11n-4) = 1/(3n-1) + 1/(3(11n-4)) + 1/(3(3n-1)(11n-4))
  2. Chamberland (Integers 2026) Theorem 1 reverse direction, eq. (4):
       4/(qr-4s1s2) = 1/(r·T - s1s2) + 1/(T·(qr-4s1s2))
                      + s1s2/(T·(rT - s1s2)·(qr-4s1s2)),  T=(q+1)/4
     with s1,s2 | T; and the concrete open-class witness
        p = 1009 = 23·47 - 4·3·6  (s1=3, s2=6, q=23, r=47)
  3. Bloom–Elsholtz (survey Theorem 1) explicit solutions from the two
     congruence-class families:
        p ≡ -a/c (mod 4acd-1): 4/p = 1/(abd) + 1/(acdp) + 1/(bcdp)
        p ≡ -(4c²d+1)/k (mod 4cd): 4/p = 1/(ad(ak-c)) + 1/(acd)
                                    + 1/((ak-c)cdp)
  4. E(4)-exceptional small integers: 288, 336, 4545 must still have ESC
     solutions (they are < 10^18), and each of the six open classes' witness
     primes (841, 1681, 121, 961, 169, 1009, 289, 1129, 361, 1201, 529,
     1369) must pass solves().

Run like:  timeout 540 python3 code/verify_new_source_identities.py 2>&1 \
              | tee code/out/verify_new_source_identities.captured.txt
Output is bounded (no sweeping, only the listed checks).
"""

from __future__ import annotations

import json
import os
import sys

from oracle import solves, solves_fraction, is_identity  # noqa: E402
from sympy import symbols  # noqa: E402

n_sym = symbols("n")
k_sym = symbols("k")
q_sym, r_sym, s1_sym, s2_sym = symbols("q r s1 s2")
a_sym, c_sym, d_sym, kk_sym = symbols("a c d kk")

results: list[tuple[str, bool, str]] = []


def record(label: str, ok: bool, note: str) -> None:
    results.append((label, ok, note))


# ---------------------------------------------------------------- 1. Detlefs
x1 = 3 * n_sym
y1 = 3 * (11 * n_sym - 3)
z1 = n_sym * (11 * n_sym - 3)
ok = is_identity(x1, y1, z1, 11 * n_sym - 3, k_symbol=n_sym)
record("Detlefs 1: 4/(11n-3) = 1/(3n)+1/(3(11n-3))+1/(n(11n-3))", ok,
       "sympy simplify == 0" if ok else "NOT an identity")

x2 = 3 * n_sym - 1
y2 = 3 * (11 * n_sym - 4)
z2 = 3 * (3 * n_sym - 1) * (11 * n_sym - 4)
ok = is_identity(x2, y2, z2, 11 * n_sym - 4, k_symbol=n_sym)
record("Detlefs 2: 4/(11n-4) = 1/(3n-1)+1/(3(11n-4))+1/(3(3n-1)(11n-4))",
       ok, "sympy simplify == 0" if ok else "NOT an identity")

# numeric on the OEIS example 1009 = 11*92 - 3
ok = solves(1009, 3 * 92, 3 * 1009, 92 * 1009) and \
     solves_fraction(1009, 3 * 92, 3 * 1009, 92 * 1009)
record("Detlefs 1 numeric: 1009 = 11·92−3",
       ok, "solves(1009, 276, 3027, 92828)" if ok else "FAILED")

# ------------------------------------------------- 2. Chamberland eq. (4)
T = (q_sym + 1) / 4
P = q_sym * r_sym - 4 * s1_sym * s2_sym
A = r_sym * T - s1_sym * s2_sym
x_ch = A
y_ch = T * P
z_ch = (T * A * P) / (s1_sym * s2_sym)  # divide by s1s2 to make third unit fraction
ok = is_identity(x_ch, y_ch, z_ch, P, k_symbol=q_sym)
record("Chamberland (4): 4/(qr-4s1s2) = 1/(rT-s1s2)+1/(TP)+s1s2/(TAP)",
       ok, "sympy simplify == 0 (as rational function of q,r,s1,s2)"
       if ok else "NOT an identity")

# concrete open-class witness 1009 = 23·47 − 4·3·6, s1=3, s2=6
q0, r0, s10, s20 = 23, 47, 3, 6
T0 = (q0 + 1) // 4          # 6
P0 = q0 * r0 - 4 * s10 * s20  # 1009
A0 = r0 * T0 - s10 * s20      # 47*6 - 18 = 282 - 18 = 264
x0 = A0
y0 = T0 * P0                  # 6 * 1009 = 6054
z0 = (T0 * A0 * P0) // (s10 * s20)
ok = solves(P0, x0, y0, z0) and solves_fraction(P0, x0, y0, z0)
record("Chamberland numeric: 1009 = 23·47−4·3·6",
       ok, f"solves(1009, 264, 6054, {z0})" if ok else
       f"FAILED (x0,y0,z0=({x0},{y0},{z0}))")

# ------------------------------------------------------ 3. Bloom–Elsholtz
# family 1: p ≡ -a/c (mod 4acd-1) with cn + a = (4acd-1)b; solution
#   x = abd, y = acdp, z = bcdp.  Take a=c=d=1, p = 6k-1 ≡ -1 (mod 3),
#   then b = (p+1)/3 = 2k exactly.
p1 = 6 * k_sym - 1
b1 = (p1 + 1) / 3            # = 2k, polynomial
x1b = b1                     # a*b*d with a=d=1
y1b = p1                     # a*c*d*p
z1b = b1 * p1                # b*c*d*p
ok = is_identity(x1b, y1b, z1b, p1, k_symbol=k_sym)
record("B-E family1: p=6k−1, (a,c,d)=(1,1,1)  x=abd,y=acdp,z=bcdp",
       ok, "sympy simplify == 0" if ok else "NOT an identity")

# family 2: p ≡ -(4c²d+1)/k (mod 4cd); solution
#   4/p = 1/(ad(ak-c)) + 1/(acd) + 1/((ak-c)cdp),  k | 4c²d+1.
# The proof defines a by p = 4acd - (4c²d+1)/k exactly, so substitute that:
p2 = 4*a_sym*c_sym*d_sym - (4*c_sym**2*d_sym + 1)/k_sym
x2b = a_sym*d_sym*(a_sym*k_sym - c_sym)
y2b = a_sym*c_sym*d_sym
z2b = (a_sym*k_sym - c_sym)*c_sym*d_sym*p2
ok = is_identity(x2b, y2b, z2b, p2, k_symbol=a_sym)
record("B-E family2: p=4acd−(4c²d+1)/k  x=ad(ak−c),y=acd,z=(ak−c)cdp",
       ok, "sympy simplify == 0 (a,c,d,k free)" if ok else "NOT an identity")

# numeric instance of family 2: c=d=1, k=5, p=4a−1; take p=19 (a=5)
ok = solves(19, 5*(5*5-1), 5, (5*5-1)*19) and \
     solves_fraction(19, 120, 5, 456)
record("B-E family2 numeric: p=19, c=d=1, k=5, a=5",
       ok, "solves(19, 120, 5, 456)" if ok else "FAILED")

# ------------------------------------------- 4. E(4)-exceptional + witnesses
for n_e in (288, 336, 4545):
    from oracle import naive_solve
    w = naive_solve(n_e, cap=10**7)
    ok = w is not None and solves(n_e, *w)
    record(f"E(4)-exceptional {n_e} still has ESC solution", ok,
           f"witness {w}" if ok else "none found in cap")

wpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "out", "witnesses.json")
with open(wpath) as fh:
    data = json.load(fh)
allw = True
count = 0
notes = []
for cls, entries in data["witnesses"].items():
    for entry in entries:
        count += 1
        n = entry["n"]
        xyz = entry["xyz"]
        if not (solves(n, *xyz) and solves_fraction(n, *xyz)):
            allw = False
            notes.append(f"{n}:{xyz}")
record(f"witnesses.json ({count} entries) all solve", allw,
       "OK" if allw else f"FAIL {notes}")

# ------------------------------------------------------------------ report
print(f"{'PASS/FAIL':<9} {'check':<72} [note]")
print("-" * 100)
all_ok = True
for label, ok, note in results:
    all_ok = all_ok and ok
    print(f"{'PASS' if ok else 'FAIL':<9} {label:<72} [{note}]")
print("-" * 100)
print(f"summary: {sum(1 for _, o, _ in results if o)}/{len(results)} passed")
sys.exit(0 if all_ok else 1)