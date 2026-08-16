# What ends this run, and what counts as a result

## The deliverable

A **proof, a disproof, or a genuine partial result stated exactly**. This
conjecture has been open since 1979 and is believed true, so the working
assumption is that you will not prove it. Claiming it on an argument that has
not survived attack is the one outright failure available here.

This workspace was cleared and restarted deliberately. Nothing in it is
inherited: every claim starts at status *unverified* and must be established
here, with its evidence class, before anything is built on it.

A partial result that would count:

- a **symbolic invariant** — a congruence, weight function, carry statistic on
  the base-2 → base-3 transducer, or automaton-theoretic obstruction — that is
  preserved by `x ↦ 2x` on `Z_3` and violated by the digit-`{0,1}` set `S`,
  together with an honest statement of the range in which it has been checked
  and of what a proof of it would require;
- a **refutation of a candidate invariant**, stated as such: the SMT encoding,
  the model the solver returned, and why it kills the candidate. A killed
  approach recorded precisely is a result here;
- any argument that constrains the **middle** ternary digits of `2^n` — the low
  digits are what the sieve reaches and the high digits are what size arguments
  reach; the middle is where every existing method is silent — or a proof that
  a stated approach cannot reach them;
- a proof of the conjecture restricted to a stated subclass of `n` (a
  congruence class, a range, a family), with the hypothesis named;
- an established consequence, for the thin sequence `2^n`, of Hausdorff
  dimension bounds on digit-restricted subsets of `Z_3` — including a precise
  statement of what dimension `log2/log3`, or even dimension 0, would *not*
  give, since a dimension statement about a set is not a statement about which
  integers lie in it;
- a machine-checked Lean 4 formalisation of whatever lemma the run does
  establish, with `#print axioms` output and every remaining `sorry` reported;
- a located error in a source, or a reproduction of Narkiewicz's bound or the
  Dimitrov–Howe digit count with the constant made explicit.

A result stated without the bound it was established under is not a result.
`|A_k|` computed for `k ≤ 12` is a fact about `k ≤ 12`. An SMT check over
digit strings of length `≤ 40` is a fact about length `≤ 40`.

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
> a sieve step, a congruence argument, or an SMT encoding forbids any of the
> three known exceptions, the argument is false. Full stop. Record it as
> refuted, not as "needs adjustment".

Verify `digit_free` by hand on the three witnesses and on a value known to
contain a `2` before trusting either of the others. An SMT encoding is only
trustworthy once it has been shown to *find* the `n = 8` solution when the
`n > 8` restriction is lifted — an encoding that returns `unsat` everywhere is
almost always over-constrained, and that is the failure mode of this route.

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
- **Z3 is a bounded instrument.** An SMT query with no bound on digit length
  will not return. State the bound in the query, capture the model or the
  `unsat` with the bound beside it, and never promote a bounded `unsat` to a
  general theorem — that promotion is the specific error this route invites.
- **A search that cannot finish is a finding about the method.** Bound it,
  capture the partial result with the bound stated, and record what was not
  covered. Do not re-run the same unbounded computation hoping it lands.

If a `k` is out of reach, say which `k` and why, and what the cost curve looks
like. That is more useful than a larger `k` computed without a stated bound.

## The traps specific to this problem

**The density trap.** An argument that establishes

> the density of integers whose ternary expansion avoids the digit 2 tends to 0

has proved something **true and irrelevant**. The conjecture is about the thin
sequence `2^n`, and no density statement about all integers reaches it.
Likewise, the probabilistic heuristic — digits behaving like independent
uniform draws, giving `(2/3)^k` — explains why the conjecture is believed and
proves nothing.

**The counting obstruction.** `problem.md` states it: the naive estimate gives
`|A_k| ≈ 2·3^(k-1)·(2/3)^k`, which **grows** like `2^k/3` rather than tending
to zero, and a prior run reports the exact count `|A_k| = 2^(k-1)`. If that is
right the sieve never closes at any finite `k`. Establish it or refute it once,
early and cheaply, and then say how the 3-adic and symbolic-invariant routes
beat it. Re-sieving to a larger `k` after that point is not progress.

**The over-constrained solver.** A Z3 encoding that returns `unsat` for every
`n` has almost certainly encoded something false, because `n = 0, 2, 8` are
satisfiable. Run the witness check on every encoding before reporting from it.

Every claim must state its evidence class: proved, verified-numerically,
conjectured, or asserted-by-source. A heuristic recorded as a proof, or a
bounded `unsat` recorded as a theorem, is the failure this file exists to
prevent.

## Ending

Stop and report when you have a partial result of the kind listed above, or
when you can state precisely what blocks **the route you actually pursued** and
why. Report the three witnesses reproduced, the evidence class of every claim,
and — if you are stopping on a blocker — which of the listed partial results you
attempted and what defeated each.

"The modular sieve cannot close" does not by itself end this run. It is the
starting obstruction, stated in `problem.md`, and the run is asked to get past
it. An obstruction only ends the run if it is an obstruction to something the
run actually attempted after that point.
