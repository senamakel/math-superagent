import Mathlib.Data.ZMod.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.GroupTheory.Perm.Basic

/-!
The out-faro (perfect riffle) shuffle of an even deck of size `n`.

Setup: an even deck of size `n` has positions `0 .. n-1`.  The top card
(position 0) and bottom card (position n-1) are fixed by the shuffle.  The
interior spread is a perfect interleave that sends a card in the top half and
the matching card in the bottom half alternately, which on the `n-1` movable
positions `0 .. n-2` acts as:

    position x  ↦  2 x mod (n-1).

Viewing those `n-1` movable positions as `ZMod (n-1)`, one shuffle is
multiplication by `2` inside `ZMod (n-1)`.  So the shuffle is a bijection
precisely when `2` is invertible mod `n-1`, i.e. `Nat.Coprime 2 (n-1)`
(which always holds for even `n`, because then `n-1` is odd).
-/

namespace OutShuffle

/-- The out-faro shuffle on the `n-1` movable positions, seen as a permutation
of `ZMod (n-1)`: card at `x` moves to `2 * x`.  Requires `0 < n-1` (so
`ZMod (n-1)` is a ring) and `2` coprime to `n-1` (so multiplication by `2` is
a bijection). -/
def outShuffle (n : ℕ) (hpos : 0 < n - 1) (h : Nat.Coprime 2 (n - 1)) :
    Equiv.Perm (ZMod (n - 1)) := by
  haveI : NeZero (n - 1) := ⟨Nat.ne_of_gt hpos⟩
  let u : (ZMod (n - 1))ˣ := ZMod.unitOfCoprime 2 h
  exact u.mulLeft

/-- The minimal number of out-faro shuffles needed to restore an even deck of
size `n`.  This is the order of the shuffle permutation on the movable
positions. -/
noncomputable def s (n : ℕ) (hpos : 0 < n - 1)
    (h : Nat.Coprime 2 (n - 1)) : ℕ :=
  orderOf (outShuffle n hpos h)

#print axioms outShuffle
#print axioms s

end OutShuffle
