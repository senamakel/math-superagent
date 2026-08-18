# Backward decomposition — Toeplitz Square Peg Problem

Worked backward from the goal. The conjecture is open; this file states what
would suffice to prove it, reduced onto the one quantity the literature's own
engine already isolates. The reduction itself is *not* this run's invention:
Matschke 2009, Theorem 2.8 / Corollary 2.9 (claim `matschke2009-mod2-intersection`)
is the parity reduction, and Corollary 2.10 (claim
`matschke2009-special-trapezoid-criterion`) is the instance of it that proves
the conjecture for locally monotone curves. What is a gap here is the step that
would promote that instance to every continuous Jordan curve.

The goal this run is actually committed to (GOAL.md) is a genuine partial
result, not the full conjecture. Two skeletons are written below:

1. `toeplitz-full` — the full conjecture, reduced to the one open lemma. This
   is the skeleton a proof of the conjecture would have to complete. It is
   `sketched`, not `live`: no attempt in this run is committed to closing it.
2. `toeplitz-locally-monotone-extension` — the partial-result skeleton this run
   is actually after: an extension of the parity argument to a named class
   strictly larger than locally monotone, with the boundary-winding / shrinkout
   step redone. This is the skeleton whose gaps the run's attempts attack.

---

## Skeleton A — the full conjecture

```skeleton
goal: Every Jordan curve γ : S¹ → R² contains four points that are the vertices of a square (Toeplitz, 1911).
implies: By Matschke 2009 Theorem 2.8 (claim matschke2009-mod2-intersection), if γ inscribes no square then for every generator ω of π₁((S¹)²\Δ(S¹)²) ≅ Z the mod-2 intersection number i(S, P₄(ω)) is well-defined and equals 1, where S ⊂ P₄ is the special-trapezoid locus and P₄(ω) is the "membrane" image of S¹ under ω. By Corollary 2.9, if for some generator ω one has P₄(ω) ∩ S = ∅ then i(S, P₄(ω)) = 0, contradicting the value 1; hence γ inscribes a square. Therefore the conjecture follows from: for every Jordan curve γ there exists a generator ω of π₁((S¹)²\Δ(S¹)²) such that the membrane P₄(ω) is disjoint from the special-trapezoid locus S (or, equivalently by Corollary 2.10, such that γ inscribes no special trapezoid of size ε for some ε, taking ω(t)=(t,t+ε)). The locally monotone case is exactly the instance where this is known: compactness gives an ε with no special trapezoid of size ε (claim matschke2009-special-trapezoid-criterion, Cor 2.10 / Cor 2.12).
status: sketched
rests-on: matschke2009-mod2-intersection, matschke2009-special-trapezoid-criterion, matschke2014-stromquist-locally-monotone
```

```gap
id: G-membrane-avoids-special-trapezoids
lemma: For every continuous Jordan curve γ : S¹ → R² there exists a generator ω of π₁((S¹)²\Δ(S¹)²) ≅ Z such that the membrane P₄(ω) ⊂ P⁰₄ is disjoint from the special-trapezoid locus S. Equivalently (Cor 2.10), there exists ε ∈ (0,1) such that γ inscribes no special trapezoid of size ε, or generically an even number.
status: open
discharged-by: —
thread: —
next: Formalise the statement in Lean as: for γ : S¹ ↪ R² continuous injective, ∃ (ω : S¹ → (S¹)²\Δ(S¹)²) representing a generator of π₁, P₄(ω) ∩ S = ∅. Then test the negation on finite polygonal models with sat_solver / smt_solver: encode "every generator ω meets S" as a finite constraint system over a polygon with rational vertices and ask the solver for UNSAT — a SAT result (a polygon where every membrane hits a special trapezoid) would be the first candidate counterexample and the oracle's exact checker would verify whether the hit is a genuine special trapezoid or a degenerate boundary termination (the Remark 2.4.2.2 escape). The honest first move is the Lean statement plus a small exact-arithmetic enumeration of special trapezoids of size ε on a fixed polygon, to see whether the "even count" parity is computable at all without regularity.
```

The one gap is the whole conjecture. It is left open because the run is not
committed to proving the full case (GOAL.md). It is recorded so the next
reducer does not re-derive the reduction: the parity theorem plus "exhibit a
good membrane" *is* the proof, and the only missing piece is the membrane
existence for wild curves.

---

## Skeleton B — the partial result this run is committed to

```skeleton
goal: There is a named class C of Jordan curves, strictly larger than Stromquist's locally monotone class, such that every γ ∈ C inscribes a nondegenerate square, proved by redoing the configuration-space parity step (Matschke Thm 2.8) for C — i.e. exhibiting, for every γ ∈ C, a generator ω with P₄(ω) ∩ S = ∅, and certifying the resulting square is not a shrinkout.
implies: Combine (i) the parity reduction matschke2009-mod2-intersection (no square ⟹ i(S,P₄(ω))=1 for every generator ω), (ii) a class-C analogue of Corollary 2.9 (∃ generator ω with P₄(ω)∩S=∅ ⟹ square), and (iii) a nondegeneracy bound showing the square found has side length bounded away from 0 on C (the device that defeats shrinkout, problem.md failure point 3 / Tao 2017 claim tao2017-shrinkout-difficulty). The locally monotone case supplies (ii) via compactness (matschke2009-special-trapezoid-criterion); the extension is to redo (ii) and add (iii) for C. A curve in C but not locally monotone, with a verified square, is the run's own result (GOAL.md completion criterion 3).
status: live
rests-on: matschke2009-mod2-intersection, matschke2009-special-trapezoid-criterion, matschke2014-stromquist-locally-monotone, tao2017-shrinkout-difficulty
```

