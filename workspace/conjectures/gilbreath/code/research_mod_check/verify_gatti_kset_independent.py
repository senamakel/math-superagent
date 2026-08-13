"""Independent re-check of the Gatti 2020 K_S claim for S = {2,3,5}.

Second route, deliberately written differently from verify_gatti_kset.py:

1. DIRECT nested-absolute expression: the Gilbreath condition for S + [k]
   (S in G_3) is that the left edge of row 3 of the 4-element triangle S+[k]
   equals 1. Writing the operator out explicitly gives the nested absolute
   |1 - |2 - |5 - k|||; no triangle machinery, no descent loop. This row 3
   left edge exists because appending k changes nothing above row 3? No:
   appending a 4th element changes rows 1..3 of the triangle (row 1 has
   3 differences ... |s_3 - k|, etc.). The apex of the full 4-row triangle
   IS row-3's left entry, so the condition is exactly:
       apex(2,3,5,k) = | | |2-3| - |3-5| | - | |3-5| - |5-k| | | == 1
   Expanded by hand this equals |1 - |2 - |5-k||| (verified: |2-3|=1,
   |3-5|=2, so row1 = (1, 2, |5-k|); row2 = (1, |2-|5-k||); apex =
   |1 - |2-|5-k|||).
2. Full-left-edge semantics: build the WHOLE triangle of S+[k] and require
   EVERY row's first entry == 1 (the definition of S+[k] being Gilbreath),
   not just the apex.
3. Wider k range [-200, 200], and inspect the full solution set, not just
   the intersection with the predicted interval.

Run: python3 code/research_mod_check/verify_gatti_kset_independent.py
"""
from itertools import product


def apex_nested_abs(k):
    """Direct nested-absolute expression for the apex of (2,3,5,k)."""
    return abs(1 - abs(2 - abs(5 - k)))


def full_triangle_gilbreath(seq):
    """S + [k] is Gilbreath iff every row of its difference triangle
    (down to the single apex) starts with 1. Operative for 4 elements."""
    cur = list(seq)
    while len(cur) > 1:
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        if cur[0] != 1:
            return False
    return True


def ks_full_semantics(kmin, kmax):
    return [k for k in range(kmin, kmax + 1) if full_triangle_gilbreath([2, 3, 5, k])]


if __name__ == "__main__":
    # (a) hand-verified candidates satisfy the direct equation
    claimed = [1, 3, 5, 7, 9]
    direct = [k for k in claimed if apex_nested_abs(k) == 1]
    print(f"direct nested-abs: apex(|1-|2-|5-k|||)==1 for k in {claimed}: {direct}")
    assert direct == claimed, "hand-checked candidates must satisfy the equation"

    # (b) brute force the DIRECT equation over [-200, 200]
    direct_all = [k for k in range(-200, 201) if apex_nested_abs(k) == 1]
    print(f"direct nested-abs, k in [-200,200]: {direct_all}  |K| = {len(direct_all)}")

    # (c) full-triangle left-edge semantics over [-200, 200]
    sem_all = ks_full_semantics(-200, 200)
    print(f"full-triangle-left-edge semantics:   {sem_all}  |K| = {len(sem_all)}")

    # (d) Gatti Eq.2 signed-sum formula (8 sign combos + tail +/-1), built
    #     from the triangle of S alone (independent of k)
    S = [2, 3, 5]
    tri = [list(S)]
    while len(tri[-1]) > 1:
        cur = tri[-1]
        tri.append([abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)])
    # anti-diagonal of S: s^2_1 = apex of (2,3,5) = 1; s^1_2 = |3-5| = 2
    anti = [tri[2][0], tri[1][1]]
    print(f"anti-diagonal of S=(2,3,5): s^2_1={anti[0]}, s^1_2={anti[1]} "
          f"(expect 1 and 2)")
    formula = set()
    for signs in product((-1, 1), repeat=2):
        for tail in (-1, 1):
            formula.add(sum(s * v for s, v in zip(signs, anti)) + S[-1] + tail)
    print(f"Eq.2 formula values: {sorted(formula)}  |K| = {len(formula)}")

    ok = (set(direct_all) == set(sem_all) == set(formula)
          and len(direct_all) == 5 and len(formula) == 5)
    print(f"ALL THREE ROUTES AGREE and |K| = 5 != 2^(3-1) = 4: {ok}")