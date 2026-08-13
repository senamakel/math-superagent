# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**. The conjecture has
stood since 1971 and is believed true, so the working assumption is that you
will not prove it. Claiming it on an argument that has not survived attack is
the one outright failure available here.

A partial result that would count:

- an **effective** bound on the number of solutions to `C(x,k1) = C(y,k2)` for
  a specific family of `(k1,k2)`, with the constant **computed**, not cited as
  existing;
- a precise statement of what Matomäki–Radziwiłł–Shao–Tao–Teräväinen leaves
  open — the exact range of `k` their interior result does not cover, and what
  would be needed to close it;
- the genus of `C(x,k1) = C(y,k2)` computed as a function of `k1, k2`, with the
  threshold above which Faltings applies made explicit;
- a proof that a stated approach **cannot** give a bound uniform in `k1, k2`,
  with the obstruction named — a clean impossibility for a method is worth as
  much as a bound;
- the infinite family with `N(a) >= 6` verified and stated exactly, since it
  is the reason `B >= 6` and constrains every proposed proof;
- a reproduction of a known `O(log a / log log a)`-type bound with its constant
  made explicit.

A result stated without the bound it was established under is not a result. A
count verified for `n <= 10^6` is a fact about `n <= 10^6`.

## The oracle here is an exact multiplicity counter and a falsifier

There is no value to recompute — the answer is a bound. So the oracle is:

1. **`multiplicity(a, n_max)`** — the exact count of `(n,k)` with `C(n,k) = a`
   and `n <= n_max`, in exact integer arithmetic. **State the convention**:
   whether `k` and `n-k` are counted once or twice. Every claim must use the
   same one, and a bound of 8 under one convention is 4 under the other.

2. **`genus(k1, k2)`** — the genus of the curve `C(x,k1) = C(y,k2)`, computed
   rather than assumed, because the Faltings threshold is exactly where it
   exceeds 1.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed bound must be run against the witness set** in
> `code/out/witnesses.json`, which holds `3003` with its eight occurrences and
> the other high-multiplicity numbers found by direct computation. A claimed
> bound `B < 8`, or any lemma implying one, is **false** — 3003 refutes it.
> Full stop: record it refuted, not weakened.

This is the specific way a proof here goes wrong. Singmaster asserts a bound,
so the tempting error is an argument that proves a bound *too small*, and 3003
is the three-line check that catches it. Any argument that would also rule out
`C(15,5) = C(14,6) = 3003` is wrong, whatever else it establishes.

## Compute policy — light, symbolic, parallel

Searching for a number with multiplicity 9 is not the deliverable and will not
find one. Keep numerical work in service of the argument.

- **Never build the triangle.** `C(n,k)` for the relevant ranges is enormous;
  compute multiplicities by inverting `C(n,k) = a` for each small `k`
  (binary search in `n`), which is `O(log)` per `k` and needs no table.
- **Bound `k`.** For fixed `a`, `C(n,k) >= C(2k,k) >= 2^k`, so only
  `k <= log2(a)` can occur. State that bound and use it; it is what makes the
  counter cheap.
- **Parallelise across `a` or across `(k1,k2)` pairs**, which are independent.
  `code/lib/parallel.py` with `code/lib/PARALLEL.md` is in this workspace; the
  box has 28 CPUs and the container has no CPU quota. Say in every capture how
  many workers ran and what range was covered.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.
- **The container cap is 8 GiB** and an OOM kill writes nothing to the console.
  Say what a run will cost before running it.

`smt_solver` and `sat_solver` are available and the temptation is to throw the
Diophantine system at Z3. Be honest about what that can return: an `unknown` is
**not** a proof, and `non-answers reported` above 0 means one was treated as an
answer. A `sat`/`unsat` result is only meaningful with the encoding size and
the exact bounds stated alongside it. Nonlinear integer arithmetic is
undecidable in general, so expect `unknown` and plan what to do with it.

## The trap specific to this problem

**Finiteness is not a bound.** Faltings and Siegel both give "finitely many"
without a computable count, and for each fixed `(k1,k2)` that is already known.
Singmaster needs uniformity over all `(k1,k2)` at once. An argument that
establishes finiteness for each pair separately has proved something true and
already known, and has not moved the conjecture. Every claim must say whether
its bound is **effective** and whether it is **uniform in `k`**.

## Ending

Stop and report when you have a partial result of the kind listed above, or
when you can state precisely what blocks the argument and why. Report the
convention used for counting, the witnesses reproduced, which bounds are
effective and which are not, and the evidence class of every claim.
