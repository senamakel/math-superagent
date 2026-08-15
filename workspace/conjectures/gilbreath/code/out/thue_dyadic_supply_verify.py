#!/usr/bin/env python3
"""Exact-integer verification of the Thue-Morse subset-zeta claim and the
corner-family supply tabulation adopted as `dyadic-linear-complexity-supply`.

PART A -- Thue-Morse subset-zeta identity (never machine-checked):
  h[j] = wt(j) mod 2.  zeta(h)[d] = XOR over submasks j of d of h[j] (mod 2).
  Claim: zeta(h)[d] == 1  <=>  d is a power of two (exactly one set bit).
  This tests  sum_{j subseteq d} wt(j) = wt(d) * 2^{wt(d)-1}  (mod 2).
  The F2 fast subset-zeta transform is O(N log N) with integer bitmath.

PART B -- load-bearing identification check:
  Build 2-then-odds q: q[0]=2, q[1]=3, gap q[j+2]-q[j+1] = 2 if h[j]=1 else 4
  (h = Thue-Morse).  Iterate the absolute-difference triangle exactly to depth
  D=4000, one row at a time.  At each depth n compute nu2(n) = # 2s in the
  maximal {0,2} suffix of the right diagonal delta(q_n), using the run's
  canonical convention (lib.rightdiag.cycle_and_nu2: body diag[:-1], suffix
  floored at index 2).  Compare nu2(n) with #{d <= n : d is a power of two}.
  If they do NOT match, report the first mismatch n with both values.

PART C -- corner-family density table:
  For each of 10 halved-gap bit families extended to length N=200000, compute
  density(zeta(h)) = #{d<=N : zeta(h)[d]=1}/N via the O(N log N) submask
  transform (integer bitmath), and report exact counts and densities.

No floats in any core computation (densities are reported as exact rationals
count/N alongside a decimal for legibility).
"""
import time
from math import isqrt


# --------------------------------------------------------------------------
# PART A / shared: F2 subset-zeta transform, O(N log N), integer bitmath.
# --------------------------------------------------------------------------
def subset_zeta(h):
    """h: list of 0/1 over indices 0..len-1.  Returns zeta[d] = XOR_{j submask
    of d} h[j] (mod 2), computed by the F2 fast zeta (subset-sum) transform.
    zeta[m] initially h[m]; for each bit b, zeta[m] ^= zeta[m ^ (1<<b)] for all
    m with bit b set."""
    N = len(h)
    z = list(h)  # must be 0/1
    b = 1
    while b < N:
        step = b << 1
        for start in range(0, N, step):
            for m in range(start + b, min(start + step, N)):
                z[m] ^= z[m - b]
        b <<= 1
    return z


def pw2_set(N):
    """Set of powers of two in 1..N (inclusive)."""
    s = set()
    p = 1
    while p <= N:
        s.add(p)
        p <<= 1
    return s


def wt(x):
    return bin(x).count("1")


def thue_morse(j):
    return wt(j) & 1


# --------------------------------------------------------------------------
# PART A
# --------------------------------------------------------------------------
def part_a(N=100000):
    t0 = time.time()
    h = [thue_morse(j) for j in range(N + 1)]
    z = subset_zeta(h)
    ones = [d for d in range(N + 1) if z[d] == 1]
    pw2 = pw2_set(N)
    correct = (set(ones) == pw2)
    mism = sorted(set(ones) ^ pw2)
    print("PART A — Thue-Morse subset-zeta identity, N=%d" % N)
    print("  # d in 0..N with zeta(h)[d]==1 : %d" % len(ones))
    print("  # powers of two in 1..N      : %d" % len(pw2))
    print("  zeta==1 set == power-of-two set : %s" % correct)
    print("  mismatches (zeta==1 but not pw2, or pw2 but zeta==0): %s"
          % (mism if mism else "none"))
    if not mismatch_first_element(ones, pw2):
        print("  -> CONFIRMED: zeta(h)[d]==1 <=> d is a power of two.")
    print("  time %.2fs" % (time.time() - t0))
    return ones


def mismatch_first_element(ones, pw2):
    return sorted(set(ones) ^ pw2) != []


# --------------------------------------------------------------------------
# PART B
# --------------------------------------------------------------------------
def part_b(D=4000, samples=(100, 500, 1000, 2000, 4000)):
    t0 = time.time()
    # build q sequence: q[0]=2, q[1]=3, gap q[j+2]-q[j+1] = 2 if h[j]=1 else 4
    q = [2, 3]
    for j in range(D + 2):
        q.append(q[-1] + (2 if thue_morse(j) else 4))
    # q must have length > D;  delta(q_n) needs q[0..n].
    assert len(q) > D + 2

    # incremental right-diagonal, one n at a time (O(N^2) diffs, O(N) mem).
    def incremental_diagonals(seq):
        D0 = [seq[0]]
        yield D0
        for n in range(1, len(seq)):
            nd = [0] * (n + 1)
            nd[0] = seq[n]
            for k in range(1, n + 1):
                nd[k] = abs(nd[k - 1] - D0[k - 1])
            D0 = nd
            yield D0

    def cycle_and_nu2(diag):
        """Canonical: maximal {0,2} suffix of body diag[:-1] floored at index 2
        (matches lib.rightdiag.cycle_and_nu2)."""
        body = diag[:-1]
        i = len(body)
        while i > 2 and body[i - 1] in (0, 2):
            i -= 1
        return body[i:].count(2)

    pw2_sets = {n: len(pw2_set(n)) for n in samples}
    pw2_set_full = pw2_set(D)

    results = {}
    first_mismatch = None
    yielder = incremental_diagonals(q)
    for n in range(0, D + 1):
        dd = next(yielder)
        nu2 = cycle_and_nu2(dd)
        if n in samples:
            pc = len(pw2_set_full & set(range(1, n + 1)))
            results[n] = (nu2, pc)
        # first-mismatch tracking over all n
        if first_mismatch is None and n >= 1:
            actual_pc = len([p for p in range(1, n + 1) if p & (p - 1) == 0])
            if nu2 != actual_pc:
                first_mismatch = (n, nu2, actual_pc)
    # For n in samples we recomputed pc; fine.
    print("PART B — identification check, D=%d (2-then-odds from Thue-Morse)" % D)
    print("  n       nu2(n)   #powers-of-two<=n   match")
    allm = True
    for n, (nu2v, pc) in results.items():
        m = (nu2v == pc)
        allm &= m
        print("  %-6d %-8d %-18d %s" % (n, nu2v, pc, "YES" if m else "NO"))
    if allm:
        print("  -> CONFIRMED on all samples: nu2(n) == #{powers of two <= n}.")
    # overall first mismatch over ALL n in 1..D
    # recompute cleanly over all n (the loop above already tracked for n>=1)
    if first_mismatch is not None:
        print("  FIRST MISMATCH over all n in 1..D: n=%d, nu2=%d, "
              "#pw2=%d  => IDENTIFICATION REFUTED" % first_mismatch)
    else:
        print("  No mismatch over ANY n in 1..%d  => full-range CONFIRMED" % D)
    print("  time %.2fs" % (time.time() - t0))
    return results, first_mismatch


