# Scholar: the Delsarte-gate contradiction is resolved — the source refutes the gate

Reading of the primary source, done this pass. Replaces the contradictory
`krawtchouk-delsarte-linear-code-holds-here` gate with the exact statement.

## What the gate claimed, and why it is wrong

The librarian's gate note (`librarian_krawtchouk_macwilliams_engine.md`) and its
claim `krawtchouk-delsarte-linear-code-holds-here` asserted:

> The Delsarte LP bound that turns the distance distribution into F_n(z) = O(n)
> needs Ĉ_n(ω) ≥ 0, which holds only for linear codes.

That conflates two distinct objects and gets the Delsarte one backwards:

1. **MacWilliams identity** — genuinely needs linearity: it relates W(C) to
   W(C^⊥) where C^⊥ is the *orthogonal complement*, which exists only for a
   linear code. Both MacWilliams 1963 and Guruswami state it that way. The
   identity itself is a distributional transform, not a bound per input.
2. **Delsarte LP bound** — the discrete bound on code sizes A(n,d) — is proved
   in Guruswami's notes for **general codes**. The constraint is
   `Σ_i A_i K_ℓ(i) ≥ 0`, and for general C it is proved (lines 519–590 of the
   full text) by a **sum of squares**:
   `Σ_i A_i^C K_ℓ(i) = (1/|C|) Σ_{wt(z)=ℓ} (Σ_{x∈C} (−1)^{x·z})² ≥ 0`,
   with `A_i^C = #{(x,y)∈C²: Δ(x,y)=i}/|C|` the *distance* distribution (inner
   distribution), defined for any subset C. No linearity appears. The LP bound
   is exactly the Delsarte theorem for arbitrary (not necessarily linear)
   codes.

So the *non-negativity* the adopted approach's condition (C) needs is the
**distance**-distribution transform `Σ_i A_i K_ℓ(i) ≥ 0`, which holds for ANY
row set — XOR-closed or not. The Krawtchouk diagonalization identity is
likewise a cube-Fourier identity valid for any multiset (verified exact in the
capture, n=4..7, several z). **The linearity of the fold's row set is a
non-obstacle for the Delsarte LP.** The only genuinely linearity-dependent
statement in the engine is the MacWilliams *identity* between a code and its
dual — and the approach never uses that identity; it uses the distance
distribution and its Krawtchouk diagonalization.

## What the gate should have been, and the real gate it exposes

The claim's real question — "does the fold's row-set distance distribution
grow slowly enough?" — is not a linearity question at all. It is the
**computed** question the capture already answers:

- `A_2 = O(n^{0.48})` (log-log exponent 0.480 over n=16..4096), NOT Θ(n²).
  The `z²n²` term that would have sunk condition (C) is absent.
- `F_n(1−2p) = O(n)` with `F_n/n → ~1.0` (exact Fractions, p up to 0.585;
  holds for every fixed |z| < ~0.86, failing only near the diagonal z=1
  where F_n(1) = (n−2)² is the diagonal-only term).
- All Krawtchouk identities exact (pairwise XOR moment, E[S²]=F_n(z),
  diagonalization), n=4..7, several z.

So the true gate — how far the *row code's distance distribution* constrains
F_n(z) — is **closed by computation** (measured-not-proved, exact over n≤4096),
not blocked by a linearity condition. What remains genuinely open is the
*arithmetic heart* (A): is `E[S(n)²] = O(n)` provable for the real prime h
(second-moment / submask-window autocorrelation bound, GOAL priority 2)?

## What this change does not do

It does NOT close request `walsh-spectral-subset-b904`. The Delsarte LP bounds
*A(n,d)* (max code size), which is not the per-input `wt(Φ_n h) ≥ c·n` the
request asks for. Condition (C) is a *second-moment* statement (the fold does
not amplify correlations); the remaining step to SUPPLY is (A), the arithmetic
input. The Krawtchouk machinery remains the *coordinate system*, not the
proof of the primes' second moment.

## Claim block

```claim
id: delsarte-lp-holds-for-nonlinear-row-sets
statement: >
  The Delsarte LP bound does NOT require the code C to be linear: for any subset
  C ⊆ F₂ⁿ with distance distribution A_i^C = #{(x,y)∈C²: Δ(x,y)=i}/|C| (WLOG
  0 ∈ C), the constraint Σ_i A_i^C K_ℓ(i) = (1/|C|) Σ_{wt(z)=ℓ} (Σ_{x∈C}(−1)^{x·z})²
  ≥ 0 holds by sum-of-squares, so A_i^C is a feasible solution of the Delsarte
  LP. The MacWilliams IDENTITY (W(C^⊥) = transform of W(C)) does need linearity,
  but the approach's condition (C) uses only the distance distribution and its
  Krawtchouk diagonalization, not the dual-code identity. Hence the fold's row
  set R_n need NOT be XOR-closed for the Krawtchouk/Delsarte engine to apply.
hypotheses: C ⊆ {0,1}^n arbitrary (nonempty, WLOG 0∈C); Krawtchouk polynomials K_ℓ; Hamming metric.
holds-here: yes — the fold row set R_n = {1_{M_d} : d∈[2,n−1]} is an arbitrary
  subset of F₂^n; the Delsarte constraints apply regardless of XOR-closure.
status: proved (Guruswami CMU Notes 5.1, §3 "general codes" proof, full text
  lines 519–590: the constraints are verified by a sum of squares with no
  linearity step)
bearing: Resolves the librarian's gate (the row set's linearity is a non-obstacle
  for the Delsarte LP). The distance-distribution growth A_2 = O(n^{0.48}) and
  F_n(1−2p)=O(n) (fold_second_moment_capture.txt, exact over n≤4096) close the
  geometry side of condition (C); the remaining open step is the arithmetic
  second moment (A), E[S(n)²]=O(n) for the real prime h.
anchor: research/sources/guruswami_macwilliams_lp_notes_fulltext.full.md, lines 519–590
contradicts: krawtchouk-delsarte-linear-code-holds-here (superseded: that claim
  asserted the Delsarte bound needs linearity, which the primary source refutes)
answers: (none — request walsh-spectral-subset-b904 stays open; the LP bounds
  code sizes, not per-input fold weight)
```

## Statement of what is correct and what is not

- **Correct and retained:** the Krawtchouk diagonalization identity is a pure
  cube-Fourier identity valid for any multiset (`krawtchouk-polynomials-encyclopedic`,
  `guruswami-macwilliams-lp-from-fourier`); the MacWilliams identity needs a
  linear code (`macwilliams-weight-distribution-theorem`); the fold row set is
  not assumed linear anywhere in the second-moment approach.
- **Retracted:** the assertion that the Delsarte *bound* additionally needs
  Ĉ(ω)≥0 / linearity. It does not; the Delsarte constraints hold for arbitrary
  codes, and the Krawtchouk diagonalization needs no nonnegativity at all (it
  is an identity, exact for any multiset).
- **The captured computation remains the gate:** A_2 = O(n^{0.48}) and
  F_n(z) = O(n) are the real content of condition (C). They are measured over
  n ≤ 4096 (exact), i.e. `measured-not-proved` for all n; the exponent fit is
  a float ratio, the verdict A_2=O(n) rests on the monotone decay of A_2/n².