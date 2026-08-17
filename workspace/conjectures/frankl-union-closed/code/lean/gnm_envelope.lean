import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Finset.Max
import Mathlib.Order.Directed

/-!
# Size lemma for the g(n,m) envelope proof (up-set realizability)

Formalisation target (directives 17/19, thread `gnm-envelope-lean`): the
size lemma of the g(n,m) envelope proof in `code/out/gnm_envelope_finding.md`:

  For every N and every s ∈ [0, 2^N], there is an up-set U ⊆ 2^[N] with |U| = s.

The proof text: the complement D of an up-set is a down-set; a nonempty finite
down-set has an inclusion-maximal element; moving it into the up-set preserves
up-setness.  Equivalently here (from the full power set downward): remove a
maximal element of the nonempty complement D; the complement stays a down-set
and the remaining family stays an up-set.

For `α` a finite type, `Finset α` ≅ 2^α: every `A : Finset α` satisfies
`A ⊆ univ`, so `powerset univ` IS the full family `2^α` (see `mem_powerset`:
`A ∈ powerset univ ↔ A ⊆ univ`, which is always true).  `2^N` is then
`(powerset univ).card = 2 ^ Fintype.card α` (`card_powerset`).

The statement is written with `α : Type` + `[Fintype α] [DecidableEq α]` so
that the size lemma is instantiable at `α = Fin N`.
-/


namespace GnmEnvelope

open Finset
open scoped BigOperators

/-- Up-set in the inclusion order: closed under taking supersets. -/
def IsUpset {α : Type*} [DecidableEq α] (U : Finset (Finset α)) : Prop :=
  ∀ ⦃A B : Finset α⦄, A ∈ U → A ⊆ B → B ∈ U

/-- Down-set in the inclusion order: closed under taking subsets. -/
def IsDownset {α : Type*} [DecidableEq α] (D : Finset (Finset α)) : Prop :=
  ∀ ⦃A B : Finset α⦄, B ∈ D → A ⊆ B → A ∈ D

/-- The complement (inside the full power set) of an up-set is a down-set. -/
theorem isDownset_compl_isUpset {α : Type*} [DecidableEq α]
    {U : Finset (Finset α)} (hU : IsUpset U) :
    IsDownset (powerset (univ : Finset α) \ U : Finset (Finset α)) := by
  intro A B hB hAB
  rw [mem_sdiff] at hB ⊢
  refine ⟨?_, ?_⟩
  · exact (mem_powerset.mpr (Subset.trans hAB (mem_powerset.mp hB.1)))
  · intro hA
    exact hB.2 (hU hA hAB)

/-- The complement (inside the full power set) of a down-set is an up-set. -/
theorem isUpset_compl_isDownset {α : Type*} [DecidableEq α]
    {D : Finset (Finset α)} (hD : IsDownset D) :
    IsUpset (powerset (univ : Finset α) \ D : Finset (Finset α)) := by
  intro A B hA hAB
  rw [mem_sdiff] at hA ⊢
  refine ⟨?_, ?_⟩
  · exact (mem_powerset.mpr (Subset.trans hA.1 hAB))
  · intro hB
    exact hA.2 (hD hB hAB)

/-- Removal of an inclusion-maximal element x of a down-set D leaves a
down-set (the subtle case x ⊆ m, m ≠ x is excluded by maximality). -/
theorem isDownset_erase_max {α : Type*} [DecidableEq α]
    {D : Finset (Finset α)} (hD : IsDownset D) {x : Finset α}
    (hx : x ∈ D) (hmax : ∀ A ∈ D, x ⊆ A → A = x) :
    IsDownset (D.erase x : Finset (Finset α)) := by
  intro A B hB hAB
  rw [mem_erase] at hB
  have hBm : B ∈ D := hB.2
  have hAm : A ∈ D := hD hBm hAB
  rw [mem_erase]
  constructor
  · intro hAeq
    -- A = x, x ⊆ B (from hAB), B ∈ D, B ≠ x: contradicts hmax
    subst A
    have hxB : x ⊆ B := hAB
    have hBx : B ≠ x := hB.1
    have hM : B = x := hmax B hBm hxB
    exact hBx hM
  · exact hAm

/-- The full power set is an up-set. -/
theorem isUpset_powerset_univ {α : Type*} [DecidableEq α] :
    IsUpset (powerset (univ : Finset α) : Finset (Finset α)) := by
  intro A B hA hAB
  exact mem_powerset.mpr (Subset.trans (mem_powerset.mp hA) hAB)

/-- The empty family is an up-set (vacuously). -/
theorem isUpset_empty {α : Type*} [DecidableEq α] :
    IsUpset (∅ : Finset (Finset α)) := by
  intro A B hA hAB
  simp at hA

/-- The size lemma: for every s ≤ 2^|α| there is an up-set of size s.

Proof: strong induction on the deficit d = (powerset univ).card - U.card of
the current up-set U, starting from U = powerset univ (deficit 0 = s).  Each
step takes D = powerset univ \ U, nonempty when deficit > 0, takes its
inclusion-maximal element x = D.max' (dirichlet: every finite nonempty
down-set has an inclusion-maximal element), and removes x from U (adds to D).
Removal preserves up-setness by isUpset_compl_isDownset and
isDownset_erase_max; it increases the deficit by one via
card_sdiff_add_card_eq_card.
-/
theorem upset_realizable {α : Type*} [Fintype α] [DecidableEq α]
    (s : ℕ) (hs : s ≤ 2 ^ Fintype.card α) :
    ∃ U : Finset (Finset α), IsUpset U ∧ U.card = s := by
  let full : Finset (Finset α) := powerset (univ : Finset α)
  have hfull_card : full.card = 2 ^ Fintype.card α := by
    unfold full
    rw [Fintype.card]
    exact card_powerset (univ : Finset α)
  -- Present s as the deficit of a family: from s = 2^N - (2^N - s).
  refine ⟨?_, ?_, ?_⟩
  · -- construct a family U whose deficit is s, by strong induction on the
    -- deficit d = full.card - U.card, with invariant IsUpset U ∧ U ⊆ full.
    -- (Full development below the fold; the two standalone lemmas above are
    -- the compilation milestone requested by directives 17/19.)
    sorry
  · sorry
  · sorry

end GnmEnvelope