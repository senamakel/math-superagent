#!/usr/bin/env python3
"""Independent re-aggregation of the PE156 answer from the on-disk per-digit
solution files.

This is NOT the solver.  It is a third, independent route to the grand total:
sum the 661 listed solutions in code/out/solutions-d{1..9}.txt — the same
numbers the two structurally different evaluators (place-value peeling and the
MSD block-sum / digit-DP of code/verify.py) produced — but recompute s(d) and
the total from scratch by plain integer addition, with no digit-counting code
at all.  It checks:
  - each file's term count against the sourced A130432 counts [84,14,36,48,5,72,49,344,9]
  - each file is strictly increasing (solutions are listed in increasing order)
  - the last term of each file equals the paper's Table 3 maxima
  - s(1) == 22786974071 (the problem statement's given value)
  - per-digit sums and the grand total
The only claims this verifies are about the on-disk data itself: that the
solution lists are complete in count, ordered, and sum to the reported answer.
"""
import os

OUT = os.path.join(os.path.dirname(__file__))
COUNTS = {1: 84, 2: 14, 3: 36, 4: 48, 5: 5, 6: 72, 7: 49, 8: 344, 9: 9}
# Paper Table 3 (Khovanova & Marton, AMM 132(8) 2025 / arXiv v2): max(E(d)).
TABLE3 = {1: 1111111110, 2: 10535000000, 3: 20500000000, 4: 30500000000,
          5: 40000000000, 6: 59628399995, 7: 69971736170, 8: 79998399997,
          9: 80000000000}

ok = True
grand = 0
for d in range(1, 10):
    path = os.path.join(OUT, f"solutions-d{d}.txt")
    with open(path) as fh:
        nums = [int(line) for line in fh if line.strip()]
    n = len(nums)
    inc = all(nums[i] < nums[i + 1] for i in range(n - 1))
    s = sum(nums)
    grand += s
    good = (n == COUNTS[d]) and inc and (nums[-1] == TABLE3[d])
    ok = ok and good
    print(f"d={d}: count={n} (A130432 {COUNTS[d]}) inc={inc} "
          f"max={nums[-1]} (Table3 {TABLE3[d]}) s(d)={s} "
          f"{'OK' if good else 'FAIL'}")

print()
s1 = sum(int(x) for x in open(os.path.join(OUT, "solutions-d1.txt")).read().split())
print("s(1) == 22786974071 (given in the statement):",
      "OK" if s1 == 22786974071 else "FAIL")
print("GRAND TOTAL sum(s(d)) d=1..9 =", grand)
print("matches the verified answer 21295121502550:",
      "OK" if grand == 21295121502550 else "FAIL")
print("ALL CHECKS:", "OK" if ok else "FAIL")
