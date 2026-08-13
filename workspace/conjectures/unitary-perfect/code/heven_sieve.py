"""B2 witness sieve for H_even cap [2,1200] (arXiv:2605.20475 Theorem 8).

Witness condition (exact).  An odd prime r divides 2^m + 1 for some even
m <= 1200 iff

    ord_r(2) is even,  v2(ord_r(2)) >= 2,  ord_r(2) <= 2400,

and then the witnessed m are exactly m = (ord/2) * s with s odd, m <= 1200
(pow(2, m, r) == r-1 is checked for every archived pair).  Proof sketch:
r | 2^m + 1  <=>  ord | 2m and ord ∤ m  <=>  ord | 2m with v2(ord) = v2(2m);
m even <= 1200 makes 2m a multiple of 4, so the order must be even with
v2(ord) >= 2 and ord <= 2400; conversely m = (ord/2)*odd works.

Enumeration.  Two sweeps, both bounded by the prime bound (not by the answer
space — no enumeration of n, no UPN search):

  * main sweep: enumerate primes r by gmpy2.next_prime; skip unless
    pow(2, 2400, r) == 1  (i.e. ord | 2400); for passers compute ord exactly
    by the divisor chain over factor(r-1).
  * complement sweep: the orders d <= 2400 with v2(d) >= 2 that do NOT divide
    2400 (set D_COMP, 576 values, computed here) can still witness because
    ord | 2m need only divide some 2m, not 2400 itself (e.g. d = 28: r = 29
    divides 2^14 + 1).  For each d in D_COMP enumerate r = 1 + d*t in the
    range, keep r with pow(2, d, r) == 1 (very few: r must divide 2^d - 1),
    certify primality by trial division to sqrt(r), pin the exact order e by
    the divisor chain, and archive witnesses under e (dedup makes sweeps
    disjoint-safe).

Tables (incremental, buffered per worker, merged and deduped at the end):
  code/out/ord_sieve_table.tsv     r<TAB>ord
  code/out/witnesses_1200.tsv      r<TAB>m<TAB>ord     every (r,m) pair, not
                                    only killing ones; heven_classify decides

USAGE (from /workspace):
  python3 code/heven_sieve.py --lo 3 --hi 100000000 --fresh [--workers N]
  python3 code/heven_sieve.py --lo 100000000 --hi 1000000000 [--workers N]

A --fresh run truncates the tables first.  Every run appends its workers'
buffers in a finally block, so a timeout loses only rows after the last flush.
"""
import os
import sys
import threading
import time
from math import isqrt

import gmpy2

from lib.higgs import factorize, is_3_higgs, ord_of_2_mod

MAX_M = 1200
MOD = 2400  # 2 * MAX_M, the largest 2m possible


def trial_division_prime(r):
    """Exact primality certification: trial division to sqrt(r)."""
    r = int(r)
    if r < 2:
        return False
    if r == 2:
        return True
    if r % 2 == 0:
        return False
    d = 3
    while d * d <= r:
        if r % d == 0:
            return False
        d += 2
    return True


def complement_orders():
    """All d with 4 <= d <= 2400, v2(d) >= 2, d not dividing 2400."""
    out = []
    v = 2
    while (1 << v) <= MOD:
        base = 1 << v
        u = 1
        while base * u <= MOD:
            d = base * u
            if MOD % d != 0:
                out.append(d)
            u += 2
        v += 1
    return sorted(out)


