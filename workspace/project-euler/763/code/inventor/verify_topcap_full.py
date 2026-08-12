#!/usr/bin/env python3
"""Full verification of the top-cap structural claims A1,A2,A3,B for the 3D
PE763 amoeba on the EXACT reachable config sets, N=1..14.

The on-disk data/level_*.txt files carry only *feature records* (level histogram,
max level M, bbox dims) — NOT cell coordinates — so the exact reachable config
sets are regenerated here with the fixed-width bitmask BFS from
lib/amoeba.next_level_bits (the same oracle that produced those files and the
values D(13), D(14) in code/out/d_values_more.txt and mhist_13_14.txt).

Per claim, reported per N as a "bad count" (=0 means the claim holds for every
config at that N), so the exact N-ranges where each claim holds are printed:

  A1 : every reachable N-config has EXACTLY 3 cells on its max level M.
  A2 : those 3 top cells = {p+e1,p+e2,p+e3} for a single parent p at level
       M-1 that is NOT in the config.
  A3 : replacing the top 3 by p yields a config that (i) lies in conf(N-1)
       (checked by set membership against the previous BFS level) and
       (ii) iterating the same unique-empty-parent cap-merge reaches {origin}
       deterministically in exactly N steps.
  B  : D(N+1) == sum over C in conf(N) of dividable_count(C), N=1..13.

Exact arithmetic throughout; the only "cost" is the BFS oracle itself (which
is the intended, already-proven method).  Library helpers imported from
lib/amoeba: children, f_of(=dividable_count), decode_bits, next_level_bits.
"""
import time
import sys

from lib.amoeba import next_level_bits, decode_bits, f_of, lvl, triangle_parent


def invert_bits(bits, S):
    """bits (set of bit indices) -> set that bitmask S has at those indices."""
    return tuple((S >> i) & 1 for i in bits)


def max_level_of(S, W):
    """Max level M = max(x+y+z) over the cubes of bitmask S (width W)."""
    W2 = W * W
    lv = 0
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        k = x + y + z
        if k > lv:
            lv = k
    return lv


def main(Nmax=14):
    W = Nmax + 1
    t_start = time.time()

    # level sets (bitmask ints).  We keep only the current and the previous
    # level: enough for the first-step "lands in conf(N-1)" membership test.
    level = {1}               # N=0 : {(0,0,0)} at bit 0
    prev_level = level

    lines = []
    def emit(s):
        print(s)
        lines.append(s)

    emit(f"{'N':>2} {'D(N)':>9} | {'A1bad':>6} {'A2bad':>6} {'A3bad':>6}"
         f" | {'B: sum_f':>10} {'D(N+1)':>10} {'Bmatch':>7} | {'t(s)':>6}")

    for n in range(1, Nmax + 1):
        t0 = time.time()
        # generate level n from level n-1
        new_level = next_level_bits(level, W)
        gen_t = time.time() - t0
        t1 = time.time()

        a1 = a2 = a3 = 0
        a3_checked = 0
        s_f = 0
        for S in new_level:
            cells = decode_bits(S, W)
            Sset = set(cells)
            s_f += f_of(cells)

            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]

            # A1: exactly 3 cells on max level
            if len(top) != 3:
                a1 += 1

            # A2: top-3 = {p+e1,p+e2,p+e3}, p at level M-1, p NOT in config
            p = triangle_parent(top)
            a2_bad = (p is None) or (lvl(p) != M - 1) or (p in Sset)
            if a2_bad:
                a2 += 1

            # A3: only meaningful where A2 holds (unique empty parent)
            if not a2_bad:
                a3_checked += 1
                a3_bad = False
                # (i) first collapse step lands in conf(n-1)
                S1 = (Sset - set(top)) | {p}
                # encode S1 as a bitmask to test membership in prev_level
                S1_mask = 0
                for c in S1:
                    x, y, z = c
                    S1_mask |= 1 << (x * W * W + y * W + z)
                if S1_mask not in prev_level:
                    a3_bad = True
                # (ii) iterate unique-empty-parent cap-merge to {origin}
                cur = S1
                steps = 1
                while cur != {(0, 0, 0)}:
                    Mm = max(lvl(q) for q in cur)
                    ttop = [q for q in cur if lvl(q) == Mm]
                    if len(ttop) != 3:
                        a3_bad = True
                        break
                    pp = triangle_parent(ttop)
                    if pp is None or lvl(pp) != Mm - 1 or pp in cur:
                        a3_bad = True
                        break
                    cur = (cur - set(ttop)) | {pp}
                    steps += 1
                if steps != n:
                    a3_bad = True
                if a3_bad:
                    a3 += 1

        check_t = time.time() - t1

        # CLAIM B for n=1..Nmax-1 (needs D(n+1))
        if n < Nmax:
            Dp1 = len(new_level)
            Byes = (s_f == Dp1)
        else:
            Dp1 = None
            Byes = None

        emit(f"{n:>2} {len(new_level):>9} | {a1:>6} {a2:>6} {a3:>6}"
             f" | {s_f:>10} {str(Dp1):>10} {str(Byes):>7} | "
             f"{(gen_t+check_t):>6.1f}")

        prev_level = level          # level n-1 (for next iteration's A3-check)
        level = new_level           # level n becomes current

    emit(f"\nGenerated exact config sets N=0..{Nmax} via bitmask BFS "
         f"(lib.amoeba.next_level_bits).")

    out_path = "/workspace/code/out/verify_topcap_full.txt"
    with open(out_path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"\nWrote {out_path}   elapsed {time.time()-t_start:.1f}s")


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    main(nmax)
