#!/usr/bin/env python3
"""Determine the exact recursion R_{k+1} = F(R_k) for the Mersenne half-constant
array (c_r/2), k=2..7.  Also derive the elementwise closed form.
"""
Rs = {
 2: [1, 1, 1],
 3: [1, 3, 2, 2, 1, 2, 1],
 4: [1, 7, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 5: [1, 15, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 6: [1, 31, 16, 16, 8, 16, 8, 8, 4, 16, 8, 8, 4, 8, 4, 4, 2, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 7: [1, 63, 32, 32, 16, 32, 16, 16, 8, 32, 16, 16, 8, 16, 8, 8, 4, 32, 16, 16, 8, 16, 8, 8, 4, 16, 8, 8, 4, 8, 4, 4, 2, 32, 16, 16, 8, 16, 8, 8, 4, 16, 8, 8, 4, 8, 4, 4, 2, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 32, 16, 16, 8, 16, 8, 8, 4, 16, 8, 8, 4, 8, 4, 4, 2, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
}

# Elementwise closed form hypothesis:
# c_r/2 = smallest value from the set {1,2,...,2^{k-1}} with structure.
# Let's test: value depends on the binary string of the complement.
for k in (3, 4, 5, 6):
    R = Rs[k]
    P = len(R)
    print(f"k={k} P={P}")
    # ones positions
    ones = [r for r in range(P) if R[r] == 1]
    print("  ones at", ones, " i.e. P-r in", [P - r for r in ones])

# Try to discover: does R_{k+1}[2j] == R_k[j] for all j?  And R_{k+1}[2j+1] == ?
print("\n--- index-mapping probe R_{k+1} vs R_k ---")
for k in (3, 4, 5):
    Rk = Rs[k]
    Rn = Rs[k + 1]
    P = len(Rk)
    ev_ok = all(Rn[2 * j] == Rk[j] for j in range(P))
    # R_{k+1}[2j+1]
    odd = [Rn[2 * j + 1] for j in range(P)]
    # compare odd against Rk
    print(f"k={k}: Rn[2j]==Rk[j] all? {ev_ok}")
    print(f"     odd = {odd}")
    print(f"     Rk  = {Rk}")
