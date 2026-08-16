"""Independent cross-check of the COLLAPSE claim K*(n) = ceil(n/2).

Fresh implementation written from scratch; deliberately does NOT import
lib.collapse.  Everything here is re-derived from the definitions in
problem.md:

  For d in [2, n-1], row down-set
      M_d = { n-1-d + o : o is a binary submask of d }
  Fold cell
      T(n,d) = XOR over i in M_d of h[i]            (h a 0/1 bitstring of length n)
  Weight
      w(h) = #{ d in [2,n-1] : T(n,d) = 1 }
  Signed excess
      S(n,h) = (n-2) - 2*w(h)
      S2     = S(n,h)**2

The fiber C_K(h) is the tuple of all pair-correlation counts
      N_ab(k) = #{ i in [0, n-1-k] : h[i]=a and h[i+k]=b }
for 1 <= k <= K and a,b in {0,1}.  Two strings are in the same C_K fiber iff
their C_K tuples are identical.

For each n in 4..12 we enumerate all 2^n strings, group by C_K for each
K in 1..n-1, and check whether S^2 is constant on every fiber.  We report:
  * the minimal K with fiber-constancy (the claimed K*),
  * whether a witness (same C_K fiber, different S^2) exists at K=1,2,3,
  * whether a witness exists at K=n-1.

There is also an explicit sample check at n=8 printing a concrete witness
pair (h, h', K<4) with equal C_K but different S^2.

Brute force on all 2^n strings is used, which at n<=12 is small (<=4096
strings), so this is an exhaustive check, not a heuristic.
"""

from itertools import product


def submasks(d):
    """Yield every binary submask o of d (o & d == o)."""
    o = d
    while True:
        yield o
        if o == 0:
            break
        o = (o - 1) & d


def M_d(n, d):
    """M_d = { n-1-d+o : o submask of d }, as a set of ABSOLUTE positions in [0, n-1]."""
    return {n - 1 - d + o for o in submasks(d)}


def T(n, d, h):
    """Fold cell: XOR (parity) over i in M_d of h[i].  h is a tuple of 0/1."""
    return sum(h[i] for i in M_d(n, d)) & 1


def w(n, h):
    """w(h) = #{ d in [2,n-1] : T(n,d) = 1 }."""
    return sum(T(n, d, h) for d in range(2, n))


def S(n, h):
    """Signed excess S(n,h) = (n-2) - 2*w(h)."""
    return (n - 2) - 2 * w(n, h)


def S2(n, h):
    """S(n,h)^2."""
    s = S(n, h)
    return s * s


def C_K(n, K, h):
    """Pair-correlation tuple: all N_ab(k) for 1<=k<=K, a,b in {0,1}."""
    out = []
    for k in range(1, K + 1):
        for a in (0, 1):
            for b in (0, 1):
                cnt = sum(1 for i in range(0, n - 1 - k + 1)
                          if h[i] == a and h[i + k] == b)
                out.append(cnt)
    return tuple(out)


def min_K_with_constancy(n):
    """Smallest K in 1..n-1 such that S2 is constant on every C_K fiber.
    Returns the K, or None if no K in range gives constancy."""
    strings = list(product((0, 1), repeat=n))
    s2 = {h: S2(n, h) for h in strings}
    for K in range(1, n):
        fibers = {}
        for h in strings:
            key = C_K(n, K, h)
            fibers.setdefault(key, set()).add(h)
        const_ok = all(len({s2[h] for h in fiber}) == 1 for fiber in fibers.values())
        if const_ok:
            return K
    return None


def witness_exists(n, K):
    """Return a witness (h, hp) with equal C_K but different S2, or None."""
    strings = list(product((0, 1), repeat=n))
    s2 = {h: S2(n, h) for h in strings}
    fibers = {}
    for h in strings:
        fibers.setdefault(C_K(n, K, h), []).append(h)
    for key, members in fibers.items():
        s2s = {s2[h] for h in members}
        if len(s2s) > 1:
            # pick two members with different S2
            base = members[0]
            for m in members[1:]:
                if s2[m] != s2[base]:
                    return (base, m)
    return None


def main():
    lines = []
    lines.append("Independent COLLAPSE cross-check: K*(n) =? ceil(n/2)")
    lines.append("S2(constant on every C_K fiber) for K=1..n-1; n=4..12")
    lines.append("=" * 78)

    header = (f"{'n':>3} {'ceil(n/2)':>9} {'min K const':>11} "
              f"{'witness K=1':>12} {'witness K=2':>12} {'witness K=3':>12} "
              f"{'witness K=n-1':>14}")
    lines.append(header)
    lines.append("-" * 78)

    mismatch = False
    for n in range(4, 13):
        mink = min_K_with_constancy(n)
        claimed = (n + 1) // 2  # ceil(n/2)
        w1 = witness_exists(n, 1) is not None
        w2 = witness_exists(n, 2) is not None
        w3 = witness_exists(n, 3) is not None
        wn1 = witness_exists(n, n - 1) is not None
        lines.append(f"{n:>3} {claimed:>9} {str(mink):>11} "
                     f"{str(w1):>12} {str(w2):>12} {str(w3):>12} "
                     f"{str(wn1):>14}")
        if mink != claimed:
            mismatch = True
            lines.append(f"   ^^ MISMATCH: claim says {claimed}, found {mink}")

    lines.append("=" * 78)

    # Explicit sample check at n=8: find a witness with K<4.
    lines.append("Sample check: n=8, find witness with equal C_K (K<4), different S2:")
    n = 8
    for K in (1, 2, 3):
        w = witness_exists(n, K)
        if w is not None:
            h, hp = w
            bits = lambda t: ''.join(str(b) for b in t)
            lines.append(f"  K={K}: witness pair:")
            lines.append(f"    h  = {bits(h)}   S2={S2(n,h)}")
            lines.append(f"    h' = {bits(hp)}  S2={S2(n,hp)}")
            lines.append(f"    C_K(h)  = {C_K(n,K,h)}")
            lines.append(f"    C_K(h') = {C_K(n,K,hp)}")
            break
    else:
        lines.append("  no witness found at n=8 with K<4")

    report = "\n".join(lines)
    print(report)
    with open("code/out/witness_crosscheck_out.txt", "w") as f:
        f.write(report + "\n")

    if mismatch:
        print("\nRESULT: CLAIM K*(n)=ceil(n/2) is REFUTED for at least one n in 4..12")
    else:
        print("\nRESULT: CLAIM K*(n)=ceil(n/2) CONFIRMED for all n in 4..12")


if __name__ == "__main__":
    main()
