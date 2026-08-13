# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**. This conjecture has
been open since 1979 and is believed true, so the working assumption is that
you will not prove it. Claiming it on an argument that has not survived attack
is the one outright failure available here.

A partial result that would count:

- an explicit `k` and a complete determination of the sieve set `A_k`, with
  the surviving residue classes listed and the classes of `n = 0, 2, 8`
  identified among them;
- a proved statement about how `|A_k|` behaves — that it grows, shrinks,
  stabilises, or satisfies a recursion — with the proof, not the data;
- a reproduction of Narkiewicz's bound with its constant made explicit, or a
  located error in it;
- a proof of the conjecture restricted to a stated subclass of `n` (a
  congruence class, a range, a family), with the hypothesis named;
- a precise statement of *why* the modular sieve cannot close, if it cannot —
  naming the obstruction rather than reporting that the search did not finish.

A result stated without the bound it was established under is not a result.
`|A_k|` computed for `k ≤ 12` is a fact about `k ≤ 12`.

## The oracle here is a sieve and a falsifier, not a search

There is no value to recompute. The answer is a proof, so the oracle is:

1. **`digit_free(m)`** — given an integer `m`, decide whether its base-3
   expansion avoids the digit `2`. Exact integer arithmetic, no floats. This
   is ground truth and everything else is measured against it.

2. **`sieve(k)`** — the residue-class sieve. Compute
   `A_k = { r mod 2·3^(k-1) : the low k ternary digits of 2^r mod 3^k avoid 2 }`
   by working modulo `3^k` only. This must **never** materialise `2^n` as a
   big integer for large `n`; that is the compute trap this problem sets.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed obstruction must be run against `n = 0, 2, 8`.** If a lemma,
> a sieve step, or a congruence argument forbids any of the three known
> exceptions, the argument is false. Full stop. Record it as refuted, not as
> "needs adjustment".

Verify `digit_free` by hand on the three witnesses and on a value known to
contain a `2` before trusting either of the others.

## Compute policy — light, parallel, bounded

The naive instrument is wrong here and will consume the run. `2^n` has about
`0.63·n` ternary digits, so testing `n` to `10^6` means arithmetic on numbers
with hundreds of thousands of digits, and it establishes nothing a sieve does
not establish faster.

- **Work modulo `3^k`.** Never build `2^n` for large `n`.
- **Sieve residue classes, not integers.** One discarded class removes an
  entire arithmetic progression.
- **Parallelise across classes.** `code/lib/parallel.py` is in this workspace
  with instructions in `code/lib/PARALLEL.md`. The box has 28 CPUs and the
  container has no CPU quota. Splitting `A_k` across workers is exactly the
  shape `parallel_union` and `parallel_any` are for. Say in every capture how
  many workers ran and what range was covered.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  A program whose output only reaches the model is destroyed when the attempt
  ends.
- **A search that cannot finish is a finding about the method.** Bound it,
  capture the partial result with the bound stated, and record what was not
  covered. Do not re-run the same unbounded computation hoping it lands.

If a `k` is out of reach, say which `k` and why, and what the cost curve looks
like. That is more useful than a larger `k` computed without a stated bound.

## The trap specific to this problem

An argument that establishes

> the density of integers whose ternary expansion avoids the digit 2 tends to 0

has proved something **true and irrelevant**. The conjecture is about the thin
sequence `2^n`, and no density statement about all integers reaches it.
Likewise, the probabilistic heuristic — digits behaving like independent
uniform draws, giving `(2/3)^k` — explains why the conjecture is believed and
proves nothing.

Every claim must state its evidence class: proved, verified-numerically,
conjectured, or asserted-by-source. A heuristic recorded as a proof is the
failure this file exists to prevent.

And note the counting obstruction stated in `problem.md`: the naive estimate
gives `|A_k| ≈ 2·3^(k-1)·(2/3)^k`, which **grows** like `2^k/3` rather than
tending to zero. Any approach must say how it beats that, or explain why the
naive estimate is wrong.

## Ending

Stop and report when you have a partial result of the kind listed above, or
when you can state precisely what blocks the sieve and why. Report the three
witnesses reproduced, the `k` reached, the surviving class count at that `k`,
and the evidence class of every claim.
