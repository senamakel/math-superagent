#!/usr/bin/env python3
"""Survivor analysis of the event-rate sweep (pattern-finder pass).

Pure read of code/out/event_rate_stats.jsonl — no row arithmetic, no sieves.

Answers exactly, and only, from the persisted dataset (1154 sequences):
  Q1  per-family death counts and death-row (first_b0) distributions
  Q2  conditioning on first gap = 2: f2 vs non-f2 matched families, and
      whether support shape still discriminates inside the f2 sub-family
  Q3  "no sequence that survived row 10 died later": max first_b0, count of
      first_b0 in [11, D], and what the survivors' end-state is
  Q4  one-sentence characterization of the surviving class, with numbers

Plus a proved-structure consistency check (the {0,2}-corner theorem):
  * gaps all 2 (consecutive): A_1 = (1,2,2,...) -> corner at row 1
  * gaps subseteq {2,4}, first gap 2 (f2-rand24): A_2 = (1, {0,2} x ...)
    -> corner at row 2 (trunc_k = 2) for every seed
  * rand24 unforced: corner at row 2 iff g_0 = 2 (so every rand24 survivor
    must have trunc_k = 2); death at row 1 iff g_0 = 4 (first_b0 = 1).
  The corner state (1, {0,2}, {0,2}, ...) is closed under |a-b|, hence
  those sequences satisfy the {0,2} property for ALL rows, provably.

Complexity: single pass over 1154 JSON lines, O(n) time/space.
"""
import json
from collections import Counter, defaultdict

STATS = "code/out/event_rate_stats.jsonl"


def load():
    with open(STATS) as f:
        return [json.loads(line) for line in f]


