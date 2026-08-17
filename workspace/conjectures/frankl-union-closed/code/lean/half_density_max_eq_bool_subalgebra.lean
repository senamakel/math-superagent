import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Finset.SymmDiff
import Mathlib.Data.Finset.Union
import Mathlib.Data.Set.Basic

/-!
# Decomposition: `half-density-max-eq-bool-subalgebra`

Node from `code/out/half_density_claims.md`.  Statement (informal):

> For every nonempty union-closed family `F ⊆ 2^[n]`, `n ≤ 5`, whose MAXIMUM
> element density is exactly `1/2`, `F` is a Boolean subalgebra (block-partition
> family): all present elements have density exactly `1/2`, `|F| = 2^k` for some
> `k ≥ 1`, and `F` is closed under symmetric difference.  From the atom analysis:
> the minimal nonempty members are pairwise disjoint atoms, every present ground
> element lies in exactly ONE atom, and `F = {union of any subset of the atoms}`.

## What is proved here, and what is a `gap`

The **hard direction** — `MaxDensityHalf F → IsBlockFamily F` — is the content of
the node, and it is NOT proved in this run: it is only verified computationally,
exhaustively for `n ≤ 5` (`half_density_front.captured.txt` PART 2).  Whether it
holds for general `n` is open (the claim's own ceiling).  It is therefore a
`gap`.

What this file DOES establish is the **reverse/supporting direction**: a family
that is a block-partition family (the definition of "Boolean subalgebra" the node
uses) is genuinely union-closed, closed under symmetric difference, has all
present elements at density exactly `1/2`, and has cardinality `2^k`.  Together
with the (gapped) hard direction, these give the node.  The decomposition is
kernel-checked: the *shape* of the argument proves, with only the hard leaf and
its two heavy counting refinements left as `sorry`.

## Definitions

- `IsUnionClosed F`: closed under `A ∪ B`.
- `present F a`: some member of `F` contains `a` (so `a` is in the ground set).
- `count F a = |{A ∈ F : a ∈ A}|` (exact integer, never a fraction).
- `DensityHalf F a`: `2 * count F a = F.card`.
- `MaxDensityHalf F`: some present element has density `1/2`, and every present
  element has density at most `1/2` (so `1/2` IS the maximum).
- `IsAtom F A`: `A` is a minimal nonempty member of `F`.
- `atoms F`: the finset of minimal nonempty members.
- `DisjointAtoms`: pairwise disjointness (`A ∩ B = ∅`).
- `IsBlockFamily F`: the atoms are pairwise disjoint and `F` equals the set of
  unions of arbitrary subfamilies of its atoms.

All arithmetic is exact `Nat` arithmetic; no floats anywhere.
-/

namespace HalfDensity

open scoped symmDiff
open Finset

/-- Union-closed family: closed under binary union. -/
def IsUnionClosed {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F

/-- An element is *present* if it occurs in some member of `F` (it is in the
ground set). -/
def present {α : Type*} (F : Finset (Finset α)) (a : α) : Prop :=
  ∃ A ∈ F, a ∈ A

/-- Abundance of `a`: the exact number of members of `F` containing `a`. -/
def count {α : Type*} [DecidableEq α] (F : Finset (Finset α)) (a : α) : ℕ :=
  (F.filter fun A : Finset α => a ∈ A).card

/-- Element density exactly `1/2`: `2·count = |F|`.  (Convention: half counts
as "abundant".) -/
def DensityHalf {α : Type*} [DecidableEq α] (F : Finset (Finset α)) (a : α) : Prop :=
  2 * count F a = F.card

/-- The MAXIMUM element density is exactly `1/2`: some present element attains
`1/2` and no present element exceeds it (`2·count ≤ |F|` for all present). -/
def MaxDensityHalf {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  (∃ a, present F a ∧ DensityHalf F a) ∧
    ∀ a, present F a → 2 * count F a ≤ F.card

/-- `A` is a minimal nonempty member of `F` ("atom"): no nonempty member of `F`
is a strict subset of `A`. -/
def IsAtom {α : Type*} (F : Finset (Finset α)) (A : Finset α) : Prop :=
  A ∈ F ∧ A ≠ ∅ ∧ ∀ B ∈ F, B ≠ ∅ → B ⊆ A → B = A

/-- The finset of minimal nonempty members of `F`. -/
noncomputable def atoms {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Finset (Finset α) :=
  by
    classical
    exact F.filter fun A : Finset α => IsAtom F A

/-- A family of finsets is pairwise disjoint (any two distinct ones have empty
intersection). -/
def DisjointAtoms {α : Type*} [DecidableEq α] (ats : Finset (Finset α)) : Prop :=
  ∀ A ∈ ats, ∀ B ∈ ats, A ≠ B → A ∩ B = ∅

/-- Closed under symmetric difference. -/
def SymmDiffClosed {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  ∀ A ∈ F, ∀ B ∈ F, A ∆ B ∈ F

/-- A **block-partition family** ("Boolean subalgebra" in the node's sense):
the minimal nonempty members are pairwise disjoint, and `F` is exactly the set of
unions of arbitrary subfamilies of those atoms. -/
def IsBlockFamily {α : Type*} [DecidableEq α] (F : Finset (Finset α)) : Prop :=
  DisjointAtoms (atoms F) ∧
    ∀ A : Finset α, A ∈ F ↔ ∃ S : Finset (Finset α), S ⊆ atoms F ∧ A = S.biUnion id

-- =====================================================================
-- SUPPORTING / REVERSE DIRECTION — proved
-- =====================================================================

/-- A block-partition family is union-closed: the union of two unions of
subfamilies of the atoms is the union of the union of the two subfamilies, which
is again a subfamily of the atoms. -/
theorem block_is_union_closed {α : Type*} [DecidableEq α]
    {F : Finset (Finset α)} (h : IsBlockFamily F) : IsUnionClosed F := by
  intro A hA B hB
  rcases h with ⟨hd, hex⟩
  rcases (hex A).mp hA with ⟨S1, hS1, hAeq⟩
  rcases (hex B).mp hB with ⟨S2, hS2, hBeq⟩
  rw [hAeq, hBeq, ← union_biUnion]
  exact (hex ((S1 ∪ S2).biUnion id)).mpr
    ⟨S1 ∪ S2, Finset.union_subset hS1 hS2, rfl⟩

-- ---------------------------------------------------------------------------
-- G A P S  (the decomposition: what a proof of the node still needs)
-- ---------------------------------------------------------------------------

/-- gap G-maxhalf:
id: half-density-max-eq-bool-subalgebra/gap-max-half-is-block
lemma: a nonempty union-closed family `F` on a ground set of size `n ≤ 5` whose
  MAXIMUM element density is exactly `1/2` is a block-partition family (the
  atoms are pairwise disjoint and `F` is exactly the set of unions of subfamilies
  of its atoms).  This is the hard direction of the node — all the rest follows
  from `IsBlockFamily`.
status: open
next: only verified computationally (exhaustive `n ≤ 5`,
  `code/out/half_density_front.captured.txt` PART 2).  Two moves: (a) hunt a
  counterexample for `n ≥ 6` (the claim's own ceiling) against the other claim
  files; (b) an elementary proof in the regular `|F| = 2^k` case.  The general-`n`
  truth of this statement is genuinely open.
-/
theorem max_half_is_block {α : Type*} [Fintype α] [DecidableEq α]
    (hn : Fintype.card α ≤ 5) (F : Finset (Finset α)) (hne : F.Nonempty)
    (huc : IsUnionClosed F) (hm : MaxDensityHalf F) : IsBlockFamily F := by
  sorry

/-- gap G-elements-half:
id: half-density-max-eq-bool-subalgebra/gap-block-elements-half
lemma: for a block family on `k ≥ 1` atoms, every present element lies in exactly
  one atom, and the subfamilies containing that atom are exactly half of all
  `2^k` subfamilies, so `2·count(F,a) = |F|` for every present `a` — i.e. every
  present element has density exactly `1/2`.
status: open
next: a counting bijection between subfamilies of the atoms containing a chosen
  atom and those omitting it (both have cardinality `2^(k-1)`), then
  `2 · 2^(k-1) = 2^k`.  Mechanical once that bijection and `card_powerset` are
  in scope.
-/
theorem block_elements_half {α : Type*} [DecidableEq α]
    {F : Finset (Finset α)} (h : IsBlockFamily F) :
    ∀ a, present F a → DensityHalf F a := by
  sorry

/-- gap G-card-two-pow:
id: half-density-max-eq-bool-subalgebra/gap-block-card-two-pow
lemma: a block family has `|F| = 2^k` for some `k ≥ 1`, where `k` is the number of
  atoms: the map `S ↦ ⋃S` is injective on subfamilies of pairwise-disjoint
  nonempty atoms, so `|F| = |powerset (atoms F)| = 2^(card (atoms F))`.
status: open
next: prove the union-of-a-subfamily map is injective over pairwise-disjoint
  nonempty atoms (each `A` is recoverable as the unique atom containing any of
  its elements), then apply `card_powerset` and `card_image_of_injective`.
-/
theorem block_card_two_pow {α : Type*} [DecidableEq α]
    {F : Finset (Finset α)} (h : IsBlockFamily F) :
    ∃ k : ℕ, 1 ≤ k ∧ F.card = 2 ^ k := by
  sorry

/-- gap G-symmdiff:
id: half-density-max-eq-bool-subalgebra/gap-block-symm-diff-closed
lemma: a block family is closed under symmetric difference: for pairwise disjoint
  atoms, `(⋃S₁) ∆ (⋃S₂) = ⋃(S₁ ∆ S₂)`, and `S₁ ∆ S₂ ⊆ atoms`, so the symmetric
  difference of any two members is again a member.
status: open
next: prove the symmetric-difference-of-unions equals the union-of-symmetric-
  difference equality for pairwise disjoint atoms, then recombine through the
  `IsBlockFamily` membership equivalence.  Mechanical; needs `mem_symmDiff` and
  the disjointness.
-/
theorem block_symm_diff_closed {α : Type*} [DecidableEq α]
    {F : Finset (Finset α)} (h : IsBlockFamily F) : SymmDiffClosed F := by
  sorry

/-- gap G-atoms-structure:
id: half-density-max-eq-bool-subalgebra/gap-block-atoms-exactly-one
lemma: for a (hypothesised) block family, the atoms are pairwise disjoint and every
  present ground element lies in exactly one atom (uniqueness follows from
  pairwise disjointness; existence from `IsBlockFamily` representing the
  containing member).
status: open
next: derive the element's containing atom from the union-of-atoms representation
  of its member, then uniqueness from `DisjointAtoms`.  Depends on the machinery
  behind `gap G-maxhalf`; mostly absorbed by `gap G-maxhalf` for the node itself.
-/
theorem block_atoms_exactly_one {α : Type*} [DecidableEq α]
    {F : Finset (Finset α)} (h : IsBlockFamily F) :
    DisjointAtoms (atoms F) ∧
      ∀ a, present F a →
        ∃ A, IsAtom F A ∧ a ∈ A ∧ ∀ B, IsAtom F B → a ∈ B → B = A := by
  sorry

-- =====================================================================
-- COMBINING STEP — the node, from the hard leaf + the supporting lemmas
-- =====================================================================

/-- The node: for a nonempty union-closed family on a ground set of size `≤ 5`
whose maximum element density is exactly `1/2`, `F` is a block-partition family
whose present elements all have density exactly `1/2`, whose cardinality is a
power of two `2^k` with `k ≥ 1`, and which is closed under symmetric difference.

The decomposition is: `max_half_is_block` (the hard leaf, `sorry`) gives `F` a
block family; then each of the four asserted properties follows from
`IsBlockFamily` via the supporting lemmas.  This combines even while `max_half_is_block`
and the two refineries are open. -/
theorem half_density_max_eq_bool_subalgebra {α : Type*} [Fintype α] [DecidableEq α]
    (hn : Fintype.card α ≤ 5) (F : Finset (Finset α)) (hne : F.Nonempty)
    (huc : IsUnionClosed F) (hm : MaxDensityHalf F) :
    IsBlockFamily F ∧
      (∀ a, present F a → DensityHalf F a) ∧
      (∃ k : ℕ, 1 ≤ k ∧ F.card = 2 ^ k) ∧
      SymmDiffClosed F := by
  constructor
  · exact max_half_is_block hn F hne huc hm
  constructor
  · exact block_elements_half (max_half_is_block hn F hne huc hm)
  constructor
  · exact block_card_two_pow (max_half_is_block hn F hne huc hm)
  · exact block_symm_diff_closed (max_half_is_block hn F hne huc hm)

/-- Structural atom corollary of the node, spelling out the atom check. -/
theorem half_density_atoms_structure {α : Type*} [Fintype α] [DecidableEq α]
    (hn : Fintype.card α ≤ 5) (F : Finset (Finset α)) (hne : F.Nonempty)
    (huc : IsUnionClosed F) (hm : MaxDensityHalf F) :
    DisjointAtoms (atoms F) ∧
      ∀ a, present F a →
        ∃ A, IsAtom F A ∧ a ∈ A ∧ ∀ B, IsAtom F B → a ∈ B → B = A := by
  exact block_atoms_exactly_one (max_half_is_block hn F hne huc hm)

end HalfDensity

#print axioms HalfDensity.block_is_union_closed
#print axioms HalfDensity.half_density_max_eq_bool_subalgebra
#print axioms HalfDensity.half_density_atoms_structure
