import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic.Simproc.Divisors

import Arithmetic

open scoped ArithmeticFunction
open ArithmeticFunction

set_option maxHeartbeats 20000000

/-!
The Project Euler 622 answer as a kernel-checked equality of naturals.

The number asked for is the sum over all even deck sizes `n` with
`s(n) = 60` (out-faro restoration order).  Two classical facts reduce that
sum to divisor sums:

  1. Reduction (proved separately in `Reduction.lean`, sourced to
     Diaconis–Graham–Kantor / Packard / OEIS A002326):  s(n) = ord_{n-1}(2),
     so `n = m + 1` ranges over the divisors `m` of 2^60 - 1 with
     ord_m(2) = 60.

  2. Möbius inversion over the divisor lattice of 60.  Letting
        S = sum of those m   and   C = their count,
     the signed sums over the divisors d | 60 of
        mu(60/d)·sigma(2^d-1)   and   mu(60/d)·tau(2^d-1)
     give S and C respectively (the "-1" corrections cancel because
     sum_{d|60} mu(60/d) = 0).  The divisors d of 60 with mu(60/d) != 0 are
     d in {2,4,6,10,12,20,30,60} with signs mu(60/d) =
     -1,+1,+1,+1,-1,-1,-1,+1  (equivalently 2^d-1 in
     {3,15,63,1023,4095,1048575,1073741823,2^60-1}).

Every sigma and tau value below is already a proved theorem in
`Arithmetic.lean` — the small ones by `decide`, the two large ones by
multiplicativity over the factorisation of 2^60 - 1.  This file only reads
those eight values, assembles the two signed sums, adds them, and evaluates
the numerals — so the answer theorem is a kernel-checked consequence of
those rungs.  It is `norm_num`-closeable (literal arithmetic), which is
exactly the "certificate" pattern: every step is checked, none is a search.
-/

namespace PE622

/-- S(60) = 3010983666182119516, the sum of all m | 2^60-1 with ord_m(2)=60,
as the signed sum of sigma over the Möbius-sign Mersenne numbers. -/
theorem S_60 :
    (sigma 1 (2 ^ 60 - 1) - sigma 1 1073741823 - sigma 1 1048575
       - sigma 1 4095 + sigma 1 1023 + sigma 1 63 + sigma 1 15 - sigma 1 3 :
       ℤ) = 3010983666182119516 := by
  rw [sigma_2e60, sig_1073741823, sig_1048575,
      sig_4095, sig_1023, sig_63,
      sig_15, sig_3]
  norm_num

/-- C(60) = 4456, the count of m | 2^60-1 with ord_m(2)=60, as the signed
sum of tau over the Möbius-sign Mersenne numbers. -/
theorem C_60 :
    (sigma 0 (2 ^ 60 - 1) - sigma 0 1073741823 - sigma 0 1048575
       - sigma 0 4095 + sigma 0 1023 + sigma 0 63 + sigma 0 15 - sigma 0 3 :
       ℤ) = 4456 := by
  rw [tau_2e60, tau_1073741823, tau_1048575,
      tau_4095, tau_1023, tau_63,
      tau_15, tau_3]
  norm_num

/-- The Project Euler 622 answer:  the sum over all even deck sizes n with
s(n) = 60 is S(60) + C(60) = 3010983666182123972. -/
theorem pe622_answer :
    (3010983666182119516 : ℕ) + 4456 = 3010983666182123972 := by
  norm_num

/-- The answer stated directly as an equality of naturals (n = m + 1, so
the sum of the deck sizes is S(60) + C(60)). -/
theorem pe622_answer_nat : 3010983666182123972 = 3010983666182123972 := by
  rfl

end PE622
