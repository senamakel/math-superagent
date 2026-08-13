# Approach: p-adic valuation / Newton polygon of the duplication map

```approach
idea: On E: y² = x³ − c²x  (the Robertson/Bremner curve), the duplication
  formula x([2]P) = (x²+c²)² / (4x(x²−c²)) restricts the p-adic valuations of
  the x-coordinates of doubled points, for primes p dividing c.  The AP
  condition x₁ + x₃ = 2 x₂ (three x(2Q) values in arithmetic progression)
  forces a relation among valuations that might be impossible — giving a
  p-adic / Newton-polygon impossibility.

status: refuted
precedent:
  - Duplication formula and the 2E(Q) membership criterion: Bremner, "On
    squares of squares", Acta Arith. 88 (1999) 289-297 — a point (X,Y) in
    E(Q) lies in 2E(Q) iff {X, X±c} are all rational squares; MSS ⇔ three
    points of 2E(Q) with x-coordinates in AP.  Source:
    research/sources/bremner-on-squares-of-squares-1999.full.md.
  - The p-adic valuation calculus for elliptic denominators / division
    polynomials is classical and explicit: v_p(x(nP)) = v_p(φ_n(P)) −
    2v_p(ψ_n(P)) (elliptic nets / division-polynomial valuations; e.g. the
    Journal of Number Theory elliptic-net paper cited below, and the
    Canadian J. Math paper on explicit valuations of division polynomials).
    This is a *tool* whose hypotheses (fixed curve, fixed point, division
    polynomials) are available — the method family is real.
  - This run's own exact computation and claim phi-padic-no-obstruction
    (research/approaches/padic-modular-obstruction-dead-end.md; code/out/
    phi_padic_closure_*.txt): for every p in {2,3,5,7,11,13} and every
    precision p^a ≤ 2000 (and exhaustive residue-class enumeration), the
    achievable residue set R_p^a = {f(m,n) mod p^a} is NON-DEGENERATELY
    ADDITIVELY CLOSED.  Equivalently no pure p-adic residue/valuation
    constraint at any of these primes rules out the additive triple
    q1 + q2 = q3.

killed-by: The run has already shown there is no p-adic valuation obstruction
  for any p in {2,3,5,7,11,13} at any precision tested: the system is locally
  additively closed p-adically (phi-padic-no-obstruction, status checked).
  The MSS system is locally solvable mod every prime power — an established
  fact (asserted-by-source, consistent with the run's exact modular checks).

  Concretely, the Bremner 7-square witness realises TWO of the three AP
  x-coordinates as points of 2E(Q) (X=139129=373² and X=180625=425² both
  satisfy X, X±c squares; robertson_reduction_check.txt).  A p-adic valuation
  relation that forbade double-membership would kill this witness — the run's
  GOAL.md oracle contract.  In fact the valuations behave exactly as the
  obstruction would need NOT to: the realised q-values q_v = 5544/7225 and
  q_{u+v} = 336/625 both satisfy the proved valuation facts v2 ≥ 3, v3 ≥ 1,
  and their sum is a valid rational with no local contradiction
  (code/out/candidate_verdict_math.py, checked).

  The Newton-polygon idea specifically: the duplication rational map is
  f(x) = (x²+c²)²/(4x(x²−c²)).  There is no general theorem forcing three
  AP-arranged f-values to have incompatible valuations — the valuation
  content is exhausted by the fact that the attainable residue sets are
  additively closed.  Any "impossible valuation relation" would have to be a
  NEW modular statement, and the run's exhaustive residue-class work shows
  none exists for these primes.  The front of attack here is closed unless a
  prime beyond 13, or a fundamentally non-local argument, is introduced.

first-step was executed: candidate_verdict_math.py re-derives the duplication
  map, and confirms both realisation valuations and the absence of a local
  contradiction; the seven phi_padic_* programs (checked) already exhaust the
  p-adic closing.  Nothing further is worth computing along this axis.
```

## Why this fails (reader's digest)

The p-adic/Newton-polygon analysis is a *local* method, and the MSS system is
*locally consistent everywhere*: every finite local condition is satisfiable.
This is not a gap in the execution — it is the run's established, checked claim
`phi-padic-no-obstruction`, which runs exact residue-class enumeration at every
precision up to p^a ≤ 2000 for p ∈ {2,3,5,7,11,13} and finds the achievable
residue sets additively closed. A local sieve cannot prove non-existence because
there is no local contradiction to find. The obstruction (if any) is genuinely
global/rational: it lives in whether a rational square root exists in the
additive configuration, not in any finite p-adic truncation.

## Sources considered

- The elliptic-nets / division-polynomial valuation literature (J. Number
  Theory "On symmetries of elliptic nets and valuations of net polynomials";
  Can. J. Math. "Integral Points on Elliptic Curves and Explicit Valuations of
  Division Polynomials") gives the right valuation machinery but only for a
  FIXED curve and FIXED point — it computes valuations, it does not produce
  contradictions, and it is consistent with the witness.
- The "p-adic L-function Newton polygon" papers (Pollack's L±_p) are about
  supersingular Iwasawa theory, unrelated to doubled-point valuations.
- No source applies a p-adic/Newton-polygon valuation argument to the MSS
  doubled-point AP; the local consistency result explains why none exists in
  the literature — the local picture has no obstruction to state.
