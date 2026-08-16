"""Independent re-check of the n=5 refutation, written differently from
witness_crosscheck.py to avoid a shared bug.

Instead of grouping by a tuple, we verify the two specific things:
  (a) At K=2, every pair of strings with equal C_2 has equal S^2.
  (b) At K=1, there exists a pair of strings with equal C_1 but different S^2
      (so K=1 is NOT enough), proving min K is exactly 2.
We also print the full picture for n=5: each string, its C_2 key, its S2.
"""

from itertools import product


def submasks(d):
    o = d
    out = []
    while True:
        out.append(o)
        if o == 0:
            break
        o = (o - 1) & d
    return out


def md(n, d):
    return sorted(n - 1 - d + o for o in submasks(d))


def T(n, d, h):
    return sum(h[i] for i in md(n, d)) & 1


def S2v(n, h):
    w = sum(T(n, d, h) for d in range(2, n))
    s = (n - 2) - 2 * w
    return s * s


def ck(n, K, h):
    return tuple(sum(1 for i in range(n - k) if h[i] == a and h[i + k] == b)
                 for k in range(1, K + 1)
                 for a in (0, 1) for b in (0, 1))


def main():
    n = 5
    strings = list(product((0, 1), repeat=n))
    # (a) K=2 constancy
    fibers2 = {}
    for h in strings:
        fibers2.setdefault(ck(n, 2, h), []).append(h)
    bad = []
    for key, mem in fibers2.items():
        if len({S2v(n, h) for h in mem}) > 1:
            bad.append((key, [(h, S2v(n, h)) for h in mem]))
    # (b) K=1 witness
    fibers1 = {}
    for h in strings:
        fibers1.setdefault(ck(n, 1, h), []).append(h)
    wit1 = []
    for key, mem in fibers1.items():
        s2s = {S2v(n, h) for h in mem}
        if len(s2s) > 1:
            wit1.append((key, [(h, S2v(n, h)) for h in mem]))

    print(f"n={n}")
    print("M_d down-sets:", {d: md(n, d) for d in range(2, n)})
    print(f"number of C_2 fibers: {len(fibers2)}")
    print(f"K=2 constancy holds (no fiber has 2 S2 values)? -> {len(bad)==0}")
    if bad:
        for key, mem in bad[:5]:
            print("  violation:", key, mem)
    print(f"number of C_1 fibers: {len(fibers1)}")
    print(f"K=1 witness exists (a C_1 fiber with 2 S2 values)? -> {len(wit1)>0}")
    if wit1:
        key, mem = wit1[0]
        print("  example C_1 key:", key)
        for h, s in mem:
            print(f"    h={''.join(map(str,h))} S2={s}")

if __name__ == "__main__":
    main()
