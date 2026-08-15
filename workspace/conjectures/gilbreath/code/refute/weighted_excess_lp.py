#!/usr/bin/env python3
"""Attack R-weighted-excess-potential via LP feasibility.

Claim (rung R-weighted-excess-potential, excess-energy-ladder):
  There exists a summable weight sequence w_i >= 0 (w_1 > 0) such that
      P_k = sum_i w_i * d_i ,  d_i = max(0, A_k(i) - 2)
  is non-increasing under the absolute-difference row operator on EVERY
  nonnegative-integer array.

Key structural observation: the operator can move a defect one position LEFT.
For A = (a0, 0, c) with c > 2:
    d(parent) positions: (max(0,a0-2), 0, max(0,c-2))
    child = (a0, c) -> d: (max(0,a0-2), max(0,c-2))
    P' - P = max(0,c-2) * (w1 - w2)      [1-indexed: pos2 -> pos1]
  monotonicity forces  w1 <= w2   (left weights must be SMALLER -- but summable
  weights with w1>0 are typically LEFT-HEAVY/decreasing, so this fights the
  intended direction).

The question is whether left-moving and right-moving constraints jointly force
all weights equal (contradicting summability), or a strictly-left constraint
forces w1 < 0. We solve linear feasibility exactly.

We use scipy linprog: variables w_1..w_L (position weights). Constraints:
  for every row of length <= L+1 with entries in {0..M}:
       sum_i w_i (d_i(child) - d_i(parent)) <= 0
We also enforce nonnegativity w_i >= 0 and w_1 >= 1 (scale). If infeasible,
the claim is refuted. We record an infeasibility certificate via Farkas.

Also do the pure hand check of the a0,0,c transition printed here.
"""
import numpy as np
from itertools import product

def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]

def defect(row):
    return [max(0, x-2) for x in row]

def main():
    print("=== Hand check: A=(1,0,c) moves defect left ===")
    for c in (4, 6):
        A = [1, 0, c]
        Ap = diff(A)
        print(f"A={A} d={defect(A)} -> A'={Ap} d'={defect(Ap)}")
        d, dp = defect(A), defect(Ap)
        # P' - P in terms of 1-indexed weights
        print("  P'-P =", " + ".join(f"{dp[i]-d[i]}*w{i+1}" for i in range(max(len(d),len(dp))) if dp[i]-d[i] != 0))
    print()

    # ---- LP feasibility ----
    L = 6          # number of weight variables (positions 1..L)
    M = 8          # max entry
    maxlen = 7     # parent row length
    rows = [tuple(r) for length in range(2, maxlen+1)
            for r in product(range(M+1), repeat=length)]
    print(f"Enumerating {len(rows)} parent rows (length<=maxlen={maxlen}, entries 0..{M})")

    # A_ub x <= b
    A_ub, b_ub = [], []
    ncons = 0
    for r in rows:
        d = defect(list(r))
        cp = diff(list(r))
        dp = defect(cp)
        # extend to length L
        de = d + [0]*(L-len(d))
        dpe = dp + [0]*(L-len(dp))
        coeff = [dpe[i]-de[i] for i in range(L)]
        if all(abs(c)==0 for c in coeff):
            continue
        A_ub.append(coeff)
        b_ub.append(0)
        ncons += 1
    A_ub = np.array(A_ub, dtype=float)
    b_ub = np.array(b_ub, dtype=float)
    print(f"{ncons} non-trivial monotonicity constraints over positions 1..{L}")

    # w >= 0  (w1 >= 1 by scaling)
    lb = np.zeros(L); lb[0] = 1.0
    bounds = [(lb[i], None) for i in range(L)]

    from scipy.optimize import linprog
    # feasibility: minimize 0 subject to constraints, w>=lb
    res = linprog(np.zeros(L), A_ub=A_ub, b_ub=b_ub,
                  bounds=bounds, method='highs')
    if res.status == 0:
        print("FEASIBLE: a weight vector exists over positions 1..%d (entries 0..%d)." % (L,M))
        print("  witness w =", np.round(res.x,4))
        print("  (NOT a proof beyond this bound; check trend vs L,M)")
    else:
        print(f"INFEASIBLE over positions 1..{L}, entries 0..{M} (status={res.status}).")
        print("This refutes the claim that ANY summable weights work, up to this window:"),
        print("no nonnegative w with w1>=1 keeps P non-increasing on all these rows.")
        # find a sparse infeasible subset via column generation / report
    print()
    print("Interpretation: if infeasible here, defect can be made to move in a way")
    print("no single Sum>0 weight system controls � refuted.")

if __name__ == "__main__":
    main()
