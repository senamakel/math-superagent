#!/usr/bin/env python3
"""FINAL exact-integer verification.
Cross-checks every component against an independent naive route, then runs the
three parts.  PART B reports the load-bearing identification outcome.
"""
import time
from math import isqrt
from fractions import Fraction

from lib.gilbreath import rows_generator
from lib.rightdiag import cycle_and_nu2, delta_diagonal


def wt(x):
    return bin(x).count("1")


def thue(j):
    return wt(j) & 1


# ---- subset-zeta: fast O(N log N) bitmath ----
def subset_zeta(h):
    N = len(h)
    z = list(h)
    b = 1
    while b < N:
        step = b << 1
        for start in range(0, N, step):
            for m in range(start + b, min(start + step, N)):
                z[m] ^= z[m - b]
        b <<= 1
    return z


# ---- naive subset-zeta: O(N * 2^wt) double loop, for cross-check ----
def subset_zeta_naive(h):
    N = len(h)
    z = [0] * N
    for d in range(N):
        s = 0
        j = d
        while True:
            s ^= h[j]
            if j == 0:
                break
            j = (j - 1) & d
        z[d] = s
    return z


# ==================== PART A ====================
def part_a():
    N = 100000
    t0 = time.time()
    h = [thue(j) for j in range(N + 1)]
    z = subset_zeta(h)

    # cross-check fast vs naive on a small slice
    zs = subset_zeta_naive([thue(j) for j in range(4096)])
    zf = subset_zeta([thue(j) for j in range(4096)])
    naive_ok = (zs == zf)

    ones = sorted(d for d in range(N + 1) if z[d] == 1)
    pw = sorted(p for p in range(1, N + 1) if p & (p - 1) == 0)
    ok = (ones == pw)
    print("PART A — Thue-Morse subset-zeta identity, N=%d" % N)
    print("  fast-vs-naive transform agree (N=4096) : %s" % naive_ok)
    print("  # d in 0..N with zeta==1               : %d" % len(ones))
    print("  # powers of two in 1..N                : %d" % len(pw))
    print("  sets identical                         : %s" % ok)
    # cleaner direct identity check on small d
    ident_ok = True
    for d in range(1, 700):
        sm = [j for j in range(d + 1) if (j & d) == j]
        lhs = sum(wt(j) for j in sm) & 1
        # zeta value = lhs mod 2 (h[j]=wt(j)%2 => XOR of wt(j) parities == sum mod 2)
        zetaval = sum(wt(j) & 1 for j in sm) & 1
        # integer identity: wt(d)*2^{wt(d)-1}
        rhs = (wt(d) * (1 << (wt(d) - 1))) & 1
        zepid = d & (d - 1) == 0 and d != 0
        if not (zetaval == lhs == rhs == (1 if zepid else 0)):
            ident_ok = False
            print("   identity check FAIL at d=", d)
            break
    print("  popcount-subset-sum identity (d<=699)   : %s" % ident_ok)
    print("  -> PART A " + ("CONFIRMED" if ok else "FAILED"))
    print("  time %.2fs" % (time.time() - t0))
    return ok


def submasks(d):
    out = []
    j = d
    while True:
        out.append(j)
        if j == 0:
            break
        j = (j - 1) & d
    return out


def bitsubmasks(d):
    return submasks(d)


# ==================== PART B ====================
def part_b(D=4000, samples=(100, 500, 1000, 2000, 4000)):
    t0 = time.time()
    q = [2, 3]
    for j in range(D + 2):
        q.append(q[-1] + (2 if thue(j) else 4))

    # cross-check triangle against lib.gilbreath.rows_generator
    rows_lib = list(rows_generator(q, 5))
    rows_mine = []
    cur = list(q)
    rows_mine.append(cur)
    for _ in range(5):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        rows_mine.append(cur)
    tri_ok = (rows_lib == rows_mine)

    # cross-check incremental diag + canonical nu2 against lib.rightdiag
    D0 = [q[0]]
    diags = [D0]
    for n in range(1, D + 1):
        nd = [0] * (n + 1)
        nd[0] = q[n]
        for k in range(1, n + 1):
            nd[k] = abs(nd[k - 1] - D0[k - 1])
        D0 = nd
        diags.append(D0)

    def canon_nu2(d):
        body = d[:-1]
        i = len(body)
        while i > 2 and body[i - 1] in (0, 2):
            i -= 1
        return body[i:].count(2)

    # verify a few against lib
    lib_ok = True
    for n in (5, 10, 50, 100):
        if canon_nu2(diags[n]) != cycle_and_nu2(diags[n])[1]:
            lib_ok = False
            break
        # also cross-check the diagonal itself
        if delta_diagonal(q, n) != diags[n]:
            lib_ok = False
            break

    # nu2 at samples and full first-mismatch
    results = {}
    first_mism = None
    for n in range(1, D + 1):
        nu2 = canon_nu2(diags[n])
        pw = len([p for p in range(1, n + 1) if p & (p - 1) == 0])
        if n in samples:
            results[n] = (nu2, pw)
        if first_mism is None and nu2 != pw:
            first_mism = (n, nu2, pw)
    # special n=0: nu2=0, pw=0
    n0 = (canon_nu2(diags[0]), 0)

    print("PART B — identification nu2(n)==#{powers of two<=n}, D=%d" % D)
    print("  triangle matches lib.gilbreath.rows_generator : %s" % tri_ok)
    print("  diag+nu2 match lib.rightdiag                  : %s" % lib_ok)
    print("  n=0: nu2=%d, #pw2=0" % n0[0])
    print("  %-6s %-8s %-18s %s" % ("n", "nu2(n)", "#pw2<=n", "match"))
    allm = True
    for n, (nu2, pw) in results.items():
        m = (nu2 == pw)
        allm &= m
        print("  %-6d %-8d %-18d %s" % (n, nu2, pw, "YES" if m else "NO"))
    print("  all samples match : %s" % allm)
    if first_mism is not None:
        print("  FIRST MISMATCH n=%d: nu2=%d vs #pw2=%d -> IDENTIFICATION "
              "REFUTED" % first_mism)
    else:
        print("  no mismatch in 1..%d -> full-range CONFIRMED" % D)
    print("  time %.2fs" % (time.time() - t0))
    return results, first_mism, tri_ok, lib_ok


