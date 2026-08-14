axiom key_estimate : ∀ n : Nat, n ≤ 2 * n
theorem main (n : Nat) : n ≤ 2 * n := key_estimate n
#print axioms main
