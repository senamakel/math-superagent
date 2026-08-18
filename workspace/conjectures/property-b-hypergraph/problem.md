# $m(n)$: the fewest edges in a non-2-colourable $n$-uniform hypergraph

*Erdős Problem #901 (erdosproblems.com/901), from Erdős–Lovász [ErLo75, p.610]
and [Er82e].*

## Statement

An `n`-uniform hypergraph `H` has **Property B** if its vertices can be
2-coloured with no edge monochromatic — equivalently, if there is a set `S` of
vertices meeting every edge but containing no edge. A hypergraph without
Property B is called **3-chromatic** in Erdős's terminology (its chromatic
number is `> 2`).

Let

```
m(n) = min { |E(H)| : H is n-uniform and does not have Property B }.
```

> **Question.** Estimate `m(n)`.

## What the statement does and does not say

- **`n`-uniform** means every edge has exactly `n` vertices. Edges may repeat
  vertices between them freely; there is no bound on the number of vertices, and
  the minimising hypergraph may use as many as it likes. (It is a standard first
  exercise that the number of vertices in a minimal example is bounded in terms
  of `m`; establish that bound here, because it is what makes the search finite.)
- **The quantity is a minimum over hypergraphs, of a maximum-like property.**
  Deciding whether one hypergraph has Property B is exactly 2-SAT-like in shape
  but NP-complete in general — it is a satisfiability question with one clause
  per edge in each colour. That is the entry point for the oracle.
- **Exact values are known and they are small**: `m(2) = 3`, `m(3) = 7`,
  `m(4) = 23`. `m(5)` is **not known** — the best bounds are far apart. Those
  four facts are the whole ground truth of this problem and every claim in this
  run is measured against them.
- The question is "estimate", so both a better upper bound (a construction) and a
  better lower bound (a proof) are results.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **`m(2) = 3`, `m(3) = 7`, `m(4) = 23`.** Reproduce `m(2)` and `m(3)` from
  scratch with the oracle — they are within exhaustive reach and they calibrate
  everything. `m(4) = 23` is a serious computation (Östergård); reproducing even
  the upper bound `m(4) <= 23` by finding a 23-edge 4-uniform example is a
  meaningful exercise for the oracle.
- **Erdős** proved `2^n << m(n) << n^2 2^n` (lower bound [Er63b], upper bound
  [Er64e]). The lower bound is the one-line union bound over 2-colourings; the
  upper bound is the random construction. **Re-derive both here on day one** —
  they are short and they set the scale.
- **Erdős conjectured `m(n)/2^n -> infinity`**, proved by **Beck [Be77]** with
  `m(n) >> (log n) 2^n`, improved by Beck [Be78] to `n^{1/3 - o(1)} 2^n`.
- **Radhakrishnan and Srinivasan [RaSr00]** improved this to
  ```
  m(n) >> sqrt(n / log n) * 2^n,
  ```
  which is the **current best lower bound**. Its proof is a random 2-colouring
  with a re-colouring/repair step, and it is short enough to reconstruct.
- **Pluhár [Pl09]** gave a very short proof of `m(n) >> n^{1/4} 2^n` — weaker,
  but the simplest argument in the area and the best place to start.
- **Erdős and Lovász [ErLo75] speculate that `n 2^n` is the right order.**

So the gap is
```
sqrt(n/log n) * 2^n   <<   m(n)   <<   n^2 * 2^n,
```
with `n 2^n` conjectured. **Both ends are open, and the upper bound `n^2 2^n`
has not moved since 1964.** Say this in `CONTEXT.md` on day one.

## The obstruction, stated honestly

1. **The lower bound is a probabilistic argument that has been pushed hard.**
   Union bound gives `2^n`; the Lovász Local Lemma and the Radhakrishnan–
   Srinivasan repair argument give `sqrt(n/log n) 2^n`. Getting to `n 2^n` from
   below appears to need a genuinely different idea, and **an approach that is a
   refinement of the random colouring is attacking the well-worked side.**

2. **The upper bound has barely moved in sixty years, and it is a
   *construction*.** `n^2 2^n` comes from a random `n`-uniform hypergraph on a
   suitable vertex set. Constructions are checkable and improvable, and **the
   gap between `n^2` and the conjectured `n` is a factor of `n` sitting on the
   side of the problem where evidence is cheap.** If this run is to contribute
   anything, the upper bound is the more likely place.

3. **Exact values stop at `n = 4` for a reason.** `m(5)` is a search over
   hypergraphs with tens of edges on a dozen-plus vertices, with a co-NP inner
   test. It is not a plain enumeration and **must not be attempted as one.**
   The right shape is SAT/CP with symmetry breaking, and even bounding `m(5)`
   better than the literature would be a genuine result.

Stated as the thing to beat:

> **A better upper bound must exhibit (or prove the existence of) an
> `n`-uniform non-2-colourable hypergraph with `o(n^2 2^n)` edges; a better lower
> bound must beat the random-colouring-plus-repair argument, which is where
> every improvement of the last twenty-five years has come from.**

Say which side the approach is on, and if it is on the lower-bound side, say
what it does that the repair argument does not.

## The oracle: a Property-B decision procedure, and the falsifier

1. **`hasPropertyB(H)`** — given an explicit `n`-uniform hypergraph, decide
   2-colourability with no monochromatic edge. **This is a SAT instance:** one
   variable per vertex, and for each edge two clauses (not-all-true and
   not-all-false). Use `sat_solver`; do not enumerate colourings past `20`
   vertices. Verify by hand on the Fano plane (`n = 3`, 7 edges, 7 vertices,
   **not** 2-colourable) and on any 6-edge 3-uniform hypergraph (which must be
   2-colourable, since `m(3) = 7`).

2. **`m(n)` exactly, for `n = 2, 3`**, by search with symmetry breaking, and the
   best upper bound the run can construct for `n = 4, 5`. **Report the method,
   the symmetry breaking used, and the wall clock.** A claimed exact `m(4) = 23`
   requires both a 23-edge example (SAT, easy to verify) and an exhaustive proof
   that 22 edges never suffice (hard — say honestly which half was done).

3. **A vertex bound.** Establish and use the standard bound on the number of
   vertices a minimal example needs, so the search space is finite and stated.
   Without it the search is not a search.

4. **The falsification oracle.** Any claimed lower bound `m(n) >= g(n)` is
   checked against `m(2)=3`, `m(3)=7`, `m(4)=23` — **a bound exceeding one of
   these is false, record it refuted, not weakened.** Any claimed construction
   is fed to `hasPropertyB` and must come back "not 2-colourable"; a claimed
   construction that is 2-colourable is refuted immediately. **Every asymptotic
   claim in this run must be evaluated at `n = 2,3,4` before it is believed.**

Expect `n <= 4` to be unable to distinguish `sqrt(n)` from `n` from `n^2`. That
is not a reason to skip it. It is the only thing standing between the run and a
plausible false theorem.

## Leads — verify each before relying on it

- **[RaSr00]** in full: the repair argument, the exact constant, and where it
  loses.
- **Pluhár [Pl09]**: the short proof, as the cheapest entry point.
- **Beck [Be77], [Be78]** and the Lovász Local Lemma formulation of the lower
  bound.
- **Erdős [Er64e]**: the random construction giving `n^2 2^n`, in full detail —
  including exactly where the `n^2` comes from, because that is the factor to
  attack.
- **Östergård** and the computation of `m(4) = 23`: what search space, what
  symmetry breaking, what hardware. It is the template for any attempt at `m(5)`.
- **Property B and the Lovász Local Lemma**, the algorithmic (Moser–Tardos)
  version, and whether it constructs anything here.
