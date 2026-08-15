# The averaging obstruction, computed exactly for n <= 8

## What was run

The Delsarte/Krawtchouk LP (correctly posed) that minimises the average
internal degree `a_1` over all feasible distance distributions of a set
`S ⊆ {0,1}^n` of size `M = 2^{n-1}+1`, and the Clifford "parity-plus-one"
structure check on the exact n=4 witness.

Backing programs: `ground_approaches.py` (initial, had the LP missing the
`Σ a_i = M` constraint — degenerate, refixed) and `delsarte_lp_correct.py`
(the correct LP, exact rational coefficients).

## Claim: the LP value

```claim
id: averaging-lp-decays-to-zero
statement: The best lower bound on f(n) obtainable from the average internal
  degree — i.e. min feasible a_1 over the Delsarte polytope of H(2,n) with
  |S| = 2^{n-1}+1 — equals 1,1,3/4,1/2,5/16,3/16,7/64,1/16 for n=1..8, which
  decays to 0 exponentially (each step ~ ×1/2). Because avg-deg(S) <= D(S),
  this LP value is a valid lower bound on f(n); it is the best one the
  averaging route can give.
hypotheses: feasibility condition sum_i a_i K_j(i) >= 0 (Delsarte) with
  K_j the Krawtchouk polynomials; a_i = n_i/M for the distance distribution.
holds-here: yes (this is a lower bound on f(n), valid for all S)
status: verified numerically (HiGHS LP), and independently: the parity-class
  + one vertex construction has avg internal degree ~ n/2^{n-1} -> 0, showing
  the LP value is essentially tight (real sets attain ~0 average degree).
falsifies: any claimed proof that a sharperning of an edge-counting/averaging
  argument reaches sqrt(n) or even log n. This LP is exactly the closure of
  that family, and it gives ~0.
```

## Why this settles the key structural obstruction

problem.md's central obstruction is:

> A method that bounds an average will not reach sqrt(n).

This computation makes that precise and actually stronger than stated. The
closure of all average/edge-counting methods — the Delsarte LP minimising
`a_1` — gives a lower bound on `f(n)` of

```
1, 1, 0.75, 0.5, 0.3125, 0.1875, 0.109375, 0.0625   (n = 1..8)
```

which is exponential decay to zero, not logarithmic. So the average route
does not even reach `log n`; it gives essentially nothing. It follows that
the known `Ω(log n)` (and the spectral `Ω(√n)` proved in this workspace)
MUST come from a non-averaging mechanism — confirming that any approach
with a real chance must produce the maximum directly (or an extremal
quantity that is a maximum by construction).

## Independent check (Clifford claim refuted)

The inventor's "extremal set = parity class + one vertex" conjecture is
FALSE for the exact n=4 witness `S = [0,1,2,5,6,11,12,13,14]`: it is not
any parity class plus one vertex (`witness is parity-plus-one? False`).
So the extremal structure is not that simple.

## Validity audit

- The LP is exact-rational (Fraction coefficients) fed to HiGHS; the values
  shown are floats of exact rational solutions.
- LP min a_1 <= a_1(S) for every admissible S (the distance distribution of
  any S is a feasible point), and a_1(S) = average internal degree of S
  <= D(S). Hence LP value is a genuine lower bound on f(n). It is not an
  upper bound and makes no claim about achievability of the LP value.
- The decay to 0 matches the explicit construction (even-weight set + one
  vertex, avg degree ~ n/2^{n-1}), so the LP value is essentially tight as a
  bound on average degree.
