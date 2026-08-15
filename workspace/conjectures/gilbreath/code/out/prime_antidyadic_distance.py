#!/usr/bin/env python3
"""DPC-prime-antidyadic distance: how far is the REAL prime mod-4 switch bit
from every power-of-two-periodic binary string?

Quantify (exact-integer, no floats in the arithmetic):

  h[j] = ((p_{j+2} - p_{j+1}) // 2) mod 2     for j in the ancestor window [2, n-1]

i.e. 1 iff the consecutive odd prime gap p_{j+2}-p_{j+1} is 2 (mod 4).  The
window [2,n-1] is the SAME ancestor window as the run's nu2 / linearization
scripts (code/gap_analysis/nu2_vs_gap_parity.py: hbits[2:n]); it is the fixed
row-1 interval whose {0,2}-fold XORs generate the dyadic nu2.

For each k = 0..6 (period p = 2^k) we compute the Hamming distance from the
windowed switch bit to its NEAREST p-periodic binary string, and report
dist/n.  Also report w(n)/(n-2) = density of 1s in the window (the swap-bit /
mod-4-gap density).

WHAT THIS BOUNDS
----------------
The DPC-prime-antidyadic gap: a quantitative statement of non-2^k-periodicity
of the prime switch bit.  If dist/n stayed >> 0 for every k, the prime switch
bit is asymptotically far from every power-of-two-periodic bit string.  This
is a PRIME statement and does NOT by itself close G-supply (nu2 >= c*n still
needs the correlation structure of the {0,2}-fold XORs, not just the bit being
non-periodic).

WHY THE MAJORITY/PER-CLASS DECOUPLING IS EXACT (derivation)
-----------------------------------------------------------
A p-periodic binary string is a block b_0..b_{p-1} repeated: position x has
bit b_{x mod p}.  Fixing the (unknown) block bit for residue class r, the
Hamming contribution of all window positions x ≡ r (mod p) is
    (# of 0s in class r) if b_r = 1,  else (# of 1s in class r).
These contributions are INDEPENDENT across residue classes (each class chooses
its own b_r; the block is unconstrained).  So the minimal distance is the
sum over r of min(count0(r), count1(r)), and it is achieved by setting b_r to
the majority bit in class r (ties split either way, same cost):
    dist(p) = sum_{r=0}^{p-1} min( c0(r), c1(r) ).
This is EXACT — coordinate-wise majority over residue classes is the true
Hamming-nearest periodic string, not a heuristic.

VERIFICATION
------------
(1) Reproduce problem.md worked rows A_1, A_2, A_3 from the prime list
    (PASS/FAIL), using lib.gilbreath rows_generator.
(2) Brute-force cross-check of the nearest-periodic shortcut for k=0..2
    (enumerating all 2^p = 2,4,16 blocks) on the n=1e4 window — must agree
    exactly with the per-class-majority formula.

Exact integers throughout.  Sieve O(N log log N), O(N) memory (one bytearray);
per (n,k) counting is O(n).  Total bounded, one row at a time.
"""
import sys, time
from lib.gilbreath import primes_up_to, rows_generator

SIEVE_LIMIT = 16_000_000          # ~1,030,000 primes > max_n=1e6 + 2
NS = [10_000, 100_000, 1_000_000]
KMAX = 6

# --------------------------------------------------------------------------
# 1) SANITY: reproduce problem.md worked rows (PASS/FAIL) from the prime list
# --------------------------------------------------------------------------
def sanity_rows():
    P = primes_up_to(60)
    gen = rows_generator(P, 3)
    next(gen)  # A_0
    A1 = next(gen); A2 = next(gen); A3 = next(gen)
    ok1 = (A1[:10] == [1, 2, 2, 4, 2, 4, 2, 4, 6, 2])
    ok2 = (A2[:9]  == [1, 0, 2, 2, 2, 2, 2, 2, 4])
    ok3 = (A3[:8]  == [1, 2, 0, 0, 0, 0, 0, 2])
    print("SANITY (problem.md rows from prime list):")
    print("  A_1 = %s  -> %s" % (A1[:10], "PASS" if ok1 else "FAIL"))
    print("  A_2 = %s  -> %s" % (A2[:9],  "PASS" if ok2 else "FAIL"))
    print("  A_3 = %s  -> %s" % (A3[:8],  "PASS" if ok3 else "FAIL"))
    allok = ok1 and ok2 and ok3
    print("  overall: %s" % ("PASS" if allok else "FAIL"))
    return allok