# ==================== PART C ====================
def fam_zeros(N):    return [0] * (N + 1)
def fam_ones(N):     return [1] * (N + 1)
def fam_alt01(N):    return [j & 1 for j in range(N + 1)]
def fam_p4(N):       return [1 if (j % 4) in (2, 3) else 0 for j in range(N + 1)]
def fam_p3(N):       return [1 if (j % 3) == 1 else 0 for j in range(N + 1)]
def fam_p5(N):       return [1 if (j % 5) in (1, 4) else 0 for j in range(N + 1)]
def fam_tm(N):       return [wt(j) & 1 for j in range(N + 1)]


def fam_rudinshapiro(N):
    r = [0] * (N + 1)
    for j in range(1, N + 1):
        if j & 1:
            n = j >> 1
            r[j] = r[n] + (1 if (n & 1) else 0)
        else:
            r[j] = r[j >> 1]
    return [v & 1 for v in r]


def fam_lcg(N, a=1103515245, c=12345, m=1 << 31, seed=1):
    x = seed
    out = []
    for _ in range(N + 1):
        out.append((x >> 30) & 1)
        x = (a * x + c) % m
    return out


def fam_primeswitch(N):
    # need N+2 primes; pi(x) ~ x/log x, take limit = 32*N (very generous,
    # pi(32N) >> N for N=2e5)
    limit = 32 * N + 1000
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i::i] = b"\x00" * (((limit - i*i) // i) + 1)
    pr = [i for i in range(2, limit + 1) if sieve[i]]
    assert len(pr) >= N + 2, "need %d primes, have %d (limit=%d)" % (
        N + 2, len(pr), limit)
    return [((pr[j + 2] - pr[j + 1]) // 2) & 1 for j in range(N + 1)]


FAMILIES = [
    ("1 all-zeros", fam_zeros),
    ("2 all-ones", fam_ones),
    ("3 alternating 0,1", fam_alt01),
    ("4 period4 0,0,1,1", fam_p4),
    ("5 period3 0,1,0", fam_p3),
    ("6 period5", fam_p5),
    ("7 Thue-Morse", fam_tm),
    ("8 Rudin-Shapiro (11-substr mod2)", fam_rudinshapiro),
    ("9 LCG pseudo-random", fam_lcg),
    ("10 real prime switch bit", fam_primeswitch),
]


def part_c(N=200000):
    t0 = time.time()
    print("PART C — corner-family density table, N=%d (d in 0..N, denom=%d)"
          % (N, N + 1))
    print("  %-28s %12s %12s  %s" % ("family", "count zeta=1",
                                     "density", "class"))
    rows = []
    for name, fn in FAMILIES:
        tf = time.time()
        h = fn(N)
        z = subset_zeta(h)
        cnt = sum(1 for d in range(N + 1) if z[d] == 1)
        f = Fraction(cnt, N + 1)
        if cnt == 0:
            cls = "{0}"
        elif cnt * 20 >= (N + 1):
            cls = "{>=c>0}"
        else:
            cls = "intermediate (0<dens, no clear lower bound)"
        rows.append((name, cnt, f, cls))
        print("  %-28s %12d %12s  %s  [%.1fs]"
              % (name, cnt, str(f), cls, time.time() - tf))
    print("  time %.2fs" % (time.time() - t0))
    return rows


def main():
    print("=" * 78)
    print("Thue-Morse subset-zeta + corner-family supply tabulation "
          "(exact ints)")
    print("=" * 78)
    part_a()
    print()
    part_b()
    print()
    part_c()


if __name__ == "__main__":
    main()
