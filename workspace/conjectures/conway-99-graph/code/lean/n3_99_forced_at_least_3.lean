import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Combinatorics.SimpleGraph.Clique
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Nat.Factorization.Basic

/-!
# n3 = 99: n3 >= 3 (sharpened), and the admissible set at (99,14)

Claim node: `n3-99-forced-at-least-3`, from `code/out/n3-screening-claims.md`.

## The informal claim, restated so every hypothesis is carried by a binder

Let `n3` be the number of *disjoint triangle pairs joined by exactly two
edges* in a hypothetical strongly regular graph `srg(99,14,1,2)`.  Then:

  (a) **residue (unconditional exact integer arithmetic over the sourced 62
      Reimbayev order-6 formulas)** — `n3 ≡ 0 (mod 3)`;
  (b) **n3 >= 1 (sourced + re-derived Makhnev 1988 conditional)** — any
      putative `srg(99,14,1,2)` has `n3 >= 1`, since `n3 = 0` would force the
      parameter-infeasible subobject `srg(33,12,1,6)`;
  (c) **cap** — `n3 <= 4158 = v·k·(k−2)/4` at `(99,14)`.

Combining (a)+(b) sharpens the previously recorded `n3 >= 1` to **`n3 >= 3`**
(`n3 in {3, 6, 9, ...}`), and with (c) the admissible set at `(99,14)` is
exactly the 1387 multiples of 3 in `[0, 4158]`.  `n3 = 0` and `n3 = 3` are both
arithmetically admissible (integrality alone forces nothing); `n3 = 4158` is
admissible while `n3 = 4159` is not (the cap 4158 is sharp).  This is a
**CONSTRAINT** on a hypothetical 99-graph, not a nonexistence proof, and it does
not claim existence.

## What is kernel-checked here and what is not

 * **Formalised (proved in Lean, no axioms).** The pure-integer core that the
   whole node rests on and that carries no graph-theoretic content:
   - the cap arithmetic `(99·14·(14−2))/4 = 4158`; `3 ∣ 4158` but `¬ 3 ∣ 4159`
     (the cap is sharp: 4158 admissible, 4159 not);
   - the *sharpening step*: `1 ≤ n ∧ 3 ∣ n ⇒ 3 ≤ n` — this is precisely the
     deduction "n3 >= 1 and n3 ≡ 0 (mod 3) hence n3 >= 3";
   - the count `#{n ∈ range 4159 | 3 ∣ n} = 1387`: the admissible set at
     (99,14) has exactly 1387 members (the multiples of 3 up to the cap,
     counting 0).

 * **Carried as `Cited` axioms** (as the run's convention for literature
   results that are not re-derived here):
   - `n3_ge_one`: `1 ≤ n3` for any putative srg(99,14,1,2) — Makhnev 1988 Thm 2
     via the contrapositive already formalised in
     `makhnev99_shorter_proof_integrality.lean` (the n3 = 0 branch forces the
     parameter-infeasible srg(33,12,1,6));
   - `n3_residue`: `3 ∣ n3` for any putative srg(99,14,1,2) — Reimbayev's 62
     order-6 count formulas, checked in exact Fraction arithmetic in
     `code/out/n3_order6_feasibility.py`;
   - `n3_cap`: `n3 ≤ 4158` for any putative srg(99,14,1,2) — the count bound
     `n3 ≤ v·k·(k−2)/4`, checked in
     `code/out/n3_upper_bounds_exact.py` / `n3_cap_crosscheck.py`.

  A theorem resting on any `Cited.*` axiom is `conditional`: the kernel checked
  the implication and checked nothing about the axioms.  `formalised` is used
  only for the pure arithmetic, which the kernel checked outright.
-/

open scoped BigOperators

namespace N3AtLeast3

