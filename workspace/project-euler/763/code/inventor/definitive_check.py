#!/usr/bin/env python3
"""Definitive claim check + decomposition for the 3D amoeba, N up to 14.

Runs the memory-compact bitmask forward BFS level by level to Nmax
(default 14).  For each reachable config it decodes it transiently and checks:

  A1        : the max level M holds EXACTLY 3 cells.
  A2_tri    : those 3 form {p+e1,p+e2,p+e3} for a single parent p (at M-1).
  A2_empty  : (stronger) that parent p is EMPTY (not in the config).
  A3        : naive deterministic top-cap collapse: replace the top 3 (whose
              parent p is empty) by p, iterate to {origin} in N steps.
  B         : D(N+1) == sum over conf(N) of f(C), f=#dividable cells.

It also tabulates, for N=2..12, the decomposition of D(N) by
  (a) max level M, (b) f(C), (c) joint (M,f), (d) level histograms.

Exact BFS; configs decoded transiently.  Writes the full report to
/workspace/scratchpad/structure_probe.txt.
"""
import time
from collections import defaultdict

from lib.amoeba import next_level_bits, decode_bits, children, f_of


def lvl(p):
    return sum(p)


def top_parent_present(cells, M, top):
    """Return (parent, present_bool) if top=={p+ei}, else (None, False)."""
    a, b, c = sorted(top)
    s = (a[0]+b[0]+c[0]-1, a[1]+b[1]+c[1]-1, a[2]+b[2]+c[2]-1)
    if s[0] % 3 or s[1] % 3 or s[2] % 3:
        return None, False
    p = (s[0]//3, s[1]//3, s[2]//3)
    if set(children(p, 3)) == set(top):
        return p, p in cells
    return None, False


def naive_collapse(cells):
    """A3: top-cap merge of an EMPTY parent, iterate to {origin} in N steps.
    Return (ok, steps)."""
    Sset = set(cells)
    steps = 0
    while Sset != {(0, 0, 0)}:
        M = max(lvl(p) for p in Sset)
        top = [p for p in Sset if lvl(p) == M]
        if len(top) != 3:
            return False, steps
        a, b, c = sorted(top)
        s = (a[0]+b[0]+c[0]-1, a[1]+b[1]+c[1]-1, a[2]+b[2]+c[2]-1)
        if s[0] % 3 or s[1] % 3 or s[2] % 3:
            return False, steps
        p = (s[0]//3, s[1]//3, s[2]//3)
        if not (set(children(p, 3)) == set(top)):
            return False, steps
        if p in Sset:          # parent present: naive cap-collapse invalid
            return False, steps
        for t in top:
            Sset.discard(t)
        Sset.add(p)
        steps += 1
        if steps > 100:
            return False, steps
    return True, steps


def main(Nmax=14):
    W = Nmax + 1
    level = {1}
    out = []
    print(f"{'N':>2} {'D(N)':>9} | {'A1bad':>6} {'A2tribad':>8} {'A2empbad':>8} "
          f"{'A3bad':>6} | {'Byes':>5} {'sumf':>8} {'D+1':>11}")
    for n in range(0, Nmax + 1):
        if n >= 1:
            level = next_level_bits(level, W)
        D = len(level)
        if n == 0:
            print(f"{n:>2} {D:>9} | start")
            out.append(f"N={n} D={D} start")
            continue

        a1 = a2tri = a2emp = a3 = 0
        s_f = 0
        M_counts = defaultdict(int)
        f_counts = defaultdict(int)
        joint = defaultdict(int)
        hist_counts = defaultdict(int)
        for S in level:
            cells = decode_bits(S, W)
            Sset = set(cells)
            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]
            if len(top) != 3:
                a1 += 1
            par, pres = top_parent_present(cells, M, top)
            if par is None:
                a2tri += 1
                a2emp += 1
            elif pres:
                a2emp += 1      # triangle holds but parent present (fail A2-empty)
            fv = f_of(cells)
            s_f += fv
            ok, st = naive_collapse(cells)
            if not ok or st != n:
                a3 += 1
            # decomposition for N in 2..12
            if 2 <= n <= 12:
                M_counts[M] += 1
                f_counts[fv] += 1
                joint[(M, fv)] += 1
                hist_counts[level_hist(cells, M)] += 1

        # B needs D(n+1); compute next level count
        Dp1 = len(next_level_bits(level, W)) if n < Nmax else None
        Byes = (s_f == Dp1) if n < Nmax else None
        print(f"{n:>2} {D:>9} | {a1:>6} {a2tri:>8} {a2emp:>8} {a3:>6} | "
              f"{str(Byes):>5} {s_f:>8} {str(Dp1):>11}")
        out.append(f"N={n} D={D} A1bad={a1} A2tri_bad={a2tri} A2empty_bad={a2emp} "
                   f"A3bad={a3} B_match={Byes} sum_f={s_f} Dplus1={Dp1}")

        if 2 <= n <= 12:
            out.append(f"  by M: {dict(sorted(M_counts.items()))}")
            out.append(f"  by f: {dict(sorted(f_counts.items()))}")
            out.append("  joint (M,f):")
            for (M, fv) in sorted(joint):
                out.append(f"    M={M} f={fv}: {joint[(M,fv)]}")
            out.append(f"  #distinct histograms={len(hist_counts)}")
            out.append("  most frequent histograms:")
            for h, c in sorted(hist_counts.items(), key=lambda kv: -kv[1])[:10]:
                out.append(f"    {h}: {c}")
            out.append("")
        if n == 12 and Nmax > 12:
            # save intermediate partial so a long run to 14 isn't lost
            with open('/workspace/scratchpad/structure_probe.txt', 'w') as fh:
                fh.write("\n".join(out) + "\n")

    with open('/workspace/scratchpad/structure_probe.txt', 'w') as fh:
        fh.write("\n".join(out) + "\n")
    print("\nWrote /workspace/scratchpad/structure_probe.txt")


def level_hist(cells, M):
    f = defaultdict(int)
    for p in cells:
        f[sum(p)] += 1
    return tuple(f.get(k, 0) for k in range(M + 1))


if __name__ == "__main__":
    import sys
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    main(Nmax)
