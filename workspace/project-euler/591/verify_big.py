"""High-precision check of the d=2, n=10^13 candidate from PE 591.

Double precision cannot resolve a claimed 1e-13 closeness at magnitudes
~6e12/4e12 (double has ~16 sig figs, ~1e-4 absolute at that size), so this
recomputes the gap |a + b*sqrt(2) - pi| in mpmath decimal with 60 digits.
"""
import mpmath as mp


def big_gap(a, b, d=2, dps=60):
    mp.mp.dps = dps
    A = mp.mpf(a)
    B = mp.mpf(b)
    val = A + B * mp.sqrt(mp.mpf(d))
    gap = abs(val - mp.pi)
    return val, gap


if __name__ == "__main__":
    a, b = -6188084046055, 4375636191520
    val, gap = big_gap(a, b)
    print(f"d=2 n=1e13 candidate: a+b*sqrt(2) = {mp.nstr(val, 50)}")
    print(f"                       pi          = {mp.nstr(mp.pi, 50)}")
    print(f"|a+b*sqrt(2)-pi| = {mp.nstr(gap, 50)}")
    print(f"< 1e-13        -> {'PASS' if gap < mp.mpf('1e-13') else 'FAIL'}")

    # also check the other side of the statement's double inequality
    a2, b2 = -1019836515172, 721133315582
    val2, gap2 = big_gap(a2, b2)
    print(f"\nupper bound candidate: {mp.nstr(val2, 50)}  gap={mp.nstr(gap2, 50)}")
    print(f"< 1e-13        -> {'PASS' if gap2 < mp.mpf('1e-13') else 'FAIL'}")
