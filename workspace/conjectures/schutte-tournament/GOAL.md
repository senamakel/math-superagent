# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on the order of `f(n)`,
the fewest vertices in a tournament in which every `n` vertices are dominated by
some other vertex. The bracket is
```
c * n * 2^n   <=   f(n)   <=   C * n^2 * 2^n,
```
unmoved since 1965.

## What a result looks like, in descending order of value

1. **An improved upper bound** — a tournament family on `o(n^2 2^n)` vertices
   with property `S_n`, or a proof one exists.
2. **An improved lower bound** past `n 2^n`, proved.
3. **New bounds on `f(4)`**, with the SAT encoding, the symmetry breaking, and
   the wall clock stated. Either end would be new territory.
4. **An explicit (derandomised) construction** closer to `n^2 2^n` than the
   Paley threshold. The explicit-versus-random gap is a recognised objective and
   progress there is a real result.
5. **The 19-vertex `S_3` witness re-derived in-workspace**, and `f(1)=3`,
   `f(2)=7` re-proved. This is calibration, not a result, but no claim in this
   run means anything until it exists.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing tournaments, property `S_n` and `f(n)`,
  with every quantifier as a binder, ending in `sorry`.
- `hasS_n(T)` verified by hand on the 3-cycle (`S_1`: yes), the Paley tournament
  on 7 vertices (`S_2`: yes), and some tournament on 6 vertices (`S_2`: must be
  no, since `f(2) = 7`).
- The SAT encoding written out with its clause count, and the symmetry breaking
  named and classified as complete or partial. **An unstated symmetry breaking
  makes a lower-bound search unciteable.**

## The falsification oracle

`f(1)=3`, `f(2)=7`, `f(3)=19` are the ground truth. Every claimed bound —
either direction — is evaluated there first. **A lower bound exceeding a known
value is refuted, not weakened; an upper bound below one is refuted.**

Note the asymmetry: an upper bound is *witnessed* by a tournament and dies to a
single `hasS_n` call, while a lower bound asserts that no tournament on `N-1`
vertices works and is only as good as the exhaustiveness of its search or the
rigour of its proof. **A SAT-based lower bound is a theorem only if the encoding
is faithful and the symmetry breaking is satisfiability-preserving** — state
both, or report the result as a search outcome rather than as a bound.

## Stop conditions

A proved bound with its evidence class, or an exactly stated gap. Not: the
search reaching a larger `N`, and not the literature being exhausted.
