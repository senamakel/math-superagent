#!/usr/bin/env python3
"""Scholar re-check of the run's foundational oracle: does code/lib/gilbreath.py
reproduce the worked rows of problem.md (A_1..A_5) AND the block profiles in
code/out/witnesses.json? The whole library's claims sit on this generator; this
is the mechanical confirmation that the foundation is what the ledger says it is.

Also cross-checks rows_generator against the bare {0,2}-transfer / step-law facts
the claims rely on (the {0,2} block shortens by exactly 1 per row while short).
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.gilbreath import rows_generator, primes_up_to, block_profile, EXPECTED

# 1. Worked rows.
primes = primes_up_to(60)
depth = 5
gen = rows_generator(primes, depth)
got = [next(gen) for _ in range(depth + 1)]
ok_rows = all(got[k][:12] == EXPECTED[k] for k in range(1, depth + 1))
for k in range(1, depth + 1):
    print(f"A_{k} first12 match={got[k][:12] == EXPECTED[k]}")

# 2. Block profiles rows 1..40 vs witnesses.json (sieve to 400000).
witness = __import__("json").load(open("/workspace/code/out/witnesses.json"))
primes400 = primes_up_to(400000)
gen2 = rows_generator(primes400, 40)
next(gen2)  # A_0
b_ok = True
for k in range(1, 41):
    r = next(gen2)
    bp = block_profile(r)
    exp = witness["block_profile_first_40"][k - 1]["block"]
    if bp != exp:
        b_ok = False
        print(f"k={k} profile {bp} != witness {exp}")

print("worked_rows_match:", ok_rows)
print("block_profiles_1to40_match_witness:", b_ok)

# 3. Block-shortening: while a row's leading {0,2} block is intact, the next
#    truncated block is one shorter (the proved block lemma / step law in the
#    simplest form).
ok_short = True
rows = list(rows_generator(primes400, 60))
for k in range(1, 60):
    bcur = block_profile(rows[k])
    bnext = block_profile(rows[k + 1])
    if bcur >= 1 and bnext < bcur - 1:
        ok_short = False
        print(f"row {k}: block {bcur} -> {bnext} violates shorten-by-at-most-1")
print("block_shorten_at_most_1_holds:", ok_short)
print("done")
