#!/usr/bin/env python3
"""Bremner's 7-square true magic square as the anchor for the Phi framework.

Bremner grid: c = 425^2, u = -41496, v = 138600, u+v = 97104, u-v = -180096.
Known (check_near_misses.py): v and u+v are in S(425); |u| and |u-v| are not.

Phi-framework prediction:  q = d/425^2 in Phi  <=>  d in S(425)
(and the representation must satisfy (m^2+n^2) | 425).  Check all four
values with the exact unbounded membership test used by the searches.
"""
from math import gcd, isqrt

E = 425
C = E * E


def in_phi_frac(A, B):
    """Exact membership: reduced A/B in Phi = {4mn(m^2-n^2)/(m^2+n^2)^2}."""
    d = B * B - A * A
    if d < 0:
        return False
    s = isqrt(d)
    if s * s != d:
        return False
    if s == 0:
        return False
    for ss in (s, -s):
        np_, dp_ = B + ss, 2 * B
        nm_, dm_ = B - ss, 2 * B
        if np_ <= 0 or dp_ <= 0 or nm_ <= 0 or dm_ <= 0:
            continue
        g1, g2 = gcd(np_, dp_), gcd(nm_, dm_)
        a1, b1 = np_ // g1, dp_ // g1
        a2, b2 = nm_ // g2, dm_ // g2
        if (isqrt(a1) ** 2 == a1 and isqrt(b1) ** 2 == b1
                and isqrt(a2) ** 2 == a2 and isqrt(b2) ** 2 == b2):
            return True
    return False


def direct_S_425(d):
    """d in S(425) by definition: 425^2 - d and 425^2 + d both squares."""
    c = C
    return isqrt(c - d) ** 2 == c - d and isqrt(c + d) ** 2 == c + d


def main():
    diffs = {"u": -41496, "v": 138600, "u+v": 97104, "u-v": -180096}
    print(f"e = {E}, c = {C}")
    for name, d in diffs.items():
        ad = abs(d)
        A, B = ad, C
        g = gcd(A, B)
        A, B = A // g, B // g
        in_phi = in_phi_frac(A, B)
        in_S = direct_S_425(ad)
        match = (in_phi == in_S)
        print(f"  d = {name:>4} = {d:>8}: |d|/e^2 = {A}/{B} "
              f"in Phi: {in_phi}; in S(425): {in_S}; agree: {match}")

    # also: q_v + q_{u+v}
    qv = 138600 / C
    quv = 97104 / C
    print(f"  q_v + q_{'{u+v}'} = {qv + quv:.6f} (> 1 -> automatically "
          "not in Phi, consistent with the missing third condition)")


if __name__ == "__main__":
    main()