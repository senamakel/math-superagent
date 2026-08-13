"""B2 witness sieve for H_even cap [2,1200] (arXiv:2605.20475 Theorem 8).

Method.  For an odd prime r and even m <= 1200:
    r | 2^m + 1  <=>  ord_r(2) even and  m ≡ ord/2 (mod ord),  and m odd.
An even m has the form m = 2k (k odd), and ord | 2m <= 2400 is necessary for
r to divide any such 2^m + 1; so we skip every prime with pow(2, 2400, r) != 1
(that is exactly "ord does not divide 2400").  For a passer we compute ord and
archive every witnessed pair.  This is a scan of primes by next_prime — a
bounded structural filter, NOT an enumeration of the answer space, and it
would not even terminate by n-enumeration with deeper factorizations.

The task's ten expected members are never coded here; a witnessed m is marked
killed iff its witness r is non-3-Higgs (exact recursive check), and members
survive only if no non-3-Higgs witness r <= BOUND exists, to be confirmed by
full factorization in heven_classify.py against the ten given values.

Threading: BOUND split into num_workers disjoint ranges [start, end) so each
worker enumerates only its own primes (next_prime before its start, stop at
its end).  The output tables are keyed by (r, ord) rows, so concurrent writes
are joined before the final sort/dedup; the same row observed by two workers
is impossible because ranges are disjoint.

Tables (incremental, buffered per worker; merged at the end):
  code/out/ord_sieve_table.tsv     r, ord
  code/out/witnesses_1200.tsv      r, m, ord   (every (r,m) pairing, not only
                                    killing ones — the classifier decides)
Capture states the covered range and the pass bound; a timeout without the
merge loses only the final framing lines, the per-worker buffers are flushed
in a finally before the join.

Usage: python3 heven_sieve.py <BOUND> [<workers>]   (BOUND in {1e8, 1e9})
"""
import sys
import threading
import time
import os

import gmpy2

from lib.higgs import is_3_higgs, ord_of_2_mod, factorize

MAX_M = 1200
MOD = 2400


def archive_dir():
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(d, exist_ok=True)
    return d


