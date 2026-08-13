# Tasks

This run's goal is the reduced seed branch of the unitary-perfect-number
problem: finiteness of `H_even = { even m : every prime divisor of 2^m + 1 is
3-Higgs }` would close the Subbarao–Warren reduction of arXiv:2605.20475. The
paper proves only the counting bounds `|H_even ∩ [2,40000]| ≤ 201` and
`|H_even ∩ [2,50000]| ≤ 272`; an independent exact verification of the small
end of this set is the concrete first step.

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

## What this run is doing

Not searching for a sixth unitary perfect number — Wall cleared past `10^102`
(see GOAL.md). Not re-deriving the 2-adic budget identity or the
no-odd-unitary-perfect-number theorem, both already proved in this workspace.
The active work is exact verification of the `H_even` classification below
~1200, which independently checks the paper's Theorem 8 on the reachable end of
the one remaining branch, ahead of any divisor-level attack on `Φ_{4p}(2)`.
