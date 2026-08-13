# Tasks

This run's goal is the reduced seed branch of the unitary-perfect-number
problem: finiteness of `H_even = { even m : every prime divisor of 2^m + 1 is
3-Higgs }` would close the Subbarao–Warren reduction of arXiv:2605.20475. The
paper proves only the counting bounds `|H_even ∩ [2,40000]| ≤ 201` and
`|H_even ∩ [2,50000]| ≤ 272`; an independent exact verification of the small
end of this set is the concrete first step.

- [ ] **Independent reproduction of the equality-case elimination** — claim
      `budget-equality-case-impossible` was adopted from operator computation
      (`code/out/equality_case_elimination.captured.txt`), not reproduced by
      this run. Directive 7: run the existing program, capture, and confirm the
      four facts by the run's own Fraction arithmetic (not the operator's).
      Command:
      ```
      timeout 540 python3 code/equality_case.py 2>&1 | tee code/out/equality_case_reproduced.captured.txt; echo EXIT_CODE=$?
      ```
      Then confirm by reading the capture:
      (1) at `a=1` the maximum product equals `4/3` EXACTLY, extremal multiset
      `{5,9}` is the odd part of 90; (2) `2^8+1 = 257` is prime, forced at
      `a=8`; (3) `9 = 3^2` and `49 = 7^2` are admissible while 3 and 7 are not;
      (4) exclusion runs `2 ≤ a ≤ 28` and stops at 29. This converts
      `budget-equality-case-impossible` from `source: operator-computation` to
      `status: checked` by this run — the only item in view that moves checked
      off 4. A discrepancy is a loud contradiction.

- [ ] **Independent exact verification of `H_even ∩ [2,1200]`** — implement and
      run `code/H_EVEN_VERIFY_SPEC.md`: reproduce the Phase A worked examples
      (sigma_star oracle on all five, 3-Higgs predicate with 17 non-Higgs /
      31 Higgs, cyclotomic and Aurifeuillean identities, the paper's m=2426 and
      Filter-N examples), then classify `H_even ∩ [2,1200]` by the witness
      sieve (primes in two passes to 10^9, collecting non-3-Higgs divisors of
      `2^m + 1`) plus full factorisation of survivors. Target output: equality
      with the paper's Theorem 8 set `{2, 6, 10, 18, 26, 30, 46, 62, 82, 122}`,
      or a loud discrepancy. Every killed `m` carries a certified witness; every
      run is bounded `timeout 540`, threads split across the 28 cores. Split
      into `code/heven_sieve.py` + `code/heven_classify.py` with shared
      `code/lib/higgs.py`. This is checking structure, never searching for a
      sixth unitary perfect number.

**Capture hygiene (standing rule):** never leave a zero-byte `.captured.txt`
in `code/out`. The capture pattern's `tee` creates the file the instant it
starts, so a command that dies before printing leaves an empty file the judge
reads as a failed experiment. Check every capture is non-empty before moving
on; a run that printed nothing gets one line in the file saying what happened
(e.g. `not run: superseded by the --lo/--hi interface`). This pass repaired
`sieve_pass_1e8` and `sieve_timing_1e6` this way — both were superseded by the
`--lo/--hi` interface, not failed experiments.

## What this run is doing

Not searching for a sixth unitary perfect number — Wall's verification bound is
`≈ 1.46 × 10^23` (not `10^102`; see Contradictions in CONTEXT.md), far beyond
anything reachable here. Not re-deriving the 2-adic budget identity or the
no-odd-unitary-perfect-number theorem, both already proved in this workspace.

**Immediate: independent reproduction of the equality-case elimination.**
Directive 7: claim `budget-equality-case-impossible` was inherited from operator
computation and must be reproduced by this run's own execution before it counts
as `checked`. Run `code/equality_case.py` under `timeout 540`, capture, and
confirm the four arithmetic facts. This is the one item in view that moves
`checked` off 4.

After the equality case is confirmed checked: independent verification of
`H_even ∩ [2,1200]` (the paper's Theorem 8), then any divisor-level attack on
`Φ_{4p}(2)`. Three approaches are proposed but unchecked against the literature
(`research/approaches/`); none is active until the equality case is closed.