def witness_rows(r, ordr):
    """All (r, m, ordr) with even m <= MAX_M, m ≡ ordr/2 (mod ordr).

    Requires ordr even with v2(ordr) >= 2 (then ordr/2 is even and every m in
    the progression is even).  Every row's pow(2, m, r) == r-1 is asserted.
    """
    if ordr % 2 != 0 or ordr % 4 != 0:
        return []
    out = []
    for m in range(ordr // 2, MAX_M + 1, ordr):
        if m % 2 == 1:
            continue
        if pow(2, m, r) != r - 1:
            raise AssertionError("ord mismatch: r=%d ord=%d m=%d" % (r, ordr, m))
        out.append((r, m, ordr))
    return out


def archive_dir():
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(d, exist_ok=True)
    return d


def main_worker(a, b, wid, ord_path, wit_path, stats):
    """Enumerate primes r in [a, b) (disjoint per worker), pow-filter, ord."""
    rows_ord, rows_wit = [], []
    local = {"primes": 0, "passers_main": 0, "pairs": 0, "witnessed_m": set(),
             "killed": set()}
    r = int(gmpy2.next_prime(a - 1 if a > 2 else 1))
    try:
        while r < b:
            local["primes"] += 1
            if pow(2, MOD, r) != 1:
                r = int(gmpy2.next_prime(r))
                continue
            local["passers_main"] += 1
            if not trial_division_prime(r):
                raise AssertionError("next_prime produced composite %d" % r)
            ordr = ord_of_2_mod(r)
            rows_ord.append((r, ordr))
            for tup in witness_rows(r, ordr):
                rows_wit.append(tup)
                local["pairs"] += 1
                local["witnessed_m"].add(tup[1])
                if not is_3_higgs(r):
                    local["killed"].add(tup[1])
            r = int(gmpy2.next_prime(r))
    finally:
        with open(ord_path, "a") as fo, open(wit_path, "a") as fw:
            for r_, o in rows_ord:
                fo.write("%d\t%d\n" % (r_, o))
            for r_, m, o in rows_wit:
                fw.write("%d\t%d\t%d\n" % (r_, m, o))
            fo.flush()
            fw.flush()
        stats[wid] = local


def comp_worker(orders, lo, hi, wid, ord_path, wit_path, stats):
    """For each d in orders: primes r = 1 + d*t in [lo, hi) with exact ord."""
    rows_ord, rows_wit = [], []
    local = {"candidates": 0, "passers_comp": 0, "pairs": 0,
             "witnessed_m": set(), "killed": set()}
    try:
        for d in orders:
            t = max(1, (lo + d - 2) // d)
            t_hi = (hi - 2) // d
            while t <= t_hi:
                r = 1 + d * t
                local["candidates"] += 1
                if pow(2, d, r) != 1:      # ord | d  required
                    t += 1
                    continue
                local["passers_comp"] += 1
                if not trial_division_prime(r):
                    t += 1
                    continue
                e = ord_of_2_mod(r)
                if e != d:                 # exact order handled at e elsewhere
                    t += 1
                    continue
                rows_ord.append((r, e))
                for tup in witness_rows(r, e):
                    rows_wit.append(tup)
                    local["pairs"] += 1
                    local["witnessed_m"].add(tup[1])
                    if not is_3_higgs(r):
                        local["killed"].add(tup[1])
                t += 1
    finally:
        with open(ord_path, "a") as fo, open(wit_path, "a") as fw:
            for r_, o in rows_ord:
                fo.write("%d\t%d\n" % (r_, o))
            for r_, m, o in rows_wit:
                fw.write("%d\t%d\t%d\n" % (r_, m, o))
            fo.flush()
            fw.flush()
        stats[wid] = local


def split_ranges(lo, hi, n):
    """n disjoint intervals covering [lo, hi)."""
    total = hi - lo
    base, extra = divmod(total, n)
    out, cur = [], lo
    for i in range(n):
        end = cur + base + (1 if i < extra else 0)
        out.append((cur, end))
        cur = end
    return out


def balance_orders(orders, lo, hi, n):
    """Assign orders to workers greedily by candidate count (hi-lo)/d."""
    work = sorted((( (hi - lo) // d, d) for d in orders), reverse=True)
    buckets = [0.0] * n
    assigns = [[] for _ in range(n)]
    for w, d in work:
        i = min(range(n), key=lambda j: buckets[j])
        assigns[i].append(d)
        buckets[i] += w
    return assigns


def merge_tables(ord_path, wit_path):
    """Sort + dedup the two tables (idempotent; safe to run repeatedly)."""
    ords = set()
    with open(ord_path) as f:
        for ln in f:
            r, o = ln.split()
            ords.add((int(r), int(o)))
    wits = set()
    with open(wit_path) as f:
        for ln in f:
            r, m, o = ln.split()
            wits.add((int(r), int(m), int(o)))
    with open(ord_path, "w") as f:
        for r, o in sorted(ords):
            f.write("%d\t%d\n" % (r, o))
    with open(wit_path, "w") as f:
        for r, m, o in sorted(wits):
            f.write("%d\t%d\t%d\n" % (r, m, o))
    return ords, wits


def main(argv):
    lo = hi = None
    workers_n = os.cpu_count() or 8
    fresh = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--lo":
            lo = int(argv[i + 1]); i += 2
        elif a == "--hi":
            hi = int(argv[i + 1]); i += 2
        elif a == "--workers":
            workers_n = int(argv[i + 1]); i += 2
        elif a == "--fresh":
            fresh = True; i += 1
        else:
            sys.exit("unknown arg %s" % a)
    if lo is None or hi is None or hi <= lo:
        sys.exit("usage: heven_sieve.py --lo L --hi H [--fresh] [--workers N]")

    out = archive_dir()
    ord_path = os.path.join(out, "ord_sieve_table.tsv")
    wit_path = os.path.join(out, "witnesses_1200.tsv")
    if fresh:
        open(ord_path, "w").close()
        open(wit_path, "w").close()

    # merge leftover rows from a previous interrupted run before appending
    if os.path.getsize(ord_path) or os.path.getsize(wit_path):
        merge_tables(ord_path, wit_path)

    t0 = time.time()
    threads, stats = [], {}
    for wid, (a, b) in enumerate(split_ranges(lo, hi, workers_n)):
        th = threading.Thread(target=main_worker, args=(
            a, b, wid, ord_path, wit_path, stats), daemon=True)
        threads.append(th); th.start()
    comp_orders = complement_orders()
    assigns = balance_orders(comp_orders, lo, hi, workers_n)
    for wid in range(workers_n):
        th = threading.Thread(target=comp_worker, args=(
            assigns[wid], lo, hi, workers_n + wid, ord_path, wit_path, stats),
            daemon=True)
        threads.append(th); th.start()
    for th in threads:
        th.join()

    ords, wits = merge_tables(ord_path, wit_path)
    dt = time.time() - t0

    tot = {"primes": 0, "passers_main": 0, "candidates": 0,
           "passers_comp": 0, "pairs": 0}
    wm = set(); killed = set()
    for st in stats.values():
        tot["primes"] += st.get("primes", 0)
        tot["passers_main"] += st.get("passers_main", 0)
        tot["candidates"] += st.get("candidates", 0)
        tot["passers_comp"] += st.get("passers_comp", 0)
        tot["pairs"] += st["pairs"]
        wm |= st["witnessed_m"]
        killed |= st["killed"]
    # authoritative killed set from merged table (same is_3_higgs test)
    killed = set()
    for r, m, o in wits:
        if not is_3_higgs(r):
            killed.add(m)
    killed_list = sorted(killed)

    print("SIEVE range [%d, %d) workers=%d wall=%.1fs"
          % (lo, hi, workers_n, dt))
    print("main sweep: primes enumerated %d, pow(2,2400,r)==1 passers %d"
          % (tot["primes"], tot["passers_main"]))
    print("complement sweep: candidates %d, pow(2,d,r)==1 passers %d"
          % (tot["candidates"], tot["passers_comp"]))
    # note: passers_comp counts both sweeps' 'passers' key; fix by separate key
    print("distinct ord rows (merged):   %d" % len(ords))
    print("witness pairs (merged):       %d" % len(wits))
    print("distinct witnessed m:         %d" % len(wm))
    print("distinct m killed (non-Higgs witness r in range): %d"
          % len(killed_list))
    print("killed m: %s" % killed_list)
    print("tables: %s\n        %s" % (ord_path, wit_path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))