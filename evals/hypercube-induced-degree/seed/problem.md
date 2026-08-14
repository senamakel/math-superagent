# Maximum degree of large induced subgraphs of the cube

## Statement

Let `Q_n` be the graph on the `2^n` vertices `{0,1}^n`, with two vertices
adjacent exactly when they differ in a single coordinate. `Q_n` is `n`-regular.

For a subset `S` of the vertices, write `Q_n[S]` for the induced subgraph and
`D(S)` for its maximum degree — the largest number of neighbours any vertex of
`S` has *inside* `S`.

A set of size `2^{n-1}` can have `D(S) = 0`: take all vertices of even weight.
That set is independent, and it is exactly half of `Q_n`. So define

```
f(n)  =  min { D(S)  :  S subset of {0,1}^n,  |S| = 2^{n-1} + 1 }
```

— one vertex more than half.

> **Question.** Determine the growth rate of `f(n)`.

Adding a single vertex to a maximum independent set forces some degree to
appear. The question is how much. What is known is

```
c * log n   <=   f(n)   <=   sqrt(n)      (for a constant c > 0, n large)
```

and **the gap between a logarithm and a square root has not moved in thirty
years.** Closing it in either direction is the objective.

## What the statement does and does not say

- `|S| = 2^{n-1} + 1` **exactly**. One vertex past half. Larger `S` makes the
  problem easier and is a different question; the whole difficulty is that the
  hypothesis is as weak as it can be while still forcing anything at all.
- `D(S)` is the maximum degree **within** `S`. Edges from `S` to its complement
  do not count. This is what makes the problem hard: the obvious counting
  arguments bound the number of *internal edges*, and a bound on edges gives an
  average degree, not a maximum. `f(n)` is a max-min quantity and averaging
  arguments do not reach it.
- The bound is asked for **every** such `S`, so an adversary picks `S` after
  seeing the argument. Constructions give upper bounds on `f(n)`; only proofs
  give lower bounds.
- Nothing here is asymptotic-only. `f(n)` is a specific finite number for each
  `n` and can be computed exactly for small `n`. Do that first.

## Both known bounds, to be reproduced before anything else

**Upper bound `f(n) <= sqrt(n)`.** There is a construction: for `n` a perfect
square, a set `S` of size `2^{n-1} + 1` in which no vertex has more than
`sqrt(n)` neighbours inside `S`. The construction is by a recursive/product
argument on blocks of coordinates. **Rebuild it here and verify it by direct
computation** for the smallest cases where it applies. If the reconstructed
family does not actually achieve `sqrt(n)`, that is itself worth knowing and
must be recorded.

**Lower bound `f(n) = Omega(log n)`.** Established in the late 1980s by a
counting/induction argument. Reconstruct it, state the constant it actually
gives, and verify the resulting inequality against exact small-`n` values.

Neither bound may be cited. Both are inputs to be re-derived in this workspace,
because the run's own machinery has to be calibrated against them before any new
claim made with that machinery means anything.

## The obstruction, stated honestly

The gap is `log n` versus `sqrt(n)`, and there are two asymmetries that say
where the truth probably lies and why it is hard to reach.

**The upper bound is a construction and is probably tight.** Constructions are
checkable; this one has been examined for decades and nothing better has
appeared. The working expectation should be that `f(n)` is around `sqrt(n)` and
that the *lower* bound is what is wrong.

**Every natural lower-bound technique is stuck at `log n`, and for a reason that
can be stated.** The available combinatorial methods —

- counting internal edges and applying an averaging argument,
- isoperimetry on the cube (the edge- and vertex-isoperimetric inequalities),
- induction on coordinates, splitting `Q_n` into two copies of `Q_{n-1}`,
- influence/Fourier arguments on Boolean functions,

— all produce bounds on **average** or **total** quantities. To get a maximum
degree of `sqrt(n)` out of an average-degree bound you would need the internal
edge count to be about `2^{n-1} * sqrt(n)`, and it is not: `S` can genuinely
have very few internal edges in total. The single extra vertex is not enough
mass to force many edges. **So the bound cannot come from counting edges.** It
must come from something that produces a *maximum* directly.

Stated as the thing to beat:

> **A method that bounds an average will not reach `sqrt(n)`. The lower bound
> has to come from a quantity that is itself a maximum, or from an object whose
> extremal value is a maximum by construction.**

Finding such a quantity is the open problem. It is *not* known what it should
be, and thirty years of combinatorial effort suggests it is not a refinement of
the four techniques above. An approach that is a sharpening of an averaging
argument is very likely attacking the wrong object; an approach that produces a
maximum directly is the one with a chance.

Say which side the approach is on, and if it claims to produce a maximum
directly, say what quantity it is a maximum *of* and why that quantity is
entitled to say anything about an arbitrary `S`.

Note also the shape of the target. `sqrt(n)` is not a natural output of counting
— counting produces linear and logarithmic quantities. A square root usually
arises from a quadratic relation somewhere, and an approach should be able to
point at where its `sqrt` is going to come from before it starts.

## The oracle: exact small cases, and a falsifier

There is no value to recompute at the end — the deliverable is a proof — but
`f(n)` is a finite computable number and **the run must know its exact values
before conjecturing anything.**

1. **`f(n)` exactly, for as many `n` as feasible.** For each `n`, minimise the
   maximum internal degree over all `S` of size `2^{n-1} + 1`. This is a finite
   optimisation: exhaustive for `n <= 4`, and reachable by ILP or SAT (ask "is
   there an `S` of this size with `D(S) <= d`?") somewhat further. Push it as
   far as the compute policy allows and **state exactly how far it got and by
   what method.**

2. **The falsification oracle, which is the one that matters.** Any claimed
   lower bound `f(n) >= g(n)` must be checked against the exact values from (1).
   A claimed bound that exceeds a computed `f(n)` is **false** — record it
   refuted, not weakened. This catches the dominant failure mode, which is an
   argument that quietly bounds the wrong quantity.

3. **The construction checker.** Given an explicit `S`, verify `|S|` and compute
   `D(S)` directly. Any claimed upper-bound construction must pass this for the
   smallest cases before its asymptotics are believed.

Expect the exact values to be small and to look uninformative — `f(n)` for
`n <= 5` cannot distinguish `log n` from `sqrt(n)`. That is not a reason to skip
them. They are the only thing standing between the run and a plausible false
theorem.

## Leads — verify each before relying on it

Not established facts here. Each needs a primary source and its own claim block
with an explicit status.

- **The `sqrt(n)` construction.** Late-1980s combinatorics; a recursive product
  construction. Get the exact statement, the constant, and the values of `n` for
  which it is stated.
- **The `Omega(log n)` lower bound** and the argument that produces it. What
  exactly does the induction bound, and where does it lose?
- **Isoperimetric inequalities on the hypercube** — edge- and vertex-forms.
  Establish precisely what they give for a set of size `2^{n-1} + 1` and confirm
  that it is an average-type bound, so the obstruction above is verified rather
  than assumed.
- **Structure of `Q_n` beyond counting** — its symmetry group, its spectrum, its
  recursive product structure, its behaviour under coordinate restriction. The
  obstruction above says the bound must come from something that is a maximum by
  construction; the run's first job on this side is to make a list of candidate
  such quantities for the cube and say what each one is known to give.
- **Connections to Boolean function complexity.** This quantity is known to be
  related to measures of how much a Boolean function depends on its inputs. A
  bound here is reported to transfer. Establish what the transfer actually is,
  because it tells you how much a partial result is worth — but do not let it
  redirect the work: the combinatorial statement above is the target.
