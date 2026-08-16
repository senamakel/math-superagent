> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/leanpool-erdostuzavaltr-capcup.lean.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/Vilin97/lean-pool/main/LeanPool/ErdosTuzaValtr/Main/CapCup.lean | converted from plain text -->

/-
Copyright (c) 2026 Jineon Baek. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Jineon Baek
-/

import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Ring.RingNF
import LeanPool.ErdosTuzaValtr.Config.Default
import LeanPool.ErdosTuzaValtr.Etv.Default

/-!
# LeanPool.ErdosTuzaValtr.Main.CapCup

Imported Lean Pool material for `LeanPool.ErdosTuzaValtr.Main.CapCup`.
-/

noncomputable section

namespace Config

variable {α : Type _} [LinearOrder α] (C : Config α)

theorem has_cap2_cup2 {S : Finset α} (hS : 1 < S.card) : C.HasNCap 2 S ∧ C.HasNCup 2 S := by
  set l := S.sort (· ≤ ·) with eq_l
  have hl : 2 ≤ l.length := by rw [eq_l, Finset.length_sort]; exact hS
  rcases List.takeHead2 hl with ⟨a, b, t, eq_ab⟩
  have sorted : l.Pairwise (· < ·) := (Finset.sortedLT_sort S).pairwise
  rw [eq_ab] at sorted
  have a_lt_b : a < b := (List.pairwise_cons.mp sorted).1 b (by simp)
  have a_in_S : a ∈ S := by
    have : a ∈ l := by rw [eq_ab]; simp
    rwa [eq_l, Finset.mem_sort] at this
  have b_in_S : b ∈ S := by
    have : b ∈ l := by rw [eq_ab]; simp
    rwa [eq_l, Finset.mem_sort] at this
  refine ⟨⟨[a, b], ⟨?_, rfl⟩, ?_⟩, ⟨[a, b], ⟨?_, rfl⟩, ?_⟩⟩
  · rw [Cap.pair]; exact a_lt_b
  · rw [List.cons_in, List.cons_in]; exact ⟨a_in_S, b_in_S, List.nil_in⟩
  · rw [Cup.pair]; exact a_lt_b
  · rw [List.cons_in, List.cons_in]; exact ⟨a_in_S, b_in_S, List.nil_in⟩

theorem binom_eq (a b : ℕ) :
    (a + b + 2).choose (a + 1) = (a + b + 1).choose a + (a + b + 1).choose (a + 1) :=
  rfl

theorem cap_cup (a b : ℕ) (S : Finset α) (hS : Nat.choose (a + b) a < S.card) :
    C.HasNCap (a + 2) S ∨ C.HasNCup (b + 2) S := by
  classical
  revert a b S hS
  refine Nat.pincerRecursion ?_ ?_ ?_
  -- case b = 0
  · intro a S hS
    rw [Nat.add_zero, Nat.choose_self] at hS
    right
    exact (C.has_cap2_cup2 hS).right
  -- case a = 0
  · intro a S hS
    rw [Nat.zero_add, Nat.choose_zero_right] at hS
    left
    exact (C.has_cap2_cup2 hS).left
  -- diagonal induction
  · intro a b
    set sz_ab1 := (a + (b + 1)).choose a with eq_sz_ab1
    set sz_a1b := (a + 1 + b).choose (a + 1) with eq_sz_a1b
    set sz_a1b1 := (a + 1 + (b + 1)).choose (a + 1) with eq_sz_a1b1
    have eq_sz : sz_a1b1 = sz_ab1 + sz_a1b := by
      rw [eq_sz_ab1, eq_sz_a1b, eq_sz_a1b1]
      rw [show a + 1 + (b + 1) = (a + (b + 1)) + 1 by ring,
        show a + 1 + b = a + (b + 1) by ring, Nat.choose_succ_succ (a + (b + 1)) a]
    -- numerical details now not relevant
    clear eq_sz_ab1 eq_sz_a1b eq_sz_a1b1
    intro hab1 ha1b S hS
    set is_start_of_cap : α → Prop := fun p =>
      ∃ c, C.Cap c ∧ c.In S ∧ c.length = a + 2 ∧ p ∈ c.head? with def_is_start_of_cap
    set T := Finset.filter is_start_of_cap S with def_T
    have eq_card : (S \ T).card + T.card = S.card :=
      by
      apply Finset.card_sdiff_add_card_eq_card
      rw [def_T]; exact S.filter_subset is_start_of_cap
    have sz_cases : sz_ab1 < (S \ T).card ∨ sz_a1b < T.card := by by_contra! h; omega
    rcases sz_cases with sz_cases | sz_cases
    -- case sz_ab1 < (S \ T).card
    · rcases hab1 (S \ T) sz_cases with hcap | hcup
      · rcases hcap with ⟨c, ⟨c_cap, c_length⟩, c_in⟩
        have c_nnil : c ≠ [] := by
          rintro rfl
          simp_all
        rcases List.takeHead c_nnil with ⟨ch, ct, eq_c⟩
        have h : ch ∈ S \ T := c_in ch (by rw [eq_c]; simp)
        rw [def_T, Finset.mem_sdiff, Finset.mem_filter] at h
        obtain ⟨c_in_S, h⟩ := h
        exfalso
        apply h
        refine ⟨c_in_S, c, c_cap, ?_, ?_, ?_⟩
        · intro x hx
          exact Finset.sdiff_subset (c_in x hx)
        · rw [c_length]
        · rw [eq_c]; simp
      · right
        refine hasNCup_supset ?_ hcup
        exact Finset.sdiff_subset
    -- case sz_a1b < T.card

*[excerpt ends; 1972 characters not shown — see `research/sources/leanpool-erdostuzavaltr-capcup.lean.full.md`]*
