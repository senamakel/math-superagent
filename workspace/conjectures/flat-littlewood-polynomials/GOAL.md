# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on: is there `c > 0`
with `max_{|z|=1}|P(z)| > (1+c)sqrt(n)` for every degree-`n` Littlewood
(`±1`-coefficient) polynomial `P`? The one outright failure available here is
claiming the conjecture on an argument that has not survived attack.

## What a result looks like, in descending order of value

1. **The conjecture, or a counterexample family.** An explicit `±1` family with
   `||P_n||_inf / sqrt(n) -> 1` disproves it and is checkable by the oracle.
2. **An unconditional constant.** Any proved `c > 0`, however small, for all
   large `n`. This is the real target.
3. **A conditional constant with the hypothesis stated exactly** — e.g. `c > 0`
   given a bounded merit factor. Label it conditional in the claim block, in
   Lean (`axiom` under `Cited` or an explicit hypothesis binder), and in
   `CONTEXT.md`. A conditional result presented as unconditional is the failure
   this file exists to prevent.
4. **Exact `m(n) = min_P ||P||_inf` for a new range of `n`**, certified, with the
   sequence `m(n)/sqrt(n)` and what it does or does not rule out.
5. **A refutation of a natural approach**, with the obstruction named exactly.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing the conjecture itself, with every
  hypothesis as a binder, ending in `sorry`.
- A **certified** `supnorm` (root-isolation, not sampling) and an exact
  `L4norm` from integer autocorrelations, both verified by hand on
  `P(z) = 1 + z` and on the degree-3 Rudin–Shapiro polynomial.
- The Parseval bound `||P||_inf >= sqrt(n+1)` re-derived here, and every
  computed `m(n)` checked against it.

## The falsification oracle

Every claimed lower bound is evaluated at the exact minimisers `m(n)` and at the
Rudin–Shapiro family. A bound exceeding a computed `m(n)` is **refuted**, not
weakened. Every claimed flat family is run through the certified `supnorm` at
several `n` before its asymptotics are discussed.

Note the direction: the conjecture asserts that *nothing* is flat. The dangerous
failure is therefore an argument that proves too much — one that would also
exclude Kahane's unimodular ultraflat polynomials. **Every lemma must state
where Kahane's construction sits relative to it.** A lemma that also kills the
unimodular case has silently dropped the discreteness hypothesis and is false.

## Stop conditions

- A proof or counterexample that survives the run's own attack, or
- an exactly stated partial result with its evidence class and its remaining gap
  named, filed as a claim and as a Lean statement.

Not a stop condition: the literature being exhausted, or the search reaching a
larger `n`.
