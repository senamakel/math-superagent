# Tasks

This run's goal is the reduced seed branch of the unitary-perfect-number
problem: finiteness of `H_even = { even m : every prime divisor of 2^m + 1 is
3-Higgs }` would close the Subbarao–Warren reduction of arXiv:2605.20475. The
paper proves only the counting bounds `|H_even ∩ [2,40000]| ≤ 201` and
`|H_even ∩ [2,50000]| ≤ 272`; an independent exact verification of the small
end of this set is the concrete first step.

- [ ] **Independent verification of the equality-case elimination** — the result
      in `research/notes/equality-case-eliminated.md` is already filed as claim
      `budget-equality-case-impossible` but was adopted from operator
      computation, not reproduced here. Write a fresh program (do not reuse
      `code/equality_case.py`) that: (a) recomputes `T(a) = 2^{a+1}/(2^a+1)`
      and the max product over the `a+1` smallest admissible sizes in exact
      `Fraction` arithmetic for `a = 1..30`; (b) confirms 257 is prime and
      forced at `a=8`, and confirms 9 and 49 are admissible while 3 and 7 are
      not (3 mod 4, so their minimal admissible power is the square); (c)
      confirms the `a=1` equality `T(1) = max = 4/3` is exact in rational
      arithmetic and attained by `{5,9}`, matching the odd part of `n=90`; (d)
      confirms the `a=8` deficit in exact arithmetic. Output to
      `code/out/equality_case_independent.captured.txt`. This is a verification
      of an already-filed result, not a new claim; a discrepancy is a loud
      contradiction. Bounded `timeout 120` — it's arithmetic, not factoring.

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

Not searching for a sixth unitary perfect number — Wall cleared past `10^102`
(see GOAL.md). Not re-deriving the 2-adic budget identity or the
no-odd-unitary-perfect-number theorem, both already proved in this workspace.
The active work is exact verification of the `H_even` classification below
~1200, which independently checks the paper's Theorem 8 on the reachable end of
the one remaining branch, ahead of any divisor-level attack on `Φ_{4p}(2)`.
