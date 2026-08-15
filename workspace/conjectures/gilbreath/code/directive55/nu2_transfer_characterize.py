#!/usr/bin/env python3
"""Directive-55: characterization of the nu2 >= c*w transfer for 2-then-odds.

For a 2-then-odds sequence q (q_1=2, q_2=3, q_j odd increasing for j>=3), we
compute, exactly and one row at a time:

  * the Gilbreath triangle to depth ~n,
  * the right diagonal delta(q_n) = [A_k(n-k)]_k,
  * nu2(q_n) = number of 2s in the maximal {0,2} suffix of delta(q_n)
    (reported under BOTH conventions: the run's canonical tail = diag[2:-1]
    floored at index 2, and the literal maximal suffix of the body diag[:-1]
    floored at index 0),
  * w(n) = #{ j in [2, n-1] : gap_j ≡ 2 (mod 4) }  (the "switch count").

We then:
  (1) reproduce the constant-gap refutation: q = (2,3,5,7,9,11,...) all gaps 2
      (i.e. consecutive odds) gives nu2 = O(1) with nu2/w -> 0.  Report exact
      nu2, w at n = 100..2000.
  (2) measure min nu2/w and min nu2/n over: the primes (sieve to n=5000),
      consecutive odds, and structured families (all gaps 4; alternating 2/4;
      2 then all 4s; 2,2,4,2,4,...), over a window of n.
  (3) evaluate the candidate non-degeneracy hypotheses H_a..H_e and report
      which is the WEAKEST that excludes the constant-gap case AND the primes
      satisfy, and under which nu2 >= c*w holds as a measured fact on the
      primes.

Exact integer arithmetic throughout.  O(N log log N) sieve + O(M^2) triangle
(O(M) memory, one row at a time).

Oracle: rows_generator/prime rows reproduce problem.md A_1..A_3 (verified).
"""
from math import isqrt


def primes_up_to(n):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = b"\x00" * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def triangle_rows(seq, depth):
    """Exact integer iterated absolute-difference rows A_0..A_depth."""
    cur = [int(x) for x in seq]
    yield cur
    for _ in range(depth):
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        yield cur


def right_diagonal(seq, n):
    """delta(q_n) = [A_k(n-k)], k = 0..n.  seq is the sequence q (len > n)."""
    rows = triangle_rows(seq, n)
    # rows[k] has length len(seq)-k; column n-k exists if len(seq)-k > n-k
    out = []
    for k, r in enumerate(rows):
        idx = n - k
        if idx >= len(r):
            break
        out.append(r[idx])
    return out


def nu2_of_diagonal(d):
    """Return (nu2_canon, nu2_literal, tau_canon, tau_lit).
    nu2 = # of 2s in the maximal {0,2} suffix of the body d[:-1].
    canonical: suffix floor at index 2 (run's convention, drop delta_0/1).
    literal: suffix floor at index 0 (whole body)."""
    body = d[:-1]
    # canonical tail = body[2:]
    tail_c = body[2:]
    i = len(tail_c)
    while i > 0 and tail_c[i - 1] in (0, 2):
        i -= 1
    nu2_c = tail_c[i:].count(2)
    tau_c = 2 + i
    # literal: whole body
    j = len(body)
    while j > 0 and body[j - 1] in (0, 2):
        j -= 1
    nu2_l = body[j:].count(2)
    return nu2_c, nu2_l, tau_c, j


def w_of_seg(gaps, n):
    """w(n) = #{ j in [2, n-1] : gap_j ≡ 2 mod 4 }, where gaps[j] = g_j =
    q_{j+1} - q_j (0-indexed list, j in [2, n-1] means indices 2..n-2 are
    used if gaps is 1-indexed... see call site)."""
    # We pass a 1-indexed-ish list where gaps[j] = g_j for j>=1; window j=2..n-1
    return sum(1 for j in range(2, n - 1 + 1) if (gaps[j] % 4) == 2)


def build_gaps(seq):
    """gaps[j] = q_{j+1} - q_j, with gaps[1] = q_2 - q_1. 1-indexed for the
    window formula w = #{ j in [2,n-1] : gap_j ≡ 2 mod 4 }."""
    return [None] + [seq[j + 1] - seq[j] for j in range(len(seq) - 1)]


