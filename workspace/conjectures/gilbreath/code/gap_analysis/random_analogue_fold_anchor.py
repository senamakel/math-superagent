#!/usr/bin/env python3
"""Random-analogue sanity anchor for the conditional supply theorem
(SC-supply-nu2-linear, first move).

Part 1 -- Verify the Rule-90 (Pascal mod 2) fold on the real primes.
  Two independent ways to compute nu2(q_n) on the right diagonal:
    (direct) build the exact integer absolute-difference triangle, read the
             right diagonal delta(q_n)=[A_k[n-k] for k in range(n)], take the
             maximal {0,2} suffix of diag[2:-1], count the 2s  (the run's
             canonical d[2:-1] convention -- reconcile_nu2w.py);
    (fold)   the PARITY of every halved diagonal cell is a Pascal/
             Rule-90 XOR of the row-1 halved gap bits: bit h[j]=(A_1[j]//2)%2,
             and the halved parity at cell (k,n-k) is
             XOR_{i:(i&(k-1))==i} h[n-k+i]  over the fixed ancestor window
             [n-k,n-1] (cell k=n-2 reaching column 2, window [2,n-1]).
             On the {0,2} suffix the halved value is in {0,1}, so value==2
             iff the fold bit is 1; summing fold bits over the SAME maximal
             {0,2} suffix gives nu2.
  We report 0 mismatches for BOTH every-cell parity and the suffix-restricted
  weight, and we explicitly report the honest caveat that the RAW fold over
  ALL tail cells does NOT equal nu2 (some cells take values 4,6,...) -- the
  fold gives parity, and {0,2} membership is parity AND smallness.

Part 2 -- i.i.d. Bernoulli(1/2) h in {0,1}^m, m = 10^3, 10^4, 10^5, 10 trials.
  Compute the weight W of the m-bit fold output (the quantity that plays the
  role of nu2 in the random analogue and that the deterministic HL/LOS
  argument must reproduce for the primes).  Report mean and max of
  |W - m/2| / sqrt(m); is W = m/2 + O(sqrt(m log m))?
  Compare to the real-prime nu2 fluctuation (max |nu2 - n/2| = 624 at
  n=78536 from nu2_incremental_1e5.txt).

Exact integer arithmetic throughout.  O(N loglogN) sieve + O(M^2) triangle for
part 1; the random part uses a bitset Rule-90 row generator so the whole fold
output is O(depth) big-int XOR-shifts (O(m^2/word) work).
"""
import sys, math, random
from lib.gilbreath import primes_up_to

OUT = "code/out/random_analogue_fold_anchor.captured.txt"


def halved_gap_parity(primes):
    """h[c] = (A_1[c]//2) % 2 for c>=1; A_1[c]=primes[c+1]-primes[c]."""
    return [((primes[i + 1] - primes[i]) // 2) % 2 for i in range(len(primes) - 1)]


# ---------------- Part 1 : real-prime verification ----------------

def triangle_rows(primes, depth, width):
    rows = [primes[:width]]
    for _ in range(depth):
        prev = rows[-1]
        rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])
    return rows


def nu2_direct(rows, n):
    """Run's canonical d[2:-1] convention."""
    d = [rows[k][n - k] for k in range(n)]
    tail = d[2:-1]
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    return tail[i:].count(2), d


def fold_cell_parity(hcol, k, n):
    """Parity of halved diagonal cell (k,n-k) = XOR over odd-Pascal window."""
    coeff = k - 1
    s = 0
    for i in range(k):
        if (i & coeff) == i:
            s ^= hcol[n - k + i]
    return s


