#!/usr/bin/env python3
"""Count, for each middle term e^2, how many three-term APs of perfect
squares share it: |S(e)| where S(e) = { d>0 : e^2-d and e^2+d are both
perfect squares }.

Each such d corresponds to a three-term AP e^2-d, e^2, e^2+d of squares.
A magic-square-of-squares solution needs e^2 to be the middle of FOUR such
APs with differences u, v, u+v, u-v that are all in S(e) (all entries
positive and distinct).  So |S(e)| is the raw material count: it bounds how
many usable differences exist at a given centre.
"""
from math import isqrt


def S(e):
    out = set()
    c = e * e
    for a in range(1, isqrt(c - 1) + 1):
        b2 = 2 * c - a * a
        r = isqrt(b2)
        if r * r == b2 and b2 != c:
            d = c - a * a
            if d > 0:
                out.add(d)
    return out


def main():
    N = 60
    seq = []
    for e in range(1, N + 1):
        s = S(e)
        seq.append(len(s))
        # check the four-AP condition: distinct u,v in S(e) with u+v,u-v in S(e)
    print(",".join(str(x) for x in seq))

    # Now check the four-difference condition for e up to N:
    # do there exist u,v (nonzero, u!=v) with u,v,u+v,u-v all in S(e)?
    found = []
    for e in range(2, N + 1):
        s = S(e)
        sl = sorted(s)
        hit = False
        for u in sl:
            for v in sl:
                if u == v:
                    continue
                if (u + v in s) and (u - v > 0 and (u - v) in s):
                    hit = True
                    found.append((e, u, v))
                    break
            if hit:
                break
    print("has u,v,u+v,u-v in S(e):", found)


if __name__ == "__main__":
    main()
