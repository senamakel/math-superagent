# Tasks

This run's goal is the reduced seed branch of the unitary-perfect-number
problem: finiteness of `H_even = { even m : every prime divisor of 2^m + 1 is
3-Higgs }` would close the Subbarao–Warren reduction of arXiv:2605.20475.

**Standing order from directive 8: stop fetching for one cycle.** Downloads
went 62 → 67 (Guy §B3, Handbook of Number Theory, Goto 2007) — all catalogue
entries about a problem already stated correctly in `problem.md`. No new
sources are needed; the one item that moves `checked` off 4 is below.

## Immediate (one item in the way)

- [ ] **Independent reproduction of the equality-case elimination.**
      Claim `budget-equality-case-impossible` was adopted from operator
      computation (`code/out/equality_case_elimination.captured.txt`), not
      reproduced by this run. Directive 4 and directive 7 both asked for this
      and it has not happened. This is the only item in view that moves
      `checked` off 4.

      Run:
      ```
      timeout 540 python3 code/equality_case.py 2>&1 | tee code/out/equality_case_reproduced.captured.txt; echo EXIT_CODE=$?
      ```

      Then confirm by reading the capture (use the run's own Fraction
      arithmetic, not the operator's):
      1. At `a=1` the maximum product equals `4/3` EXACTLY, and the extremal
         multiset `{5, 9}` is the odd part of 90. This is the one that matters:
         if the a=1 maximum equals 4/3 exactly and is realised by the odd part
         of an actual unitary perfect number, the estimate is not lossy at the
         bottom.
      2. `2^8 + 1 = 257` is prime, so 257 is forced as a component when `a=8`.
      3. `9 = 3^2` and `49 = 7^2` are admissible; 3 and 7 are not.
      4. The exclusion runs `2 ≤ a ≤ 28` and stops at `a=29`.

      **Check the capture is non-empty before moving on.** A discrepancy is a
      loud contradiction.

## Next (blocked on the equality-case reproduction)

- [ ] **Independent exact verification of `H_even ∩ [2,1200]`** — per
      `code/H_EVEN_VERIFY_SPEC.md`: reproduce the paper's Theorem 8 set
      `{2, 6, 10, 18, 26, 30, 46, 62, 82, 122}`. This is blocked on:
      - The verify harness bugs in `heven_classify.py` (A2 literal direction
        reversed, A3 `.eval(2)` crash — see CONTEXT.md Gaps §1)
      - Full sieve passes to 10^8 / 10^9 not captured (CONTEXT.md Gaps §2)
      - `code/higgs/check_a057447.py` never run (CONTEXT.md Gaps §6)

      Do not start this until the equality-case capture above is confirmed.

## Do not do

- Do not fetch new sources. The library phase is closed; survey literature
  (Guy, Handbook of Number Theory, Goto) adds catalogue entries about a problem
  already correctly stated here.
- Do not propose new approaches. Approaches went 4 → 7 and none are checked
  against the literature. Ground existing proposals before adding more.
- Do not diversify away from H_even. The [74:08] "progress no" came from a
  judge that timed out, not from an assessment.

## Standing capture hygiene

Never leave a zero-byte `.captured.txt` in `code/out`. `tee` creates the file
instantly, so a command that dies before printing leaves an empty file. A run
that printed nothing gets one line saying what happened.