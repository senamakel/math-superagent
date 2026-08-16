/-- The perfect out-shuffle on `n` cards, viewed on 0-based positions from the top:
card at original position `i` moves to position `2*i` if it was in the top half,
and to `2*(i - n/2) + 1` if it was in the bottom half. -/
def outShuffle (n i : ℕ) : ℕ :=
  if i < n / 2 then 2 * i else 2 * (i - n / 2) + 1

/-- Applying the perfect out-shuffle `s` times to position `i` in an `n`-card deck. -/
def outShufflePow (n s i : ℕ) : ℕ :=
  match s with
  | 0 => i
  | s' + 1 => outShuffle n (outShufflePow n s' i)

/-- For an even deck of `n ≥ 4` cards, `s` perfect out-shuffles restore the original
order iff `n - 1` divides `2^s - 1`. -/
theorem outShuffle_order_iff (n s : ℕ) (hn_even : ∃ m, n = 2 * m) (hn_ge : 4 ≤ n) :
    (∀ i, i < n → outShufflePow n s i = i) ↔ (n - 1) ∣ (2 ^ s - 1) := by
  sorry
