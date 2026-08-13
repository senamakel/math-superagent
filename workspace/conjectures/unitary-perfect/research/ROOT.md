# ROOT — starting position of this run

The problem is Erdős #1052 (https://www.erdosproblems.com/1052): are there
only finitely many unitary perfect numbers, i.e. `n` with
`σ*(n) = Π_{p^a∥n}(p^a+1) = 2n`? Five are known; no sixth has been found and
finiteness is open. Wall cleared the search past `10^102` in 1975, so this run
produces no new search; its deliverable is a structural theorem or an exact
partial result. Oracle and witness set (`6, 60, 90, 87360,
146361946186458562560000`) verified in `code/out/known_five_verified.captured.txt`.

## 1. Structure of a minimal counterexample

Any *sixth* unitary perfect number `n = 2^a · m` (m odd) must be:

- **Even** — no odd unitary perfect number exists (Subbarao–Warren 1966; proof
  in `research/notes/parity-and-2-adic-budget.md`). So `a ≥ 1`.
- **Non-squarefree odd part** — Graham 1989 (`research/summaries/graham-1989-squarefree-odd-part.md`,
  `research/sources/graham-1989-squarefree-odd-part.full.md`) proved the
  squarefree-odd-part numbers are exactly `6, 60, 87360`. So a sixth has a
  repeated odd prime power (like `3^2` in 90, `5^4` in the fifth). The two
  occurring kernels are the sharpest edge of the witness set: any lemma killing
  all repeated odd prime powers is false.
- **At least 9 odd components** — Wall 1988, *New unitary perfect numbers have
  at least nine odd components*, Fib. Quart. 26(4):312–317
  (`research/sources/wall-1988-nine-odd-components.full.md`).
- **Seed branch in H_even** — the seed factor `2^a + 1` appears explicitly in
  the full balance `(2^a+1)·Π(p_i^{e_i}+1) = 2^{a+1}·Π p_i^{e_i}`. Maciejewski
  (arXiv:2605.20475) reduces the surviving branch to the auxiliary set
  `H_even = { even m : every prime divisor of 2^m + 1 is 3-Higgs }`, where a
  3-Higgs prime `p` has `p−1 | (product of smaller 3-Higgs primes)^3`
  (working form: every `q | p−1` is 3-Higgs and `v_q(p−1) ≤ 3`; first
  non-Higgs is 17, since `v2(16) = 4`).

Workspace-added: combining Wall 1988 with the proved 2-adic budget identity
`Σ v2(p_i^{e_i}+1) = a+1` (so `ω(odd) ≤ a+1`) gives `a ≥ ω(odd) − 1 ≥ 8` for
any sixth — **`2^8 = 256` divides it** — checked against all five in
`code/out/wall1988_budget_lower_bound.captured.txt` and recorded in
`research/notes/lower-bound-on-a.md`.

## 2. Current verification bound

`|H_even ∩ [2, 50000]| ≤ 272` rigorous, established in arXiv:2605.20475
(`research/sources/maciejewski-bounded-box-subbarao-warren.full.md`), with the
counting bound `|H_even ∩ [2, 40000]| ≤ 201` also stated. The known
`H_even ∩ [2,1200] = {2, 6, 10, 18, 26, 30, 46, 62, 82, 122}` (paper Theorem 8).

There are **262 undecided candidates**; every one is `m = 2p` with `p` an odd
Higgs prime. They are blocked not by mathematics but by **unfactored 355–6000
digit cofactors** of `2^{2p} + 1`, which current ECM/SNFS has not resolved. This
is why independence of `H_even` below ~1200 matters: it is the part of the
branch reachable by exact integer work in this container, and it is the target
of the `H_even` verification spec.

## 3. Restricted classes already settled (with hypotheses)

- **No odd unitary perfect number** — Subbarao–Warren 1966
  (`research/sources/subbarao-warren-1966-unitary-perfect.full.md`). Proved
  outright.
- **Squarefree odd part exactly {6, 60, 87360}** — Graham 1989 (source above).
  So every other number has a repeated odd prime; the only kernels known to
  occur are `3^2` and `5^4`.
- **Impostor kernels eliminated for `1 ≤ a ≤ 10000`** in the bounded box —
  Maciejewski Theorem 2. Within the bounded enumeration of the odd dependency
  graph every admissible source kernel is `3^2`, `5^4`, or one of **five
  impostor kernels**; the three-filter certificate (Filter Z: Zsigmondy/Higgs
  exponent; Filter N: seed-divisor non-3-Higgs witness; Filter O: 2-adic
  budget overshoot) eliminates the impostors for all seed classes with
  `1 ≤ a ≤ 10000`. Hypothesis: the bounded box and `a ≤ 10000`; it does not
  prove finiteness.

This run's current goal: the independent exact verification of
`H_even ∩ [2,1200]` per `code/H_EVEN_VERIFY_SPEC.md` (see TASKS.md), the first
concrete step toward the reduced seed branch.