# --------------------------------------------------------------------------
# PART C families
# --------------------------------------------------------------------------
def fam_zeros(N):
    return [0] * (N + 1)


def fam_ones(N):
    return [1] * (N + 1)


def fam_alt01(N):
    return [j & 1 for j in range(N + 1)]


def fam_period4_0011(N):
    return [1 if (j % 4) in (2, 3) else 0 for j in range(N + 1)]


def fam_period3(N):
    return [1 if (j % 3) == 1 else 0 for j in range(N + 1)]


def fam_period5(N):
    return [1 if (j % 5) in (1, 4) else 0 for j in range(N + 1)]


def fam_thuemorse(N):
    return [wt(j) & 1 for j in range(N + 1)]


def fam_rudinshapiro(N):
    """r(j) = # occurrences of substring '11' in binary expansion of j, mod 2.
    Recurrence: r(2n)=r(n); r(2n+1)=r(n)+[n odd].  h = r mod 2."""
    r = [0] * (N + 1)
    for j in range(1, N + 1):
        if j & 1:
            n = j >> 1
            r[j] = r[n] + (1 if (n & 1) else 0)
        else:
            r[j] = r[j >> 1]
    return [v & 1 for v in r]


def fam_lcg(N, a=1103515245, c=12345, mod=1 << 31, seed=1):
    x = seed
    out = []
    for _ in range(N + 1):
        out.append((x >> 30) & 1)      # top bit
        x = (a * x + c) % mod
    return out


def fam_prime_switch(N):
    """h[j] = [(p_{j+2} - p_{j+1})/2 mod 2] for j=0..N-1.  Sieve enough primes."""
    # need primes[j] for j up to N+1;  the (N+1)-th prime is ~ N log N.
    limit = 8 * max(100, N)   # generous: pi(8N) > N for N=200000
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i::i] = b"\x00" * (((limit - i*i) // i) + 1)
    pr = [i for i in range(2, limit + 1) if sieve[i]]
    assert len(pr) >= N + 2, "need %d primes, have %d" % (N + 2, len(pr))
    h = [((pr[j + 2] - pr[j + 1]) // 2) & 1 for j in range(N + 1)]
    return h


FAMILIES = [
    ("1 all-zeros", fam_zeros),
    ("2 all-ones", fam_ones),
    ("3 alternating 0,1", fam_alt01),
    ("4 period4 0,0,1,1", fam_period4_0011),
    ("5 period3 0,1,0", fam_period3),
    ("6 period5", fam_period5),
    ("7 Thue-Morse", fam_thuemorse),
    ("8 Rudin-Shapiro (11-substr mod2)", fam_rudinshapiro),
    ("9 LCG pseudo-random", fam_lcg),
    ("10 real prime switch bit", fam_prime_switch),
]


def part_c(N=200000):
    t0 = time.time()
    print("PART C — corner-family density table, N=%d" % N)
    print("  %-30s %12s %10s   %s" % ("family", "count zeta=1", "density",
                                      "class"))
    rows = []
    for name, fn in FAMILIES:
        tf = time.time()
        h = fn(N)
        z = subset_zeta(h)
        cnt = sum(1 for d in range(N + 1) if z[d] == 1)
        dens = cnt / (N + 1)          # count over d=0..N
        # exact rational
        from fractions import Fraction
        f = Fraction(cnt, N + 1)
        # classify
        if cnt == 0:
            cls = "{0}"
        elif f.numerator >= 1 and cnt * 20 >= (N + 1):   # density >= 1/20
            cls = "{>=c>0}"
        else:
            cls = "intermediate (0<dens, not clearly bounded below)"
        rows.append((name, cnt, dens, str(f), cls))
        print("  %-30s %12d %10.6f (%s)  %s  [%s]"
              % (name, cnt, dens, str(f), cls, "%.1fs" % (time.time() - tf)))
    print("  time %.2fs" % (time.time() - t0))
    return rows


def main():
    print("=" * 78)
    print("Thue-Morse subset-zeta + corner-family supply tabulation "
          "(exact ints)")
    print("=" * 78)
    part_a(N=100000)
    print()
    part_b(D=4000)
    print()
    part_c(N=200000)


if __name__ == "__main__":
    main()
