# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on the order of
`m(n)` — the fewest edges in an `n`-uniform hypergraph with no proper
2-colouring. The bracket is
```
sqrt(n/log n) 2^n  <<  m(n)  <<  n^2 2^n,     conjectured  n 2^n.
```

## What a result looks like, in descending order of value

1. **An improved upper bound** — an `n`-uniform non-2-colourable hypergraph
   family with `o(n^2 2^n)` edges. This side has not moved since 1964 and is
   where a construction-capable run has the best chance.
2. **An improved lower bound** past `sqrt(n/log n) 2^n`, proved.
3. **Better bounds on `m(5)`**, with the search method stated and the
   symmetry breaking made explicit. Even a good upper bound for `m(5)` is new
   territory reachable by SAT.
4. **Exact `m(2)`, `m(3)` re-derived in-workspace**, and a verified 23-edge
   witness for `m(4) <= 23`. This is calibration, not a result, but no claim in
   this run means anything until it exists.
5. **A refutation of a natural approach**, with the obstruction named exactly.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing Property B, `n`-uniformity and `m(n)`,
  with every hypothesis as a binder, ending in `sorry`.
- The SAT-backed `hasPropertyB` decision procedure, verified by hand on the
  Fano plane (`n=3`, 7 edges — **not** 2-colourable) and on a 6-edge 3-uniform
  hypergraph (which must be 2-colourable since `m(3)=7`).
- The stated vertex bound making the search for `m(n)` finite.

## The falsification oracle

`m(2)=3`, `m(3)=7`, `m(4)=23` are the ground truth. **Every claimed lower bound
is evaluated at `n = 2,3,4`; one that exceeds a known value is refuted, not
weakened.** Every claimed construction is fed to `hasPropertyB`, and a
construction that turns out 2-colourable is refuted immediately.

Note the direction: an upper-bound claim is *witnessed* and dies to a single SAT
call, while a lower-bound claim is a statement about all hypergraphs and cannot
be checked directly — only sanity-checked at small `n`. Treat lower-bound claims
with correspondingly more suspicion, and state for each one where its
probabilistic step could be lossy.

## Stop conditions

A proved bound with its evidence class, or an exactly stated gap. Not: the
search reaching a larger `n`, and not the literature being exhausted.