def main():
    seqs = load()
    n = len(seqs)
    died = [s for s in seqs if s["first_b0"] is not None]
    surv = [s for s in seqs if s["first_b0"] is None]
    print(f"sequences: {n}")
    print(f"died (first_b0 set): {len(died)} ({len(died)/n:.1%})")
    print(f"survived to batch depth: {len(surv)} ({len(surv)/n:.1%})")
    print()

    # ---- Q1: per-family deaths and death-row distribution --------------
    print("Q1  per family (all batches pooled; death = first_b0; "
          "death rows are 1-based row indices)")
    print(f"{'family':<16} {'n':>4} {'died':>5} {'surv':>5} {'die%':>6} "
          f"{'min':>3} {'med':>3} {'max':>3}   death-row histogram k=1..10")
    fams = sorted({s["family"] for s in seqs})
    hist_all = Counter(s["first_b0"] for s in died)
    for fam in fams:
        sel = [s for s in seqs if s["family"] == fam]
        d = [s for s in sel if s["first_b0"] is not None]
        h = Counter(s["first_b0"] for s in d)
        if d:
            rows = sorted(s["first_b0"] for s in d)
            med = rows[len(rows) // 2]
            hist = " ".join(str(h.get(k, 0)) for k in range(1, 11))
            print(f"{fam:<16} {len(sel):>4} {len(d):>5} {len(sel)-len(d):>5} "
                  f"{len(d)/len(sel):>6.0%} {rows[0]:>3} {med:>3} "
                  f"{rows[-1]:>3}   {hist}")
        else:
            print(f"{fam:<16} {len(sel):>4} {len(d):>5} {len(sel):>5} "
                  f"{0:>6.0%} {'-':>3} {'-':>3} {'-':>3}")
    print()
    print("overall death-row histogram (all 852 deaths):")
    for k in range(1, 11):
        c = hist_all.get(k, 0)
        cum = sum(v for kk, v in hist_all.items() if kk <= k)
        print(f"  k={k:>2}: {c:>4}   cumulative {cum:>4}")
    print(f"  max first_b0 over all sequences: "
          f"{max(s['first_b0'] for s in died)}")
    print()

    # ---- Q2: first-gap-2 conditioning ----------------------------------
    print("Q2  first-gap-2 conditioning (matched families, pooled batches)")
    pairs = [
        ("rand24", "f2-rand24"), ("skew246", "f2-skew246"),
        ("skew24810", "f2-skew24810"), ("uniform3", "f2-uniform3"),
        ("uniform5", "f2-uniform5"), ("uniform10", "f2-uniform10"),
        ("uniform25", "f2-uniform25"), ("uniform50", "f2-uniform50"),
        ("geo05", "f2-geo05"), ("geo025", "f2-geo025"),
    ]
    print(f"{'base':<14} {'n':>4} {'die%':>6} {'min':>3} {'med':>3} "
          f"{'max':>3} | {'f2-':<14} {'n':>4} {'die%':>6} {'min':>3} "
          f"{'med':>3} {'max':>3}")
    for base, f2 in pairs:
        def bstats(name):
            sel = [s for s in seqs if s["family"] == name]
            d = [s for s in sel if s["first_b0"] is not None]
            if d:
                rows = sorted(s["first_b0"] for s in d)
                return len(sel), len(d)/len(sel), rows[0], \
                    rows[len(rows)//2], rows[-1]
            return len(sel), 0.0, "-", "-", "-"
        nb, db, mnb, mdb, mxb = bstats(base)
        nf, df, mnf, mdf, mxf = bstats(f2)
        print(f"{base:<14} {nb:>4} {db:>6.0%} {str(mnb):>3} {str(mdb):>3} "
              f"{str(mxb):>3} | {f2:<14} {nf:>4} {df:>6.0%} "
              f"{str(mnf):>3} {str(mdf):>3} {str(mxf):>3}")
    print()
    print("does support shape still discriminate inside f2? "
          "(all f2 families, pooled, sorted by death rate)")
    f2fams = [f for f in fams if f.startswith("f2-")]
    rows = []
    for fam in f2fams:
        sel = [s for s in seqs if s["family"] == fam]
        d = [s for s in sel if s["first_b0"] is not None]
        if d:
            fr = sorted(s["first_b0"] for s in d)
            rows.append((len(d)/len(sel), fam, len(sel), len(d),
                         fr[0], fr[len(fr)//2], fr[-1]))
        else:
            rows.append((0.0, fam, len(sel), 0, "-", "-", "-"))
    for rate, fam, nb, nd, mn, md, mx in sorted(rows):
        print(f"  {fam:<16} died {nd:>3}/{nb:<3} ({rate:>5.0%})  "
              f"death k: min {mn}, med {md}, max {mx}")
    print("  mean gap per family (for reference): "
          "rand24 3 | skew246 2.9 | skew24810 3.16 | uniform3 4 | "
          "uniform5 6 | uniform10 11 | uniform25 26 | uniform50 51 | "
          "geo05 4 | geo025 8 | geo0125 16 | geo00625 32")
    print()

    # ---- Q3: no survivor of row 10 dies later --------------------------
    print("Q3  survival past row 10")
    max_fb0 = max(s["first_b0"] for s in died)
    late = [s for s in seqs if (s["first_b0"] or 0) > 10]
    print(f"  max first_b0 among the {len(died)} deaths: {max_fb0}")
    print(f"  sequences with first_b0 > 10: {len(late)} "
          f"(should be 0) -> these are exactly the sequences that "
          f"reached row 11 with b >= 1")
    # all survivors reached batch depth: first_b0 None means the measurement
    # loop ran to D (or ended early at trunc_k, which is a corner, not a death)
    for s in surv:
        assert s["trunc_k"] is None or s["trunc_k"] <= s["D"]
    trunc = [s for s in surv if s["trunc_k"] is not None]
    full = [s for s in surv if s["trunc_k"] is None]
    print(f"  survivors: {len(surv)} = {len(full)} ran full depth with "
          f"intruder present + {len(trunc)} reached the {0,2}-corner "
          f"(block filled the finite row) at trunc_k")
    print(f"  survivor trunc_k distribution (corner-entry row):")
    tc = Counter(s["trunc_k"] for s in trunc)
    for k in sorted(tc):
        print(f"    trunc_k={k}: {tc[k]}")
    print()

    # ---- Q4: surviving class -------------------------------------------
    print("Q4  surviving class characterization")
    nd = [s for s in surv if s["events"] > 0]
    print(f"  survivors with events > 0 (non-degenerate): {len(nd)}")
    rates = sorted(s["rho_live"] for s in nd)
    mb = sorted(s["b_min"] for s in nd)
    print(f"    rho_live: min {rates[0]:.4f}, median "
          f"{rates[len(rates)//2]:.4f}, max {rates[-1]:.4f}")
    print(f"    b_min:    min {mb[0]}, median {mb[len(mb)//2]}, "
          f"max {mb[-1]}")
    per_fam = defaultdict(int)
    for s in surv:
        per_fam[s["family"]] += 1
    print("  survivor counts per family:")
    for fam, c in sorted(per_fam.items(), key=lambda kv: -kv[1]):
        print(f"    {fam:<16} {c:>3}")
    # corner-class counts: consecutive (trunc_k=1), f2-rand24 (trunc_k=2),
    # rand24 survivors (should all be trunc_k=2 by the theorem)
    corner = [s for s in surv if s["trunc_k"] is not None]
    c_cons = sum(1 for s in corner if s["family"] == "consecutive")
    c_f2r24 = sum(1 for s in corner if s["family"] == "f2-rand24")
    c_r24 = sum(1 for s in corner if s["family"] == "rand24")
    n_cons = sum(1 for s in seqs if s["family"] == "consecutive")
    n_f2r24 = sum(1 for s in seqs if s["family"] == "f2-rand24")
    n_r24 = sum(1 for s in seqs if s["family"] == "rand24")
    r24_surv = sum(1 for s in seqs if s["family"] == "rand24"
                   and s["first_b0"] is None)
    print(f"  corner-class check (block fills row => immortal state, "
          f"provably):")
    print(f"    consecutive trunc_k=1: {c_cons}/{n_cons} (theorem: all)")
    print(f"    f2-rand24 trunc_k=2:   {c_f2r24}/{n_f2r24} (theorem: all)")
    print(f"    rand24 survivors with trunc_k=2 (theorem: iff g_0=2): "
          f"{c_r24}/{r24_surv}")
    r24_dead_k1 = sum(1 for s in seqs if s["family"] == "rand24"
                      and s["first_b0"] == 1)
    print(f"    rand24 deaths at k=1 (theorem: iff g_0=4): "
          f"{r24_dead_k1}/{n_r24}")
    print()

    # ---- independent consistency with the recorded analysis -------------
    print("consistency with recorded analysis (captured.txt):")
    tot_ev = sum(s["events"] for s in seqs)
    tot_elig = sum(s["eligible"] for s in seqs)
    print(f"  sum events   = {tot_ev} (recorded 20013)")
    print(f"  sum eligible = {tot_elig} (recorded 46528)")
    print(f"  died {len(died)} / surv {len(surv)} (recorded 852/302)")


if __name__ == "__main__":
    main()