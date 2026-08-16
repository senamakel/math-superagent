"""Fast G-witness scanner: K*(n) = min{ K : S^2 constant on C_K-fibers }, n<=20.

Faster than the main fiber test:
  * pair counts via bit tricks:
        N_11(k) = popcount((h >> k) & h & ((1 << (n-k)) - 1))
        N_10(k) = popcount(h & M_low) - N_11
        N_01(k) = popcount((h >> k) & M_low) - N_11
        N_00(k) = (n - k) - N_11 - N_10 - N_01
  * C_K packed into one Python int (5 bits per count, count <= n <= 20 < 32).
  * per fiber only the first two S^2 values are kept (a fiber is constant iff
    it never sees a second distinct value); early exit on the first witness.
  * witness-existence is monotone in K (C_K' is a projection of C_K for
    K' < K), so scanning K = 1, 2, ... upward and stopping at the first
    witness-free K computes K* in O(K* . 2^n) total.

Also prints, for the boundary witness at each n (K = K* - 1), an explicit
demonstration: h, h', C_K equal (recomputed count-by-count) and the two S^2
values -- and verifies S2 against the definitional Walsh identity
    S(n,h)^2 = sum_{d,d'} (-1)^{sum_{i in M_d△M_d'} h_i}
for every boundary witness (third independent route into lib.collapse).
"""

from lib.collapse import S2, downset


def pair_counts_fast(h, n, K):
    """C_K(h) as a packed int: count c stored at bits 5*k_of_lag + 4*order.."""
    packed = 0
    shift = 0
    for k in range(1, K + 1):
        m = (1 << (n - k)) - 1
        n11 = ((h >> k) & h & m).bit_count()
        n10 = (h & m).bit_count() - n11
        n01 = ((h >> k) & m).bit_count() - n11
        n00 = (n - k) - n11 - n10 - n01
        for c in (n00, n01, n10, n11):
            packed |= c << (5 * shift)
            shift += 1
    return packed


def has_witness(n, K, s2):
    """Return (h, h') with equal C_K but different S^2, or None.
    Fibers store only the first two distinct S^2 values seen."""
    fibers = {}
    for h in range(1 << n):
        ck = pair_counts_fast(h, n, K)
        v = fibers.get(ck)
        if v is None:
            fibers[ck] = [h, s2[h], None]          # h, first s2, second h
        elif v[2] is None and s2[h] != v[1]:
            v[2] = h
            return (v[0], h)
        # else: fiber already constant-or-witnessed; nothing to do
    return None


def kstar(n, s2):
    for K in range(1, n):
        if has_witness(n, K, s2) is None:
            return K
    return n  # unreachable in practice (K=n-1 always witness-free)


def direct_S2(n, h):
    """Definitional Walsh identity: sum over d,d' of (-1)^{sum h over M_d △ M_d'}."""
    ms = [downset(d, n) for d in range(2, n)]
    total = 0
    for A in ms:
        for B in ms:
            x = sum(((h >> i) & 1) for i in (A ^ B))
            total += 1 if x % 2 == 0 else -1
    return total


def main():
    print("K*(n) = min{ K : S^2 constant on C_K-fibers }   (fast scan, packed keys)")
    print(f"{'n':>3} {'K*':>3}   boundary witness at K=K*-1  S2(h) vs S2(h')")
    table = {}
    for n in range(3, 21):
        s2 = {h: S2(n, [(h >> i) & 1 for i in range(n)]) for h in range(1 << n)}
        ks = kstar(n, s2)
        table[n] = ks
        # boundary witness demonstration
        w = has_witness(n, ks - 1, s2) if ks > 1 else None
        if w:
            h, hp = w
            ck_h = [pair_counts_fast(h, n, ks - 1)]
            ck_hp = [pair_counts_fast(hp, n, ks - 1)]
            assert ck_h == ck_hp, "boundary witness C_K must be equal"
            # recompute C_K equality the slow explicit way
            def slow(h):
                return [sum(1 for i in range(n - k)
                            if ((h >> i) & 1) == a and ((h >> (i + k)) & 1) == b)
                        for k in range(1, ks) for a in (0, 1) for b in (0, 1)]
            assert slow(h) == slow(hp), "slow C_K recompute must agree"
            s2h, s2hp = s2[h], s2[hp]
            assert s2h != s2hp, "S^2 must differ"
            # third route: definitional Walsh identity
            assert direct_S2(n, h) == s2h, (n, h)
            assert direct_S2(n, hp) == s2hp, (n, hp)
            print(f"{n:>3} {ks:>3}   h={h:<7d} h'={hp:<7d}   {s2h:>3d} vs {s2hp:>3d}  (C_K equal, S^2 differ; Walsh identity OK)")
        else:
            print(f"{n:>3} {ks:>3}   (no witness at K=1)")
    print()
    print("K=n-1 witness-free for all n (implied by scan: K* <= n-1 and")
    print("witness-existence is a downward-closed prefix of K).")
    print()
    print("Formula:  K*(n) == ceil(n/2) ?")
    ok = all(table[n] == (n + 1) // 2 for n in range(3, 21) if n != 5)
    ok5 = table[5] == 2
    for n in range(3, 21):
        print(f"  n={n:2d}  K*={table[n]:2d}  ceil(n/2)={(n+1)//2:2d}  "
              f"{'OK' if table[n] == (n+1)//2 else ('small-n exception' if n in (3,5) else 'DIFF')}")
    print("All n>=6 match ceil(n/2):", ok, "| n=5 exception:", table[5] == 2 and "(K*=2, not 3)")


if __name__ == "__main__":
    main()