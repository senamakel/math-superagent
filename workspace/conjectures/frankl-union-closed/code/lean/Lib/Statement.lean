import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Finset.Union
import Mathlib.Data.Set.Basic

/-!
# The union-closed sets conjecture (Frankl) — statement only

Informal statement (`problem.md`):

> Let `F` be a finite family of finite sets, closed under union:
> `A, B ∈ F ⟹ A ∪ B ∈ F`, and `F ≠ {∅}`.  Then there exists an element `x`
> belonging to at least `|F|/2` of the members of `F`.  Call such an element
> *abundant*.  The conjecture asserts every union-closed family (other than
> the trivial `{∅}`) has one.

This file formalises that conjecture as a Lean `theorem` whose *type* carries
every hypothesis, ending in `:= by sorry`.  It is NOT a proof — the conjecture
is open, and the deliverable here is a statement that elaborates, i.e. a type
that could be inhabited if the conjecture is true.

## How the informal statement is rendered, and where it could differ

- **Family as a `Finset (Finset α)`.**  `F` is the finite family; its finiteness
  and the finiteness of each member are both carried by `Finset`.  The ground
  set of candidate elements is `α`, required `[Fintype α]` so that "some element"
  ranges over a finite type.  A member of `F` that contains `a` witnesses
  `present F a`; elements not in the union of `F` never occur in any member, so
  `present` is the right domain for "elements of the family".
- **Union-closure** is `IsUnionClosed F := ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F`.
- **"At least `|F|/2`"** is rendered exactly, over integers, as
  `2 * count F a ≥ F.card`.  Since `count` is a `ℕ`, this is equivalent to the
  real inequality `count ≥ |F|/2` and does not involve division or rounding.
- **The trivial-family exclusion** is stated as two separate hypotheses:
  `hne : F.Nonempty` and `hntriv : F ≠ ({∅} : Finset (Finset α))`.  The informal
  "other than `{∅}`" is exactly `hntriv`, and `hne` is added because the empty
  family `F = ∅` satisfies union-closure and `F ≠ {∅}` but has no element at
  all — so a statement without `hne` would be *false for `F = ∅`*.  This is the
  main place a careless rendering diverges: `problem.md`'s "F ≠ {∅}" alone is
  not enough to exclude the empty family.
- **`present F a`** is included in the conclusion so the abundant element is
  genuinely an element of the family's ground set (for `F ≠ {∅}` nonempty this
  is automatic, but keeping it explicit makes the statement self-contained).

The conjecture itself is stated as `union_closed_conjecture` below.
-/

namespace UC

open Finset

/-- Union-closed family: closed under binary union. -/
def IsUnionClosed {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F

/-- An element is *present* if it occurs in some member of `F` (it is in the
union / ground set of the family). -/
def present {α : Type*} (F : Finset (Finset α)) (a : α) : Prop :=
  ∃ A ∈ F, a ∈ A

/-- Abundance of `a`: the exact number of members of `F` containing `a`. -/
def count {α : Type*} [DecidableEq α] (F : Finset (Finset α)) (a : α) : ℕ :=
  (F.filter fun A : Finset α => a ∈ A).card

/-- **Frankl's union-closed sets conjecture.**

Every finite union-closed family `F` of subsets of a finite ground set, other
than the trivial `{∅}`, has an *abundant* element: some element `a` present in
`F` that belongs to at least half of the members (equivalently
`2 · count F a ≥ F.card`).

This is the statement, not a proof.  The `sorry` is the whole point: the
conjecture is open, and the type above is what a proof would have to inhabit.
-/
theorem union_closed_conjecture {α : Type*} [Fintype α] [DecidableEq α]
    (F : Finset (Finset α)) (huc : IsUnionClosed F) (hne : F.Nonempty)
    (hntriv : F ≠ ({∅} : Finset (Finset α))) :
    ∃ a : α, present F a ∧ 2 * count F a ≥ F.card := by
  sorry

end UC

#print axioms UC.union_closed_conjecture
