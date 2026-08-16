"""Determine empirically, with the EXACT oracle, which merge placement makes the
g(a,b) = no a-cup, no b-cap recursion valid.

Sizes must be C(a+b-4,a-2): S(a,b) = S(a,b-1) ∪ S(a-1,b), sizes summing correctly.
We test which of {cross slopes MAXIMAL} vs {cross slopes MINIMAL} placement, and
which side is A (left) vs B (right), yields no a-cup AND no b-cap for the union.
This is legitimate oracle-driven fixing of a separation lemma, NOT a search of
the answer space (no enumeration over point sets; just the two possible
geometric placements).
"""
from fractions import Fraction
from lib.es_geom import longest_cup, longest_cap
from lib.es_lower import _flatten, _bbox, g as current_g
from math import comb


def _mk(a, b, cross_is_max, a_is_left):
    """Recursively build no-a-cup-no-b-cap set with chosen geometry.
    a_is_left: if True, the 'a'-recurse block (slice reducing a) goes on the
    left. cross_is_max: whether cross slopes are maximal (lift) or minimal."""
    if a <= 2 or b <= 2:
        return [(Fraction(0), Fraction(0))]
    A = _flatten(_mk(a - 1, b, cross_is_max, a_is_left))      # no (a-1)-cup, no b-cap
    B = _flatten(_mk(a, b - 1, cross_is_max, a_is_left))      # no a-cup, no (b-1)-cap
    if a_is_left:
        left, right = A, B
    else:
        left, right = B, A
    Ax0, Ax1, Ay0, Ay1 = _bbox(left)
    Bx0, Bx1, By0, By1 = _bbox(right)
    gap = Fraction(10)
    shiftx = Ax1 - Bx0 + gap
    if cross_is_max:
        # lift right block so cross slopes are the maximum (steep up)
        dy = Ay1 + Fraction(2) * gap - By0   # cross slope ~2, internal ~0.1
    else:
        # sink right block so cross slopes are minimal (steep down)
        dy = Ay0 - Fraction(2) * gap - By1
    Rs = [(x + shiftx, y + dy) for (x, y) in right]
    return left + Rs


for cross_max in (True, False):
    for a_left in (True, False):
        ok_all = True
        row = []
        for (a, b) in [(4, 4), (4, 5), (5, 4), (5, 5), (5, 6), (6, 5)]:
            S = _mk(a, b, cross_max, a_left)
            cu = longest_cup(S)
            ca = longest_cap(S)
            size_ok = (len(S) == comb(a + b - 4, a - 2))
            cup_ok = (cu <= a - 1)
            cap_ok = (ca <= b - 1)
            ok = size_ok and cup_ok and cap_ok
            ok_all &= ok
            row.append(f"g({a},{b})sz={len(S)}/{comb(a+b-4,a-2)} cup={cu}(<={a-1}) cap={ca}(<={b-1}) {'OK' if ok else 'BAD'}")
        print(f"cross_is_max={cross_max} a_is_left={a_left} -> all_ok={ok_all}")
        for r in row:
            print("   ", r)
        print()