/-- Number of edges between two (ordered) vertex subsets, i.e. the number of
pairs `(x,y)` with `x ∈ s`, `y ∈ t`, and `G.Adj x y`. -/
def edgeCountBetween {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (s t : Finset V) : ℕ :=
  ((s.product t).filter (fun p : V × V => G.Adj p.1 p.2)).card

/-- A pair of triangles `{T1, T2}` (an unordered 2-subset of the triangle set)
is *2-joined* when the two triangles are disjoint and have exactly two edges
between them.  This is Reimbayev's `n₃` configuration: a disjoint triangle
pair joined by exactly two edges. -/
def TwoJoinedBy {V : Type} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (P : Finset (Finset V)) : Prop :=
  ∃ T1 : Finset V, T1 ∈ P ∧
    ∃ T2 : Finset V, T2 ∈ P ∧ T1 ≠ T2 ∧ Disjoint T1 T2 ∧ edgeCountBetween G T1 T2 = 2

/-- `n3 G` — Reimbayev's n₃: the number of unordered disjoint triangle pairs
joined by exactly two edges in `G` (the triangles are the 3-cliques of `G`). -/
noncomputable def n3 {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    [DecidableRel G.Adj] : ℕ := by
  classical
  exact ((G.cliqueFinset 3).powersetCard 2).filter (fun P : Finset (Finset V) => TwoJoinedBy G P) |>.card

/-! ## Cited geometric/computational input (literature results) -/

namespace Cited

/-- src: Makhnev 1988, Mat. Zametki 44(5) 667–672, Thm 2 — any putative
srg(99,14,1,2) has `n₃ ≥ 1`, because `n₃ = 0` (Makhnev's condition (∗)) forces
the parameter-infeasible subobject srg(33,12,1,6).  This is the contrapositive
of `Makhnev99.no_srg_99_14_1_2_condstar` in
`code/lean/makhnev99_shorter_proof_integrality.lean`, where the arithmetic of
the rejection is kernel-checked and only the forced-subobject content is cited.
Here it is re-cited for self-containment of this file. -/
axiom n3_ge_one {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) :
  1 ≤ n3 G

/-- src: R. Reimbayev, order-6 induced-subgraph counts for the family
srg(n,k,1,2) (arXiv:2508.03377) — of the 62 order-6 count formulas, all force
`n₃ ≡ 0 (mod 3)`.  Checked in exact Fraction arithmetic in
`code/out/n3_order6_feasibility.py` (capture
`code/out/n3_order6_feasibility.captured.txt`); the residue is independent of
any nonexistence assumption, so the order-6 counts alone force `3 ∣ n3`. -/
axiom n3_residue {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) :
  3 ∣ n3 G

/-- src: count bound — `n₃ ≤ v·k·(k−2)/4 = 4158` at (99,14).  Checked in
exact integer arithmetic in `code/out/n3_upper_bounds_exact.py` and
`code/out/n3_cap_crosscheck.py`. -/
axiom n3_cap {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
    [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) :
  n3 G ≤ 4158

end Cited

/-! ## 1. The pure arithmetic kernel (formalised, no axioms) -/

/-- The cap at (99,14): `v·k·(k−2)/4 = 99·14·12/4 = 4158`. -/
lemma cap_eq : (99 : ℕ) * 14 * (14 - 2) / 4 = 4158 := by
  norm_num

/-- `3 ∣ 4158`: the cap is a multiple of 3. -/
lemma three_dvd_cap : (3 : ℕ) ∣ 4158 := by
  norm_num

/-- `¬ 3 ∣ 4159`: the cap is sharp — 4158 is admissible but 4159 is not. -/
lemma not_three_dvd_cap_succ : ¬ (3 : ℕ) ∣ 4159 := by
  norm_num

/-- The sharpening step — the deductive heart of the node: a positive multiple
of 3 is at least 3.  This is "n3 >= 1 and n3 ≡ 0 (mod 3) hence n3 >= 3". -/
lemma sharpen {n : ℕ} (h1 : 1 ≤ n) (hdvd : 3 ∣ n) : 3 ≤ n := by
  rcases hdvd with ⟨c, hc⟩
  by_contra h
  have hlt : n < 3 := by omega
  omega

/-- The admissible set at (99,14) has exactly 1387 members: the multiples of 3
(including 0) in `[0, 4158]`.  Uses `Nat.card_multiples'` to count the nonzero
multiples of 3 in the range, then adds the single zero multiple. -/
lemma count_admissible_multiples :
    ((Finset.range 4159).filter fun n => 3 ∣ n).card = 1387 := by
  have hcard := Nat.card_multiples' (N := 4158) (n := 3)
  have hB : ((Finset.range 4159).filter fun n : ℕ => n ≠ 0 ∧ 3 ∣ n).card = 1386 := by
    simpa using hcard
  have hfull : (Finset.range 4159).filter (fun n : ℕ => 3 ∣ n)
      = insert 0 ((Finset.range 4159).filter fun n : ℕ => n ≠ 0 ∧ 3 ∣ n) := by
    ext n
    by_cases hn0 : n = 0
    · subst n; simp
    · constructor
      · intro hn
        rw [Finset.mem_filter] at hn
        rcases hn with ⟨hlt, hd⟩
        rw [Finset.mem_insert]
        apply Or.inr
        rw [Finset.mem_filter]
        exact ⟨hlt, hn0, hd⟩
      · intro hn
        rw [Finset.mem_insert] at hn
        rcases hn with hz | hB
        · exfalso; exact hn0 hz
        · rw [Finset.mem_filter] at hB
          rw [Finset.mem_filter]
          exact ⟨hB.1, hB.2.2⟩
  have h0B : 0 ∉ (Finset.range 4159).filter (fun n : ℕ => n ≠ 0 ∧ 3 ∣ n) := by
    simp
  rw [hfull]
  rw [Finset.card_insert_of_notMem h0B]
  rw [hB]

/-! ## 2. The sharpened bound, conditional on the cited input

`conditional`: rests on `Cited.n3_ge_one`, `Cited.n3_residue`, `Cited.n3_cap`. -/

/-- Any putative srg(99,14,1,2) has `n3 >= 3`: from the Makhnev conditional
(`n3 >= 1`) and the Reimbayev residue (`3 ∣ n3`).  This sharpens the recorded
`n3 >= 1`.  `conditional` on `Cited.n3_ge_one` and `Cited.n3_residue`. -/
theorem any_srg99_n3_ge_three {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) :
    3 ≤ n3 G := by
  exact sharpen (Cited.n3_ge_one G hG) (Cited.n3_residue G hG)

/-- Any putative srg(99,14,1,2) has `n3` a positive multiple of 3 within the
cap, i.e. `n3 ∈ {3, 6, 9, ..., 4158}` — the admissible set at (99,14).
`conditional` on all three `Cited` axioms. -/
theorem any_srg99_n3_admissible {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hG : G.IsSRGWith 99 14 1 2) :
    3 ≤ n3 G ∧ 3 ∣ n3 G ∧ n3 G ≤ 4158 := by
  exact ⟨sharpen (Cited.n3_ge_one G hG) (Cited.n3_residue G hG),
         Cited.n3_residue G hG, Cited.n3_cap G hG⟩

/-! ## 3. Kernel-checked sanity facts (formalised, no axioms)

`n3 = 0` and `n3 = 3` are both arithmetically admissible (the residue alone
forces nothing); `n3 = 4158` is admissible while `n3 = 4159` is not.  These
record the sharp boundary on the n3 axis purely arithmetically. -/

/-- `0` satisfies the residue but not the `n3 >= 1`/`n3 >= 3` bound — so the
residue and cap alone admit `n3 = 0`, as the controls (n3 = 0 and exist) also
show. -/
lemma residue_alone_admits_zero : 3 ∣ (0 : ℕ) := by
  exact dvd_zero 3

/-- `4158` satisfies the cap and the residue (admissible); `4159` exceeds the
cap (not admissible). -/
lemma cap_sharp : 3 ∣ (4158 : ℕ) ∧ (4159 : ℕ) > 4158 := by
  constructor <;> norm_num

#check N3AtLeast3.cap_eq
#check N3AtLeast3.three_dvd_cap
#check N3AtLeast3.not_three_dvd_cap_succ
#check N3AtLeast3.sharpen
#check N3AtLeast3.count_admissible_multiples
#check N3AtLeast3.any_srg99_n3_ge_three
#check N3AtLeast3.any_srg99_n3_admissible

-- The pure arithmetic: formalised (no axioms).
#print axioms N3AtLeast3.cap_eq
#print axioms N3AtLeast3.three_dvd_cap
#print axioms N3AtLeast3.not_three_dvd_cap_succ
#print axioms N3AtLeast3.sharpen
#print axioms N3AtLeast3.count_admissible_multiples

-- The sharpened bound: rests on Cited axioms -> conditional.
#print axioms N3AtLeast3.any_srg99_n3_ge_three
#print axioms N3AtLeast3.any_srg99_n3_admissible

end N3AtLeast3
