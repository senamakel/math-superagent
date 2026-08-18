#!/usr/bin/env python3
"""
Test conjecture (C) and theorem (T) on the OeS Top-50 tail data — correctly.

The Top-50 table has rank 1..50, p = 9781 (rank 1) down to 8419 (rank 50),
S(p) ~ 1e18.  Parse ONLY rows whose first field is an integer rank in 1..50
and whose second field p is a plausible minimal prime (>= 8419, odd).
The index display lines ("0000 | 0001 | ...") have first field divisible by
20 with value < 5000, and are NOT data rows.

(C): p > 7  ==>  S(p) != 0 (mod 6)   [data conjecture]
(T) [proved congruence]: p>3, p=1 mod 3  ==>  S(p) in {0,2} mod 6;
                         p>3, p=2 mod 3  ==>  S(p) in {0,4} mod 6.
"""
from pathlib import Path
import re

text = Path('research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md').read_text()
rows = []
for line in text.splitlines():
    m = re.match(r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([0-9 ]+)\s*\|', line)
    if not m:
        continue
    rank, p, Sstr = int(m.group(1)), int(m.group(2)), m.group(3).replace(' ', '')
    # restrict to the actual Top-50: rank 1..50, p prime-looking (odd, >= 8000)
    if 1 <= rank <= 50 and p >= 8000 and p % 2 == 1:
        rows.append((rank, p, int(Sstr)))
print(f"parsed {len(rows)} genuine Top-50 rows")
for rank, p, S in rows:
    print(f"  rank {rank:3d}  p={p:6d}  S mod 6 = {S % 6}  p mod 3 = {p % 3}")

from collections import Counter
cres = Counter()
badT = []
badC = []
for rank, p, S in rows:
    if p > 3:
        cres[(p % 3, S % 6)] += 1
        if p % 3 == 1 and S % 6 == 4:
            badT.append((rank, p, S))
        if p % 3 == 2 and S % 6 == 2:
            badT.append((rank, p, S))
    if p > 7 and S % 6 == 0:
        badC.append((rank, p, S))

print(f"\n=== OeS Top-50 tail (S ~ 1e18, p ~ 1e4): {len(rows)} rows ===")
print(f"residue table (p%3, S%6): {dict(cres)}")
print(f"(T) congruence violations: {len(badT)}  {badT[:3]}")
print(f"(C) violations (p>7, S=0 mod 6): {len(badC)}  {badC[:3]}")
