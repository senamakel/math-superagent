"""Down-set ('submask-set') structure and its run decomposition for the SUPPLY fold.

Context: the depth-d fold cell (Pascal-mod-2 / Lucas) XORs a bit string h over
the bitwise submasks of d. h is taken with a boundary r over {1,3} (residues
mod 4 of the odd primes), where h[j] = [r_{j+1} != r_j] (mod-4 mismatch
indicator). The down-set of d decomposes into maximal consecutive-integer runs,
and XOR telescopes across each run. This module exposes that decomposition;
each function is verified against brute enumeration in
code/gfold/g_run_telescope_verify.py.

All functions exact integer arithmetic.
"""


def trailing_ones(n):
    """g = number of trailing 1-bits of n (n >= 0). Equals nu2(n+1)."""
    g = 0
    while n & 1:
        g += 1
        n >>= 1
    return g


def v2(n):
    """2-adic valuation of n (n >= 1): largest g with 2^g | n."""
    g = 0
    while n & 1 == 0:
        g += 1
        n >>= 1
    return g


def and_subsets(x):
    """Yield every bitwise submask of x, largest value first, ending at 0."""
    s = x
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & x


def downset_brute(d):
    """All bitwise submasks of d, enumerated directly (2^popcount of them).

    The standard submask iteration visits exactly the submasks, which is far
    cheaper than scanning every o in [0, d] (O(2^popcount) vs O(d))."""
    return set(and_subsets(d))


def runs_of_set(S):
    """Maximal consecutive-integer runs of a set S, as sorted [u, v] pairs."""
    runs = []
    for x in sorted(S):
        if runs and x == runs[-1][1] + 1:
            runs[-1][1] = x
        else:
            runs.append([x, x])
    return runs


def downset_runs(d):
    """Partition of down-set(d) = {o in [0,d] : o submask of d} into maximal
    consecutive-integer runs [u, v] (inclusive), sorted ascending.

    Structural facts (verified by brute force):
      * g = trailing_ones(d) gives each run length exactly 2^g;
      * number of runs is 2^(popcount(d) - g);
      * every run is a block [m*2^g, (m+1)*2^g - 1].

    Derivation: d = 2^(g+1)*H + (2^g - 1) with H = d >> (g+1), the g low bits
    all 1 and bit g zero. Every submask of d is (submask of H)<<(g+1) plus an
    arbitrary low-g pattern in [0, 2^g - 1], so the down-set is the disjoint
    union over submasks s of H of the block [2^(g+1)s, 2^(g+1)s + 2^g - 1].
    """
    g = trailing_ones(d)
    H = d >> (g + 1)
    step = 1 << (g + 1)
    runs = [[step * s, step * s + (1 << g) - 1] for s in and_subsets(H)]
    runs.sort()
    return runs


def boundary_from_h(h):
    """Two-valued boundary r in {1,3} with h[j] = [r_{j+1} != r_j].

    Exists for EVERY binary string h: set r[0] = 1 and flip on a 1 in h.
    Returns list r of length len(h)+1. Verified here internally.
    """
    r = [0] * (len(h) + 1)
    r[0] = 1
    for j, b in enumerate(h):
        r[j + 1] = r[j] if b == 0 else (3 - r[j])
    return r


def fold_xor(h, d, pos):
    """Brute depth-d fold cell over submasks of d: XOR_{o submask of d} h[pos+o].
    Direct summation over the down-set; the reference 'brute submask-XOR'."""
    acc = 0
    for o in and_subsets(d):
        acc ^= h[pos + o]
    return acc
