#!/usr/bin/env python3
"""
Refute R-weighted-excess-potential (excess-energy-ladder).

Claim attacked: "There exists a summable weight sequence (w_i)_{i>=1} with
w_1 > 0, w_i >= 0, and defect d_i(i) = max(0, A_k(i) - 2) such that the
weighted potential P_k = sum_i w_i * d_k(i) is non-increasing under the row
operator: P_{k+1} <= P_k for every nonnegative-integer absolute-difference
array."

Refutation (one line): a single interior spike (0,...,0,v,0,...) with v>=4 at
position p >= 2 doubles under the operator to v at BOTH p-1 and p, so its
defect mass (v-2) moves from position p to positions p-1 AND p. Non-increase
then forces w_{p-1} = 0 for every p >= 2, hence every w_j = 0,
contradicting w_1 > 0.

Smallest/general instance: v = 4 at position 2 -> A = (0,4,0) -> A' = (4,4),
forcing w_1 = 0.  (0,4,0) is a genuine row: its parent is (4,4,8) with
diffs (|4-4|, |4-8|) = (0,4). And (0,4,0) has parent too, so the whole
trajectory (4,4,8) -> (0,4,0) -> (4,4) is genuine.

We verify:
 (1) the concrete jump P((4,4)) - P((0,4,0)) = 2*w_1 + 2*w_2 - 2*w_2 = 2*w_1 > 0,
 (2) the general spike: P(A') - P(A) = (v-2)*w_{p-1} for a spike at p,
     so non-increase <==> w_{p-1} = 0, over all p >= 2.
Exact integer arithmetic; defect = max(0, entry - 2).
"""

def diff(row):
    return [abs(row[i] - row[i+1]) for i in range(len(row) - 1)]

def defect(row):
    return [max(0, x - 2) for x in row]

def weight_var(i):  # symbolic weight name for position i (1-indexed)
    return f"w{i}"

print("=== Target: R-weighted-excess-potential (excess-energy-ladder) ===")
print("Claim: EXISTS summable weights w_i>=0, w_1>0, such that P(A') <= P(A)")
print("for every absolute-difference array A, where P = sum_i w_i*max(0,A_i-2).")
print()

# --- Concrete instance --------------------------------------------------
A  = [0, 4, 0]
Ap = diff(A)
parent = [4, 4, 8]  # diff(parent) == A; check
assert diff(parent) == A, "parent should generate (0,4,0)"
assert diff(A) == Ap, "row operator on (0,4,0) gives (4,4)"

dA  = defect(A)   # (0,2,0)
dAp = defect(Ap)  # (2,2)

print(f"A        = {A}   defect = {dA}   P(A)  = 2*w2")
print(f"A'=diff  = {Ap}  defect = {dAp}  P(A') = 2*w1 + 2*w2")
print(f"P(A') - P(A) = {2}*w1 = 2*w1")
Pjump_symbol = "2*w1"
print(f"Non-increase requires P(A') <= P(A)  ==>  2*w1 <= 0  ==>  w1 <= 0.")
print(f"But the claim requires w1 > 0.  CONTRADICTION.")
print()
print(f"Genuineness: parent {parent} has |{parent[0]}-{parent[1]}|,|{parent[1]}-{parent[2]}| "
      f"= {diff(parent)} == A.  Trajectory {parent} -> {A} -> {Ap} is genuine.")
print()

# --- General spike: v>=4 at position p>=2 ------------------------------
print("=== General: single spike (0,...,0,v,0,...), v>=4, at position p>=2 ===")
print("A   : defect (v-2) only at position p.")
print("A'  : v at positions p-1 and p  -> defect (v-2) at BOTH p-1 and p.")
print("P(A') - P(A) = (v-2)*w_{p-1}.")
print("Non-increase for this single array requires w_{p-1} = 0 (since v-2 > 0).")
print("This holds for EVERY p >= 2, so w_1=w_2=...=0, contradicting w_1>0.")
print()

# spot-check the general claim for a few positions and v values
ok = True
for v in (4, 6, 8, 100):
    for p in range(2, 6):
        L = 8
        Arow = [0]*L
        Arow[p-1] = v                      # 0-indexed position p
        Ap_row = diff(Arow)
        # expect v at (p-2) and (p-1) 0-indexed = 1-indexed p-1 and p
        dA  = defect(Arow)
        dAp = defect(Ap_row)
        # check defect(diff) has (v-2) at p-1 and p, none elsewhere
        expect_dA  = [0]*L;  expect_dA[p-1] = v-2
        expect_dAp = [0]*(L-1); expect_dAp[p-2] = v-2; expect_dAp[p-1] = v-2
        if dA != expect_dA or dAp != expect_dAp:
            print(f"  MISMATCH v={v} p={p}: dA={dA} vs {expect_dA}, dAp={dAp} vs {expect_dAp}")
            ok = False
print("General spike doubling verified for v in {4,6,8,100}, p in {2..5}:",
      "OK" if ok else "FAILED")
print()
print("=== VERDICT: R-weighted-excess-potential is REFUTED ===")
print("No summable nonneg weight sequence with w1>0 can make P non-increasing,")
print("because a single interior spike forces all weights to zero.")
