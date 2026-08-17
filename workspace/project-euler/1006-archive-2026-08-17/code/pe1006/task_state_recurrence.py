"""Analyze how Psi(k) and derived factor-level quantities evolve with k.

For each k, the length-k factors extend to length-(k+1) factors by appending
0 and/or 1. Exactly one factor (the right-special factor R) extends both ways,
every other extends exactly one way. This gives:

    Psi(k+1) = sum_w [(1_{w0})(10 v_w)^2 + (1_{w1})(10 v_w+1)^2]
              = 100 (Psi(k) + v_R^2) + 20 P1(k) + N1(k)

where:
  P1(k) = sum of v_w over length-k factors w with w+'1' a factor
  N1(k) = count of such factors
  v_R   = value of the right-special factor

We tabulate the full state vector for k=1..60 and look for a small-order
constant-coefficient linear recurrence mod M among state components.
"""
import json, os

MOD = 101001001

with open(os.path.join(os.path.dirname(__file__), "..", "out", "structure.json")) as f:
    structure = json.load(f)

ks = sorted(int(k) for k in structure)

print("k : P(k) mod M : S(k) : N1 : P1 mod M : v_R mod M : Psi(k+1) via extension vs direct")
prev_ok = True
for k in ks:
    d = structure[str(k)]
    P = d["Psi"]
    values = d["values"]
    S = sum(values)
    N1 = d["N1"]
    P1 = d["P1"]
    vR = d["R"]
    # N0 = number with w0 factor
    ext = d["extensions"]  # '0','1','S'
    N0 = sum(1 for e in ext if e in ('0', 'S'))
    # recompute via extension formula -> predicted Psi(k+1)
    if str(k+1) in structure:
        pred = 100 * (P + vR*vR) + 20 * P1 + N1
        actual = structure[str(k+1)]["Psi"]
        ok = (pred == actual)
        prev_ok = prev_ok and ok
        print(f"{k:3d} : {P%MOD:9d} : {S} : N1={N1:2d} N0={N0:2d} : {P1%MOD:9d} : {vR%MOD:9d} : pred={pred%MOD:9d} actual={actual%MOD:9d} ok={ok}")

print()
print("Extension formula held for every k transition:", prev_ok)
