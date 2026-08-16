#!/usr/bin/env python3
"""Fresh re-check of the popcount/run-count stratification of S(n) for SUPPLY.

Reproduces the earlier table (code/out/dyadic_stratify_by_popcount.captured.txt)
as a pipeline correctness check, then answers the specific question: does the
bulk of S(n)'s weight live in LOW-popcount (few-run) strata or is it spread?

For n in {400, 1000, 4000}, using exact arithmetic via lib.supply_fold:
  terms[d] = (-1)^{T(n,d)}, d = 2..n-1   (s_terms_sos)
  group d by popcount(d):
    (a) count of depths with popcount<=5 vs >5, and #+1 vs #-1 terms inside each
    (b) net sign-sum S contributed by each group
    (c) |S_low| / |S_high| and |S_low| / |S|(total)
    (d) group d by RUN COUNT of its downset (few-run depths), net sign-sum per
        run-count class
Then a one-line verdict vs the route's falsifier (LIVE iff low/few-run group is
same-signed and dominant; DEAD iff balanced/spread).

Exact ints only; the ratios are printed floats for readability.
"""

from lib.primes import mod4_string
from lib.supply_fold import h_from_r, s_terms_sos, s_sos, runs_of_downset


def popcount(x):
    return bin(x).count("1")


def run_count(d):
    return len(runs_of_downset(d))


def split_by(n, terms, keyfn, keyname, split_popcount=5):
    """Group terms (i=0 -> d=2) by keyfn(d); report per-key counts of +1/-1,
    net sign-sum, and the <=split vs >split aggregate."""
    per_key = {}
    for i, t in enumerate(terms):
        d = i + 2
        k = keyfn(d)
        cnt_p, cnt_m, s = per_key.get(k, (0, 0, 0))
        per_key[k] = (cnt_p + (1 if t == 1 else 0),
                      cnt_m + (1 if t == -1 else 0),
                      s + t)
    lines = []
    lines.append(f"  [{keyname}]  per-class counts(+1/-1) and net sign-sum:")
    for k in sorted(per_key):
        cp, cm, s = per_key[k]
        lines.append(f"    {keyname}={k:>4}:  +1={cp:6d}  -1={cm:6d}  net={s:+8d}")
    # aggregate low (<=split) vs high (>split)
    low_n = low_p = low_m = 0
    high_n = high_p = high_m = 0
    for i, t in enumerate(terms):
        d = i + 2
        k = keyfn(d)
        if k <= split_popcount:
            low_n += 1
            low_p += (t == 1)
            low_m += (t == -1)
        else:
            high_n += 1
            high_p += (t == 1)
            high_m += (t == -1)
    return lines, (low_n, low_p, low_m, low_p - low_m), \
        (high_n, high_p, high_m, high_p - high_m)


def run(n, r, label, split=5):
    h = h_from_r(r)
    terms = s_terms_sos(n, h)
    S, ones = s_sos(n, h)
    assert sum(terms) == S and terms.count(-1) == ones
    n_terms = n - 2
    lines = [f"==== {label}: n={n} ====",
             f"S(n) = {S}, |S|/n = {abs(S)/n:.4f}, density(T=1) = {ones/n_terms:.4f}"]

    # --- (a),(b),(c) popcount split ---
    pc_lines, low, high = split_by(n, terms, popcount, "popcount", split)
    lines += pc_lines
    low_n, low_p, low_m, low_s = low
    high_n, high_p, high_m, high_s = high
    lines.append(
        f"  popcount<= {split}: {low_n} depths ({low_n/n_terms:.3f} of all), "
        f"+1={low_p}, -1={low_m}, net S_low={low_s:+d}"
    )
    lines.append(
        f"  popcount>  {split}: {high_n} depths ({high_n/n_terms:.3f} of all), "
        f"+1={high_p}, -1={high_m}, net S_high={high_s:+d}"
    )
    lines.append(
        f"  ratios: |S_low|/|S_high| = {abs(low_s)}/{abs(high_s)} = "
        f"{abs(low_s)/abs(high_s) if high_s else float('inf'):.3f},  "
        f"|S_low|/|S| = {abs(low_s)}/{abs(S)} = "
        f"{abs(low_s)/abs(S) if S else float('inf'):.3f}"
    )

    # --- (d) run-count split (few-run depths) ---
    lines.append("  [run-count]  per-class counts and net sign-sum:")
    per_run = {}
    for i, t in enumerate(terms):
        d = i + 2
        k = run_count(d)          # number of runs in downset of d (a power of 2)
        cp, cm, s = per_run.get(k, (0, 0, 0))
        per_run[k] = (cp + (t == 1), cm + (t == -1), s + t)
    for k in sorted(per_run):
        cp, cm, s = per_run[k]
        lines.append(f"    runs={k:>4}:  +1={cp:6d}  -1={cm:6d}  net={s:+8d}")
    # few-run aggregate: runs <= 4 (<=2 gaps) vs many-run (runs>=8)
    few = sorted(k for k in per_run)
    maxrun = few[-1]
    # few-run = runs <= max(4, ...) : use runs<=4 as the "few-run" cutoff
    int_n = int_p = int_m = 0
    ext_n = ext_p = ext_m = 0
    for i, t in enumerate(terms):
        d = i + 2
        k = run_count(d)
        if k <= 4:
            int_n += 1; int_p += (t == 1); int_m += (t == -1)
        else:
            ext_n += 1; ext_p += (t == 1); ext_m += (t == -1)
    int_s = int_p - int_m
    ext_s = ext_p - ext_m
    lines.append(
        f"  runs<=4 (few-run): {int_n} depths ({int_n/n_terms:.3f} of all), "
        f"+1={int_p}, -1={int_m}, net={int_s:+d}"
    )
    lines.append(
        f"  runs>=8 (many-run): {ext_n} depths ({ext_n/n_terms:.3f} of all), "
        f"+1={ext_p}, -1={ext_m}, net={ext_s:+d}"
    )
    lines.append("")
    summary = (S, low_s, high_s, abs(low_s) / abs(S) if S else float("inf"),
               int_s, ext_s)
    return lines, summary


def main():
    big_ns = [400, 1000, 4000]
    for n in big_ns:
        r = mod4_string(n + 1)
        lines, _ = run(n, r, "PRIMES")
        print("\n".join(lines))


if __name__ == "__main__":
    main()
