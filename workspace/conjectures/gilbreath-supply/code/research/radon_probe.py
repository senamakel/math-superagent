#!/usr/bin/env python3
"""Probe the Radon-transform candidate's central spectral claim.

The candidate says the fold weight's K>1 content lives in the Walsh degrees
>= 2 of the partial subcube Radon transform. The falsifier: if all spectral
mass of the energy operator R*R sits at degree <= 1, the route is dead.

We can test the structure directly on the witness that REOPENED gives:
h = 00000010 (index 6) vs h' = 00000100 (index 5), n=8. Identical C_1
(pair correlation), different S^2. We confirm the fold reads degree >= 2.

Claim to check: two single-point inputs differ in fold weight even though
they have identical Walsh degree-1 content (both are single point masses so
all their Walsh degree is determined by the point's position - low order).
Actually each single point at position u has Walsh content spread over many
degrees; but the fold weight differs because different upsets.
"""
from lib.supply_fold import s_sos


def fold_weight(n, S):
    h = [0] * n
    for j in S:
        h[j] = 1
    _, ones = s_sos(n, h)
    return ones


n = 8
# h: 00000010 -> the 1 at index 6. S = {6}? but h is length n. 
# In REOPENED the string is h = 00000010 (index 6), h'=00000100 (index 5).
print("n=8 witness:")
print("  single point index 5: nu2 =", fold_weight(n, {5}))
print("  single point index 6: nu2 =", fold_weight(n, {6}))

# Check the Kruskal-Katona single-point formula directly.
# For a single point u, nu2(n) = #{ d in [2,n-1] : u submask of d }.
for n2 in (8, 16, 32):
    for p in range(0, 6 + 1):
        u = (1 << p) - 1 if p else 0
        cnt = 0
        for d in range(2, n2):
            if (u & ~d) == 0:  # u submask of d
                cnt += 1
        # formula: # of d in [2,n-1] with u submask d = 2^{m-pc(u)} minus loses
        m = n2.bit_length() - 1
        upto = 2 ** (m - p)  # all d with u submask, ignoring range
        print(f"n={n2} u=2^p-1 p={p}: count={cnt} 2^(m-p)={upto}")
