#!/usr/bin/env python3
"""Attack R-depth-k-finite (depth-survival-ladder rung).

Claim: For every fixed k>=1, S_k = { (2,g_2,...,g_k) : all g_i even positive,
A_k(1) in {0,2} } is FINITE: each gap is bounded by a function of the others
and k.

Suspect family (k=3): (2, 2M, 2) for every even positive M.
  A_3(1) = ||2-2M| - |2M-2||.
Test directly.
"""
def A_depth3(g1, g2, g3):
    # nested absolute differences of the gaps as in the ladder
    return abs(abs(g1 - g2) - abs(g2 - g3))

# g1 = 2 always. Scan g3 = 2 fixed, g2 = 2M varying.
print("g1=2, g3=2, g2=2M varying:")
count = 0
for M in range(1, 51, 2):   # odd M to keep things varied
    g2 = 2*M
    val = A_depth3(2, g2, 2)
    ok = val in (0, 2)
    if ok: count += 1
    print(f"  M={M} g2={g2}: A_3(1)={val} in{{0,2}}={ok}")
print("surviving so far:", count, "(all M give 0 -> infinite family)")

# Second family check: verify the 3-gap nested value against the FULL
# triangle semantics (A_0 = (2,3,5,...) with gaps g1=2,g2,g3 applied to odds)
def full_triangle(gaps):
    row0 = [2, 3]
    x = 3
    for g in gaps:
        x += g
        row0.append(x)
    rows = [row0]
    for _ in range(1, len(row0)):
        p = rows[-1]
        rows.append([abs(p[i]-p[i+1]) for i in range(len(p)-1)])
    return rows

print("\nCross-check with FULL triangle (A_0=2,3,5,... + gaps):")
for M in [1, 3, 7, 20]:
    gaps = [2, 2*M, 2]
    rows = full_triangle(gaps)
    # A_1(1) = g_1 = 2; need A_3(1)
    print(f"  gaps={gaps}: A_1(1)={rows[1][1]}, A_2(1)={rows[2][1]}, "
          f"A_3(1)={rows[3][1]} in{{0,2}}={rows[3][1] in (0,2)}")
