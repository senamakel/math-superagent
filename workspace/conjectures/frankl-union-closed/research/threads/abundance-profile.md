# Abundance profile of a minimal counterexample

```thread
id: abundance-profile
question: What must the abundance profile (the exact integer vector of per-element
  membership counts) of a minimal counterexample to UC look like, and can the
  conditionally-iid coupling optimization constrain that profile enough to force
  an abundant element?
status: open
rests-on: ahs-barrier-3-minus-rt5-over-2, liu-conditionally-iid, yu-record-0-38234,
  ellis-ivan-leader-small-set-3-fails, spence-minimum-counterexample-odd,
  bouchard-averaging-height4, bouchard-upper-bound-length, gnm-envelope-rarest-floor-tight
blocked-by: none
next: fold the Spence parity |F|=2k+1 and tight-witness-per-deletion properties
  into the oracle profile scan (code/lib/uc.py) as necessary conditions to ASSERT
  on a minimal counterexample, rather than re-deriving them; then state ONE new
  structural claim about the counterexample profile and attack it (SAT for finite
  existence).
```

## Why this direction

Started by operator directive: the counting sequence of union-closed families
(3, 13, 121, 4959, 2771103, … = OEIS A102896) is out of scope — a recurrence
for the count says nothing about whether an abundant element exists. The effort
belongs on the **abundance profile** instead: the exact integer vector
`(|{A∈F : x∈A}|)_{x∈[n]}`.

The profile is where the entropy-coupling bound lands: the coupling inequality
says that if every coordinate density is `< 1/2`, then `H(A∨B) > H(A)`, which
contradicts union-closure. So a candidate counterexample is exactly a profile
whose maximum density is `< 1/2`.

## What would falsify it

A union-closed family whose maximum density is `< 1/2` and for which the
conditionally-iid coupling inequality is *satisfied* (i.e. the coupling bound
does not reach `1/2`) would show the profile is not constrained enough by this
coupling class alone.

## Claims this thread now rests on (all filed, searchable)

Each of these is on the shelf via `search_claims`; the thread-index "resting on
nothing" rows are stale (the claims exist):

- **`spence-minimum-counterexample-odd`** (asserted): a minimum-cardinality
  counterexample has ODD |F|=2k+1, every element frequency ≤ k, every
  admissibly-removable member omits a tight freq-k element; lattice form has
  every two meet-irreducibles sharing a lattice-tight join-irreducible. Adds
  parity + tight-witness structure that ROOT.md's |F|≥51 does not carry.
- **`bouchard-averaging-height4`** (asserted): separating UC families of height
  ≤4 (with |B|≤2 nuance) have Avg ≥ n/2 hence an abundant element; h=4 is the
  largest averaging-reachable height.
- **`bouchard-upper-bound-length`** (asserted): |A| ≤ Σ_{i≤ℓ} C(n,i) with full
  equality characterisation; with Karpas |F|<2^{n−1} it bounds how short a
  counterexample's height can be.
- **`gnm-envelope-rarest-floor-tight`** (asserted, proof in the anchor): the
  rarest element's count g(n,m) = max(1, m−2^{n−1}), tight for every m.
- **`min-density-uc-families-are-near-n-cube`** (asserted): the min-density
  (WORST=1/(2^{n-1}+1)) class is exactly one isomorphism class, the near-n-cube.

## Correction recorded this pass (odd-filter min-max)

`research/backward/abundance-profile-odd-filter-minmax.md` is corrected: the
min-max-density value over NON-Boolean UC families is 2^{n-1}/(2^n−1) (correct)
but the odd filter is NOT the unique minimizer — there are n+1 minimizers (odd
filter + the n power-set-minus-singletons). This is NOT counterexample-relevant
(those families have max density far above 1/2); it was a stale-extremal
cleanup, not a new bound. Claim `odd-filter-max-density-extremal-nonboolean`.

## Next

Fold parity |F|=2k+1 and the tight-witness property into the oracle profile
scan as necessary conditions to assert (not re-derive). A minimal counterexample
sits at |F|≥51, odd, every frequency ≤ (|F|−1)/2 but (being a counterexample)
no frequency ≥ |F|/2, no degree-1 element, and each removable member omits a
tight freq-(|F|−1)/2 element. Any claimed minimal-counterexample profile must
be checked against all of these simultaneously.
