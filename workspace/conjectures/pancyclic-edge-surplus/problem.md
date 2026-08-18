# The edge surplus of the sparsest pancyclic graph

*Erdős Problem #1016 (erdosproblems.com/1016), from [Er71]; originally a problem
of Bondy [Bo71].*

## Statement

A graph on `n` vertices is **pancyclic** if it contains a cycle of length `k`
for every `k` with `3 <= k <= n`. Let

```
h(n) = min { m - n : there is a pancyclic graph on n vertices with m edges },
```

so `n + h(n)` is the fewest edges a pancyclic graph on `n` vertices can have.

> **Question.** Estimate `h(n)`. In particular, is it true that
>
> ```
> h(n)  >=  log_2 n + log_* n - O(1),
> ```
>
> where `log_* n` is the iterated logarithm?

## What the statement does and does not say

- A pancyclic graph contains a Hamilton cycle (`k = n`), hence has at least `n`
  edges — so `h(n) >= 0` and the "surplus" framing is the right one. The
  question is how many **extra** edges beyond a Hamilton cycle are needed to
  realise every cycle length at once.
- `log_* n` is the iterated logarithm: the number of times `log_2` must be
  applied to reach at most `1`. It grows **absurdly slowly** — `log_* n <= 5`
  for every `n` below `2^65536`. **This is the crux of the problem's
  difficulty and must be stated in `CONTEXT.md` on day one:** the conjectured
  term is invisible to any computation that will ever be run, and any claim
  that computation supports or refutes the `log_*` term is false.
- What computation *can* do is settle `h(n)` exactly for small `n`, pin down the
  constant, and test the far weaker and still-open statement
  `h(n) - log_2 n -> infinity`.
- `h(n)` is a **finite exactly computable number** for each `n`: "is there a
  graph on `n` vertices with `m` edges containing a cycle of every length
  `3..n`?" is a decision problem.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **Bondy [Bo71]** claimed, without published details,
  ```
  log_2(n - 1) - 1   <=   h(n)   <=   log_2 n + log_* n + O(1).
  ```
- **Griffin [Gr13]** supplied a proof of the lower bound.
- **George, Khodkar and Wallis [GKW16]**, Chapter 4.5, appears to contain the
  first published proof of the upper bound.
- **Erdős [Er71]** believed the **upper** bound is closer to the truth — i.e.
  that the `log_*` term is real — but **could not even prove
  `h(n) - log_2 n -> infinity`.**

So the state is: the order `log_2 n` is settled at both ends; the open content is
the additive term, and even the weakest form of it (does `h(n) - log_2 n` grow at
all?) is open.

## The obstruction, stated honestly

1. **The lower bound `log_2 n - O(1)` is a counting argument and is tight in
   order.** A graph with `n + h` edges has a bounded cycle space (dimension
   `h + 1`), and the number of distinct cycle *lengths* it can realise is
   bounded by something exponential in `h` — which gives `h >> log n`
   immediately. **Re-derive this here on day one; it is short, and it is the
   scale of everything.**

2. **Getting an additive `log_* n` out of that counting is a different kind of
   argument.** The counting bound gives `2^h >= n`, so improving it means
   showing the cycle lengths a sparse graph realises are *further* constrained —
   not merely `2^h` many, but structured, so that covering an interval
   `{3,...,n}` costs extra. **An approach that only counts cannot produce a
   `log_*` term**, because counting saturates at `2^h`. The extra must come from
   an iterated/recursive structure, which is exactly where `log_*` comes from in
   the upper-bound construction.

3. **`log_*` is uncomputably slow.** No experiment distinguishes
   `log_2 n + C` from `log_2 n + log_* n + C`. **So the computational half of
   this run cannot address the headline question, and must not pretend to.**
   What it can do — exactly `h(n)` for small `n`, the exact constant, the
   structure of the extremal graphs — is genuinely useful and is what this
   workspace is for.

Stated as the thing to beat:

> **A proof that `h(n) - log_2 n -> infinity` must show that the cycle lengths
> realisable by a graph with `n + h` edges are not merely `<= 2^h` in number but
> constrained in position, so that covering `{3,...,n}` costs more than the
> counting bound demands. Counting alone saturates and cannot do this.**

Say which side the approach is on. Note that `h(n) - log_2 n -> infinity` is the
first real target, not the full `log_*`.

## The oracle: exact `h(n)`, and a witness checker

1. **`isPancyclic(G)`** — does `G` contain a cycle of every length `3..n`?
   Compute the full **cycle spectrum** (the set of realised cycle lengths). For
   small `n` this can be done exactly; note that deciding the existence of a
   cycle of a given length is NP-hard in general, so for larger `n` use a SAT/ILP
   encoding rather than a search that will silently miss cycles. **A cycle
   spectrum computed by an incomplete search is not a cycle spectrum, and a
   "pancyclic" witness produced by one is worthless.** Verify by hand on `K_4`
   (pancyclic) and on `C_n` (not, for `n >= 4`).

2. **`h(n)` exactly, for as many `n` as feasible.** For each `n` and each
   candidate surplus `h = 0, 1, 2, ...`, decide whether some graph on `n`
   vertices with `n + h` edges is pancyclic. Encode the whole thing as one
   satisfiability instance — edge variables plus, for each length `k`, a
   certificate that a `k`-cycle exists — with symmetry breaking, and **state the
   encoding and the symmetry breaking before running it.** Report the largest
   `n` reached, the method, and the wall clock.

3. **The extremal graphs themselves.** For each `n`, store every minimal
   pancyclic graph found in `code/out/`, in graph6, re-verified by an independent
   checker. **Their structure is the deliverable**: the upper-bound construction
   is recursive, and whether the exact optima look recursive at `n = 10..20` is
   the only empirical evidence about the `log_*` term this run can obtain — weak
   evidence, and it must be labelled as such.

4. **The falsification oracle.** Every claimed bound `h(n) >= g(n)` or
   `h(n) <= g(n)` is evaluated against the exact table. **A claimed lower bound
   exceeding a computed `h(n)` is false — refuted, not weakened.** Every claimed
   construction goes through `isPancyclic` at several `n` before its asymptotics
   are discussed.

**And the standing honesty check for this problem:** any statement of the form
"the computation supports/refutes the `log_* n` term" is false and must be
refused. `log_* n <= 5` throughout the computable range.

## Leads — verify each before relying on it

- **Bondy [Bo71]**: the original claim and whatever details exist.
- **Griffin [Gr13]**: the proof of the lower bound, and exactly where it is
  lossy.
- **George–Khodkar–Wallis [GKW16] Ch. 4.5**: the upper-bound construction in
  full. **Where the `log_*` comes from is the single most important thing to
  extract** — it is an iterated construction, and understanding the iteration is
  how one decides whether it is real or an artifact.
- **Cycle spectra of sparse graphs**: what is known about which sets of cycle
  lengths a graph with `n + h` edges can realise. This is the constraint the
  lower bound needs.
- **Bondy's meta-conjecture** ("almost every non-trivial condition implying
  Hamiltonicity implies pancyclicity") and the pancyclicity literature, for
  where sparse pancyclic constructions come from.
