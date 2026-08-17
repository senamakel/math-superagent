import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card

/-!
# Spence's minimal-counterexample structural statement — statement only

Source claim (this file asserts the *structure*, it does not prove it):

> **Theorem 6.3 (Odd-cardinality reduction).** A minimum-cardinality
> counterexample `F` to Frankl's union-closed conjecture has odd cardinality:
> writing `|F| = 2k + 1`, every element has frequency at most `k`.
>
> **Theorem 6.4 (Tight witness for deletion).** Let `A ∈ F` be admissibly
> removable.  Then there exists an element `x_A ∉ A` with `d_F(x_A) = k`.

The hypotheses mirror the existing UC library (`UC.IsUnionClosed`,
`UC.present`, `UC.count`) which lives in `Lib/Statement.lean`.  **Import note:**
this container is a read-only root with no lake project, so sibling `.lean`
modules cannot resolve to `.olean` — `import Lib.Statement` fails with "module
not on the Lean search path".  The three definitions (`IsUnionClosed`,
`present`, `count`) are therefore duplicated verbatim below so the statement
elaborates standalone.  They are type-identical to the `Lib/Statement.lean`
versions; a reader who wants the single source of truth should compare against
that file before proving anything that imports this one.

The minimum-cardinality hypothesis is: every *smaller* union-closed nonempty
nontrivial family on the same ground set satisfies Frankl's conjecture.
Normalization per Prop 6.2 gives `empty_mem : ∅ ∈ F`.

## How the informal statement is rendered

- **`k` is shared.**  Both conclusions use the *same* `k : ℕ` witnessing
  `2*k + 1 = F.card`.  Conclusion (1) asserts this `k` exists and bounds every
  frequency by it; conclusion (2) asserts the tight-witness frequency is exactly
  this `k`.  This is the source's "Henceforth write `|F| = 2k + 1`".
- **Frequency** is `UC.count F a = (F.filter (a ∈ ·)).card`, rendered exactly.
- **Admissibly removable** (Definition 2.1): `F.erase A` is union-closed *and*
  still contains a nonempty member.  The latter clause makes the deleted family
  non-trivial (`≠ {∅}`), which is exactly what Thm 6.4's minimality call needs.
  (A family with a nonempty member is automatically not `{∅}`.)  The source's
  Lemma 6.1 supplies that every inclusion-minimal nonempty member is at least
  removable; Thm 6.4 states the tight witness for every *admissibly* removable
  member, the stronger clause rendered here.
- **`x ∉ A`** is written as `x ∉ A` on the `Finset α` level, matching the
  source's `x_A ∉ A`.
- **Elements of the family** are per `UC.present`; a tight witness `x` is a
  ground-set element omitted by `A`.

This is a *statement-carrying type*, not a proof: the `sorry` bodies assert the
source's theorems under the stated hypotheses.  `#print axioms` below reports
`sorryAx` (the truth of these theorems rests on the paper, not on the kernel).
-/

namespace UC

open Finset

/-- Union-closed family: closed under binary union.  (Identical to
`Lib/Statement.lean`.  Duplicated here because sibling imports don't resolve in
this container.) -/
def IsUnionClosed {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F

/-- An element is *present* if it occurs in some member of `F`. -/
def present {α : Type*} (F : Finset (Finset α)) (a : α) : Prop :=
  ∃ A ∈ F, a ∈ A

/-- Abundance of `a`: the exact number of members of `F` containing `a`. -/
def count {α : Type*} [DecidableEq α] (F : Finset (Finset α)) (a : α) : ℕ :=
  (F.filter fun A : Finset α => a ∈ A).card

end UC

namespace Spence

open Finset
open UC

/-- A member `A` is *removable* (Spence Definition 2.1) if `F.erase A` is
union-closed. -/
def Removable {α : Type*} [DecidableEq α] (F : Finset (Finset α)) (A : Finset α) : Prop :=
  IsUnionClosed (F.erase A)

/-- A member `A` is *admissibly removable* (Spence Definition 2.1) if deleting
it keeps the family union-closed and leaves at least one nonempty member.  The
latter clause makes the deleted family non-trivial, which is what the
minimality hypothesis in Thm 6.4 requires. -/
def AdmissiblyRemovable {α : Type*} [DecidableEq α]
    (F : Finset (Finset α)) (A : Finset α) : Prop :=
  IsUnionClosed (F.erase A) ∧ (F.erase A).Nonempty

/-- **Spence Thm 6.3 + 6.4, structural assertion for a minimum-cardinality
counterexample** (`src: Spence 2026 zenodo 20800102, Thm 6.3/6.4`).

Hypotheses: `F` is finite (`Finset (Finset α)`) on ground set `α`; union-closed;
nonempty; non-trivial (`F ≠ {∅}`); normalized with `∅ ∈ F` (Prop 6.2); and
*minimum-cardinality* — every strictly smaller union-closed nonempty nontrivial
family on `α` has an abundant element (`∃ a, present G a ∧ 2 * count G a ≥
G.card`).

Conclusions:
1. `∃ k, 2*k + 1 = F.card ∧ ∀ a, count F a ≤ k`   (Thm 6.3).
2. For the same `k`: every admissibly-removable `A ∈ F` is omitted by some
   element `x` whose frequency in `F` is exactly `k` (Thm 6.4).

Asserting the source statement, not proving it — the `sorry` is the point. -/
theorem spence_minimal_counterexample_structure {α : Type*} [Fintype α] [DecidableEq α]
    (F : Finset (Finset α))
    (huc : IsUnionClosed F)
    (hne : F.Nonempty)
    (hntriv : F ≠ ({∅} : Finset (Finset α)))
    (empty_mem : (∅ : Finset α) ∈ F)
    (hmin : ∀ G : Finset (Finset α), IsUnionClosed G → G.Nonempty →
      G ≠ ({∅} : Finset (Finset α)) → G.card < F.card →
        ∃ a : α, present G a ∧ 2 * count G a ≥ G.card) :
    ∃ k : Nat,
      2 * k + 1 = F.card
        ∧ (∀ a : α, count F a ≤ k)
        ∧ (∀ A ∈ F, AdmissiblyRemovable F A → ∃ x : α, x ∉ A ∧ count F x = k) := by
  sorry

end Spence

#print axioms Spence.spence_minimal_counterexample_structure
