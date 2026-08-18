claim:
  id: g4-additive-summary-collision-refuted
  status: checked
  statement: The additive block summary proposed as the smallest concrete route toward G4 can be used as a sufficient state for extensions.
  counterexample: Blocks 010 and 101 are assigned the same summary, while their extensions by 0 are distinct. In the finite two-element model returned for code/refute/g4_joint_intercept.p, summary(block010)=summary(block101), but extend(block010,0) != extend(block101,0).
  check: The model satisfies binary digit distinctness, the summary collision axiom, and the extension-difference axiom; it falsifies the conjecture that the summaries differ.
  search-frame: finite first-order model with a two-element domain; this is the k=2 additive-summary collision, not a counterexample to every conceivable fixed-dimensional G4 state.
