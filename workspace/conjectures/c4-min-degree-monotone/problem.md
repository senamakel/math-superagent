# Is the minimum degree forcing a $C_4$ monotone in $n$?

*Erdős Problem #85 (erdosproblems.com/85), stated in [Er93, p.345], [Er94b],
[Er95], [Er96].*

## Statement

For `n >= 4` let

```
f(n) = min { d : every graph on n vertices with minimum degree >= d contains a C_4 }.
```

Equivalently, `f(n) - 1` is the largest minimum degree of a `C_4`-free graph on
`n` vertices.

> **Question.** Is it true that, for all large `n`,
>
> ```
> f(n + 1)  >=  f(n) ?
> ```

A weaker form, also open: is there a constant `c` with `f(m) > f(n) - c` for all
`m > n`?

## What the statement does and does not say

- **`C_4` means a cycle of length exactly 4** — four distinct vertices in a
  4-cycle. Not `K_4`, and not "a cycle of length at most 4".
- **Minimum degree, not average degree, and not edge count.** The classical
  Turán-type problem `ex(n; C_4)` bounds *edges*; this is a *minimum degree*
  problem and the two are genuinely different — a graph can have many edges and
  a low-degree vertex.
- **The question is monotonicity, not growth.** The asymptotics are essentially
  known: `f(n) = (1 + o(1)) sqrt(n)` and `f(n) < sqrt(n) + 1`. So the answer is
  known to within `1 + o(1)`, and **the entire open content is whether the
  sequence ever goes *down***. That is what makes this a genuinely
  computation-friendly problem: it is a question about a specific integer
  sequence, and computing the sequence is the point.
- **Adding a vertex can only help an adversary in one way and hurt in another**,
  which is the whole difficulty: a `C_4`-free graph on `n+1` vertices restricted
  to `n` vertices may lose minimum degree, and a `C_4`-free graph on `n` vertices
  extended by an isolated-ish vertex has minimum degree `0`. **There is no
  trivial embedding argument in either direction, and finding out why is the
  first thing to establish in this workspace.**
- `f(4) = 2`, easily checked. Every `f(n)` is a finite exactly computable number.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **`f` is a reformulation of a Ramsey number.** With `R(C_4, K_{1,n})` the
  Ramsey number for a `C_4` against a star,
  ```
  R(C_4, K_{1,n}) = min { m : f(m) <= m - n },      f(n) = min { m : m >= R(C_4, K_{1,n-m}) }.
  ```
  **Derive and verify both identities here** — they are the bridge to the
  literature, and Erdős Problem #552 is the study of `R(C_4, S_n)` itself.
- The bounds from #552 imply `f(n) < sqrt(n) + 1` and `f(n) = (1+o(1))sqrt(n)`.
- **`f(4) = 2`**, easily checked.
- **The `C_4`-free extremal structures** are the Erdős–Rényi polarity graphs of
  projective planes, defined for `n = q^2 + q + 1` with `q` a prime power. These
  are `q`-regular-ish and are the reason the answer is `~sqrt(n)`. **They exist
  only at those special `n`, and that irregularity is exactly what could make
  `f` non-monotone.** Construct them here — they are explicit, small, and
  checkable, and they are the most likely source of a counterexample.

## The obstruction, stated honestly

1. **The asymptotics are settled; the question is about local behaviour of an
   integer sequence.** No asymptotic result can answer it. **Any argument that
   proceeds by estimating `f(n)` to within `o(sqrt n)` is answering a different
   question**, and this must be said out loud whenever such an estimate appears.

2. **The extremal objects exist only at sporadic `n`.** Polarity graphs live at
   `n = q^2 + q + 1` for prime powers `q`. Between those values the extremal
   `C_4`-free graphs are obtained by deletion or ad-hoc constructions, and their
   minimum degree does not vary smoothly. **A drop in `f` — if it happens — will
   happen just past such a special value**, so the search for a counterexample
   has an address, and the run should go there first.

3. **There is no monotone embedding.** Neither restriction nor extension
   preserves the relevant quantity, so monotonicity is not formal. **A proof
   would have to show that an extremal `C_4`-free graph on `n+1` vertices can
   always be converted into one on `n` vertices without losing minimum degree.**
   That is a concrete combinatorial statement, and it is either true and
   provable by a deletion/contraction argument, or false with a small witness.

Stated as the thing to beat:

> **Show that every `C_4`-free graph on `n+1` vertices with minimum degree `d`
> yields a `C_4`-free graph on `n` vertices with minimum degree `>= d` — or find
> an `n` where it fails, which is a finite computation with a known address.**

Say which of the two the approach is on.

## The oracle: exact `f(n)`, and the counterexample hunt

1. **`exists(n, d)`** — is there a `C_4`-free graph on `n` vertices with minimum
   degree `>= d`? SAT: one Boolean per pair; a clause forbidding each potential
   `C_4` (for every 4-set, forbid each of its three 4-cycles); a cardinality
   constraint per vertex for the degree. **State the clause count before
   running.** Then `f(n) = 1 + max { d : exists(n, d) }`.

2. **The sequence itself.** Compute `f(n)` exactly for as many `n` as reachable,
   starting at `n = 4` and pushing up. **This is the deliverable.** Report the
   largest `n` reached, the encoding, the symmetry breaking, and the wall clock.
   **The moment the table shows `f(n+1) < f(n)` for any `n`, the problem is
   answered in the negative for that `n`** — and the interesting question
   becomes whether it happens for arbitrarily large `n`.

3. **Targeted search near `n = q^2 + q + 1`.** Construct the Erdős–Rényi polarity
   graphs for `q = 2,3,4,5,7,8,9,11,...`, verify they are `C_4`-free with an
   independent checker, record their minimum degrees, and compute `f` on the
   windows just above and below those `n`. **If `f` ever drops, this is where.**

4. **The falsification oracle.** Every claimed value of `f(n)` requires **both**
   halves: a `C_4`-free witness with minimum degree `f(n)-1` (a graph, verified
   by an independent checker) and the unsatisfiability of `exists(n, f(n))` (a
   SAT proof, or an exhaustive argument). **Say which half was actually done for
   each entry in the table**; a table half of whose entries are only upper bounds
   is fine and useful, and a table that hides which is which is worthless.
   Every claimed general bound is evaluated at `f(4) = 2` and at every entry
   computed.

## Leads — verify each before relying on it

- **Erdős Problem #552**, `R(C_4, S_n)`, and the exact bounds it supplies; the
  translation identities above are the bridge.
- **Erdős–Rényi polarity graphs** of `PG(2,q)`: construction, `C_4`-freeness,
  degree sequence (`q+1` except for the `q+1` absolute points of degree `q`),
  and their number of vertices `q^2+q+1`. **The degree irregularity at absolute
  points is exactly the kind of defect that makes the minimum-degree problem
  behave unlike the edge-count problem — study it closely.**
- **`ex(n; C_4)`**, the Kővári–Sós–Turán bound and Füredi's exact results, and
  precisely how the edge problem and the minimum-degree problem differ.
- **`C_4`-free graphs with prescribed minimum degree** — any literature on
  maximum minimum degree, which is the exact quantity `f(n) - 1`.
- **Known values of `f(n)` or of `R(C_4, K_{1,n})`** in the literature: a
  published table would both calibrate the oracle and say where the frontier is.
  Find it.
