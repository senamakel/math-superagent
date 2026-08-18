import Mathlib

namespace PE1006G1

def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

def FactorSet {α : Type*} (w : List α) (k : ℕ) : Set (List α) :=
  {u | ∃ i, (w.drop i).take k = u ∧ i + k ≤ w.length}

def FibSubwords (k : ℕ) : Set (List Char) :=
  {u | ∃ n, u ∈ FactorSet (fibWord n) k}

/- gap
id: g1-factor-stabilisation
lemma: ∀ (k : ℕ), ∃ n, FibSubwords k = {u | u ∈ FactorSet (fibWord n) k}
status: open
next: prove using fibWord-prefix nesting and a length bound for factors
end_gap -/
axiom g1_factor_stabilisation : ∀ (k : ℕ), ∃ n, FibSubwords k = {u | u ∈ FactorSet (fibWord n) k}

/- gap
id: g1-fibonacci-sturmian-complexity
lemma: ∀ (k : ℕ) (h : 1 ≤ k), InfiniteFibFactors k).ncard = k + 1
status: open
next: define the infinite Fibonacci word factor set and invoke the Sturmian complexity theorem
end_gap -/
axiom g1_fibonacci_sturmian_complexity : ∀ (k : ℕ) (h : 1 ≤ k), True

/- gap
id: g1-finite-infinite-factor-equivalence
lemma: ∀ (k : ℕ), ∃ n, (FibSubwords k).ncard = (FactorSet (fibWord n) k).ncard
status: open
next: derive by rewriting with g1-factor-stabilisation and taking cardinalities
end_gap -/
axiom g1_finite_infinite_factor_equivalence : ∀ (k : ℕ), ∃ n, (FibSubwords k).ncard = (FactorSet (fibWord n) k).ncard

theorem fib_subword_count : ∀ (k : ℕ) (h : 1 ≤ k), (FibSubwords k).ncard = k + 1 := by
  intro k hk
  obtain ⟨n, hstab⟩ := g1_factor_stabilisation k
  obtain ⟨hcomplex⟩ := g1_fibonacci_sturmian_complexity k hk
  obtain ⟨n', heq⟩ := g1_finite_infinite_factor_equivalence k
  sorry

#print axioms fib_subword_count

end PE1006G1
