# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on
`F(n) / log n -> infinity`, where `F(n)` is the largest `k` such that every
graph on `n` vertices has an induced regular subgraph on `k` vertices.
Equivalently `G(k) <= 2^{o(k)}` for the dual function.

## The problem, restated so the run cannot lose sight of it

`F(n) >> log n` is Ramsey's theorem, and **nothing better is known**. The
believed truth is around `n^{1/2}`, and the known upper bound is `n^{1/2}`. So
the conjecture is a *very weak* statement that is nonetheless completely open,
and any improvement of the lower bound — `F(n) >> (log n)^{1+c}`, or
`F(n) - t(n) -> infinity` for `t(n)` the Ramsey bound — is a genuine result.

## What a result looks like, in descending order of value

1. **Any lower bound beating Ramsey**, proved. This is the conjecture's content.
2. **An improved bound on `G(6)` or `G(7)`.** A lower bound needs one explicit
   graph and is verifiable in seconds; this is the most reachable new fact in
   the problem.
3. **Exact `G(6)`**, if the search can be made to terminate, with the generation
   method and symmetry breaking stated.
4. **A sharpened upper bound** below `n^{1/2}`, or a construction showing
   `n^{1/2}` is tight.
5. **A refutation of a natural approach**, with the obstruction named exactly —
   in particular, a proof that some class of argument can only ever produce a
   trivial regular induced subgraph.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing induced regular subgraphs, `F(n)` and
  `G(k)`, with every hypothesis as a binder, ending in `sorry`.
- `maxRegularInduced(G)` as a SAT/ILP procedure — **not** subset enumeration —
  verified by hand on `C_5` and the Petersen graph.
- Every extremal graph stored explicitly in `code/out/` and re-verified by an
  independent checker, never by the search that produced it.

## The falsification oracle

The ground truth is `F(5)=3`, `F(7)=4`, `G(3)=5`, `G(4)=7`, `G(5)=17`,
`G(6)>=21`, `G(7)>=30`. Every claimed bound is evaluated there. **A claimed
lower bound on `F` exceeding `F(5)=3` or `F(7)=4` is refuted, not weakened.**

The standing structural check, which catches the characteristic failure of this
problem: **for every argument, name the regular induced subgraph it actually
produces.** If it is a clique or an independent set, the argument is Ramsey in
disguise and has improved nothing, however it is dressed.

## Stop conditions

A proved bound with its evidence class, or an exactly stated gap. Not: the
search reaching a larger `k`, and not the literature being exhausted.
