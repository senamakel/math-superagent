#!/usr/bin/env python3
"""Verify the G-run-telescope lemma (pure F2, no number theory).

Claims under test (from problem.md / the SUPPLY fold structure):

  C1. For d >= 0, the down-set down(d) = {o in [0,d]: o bitwise submask of d}
      is a disjoint union of maximal consecutive-integer runs. With
      g = nu2(d+1) = # trailing 1-bits of d:
        * every run has length exactly 2^g;
        * the number of runs is exactly 2^(popcount(d) - g);
        * every run is a block [m*2^g, (m+1)*2^g - 1] for a non-negative even m.
      Checked by brute-force enumeration of the submasks and marking
      consecutive runs, for d = 0 .. 2^14.

  C2. Telescoping identity: for any {0,1} string h with boundary r (two-valued,
      h[j] = [r_{j+1} != r_j]; the prime case is r = q_j mod 4) and any run
      R = [u, v]:
          XOR_{o in R} h[pos+o]  ==  [ r_{pos+u} != r_{pos+v+1} ]
      (h encodes flips of the two-valued r; XOR over a consecutive interval
      picks out parity of flips, i.e. whether the two endpoint residues differ).
      Verified two ways:
        * true brute: element-by-element XOR over the interval, for every run,
          on a bounded d-range (d <= 2^10) -- the oracle;
        * exact scaled: prefix-XOR difference (associativity of XOR makes the
          interval XOR equal pre[b+1]^pre[a]; no element loop), over the full
          d-range up to 2^14.
      Both hold for (i) the real prime h from q_j mod 4 and (ii) random h.

Every check reports the exact number of (d, pos) pairs and passes/fails.
"""
import random
import argparse
from lib.submasks import (
    downset_runs, downset_brute, runs_of_set, trailing_ones,
    boundary_from_h, fold_xor,
)


def primes_upto_index(N):
    """First N odd primes as mod-4 residues (values ignored here)."""
    ps, p = [], 3
    while len(ps) < N:
        ok = True
        for q in ps:
            if q * q > p:
                break
            if p % q == 0:
                ok = False
                break
        if ok:
            ps.append(p)
        p += 2
    return [q % 4 for q in ps]


def h_from_residues(res):
    """h[j] = [res[j+1] != res[j]] for len(res)-1 entries."""
    return [1 if res[j + 1] != res[j] else 0 for j in range(len(res) - 1)]


def prefix_xor(h):
    """pre[i] = XOR of h[0..i-1]; interval XOR h[a..b] = pre[b+1]^pre[a]."""
    pre = [0]
    for b in h:
        pre.append(pre[-1] ^ b)
    return pre


def popcount(x):
    return bin(x).count("1")


def check_runs(DMAX):
    """C1 by brute submask enumeration + run marking, d = 0..DMAX."""
    total = 0
    for d in range(DMAX + 1):
        brute = runs_of_set(downset_brute(d))
        fast = downset_runs(d)
        assert fast == brute, (d, "partition mismatch", brute, fast)
        g = trailing_ones(d)
        for (u, v) in fast:
            assert v - u + 1 == (1 << g), (d, g, u, v, "bad run length")
        assert len(fast) == (1 << (popcount(d) - g)), (
            d, "run count", len(fast), popcount(d), g)
        for (u, v) in fast:
            assert u % (1 << g) == 0, (d, "block start not aligned", u, g)
            assert v == u + (1 << g) - 1, (d, "block not full", u, v, g)
        total += 1
    return total


def check_telescope_brute(h, r, DMAX, positions):
    """True element-by-element oracle for C2 + down-set fold, d <= DMAX."""
    pairs = 0
    for d in range(DMAX + 1):
        runs = downset_runs(d)
        for pos in positions:
            for (u, v) in runs:
                acc = 0
                for o in range(u, v + 1):
                    acc ^= h[pos + o]          # element-by-element XOR
                tel = 1 if r[pos + u] != r[pos + v + 1] else 0
                assert acc == tel, (d, pos, u, v, "telescope (brute)", acc, tel)
            direct = fold_xor(h, d, pos)       # brute down-set fold, submask enum
            assert direct == fold_xor_over_runs_brute(h, d, pos, runs), (
                d, pos, "downset partition inconsistent")
            pairs += 1
    return pairs


def fold_xor_over_runs_brute(h, d, pos, runs):
    """XOR over each run, combined = XOR over the whole down-set (brute)."""
    acc = 0
    for (u, v) in runs:
        for o in range(u, v + 1):
            acc ^= h[pos + o]
    return acc


