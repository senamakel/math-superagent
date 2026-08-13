"""Verify Gatti 2020 Cor 1 / Lemma 4 claims about the valid-extension set K_S.

Checks, for S = {2,3,5} (G_3 by the run's oracle):
1. K_S computed by direct brute force over a range of k (the definition: S' in G_4 iff
   the Gilbreath equation |s^3_1 - |s^2_2 - |s_3 - k||| = 1 holds).
2. Compare K_S with the Eq.2 signed-sum formula K = +/-s^2_1 +/- s^1_2 + s_3 +/- 1
   (2^{n} = 8 signed combinations, dim claimed = 2^{n-1} = 4).
3. Compare with Gatti's Lemma 4 prediction: K_S = parity class of odd numbers in
   ]min K, max K[ (interval completeness).

Run: python3 code/research_mod_check/verify_gatti_kset.py
"""
from itertools import product


def triangle_left_edge(s):
    """Rows of the absolute-difference triangle of s (extended by k later).
    Returns the list of first entries of rows 1.. (0-based row index 1 = first diff)."""
    rows = []
    cur = list(s)
    while len(cur) > 1:
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        rows.append(cur)
    return rows


def row1_of_extended(s, k):
    """First row of the triangle of s + [k]."""
    n = len(s)
    cur = list(s) + [k]
    out = []
    for _ in range(n):          # descend to the single apex row
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        out = cur
    return out[0]


def ks_by_definition(s, kmin=-40, kmax=40):
    """K_S = {k : s + [k] is Gilbreath} via the left-edge definition."""
    K = []
    for k in range(kmin, kmax + 1):
        # S in G_n already; extending keeps rows 1..n-1 left edges = 1 automatically?
        # No: appending k changes nothing above row n, so only the new apex matters.
        if row1_of_extended(s, k) == 1:
            K.append(k)
    return K


def ks_by_formula(s):
    """Eq.2 signed-sum formula: k = +/-s^{n-1}_1 +/-s^{n-2}_2 +/-... +/-s^1_{n-1} + s_n +/- 1.

    Build the anti-diagonal s^b_a of the triangle of s first, then all sign choices,
    then the final +/-1.
    """
    n = len(s)
    tri = [list(s)]
    while len(tri[-1]) > 1:
        cur = tri[-1]
        tri.append([abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)])
    # anti-diagonal entries s^b_a with a + b = n  (0-based row b, col a), a>=1... n-1
    anti = []
    for b in range(0, n - 1):          # rows 0..n-2 of the triangle
        a = n - 1 - b                  # col such that a + b = n-1  (0-based, so original index a+1)
        if a > 0:
            anti.append(tri[b][a])
    vals = set()
    for signs in product([-1, 1], repeat=len(anti)):
        for tail in (-1, 1):
            k = sum(s * v for s, v in zip(signs, anti)) + s[-1] + tail
            vals.add(k)
    return sorted(vals)


if __name__ == "__main__":
    S = [2, 3, 5]
    K_def = ks_by_definition(S)
    K_formula = ks_by_formula(S)
    print(f"S = {S}")
    print(f"K_S by definition (k in [-40,40]): {K_def}  |K| = {len(K_def)}")
    print(f"K_S by Eq.2 signed-sum:            {K_formula}  |K| = {len(K_formula)}")
    print(f"sets equal: {set(K_def) == set(K_formula)}")
    # Gatti's predictions
    n = len(S)
    print(f"Gatti dim prediction 2^(n-1) = {2 ** (n - 1)}; actual |K| = {len(K_def)}")
    mn, mx = min(K_def), max(K_def)
    parity_class = [k for k in range(mn, mx + 1) if k % 2 == 1]
    print(f"Lemma-4 interval-completeness prediction: {parity_class}")
    print(f"K_S == full odd interval: {sorted(K_def) == parity_class}")
    holes = [k for k in parity_class if k not in K_def]
    print(f"holes in the odd interval: {holes}")