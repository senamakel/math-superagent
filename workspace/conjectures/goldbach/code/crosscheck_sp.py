#!/usr/bin/env python3
"""Cross-check the three independent S(p) computations where they overlap."""
from pathlib import Path

def load_pairs(path):
    """Parse 'p S' or '(p, S)' lines into dict."""
    d = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('('):
            # "(p, S)" format
            a, b = line[1:-1].split(',')
            d[int(a)] = int(b)
        else:
            parts = line.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                d[int(parts[0])] = int(parts[1])
    return d

# pairwise comparisons
runs = {
    'pair-enum N=2e5': load_pairs('code/out/seq_sp_eff_200000.txt'),
    'vec N=2e6':       load_pairs('code/out/seq_sp_vec_2000000.txt'),
    'vec N=1e7':       load_pairs('code/out/seq_sp_vec_10000000.txt'),
}

def compare(nameA, dA, nameB, dB):
    common = set(dA) & set(dB)
    diffs = [(p, dA[p], dB[p]) for p in common if dA[p] != dB[p]]
    print(f"{nameA} vs {nameB}: {len(common)} common primes, {len(diffs)} disagreements")
    if diffs[:5]:
        print(f"  first disagreements: {diffs[:5]}")
    return len(diffs)

total = 0
total += compare('pair-enum N=2e5', runs['pair-enum N=2e5'], 'vec N=2e6', runs['vec N=2e6'])
total += compare('pair-enum N=2e5', runs['pair-enum N=2e5'], 'vec N=1e7', runs['vec N=1e7'])
total += compare('vec N=2e6', runs['vec N=2e6'], 'vec N=1e7', runs['vec N=1e7'])
print(f"\nTOTAL DISAGREEMENTS: {total}")
print("(0 disagreements = the two independent methods agree exactly where they overlap)")

# also: confirm the mod-3 theorem on every computed pair
bad = []
for name, d in runs.items():
    for p, s in d.items():
        if p > 3:
            if p % 3 == 1 and s % 6 == 4:
                bad.append((name, p, s))
            if p % 3 == 2 and s % 6 == 2:
                bad.append((name, p, s))
print(f"\nmod-3 theorem violations across all {sum(len(d) for d in runs.values())} computed S(p) pairs: {len(bad)}")
if bad[:5]:
    print(bad[:5])

# (C) conjecture: p > 7 with S(p) == 0 mod 6
badC = []
for name, d in runs.items():
    for p, s in d.items():
        if p > 7 and s % 6 == 0:
            badC.append((name, p, s))
print(f"(C) p>7 with S(p)=0 mod 6, across all runs: {len(badC)}")