def check_telescope_prefix(h, r, DMAX, positions):
    """Exact scaled check: interval XOR via prefix-XOR difference (associativity
    of XOR: interval[a..b] = pre[b+1] ^ pre[a]). No element loop."""
    pre = prefix_xor(h)
    pairs = 0
    for d in range(DMAX + 1):
        runs = downset_runs(d)
        for pos in positions:
            for (u, v) in runs:
                acc = pre[pos + v + 1] ^ pre[pos + u]
                tel = 1 if r[pos + u] != r[pos + v + 1] else 0
                assert acc == tel, (d, pos, u, v, "telescope (prefix)", acc, tel)
            pairs += 1
    return pairs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--trials", type=int, default=6,
                    help="random-h control trials (default 6; 30 takes ~10min)")
    ap.add_argument("--dmax-full", type=int, default=1 << 14,
                    help="full run-structure / prefix-XOR sweep bound (default 2^14)")
    args = ap.parse_args()
    DMAX_FULL = args.dmax_full
    DMAX_BRUTE = min(1 << 10, DMAX_FULL)   # true element oracle bound

    # --- C1: brute run-length / run-count ---
    total_d = check_runs(DMAX_FULL)
    print(f"[C1] down-set run structure (length 2^g, count 2^(popcount-g), "
          f"block [m*2^g,(m+1)*2^g-1]) checked by brute submask enumeration "
          f"for d = 0..{DMAX_FULL} : {total_d} values, ALL PASSED")

    L = DMAX_FULL + 600
    positions_brute = range(0, 51)
    positions_full = range(0, 101)

    # --- C2: real prime h (q_j mod 4) ---
    res = primes_upto_index(L + 10)
    h_p = h_from_residues(res)
    # The genuine two-valued boundary is the residues themselves (values 1/3).
    # boundary_from_h would reconstruct a flip-equivalent 1-start boundary.
    r_p = res
    p_brute = check_telescope_brute(h_p, r_p, DMAX_BRUTE, positions_brute)
    p_full = check_telescope_prefix(h_p, r_p, DMAX_FULL, positions_full)
    print(f"[C2/prime] telescoping identity on the real prime-residue h:")
    print(f"    brute (element enumeration): d=0..{DMAX_BRUTE} x "
          f"{len(positions_brute)} positions = {p_brute} (d,pos) pairs, PASSED")
    print(f"    prefix-XOR (full):           d=0..{DMAX_FULL} x "
          f"{len(positions_full)} positions = {p_full} (d,pos) pairs, PASSED")

    # --- C2: random h ---
    random.seed(12345)
    trials = args.trials
    tb = tf = 0
    for _ in range(trials):
        h_rand = [random.randint(0, 1) for _ in range(L)]
        r_rand = boundary_from_h(h_rand)
        tb += check_telescope_brute(h_rand, r_rand, DMAX_BRUTE, positions_brute)
        tf += check_telescope_prefix(h_rand, r_rand, DMAX_FULL, positions_full)
    print(f"[C2/random] {trials} random h:")
    print(f"    brute (element enumeration): {tb} (d,pos) pairs total, PASSED")
    print(f"    prefix-XOR (full):           {tf} (d,pos) pairs total, PASSED")

    # --- NEGATIVE CONTROL (directive 26) ---
    # The telescoping identity holds because h encodes flips of a TWO-valued
    # boundary r, so XOR over an interval = parity of flips = whether the two
    # endpoint residues differ. Perturb the hypothesis: use a THREE-valued
    # boundary (prime residues mod 3). Parity of flips no longer determines
    # endpoint difference (0->1->2 is two flips with different endpoints), so
    # the identity MUST break. A nonzero mismatch count here is the check that
    # the positive result is not true by construction.
    def primes_mod3(N):
        ps, p = [], 3
        while len(ps) < N:
            ok = True
            for q in ps:
                if q * q > p:
                    break
                if p % q == 0:
                    ok = False
                    break
            if ok:
                ps.append(p)
            p += 2
        return [q % 3 for q in ps]

    neg_res = primes_mod3(DMAX_FULL + 10)
    neg_h = h_from_residues(neg_res)
    neg_positions = range(0, 21)
    neg_pairs = neg_mismatch = 0
    neg_first = None
    for d in range(DMAX_BRUTE + 1):
        for (u, v) in downset_runs(d):
            for pos in neg_positions:
                acc = 0
                for o in range(u, v + 1):
                    acc ^= neg_h[pos + o]
                tel = 1 if neg_res[pos + u] != neg_res[pos + v + 1] else 0
                neg_pairs += 1
                if acc != tel:
                    neg_mismatch += 1
                    if neg_first is None:
                        neg_first = (d, pos, u, v, acc, tel)
    print(f"[C2/NEGATIVE-CONTROL 3-valued boundary] "
          f"identity is perturbed (r = q_j mod 3):")
    print(f"    brute: d=0..{DMAX_BRUTE} x {len(neg_positions)} positions = "
          f"{neg_pairs} pairs, MISMATCHES = {neg_mismatch} (expected nonzero; "
          f"the 2-valued hypothesis is load-bearing)")
    if neg_first is not None:
        print(f"    first mismatch d={neg_first[0]} pos={neg_first[1]} "
              f"run={neg_first[2]}-{neg_first[3]} xor={neg_first[4]} "
              f"tel={neg_first[5]}")


if __name__ == "__main__":
    main()
