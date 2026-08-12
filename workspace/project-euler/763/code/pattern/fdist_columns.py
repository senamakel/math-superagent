"""Test closed-form structure of f-distributions within each max-level column.

For the diagonal column M=N (offset k=0): count with f dividable cells =
  3 * C(N-2, f-3) * 2^(f-3)  (verified N=2..14 incl OOS 13,14).

Model for sub-diagonal columns M=N-k (offset k): try
  count(M=N-k, f) = A_k * C(N-something, f-3) * 2^(f-3) * [polynomial]
Look for whether each column's f-distribution, divided by 2^(f-3), is a
polynomial in f scaled by binomial factors -- OR just record the observed
tables cleanly so a later role can spot the pattern.

Data source: scratchpad/structure_probe.txt joint (M,f) for N=2..12, plus the
fresh N=13,14 diagonal already verified.  Here we dump the sub-diagonal
columns' f-distributions and compare against guesses.
"""
import re, math
from collections import defaultdict

# Parse joint (M,f) data from scratchpad/structure_probe.txt
joint = defaultdict(dict)  # N -> (M,f) -> count
Ncur = None
for line in open('scratchpad/structure_probe.txt'):
    line = line.strip()
    m = re.match(r'N=(\d+)', line)
    if m:
        Ncur = int(m.group(1))
    if line.startswith('M='):
        mm = re.match(r'M=(\d+) f=(\d+): (\d+)', line)
        if mm:
            M, f, c = int(mm.group(1)), int(mm.group(2)), int(mm.group(3))
            joint[Ncur][(M, f)] = c

# For each N, group by offset k=N-M
for k in [0, 1, 2, 3]:
    print(f"\n===== offset k={k} (column M=N-{k}) =====")
    for N in sorted(joint):
        col = {f: c for (M, f), c in joint[N].items() if N - M == k}
        if not col:
            continue
        # normalize: divide by 2^(f-3)
        print(f"  N={N:2d} tot={sum(col.values()):7d}: f-dist {dict(sorted(col.items()))}")

# Now add the fresh N=13,14 diagonal to confirm (already done in diag_f_oos)
# Check sub-diagonal at N=13,14 from bitmask rerun?  That requires a new run;
# first show the pattern in 2..12.
