# Frankl's union-closed sets conjecture

Let `F` be a finite family of finite sets, closed under union:

```
A, B ∈ F  ⟹  A ∪ B ∈ F,      F ≠ {∅},   |F| < ∞.
```

> **(UC)** There exists an element `x` belonging to at least `|F|/2` of the
> members of `F`.

Call an element with that property *abundant*. The conjecture asserts every
union-closed family (other than the trivial `{∅}`) has one.

Attributed to Péter Frankl, around 1979. Open.

## Equivalent statements, and they are genuinely equivalent

Each of these is standard; each should be **re-established from a source**
before it is used as a rewriting rule, because the direction of each equivalence
and its exact hypotheses are where errors enter.

1. **Intersection-closed dual.** Complementing every set inside the ground set
   turns union-closed into intersection-closed and "in at least half" into "in
   at most half". A statement proved on one side transfers; a *method* often
   does not, and which side a technique is natural on is worth recording.
2. **Lattice form (Poonen).** A finite union-closed family ordered by inclusion
   is a finite lattice, and every finite lattice arises this way. UC becomes: in
   every finite lattice `L` with `|L| ≥ 2` there is a join-irreducible `j` with
   at most half the elements of `L` above it. So UC is a statement about *all
   finite lattices*, which is why partial results are usually stated for lattice
   classes (lower semimodular, geometric, modular, …).
3. **Graph form (Bruhn–Charbit–Schaudt–Telle).** Every graph induces a
   union-closed family from its maximal independent sets / its "stable set"
   family; UC restricted to that family is a statement about a vertex lying in
   at least half of the maximal independent sets, and the general conjecture is
   equivalent to the bipartite case of the graph formulation. Confirm which
   direction is the theorem and which the trivial inclusion.
4. **Weight / averaging form.** UC holds for `F` iff a suitable non-negative
   weighting of the ground set has average abundance `≥ 1/2`; "FC-families"
   (families `A` whose presence inside any union-closed `F` forces UC for `F`)
   are the systematic version of this, and are the engine behind most
   pre-2022 progress.

## The state of the art — leads, not imports

**Everything below is recalled from memory and must be re-established from
primary sources before anything is built on it. Print the source, year and the
exact statement beside each one you confirm; strike any you cannot.**

### The entropy line (this is where the live frontier is)

- **Gilmer (Nov 2022, arXiv:2211.09055).** The breakthrough: there is an
  absolute constant `c > 0` — Gilmer's own value around `0.01` — such that every
  union-closed family has an element in at least `c·|F|` of its sets. Method:
  take `A, B` independent uniform members of `F`; `A ∪ B ∈ F`, so
  `H(A ∪ B) ≤ log|F| = H(A) = H(B)`; if every element had density `< c`, an
  entropy inequality would force `H(A ∪ B) > H(A)`, a contradiction. The whole
  content is a one-variable inequality relating `h(p)` to `h(2p − p²)`.
- **The `(3 − √5)/2` barrier.** Independently and within days, several groups
  (Alweiss–Huang–Sellke; Chase–Lovett; Pebody; and Sawin) pushed the constant to
  `(3 − √5)/2 = 0.381966…` and showed that this is exactly where Gilmer's
  argument as stated stops: the entropy inequality being used is *tight* at that
  value. **Verify the attribution and who proved which half — the "improvement"
  and the "barrier" are different theorems.**
- **Sawin.** Showed the barrier is not the truth: a refinement (using that `A`
  and `B` need not be independent / an approximate-union step) gives a constant
  **strictly greater** than `(3 − √5)/2`, though without an explicit clean value
  at first. Later work (Cambie; Yu; others) made an explicit improvement —
  something near `0.3823` — **the exact current record and its source is the
  first thing this run must pin down.**
- **What the entropy method has *not* done:** reached `1/2`. `1/2` is the
  conjecture and every entropy proof so far is bounded away from it by the
  structure of the inequality, not by slack in the estimates.

### The combinatorial line (pre-2022, and still the only route to exact results)

- **Small ground sets.** UC is verified for all families on a ground set of at
  most 11 or 12 elements (Bošnjak–Marković for `n = 11`; Vučković–Živković
  extended it) and for `|F| ≤ 50` (Roberts–Simpson, Faro, and others). **Get the
  exact current verified range for both parameters, with the source.**
