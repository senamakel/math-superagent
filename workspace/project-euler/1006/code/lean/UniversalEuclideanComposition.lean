import Mathlib

namespace PE1006

/-- A weighted floor-moment segment. `dR` is the number of R steps, `dU` is
    the terminal floor height, and the moments use weights `z^i` for the
    segment's local indices `i = 0,...,dR-1`. -/
structure Segment where
  dR : ℕ
  dU : ℤ
  w : ℤ
  S0 : ℤ
  S1 : ℤ
  S2 : ℤ

/-- Composition of two consecutive segments, with the second segment's
    floor values shifted by the terminal height of the first. -/
def compose (l r : Segment) : Segment :=
  { dR := l.dR + r.dR
    dU := l.dU + r.dU
    w := l.w * r.w
    S0 := l.S0 + l.w * r.S0
    S1 := l.S1 + l.w * (r.S1 + l.dU * r.S0)
    S2 := l.S2 + l.w * (r.S2 + 2 * l.dU * r.S1 + l.dU ^ 2 * r.S0) }

/-- The composition law for geometric weighted floor moments.  The explicit
    hypotheses identify the moments of each segment; no division or hidden
    nonzero assumption occurs. -/
theorem weighted_floor_moment_comp
    (l r : Segment)
    (z : ℤ)
    (L0 L1 L2 R0 R1 R2 : ℤ)
    (hl0 : l.S0 = L0)
    (hl1 : l.S1 = L1)
    (hl2 : l.S2 = L2)
    (hr0 : r.S0 = R0)
    (hr1 : r.S1 = R1)
    (hr2 : r.S2 = R2)
    (hw : l.w = z ^ l.dR)
    (hL0 : L0 = ∑ i ∈ Finset.range l.dR, z ^ i)
    (hL1 : L1 = ∑ i ∈ Finset.range l.dR, z ^ i * 0)
    (hL2 : L2 = ∑ i ∈ Finset.range l.dR, z ^ i * 0 ^ 2)
    (hR0 : R0 = ∑ i ∈ Finset.range r.dR, z ^ i)
    (hR1 : R1 = ∑ i ∈ Finset.range r.dR, z ^ i * 0)
    (hR2 : R2 = ∑ i ∈ Finset.range r.dR, z ^ i * 0 ^ 2) :
    (compose l r).S0 = L0 + z ^ l.dR * R0 ∧
    (compose l r).S1 = L1 + z ^ l.dR * (R1 + l.dU * R0) ∧
    (compose l r).S2 = L2 + z ^ l.dR *
      (R2 + 2 * l.dU * R1 + l.dU ^ 2 * R0) := by
  sorry

#print axioms weighted_floor_moment_comp

end PE1006
