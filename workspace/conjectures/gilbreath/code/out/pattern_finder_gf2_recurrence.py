#!/usr/bin/env python3
"""Test exact linear recurrences over GF(2) on binary sequences derived from
the run's computed rows (blocks_depth1000.json), plus eventual-periodicity.

Binary sequences analysed:
  sbit_k   = s_k/1  mapping 0->0, 2->1   (second entry, the conjecture object)
  ebit_k   = 1 if intruder==4 else 0     (the (2,4) recharge trigger)
  rbit_k   = 1 if row k is a regen row   (b_{k+1} > b_k)
Exact over GF(2). A recurrence over GF(2) of order d: sum_{j=0..d} c_j b_{k-j}=0.
We find the shortest such recurrence via Gaussian elimination on the matrix of
shifted windows, then verify against every term.
"""
import json
import numpy as np

D = json.load(open("code/out/blocks_depth1000.json"))
b, s, intr = D["b"], D["s"], D["intruder"]

GEN = 161  # genuine regime; rows k=1..161
sbit = [int(v // 2) for v in s[:GEN]]           # 0 or 1
ebit = [1 if (intr[k] == 4) else 0 for k in range(GEN)]
rbit = [1 if (k + 1 < GEN and b[k + 1] > b[k]) else 0 for k in range(GEN)]


def gf2_recurrence(seq, max_order):
    """Find c_0..c_d with c_0=1 and sum_i c_i * seq[n-i] = 0 over GF(2)."""
    n = len(seq)
    for d in range(1, max_order + 1):
        # equations over windows of length d+1 : x_{i}..x_{i+d}, want
        # sum_{j=0..d} c_j x_{i+d-j} = 0, c_0=1 => sum_{j>=1} c_j x_{i+d-j} = x_{i+d}
        rows = []
        rhs = []
        for i in range(n - d):
            rows.append([seq[i + d - j] for j in range(1, d + 1)])  # x_{i+d-1}..x_i
            rhs.append(seq[i + d])
        A = np.array(rows, dtype=np.int8) % 2
        y = np.array(rhs, dtype=np.int8) % 2
        # Gaussian elimination over GF(2)
        A = A.copy(); y = y.copy()
        r = 0
        cols = d
        piv = []
        for c in range(cols):
            pivrow = None
            for rr in range(r, A.shape[0]):
                if A[rr, c]:
                    pivrow = rr; break
            if pivrow is None:
                continue
            A[[r, pivrow]] = A[[pivrow, r]]
            y[[r, pivrow]] = y[[pivrow, r]]
            for rr in range(A.shape[0]):
                if rr != r and A[rr, c]:
                    A[rr] ^= A[r]
                    y[rr] ^= y[r]
            piv.append(c)
            r += 1
            if r >= A.shape[0]:
                break
        # consistency: check remaining rows
        consistent = True
        for rr in range(r, A.shape[0]):
            if np.any(A[rr]) == 0 and y[rr] == 1:
                consistent = False; break
        # free variables -> the family may still hold for specific choice; we
        # just report whether a solution with c_0=1 exists for all windows.
        # A cleaner check: solve exactly and verify.
        # Build solution: variables = non-pivot columns set 0
        sol = [0] * cols
        # back substitute using pivot columns
        # We already did full elimination; reconstruct:
        # redo properly: find pivot positions in reduced A
        pivot_cols = []
        for rr in range(A.shape[0]):
            nzcol = [c for c in range(cols) if A[rr, c]]
            if nzcol:
                pivot_cols.append(nzcol[0])
        # set free vars (non-pivots) to 0, solve pivots
        col_pivot = {}
        row_of = {}
        for rr in range(A.shape[0]):
            nzcol = [c for c in range(cols) if A[rr, c]]
            if nzcol:
                col_pivot[nzcol[0]] = rr
        for c in range(cols):
            if c not in col_pivot:
                sol[c] = 0
        # solve pivot rows
        for c, rr in col_pivot.items():
            val = y[rr]
            for cc in range(c + 1, cols):
                val ^= A[rr, cc] * sol[cc]
            sol[c] = val
        cj = [1] + sol  # c_0..c_d
        # verify fwd: for all i>=d, sum_j c_j seq[i-j]=0
        ok = all(sum(cj[j] * seq[i - j] for j in range(d + 1)) % 2 == 0
                 for i in range(d, n))
        if ok:
            return d, cj
    return None, None


for name, seq in [("sbit (second entry)", sbit),
                  ("ebit (intruder==4)", ebit),
                  ("rbit (regen indicator)", rbit)]:
    d, cj = gf2_recurrence(seq, 12)
    if cj is not None:
        print(f"{name}: GF(2) recurrence of order {d}: coeffs(c1..c{d}) = {cj[1:]}")
    else:
        print(f"{name}: no GF(2) linear recurrence of order <= 12")

# eventual periodicity of the binary second-entry pattern over the full 1000
full_sbit = [int(v // 2) for v in s]
# first occurrence of each length-12 window -> if the sequence were eventual periodic
# with period p, windows repeat with that period. Look for the smallest p such that
# full_sbit[i] == full_sbit[i+p] for all i in a long range.
L = len(full_sbit)
period = None
for p in range(1, L // 2):
    if all(full_sbit[i] == full_sbit[i + p] for i in range(L - p)):
        period = p
        break
print("smallest eventual period of full 1000-term second-entry binary:", period)
