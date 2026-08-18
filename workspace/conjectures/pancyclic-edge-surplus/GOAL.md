# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on `h(n)` — the fewest
extra edges beyond `n` that a pancyclic graph on `n` vertices needs. The known
bracket is
```
log_2(n-1) - 1   <=   h(n)   <=   log_2 n + log_* n + O(1).
```

## The honesty constraint that governs this run

`log_* n <= 5` for every `n` below `2^65536`. **No computation this run can
perform says anything about the `log_*` term.** Any claim that the data supports
or refutes it is false and must be refused, in `CONTEXT.md`, in every claim
block, and in the final report.

The first real target is therefore the far weaker, still-open statement Erdős
could not prove:

> **`h(n) - log_2 n -> infinity`.**

## What a result looks like, in descending order of value

1. **`h(n) - log_2 n -> infinity`**, proved. This is Erdős's own stated gap.
2. **Any improvement to the additive constant** at either end, proved.
3. **Exact `h(n)` for a range of `n`**, with the encoding, the symmetry breaking
   and the wall clock stated, plus the minimal pancyclic graphs themselves and a
   description of their structure.
4. **A proof that the counting argument saturates** — i.e. an exact obstruction
   showing that no purely counting-based argument can give more than
   `log_2 n - O(1)`, with a different mechanism proposed.
5. **A refutation of a natural approach**, with the obstruction named exactly.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing pancyclicity and `h(n)`, with every
  hypothesis as a binder, ending in `sorry`.
- A **complete** cycle-spectrum computation — SAT/ILP-backed, never an
  incomplete search — verified by hand on `K_4` (pancyclic) and `C_n`
  (`n >= 4`, not pancyclic).
- Every minimal pancyclic graph stored in graph6 in `code/out/` and re-verified
  by a checker that did not find it.

## The falsification oracle

Every claimed bound is evaluated against the exact table of `h(n)`. **A claimed
lower bound exceeding a computed `h(n)` is refuted, not weakened.** Every
claimed construction is run through the complete pancyclicity check at several
`n` before its asymptotics are discussed.

The characteristic failure here is a **false negative**: an incomplete cycle
search reports a length missing, or fails to find a cycle that exists, and a
graph is misclassified. The check must be complete, and the completeness is what
gets certified.

## Stop conditions

A proved bound with its evidence class, or an exactly stated gap. Not: the
search reaching a larger `n`, and not the literature being exhausted.
