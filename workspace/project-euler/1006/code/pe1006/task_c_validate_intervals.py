"""Validate the circular-interval structural claim by re-deriving Psi(k) from
interval intersections, and report whether it reproduces the oracle.

Psi(k) = sum_j val(w_j)^2. Write val(w_j) = sum_i w_j[i] * 10^(k-1-i) (decimal).
Then Psi = sum_{i,l} A(i,l) * 10^(2k-2-i-l) where A(i,l)=# factors with 1 at
both i and l. A(i,i)=N(i)= column length of interval i; A(i,l) for i!=l is the
size of the intersection of column-interval i and column-interval l.

We confirm: (a) A(i,l) from circular intervals equals direct count; (b) Psi
recomputed from A via powers of 10 matches oracle Psi. This validates the
structural ground, and shows what the closed-form computation must sum.

Exact integer arithmetic.
"""
import json, os

MOD = 101001001
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
PSI = os.path.join(os.path.dirname(__file__), "..", "out", "psi_data_1_150.txt")


def load_psi():
    psi = {}
    for line in open(PSI):
        line = line.strip()
        if not line or ":" not in line:
            continue
        parts = line.split(":")
        try:
            k = int(parts[0].strip())
        except ValueError:
            continue
        psi[k] = int(parts[-1].strip())
    return psi


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


def circle_inter_size(sa, La, sb, Lb, n):
    """Intersection size of two circular intervals [sa, sa+La) and [sb, sb+Lb)."""
    # Represent the circle as n points 0..n-1; interval covers length La from sa
    overlapping = 0
    for t in range(La):
        p = (sa + t) % n
        # is p in interval b? check circular membership
        if (p - sb) % n < Lb:
            overlapping += 1
    return overlapping


def main():
    data = json.load(open(DATA))
    psi = load_psi()

    print("Validate circular-interval representation reproduces Psi(k).")
    allok = True
    for k in [3, 4, 5, 6, 8, 10, 12, 15]:
        facs = data[str(k)]
        n = k + 1
        # A(i,l)
        A = [[0] * k for _ in range(k)]
        intervals = {}
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            s, L = circ_interval(bits)
            intervals[i] = (s, L)
        # recompute A from intervals
        Arec = [[0] * k for _ in range(k)]
        for i in range(k):
            sa, La = intervals[i]
            for l in range(k):
                sb, Lb = intervals[l]
                Arec[i][l] = circle_inter_size(sa, La, sb, Lb, n)
        # direct
        for i in range(k):
            for l in range(k):
                A[i][l] = sum(1 for f in facs if f[i] == '1' and f[l] == '1')
        if A != Arec:
            allok = False
            print("  k=%d: interval intersection DOES NOT match direct pair count" % k)
        # Psi from A
        P = 0
        for i in range(k):
            for l in range(k):
                P += A[i][l] * 10 ** (2 * k - 2 - i - l)
        ok = (P == psi[k])
        if not ok:
            allok = False
        print(f"  k={k}: Psi from A = {P} == oracle {psi[k]}? {ok}")
    print()
    print("ALL interval-reconstruction checks passed:", allok)


if __name__ == "__main__":
    main()
