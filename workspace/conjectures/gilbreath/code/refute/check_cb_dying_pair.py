#!/usr/bin/env python3
"""Check the CB-dying-pair claim against a real failing 2-then-odds triangle.

The claim states: at the first failure row K, the dying row K-1 satisfies
b_{K-1} = 1, A_{K-1}(0) = 1, and A_{K-1}(1) in {4,6,8,...}.

We use the delete-7 sequence (2,3,5,11,13,17,19,23,...): a 2-then-odds
sequence with first-2 and a 6-gap (Colonna class), which is known to fail.
Compute the actual rows, block lengths, and first-failure row, and test
whether the claim's b_{K-1}=1 can hold simultaneously with
A_{K-1}(1) in {4,6,...}.
"""
from lib.gilbreath import rows_generator, block_profile

# delete 7 from the primes
primes = [2,3,5,11,13,17,19,23,29,31,37,41,43,47]
rows = list(rows_generator(primes, 10))

# first failure row K: A_K(0) != 1
K = None
for k in range(1, len(rows)):
    if rows[k][0] != 1:
        K = k
        break
print("first failure row K =", K)
rows[K-1][1]  # the dying row's second entry

print("row K-1 (dying row):", rows[K-1][:10], " b =", block_profile(rows[K-1]))
print("  A_{K-1}(1) =", rows[K-1][1], "  in {4,6,8,...}?", rows[K-1][1] in (4,6,8,10,12))
print("row K-2:", rows[K-2][:10], " b =", block_profile(rows[K-2]))
print("row K-3:", rows[K-3][:10], " b =", block_profile(rows[K-3]))

# The claimed conjunction: b_{K-1}=1 AND A_{K-1}(1) in {4,6,...}
# By definition b counts leading {0,2} entries from position 1.
b_val = block_profile(rows[K-1])
sn = rows[K-1][1]
print()
print("Claim holds (b_Km1=1 and A(1) in {4,6,..})?", (b_val == 1) and (sn in (4,6,8,10,12)))
print("b_{K-1} actually:", b_val)
print("A_{K-1}(1) actually:", sn)

# Definitional point: A_K(0) = |1 - A_{K-1}(1)|, failure means A_{K-1}(1) not in {0,2},
# which forces b_{K-1} = 0 (block empty), never 1.
print()
print("reduction check: |1 - A_{K-1}(1)| =", abs(1 - sn), " (must be != 1)")
