# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on `h_3(k)`, the fewest
vertices in a triangle-free graph of chromatic number `k`: an asymptotic
formula, or the ratio statement `h_3(k+1)/h_3(k) -> 1`.

## The two halves are not equally reachable — choose deliberately

- The **asymptotic constant** in `h_3(k) ~ c k^2 log k` is entangled with the
  asymptotics of `R(3,k)` (Erdős Problem #165). An approach that would settle it
  must say why it beats that barrier. Expect not to.
- The **ratio statement** `h_3(k+1)/h_3(k) -> 1` may not need the constant. It
  asks for a construction turning a `k`-chromatic triangle-free graph on `n`
  vertices into a `(k+1)`-chromatic one on `(1+o(1))n` vertices. Mycielski's
  construction does it at cost factor `~2`. **Beating `2` — by any amount, even
  `1.9` — is a real result and is the target with the best ratio of
  reachability to value.**

State in `CONTEXT.md` which half this run is attacking and why.

## What a result looks like, in descending order of value

1. **The ratio statement proved**, or any construction incrementing the
   chromatic number at vertex-cost factor `< 2`.
2. **An improved constant** at either end of
   `(1/2-o(1)) k^2 log k <= h_3(k) <= (1+o(1)) k^2 log k`, proved.
3. **New bounds on `h_3(6)`** — the smallest open value. An upper bound is a
   single graph, verifiable in seconds by the oracle.
4. **`h_3(3)=5`, `h_3(4)=11`, `h_3(5)=21` re-derived in-workspace** with exact
   chromatic numbers. Calibration, not a result, but nothing else counts until
   it exists.
5. **A refutation of a natural approach**, with the obstruction named exactly —
   in particular a proof that a class of amalgamation constructions cannot beat
   cost factor `2`.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing triangle-freeness, chromatic number and
  `h_3(k)`, with every hypothesis as a binder, ending in `sorry`.
- Exact `chi(G)` via SAT/ILP — **never a greedy or heuristic colouring** — with
  the Grötzsch graph (`chi = 4`, 11 vertices, triangle-free) reproduced by the
  oracle on its own.
- Every witness graph stored explicitly in `code/out/` and re-verified by a
  checker that did not find it.

## The falsification oracle

Ground truth: `h_3(3)=5`, `h_3(4)=11`, `h_3(5)=21`. Every claimed bound is
evaluated there; **one exceeding a known value is refuted, not weakened.**

The characteristic failure of this problem is a **witness that is not actually
`k`-chromatic** — a heuristic colouring failed to find a `(k-1)`-colouring and
was read as a proof that none exists. Every witness carries an exact `chi`
computed by a complete method, and the negative half (no `(k-1)`-colouring) is
the half that must be certified.

## Stop conditions

A proved bound or construction with its evidence class, or an exactly stated
gap. Not: the search reaching a larger `k`, and not the literature being
exhausted.
