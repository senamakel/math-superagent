"""Extract the circular-interval representation of each column.

Each column i of the (k+1)xk factor matrix is a circular interval: a contiguous
run of ones on the (k+1)-circle. Represent it as (start s(i), length N(i)).
Determine whether s(i) and N(i) follow closed forms in (k,i).

If they do, then pair-correlation C(i,l) = |interval_i ∩ interval_l| is
computable from (s(i),N(i)),(s(l),N(l)) and the whole sum-of-squares collapses.
"""
import json, os
from mpmath import mp, mpf, sqrt, floor

mp.dps = 80
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
a = mpf(3) / 2 - sqrt(5) / 2


def load():
    return json.load(open(DATA))


def circ_interval(bits):
    """Return (start, length) of the circular interval of ones (row index mod n)."""
    n = len(bits)
    ones = [j for j, b in enumerate(bits) if b == 1]
    if not ones:
        return None, 0
    if len(ones) == n:
        return 0, n
    # find a gap (a 0); start right after the first zero encountered going around
    z0 = next(j for j, b in enumerate(bits) if b == 0)
    # walk forward from z0+1 collecting ones
    start = None
    L = 0
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
    print("Circular-interval representation of each column: (start s(i), length N(i))")
    for k in [6, 8, 10, 12, 14]:
        facs = data[str(k)]
        n = k + 1
        print(f"\n--- k={k} (circle size {n}) ---")
        print("  i | bits (ones on circle rows 0..k) | s(i) N(i)")
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            s, L = circ_interval(bits)
            print(f"  {i:2d} | {''.join(map(str,bits))} | s={s} N={L}")

    # Hypothesis: s(i) or N(i) follow a floor/Beatty law. Test for a clean s(i).
    print("\nTesting: is N(i) given by floor/ceil rule and does s(i) follow a Beatty form?")
    # From earlier: N(i) in {floor((k+1)a), floor((k+1)a)+1}. So N is basically
    # constant = K. Each column same length K. Check that.
    for k in [6, 8, 10, 14, 20]:
        facs = data[str(k)]
        Ls = []
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            _, L = circ_interval(bits)
            Ls.append(L)
        print(f"  k={k}: all column lengths N(i) = {set(Ls)} (should be { {int(floor((k+1)*a)), int(floor((k+1)*a))+1} })")


if __name__ == "__main__":
    main()
