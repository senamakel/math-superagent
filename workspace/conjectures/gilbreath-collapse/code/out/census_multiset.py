"""MULTISET CENSUS for COLLAPSE, n=2..20.

For each n iterate S2_char(n) = multiset {A = M_d △ M_d' : d,d' in [2,n-1]}
with multiplicity m(A). For each DISTINCT A write a row:
    |A|, diam(A)=max-min, run_count(A), run_lengths(A), m(A).
Also compute the weighted span histogram H_n(k) = sum m(A) over A with diam=k
and, for each n, the largest diam occurring with its total multiplicity.

Output: code/out/multiset_census_n20.txt
"""
import sys
from collections import Counter, defaultdict
from lib.collapse import S2_char, run_count


def run_lengths(A):
    """Lengths of maximal runs of consecutive integers in frozenset A, in position order."""
    if not A:
        return []
    s = sorted(A)
    out = []
    run_start = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i - 1] + 1:
            out.append(s[i - 1] - run_start + 1)
            run_start = s[i]
    out.append(s[-1] - run_start + 1)
    return out


def main():
    out = sys.stdout
    lines = []
    for n in range(2, 21):
        c = S2_char(n)
        rows = []          # per distinct A
        hist = defaultdict(int)   # diam -> total multiplicity
        maxdiam = -1
        maxdiam_mult = 0
        for A, m in c.items():
            if not A:
                diam = None
            else:
                lo, hi = min(A), max(A)
                diam = hi - lo
                hist[diam] += m
                if diam > maxdiam or (diam == maxdiam and True):
                    if diam > maxdiam:
                        maxdiam = diam
                        maxdiam_mult = m
            rows.append((len(A), diam, run_count(A), run_lengths(A), m))
        rows.sort(key=lambda r: (r[2], r[0]))  # by run_count then size
        lines.append(f"\n=== n={n}: distinct sets={len(rows)}  "
                     f"total pairs=(n-2)^2={(n-2)**2}  "
                     f"largest diam={maxdiam} multiplicity={maxdiam_mult} ===")
        if maxdiam >= 0:
            H = " ".join(f"{k}:{hist[k]}" for k in sorted(hist))
            lines.append(f"  weighted span histogram diam->mult: {H}")
        for (size, diam, rc, rl, m) in rows:
            dstr = '-'
            if diam is not None:
                dstr = str(diam)
            lines.append(f"  |A|={size:3d} diam={dstr:>3s} runs={rc} "
                         f"run_lengths=[{','.join(map(str, rl))}] m={m}")
    text = "\n".join(lines) + "\n"
    # atomic write: temp file then move
    with open("code/out/.census.tmp", "w") as f:
        f.write(text)
    import os
    os.replace("code/out/.census.tmp", "code/out/multiset_census_n20.txt")
    out.write(text)


if __name__ == "__main__":
    main()
