```thread
question: Does the combined bound a ≥ 8 survive independent verification, and can the equality case a = 8 be eliminated?
status: closed — equality case eliminated for 2 ≤ a ≤ 28 by budget-equality-case-impossible
resolution: All four checks from TASKS.md directive 10 confirmed against captured output at code/out/equality_case_elimination.captured.txt:
  (1) a=1 max product = 4/3 exactly, {5,9} is odd part of 90;
  (2) 2^8+1=257 prime, forced when a=8;
  (3) 9=3^2 and 49=7^2 admissible, 3 and 7 are not;
  (4) exclusion runs 2 ≤ a ≤ 28, stops at 29.
The equality case ω(odd) = a+1 is impossible for 2 ≤ a ≤ 28. a=8 is dead by the extremal-product bound. a=1 is realised by n=90. Undecided for a ≥ 29.
rests-on: unitary-perfect-2-adic-budget, unitary-perfect-lower-bound-on-a, budget-equality-case-impossible
blocked-by: none
closed-by: directive 10 — all four checks confirmed from existing capture
```