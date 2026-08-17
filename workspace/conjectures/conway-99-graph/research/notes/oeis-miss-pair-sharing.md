# OEIS lookup: the 84-vertex pair-labeling s-sharing sequences are not catalogued

Two family sequences from the 84-vertex pair-labeling reduction (round 31) were
looked up in OEIS over the five feasible members `k ∈ {4,14,22,112,994}`:

1. `[4, 84, 220, 6160, 493024]` — the number M = C(k,2) − k/2 of non-matching
   pairs of a k-set with a perfect matching. **No match.**
2. `[2, 2562, 19910, 18298280, 121047498992]` — the s=0 pair-pair count
   M·(M−1−2(k−3))/2. **No match.**

Both are closed-form-determinable from k alone (parameter-determined), so the
miss confirms no external closed form surfaces. Recorded so nobody searches
OEIS for them again. (Same class as `oeis-miss-distance2-and-replication.md`.)
