# Hilbert's 3rd problem — scissors congruence beyond dimension four

## The original question, and its answer

> Given two polyhedra of equal volume in `R³`, can one always be cut into
> finitely many polyhedral pieces and reassembled into the other?

**Dehn (1900) answered no**, by the invariant that carries his name: to a
polyhedron `P` with edges of length `ℓ_i` and dihedral angles `θ_i`, assign

```
D(P) = Σ ℓ_i ⊗ θ_i  ∈  R ⊗_Z (R/πQ).
```

`D` is unchanged by cutting and reassembling, is `0` for a cube, and is nonzero
for a regular tetrahedron — so the two are not scissors congruent at equal
volume. The original question is closed and is **not** this workspace's target.

## The target

The natural completion of Dehn's answer is: are volume and the Dehn invariant
*together* a **complete** invariant of scissors congruence? Recalled status,
to be confirmed or struck against sources:

- **`R³`: yes** — Sydler (1965). Two polyhedra in Euclidean 3-space are
  scissors congruent iff they have the same volume and the same Dehn invariant.
- **`R⁴`: yes** — Jessen, reducing to Sydler.
- **`R^n`, `n ≥ 5`: open.** Whether volume and Dehn invariant are complete is
  not known in any dimension from five upward.
- **Hyperbolic and spherical 3-space: open.** The analogous statement — often
  stated as the *Dehn invariant sufficiency conjecture* — is open in `H³` and
  `S³`, and is the form of the question that gets the most attention.
- The modern framework is the **scissors congruence group** `P(X)` and its
  homological description (Dupont, Sah, Goncharov); the conjecture connects to
  the Bloch group, the dilogarithm, rigidity of `SL_2(C)`, and algebraic
  `K`-theory. Recent work reframes scissors congruence as a `K`-theory spectrum
  (Zakharevich and collaborators).

> **(H3.n)** For `n ≥ 5`, are two Euclidean polytopes of equal volume and equal
> Dehn invariant scissors congruent?
>
> **(H3.hyp)** In `H³` (and `S³`), is the Dehn invariant, together with volume,
> a complete invariant of scissors congruence?

Either is a target. Both are questions about explicit polytopes with rational or
algebraic data, which is what makes them reachable here.

## Where a machine has traction

- **Explicit dissections.** A scissors congruence between two named polytopes is
  a *finite certificate*: a list of pieces and isometries. Producing one settles
  a case affirmatively and is checkable exactly.
- **Dehn invariants are computable.** `Σ ℓ_i ⊗ θ_i` in `R ⊗ R/πQ` reduces, for
  polytopes with algebraic data, to a question about `Q`-linear relations among
  logarithms of algebraic numbers and rational multiples of `π` — decidable in
  practice for specific cases and where a lower bound has real content.
- **The dilogarithm side is numeric with exact structure.** Five-term relations
  and Bloch-group identities are checkable to high precision as a filter, and
  provable exactly in the cases that matter.

## The cheap tests every candidate must pass first

1. **The Dehn test.** Any claimed dissection between two polytopes must have
   both invariants checked first — equal volume *and* equal Dehn invariant. A
   dissection claimed between polytopes with different Dehn invariants is an
   error in the dissection, found in seconds. Run this before any search.
2. **The dimension test.** Sydler and Jessen settle `n ≤ 4`. Any proof strategy
   for `n ≥ 5` must say what it uses that fails at four, or explain why it
   should have settled the open case already. An argument uniform in dimension
   that concludes completeness is refuted by the fact the question is open.
3. **The curvature test.** Euclidean, hyperbolic and spherical scissors
   congruence are *different* subjects: in `H³` and `S³` volume is not a
   separate invariant in the same way (it is itself of Dehn-invariant type, and
   the scaling argument that drives the Euclidean proofs is unavailable).
   Any argument transported from `R³` must name where the Euclidean scaling
   entered. This is the single most common way a claim here is wrong.

## What is genuinely unknown

- H3.n for every `n ≥ 5`.
- H3.hyp in `H³` and `S³`.
- Whether there is *any* invariant beyond volume and Dehn in dimension 5 —
  no candidate additional invariant is known, which is why the conjecture is
  believed and why nobody can prove it.
- Explicit scissors congruences between named hyperbolic polytopes of equal
  volume and Dehn invariant — even single cases would be evidence.
- The structure of the scissors congruence group `P(H³)` as a `Q`-vector space,
  and whether specific classes are nonzero.

## What counts as a result

In descending order of value.

1. A resolution of H3.hyp or H3.n in either direction. A negative answer is a
   *new invariant* plus two polytopes it separates — the most valuable outcome
   available here, and the one nobody expects.
2. An explicit, verified scissors congruence between two named polytopes with
   equal volume and Dehn invariant where none is recorded — especially in `H³`,
   where each case is evidence for the conjecture and none is easy.
3. A complete, machine-checked verification of a published dissection (Sydler's
   or Dupont–Sah's constructions), reproduced exactly with the pieces and
   isometries listed.
4. A proof of completeness for a stated *subclass* of polytopes in dimension 5
   (orthoschemes, products, a family closed under a named operation), with the
   obstruction to removing the restriction named.
5. An exact determination of the Dehn invariant of a named family, with the
   `Q`-linear independence of the angles involved proved rather than checked
   numerically.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim a new invariant on a numerical computation.** A separating
invariant must be proved invariant under cutting and reassembly; a number that
differs between two polytopes is a lead until it does.
