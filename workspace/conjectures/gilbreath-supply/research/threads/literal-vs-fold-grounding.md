# Literal vs fold: resolving the grounding defect with a third path

Operator directive 4. The literal geometric definition of ν₂ (maximal {0,2}
suffix of the right diagonal) reads identically 0 through the run's literal
helper, while the imported linearisation ν₂ = wt(Φ_n h) gives nonzero values
matching the measured object. This is not a convention difference: the literal
object is the definition, and the fold is an imported theorem about it. This
thread carries the resolution.

```thread
id: literal-vs-fold-grounding
question: Does the literal definition of ν₂ — the maximal {0,2} suffix of the
  right diagonal δ_k(n) = A_k(n−1−k) — match the fold wt(Φ_n h), or is the
  imported linearisation false? The run's literal helper returns 0 for every
  n in 3..60 while the fold gives 7 at n=10 and 1976 at n=4000.
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: linearisation (ν₂(n) = wt(Φ_n h), imported from problem.md fact 1)
blocked-by:
next: none — the defect was in problem.md's definition, not in the code. The
  bottom cell A_{n−1}(0) is always 1, so an unfloored bottom-end reading is
  identically 0 for every n ≥ 2 and the problem is vacuous. problem.md now
  states the operative range k∈[2,n−1] explicitly and records the unfloored
  reading as vacuous, with oracle_validation_report.md and avg_supply_note.md
  as anchors. literal_suffix_nu2 is kept as the labelled negative control.
```

## Resolution (directive 6)

Directive 4's hypothesis was wrong: `literal_suffix_nu2` is not buggy. The
unfloored reading was the vacuous one, so no third path was needed. The
operative definition is the floored range `k ∈ [2, n−1]`; the fold
`wt(Φ_n h)` is a theorem about that floored object, and the measured values
refer to it. Nothing about the linearisation is in question.

## Why this is not a convention difference

problem.md defines ν₂ as the literal object; wt(Φ_n h) is imported fact 1, a
theorem about it. An identically-zero literal column is either a bug in the
literal helper or a falsification of fact 1. Demoting the literal object to a
"degenerate negative control" assumes fact 1 is fine and hides the bug. A
capture with an identically-zero column must not read as a pass.

## Notes for whoever resolves it

- The canonical `lib.rightdiag.cycle_and_nu2` that problem.md cites does not
  exist on disk; `lib.nu2.literal_suffix_nu2` was written fresh and is the
  suspect helper.
- `code/direct_triangle.py` already builds the triangle and reads the diagonal,
  but verify its suffix-floor reading against problem.md's definition before
  trusting it as the third path — pin the correct reading first, do not assume.
- Print all three columns (literal | direct | fold) for n=3..60, include a
  negative control that should fail, and state the range checked.
