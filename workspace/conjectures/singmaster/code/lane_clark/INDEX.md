# Index — code/lane_clark

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_lane_clark_bound.py` | Checks Lane Clark 2010 (INTEGERS 10 #A14) normal-array binomial bound N(a) < 2 log2 a + 2 against code/out/witnesses.json and brute force over 2<=a<=60 — the verification oracle for claim lane-clark-normal-array-bound. Correctness: exact integer arithmetic; brute count checks each k in 2..999 by binary search in n (never builds the triangle); matches witnesses.json N values. Fresh operator re-run captured at code/out/verify_lane_clark_bound.newcaptured.txt, EXIT_CODE=0, all checks pass (prior capture not adopted as evidence). Claim checked; effective:yes, uniform-in-k:yes. |
