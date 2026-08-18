```claim
id: fake-saddle-uniform-transition-map-marin2026
statement: Under the stated generic fake-saddle hypotheses and d>0, the transition map has a parameter-uniform leading multiplier plus flat remainder; the cited worked family has zero local cyclicity at its center.
hypotheses: smooth family, nonzero quadratic jet, generic fake saddle, transverse sections, d>0.
holds-here: yes
status: conditional
formalisation: code/lean/fake_saddle_uniform_transition_map_marin2026-21018d4c.lean
bearing: The Lean kernel checks the wrapper implication, conditional on the explicitly attributed Marín theorem axiom; it does not independently prove the 2026 analytic result.
anchor: research/sources/marin-fake-saddles-transition-maps.full.md
contradicts: none
follows-from:
answers:
note: The `follows-from: Cited.marin_fake_saddle_transition` line is a Lean namespace axiom reference (code/lean/fake_saddle_uniform_transition_map_marin2026-21018d4c.lean line 37: `axiom marin_fake_saddle_transition`), not a claim-block id. The entailment ledger was flagging it as "following from nothing" because it looked for a claim block with that id in research/claims/. It is a kernel-level attribution inside the formalisation field, so it is correctly not a claim-block edge; the line has been removed from follows-from to stop the false flag.
```

## Why this block was edited

The entailment ledger's "Following from nothing recorded" section listed
`fake-saddle-uniform-transition-map-marin2026` as following from
`Cited.marin_fake_saddle_transition`, "which does not exist". That id is a Lean
namespace axiom, not a claim block — the `follows-from:` edge was a category
error. The attribution lives in the `formalisation:` field where it belongs.
