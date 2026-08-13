```thread
question: Does the combined bound a ≥ 8 survive independent verification, and can the equality case a = 8 be eliminated?
status: closed — equality case eliminated for 2 ≤ a ≤ 28 by budget-equality-case-impossible
resolution: All four checks confirmed against captured output at code/out/equality_case_verification.captured.txt:
  (1) a=1 max product = 4/3 exactly, {5,9} is odd part of 90;
  (2) 2^8+1=257 prime, forced when a=8;
  (3) 9=3^2 and 49=7^2 admissible, 3 and 7 are not;
  (4) exclusion runs 2 ≤ a ≤ 28, stops at 29; M(28)=1.997752860 < T(28)=1.999999993; M(29)=2.004964964 > T(29)=1.999999996.
The equality case ω(odd) = a+1 is impossible for 2 ≤ a ≤ 28. a=8 is dead by the extremal-product bound. a=1 is realised by n=90. Undecided for a ≥ 29.

BUG-FIX (directive 11): admissible_sizes() in equality_case_verify.py originally iterated primes in order, took the first `count`, then sorted — missing admissible sizes 37, 41, 53 while wrongly including 121, 361, 529. Fixed to generate over BOUND=800, sort all, then slice, with a safety assertion. The exclusion 2 ≤ a ≤ 28 survives the fix (both buggy and fixed code agree on this boundary for different reasons — with the buggy code the bound was undershooting, but the crossing from < to > happened at the same a); the claim that a=29 is excluded, which would have been false, was never recorded in any task or thread. Verified output at code/out/equality_case_verify.captured.txt is post-fix and correct.

rests-on: unitary-perfect-2-adic-budget, unitary-perfect-lower-bound-on-a, budget-equality-case-impossible
blocked-by: none
closed-by: directive 10 — all four checks confirmed; directive 11 — bug found and fixed, boundary confirmed correct at a=28
```