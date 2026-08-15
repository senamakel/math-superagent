import Mathlib

-- probe 2 : digit sums, popcount
#check Nat.digits
#check Nat.digits_len
#check Nat.s_digits
#check Nat.digit
#check Nat.ofDigits
#check Nat.bit
#check Nat.testBit
#check Nat.shiftRight
#check Nat.land
#check Nat.lor
#check Nat.lxor
#check Nat.two_mul
#check Nat.ofBits
#check Nat.ofBits_lt
#check Nat.setBit
#check Nat.add_testBit
#check Nat.eq_zero_of_testBit_eq_false
#check Nat.testBit_eq_false
#check Nat.testBit_two_pow

-- does Mathlib state the "subset" characterization j <= d <-> j testBit <= d testBit?
#check Nat.lt_of_testBit
#check Nat.testBit_le_testBit
#check Nat.le_testBit_iff  -- ?

-- freshmen dream in char p ?
#check pow_ringChar
#check CharP.cast_eq_zero
#check sub_eq_zero
#check add_pow_charP
#check add_pow_eq_add_pow
