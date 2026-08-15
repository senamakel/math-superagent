#!/usr/bin/env python3
"""Independent second-route verification of Mycielski vertex/edge closed forms
from the construction recurrences, using sympy exact arithmetic.

Construction: Mycielski transition on an abstract graph:
   V_{k+1} = 2 V_k + 1
   E_{k+1} = 3 E_k + V_k
(keep G, add n mirror vertices each copying G's edges to a new apex via a star.)

This run derives closed forms from the recurrences symbolically and checks the
known OEIS forms as k solving the recurrence, not by fitting.
"""
import sympy as sp

k = sp.symbols('k', integer=True)

# --- vertices ---
# V_{k+1} = 2 V_k + 1, base V_1 = 5. Ansatz V_k = A*2^k + B.
A, B = sp.symbols('A B')
sol = sp.solve([sp.Eq(A*2 + B, 5), sp.Eq(A*4 + B, 11)], [A, B], dict=True)[0]
V_form = sp.simplify(sol[A]*2**k + sol[B])
print("V_k closed form from recurrence:", V_form)
V_seq = [int(sp.simplify(V_form.subs(k, kk))) for kk in range(1, 9)]
print("V_1..V_8 =", V_seq)
assert V_seq == [3*2**kk - 1 for kk in range(1, 9)], "vertex closed form mismatch"

# --- edges ---
# E_{k+1} = 3 E_k + V_k = 3 E_k + (3*2^k - 1)   [doubly-indexed recurrence]
# Solve the first-order linear difference equation exactly.
d = sp.symbols('d')  # dummy index
# Solution of x_{k+1} = 3 x_k + 3*2^k - 1 with x_1 = 5.
# use sympy rsolve
x = sp.Function('x')
re = sp.Eq(x(k+1), 3*x(k) + 3*2**k - 1)
E_sol = sp.rsolve(re, x(k), {x(1): 5})
E_form = sp.simplify(E_sol)
print("E_k closed form from recurrence:", E_form)
E_seq = [int(sp.simplify(E_form.subs(k, kk))) for kk in range(1, 8)]
print("E_1..E_7 =", E_seq)
expected_E = [5, 20, 71, 236, 755, 2360, 7271]
assert E_seq == expected_E, f"edge closed form mismatch: {E_seq}"
print("expected       =", expected_E)

# Cross-check against the known OEIS form (1 - 6*2^k + 7*3^k)/2
alt = sp.simplify((1 - 6*2**k + 7*3**k)/2 - E_form)
print("difference from OEIS form (1-6*2^k+7*3^k)/2:", sp.simplify(alt))
assert sp.simplify((1 - 6*2**k + 7*3**k)/2 - E_form) == 0

# Verify the order-3 recurrence E_k = 6E_{k-1} - 11E_{k-2} + 6E_{k-3} exactly.
E_expr = sp.simplify((1 - 6*2**k + 7*3**k)/2)
for kk in range(4, 10):
    lhs = E_expr.subs(k, kk)
    rhs = 6*E_expr.subs(k, kk-1) - 11*E_expr.subs(k, kk-2) + 6*E_expr.subs(k, kk-3)
    assert sp.simplify(lhs - rhs) == 0, f"recurrence fails at k={kk}"
print("order-3 recurrence E_k=6E_{k-1}-11E_{k-2}+6E_{k-3} verified symbolically for k=4..9")
print("ALL CLOSED-FORM AND RECURRENCE CHECKS PASS (independent sympy derivation)")
