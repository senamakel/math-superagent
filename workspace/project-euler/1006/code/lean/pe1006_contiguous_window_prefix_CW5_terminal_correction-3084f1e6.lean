import Mathlib

namespace PE1006CW5

/-!
CW5 decomposition.  The original node omitted the essential width hypothesis
`k + 1 ≤ N`: without it, truncated natural subtraction makes the asserted
identity false (for example N=3,k=10,V=1).  The gaps below isolate the exact
partition and the semantic identification of the terminal block with Ψ.
-/

abbrev SumI (V : ℕ → ℤ) (a b : ℕ) : ℤ :=
  ∑ r ∈ Finset.Icc a b, (V r)^2

/- gap
id: CW5-range-partition
lemma: ∀ (N k : ℕ), k + 1 ≤ N → Finset.Icc 0 (N - 1) = Finset.Icc 0 (N - k - 2) ∪ Finset.Icc (N - k - 1) (N - 1)
status: open
next: Prove by ext r; omega, then discharge the finite-set disjointness needed by sum_union.
-/

/- gap
id: CW5-range-disjoint
lemma: ∀ (N k : ℕ), k + 1 ≤ N → Disjoint (Finset.Icc 0 (N - k - 2)) (Finset.Icc (N - k - 1) (N - 1))
status: open
next: Apply Finset.disjoint_left and omega to the two membership inequalities.
-/

/- gap
id: CW5-terminal-identification
lemma: ∀ (N k : ℕ) (V : ℕ → ℤ), Ψ k = SumI V (N-k-1) (N-1)
status: open
next: Instantiate CW1's exact terminal-window bijection and CW2's value-preservation lemma; then rewrite the finite sum over the bijection.
-/

lemma range_partition
    (N k : ℕ) (hwidth : k + 1 ≤ N) :
    Finset.Icc 0 (N - 1) =
      Finset.Icc 0 (N - k - 2) ∪ Finset.Icc (N - k - 1) (N - 1) := by
  ext r
  simp only [Finset.mem_Icc, Finset.mem_union]
  omega

lemma range_disjoint
    (N k : ℕ) (hwidth : k + 1 ≤ N) :
    Disjoint (Finset.Icc 0 (N - k - 2)) (Finset.Icc (N - k - 1) (N - 1)) := by
  apply Finset.disjoint_left.mpr
  intro r hr₁ hr₂
  simp only [Finset.mem_Icc] at hr₁ hr₂
  omega

lemma sum_partition
    (N k : ℕ) (V : ℕ → ℤ) (hwidth : k + 1 ≤ N) :
    SumI V 0 (N - 1) = SumI V 0 (N - k - 2) + SumI V (N - k - 1) (N - 1) := by
  rw [range_partition N k hwidth]
  rw [Finset.sum_union (range_disjoint N k hwidth)]
  rfl

/--
The terminal-correction identity, conditional on the two substantive leaves:
CW1 identifies Ψ with the terminal block, while `hwidth` ensures the natural
intervals really partition the full range.  The original node's `hlo` and
`hhi` are retained as interface hypotheses, although `hwidth` is the crucial
one for avoiding underflow.
-/
theorem terminal_correction
    (N k : ℕ) (V : ℕ → ℤ) (Ψ : ℕ → ℤ)
    (hlo : N - k - 1 ≤ N - 1)
    (hhi : N - k - 2 < N)
    (hwidth : k + 1 ≤ N)
    (hterminal : Ψ k = SumI V (N - k - 1) (N - 1)) :
    Ψ k = SumI V 0 (N - 1) - SumI V 0 (N - k - 2) := by
  rw [hterminal]
  have hp := sum_partition N k V hwidth
  linarith

#print axioms range_partition
#print axioms range_disjoint
#print axioms sum_partition
#print axioms terminal_correction

end PE1006CW5
