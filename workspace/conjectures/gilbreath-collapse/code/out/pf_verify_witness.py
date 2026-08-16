"""Pattern-finder's INDEPENDENT verification of the G-witness fiber result.

Question this run must settle (GOAL priority 3): does S^2 factor through
short-range pair correlations?  Concretely, for pair-correlation order K
(joint counts N_ab(k) for 1<=k<=K), is S(n,h)^2 CONSTANT on each C_K-fiber
of h in F2^n?  The existing run claims K*(n) = min{K: constant} ~ n/2, i.e.
NOT bounded -> refutes the bounded-order collapse.

This script re-derives K*(n) from scratch (different pair-count routine,
canonical S from lib.collapse) for n=3..13, prints the actual witness pairs,
and reports the K*(n) sequence.

Exact arithmetic; O(2^n) per (n,K), n<=13 -> 8192 strings.  Exhaustive over
the whole input space = "exhaustive at small n", not a search to terminate.
"""
from collections import defaultdict
from lib.collapse import S2


def pair_counts(hbits, n, K):
    """Joint counts N_ab(k), 1<=k<=K, computed by bit-sliced comparison."""
    out = []
    for k in range(1, K + 1):
        nk = n - k
        for a in (0, 1):
            for b in (0, 1):
                c = 0
                for i in range(nk):
                    if ((hbits >> i) & 1) == a and ((hbits >> (i + k)) & 1) == b:
                        c += 1
                out.append(c)
    return tuple(out)


def fiber_witness(n, K, s2):
    """Return first (h,h') with equal C_K but different S^2, else None."""
    fibers = defaultdict(list)
    for h in range(1 << n):
        fibers[pair_counts(h, n, K)].append(h)
    for ck, hs in fibers.items():
        if len(hs) >= 2:
            base = s2[hs[0]]
            for h in hs[1:]:
                if s2[h] != base:
                    return (hs[0], h)
    return None


def main():
    print("Independent re-derivation of K*(n) = min K with S^2 constant on C_K fibers.")
    kstar = {}
    all_witnesses = {}
    for n in range(3, 14):
        s2 = {h: S2(n, [(h >> i) & 1 for i in range(n)]) for h in range(1 << n)}
        ks = None
        for K in range(1, n):
            w = fiber_witness(n, K, s2)
            if w is None:
                ks = K
                break
            else:
                all_witnesses.setdefault(n, []).append((K, w))
        # negative control: K=1 must ALWAYS have a witness when n-2>=2 (i.e. n>=4)
        kstar[n] = ks
        print(f"n={n:2d}  K*(n)={ks}  "
              + ("witness@K=1 confirmed" if all_witnesses.get(n, []) and all_witnesses[n][0][0] == 1 else "no witness@K=1"))
    print("\nK*(n) sequence (n=3..13):", [kstar[n] for n in range(3, 14)])
    print("\nFirst witness for each n (smallest K):")
    for n in sorted(all_witnesses):
        K, (h, hp) = all_witnesses[n][0]
        hl = [(h >> i) & 1 for i in range(n)]
        hpl = [(hp >> i) & 1 for i in range(n)]
        s2h = S2(n, hl)
        s2hp = S2(n, hpl)
        print(f"  n={n:2d} K={K}: h={h:0{n}b} h'={hp:0{n}b}  S2(h)={s2h} S2(h')={s2hp}  (C_K equal)")


if __name__ == "__main__":
    main()