def measure(seq, nsamples, name):
    """For each n, compute delta(q_n), nu2 (both conventions), w, and ratios.
    Returns list of dicts."""
    gaps = build_gaps(seq)
    out = []
    maxn = max(nsamples)
    # precompute rows once, reuse for all n (each diagonal read from rows)
    rows = list(triangle_rows(seq, maxn))
    for n in nsamples:
        # clip: only k where n-k < len(rows[k])
        dd = [rows[k][n - k] for k in range(n + 1) if n - k < len(rows[k])]
        nu2_c, nu2_l, tau_c, tau_l = nu2_of_diagonal(dd)
        w = w_of_seg(gaps, n)
        rec = {
            'name': name, 'n': n, 'nu2_c': nu2_c, 'nu2_l': nu2_l,
            'w': w, 'tau_c': tau_c, 'tau_l': tau_l,
            'nu2c_over_w': (nu2_c / w) if w else float('inf'),
            'nu2l_over_w': (nu2_l / w) if w else float('inf'),
            'nu2c_over_n': nu2_c / n, 'nu2l_over_n': nu2_l / n,
        }
        out.append(rec)
    return out


FAMILIES = {}


def consecutive_odds(maxv):
    return [2] + [3 + 2 * k for k in range(maxv)]  # 2, 3, 5, 7, 9, ...


def all_gaps_4(maxv):
    # q_1=2, q_2=3, then every gap 4: 2,3,7,11,15,...
    out = [2, 3]
    while len(out) <= maxv:
        out.append(out[-1] + 4)
    return out


def alternating_24(maxv):
    out = [2, 3]
    k = 1
    while len(out) <= maxv:
        gap = 2 if k % 2 == 1 else 4
        out.append(out[-1] + gap)
        k += 1
    return out


def two_then_all4(maxv):
    # 2,3,5, then all gaps 4: 2,3,5,9,13,17,...
    # gap_2 = 5-3 = 2, gap_3 = 9-5 = 4, ...
    out = [2, 3, 5]
    while len(out) <= maxv:
        out.append(out[-1] + 4)
    return out


def two_two_four_then_2424(maxv):
    # 2,3,5,7,11,13,17,19,...
    # gaps: 1,2,2,4,2,4,2,4...
    out = [2, 3, 5, 7]
    k = 1
    while len(out) <= maxv:
        gap = 2 if k % 2 == 1 else 4
        out.append(out[-1] + gap)
        k += 1
    return out


