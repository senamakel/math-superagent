import Mathlib.Data.ZMod.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement

import Shuffle

/-!
The central reduction for Project Euler 622:

  For an even deck of size `n >= 4`, the number of out-faro shuffles needed to
  restore the deck is the multiplicative order of `2` modulo `n-1`:

       s(n) = orderOf (2 : (ZMod (n-1))ˣ).

Reason: on the `n-1` movable positions (bijecting with `ZMod (n-1)`), one
shuffle acts as multiplication by `2`.  After `k` shuffles a card has moved by
`2^k * x`; it is back in place for every card iff `2^k ≡ 1 mod (n-1)`, i.e.
iff `k` is a multiple of the multiplicative order of `2` mod `n-1`.  The least
such `k` is therefore that order.

Sourced to Diaconis–Graham–Kantor (perfect shuffles), Packard, and OEIS
A002326.
-/

namespace OutShuffle

/-- For an even deck of size `n >= 4`, `s(n)` (the minimal number of out-faro
shuffles to restore the deck) equals the multiplicative order of `2` modulo
`n-1`. -/
theorem s_eq_orderOf
    (n : ℕ) (hn_even : Even n) (hn4 : 4 ≤ n)
    (hpos : 0 < n - 1) (h : Nat.Coprime 2 (n - 1)) :
    s n hpos h = orderOf (ZMod.unitOfCoprime 2 h) := by
  sorry

end OutShuffle
