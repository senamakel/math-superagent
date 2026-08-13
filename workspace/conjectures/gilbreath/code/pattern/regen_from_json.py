#!/usr/bin/env python3
"""Summarise regeneration from the existing blocks_depth1000.json -- no sieve.

For every k where b_{k+1} >= b_k (a regeneration event, diff >= 0) report
k, b_k, b_{k+1}, diff and the intruder c_k (first entry past the leading
{0,2} block on row k). Also erosion-run statistics and intruder mod-4
distribution, all re-derived from the JSON so the file is captured without
recomputing the 20M sieve.
"""
import collections
import json

D = json.load(open('/workspace/code/out/blocks_depth1000.json'))
b, s, intr = D['b'], D['s'], D['intruder']
n = len(b)


def nice(x):
    return 'None' if x is None else str(x)


print(f"depth {n}; oracle_agree_first_40={D['oracle_agree_first_40']} first_bad={D['first_bad']}")
print(f"min_block={D['min_block']} at k={b.index(D['min_block']) + 1}; "
      f"max_block={D['max_block']} at k={b.index(D['max_block']) + 1}")

diffs = [b[i + 1] - b[i] for i in range(n - 1)]
regen = [(i + 1, b[i], b[i + 1], diffs[i], intr[i], intr[i + 1])
         for i in range(n - 1) if diffs[i] >= 0]
print(f"\nTotal transitions {n - 1}; regeneration events (b_[k+1] >= b_k): {len(regen)}")
print(f"fraction of transitions that regenerate: {len(regen) / (n - 1):.4f}")
print("\nregeneration: k->k+1, b_k, b_{k+1}, diff, c_k, c_{k+1}")
for r in regen:
    print(f"  k={r[0]}->{r[0] + 1}: b {r[1]}->{r[2]} (diff +{r[3]})  "
          f"c_k={nice(r[4])} c_{r[0] + 1}={nice(r[5])}")

# erosion runs: maximal consecutive -1
best_er = 0
runs = []
er = 0
start = None
for i in range(n - 1):
    if diffs[i] == -1:
        if er == 0:
            start = i + 1
        er += 1
        if er > best_er:
            best_er = er
    else:
        if er > 0:
            runs.append((start, er))
        er = 0
if er > 0:
    runs.append((start, er))
runs.sort(key=lambda t: -t[1])
print(f"\nLongest pure-erosion run (consecutive b(k+1)=b(k)-1): {best_er}")
print("Longest erosion runs (k_start, length):", runs[:8])
print("erosion runs of length >= 5 (start k, len, b at start, c at start):")
for r in runs:
    if r[1] >= 5:
        k0 = r[0]
        print(f"  k={k0} len {r[1]} b={b[k0 - 1]} c={nice(intr[k0 - 1])}")

nonnull = [x for x in intr if x is not None]
mod4 = collections.Counter(x % 4 for x in nonnull)
print(f"\nintruder c_k: {len(nonnull)} non-null of {n}; min {min(nonnull)} max {max(nonnull)}")
print("c mod 4 distribution:", sorted(mod4.items()))
print("c == 4 share:", round(sum(1 for x in nonnull if x == 4) / len(nonnull), 4))

small = [r for r in regen if r[1] < 100]
print(f"\nregenerations with b_k < 100: {len(small)} of {len(regen)}")
bk_at_regen = sorted(set(r[1] for r in regen))
print("b_k values at which a regeneration occurs:", bk_at_regen)
cnt = collections.Counter(b)
print("\nb value -> count over all rows:", sorted(cnt.items()))
