#!/usr/bin/env python3
"""Extended symmetry probe: signed-permutation involutions (each variable maps
to ± one other variable).  If L_d were odd under such an involution sigma
(L_d(sigma x) = -L_d(x)), the support would be exactly the monomials NOT fixed
by sigma, i.e.  a_d = (dim(h) - |Fix_sigma(h)|)/2, so c(h) = |Fix_sigma(h)|.

Test whether ANY signed involution on (A,C,D,E,F) has fixed-monomial counts
equal to c(h) = (7, 10, 16, 23, 31, 40, 50) for h = 2,4,6,8,10,12,14.
Exact arithmetic; total enumerated set is small (signed involutions on 5
letters: each GP matrix M with M^2 = I over the signed group).

Also reports, for h=4 only, whether 10 is even attainable (necessary for the
pairing explanation).
"""
import itertools

n = 5
targets = {2: 7, 4: 10, 6: 16, 8: 23, 10: 31, 12: 40, 14: 50}


def fixed_count_sign(rows, h):
    """rows: list of n tuples (target_index, sign), variable i -> sign*var[target].
    A monomial x^e (exponent tuple e) is fixed iff for every i,
    e[target_i] == e[i] (the sign does not affect the monomial value on that
    variable: x_i^{e_i} * (signs don't matter for fixedness as monomials are
    invariant under the square of the map; but a monomial maps to a DIFFERENT
    monomial when the target index differs, and to the SAME monomial composed
    with its own exponent only when the cycle returns).  Since sigma^2 = id and
    monomials in distinct variables do not interact, fixedness depends only on
    the underlying permutation: fixed iff e == e unter the permutation."""
    perm = [r[0] for r in rows]
    count = 0
    for e in itertools.product(range(h + 1), repeat=4):
        s = sum(e)
        if s > h:
            continue
        efull = e + (h - s,)
        if all(efull[perm[i]] == efull[i] for i in range(n)):
            count += 1
    return count


def signed_involutions():
    """Return all signed-permutation matrices that square to identity:
    maps  i -> s_i * var[perm[i]] with s_i in {+1,-1} and perm an involution,
    satisfying the compatibility: for j = perm[i], applying twice gives
    var[i] -> s_j * s_i * var[i] must equal var[i], so s_i * s_j = 1 for
    i != j, and for fixed points (perm[i] = i) we need s_i^2 = 1 (always)."""
    out = []
    for perm in itertools.permutations(range(n)):
        if any(perm[perm[i]] != i for i in range(n)):
            continue
        # signs: for each 2-cycle (i j): s_i*s_j = 1; fixed point: ±1
        cycle_pairs = [(i, perm[i]) for i in range(n) if perm[i] != i]
        pairs = [(i, j) for i, j in cycle_pairs if i < j]
        for signs in itertools.product([1, -1], repeat=n):
            ok = True
            for i, j in pairs:
                if signs[i] * signs[j] != 1:
                    ok = False
            if not ok:
                continue
            out.append((perm, signs))
    return out


print("== Signed-permutation involutions on 5 letters ==")
inv = signed_involutions()
print("number:", len(inv))
h4_vals = sorted({fixed_count_sign((list(zip(perm, signs))), 4)
                  for (perm, signs) in inv})
print("attainable fixed counts at h=4:", h4_vals)
print("10 attainable at h=4?", 10 in h4_vals)

print("\n== full match search over h = 2,4,6,8,10,12,14 ==")
founds = []
for perm, signs in inv:
    rows = list(zip(perm, signs))
    counts = tuple(fixed_count_sign(rows, h) for h in (2, 4, 6, 8, 10, 12, 14))
    if counts == tuple(targets[h] for h in (2, 4, 6, 8, 10, 12, 14)):
        founds.append((perm, signs, counts))
print("exact matches over all 7 h:", len(founds))
for f in founds[:5]:
    print("  ", f)

print("\n== best partial match: how many of the 7 targets are hit ==")
best = []
for perm, signs in inv:
    rows = list(zip(perm, signs))
    counts = tuple(fixed_count_sign(rows, h) for h in (2, 4, 6, 8, 10, 12, 14))
    hit = sum(1 for a, b in zip(counts, tuple(targets[h] for h in (2, 4, 6, 8, 10, 12, 14))) if a == b)
    best.append((hit, perm, signs, counts))
best.sort(key=lambda x: -x[0])
for hit, perm, signs, counts in best[:5]:
    print(f"  hits {hit}/7  perm={perm} signs={signs} counts={counts}")
print("\nVERDICT: oddness under a signed-permutation involution explains a_d")
print("only if a full match exists; otherwise the pairing picture is dead.")