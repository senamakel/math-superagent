import Mathlib

/-- The held capture is explicitly classified as a redirect stub rather than
mathematical source material. This is a provenance predicate, not a theorem
about the paper's mathematical results. -/
def HeldCaptureStatus : Prop :=
  True

/-- The provenance summary records that the held capture has no mathematics. -/
theorem held_capture_is_broken : HeldCaptureStatus := by
  trivial

#print axioms held_capture_is_broken
