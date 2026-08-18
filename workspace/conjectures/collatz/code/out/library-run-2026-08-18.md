# Computation record — 2026-08-18

The existing naive oracle `code/collatz_oracle.py` was inspected as the required small-instance checker. It declares `complexity_class = "exponential"` and `oracle_bound = 10000`, so it is not used as a full-size method. It reproduces the hand examples 1, 2, 3, and 6 and checks 1..10000.

No larger run was made: a larger run would only extend a verified finite frontier and would not settle the open conjecture without a new structural reduction. The next computational task should test the precise parity-word identity in `code/lean/Lib/AcceleratedCycleIdentity.lean` against the naive oracle, rather than merely increasing the bound.

Attack condition: the blueprint could be wrong if the parity hypotheses do not actually imply the claimed affine formula, especially at empty words, zero, or the accelerated odd-step convention. Those boundary cases remain to be tested before promoting it.
