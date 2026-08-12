# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk: the
established results with their basis, the approaches that failed and why, what
the computed numbers look like, and what durable memory holds about this
problem from earlier runs. It is not a catalogue of files (`research/INDEX.md`
is that) and not a narration of what agents did.

**Token budget 10,000.** The file is re-sent on every model call in every role,
so length is a bill paid many times over.

## Problem (Project Euler 346 — sourced, `problem.md`)

A **strong repunit** is a positive integer that is a repunit (a number written
with only the digit `1`) in **at least two distinct bases `b > 1`**.

- Repunit with `k` digits in base `b`: `R(b,k) = 1 + b + ... + b^(k-1) = (b^k - 1)/(b - 1)`.
- Every `n >= 3` is `11` in base `n-1` (length `k=2`), so length-2 gives every
  `n >= 3` one automatic representation.
- `1` is a single-digit (`k=1`) repunit in every base — hence counted.
- **Task:** sum of all strong repunits below `10^12`.

**Oracle (test checks, given in statement):**
- The 8 strong repunits below 50: `{1, 7, 13, 15, 21, 31, 40, 43}`.
- Sum of all strong repunits below 1000 = **15864**.

**Governing structure (step-2 theory; NOT yet verified by a program):** a value
`n < 10^12` is a strong repunit iff it occurs with frequency >= 2 in the
enumeration of `R(b,k)` over bases `b>1` and lengths `k >= 2` (a `k>=3` repunit
always pairs with the automatic `k=2` one; distinct `k>=3` reps also count;
`1` added by hand). The bound makes enumeration cheap: for `k >= 3`,
`b^(k-1) < 10^12` forces `b < 10^6` at `k=3` and shrinks fast, so the work grows
with the *number of bases/lengths*, not with `10^12`. This is the structural
fact that defeats scanning all `n < 10^12`. **To be derived and executed in
solution.md / solution.py; brute.py is the oracle.**

## Established

Nothing computed yet — this is a fresh run. The two oracle facts above are
sourced from the statement; nothing else is marked established.

## Ruled out

Nothing yet. (Brute force over all `n < 10^12` is the naive wrong method the
theory above avoids — do not rebuild it at full size.)

## Numbers

Only the statement's oracle values (above). No program output yet.

## Recalled

`recall_memory` for "strong repunit / repunit / Euler 346" returns **nothing on
this problem** — only unrelated runs (project_euler_763, project_euler_185).
There is no prior-run finding to import; the oracle values must be reproduced
by brute.py before they are trusted as the run's own.

## Contradictions

None so far.

## Gaps

- No `brute.py` oracle yet: must reproduce the 8-below-50 set and the
  sum-below-1000 = 15864 before any method is trusted.
- The step-2/3 derivation above is a sketch, not checked. Confirm the
  frequency>=2 counting (including `1` and the automatic `k=2` term) against
  the oracle, then run at `10^12`.
