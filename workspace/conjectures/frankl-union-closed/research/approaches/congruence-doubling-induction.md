# Congruence quotients and Day doubling: induction on lattices through de-doubling

```approach
idea: Induct on finite lattices through quotients by maximal congruences, using
  Day's doubling. A maximal congruence θ (an atom of the congruence lattice
  Con(L)) is, by Day's theorem, a single interval-doubling: L = (L/θ)[C] for a
  convex (doubling-closed) set C, with |L| = |L/θ| + |C|. Funayama–Nakayama /
  Grätzer–Schmidt give that Con(L) of a finite lattice is distributive, so these
  atoms exist and the quotient strictly shrinks.
mechanism: By minimality L/θ satisfies UC: some join-irreducible j′ has
  |↑j′| ≤ |L/θ|/2. Lifting through the doubling is exact bookkeeping: a
  join-irreducible x ∉ C stays one element with |↑x|_L = |↑x|_{L/θ} + |↑x ∩ C|;
  a join-irreducible x ∈ C splits into two, x₀, x₁. The abundant element
  survives the de-doubling iff some abundant j′ (or a split copy of an element of
  C) has its filter meet C in at most |C|/2 elements. So UC is equivalent to:
  every doubling-closed convex set C of every finite lattice has a
  join-irreducible whose filter meets C in ≤ |C|/2 elements and whose image is
  abundant in the quotient. This reduces the conjecture to a statement about ONE
  interval and its filters — a concrete, checkable object the entropy line never
  sees.
status: refuted
killed-by: day-doubling-hypothesis-fails-general / bounded-iff-interval-doublings — Day's interval-doubling construction produces EXACTLY the bounded lattices (Freese–Ježek–Nation: finite bounded lattices are exactly those from the one-element lattice by finitely many interval doublings), and convex-set doublings produce the CONGRUENCE NORMAL lattices, with "L bounded ⟺ L congruence normal AND semidistributive" (Geyer). Bounded and congruence-normal lattices are PROPER subclasses of all finite lattices. Hence a minimal counterexample to Frankl's conjecture is NOT forced to be a single interval-doubling of a maximal-congruence quotient, and the de-doubling induction cannot be applied to it in general. The lift bookkeeping (the inventor's speculative step) has no published treatment even within the bounded class.
precedent: bounded-iff-interval-doublings (Geyer, Order 1993, https://link.springer.com/article/10.1007/BF01108710; Day, Can. J. Math 1992, https://doi.org/10.4153/cjm-1992-017-7; Freese–Ježek–Nation); Nation, Congruences of finite semidistributive lattices (2024). Funayama–Nakayama (Con(L) distributive, so maximal congruences/atoms exist) is established but does NOT rescue the induction — the obstruction is that the quotient is not generally a single doubling.
first-step: (refuted as a route to the general conjecture. At best it survives as a bounded-lattice special case: prove UC for finite BOUNDED lattices by induction on interval doublings — a genuine but proper subclass, not the conjecture. Do not re-attempt the general single-doubling claim.)
```

**Refuted on evidence.** The Day hypothesis the inventor flagged as needing
confirmation is decisively false for general lattices: interval doublings give
exactly the bounded lattices and convex-set doublings the congruence-normal
ones, both proper subclasses. A minimal counterexample is not a single doubling
of a quotient, so the induction cannot start. The proposal survives only
narrowed to the bounded-lattice special case (a proper subclass, already a
partial result if proven but not the conjecture), and even there the lift is
unproven.