- **Small sets force it.** If `F` contains a singleton `{x}`, then `x` is
  abundant, immediately. If `F` contains a 2-element set `{x, y}` then one of
  `x, y` is abundant (Sarvate–Renaud / folklore). The 3-element case is
  *not* generally true and the exact status of "contains a 3-set" is a real
  fault line — record it precisely.
- **FC-families.** A family `A` is an FC-family if every union-closed `F ⊇ A`
  satisfies UC. Deciding FC-ness for a given small `A` is a finite LP / weight
  computation. This machinery settles many cases and is *computationally
  attackable*, which matters for this run.
- **Large families.** UC holds when `|F| ≥ 2^{n−1}` — and more precisely for
  families that are large relative to `2^n` — by counting.
- **Lattice classes.** UC is known for lower semimodular lattices, for modular
  and geometric lattices, and for several other classes; Reinhold, Abe–Nakano,
  Czédli–Schmidt and others. This is where the lattice reformulation earns its
  keep.
- **Knill; Wójcik.** Bounds of the form "some element is in at least
  `(|F| − 1)/log₂|F|` sets", predating and asymptotically weaker than Gilmer's
  linear bound but *unconditional in a different regime* — worth checking
  whether anything in the small-`|F|` regime is still best from these.
- **Bruhn–Schaudt, "The journey of the union-closed sets conjecture" (2015).**
  The survey. It is the map of everything before the entropy era, and it is the
  right first read for the combinatorial line.

## What is genuinely unknown

- UC itself, for any constant `c ≥ (3−√5)/2 + ε` beyond what is published.
- Whether the entropy method can reach `1/2` at all, or whether there is a
  *proved* barrier — an explicit family of distributions showing that any
  argument of this shape (approximate-union entropy inequality on two
  independent copies) cannot pass some `c₀ < 1/2`. **A theorem that the method
  is capped is as valuable here as an improvement, and is a more realistic
  target.**
- UC for families containing a 3-element set, in full.
- UC for graphs / lattices in classes not yet covered — in particular whether
  the bipartite graph formulation is more tractable than the general one.
- Any structural theorem about a minimal counterexample: bounds on `n`, on
  `|F|`, on the sizes of its sets, on the abundance profile (the sorted vector
  of element densities). Empirically the *minimum* over `x` of density is what
  is bounded; nothing forces the *shape* of the density vector.

## Hard constraints every proof must satisfy

Three negative controls. Any argument in this workspace must be run against all
three, and the step that fails must be named.

1. **Tightness families.** There are union-closed families where the best
   element sits at density exactly `1/2` — e.g. the power set `2^[n]` (every
   element has density exactly `1/2`), and small hand-built examples. **Any
   argument proving `> 1/2` is wrong.** This is the cheapest possible test and
   it must be applied to every candidate.
2. **The union-closure hypothesis must be used.** Drop it and UC is false
   (an antichain of large sets on a big ground set has every element rare). An
   argument that never uses `A ∪ B ∈ F` proves a false statement.
3. **Finiteness must be used.** Record where. Infinite / measure-theoretic
   analogues of UC behave differently and an argument that survives verbatim in
   an infinite setting is suspect.

An argument that survives all three is not thereby correct — but one that fails
any is refuted, cheaply, before effort is spent.

## What counts as a result

In descending order of value.

1. UC itself. Do not expect this; see the closing rule.
2. An explicit constant strictly better than the published record, with a
   verified proof and a script that checks the underlying inequality.
3. A **proved barrier**: a theorem that entropy arguments of a stated shape
   cannot exceed some `c₀ < 1/2`, with the extremal object exhibited. This
   converts folklore ("the method seems to stop here") into mathematics and is
   the most realistic large result available.
4. UC for a natural class not previously covered (a lattice class, a graph
   class, families containing a specified small set), proved.
5. A structural theorem about a minimal counterexample, proved rather than
   measured.
6. An exact computational extension: a new verified range of `n` or `|F|`, or a
   new FC-family certified, provided it is reproducible from `code/` and its
   correctness argument is written down.
7. A refutation of a published or folklore claim, with an explicit witness.

**Do not claim UC.** A proof of the full conjecture produced in a run of this
length is, on prior, an error. If you believe you have one, the deliverable is
the argument written out with every step labelled by status and all three
negative controls applied explicitly — not an announcement.