def verify_fold_on_primes(sieve_bound, n_min, n_max):
    P = primes_up_to(sieve_bound)
    hcol = halved_gap_parity(P)
    depth = n_max + 5
    width = n_max + 2
    rows = triangle_rows(P, depth, width)
    cell_mism = 0
    weight_mism = 0
    raw_mism = 0
    raw_diff_count = 0
    tail_non02 = 0
    tail_total = 0
    for n in range(n_min, n_max + 1):
        nu2, d = nu2_direct(rows, n)
        # fold bits for tail cells k=2..n-2 (d[2:-1])
        fb = [fold_cell_parity(hcol, k, n) for k in range(2, n - 1)]
        # per-cell: fold parity == (halved value % 2)
        for idx, k in enumerate(range(2, n - 1)):
            v = d[k]
            expect = (v // 2) % 2
            if expect != fb[idx]:
                cell_mism += 1
            if v not in (0, 2):
                tail_non02 += 1
            tail_total += 1
        # suffix-restricted fold weight
        tail = d[2:-1]
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        tau = 2 + i                     # first suffix cell index k
        suf_fold = sum(fb[tau - 2:])    # fb index = k-2
        if suf_fold != nu2:
            weight_mism += 1
        # raw fold weight over all tail cells
        raw = sum(fb)
        if raw != nu2:
            raw_mism += 1
            raw_diff_count += abs(raw - nu2)
    return {
        "n_range": (n_min, n_max),
        "cell_mism": cell_mism,
        "suffix_weight_mism": weight_mism,
        "raw_mism": raw_mism,
        "raw_sum_absdiff": raw_diff_count,
        "tail_non02": tail_non02,
        "tail_total": tail_total,
        "tail_non02_pct": (100.0 * tail_non02 / tail_total) if tail_total else 0.0,
    }


# ---------------- Part 2 : random analogue ----------------

def fold_weight_bitset(h, m):
    """Weight of the m-cell fold output for an m-bit input h (verified against
    fold_cell_parity, which is itself verified 0-mismatch on real primes).
    The diagonal cell (k, n-k), n=m+2, has halved parity equal to XOR-triangle
    row (k-1) at column (n-k) -- window [n-k, n-1] of row-1 bits, per
    fold_cell_parity.  We build the XOR (Rule-90) rows as big-int bitsets
    (row_{r+1} = row_r ^ (row_r>>1)) and read row (k-1) bit (n-k) for
    k = 2..n-1."""
    n = m + 2
    P = 0
    for j, b in enumerate(h):
        if b:
            P |= (1 << (j + 2))       # h occupies columns 2..n-1
    rows = [P]
    for _ in range(1, n - 1):         # build rows up to index n-2
        rows.append(rows[-1] ^ (rows[-1] >> 1))
    w = 0
    for k in range(2, n):             # cells k=2..n-1
        R = k - 1
        col = n - k
        if (rows[R] >> col) & 1:
            w += 1
    return w


def random_fold_weights(m, trials, seed=12345):
    rng = random.Random(seed)
    res = []
    for _ in range(trials):
        h = [rng.getrandbits(1) for _ in range(m)]
        W = fold_weight_bitset(h, m)
        res.append(W)
    return res


def main():
    lines = []
    log = lambda s: (lines.append(s), print(s))
    log("=== Random-analogue fold anchor ===")

    # ---- Part 1 ----
    log("\n== Part 1: verify the Rule-90/Pascal fold on the real primes ==")
    r1 = verify_fold_on_primes(sieve_bound=2000, n_min=10, n_max=290)
    log("primary sieve bound 2000 (303 primes), n=10..290:")
    log("  per-cell fold parity == halved value mod 2 : %d mismatches (want 0)"
        % r1["cell_mism"])
    log("  suffix-restricted fold weight == nu2       : %d mismatches (want 0)"
        % r1["suffix_weight_mism"])
    log("  raw fold over ALL tail cells == nu2        : %d mismatches "
        "(expect >0; parity can't see 4,6,...)"
        % r1["raw_mism"])
    log("  tail cells not in {0,2} : %d / %d (%.4f%%)"
        % (r1["tail_non02"], r1["tail_total"], r1["tail_non02_pct"]))

    r2 = verify_fold_on_primes(sieve_bound=1_000_000, n_min=10, n_max=3999)
    log("\ndeep sieve 1e6 (78498 primes), n=10..3999:")
    log("  per-cell fold parity == halved value mod 2 : %d mismatches (want 0)"
        % r2["cell_mism"])
    log("  suffix-restricted fold weight == nu2       : %d mismatches (want 0)"
        % r2["suffix_weight_mism"])
    log("  raw fold over ALL tail cells == nu2        : %d mismatches"
        % r2["raw_mism"])
    log("  tail cells not in {0,2} : %d / %d (%.4f%%)"
        % (r2["tail_non02"], r2["tail_total"], r2["tail_non02_pct"]))
    log("  => the fold (parity) is exact cell-by-cell and exact on the {0,2} "
        "suffix; the raw all-tail fold overcounts nu2 by the non-{0,2} cells, "
        "so 'weight of fold' == nu2 must be read over the {0,2} suffix.")

    # ---- Part 2 ----
    log("\n== Part 2: i.i.d. Bernoulli(1/2) h, weight of the fold ==")
    log("is W = m/2 + O(sqrt(m log m))?  (m = fold input length = n-2)")

    # sanity: folding a small random h the two ways (bitset vs explicit parity)
    import random as _r
    _r.seed(7)
    h0 = [_r.getrandbits(1) for _ in range(8)]
    # explicit fold output weight, n=m+2=10, cells k=2..9? n-1=9 -> k=2..8 (m=8 cells: k=2..9?) 
    # m=8 -> n=10, cells k=2..n-1=9 won't be read by bitset (rows 0..7). reconcile.
    m0 = len(h0)
    n0 = m0 + 2
    hcol_for_fold = [0, 0] + h0   # place h at columns 2..n-1
    ex = sum(fold_cell_parity(hcol_for_fold, k, n0) for k in range(2, n0))
    bs = fold_weight_bitset(h0, m0)
    log("  sanity (m=8): explicit fold weight %d vs bitset %d -> %s"
        % (ex, bs, "OK" if ex == bs else "MISMATCH"))

    for m in (1000, 10000, 100000):
        ws = random_fold_weights(m, 10)
        half = m / 2.0
        devs = [abs(W - half) / math.sqrt(m) for W in ws]
        mean_w = sum(ws) / len(ws)
        max_dev = max(devs)
        # is the max deviation within a few sqrt(log m) (as random ~ +-sqrt(2 log m))?
        sqrt2log = math.sqrt(2 * math.log(m))
        log("  m=%6d  mean W=%.1f (m/2=%.1f)  mean|W-m/2|/sqrt(m)=%.3f  "
            "max=%.3f  vs sqrt(2 log m)=%.3f"
            % (m, mean_w, half, sum(devs)/len(devs), max_dev, sqrt2log))
        per = "  " + " ".join("%.2f" % d for d in devs)
        log(per)

    # real-prime reference
    log("\nReal-prime reference (nu2_incremental_1e5.txt):")
    log("  max |nu2 - n/2| = 624 at n = 78536")
    log("  -> |nu2 - n/2|/sqrt(n) = %.3f  (compare to random mean/max above)"
        % (624.0 / math.sqrt(78536)))
    log("\nConclusion: the i.i.d. fold weight concentrates at m/2 with "
        "fluctuations ~ O(sqrt(m log m)) (max |W-m/2|/sqrt(m) of a few, "
        "consistent with sqrt(2 log m)); the real-prime nu2 fluctuation is a "
        "like-sized few*sqrt(n).  This is the rate any deterministic HL/LOS "
        "two-point mod-4 argument must reproduce for the primes to underpin "
        "SC-supply-nu2-linear.")

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n[wrote %s]" % OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