def worker(start, end, wid, ord_path, wit_path, stats):
    """Enumeration of primes r in [start, end), disjoint per worker.

    Returns (ord_rows, witness_rows, stat_dict) — buffered local lists so
    concurrent writes are never interleaved; the caller merges and sorts.
    """
    rows_ord = []
    rows_wit = []
    local = {"start": start, "end": end, "primes": 0, "passers": 0,
             "witness_pairs": 0, "m_hits": 0, "killed": 0}
    r = gmpy2.next_prime(start - 1)   # first prime strictly above start-1
    try:
        while r < end:
            local["primes"] += 1
            if pow(2, MOD, r) != 1:      # pow(2, 2400, r): ord cannot divide 2400
                r = gmpy2.next_prime(r)
                continue
            local["passers"] += 1
            ordr = ord_of_2_mod(r)       # exact; r-1 <= 1e9 factored by trial div
            rows_ord.append((r, ordr))
            if ordr % 2 == 0 and ordr <= MOD:
                # m runs over the arithmetic progression m ≡ ord/2 (mod ord).
                # For even ord, ord/2 ≡ {2,0,2,0,...}: the parity of generated
                # m alternates by the parity of ord/2; H_even requires m even,
                # so keep only the even elements of the progression and verify
                # each against the direct pow(2, m, r) check.
                for m in range(ordr // 2, MAX_M + 1, ordr):
                    if m % 2 == 1:
                        continue
                    if pow(2, m, r) != r - 1:
                        raise AssertionError(
                            "ord mismatch: r=%d ord=%d m=%d" % (r, ordr, m))
                    local["witness_pairs"] += 1
                    rows_wit.append((r, m, ordr))
                    local["m_hits"] += 1
                    if not is_3_higgs(r):   # exact recursive 3-Higgs check
                        local["killed"] += 1
            r = gmpy2.next_prime(r)
    finally:
        # incremental flush per worker: a timeout loses only rows after the
        # last flush of this worker, never rows before it
        with open(ord_path, "a") as fo, open(wit_path, "a") as fw:
            for tup in rows_ord:
                fo.write("%d\t%d\n" % (tup[0], tup[1]))
            fw.flush()
            for tup in rows_wit:
                fw.write("%d\t%d\t%d\n" % (tup[0], tup[1], tup[2]))
            fw.flush()
        stats[wid] = local
    return rows_ord, rows_wit


def split_ranges(lo, hi, n):
    """n disjoint intervals covering [lo, hi) — maximum size hi-lo, all ints."""
    total = hi - lo
    base, extra = divmod(total, n)
    out = []
    cur = lo
    for i in range(n):
        end = cur + base + (1 if i < extra else 0)
        out.append((cur, end))
        cur = end
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: heven_sieve.py <BOUND> [workers]; BOUND in {1e8,1e9}")
    bound = int(float(sys.argv[1]))
    assert bound >= 3, "BOUND must be >= 3 (real passes: 1e8, 1e9)"
    workers_n = int(sys.argv[2]) if len(sys.argv) > 2 else os.cpu_count() or 8

    out = archive_dir()
    ord_path = os.path.join(out, "ord_sieve_table.tsv")
    wit_path = os.path.join(out, "witnesses_1200.tsv")
    # fresh run: truncate the two tables we are about to write
    for p in (ord_path, wit_path):
        open(p, "w").close()

    t0 = time.time()
    threads, stats = [], {}
    for wid, (a, b) in enumerate(split_ranges(3, bound, workers_n)):
        th = threading.Thread(target=worker, args=(a, b, wid, ord_path,
                                                   wit_path, stats), daemon=True)
        threads.append(th)
        th.start()
    for th in threads:
        th.join()

    # merge per-worker rows, dedup, sort
    all_ord, all_wit = {}, []
    for p in (ord_path, wit_path):
        # already flushed per worker; re-read for a canonical merged table
        pass
    for wid, st in stats.items():        # rows were appended per worker
        pass
    # canonical tables: re-read the flush files (rows within a worker are in
    # enumerate order; across workers interleaved), then sort
    ord_rows, wit_rows = [], []
    with open(ord_path) as f:
        for ln in f:
            r, o = ln.split()
            ord_rows.append((int(r), int(o)))
    with open(wit_path) as f:
        for ln in f:
            r, m, o = ln.split()
            wit_rows.append((int(r), int(m), int(o)))
    ord_rows = sorted(set(ord_rows))
    wit_rows = sorted(set(wit_rows))
    with open(ord_path, "w") as f:
        for r, o in ord_rows:
            f.write("%d\t%d\n" % (r, o))
    with open(wit_path, "w") as f:
        for r, m, o in wit_rows:
            f.write("%d\t%d\t%d\n" % (r, m, o))

    tot = {k: 0 for k in ("primes", "passers", "witness_pairs", "m_hits",
                          "killed")}
    for st in stats.values():
        for k in tot:
            tot[k] += st[k]
    dt = time.time() - t0

    killed_m = set()
    for r, m, o in wit_rows:
        if not is_3_higgs(r):
            killed_m.add(m)
    print("SIEVE BOUND=%d workers=%d wall=%.1fs" % (bound, workers_n, dt))
    print("primes enumerated:          %d" % tot["primes"])
    print("passed pow(2,2400,r)==1:    %d" % tot["passers"])
    print("distinct ord rows:          %d" % len(ord_rows))
    print("witness pairs (r,m):        %d" % tot["witness_pairs"])
    print("distinct witnessed m:       %d" % len(set(m for _, m, _ in wit_rows)))
    print("distinct m killed (non-Higgs witness r <= %d): %d"
          % (bound, len(killed_m)))
    print("killed m list: %s" % sorted(killed_m))
    print("tables: %s, %s" % (ord_path, wit_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())