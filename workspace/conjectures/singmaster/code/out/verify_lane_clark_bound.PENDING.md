# Verification program for Lane Clark's normal-array binomial bound.

The executable lives at `code/lane_clark/verify_lane_clark_bound.py` (see
`code/lane_clark/INDEX.md`). Run it from the workspace root:

    python3 code/lane_clark/verify_lane_clark_bound.py

It checks the claim `lane-clark-normal-array-bound` (N(a) < 2 log2 a + 2 for
the binomial normal array, Lane Clark INTEGERS 10 #A14 2010) two ways:
(1) every witness in `witnesses.json` satisfies the bound, and
(2) brute force over 2 <= a <= 60 reproducing the exact bound.

Its captured output should be written to `verify_lane_clark_bound.captured.txt`
and this folder's INDEX updated when a tool role runs it. The librarian does not
execute programs, so this capture is pending.