```gap
id: G-named-class-membrane
lemma: Define a named class C ⊋ {locally monotone curves} (candidate: curves locally monotone except at a finite controlled set of points; or curves that are a union of two Lipschitz-graph arcs with Lipschitz constant < 1 — Tao's class, claim tao2017-two-lipschitz-graphs, already proved but by a different method; or Hölder curves with exponent α and a boundary winding number definable from the Hölder data) and prove: for every γ ∈ C there exists a generator ω of π₁((S¹)²\Δ(S¹)²) with P₄(ω) ∩ S = ∅.
status: open
discharged-by: —
thread: —
next: Pick the concrete candidate C = {locally monotone except at a finite set F ⊂ S¹, |F| finite} and write the Lean statement of the membrane-avoidance for it. The first concrete move is: for a polygon (locally monotone, F = ∅) the exact oracle enumerates special trapezoids of size ε and confirms Cor 2.10 computationally; then add one controlled corner (|F|=1) and check whether the membrane ω(t)=(t,t+ε) still avoids S for small ε, using exact arithmetic on the algebraic vertices. This is a tool_builder / coder job today: extend the exact special-trapezoid enumerator to a polygon with one non-locally-monotone vertex and report whether S(ε) is empty for some ε.
```

```gap
id: G-nondegeneracy-bound-on-C
lemma: For the class C of G-named-class-membrane, every square produced by the parity argument has side length bounded below by a positive constant depending only on γ (not on the approximating sequence), so that shrinkout (problem.md failure point 3) cannot occur.
status: open
discharged-by: —
thread: —
next: State in Lean the side-length lower bound for the candidate C, and verify it computationally on the same one-corner polygon used for G-named-class-membrane: the exact checker reports the side length of the found square, and the claim is it is ≥ c(γ) > 0. The annulus theorem (matschke2009-annulus-quantitative, side ≥ √2) is the published prototype for such a bound; the move is to compute whether the one-corner polygon's square side length is bounded away from 0 as the corner sharpens, to find where (if anywhere) the bound collapses — that collapse point is the obstruction that bounds C.
```

```gap
id: G-curve-outside-published-classes
lemma: Exhibit at least one Jordan curve γ₀ ∈ C (the class of G-named-class-membrane) that is not locally monotone, not in Matschke's open-dense class, and not a two-Lipschitz-graphs curve, together with an exact-arithmetic verification that γ₀ inscribes a nondegenerate square — an instance exercising the configuration-space map outside prior published verification.
status: open
discharged-by: —
thread: —
next: Construct γ₀ as a polygon with rational/algebraic vertices having one vertex where local monotonicity fails (the projection ℓ∘γ is not monotone in any neighborhood), run the exact oracle to find its inscribed square, and certify the square's vertices are exact points of γ₀ with positive side length. This is a coder job today once the oracle (GOAL.md phase 4, not yet built) exists; the first move is to specify the oracle's exact-arithmetic contract for "inscribed square on a polygon with algebraic vertices" so the construction can be checked.
```

---

## What is already discharged (not a gap)

- **The parity reduction itself** — "no square ⟹ i(S, P₄(ω)) = 1 for every generator ω" — is claim `matschke2009-mod2-intersection` (Matschke 2009 Thm 2.8). It is asserted-by-source, not proved here; a Lean `Cited` axiom is the planned formalisation. It is *not* a gap: it is the inference both skeletons rest on.
- **The locally monotone instance** — "locally monotone ⟹ ∃ ε with no special trapezoid of size ε ⟹ square" — is claim `matschke2009-special-trapezoid-criterion` (Cor 2.10) together with `matschke2014-stromquist-locally-monotone`. Discharged as the base case of the extension.
- **The shrinkout obstruction** as a *named difficulty* — claim `tao2017-shrinkout-difficulty` — is discharged as the reason G-nondegeneracy-bound-on-C is required. It is not a proof of the bound; it is the statement that the bound is the hard part.
- **The CDM full-conjecture claim is false** — claim `cdm2022-no-full-conjecture-proof`: no CDM paper proves the conjecture for all continuous curves. This closes the "is it already solved?" question and is why the conjecture is treated as open.

## What would falsify the reduction

- A Jordan curve γ for which the mod-2 intersection number i(S, P₄(ω)) is **not well-defined** for some generator ω. Theorem 2.8 requires well-definedness under the hypothesis "γ inscribes no square"; if a wild curve makes the intersection number ill-defined even under that hypothesis, the reduction's premise fails and Skeleton A does not apply. This is problem.md failure point 1 (no boundary winding number) and is the most likely way the full-conjecture reduction breaks. It is *not* a gap to close; it is the obstruction that bounds how far Skeleton B's class C can reach.
- A curve where every membrane P₄(ω) meets S only in degenerate boundary-terminating configurations (Remark 2.4.2.2): the parity counts 1 but no genuine square is forced. This is failure point 2 (spurious interior zeros) and is exactly what G-nondegeneracy-bound-on-C is designed to rule out for C.

## Which gap to attack first

**G-named-class-membrane**, with the concrete first move of extending the exact
special-trapezoid enumerator to a polygon with one non-locally-monotone vertex.
It is the load-bearing gap: Skeleton B's other two gaps (nondegeneracy bound,
exhibit a curve) both depend on a named class C being fixed, and fixing C is
what this gap does. It is attackable today by a tool_builder (exact enumeration
of special trapezoids of size ε on an algebraic-vertex polygon with one bad
corner), and its output — does S(ε) stay empty, and does the found square stay
nondegenerate, as the corner sharpens? — directly measures both G-named-class-membrane
and G-nondegeneracy-bound-on-C. The collapse point, if any, is the obstruction
that bounds C and is the run's partial result.
