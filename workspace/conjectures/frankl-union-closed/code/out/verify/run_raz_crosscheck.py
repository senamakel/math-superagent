#!/usr/bin/env python3
"""Independently verify Raz (2017) counterexample abundance half, using the
canonical oracle stub's data (not re-typed) plus an OR-closure sanity check:
the family as printed must NOT be union-closed (it is a Reimer-condition
family, not a UC family) — confirming we are measuring the right object.

This reproduces the paper's claim that no element lies in >= |A|/2 sets.
"""
import sys, os
sys.path.insert(0, "/workspace/code/out")
from verify_raz_counterexample import S, main
from lib.uc import decide_union_closed as is_union_closed

# 1. Abundance half, via the stub's own computation
print("--- abundance half (from stub) ---")
main()

# 2. Negative-control sanity: the family is NOT union-closed, so the
#    "no abundant element" statement is a claim about the Reimer-condition
#    class, not a UC counterexample.
S_as_bitmasks = [sum(1 << (x - 1) for x in A) for A in S]
uc = is_union_closed(S_as_bitmasks)
print("family is union-closed:", uc)
assert not uc, "sanity: Raz's Reimer-condition family should not be union-closed"

# 3. Explicit per-element counts (second route, counted directly)
from collections import Counter
cnt = Counter()
for A in S:
    for x in A:
        cnt[x] += 1
maxc = max(cnt.values())
print("max per-element count:", maxc, "|A|=11, half=5.5 -> abundant needs >=6")
assert maxc <= 5, "an element is abundant"
print("CROSSCHECK PASS: no element abundant; family not union-closed (negative control OK)")
