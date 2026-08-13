#!/usr/bin/env python3
"""Job 3: last-line / EXIT_CODE sweep over every capture in code/out/*.captured.txt.

Reports, per capture, the last line and whether it carries an EXIT_CODE entry
(the convention used by this run's capture pipeline: `echo EXIT_CODE=$? >> cap`).
Also lists captures with no EXIT_CODE line and the distinct recorded values.
Pure read-only analysis; linear in the total size of the captures.
"""
import glob
import re
from collections import Counter

caps = sorted(glob.glob('code/out/*.captured.txt'))
rows = []
for f in caps:
    lines = [l.rstrip('\n') for l in open(f, errors='replace')]
    last = lines[-1] if lines else '<EMPTY FILE>'
    m = re.search(r'EXIT_CODE=(\S+)', last)
    rows.append((f, last, m.group(1) if m else None))

with open('code/out/exitcode_sweep.captured.txt', 'w') as out:
    out.write(f"Total captures: {len(caps)}\n\n")
    for f, last, ec in rows:
        out.write(f"{f}: last line = {last!r}\n    EXIT_CODE = {ec if ec is not None else 'ABSENT'}\n")
    vals = [ec for _, _, ec in rows if ec is not None]
    nolast = [f.split('/')[-1] for f, _, ec in rows if ec is None]
    out.write(f"\nCaptures with an EXIT_CODE line ({len(vals)}): " +
              ", ".join(f.split('/')[-1] for f, _, ec in rows if ec is not None) + "\n")
    out.write(f"\nDistinct EXIT_CODE values: {dict(Counter(vals))}\n")
    out.write(f"\nCaptures with NO EXIT_CODE line ({len(nolast)}):\n" +
              "\n".join(f"  - {n}" for n in nolast) + "\n")
print("wrote code/out/exitcode_sweep.captured.txt")
print("captures with EXIT_CODE:", sum(1 for _,_,ec in rows if ec is not None))
print("captures without:", sum(1 for _,_,ec in rows if ec is None))