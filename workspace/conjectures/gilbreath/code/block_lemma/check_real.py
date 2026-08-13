#!/usr/bin/env python3
"""Check the exact block lemma against the REAL prime rows and measure the
actual regeneration margin (not the worst case).

For each real row k with leading {0,2}-block of length n_k, the block lemma
guarantees rows k..k+n_k start with 1 (that they do is automatic). The
informative quantity is the ACTUAL horizon past the guaranteed end over which
the row's second entry stays in {0,2} — i.e. how far real data regenerates
beyond the lemma's guarantee. If for every k the real row keeps its second
entry in {0,2} to depth 600, then k+n_k row's position 1 surviving means
regeneration is happening faster than consumption.
"""
import json, os
from lib.gilbreath import primes_up_to, rows_generator, block_profile

here = os.path.dirname(os.path.abspath(__file__))
wsp = json.load(open(os.path.join(here, "..", "out", "witnesses.json")))

# Regenerate rows exactly as witnesses.json did: sieve to 400000, 600 rows.
primes = primes_up_to(400000)
print("primes rebuilt:", len(primes))
gen = rows_generator(primes, 600)
next(gen)  # A_0

rows = {}
for k in range(1, 601):
    rows[k] = next(gen)

# 1) For every real row, record its leading {0,2}-block length n_k and verify
#    that rows k..k+n_k indeed all start with 1 (the lemma's guarantee).
violations = 0
min_horizon = None
min_horizon_k = None
horizons = []
for k in range(1, 601):
    nk = block_profile(rows[k])
    horizon = k + nk          # last row the lemma protects = k + n_k
    if k + nk > 600:
        continue              # past the window
    for kk in range(k, k + nk + 1):
        if rows[kk][0] != 1:
            violations += 1
    if min_horizon is None or horizon < min_horizon:
        min_horizon = horizon
        min_horizon_k = k
    horizons.append(horizon)

print(f"\n[1] Real rows k=1..600: block lemma guarantee (rows k..k+n_k start with 1)")
print(f"    violations found: {violations}")
print(f"    min protected horizon (k + n_k) over rows that stay inside the window: "
      f"{min_horizon} at row k={min_horizon_k}")
print(f"    median protected horizon: {sorted(h for h in horizons if h <= 600)[len([h for h in horizons if h<=600])//2]}")

# 2) Regeneration margin: for each row k, how far past k+n_k does the SECOND
#    entry stay in {0,2}?  If the second entry leaves {0,2} at row k+n_k+1,
#    regeneration barely keeps up (binding). If it stays in {0,2} much longer,
#    regeneration is comfortably above the guarantee.
import statistics
margins = []
binding = 0
for k in range(1, 601):
    nk = block_profile(rows[k])
    # walk down from row k+n_k+1 while second entry in {0,2}
    j = k + nk + 1
    depth = 0
    while j <= 600 and rows[j][1] in (0, 2):
        depth += 1
        j += 1
    margins.append(depth)
    if depth == 0:
        binding += 1

print(f"\n[2] Regeneration margin (rows past k+n_k whose 2nd entry stays in {{0,2}}), "
      f"rows with k+n_k inside window:")
subset = [m for (k, m) in zip(range(1, 601), margins) if k + block_profile(rows[k]) <= 598]
print(f"    rows assessed: {len(subset)}")
print(f"    min margin: {min(subset)}   (a 0 would mean the 2nd entry escaped the row"
      f" immediately after the guarantee end)")
print(f"    median margin: {statistics.median(subset)}")
print(f"    mean margin: {statistics.mean(subset):.1f}")
print(f"    max margin: {max(subset)}")
print(f"    rows where margin == 0 (block fully exhausted, no free regeneration): {subset.count(0)}")

# 3) Report the minimal and typical n_k (the resource being consumed).
nks = [block_profile(rows[k]) for k in range(1, 601)]
print(f"\n[3] Block lengths n_k over real rows k=1..600:")
print(f"    min n_k = {min(nks)}, median = {statistics.median(nks)}, max = {max(nks)}")

print("\nNote: the lemma guarantees only n_k+1 rows. The real rows keep position 1 "
      "in {0,2} far longer because the absolute-difference operator REGENERATES "
      "{0,2} from below (large evens leak in from the boundary and get reduced). "
      "The margin in [2] measures exactly that free regeneration.")
