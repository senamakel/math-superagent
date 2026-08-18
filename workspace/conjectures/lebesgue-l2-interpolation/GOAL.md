# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on
`min I = 2 - (1+o(1))/n`, where
`I(x_1..x_n) = integral_{-1}^{1} sum_k l_k(x)^2 dx` over node systems in
`[-1,1]`.

## The problem, restated so the run cannot lose sight of it

The upper bound `min I <= 2 - 2/(2n-1) = 2 - (1+o(1))/n` is **already proved**
and constructive. The open half is the **lower bound**: [ESVV94] gives
`min I >= 2 - O((log n)^2 / n)`, and the conjecture asks to replace `(log n)^2`
by `O(1)`. A run that produces yet another construction has produced nothing
new. **Locate the step that loses `(log n)^2` and attack it.**

## What a result looks like, in descending order of value

1. **`min I >= 2 - C/n`** for an absolute constant `C`. This is the conjecture.
2. **Any improvement on `(log n)^2`** — `log n`, `(log log n)^2`, anything
   asymptotically smaller — proved.
3. **The exact minimiser and exact `min I` for a range of `n`**, obtained from
   the critical-point polynomial system, with the structure of the optimal node
   system described and a conjecture for its asymptotics.
4. **A proof that `(log n)^2` is necessary for the [ESVV94] method**, i.e. an
   exact obstruction to that argument, with a different method proposed.
5. **A refutation of a natural approach**, with the obstruction named exactly.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing `I` and the conjecture, with node
  distinctness and the interval as binders, ending in `sorry`.
- The exact rational oracle, verified against the hand computation `n = 2`,
  nodes `{-1,1}`, `I = 4/3`.
- The table of `n`, exact `min I`, and `n*(2 - min I)` — the column that decides
  whether the conjectured constant `1` is even right.

## The falsification oracle

Every claimed lower bound is evaluated against the exact optimum for every `n`
in the table; a bound exceeding a computed `min I` is **refuted**, not weakened.

The standing trap: **Erdős's own first guess was wrong.** The
Legendre-integral nodes are *not* optimal for `n > 3` (Szabados). Any lemma
implying they are is false, and this is the cheapest check available here — run
every structural claim against `n = 4,...,7` before believing it.

## Stop conditions

A proved bound with its evidence class, or an exactly stated gap naming the step
that resists. Not: a better construction, and not the literature being
exhausted.
