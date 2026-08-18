# Lean formalisation — Toeplitz statement and Stromquist theorem

Kernel-checked statements written in Lean 4 against this workspace's Mathlib.
Verdicts read off `lean_check` (recorded in `code/out/lean/*.json`).

## The conjecture statement

```claim
id: lean-toeplitz-statement
statement: Toeplitz's inscribed-square conjecture, stated as a type: for every continuous
  injective map γ : S¹ → ℝ² (S¹ = AddCircle 1, the additive circle ℝ/ℤ, and ℝ² = EuclideanSpace
  ℝ (Fin 2)) there exist four parameter values t₁ t₂ t₃ t₄ : S¹, occurring in cyclic order
  around the circle (lifts a < b < c < d < a+1), pairwise distinct, whose images are the
  vertices of a nondegenerate square in the prescribed order — diagonals share a midpoint
  (γt₁ + γt₃ = γt₂ + γt₄), are perpendicular (inner product of the two diagonals is 0),
  and have equal length (norms equal).
hypotheses:
  - γ : Circle → Plane is continuous.
  - γ is injective (a Jordan curve parametrisation).
  - Nondegeneracy: the four points are pairwise distinct, and the cyclic-order hypothesis
    separates a genuine square from a crossed quadrilateral.
status: asserted
formalisation: code/lean/Lib/Statement.lean
evidence: `lean_check` on code/lean/Lib/Statement.lean: compiled, outcome `failed` only
  because the theorem ends in `:= by sorry` (the conjecture is unproved; sorryAx is the
  only extra axiom).  The statement elaborates: every name resolves, the types carry every
  hypothesis.  Not `formalised` — the conjecture is open and the kernel has no proof.
holds-here: yes — this is the exact problem under attack
bearing: The conjecture itself pinned down as a Lean type — the deliverable of the run's
  Lean arm is to upgrade this from `asserted` to `formalised` by proving it, or to
  `conditional` by reducing it to a cited theorem.
falsifies: a Lean file whose statement, after substitution, fails to elaborate; or a
  mismatch found between this type and the informal statement (the injectivity hypothesis
  and the diagonal-formulation of squareness are the two places a discrepancy could hide).
```

The statement is deliberately weaker than the informal conjecture in two recorded ways
(marked in the file's own docstring): the curve is given by an injective parametrisation
(rather than as a set, which is the standard equivalent formulation), and "square" is
captured by the diagonal conditions in the prescribed cyclic order rather than by an
intrinsic definition of a square as a set — the equivalence is part of the work.

## Stromquist's theorem, as a cited axiom

The Lean file states Stromquist's theorem as an axiom under `namespace Cited`.  The
`lean_check` verdict on the file is `conditional` — the kernel accepted the axiom as
attributed.  The claim itself, however, is `asserted-by-source`: there is no proved
implication in the file yet, so nothing downstream can be `conditional` on it.  The
`conditional` status is earned by the first theorem proved *from* this axiom.

```claim
id: lean-stromquist-locally-monotone
statement: Every locally monotone Jordan curve inscribes a square: for every continuous
  injective γ : S¹ → ℝ² that is locally monotone (every point of S¹ has a neighbourhood
  whose lift to ℝ is mapped strictly monotonically along some nonzero linear functional
  ℓ : ℝ² →ₗ ℝ), there exist cyclically ordered, pairwise distinct t₁ t₂ t₃ t₄ : S¹ whose
  images form a nondegenerate square in the diagonal sense above.
hypotheses:
  - γ : Circle → Plane is continuous.
  - γ is injective.
  - γ is locally monotone, in the sense of Matschke 2014 survey Theorem 2 (which attests
    Stromquist 1989): every point has a neighbourhood on which some linear functional is
    strictly monotone.
status: asserted-by-source
formalisation: code/lean/Lib/Stromquist.lean
evidence: `lean_check` on code/lean/Lib/Stromquist.lean: compiled, outcome `conditional`,
  cited axiom `Cited.stromquist_square_peg`.  The kernel accepted the axiom as a Cited
  declaration; the paper itself is the unproved hypothesis.  The claim is recorded as
  asserted-by-source until a theorem is proved from the axiom, at which point that
  theorem earns `conditional`.
holds-here: yes — this is the load-bearing theorem GOAL.md names as the base to formalize
  and extend
bearing: The base theorem the run builds from.  The next step is to state and prove the
  supporting lemmas of the configuration-space argument (the Möbius-band identification,
  the map F, the boundary degenerate locus) with this as the goal; each lemma proved from
  the cited axiom is `conditional`.
falsifies: a locally monotone Jordan curve without an inscribed square; or a discrepancy
  between the formal definition of local monotonicity and the survey's definition.
```

The cited axiom's own source, so the attribution is recorded:

```claim
id: cited-stromquist-1989
statement: Stromquist's theorem (1989, Mathematika 36(2), 187–197): every locally monotone
  Jordan curve inscribes a square.  The class of locally monotone curves contains convex
  curves, polygons, and piecewise-C¹ curves (with restrictions).
status: asserted-by-source
evidence: Stromquist 1989 (primary, paywalled; abstract confirms the theorem and the
  weaker condition); attested at second hand by Matschke 2014 Notices AMS 61(4), 346–352,
  Theorem 2, full text in research/sources/matschke2014-survey-square-peg.full.md.
holds-here: yes — this is the content the Lean file `Cited.stromquist_square_peg` stands on.
bearing: The source row for the cited axiom.  The run's earlier claim
  matschke2014-stromquist-locally-monotone is the same content; this row exists so the
  cited axiom has its own claim carrying the source, as the claims ledger requires.
falsifies: a locally monotone Jordan curve without an inscribed square, or a discrepancy
  with the primary source's exact hypothesis.
```

## Environment gotchas (learned this pass, worth not re-learning)

1. **Cross-file imports do not resolve.** `import Lib.Statement` fails with
   "unknown module prefix 'Lib'" — no `Lib.olean` is on the search path. Every
   `.lean` file must be self-contained: `Stromquist.lean` re-declares
   `Circle`, `Plane`, `CyclicallyOrdered`, `IsInscribedSquare` rather than
   importing them from `Statement.lean`.
2. **The circle module is `Mathlib.Analysis.Complex.Circle`** (defines the
   `Circle` type as the unit sphere in ℂ). `Mathlib.Topology.Instances.Circle`
   does not exist.
3. **No `Inner` instance on `ℝ × ℝ`** in this Mathlib. `EuclideanSpace ℝ (Fin 2)`
   works for the plane and carries the inner product and norm.
4. **`AddCircle` has no `LinearOrder`**, so `StrictMonoOn` cannot be stated on
   the circle directly. Monotonicity is stated on real lifts: the locally
   monotone definition quantifies over `t : ℝ` and the open set `I ∋ t` in ℝ.
5. **A docstring directly before `namespace` is a parse error** ("unexpected
   token 'namespace'; expected 'lemma'").
6. **`#print axioms` must use the fully-qualified name** (`Cited.stromquist_square_peg`,
   placed outside the namespace) — with the short name, `lean_check` cannot
   attribute the axiom and reports "nothing attributed".
7. The verdict taxonomy in practice: a file whose only content is a `Cited`
   axiom gets `conditional` at the kernel level, but the claims ledger records
   it as `asserted-by-source` (the paper is the unproved hypothesis; there is
   no implication the kernel checked *from* the axiom). A theorem proved from
   the axiom is what earns `conditional` in the ledger.

