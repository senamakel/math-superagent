# Attempt 2 result: four-passage ECT obstruction

## Status
Verified-computationally for explicitly stated toy functions; not a counterexample to the actual I^1_6b dynamics.

## Exact result
Individual ECT pairs need not remain ECT after addition. The exact toy pairs are A=(1,x), B=(-1,-x): each has Wronskian 1, while A+B=(0,0) has zero Wronskian. A separate exact iterated-log toy gave W3=0. A vanishing leading slow-divergence coefficient likewise removes first-order displacement control; higher-order terms must be analyzed.

## Mathematical consequence
The adopted route cannot assert that four second-type Dulac passages form a common ECT family merely because individual passages do. It needs a common finite-dimensional basis, Wronskian/nondegeneracy certificates on every parameter stratum, higher-order treatment when slow divergence vanishes, and uniform remainder estimates. Scholar audit confirms Huzak 2018 is graphic-specific to DF_2a and GMV concerns first-order Abelian integrals; neither source supplies these hypotheses for I^1_6b.

## Evidence
Programs: code/refute/i6b_ect_diagnostic.py, existing code/i6b_second_type_toy.py and code/i6b_four_passage_oracle.py. Capture: code/out/i6b_ect_diagnostic.captured.txt. Lean partial theorem: code/lean/Lib/SlowDivergenceECTBound.lean, compiled verified with no sorry and axioms propext, Classical.choice, Quot.sound; it proves only the abstract ECT zero bound conditional on explicit ECT hypotheses.
