#!/usr/bin/env python3
"""DPC-prime-antidyadic anchor.

Question: is the prime mod-4 switch bit h[j] = ((p_{j+2}-p_{j+1})//2) mod 2
(1 iff consecutive odd primes differ by 2 mod 4) asymptotically FAR from
every 2^k-periodic string?

We measure, for n in {1e5,2e5,5e5,1e6} and k in 0..6, the Hamming distance
between h[0:n] and its NEAREST 2^k-periodic string, as a fraction distance/n.

The Hamming distance to a periodic string decomposes independently over the
2^k residue classes mod 2^k: positions i ≡ r (mod 2^k) all need the same bit,
and the optimal choice is the majority bit in that class.  Hence coordinate-
wise MAJORITY gives the EXACT Hamming-nearest periodic string for every k
(it is not a heuristic).  Per class of size m_r the best we can do is
m_r - max(#0,#1) mismatches; summing over classes gives distance.

Expectation / claim: distance/n stays near 0.4-0.6 and never tends to 0 for
any k.  (For uncorrelated bits, each class of ~n/2^k bits leaves ~half
mismatched, and with 2^k classes the total is ~n/2.)  A distance/n -> 0 for
any k would empirically refute DPC-prime-antidyadic.

Sanity cross-check: for k = 0,1,2 the majority answer is compared to true
brute-force enumeration over all 2^(2^k) blocks (2,4,16 blocks) — the two
must agree exactly.

Exact integers throughout.  One row at a time, O(16e6) sieve memory.
"""
import sys, time
from math import isqrt

SIEVE_LIMIT = 16_000_000
NS = [100_000, 200_000, 500_000, 1_000_000]
KMAX = 6

t0 = time.time()
sieve = bytearray(b"\x01") * (SIEVE_LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(SIEVE_LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((SIEVE_LIMIT - i * i) // i) + 1)
primes = [i for i in range(2, SIEVE_LIMIT + 1) if sieve[i]]
print("sieve to %d : %d primes (%.1fs)" % (SIEVE_LIMIT, len(primes), time.time() - t0))

need = max(NS) + 2
if len(primes) < need:
    print("need %d primes, have %d -> raise SIEVE_LIMIT" % (need, len(primes)))
    sys.exit(2)

# h[j] for j=0.. : between p_{j+1} and p_{j+2} (0-indexed into primes)
bits = [(p2 - p1) // 2 % 2 for p1, p2 in zip(primes, primes[1:])]
print("switch-bit prefix available: %d bits (%.1fs)" % (len(bits), time.time() - t0))


def nearest_periodic_majority(seq, p):
    """Exact Hamming distance of seq (length n) to nearest p-periodic string,
    via coordinate-wise majority over residue classes mod p.  Returns
    (distance, block, per-class-optimal)."""
    n = len(seq)
    cnt0 = [0] * p
    cnt1 = [0] * p
    for j, b in enumerate(seq):
        r = j % p
        if b:
            cnt1[r] += 1
        else:
            cnt0[r] += 1
    dist = 0
    block = []
    for r in range(p):
        if cnt1[r] >= cnt0[r]:
            dist += cnt0[r]
            block.append(1)
        else:
            dist += cnt1[r]
            block.append(0)
    return dist, block


def nearest_nonconstant_periodic_majority(seq, p):
    """Exact Hamming distance to the nearest p-periodic string whose block is
    NOT constant (at least one bit differs from the rest).  When the plain
    majority gives a constant block (all-0 or all-1), we force one class to
    take its minority bit, choosing the class where that costs least.
    Returns (distance, block)."""
    n = len(seq)
    cnt0 = [0] * p
    cnt1 = [0] * p
    for j, b in enumerate(seq):
        r = j % p
        if b:
            cnt1[r] += 1
        else:
            cnt0[r] += 1
    dist = 0
    block = []
    for r in range(p):
        if cnt1[r] >= cnt0[r]:
            dist += cnt0[r]
            block.append(1)
        else:
            dist += cnt1[r]
            block.append(0)
    n0 = block.count(0)
    n1 = p - n0
    if n0 == p or n1 == p:
        # constant block: force one class to its minority bit, cheapest one.
        # Switching class r from majority to minority adds
        #   majority - minority = |cnt1[r] - cnt0[r]|
        # to the distance; the cheapest single class is globally optimal by
        # non-negativity (flipping more only adds more, and p>1).
        best_extra = None
        for r in range(p):
            extra = abs(cnt1[r] - cnt0[r])
            if best_extra is None or extra < best_extra:
                best_extra = extra
        dist += best_extra
    return dist, block


def nearest_periodic_bruteforce(seq, p):
    """Exact nearest p-periodic Hamming distance by enumerating all 2^p blocks.
    Only for small p (verification of the majority shortcut)."""
    n = len(seq)
    best = None
    for bval in range(1 << p):
        block = [(bval >> r) & 1 for r in range(p)]
        d = sum(1 for j in range(n) if seq[j] != block[j % p])
        if best is None or d < best[0]:
            best = (d, block)
    return best[0], best[1]


def brute_check(seq, p):
    dm, bm = nearest_periodic_majority(seq, p)
    db, bb = nearest_periodic_bruteforce(seq, p)
    ok = (dm == db and bm == bb)
    print("   sanity k=%d (p=%d, 2^p=%d blocks): majority=%d brute=%d match=%s"
          % (p.bit_length() - 1 if p > 1 else 0, p, 1 << p, dm, db, ok))
    return ok


# ---- small-k brute-force sanity cross-check on the first n ----
sanity_n = NS[0]
s_allok = True
for k in range(3):                      # k=0 (p=1), k=1 (p=2), k=2 (p=4)
    seq = bits[:sanity_n]
    if not brute_check(seq, 1 << k):
        s_allok = False
print("brute-force cross-check (k=0..2) all match:", s_allok)

# ---- main table ----
print()
print("Hamming distance of switch-bit prefix to nearest 2^k-periodic string")
print(" (%d bits)" % len(bits))
print("n-values: %s ; exact via coordinate-wise majority for all k" % NS)
header = "n".ljust(10) + "".join("k=%d".ljust(14) % k for k in range(KMAX + 1))
print(header)
print("(columns A = nearest periodic, exact; bias-corrected B = nearest")
print(" NON-constant periodic, also exact — the all-zero collapse removed)")
for n in NS:
    seq = bits[:n]
    ones = sum(seq)
    density = ones / n
    row = str(n).ljust(10)
    driftA = ""   # skip for header alignment; print under
    for k in range(KMAX + 1):
        p = 1 << k
        d, _ = nearest_periodic_majority(seq, p)
        if k >= 1:
            dn, _ = nearest_nonconstant_periodic_majority(seq, p)
            row += ("A:%.4f/B:%.4f" % (d / n, dn / n)).ljust(20)
        else:
            row += ("A:%.4f   (B n/a)" % (d / n)).ljust(20)
    print("%-10s %s" % (n, row))
    sys.stdout.flush()

print("elapsed %.1fs total" % (time.time() - t0))
