import Mathlib.Data.Nat.Bitwise
import Mathlib

-- A number whose every set bit is a set bit of 2^m is 0 or 2^m.
-- IsSubmask j d := ∀ b, j.testBit b → d.testBit b

#check Nat.testBit_two_pow
#check Nat.testBit
#check Nat.testBit_eq_false_of_lt
#check Nat.testBit_lt  -- ?
#check Nat.eq_of_testBit_eq  -- ?
#check Nat.testBit_pos -- ?

-- 2^m has only bit m set
example (m b : Nat) : (2 ^ m).testBit b = decide (b = m) := by
  exact Nat.testBit_two_pow

-- if j is a submask of 2^m then j = 0 or j = 2^m
example (m j : Nat) (h : ∀ b, j.testBit b → (2 ^ m).testBit b) :
    j = 0 ∨ j = 2 ^ m := by
  by_cases hm : j.testBit m
  · -- j has bit m; show no other bits and j = 2^m
    right
    -- need: j ≤ 2^m and 2^m ≤ j
    have hle : j ≤ 2 ^ m := by
      -- all bits of j are subset of bits of (2^m) which are {m}
      apply Nat.lt_of_testBit
      · exact hm
      · -- j does not have bits > m
        intro bb hbgt hmbb
        -- (2^m).testBit bb = false since bb ≠ m
        have : (2 ^ m).testBit bb = false := by
          rw [Nat.testBit_two_pow]
          simp [hbgt.ne']
        have : j.testBit bb = false := not_of... -- from h? h gives j.testBit bb → (2^m).testBit bb
        exact (this ▸ hmbb) -- hmbb : j.testBit bb = true, contradiction
    -- hmm need 2^m ≤ j too
    sorry
  · -- j has no bit m
    sorry

-- Function.iterate decomposition
#check Function.iterate_add
#check Function.iterate_mul
#check Function.iterate_succ
#check Function.iterate_zero
#check Function.iterate_comp
