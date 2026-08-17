"""Probe whether the column-circular-interval starts s(i) and lengths N(i) follow
closed mechanical (Beatty/floor) forms in (k,i).

Generated from the factor matrix. We want: does adding the full matrix = sum over
pairwise interval intersections with power weights, and are s(i), N(i) floor
functions of (k,i)? Report the empirical form if found.
"""
import json, os
from mpmath import mp, mpf, sqrt, floor

mp.dps = 80
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
a = mpf(3) / 2 - sqrt(5) / 2
phi = (mpf(5) ** 0.5 + 1) / 2


def load():
    return json.load(open(DATA))


def circ_interval(bits):
    n = len(bits)
    ones = [j for j, b in enumerate(bits) if b == 1]
    if not ones:
        return None, 0
    if len(ones) == n:
        return 0, n
    z0 = next(j for j, b in enumerate(bits) if b == 0)
    start, L = None, 0
    j = (z0 + 1) % n
    seen = 0
    while seen < n:
        if bits[j] == 1:
            if start is None:
                start = j
            L += 1
        else:
            if start is not None:
                break
        seen += 1
        j = (j + 1) % n
    return start, L


def main():
    data = load()
    print("Column starts s(i) for each k (n=k+1), i=0..k-1:")
    starts = {}
    lens = {}
    for k in range(1, 41):
        facs = data[str(k)]
        sv, lv = [], []
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            s, L = circ_interval(bits)
            sv.append(s)
            lv.append(L)
        starts[k] = sv
        lens[k] = lv
    for k in [6, 8, 10, 12, 14, 16]:
        print(f"  k={k}: s(i) = {starts[k]}")
        print(f"         N(i) = {lens[k]}")

    print()
    print("Fit s(i) mod n = floor((i + off) * t)  for candidate t,off; count exact matches:")
    # For each k test beatty form s(i) = floor((i*beta + gamma)) mod n with beta in
    # candidates. Check whether s(i+1)-s(i) mod n takes only two values (mechanical walk).
    print("First: are increments s(i+1)-s(i) mod n only two-valued (mechanical)?")
    for k in [8, 10, 12, 14, 16, 20]:
        sv = starts[k]
        inc = [(sv[i + 1] - sv[i]) % (k + 1) for i in range(k - 1)]
        print(f"  k={k}: increments mod n = {inc}  unique = {sorted(set(inc))}")


if __name__ == "__main__":
    main()