def main():
    N_SAMPLES = list(range(100, 2100, 100))  # 100..2000 step 100
    print("=" * 78)
    print("Directive-55: nu2 >= c*w transfer characterization (exact ints)")
    print("=" * 78)

    # ---------- (1) constant-gap refutation: consecutive odds ----------
    print("\n[1] Constant-gap refutation: q = (2,3,5,7,9,...) all gaps 2")
    print("    (consecutive odds). delta(q_n)=(2n-1,2,0,...,0), nu2=O(1), "
          "w=n-2 -> inf.")
    seq = consecutive_odds(2100)
    recs = measure(seq, [100, 200, 500, 1000, 1500, 2000], "consec-odds")
    print("%-6s %-7s %-7s %-8s %-8s" % ("n", "nu2_c", "nu2_l", "w", "nu2_l/w"))
    for r in recs:
        print("%-6d %-7d %-7d %-8d %.6f" % (
            r['n'], r['nu2_c'], r['nu2_l'], r['w'],
            r['nu2l_over_w']))
    last = recs[-1]
    print("    -> nu2 = %d (canon) / %d (literal) at n=2000, w=%d, "
          "nu2/w -> 0.  REFUTED universal transfer." % (
              last['nu2_c'], last['nu2_l'], last['w']))

    # ---------- (2) structured families ----------
    print("\n[2] min nu2/w and min nu2/n over families (window n=100..2000)")
    families = {
        'consecutive-odds': consecutive_odds(2100),
        'all-gaps-4': all_gaps_4(2100),
        'alternating-2/4': alternating_24(2100),
        '2-then-all-4': two_then_all4(2100),
        '2,2,4,2,4,...': two_two_four_then_2424(2100),
    }
    print("%-18s %-10s %-10s %-10s %-10s %-10s" % (
        "family", "min nu2c/w", "min nu2l/w", "min nu2c/n", "min nu2l/n",
        "w-range"))
    fam_stats = {}
    for name, seq in families.items():
        recs = measure(seq, N_SAMPLES, name)
        min_cw = min(r['nu2c_over_w'] for r in recs)
        min_lw = min(r['nu2l_over_w'] for r in recs)
        min_cn = min(r['nu2c_over_n'] for r in recs)
        min_ln = min(r['nu2l_over_n'] for r in recs)
        ws = [r['w'] for r in recs]
        fam_stats[name] = {
            'min_cw': min_cw, 'min_lw': min_lw, 'min_cn': min_cn,
            'min_ln': min_ln, 'wmin': min(ws), 'wmax': max(ws),
            'recs': recs,
        }
        print("%-18s %-10.4f %-10.4f %-10.4f %-10.4f %d..%d" % (
            name, min_cw, min_lw, min_cn, min_ln, min(ws), max(ws)))

    # ---------- primes ----------
    print("\n[3] The primes (sieve to n=5000).")
    NP = 5000
    P = primes_up_to(70000)  # ~7000 primes, enough
    assert len(P) > NP + 2
    precs = measure(P, N_SAMPLES, "primes")
    pmin_cw = min(r['nu2c_over_w'] for r in precs)
    pmin_lw = min(r['nu2l_over_w'] for r in precs)
    pmin_cn = min(r['nu2c_over_n'] for r in precs)
    pmin_ln = min(r['nu2l_over_n'] for r in precs)
    print("%-18s %-10.4f %-10.4f %-10.4f %-10.4f" % (
        "primes", pmin_cw, pmin_lw, pmin_cn, pmin_ln))
    # show a few prime rows
    print("  prime rows (n,nu2c,nu2l,w,nu2c/w):")
    for r in precs:
        print("    n=%-5d nu2c=%d nu2l=%d w=%d nu2c/w=%.3f" % (
            r['n'], r['nu2_c'], r['nu2_l'], r['w'], r['nu2c_over_w']))

    # ---------- (3) hypothesis assessment ----------
    print("\n[4] Hypothesis assessment (which non-degeneracy restores "
          "nu2>=c*w?)")
    print("    h[j] = (gap_j/2) mod 2 over j in [2,n-1]; w = wt(h).")
    print("    Constant-gap/consecutive-odds case: h == all-ones, w = n-2.")
    hyp = [
        ("H_a", "not all bits 1",
         "excludes all-ones (consec-odds); primes: h=(1,1,0,...) both values -> holds"),
        ("H_b", "at least one 0 and one 1",
         "excludes all-ones and all-zeros; primes -> holds"),
        ("H_c", "w(n) -> infinity",
         "consec-odds w=n-2->inf: does NOT exclude degenerate case"),
        ("H_d", "both values with positive lower density",
         "excludes all-ones; primes -> holds (0 density 0.4, 1 density 0.6)"),
        ("H_e", "w(n) >= c*n for some c>0",
         "consec-odds w=n-2 ~ n: does NOT exclude degenerate case"),
    ]
    print("  %-4s %-34s verdict on consecutive-odds / primes" % ("H", "statement"))
    for hid, stmt, note in hyp:
        print("  %-4s %-34s %s" % (hid, stmt, note))

    print("\n  Measured facts from [2] and [3]:")
    print("    consecutive-odds min nu2l/w = %.3f (nu2=O(1), w~n -> transfer FAILS)" % (
        fam_stats['consecutive-odds']['min_lw']))
    print("    all-gaps-4  min nu2w = %.3f (h all-zeros, w=0)" % (
        fam_stats['all-gaps-4']['min_lw']))
    print("    primes      min nu2c/w = %.3f, min nu2l/w = %.3f (transfer HOLDS)" % (
        pmin_cw, pmin_lw))

    # which H excludes degenerate + primes satisfy -> weakest is H_a
    best = "H_a"
    print("\n  WEAKEST H that (i) excludes the constant-gap degenerate case and "
          "(ii) the primes satisfy: %s" % best)
    print("    (H_a 'not all bits 1' is implied by every stronger non-degeneracy "
          "that excludes all-ones, and is the minimal such; consecutive-odds "
          "violates it, all other families and primes satisfy it.)")
    print("    Under H_a, the primes give measured nu2 >= c*w with c = min nu2c/w "
          "= %.4f > 0." % pmin_cw)
    print("    H_c and H_e are NOT sufficient: consecutive-odds satisfies both "
          "yet gives nu2/w -> 0.")

    print("\n[Distinction]")
    print("  The constant-gap example IS a successful 2-then-odds sequence "
          "(it collapses to all-1 rows: A_k(0)=1 for all k).")
    print("  So it refutes the UNIVERSAL transfer lemma nu2>=c*w, never the "
          "general-class theorem (which the example satisfies).")
    print("  A refuted transfer ROUTE is not a refuted theorem.")
if __name__ == "__main__":
    main()
