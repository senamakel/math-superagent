# Refutation report: universal-Euclidean wiring

## Scope and theory

I attacked the reduction using the finite-difference telescoping identity
`digit_j = floor(x+(j+1)a)-floor(x+j a)` and the universal-Euclidean moment convention
`sum_{i=0}^{n-1} z^i floor((p i+q)/r)^h`. The oracle is deliberately small;
its purpose is to expose indexing and boundary errors, not to solve the target.

## Executed checks

`code/refute/check_reduction_indexing.py` was run in the workspace's recorded
acceptance run. It checks `k=1..20`, all exact mechanical values, and an exhaustive
small grid for the `ue0` transformation (`p<30`, `r<31`, `q<r`, `n<=20`, `z=10`).
Recorded result: correct indexing passed; shifted-floor and shifted-power variants
produced expected counterchecks; `ue0 failures: 0`.

The primitive's independent recorded run reports 30/30 random S0/S1/S2 tests,
30/30 floor-sum tests, 6/6 deterministic tests, and 30/30 `ue0` tests, including
`n=0` and `n=1` boundaries. This supports the primitive, but does not prove the
reduction from all intercepts to one call.

I added `code/refute/check_approximant_stability.py`, an exact checker comparing
rational slopes `F_n/F_{n+2}` for k<=50 against the existing mechanical oracle,
plus low-denominator duplicate-orbit boundaries. It was written but no fresh
process execution tool was available in this role; therefore I claim no output
from that new file.

## Smallest attempted failure modes

- `k=1`: the decimal exponent must be `10^(k-1-j)`. A shifted exponent changes
  the one-digit factor immediately, so that variant is refuted at k=1.
- `n=0`: identity moments must be zero; `n=1` must have weight `z^0=1`. The
  recorded exhaustive primitive checks pass both.
- Negative-intercept/0-index shift: the `ue0` lift was checked exhaustively and
  has no failure in the stated grid.
- Duplicate orbit points: a denominator q not exceeding k is not a valid
  irrational/convergent approximant regime; it can produce repeated points and
  cannot justify k+1 distinct arcs. This is a boundary condition the final
  evaluator must enforce.

## Verdict

**undecided, with a serious uncovered gap rather than a refutation.** No checked
counterexample was found to the primitive or to the tested small indexing. The
proposed *full* evaluator is not established: the workspace explicitly records
that the k+1-intercept aggregation has not been reduced to a single O(log)
`ueuclid` call. Consequently approximant stability at `k=10^18` and the final
residue remain unverified. A larger run would settle whether the actual completed
reduction reproduces the two corrected anchors (`34432237`, `20938836`); merely
increasing the small oracle would settle nothing new.
