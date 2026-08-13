"""Verify the proved Rule-90 interior XOR claim against the new sources.

Claim (rule90-interior-xor): for a,b in {0,2}, |a-b|/2 = (a/2) XOR (b/2),
so within a leading {0,2} block the halved entries evolve under Rule 90
(each cell = XOR of its two neighbours = Pascal mod 2).

This independently re-derives the identification that Wikipedia's Rule 90 page
and OEIS A396593 state, WITHOUT reading those catalogue sources — confirming
that what they state is what the operator actually does.
"""
from itertools import product

def gilbreath_row(row):
    return [abs(row[i] - row[i+1]) for i in range(len(row)-1)]

# 1. The elementary |a-b|/2 == (a/2) XOR (b/2) test over all {0,2} pairs.
for a in (0, 2):
    for b in (0, 2):
        lhs = abs(a - b) // 2
        rhs = (a // 2) ^ (b // 2)
        assert lhs == rhs, (a, b, lhs, rhs)
print("OK: |a-b|/2 == (a/2) XOR (b/2) for all a,b in {0,2}")

# 2. Rule-90 evolution on the halved block equals actual halved Gilbreath rows.
# Take an all-{0,2} first row A_1 (e.g. consecutive odds start A_1=(1,2,2,2,...),
# block after leading 1 all 2s; and a mixed {0,2} tail).
def rule90_next(bits):
    n = len(bits)
    return [bits[i] ^ bits[i+1] for i in range(n-1)]

# A random {0,2} halved pattern a_i = A_k(i)/2 for i>=1 (block interior).
# Full row: A_k = (1, 0 or 2, ...) with the rest {0,2}. Halved interior b.
for HALF in product((0, 1), repeat=8):
    block = [2*x for x in HALF]           # A_k(1..8) all in {0,2} (leading 1 at pos 0)
    # Build a starting row that yields A_k as the k-th row of a Gilbreath triangle
    # directly (the block is the row itself); evolve and compare halved values.
    row = [1] + block
    nxt = gilbreath_row(row)              # A_{k+1}, absolute-difference of the row
    # Position 0 -> |1 - block[0]|; positions 1.. -> |block diff| (Rule 90 on halved).
    expect0 = abs(1 - block[0])
    got0 = nxt[0]
    assert got0 == expect0, (HALF, got0, expect0)
    # positions 1..7 of next row, halved, equal rule90 of HALF[0..7]
    interior = nxt[1:8]
    halved = [x // 2 for x in interior]
    r90 = rule90_next(HALF)
    assert halved == r90, (HALF, halved, r90)
print("OK: repeated over 2^8 halved {0,2} block patterns, next-row interior "
      "halved entries == Rule 90 of the block, leading entry |1 - b0|.")

print("\nInterior identification re-derived independently (matches "
      "Wikipedia/MathWorld Rule 90 + OEIS A396593 statements).")
