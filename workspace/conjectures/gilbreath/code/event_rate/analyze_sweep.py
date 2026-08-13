#!/usr/bin/env python3
"""Post-analysis of the event-rate sweep: death-depth distribution, per-family
survival, and the surviving class's regeneration rates.

Reads code/out/event_rate_stats.jsonl (written by event_rate_sweep.py before
report()).  Answers, with exact counts:

  1. Distribution of first_b0 (the row at which the leading {0,2} block
     first hits length 0) over the 1154 sequences.
  2. Per-family survival fractions, split by batch, with death depth.
  3. Among NON-degenerate survivors (first_b0 is None and events > 0),
     min_b and rate summaries -- the sequences this class offers that look
     like the primes at all.
  4. The phase-boundary story: survival vs the gap-distribution support.

Complexity: single pass over 1154 JSON lines, O(n) time/space.
"""
import json
from collections import Counter, defaultdict

STATS = "code/out/event_rate_stats.jsonl"


def load():
    out = []
    with open(STATS) as f:
        for line in f:
            out.append(json.loads(line))
    return out


def main():
    seqs = load()
    print(f"sequences: {len(seqs)}")
    died = [s for s in seqs if s["first_b0"] is not None]
    alive = [s for s in seqs if s["first_b0"] is None]
    print(f"died (b reached 0 within batch depth): {len(died)} "
          f"({len(died)/len(seqs):.1%})")
    print(f"survived full depth: {len(alive)} ({len(alive)/len(seqs):.1%})")
    print()

    # ---- death-depth distribution -------------------------------------
    hist = Counter(s["first_b0"] for s in died)
    print("death-depth distribution (first row k with b_k == 0):")
    for k in sorted(hist):
        print(f"  k={k:>4}: {hist[k]:>4}  cumulative <= k: "
              f"{sum(v for kk, v in hist.items() if kk <= k):>4}")
    n_inst = sum(v for k, v in hist.items() if k <= 3)
    n_early = sum(v for k, v in hist.items() if k <= 10)
    n_100 = sum(v for k, v in hist.items() if k <= 100)
    print(f"deaths at k<=3 : {n_inst}/{len(died)} ({n_inst/len(died):.1%})")
    print(f"deaths at k<=10: {n_early}/{len(died)} ({n_early/len(died):.1%})")
    print(f"deaths at k<=100: {n_100}/{len(died)} ({n_100/len(died):.1%})")
    print()

    # ---- per-family table ----------------------------------------------
    print(f"{'batch':<6} {'family':<16} {'n':>4} {'died':>5} {'surv':>5} "
          f"{'min_fb0':>6} {'med_fb0':>7} {'%die':>5}")
    fams = sorted({s["family"] for s in seqs})
    for batch in ["sweep", "deep", "long"]:
        for fam in fams:
            sel = [s for s in seqs if s["batch"] == batch and
                   s["family"] == fam]
            if not sel:
                continue
            d = [s for s in sel if s["first_b0"] is not None]
            fb0 = sorted(s["first_b0"] for s in d)
            med = fb0[len(fb0) // 2] if fb0 else None
            print(f"{batch:<6} {fam:<16} {len(sel):>4} {len(d):>5} "
                  f"{len(sel)-len(d):>5} {str(fb0[0] if fb0 else '-'):>6} "
                  f"{str(med):>7} {len(d)/len(sel):>5.0%}")
    print()

    # ---- survivors that look like the primes ---------------------------
    # non-degenerate: block survived, with at least one event (so the
    # regeneration mechanism actually fired), and a non-trivial min_b.
    nd = [s for s in alive if s["events"] > 0]
    print(f"survivors with events > 0 (non-degenerate): {len(nd)}")
    if nd:
        rates = sorted(s["rho_live"] for s in nd if s["rho_live"] is not None)
        minbs = sorted(s["b_min"] for s in nd)
        print(f"  rho_live of that set: min {rates[0]:.4f}, "
              f"median {rates[len(rates)//2]:.4f}, max {rates[-1]:.4f}")
        print(f"  min_b of that set:    min {minbs[0]}, "
              f"median {minbs[len(minbs)//2]}, max {minbs[-1]}")
        print("  per family:")
        d2 = defaultdict(list)
        for s in nd:
            d2[s["family"]].append((s["batch"], s["seed"], s["b_min"],
                                    s["rho_live"], s["live_rows"]))
        for fam in sorted(d2):
            rows = d2[fam]
            rl = [r[3] for r in rows if r[3] is not None]
            print(f"    {fam:<16} n={len(rows):>3} min_b in "
                  f"{[r[2] for r in rows]} rho_live "
                  f"{min(rl):.3f}..{max(rl):.3f}")
    print()

    # ---- phase boundary: death fraction vs min possible gap support ----
    print("phase boundary by gap support (sweep batch, n=48 per family):")
    support = {
        "consecutive": "{2}", "rand24": "{2,4}", "f2-rand24": "{2,4} f2",
        "skew246": "{2,4,6} skew", "f2-skew246": "{2,4,6} skew f2",
        "uniform3": "{2,4,6}", "f2-uniform3": "{2,4,6} f2",
        "skew24810": "{2,4,6,8,10} skew", "f2-skew24810": "{2,4,6,8,10} f2",
        "uniform5": "{2..10}", "f2-uniform5": "{2..10} f2",
        "uniform10": "{2..20}", "f2-uniform10": "{2..20} f2",
        "uniform25": "{2..50}", "f2-uniform25": "{2..50} f2",
        "uniform50": "{2..100}", "f2-uniform50": "{2..100} f2",
        "geo05": "Geom(p=.5)", "f2-geo05": "Geom(p=.5) f2",
        "geo025": "Geom(p=.25)", "f2-geo025": "Geom(p=.25) f2",
        "geo0125": "Geom(p=.125)", "f2-geo0125": "Geom(p=.125) f2",
        "geo00625": "Geom(p=.0625)", "f2-geo00625": "Geom(p=.0625) f2",
    }
    for fam in FAMILY_ORDER():
        sel = [s for s in seqs if s["batch"] == "sweep" and
               s["family"] == fam and s["D"] == 600]
        if not sel:
            continue
        d = len([s for s in sel if s["first_b0"] is not None])
        print(f"  {support.get(fam, fam):<22} died {d:>2}/48 "
              f"({d/len(sel):>4.0%})")


def FAMILY_ORDER():
    return ["consecutive", "rand24", "f2-rand24",
            "skew246", "f2-skew246", "uniform3", "f2-uniform3",
            "skew24810", "f2-skew24810",
            "uniform5", "f2-uniform5", "uniform10", "f2-uniform10",
            "uniform25", "f2-uniform25", "uniform50", "f2-uniform50",
            "geo05", "f2-geo05", "geo025", "f2-geo025",
            "geo0125", "f2-geo0125", "geo00625", "f2-geo00625"]


if __name__ == "__main__":
    main()