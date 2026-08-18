# $h_3(k)$: the smallest triangle-free graph of chromatic number $k$

*Erdős Problem #1013 (erdosproblems.com/1013), from [Er71].*

## Statement

Let

```
h_3(k) = min { n : there is a triangle-free graph on n vertices with chromatic number k }.
```

> **Question.** Find an asymptotic formula for `h_3(k)`, and prove
>
> ```
> lim_{k -> infinity}  h_3(k+1) / h_3(k)  =  1.
> ```

## What the statement does and does not say

- **Triangle-free** means no `K_3` as a subgraph. Chromatic number `k` means
  exactly `k` (equivalently, at least `k` — a graph with chromatic number `> k`
  contains an induced subgraph of chromatic number exactly `k`, so the two
  readings give the same minimum; establish this small fact here, since the Lean
  statement has to pick one).
- **`h_3` is the inverse of a maximum.** With
  `f(n) = max { chi(G) : G triangle-free on n vertices }` (Erdős Problem #1104),
  `h_3(k) = n` iff `n` is minimal with `f(n) = k`. **The two problems are the
  same problem, and every bound transfers.** Say so in `CONTEXT.md` on day one
  and use whichever direction is easier at each step.
- **The second question is a ratio, not a formula.** `h_3(k+1)/h_3(k) -> 1`
  says the sequence has no jumps at scale — it does *not* follow from any known
  asymptotic bound with a constant-factor gap, and it is the more approachable
  half only if the asymptotics are pinned down. Note carefully: the known
  bracket `(1/2 - o(1)) k^2 log k <= h_3(k) <= (1+o(1)) k^2 log k` has a factor-2
  gap, and **a factor-2 gap does not imply the ratio tends to 1.** They are
  genuinely different targets.
- Every value `h_3(k)` is a **finite exactly computable number**. The known ones
  are famous graphs.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **Exact small values.** `h_3(1) = 1`, `h_3(2) = 2`, `h_3(3) = 5` (the
  5-cycle), `h_3(4) = 11` (the **Grötzsch graph**), `h_3(5) = 21` (Chvátal;
  the 21-vertex example, and the exhaustive proof that 20 vertices do not
  suffice). **`h_3(6)` is not known exactly** — verify the current bracket for
  it, which is the smallest genuinely open value and therefore the natural
  computational target of this run.
- **Graver and Yackel [GrYa68]** proved
  ```
  h_3(k)  >>  k^2 * log k / log log k.
  ```
- The bounds for `f(n)` from Erdős Problem #1104 imply
  ```
  (1/2 - o(1)) k^2 log k   <=   h_3(k)   <=   (1 + o(1)) k^2 log k.
  ```
  Track down exactly which results on `f(n)` these come from (they are the
  Ajtai–Komlós–Szemerédi / Shearer independence-number bounds for triangle-free
  graphs, and Kim's construction, in some combination) and **state precisely
  which theorem supplies which end.** That attribution is the single most useful
  early deliverable here, because it says which end is which technique's.
- See Erdős Problem #920 for the `K_r`-free generalisation, and #1104 for the
  dual function.

So the state is: **the order `k^2 log k` is known, the constant is not**, and
the ratio question is open.

## The obstruction, stated honestly

1. **The two ends come from different machinery and neither is tight.** The
   upper bound on `h_3` (a small triangle-free graph with large chromatic
   number) comes from a random or pseudo-random construction — Kim's
   `R(3,k) >> k^2/log k` construction and its relatives — and the lower bound
   comes from independence-number theorems (every triangle-free graph on `n`
   vertices has an independent set of size `>> sqrt(n log n)`, so
   `chi >> sqrt(n/log n)`). **The factor 2 between them is the gap between the
   best known independence bound and the best known construction, and closing it
   is essentially the `R(3,k)` problem** — Erdős Problem #165, one of the
   best-known open problems in the area.

2. **So the asymptotic half of this problem is not independent of `R(3,k)`.**
   Say so plainly, and do not spend the run rediscovering that. **The ratio
   question `h_3(k+1)/h_3(k) -> 1` is the half that might not need it**, since
   a smoothness statement can sometimes be proved without knowing the function —
   by an amalgamation or interpolation construction turning a `k`-chromatic
   triangle-free graph on `n` vertices into a `(k+1)`-chromatic one on
   `(1+o(1)) n` vertices. **That is the target with the best ratio of
   reachability to value, and it should be attacked directly.**

3. **Exact values stop at `k = 5` for a reason.** `h_3(6)` needs either a small
   triangle-free 6-chromatic graph (an upper bound — checkable in seconds) or an
   exhaustive proof that none is smaller (a search over all triangle-free graphs
   on ~30–40 vertices, which is not an enumeration).

Stated as the thing to beat:

> **Improving the constant in `h_3(k) ~ c k^2 log k` requires improving either
> the triangle-free independence-number bound or the Ramsey-type construction —
> i.e. it is the `R(3,k)` problem. The ratio statement may be reachable without
> that, via a construction that increments the chromatic number at sublinear
> vertex cost.**

Say which of these the approach is on. An approach that would settle the
constant should say why it beats the `R(3,k)` barrier.

## The oracle: exact chromatic numbers, and the falsifier

1. **`isTriangleFree(G)` and `chi(G)`**, exactly. Chromatic number is a SAT/ILP
   question — one Boolean per (vertex, colour) pair, at-least-one-colour per
   vertex, and a conflict clause per edge and colour — and it must be computed
   that way, never by greedy or heuristic colouring. **A heuristic upper bound
   on `chi` is not `chi`, and a claimed `k`-chromatic witness that is actually
   `(k-1)`-colourable is the characteristic failure of this problem.**

2. **Calibration, before any new graph is tried.** The oracle must confirm, on
   its own: `C_5` is triangle-free with `chi = 3`; the **Grötzsch graph** is
   triangle-free on 11 vertices with `chi = 4`; and Chvátal's 21-vertex graph is
   triangle-free with `chi = 5`. Also that no triangle-free graph on 10 vertices
   is 4-chromatic (a bounded search, feasible). An oracle that cannot reproduce
   `h_3(4) = 11` makes every later number worthless.

3. **`h_3(6)`.** Search for small triangle-free 6-chromatic graphs — Mycielski's
   construction gives one, of a known and probably non-optimal size, so compute
   it and then try to beat it. **Report the best upper bound found, the method,
   and the wall clock.** A lower bound requires exhaustive generation of
   triangle-free graphs with symmetry breaking; say honestly whether it was done.

4. **The falsification oracle.** Every claimed bound is evaluated at
   `h_3(3)=5`, `h_3(4)=11`, `h_3(5)=21`. **A claimed lower bound exceeding one
   of these is false — refuted, not weakened.** Every claimed witness graph goes
   through `isTriangleFree` and exact `chi` before it is written into any file.

Expect `k <= 5` to say nothing about a `k^2 log k` constant. Compute it anyway;
it is the only thing standing between the run and a plausible false theorem.

## Leads — verify each before relying on it

- **Erdős Problem #1104** (the dual `f(n)`) and exactly which theorems give the
  `(1/2 - o(1))` and `(1 + o(1))` constants.
- **Mycielski's construction**: it increments the chromatic number while keeping
  triangle-freeness, at the cost of roughly doubling the vertex count. **The
  ratio question is precisely asking for a construction that does this at
  `(1+o(1))` cost instead of `2`** — so Mycielski is both the baseline and the
  thing to beat, and understanding exactly why it doubles is the first step.
- **Grötzsch (11 vertices, `chi=4`)** and **Chvátal (21 vertices, `chi=5`)**:
  their structures, and whether they are Mycielskian or something better.
- **Ajtai–Komlós–Szemerédi and Shearer**: the independence number of
  triangle-free graphs, which supplies the lower bound.
- **Kim's `R(3,k)` construction** and its relation to the upper bound.
- **Erdős Problem #165** (asymptotics of `R(3,k)`) and #920 (`K_r`-free), for
  where this problem sits.
