#!/usr/bin/env python3
"""Exact p(3,L) values (fraction even) from the arrangement enumeration,
captured before the n=4 run overwrote the workspace file. Source: exact n=3
simplex subdivision. L -> p(3,L), exact rational."""
DATA = {
    160: "56/135",
    240: "2/5",
    320: "36/91",
    400: "542/1377",
    480: "272/693",
    640: "1532/3915",
    800: "824/2109",
    1000: "1981/5076",
    1200: "1934/4959",
    1400: "444/1139",
    1600: "10532/27027",
    1800: "2237/5742",
}

if __name__ == "__main__":
    from fractions import Fraction as F
    keys = sorted(DATA)
    for L in keys:
        print(f"L={L:5d}  p={F(DATA[L])}  float={float(F(DATA[L])):.8f}")
