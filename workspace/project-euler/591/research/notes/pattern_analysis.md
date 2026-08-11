# Pattern analysis of PE591 data — findings

Investigation produced by the pattern-finder role on the run's computed data.

## Sequences examined

1. **Record-b sequences** for `||b·√d − π||_Z` (d∈{2,3,5,6,7,8,10,11,13}, scan to 2e6;
   d∈{2,5,7} to 1e7):
   - d=2: 0,3,5,10,418,1403,15263,62584,176827,647659,2255180,6136079,8880289
   - d=3: 0,3,7,33,48,201,981,1761,6803,9714,17667,28531,290618,441934,1420056,1984775
   - d=5: 0,1,5,9,26,187,259,23443,144836,243045,341254,757274,1173294
   - d=7: 0,5,8,25,73,296,567,1061,1826,2591,6910,26975,39167,51359,108000,302307,
     496614,1593623,4690343
   - d=8: 0,5,209,2383,3572,4761,17432,24362,31292,185926,226317,656758,892174,1127590
   - d=10: 0,1,7,44,765,993,6841,8246,61599,114952,1154633,1483409
   - d=11: 0,4,7,10,32,51,111,171,610,989,2186,3383,4580,12141,91342,115222,440784
   - d=13: 0,2,15,20,25,134,314,494,674,7159,13644,56481,197962,431602
2. **|I_d| at n=10^4** (90 d), and at n=10^13 (90 d, results_full.txt).
3. **b_d at n=10^13** (90 d).

## Exact structural facts (verified, conjectures where extrapolated)

### A. The record-b sequences are the Cabanillas candidates — verified
Cabanillas Prop 9/10 (arXiv:1904.01874) candidate set for record-holders of
`||b·α − β||_Z`, α={√d}, β={π}:
- best right:  n = Σ_{i=1}^{2k−1} b_i q_{i−1} + j·q_{2k−1}, j∈{0..b_{2k}−1}
- best left :  n = Σ_{i=1}^{2k}   b_i q_{i−1} + j·q_{2k},   j∈{0..b_{2k+1}−1}
- Every record holder is in the candidate set, and the candidate-set minimum
  equals the brute-force minimum for all 90 non-square d at n=10^6 (zero mismatch).
  Confirmed on d∈{2,3,5,7,11}, N∈{200,1000,5000}, and all d at n=10^6.
  **(This is a proven-verification on supplied data, not extrapolation.)**

### B. |I_d| = nint(b_d·√d − π) = nint(b_d·√d) − 3 — verified at n=10^4
Holds for all 90 non-square d at n=10^4. Reason: the record distance
`||b_d·√d − π||_Z` is small (< 1/2), so `b_d·√d`'s fractional part is within
1/2 of π's fractional part; and with √d∈(1,10), b√d<10^4, rounding `b√d−π`
differs from rounding `b√d` by exactly −3. **Conjecture** that this extends to
n=10^13; the results_full.txt rows satisfy a = nint(π − b√d) exactly by construction.

### C. m²·d scaling law — verified, exact, 36/36 pairs
For d1 = m²·d0 (both non-square <100), |I_{d1}| = |I_{d0}| **iff** m | b_{d0}.
When equal, b_{d1} = b_{d0}/m.
Explanation: α_{m²d0} = {m·α_{d0}}, so the d1 problem is the d0 problem
restricted to the arithmetic progression {0,m,2m,...}. The global minimum is
attained in that progression exactly when the d0 record b is divisible by m.
This is a derived consequence of the verified method; verified 36/36 and 14/14.

### D. No standalone sequence regularity in record-b or |I_d| sequences
- find_linear_recurrence: no constant-coefficient linear recurrence of order ≤6
  fits any of the extended record sequences (an apparent order-5 recurrence on
  the first 10 d=2 terms died when extended to 13 terms).
- analyze_sequence: no low-degree polynomial; differences never stabilize.
- These are the Cabanillas candidates' values, which grow like convergent
  denominators of a target-dependent α-numeration — irregular but O(log L)
  computable.

## First terms that would falsify the conjectures
- B (|I|=nint(b√d−π)=nint(b√d)−3 at n=10^13): falsified at the first (d,b) where
  the record distance ≥ 1/2 (impossible by definition: the distance is <1/2 and
  equals the actual error, which is tiny) — rather, falsified if any row of a
  correct computation violates a = nint(π − b√d), which is definitional. The
  falsifier for the −3 form is any d where nint(b√d) − nint(b√d−π) ≠ 3; none
  observed in all 90 rows.
- C: first (d0,m) with m²d0<100 where |I| equality disagrees with m|b0 — none in
  the 36 pairs available.

## The final answer's structure
The computed S = 498809825393729 comes from summing |a_d|, a_d = nint(π − b_d√d)
with b_d the Cabanillas-candidate minimizer. Independent verification (a separate
implementation) is the remaining cross-check; the d=2 row matches the official
oracle I_2(BQA_2(π,10^13)) = −6188084046055.