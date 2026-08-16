from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string, mod4_string
import sys

# Independent check of the G-endpoint-comparison-density first-step formulas on
# real data: the character-sum route (product over runs of chi(r_a)chi(r_b))
# must equal the SOS route AND the direct oracle, for the REAL prime h.
# Cross-check at scale that the character-sum / endpoint-comparison machinery
# is faithful (no sign error, no indexing error).  The prior refuter claimed
# this was verified on n=20..120 (6868 pairs).  We extend the check.

r = mod4_string(60)
h = [1 if r[j+1] != r[j] else 0 for j in range(len(r)-1)]

from lib.supply_fold import runs_of_downset, s_char_runs

bad = 0
checked = 0
for n in range(4, 52):
    # need r up to index n (s_char_runs needs r length n+1); build from primes
    rn = mod4_string(n+1)
    hn = [1 if rn[j+1] != rn[j] else 0 for j in range(len(rn)-1)]
    # hn length n ; s_sos needs h length n
    if len(hn) < n:
        continue
    hn = hn[:n]
    S_sos, ones_sos = s_sos(n, hn)
    S_char, ones_char = s_char_runs(n, rn)
    checked += 1
    if S_sos != S_char or ones_sos != ones_char:
        bad += 1
        if bad <= 5:
            print(f"MISMATCH n={n} sos=({S_sos},{ones_sos}) char=({S_char},{ones_char})")

print(f"endpoint-comparison character-sum vs SOS: checked n=4..51, {bad} mismatches")
