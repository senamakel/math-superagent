"""
Quick check: identity A_k(1) = |Δ_k(1)| where Δ_k(i) = Σ_{j=0}^k (-1)^{k-j} C(k,j) A_0(i+j).
"""
from math import comb

A0 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def signed_fd(k, i):
    """Δ_k(i) = signed k-th forward difference at position i"""
    total = 0
    for j in range(k + 1):
        total += ((-1) ** (k - j)) * comb(k, j) * A0[i + j]
    return total

# Gilbreath A_k(1) from problem.md worked example
# A_1 = (1,2,2,4,2,4,2,4,6,2)
# A_2 = (1,0,2,2,2,2,2,2,4)
# A_3 = (1,2,0,0,0,0,0,2)
# A_4 = (1,2,0,0,0,0,2,2)
gilbreath_Ak1 = {1: 2, 2: 0, 3: 2, 4: 2}

for k in range(1, 7):
    d = signed_fd(k, 1)
    g = gilbreath_Ak1.get(k, None)
    match = "✓" if abs(d) == g else "✗ MISMATCH"
    print(f"k={k}: Δ_{k}(1) = {d}, |Δ| = {abs(d)}, A_{k}(1) = {g}  {match}")
    if abs(d) != g and g is not None:
        print(f"  → Identity A_k(1) = |Δ_k(1)| FAILS at k={k}")
        # Trace the failure
        print(f"  → Trace: Δ_{k}(1) = Δ_{k-1}(2) - Δ_{k-1}(1)")
        d1 = signed_fd(k-1, 1)
        d2 = signed_fd(k-1, 2)
        print(f"  → Δ_{k-1}(1) = {d1}, Δ_{k-1}(2) = {d2}")
        print(f"  → Δ_{k-1}(2) - Δ_{k-1}(1) = {d2} - {d1} = {d2 - d1} = {d}")
        print(f"  → But A_{k-1}(1) = {gilbreath_Ak1.get(k-1)}, A_{k-1}(2) would be needed")
        print(f"  → The Gilbreath step computes |A_{k-1}(1) - A_{k-1}(2)|, NOT |Δ_{k-1}(2) - Δ_{k-1}(1)|")
        print(f"  → The min(a,b) branch at intermediate rows broke the sign coherence")
        break