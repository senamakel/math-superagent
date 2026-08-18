# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on whether
`f(n+1) >= f(n)` for all large `n`, where `f(n)` is the least minimum degree
forcing a `C_4` in an `n`-vertex graph.

## What makes this problem different from its neighbours

The asymptotics are known: `f(n) = (1+o(1))sqrt(n)` and `f(n) < sqrt(n)+1`. **No
asymptotic estimate answers this question.** It is a statement about the local
behaviour of a specific integer sequence, so **computing the sequence exactly is
not preliminary work here — it is the main line.**

## What a result looks like, in descending order of value

1. **A proof of monotonicity for large `n`**, or **a counterexample `n` with
   `f(n+1) < f(n)`**, certified in both directions.
2. **The weaker form** `f(m) > f(n) - c` for all `m > n`, proved with an explicit
   `c`.
3. **The table of exact `f(n)`** for a new range, with each entry labelled by
   which half was certified: the witness graph (upper bound on the max `C_4`-free
   minimum degree) and the unsatisfiability proof (lower bound). A table hiding
   which is which is worthless.
4. **The behaviour of `f` near `n = q^2 + q + 1`** — the polarity-graph values,
   the windows above and below, and whether the sequence is locally flat, rising,
   or drops. **This is where a counterexample lives if there is one.**
5. **A refutation of a natural approach**, with the obstruction named exactly —
   in particular, a proof that no deletion/contraction argument converts an
   extremal `C_4`-free graph on `n+1` vertices into one on `n`.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing `C_4`-freeness, minimum degree and
  `f(n)`, with every hypothesis as a binder, ending in `sorry`.
- The SAT encoding of `exists(n,d)` written out with its clause count, and the
  symmetry breaking named and classified as complete or partial.
- `f(4) = 2` reproduced by the oracle on its own, and the Erdős–Rényi polarity
  graphs constructed and independently verified `C_4`-free.

## The falsification oracle

Every entry in the `f` table is two claims, not one: a witness graph and an
unsatisfiability result. **Report both, or report the entry as a bound.** Every
claimed general statement is evaluated against every computed entry; one that
contradicts an entry is **refuted, not weakened**.

The characteristic failure of this problem is an **asymptotic argument dressed
as an answer**. Monotonicity is not implied by any estimate with an `o(sqrt n)`
error, since the sequence moves by `1`. Whenever an estimate appears in this
run, state explicitly whether it could possibly bear on monotonicity. Usually it
cannot.

## Stop conditions

A proof, a certified counterexample, or an exactly stated gap plus the table.
Not: the search reaching a larger `n`, and not the literature being exhausted.
