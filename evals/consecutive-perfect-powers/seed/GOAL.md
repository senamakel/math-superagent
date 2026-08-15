# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on
`x^p - y^q = 1`.

The question has stood since the nineteenth century and is believed to have
exactly one solution. The working assumption is that you will not settle it.
Claiming it on an argument that has not survived attack is the one outright
failure available here — and this problem makes that failure unusually easy,
because an argument that proves too much looks exactly like an argument that
works. See the trap below.

Results that would count, in rough order of value:

- a **proof that `(3,2,2,3)` is the only solution**;
- a **proof for all odd prime exponent pairs satisfying a stated, checkable
  condition** — a conditional theorem with the hypothesis named exactly, which
  is the realistic shape of a real contribution here;
- a **new necessary condition** on a hypothetical second solution, proved, and
  verified against the known solution and against a computational search;
- the **divisibility conditions re-derived with proofs**, rather than cited,
  together with a search confirming them to a stated exponent bound — this is
  reachable and it is the foundation everything else needs;
- the **exponent-2 cases proved in full** in this workspace, both of them;
- a **located gap or error** in a published partial result, recorded as refuted
  with the failing step named. A located error is a genuine result;
- a **Lean 4 formalisation** of the reduction to odd prime exponents, or of one
  exponent-2 case, with `#print axioms` reported and every `sorry` listed.

A result stated without the hypotheses it was established under is not a result.
A condition verified for exponents below `10^4` is a fact about exponents below
`10^4` unless it is proved.

## The oracle is a bounded exact search and a falsifier

1. **`solutions(N)`** — all `(x, p, y, q)` with `x^p, y^q <= N`, by exact
   integer arithmetic. It must return exactly `(3,2,2,3)`. **Integer arithmetic
   only**: `x^p` leaves float range almost immediately, and a float comparison
   manufactures solutions that are not there. Report the `N` reached.

2. **`check_conditions(p, q)`** — the reconstructed necessary conditions,
   evaluated directly. Calibrate on `(2,3)`: the known solution must satisfy
   them. A condition set that rejects `(2,3)` is wrong.

3. **The falsification oracle, which is the one that matters.**

> **Run every claimed lemma against `3^2 - 2^3 = 1`.** The conjecture asserts
> that no *second* solution exists, so any lemma implying that no solution
> exists at all is false. Record it refuted, not weakened. Every lemma must
> state explicitly where the known solution sits relative to it — satisfied,
> excluded by hypothesis, or a genuine exception.

## The trap specific to this problem

The target is a **negative** statement, so the failure mode is an argument that
eliminates too much. The two ways it happens here:

- **Silently assuming both exponents are odd.** The reduction to odd primes is
  legitimate *after* the exponent-2 cases are separately proved. An argument
  that assumes it without having done that has not proved the theorem, and its
  conclusion will appear to exclude `(3,2,2,3)`, which should be caught
  immediately by the falsifier.
- **Dividing by something that vanishes.** Cyclotomic manipulations produce
  expressions that are zero exactly in the small cases. An argument that divides
  by one of them proves the statement everywhere except where it matters.

Both are caught by the same discipline: **every lemma is evaluated at the known
solution before it is believed.** This is cheap and it is not optional.

A third trap, of a different kind: **do not propose to finish by computation.**
The effective bound is astronomically larger than anything reachable, and a run
that spends itself extending a search is confirming what is already confirmed.
Establish the bound, state the gap in orders of magnitude, and stop.

## Compute policy — light, parallel, bounded

- **Exact integer arithmetic throughout.** Python integers are arbitrary
  precision; use them. No floats, no logarithms for comparison, no `math.pow`.
- **The container has an 8 GiB cap and an OOM kill writes nothing to the
  console.** Say what a run will cost before running it. An OOM is a finding
  about the method, not a reason to ask for more memory.
- **Parallelise over exponent pairs and over hypotheses, not over the size of a
  single search.** `code/lib/parallel.py` with `code/lib/PARALLEL.md` is in this
  workspace; the box has 28 CPUs and no container CPU quota. Verifying a
  divisibility condition across many `(p, q)` is exactly the shape
  `parallel_map` is for.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.

`symbolic_math` is the right role for the cyclotomic arithmetic — class numbers,
units and ideal factorisations in `Q(zeta_p)` are exactly what a computer
algebra system is for, and doing them by hand in prose is how this problem
produces confident nonsense. `lean_prover` suits the reduction to odd primes and
the exponent-2 cases, which are small and elementary.

## Ending

Stop and report when you have a partial result of the kind listed above, or when
you can state precisely what blocks **the route you actually pursued** and why.

Report: the `N` reached by the search and its runtime; the divisibility
conditions established, with proofs or with the range they were verified over;
where the known solution sits relative to every lemma; which claims are proved
versus verified numerically; the size of the effective bound and its distance
from feasibility; and every remaining `sorry`.
