"""Negative control, shown concretely: true run-count histogram vs a
deliberately wrong run_count (+1 shift) at n = 64. The comparison used in the
census (assert dict(Rb) != dict(R) at every n) is displayed here with numbers.
"""

from collections import Counter
from lib.collapse import downset, run_count


def broken_run_count(A):
    return run_count(A) + 1


def hist(n):
    ds = {d: downset(d, n) for d in range(2, n)}
    R, Rb = Counter(), Counter()
    for d in range(2, n):
        for dp in range(2, n):
            A = frozenset(ds[d] ^ ds[dp])
            R[run_count(A)] += 1
            Rb[broken_run_count(A)] += 1
    return R, Rb


for n in (32, 64, 128):
    R, Rb = hist(n)
    print(f"n = {n}")
    print(f"  true    run histogram: {dict(sorted(R.items()))}")
    print(f"  broken  run histogram: {dict(sorted(Rb.items()))}")
    print(f"  differ? {dict(R) != dict(Rb)}")
    assert dict(R) != dict(Rb)
print("negative control: broken run_count changes the histogram at every checked n")