# --------------------------------------------------------------------------
# 2) Nearest p-periodic Hamming distance, EXACT via per-class majority
# --------------------------------------------------------------------------
def per_class_counts(window_bits, start_index, p):
    """Count (c0, c1) per residue class mod p over window_bits placed at
    absolute indices start_index, start_index+1, ...."""
    c0 = [0] * p
    c1 = [0] * p
    for off, b in enumerate(window_bits):
        r = (start_index + off) % p
        if b:
            c1[r] += 1
        else:
            c0[r] += 1
    return c0, c1


def nearest_periodic_dist_window(window_bits, start_index, p):
    """Exact Hamming distance of window_bits (at absolute indices
    start_index..) to the nearest p-periodic string.  sum_r min(c0,c1)."""
    c0, c1 = per_class_counts(window_bits, start_index, p)
    return sum(min(c0[r], c1[r]) for r in range(p))


def nearest_periodic_bruteforce(window_bits, start_index, p):
    """Oracle for small p: enumerate all 2^p blocks, min Hamming distance."""
    n = len(window_bits)
    best = None
    for bval in range(1 << p):
        block = [(bval >> r) & 1 for r in range(p)]
        d = sum(1 for off, b in enumerate(window_bits)
                if b != block[(start_index + off) % p])
        if best is None or d < best:
            best = d
    return best


# --------------------------------------------------------------------------
# 3) Main run
# --------------------------------------------------------------------------
def main():
    t0 = time.time()
    if not sanity_rows():
        print("FATAL: worked rows do not reproduce; refusing to run at scale.")
        sys.exit(2)

    print("\nSIEVING to %d ..." % SIEVE_LIMIT)
    P = primes_up_to(SIEVE_LIMIT)
    need = max(NS) + 2
    if len(P) < need:
        print("need %d primes, have %d -> raise SIEVE_LIMIT" % (need, len(P)))
        sys.exit(2)
    print("sieve to %d : %d primes (%.1fs)" % (SIEVE_LIMIT, len(P), time.time() - t0))

    # h[j] = ((p_{j+2} - p_{j+1})//2) % 2  <=>  gap primes[j+1]-primes[j], with
    # primes[0]=p_1=2.  bits[i] is the bit for 1-indexed j = i.
    bits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]

    # Explicit convention statement + first ~20 window bits.
    print("\nCONVENTION:")
    print("  bits[i] = ((primes[i+1]-primes[i])//2) % 2 ;  primes[0]=p_1=2.")
    print("  h[j] = bits[j] for the 1-indexed gap index j (cell ancestor"),
    print("  window is j in [2, n-1] <=> bits[2:n], same as nu2_vs_gap_parity).")
    print("  h[j]=1  <=>  gap p_{j+2}-p_{j+1} == 2 (mod 4).")
    print("  first ~20 window bits h[2]..h[21] = %s" % (bits[2:22]))

    # Brute-force cross-check of the shortcut on the n=1e4 window, k=0..2.
    n_sanity = NS[0]
    win = bits[2:n_sanity]
    print("\nbrute-force oracle check on n=%d window, k=0..2:" % n_sanity)
    allok = True
    for k in range(3):
        p = 1 << k
        maj = nearest_periodic_dist_window(win, 2, p)
        br = nearest_periodic_bruteforce(win, 2, p)
        ok = (maj == br)
        allok &= ok
        print("  k=%d p=%d: per-class=%d brute=%d %s"
              % (k, p, maj, br, "OK" if ok else "MISMATCH"))
    print("brute-force cross-check: %s" % ("ALL MATCH" if allok else "FAILED"))
    if not allok:
        print("FATAL: nearest-periodic shortcut disagrees with brute force.")
        sys.exit(2)

    # Main table.
    print("\nmain results — Hamming distance to nearest 2^k-periodic string,")
    print("over window bits[2:n] (length n-2), reported as dist/n:")
    hdr = "n".ljust(9) + "".join("k=%d".ljust(10) % k for k in range(KMAX + 1))
    print(hdr)
    for n in NS:
        win = bits[2:n]
        L = n - 2
        ones = sum(win)
        w_density = ones / L
        row = str(n).ljust(9)
        for k in range(KMAX + 1):
            p = 1 << k
            d = nearest_periodic_dist_window(win, 2, p)
            row += ("%.4f" % (d / n)).ljust(10)
        print("%s   w/(n-2)=%.4f" % (row, w_density))
        sys.stdout.flush()

    print("\nw(n)/(n-2) is the swap-bit / mod-4-gap density in the ancestor")
    print("window; dist/n is the DPC-prime-antidyadic gap (quantitative")
    print("non-2^k-periodicity of the prime switch bit).  PRIME measurement,")
    print("does NOT close G-supply.")
    print("\nelapsed %.1fs total" % (time.time() - t0))


if __name__ == "__main__":
    main()
