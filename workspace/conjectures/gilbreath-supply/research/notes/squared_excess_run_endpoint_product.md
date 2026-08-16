# Squared-excess identity: S(n)² as a weighted sum of run-endpoint character products

Author: inventor (adversarial school), convergence pass. The reformulation lives at
`research/approaches/squared-excess-higher-order-dyadic-correlations.md` (adopted).
This note carries the load-bearing claim as a fenced block so it reaches
`research/CLAIMS.md`, and states exactly what is derived vs. what is open.

## The identity (derived, machine verification is the approach's first-step)

Fix n, rows d ∈ [2, n−1], windows M_d = {n−1−d+o : o ⊆ d}, the prime residue
string r_j = q_j mod 4 (r_0 = 2, r_j ∈ {1,3} for j ≥ 1), h[j] = [r_j ≠ r_{j+1}],
and the excess S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} = Σ_d ε_d, with
ν₂(n) = (n−2−S(n))/2 (imported, checked: excess-is-negative-character-sum).

Squaring and using the run telescope (imported, checked: g-run-telescope-verified,
valid for ANY consecutive run in a two-symbol alphabet):

```
S(n)² = (n−2) + Σ_{d≠d'} ∏_{R ∈ runs(M_d △ M_{d'})} χ(r_{a_R}) χ(r_{b_R}),
```

where [a_R, b_R−1] is a maximal consecutive run of the symmetric difference and
(−1)^{[r_a≠r_b]} = χ(r_a)χ(r_b) for r ∈ {1,3}.

Hand check (n=5, d=2, d'=3): M₂△M₃ = {1,3} = two singletons,
ε₂ε₃ = χ(r₁)χ(r₂)·χ(r₃)χ(r₄) = u₁u₃ with u_j = χ(r_j)χ(r_{j+1}). ✓
(The real residue string r=(2,3,1,3,3) gives −1, matching the raw side.)

```claim
id: squared-excess-run-endpoint-product
statement: >
  For every n and every ordered pair (d,d') with d,d' in [2,n−1] and d ≠ d',
  ε_d ε_{d'} = ∏_{R ∈ runs(M_d △ M_{d'})} χ(r_{a_R}) χ(r_{b_R}), where
  [a_R, b_R−1] runs over the maximal consecutive runs of the symmetric
  difference M_d △ M_{d'} = {n−1−d+o : o ⊆ d} △ {n−1−d'+o : o ⊆ d'}, and
  χ(r_a)χ(r_b) = (−1)^{[r_a ≠ r_b]} for r ∈ {1,3}. Consequently
  S(n)² = (n−2) + Σ_{d≠d'} ∏_R χ(r_{a_R})χ(r_{b_R}).
hypotheses: r_0 = 2 is not a unit mod 4, so χ(r_0) is undefined; runs touching
  position 0 (only symmetric differences of pairs involving d = n−1, O(n) of
  them) must be read in the raw [r_a ≠ r_b] form. No hypothesis on the prime
  string beyond the two-symbol boundary r_j ∈ {1,3}.
holds-here: yes — it is an F₂/character identity independent of the primes'
  arithmetic, resting on the linearisation, the run telescope, and the
  two-symbol fact [r_a≠r_b] = (1−χ(r_a)χ(r_b))/2.
status: derived-by-hand (n=5, d=2, d'=3 exhibited); machine verification of the
  identity for n ≤ 60 over all pairs is first-step (1) of the adopted approach,
  with a 3-valued negative control.
bearing: rewrites the single open arithmetic input (A) — the second moment of
  S(n) for the fixed prime string — exactly in the fold's own coordinates as a
  weighted sum of run-endpoint character products, with the weights being the
  exact distance distribution (a theorem). It does NOT bound S(n)²; it converts
  (A) into a named correlation statement and pins its minimal priced object.
anchor: research/approaches/squared-excess-higher-order-dyadic-correlations.md
follows-from: linearisation-fold-weight, excess-is-negative-character-sum,
  g-run-telescope-verified
```

## The structural fact (theorem-level, no arithmetic)

```claim
id: no-standalone-switch-sign-in-squared-excess
statement: >
  No off-diagonal term of S(n)² is a single switch sign u_j = χ(r_j)χ(r_{j+1}).
  A term equal to u_j would require M_d △ M_{d'} = {j} (a singleton symmetric
  difference); but |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1} is
  ALWAYS EVEN for d,d' ≥ 2 (each summand is a positive power of two), so a
  singleton is impossible. Single-run terms exist and have even run length ≥ 4
  (a length-2 run would be a consecutive doubleton, but the distance-2 pairs are
  classified as TWO singletons, never a doubleton — a2-is-theta-log-squared-confirmed).
  The distance-2 stratum is a sum of products u_a u_b of exactly two switch signs
  at classified non-adjacent positions (Type A: separation 2^a−2^b; Type B:
  separation 2^g).
hypotheses: d,d' ∈ [2,n−1], d ≠ d'; the meet formula
  downset-row-intersection-meet-formula and the A₂ classification
  a2-is-theta-log-squared-confirmed (both imported as established).
holds-here: yes, unconditionally — pure combinatorics of the row set, no
  hypothesis on the primes.
status: proved-by-derivation (evenness is a parity count of powers of two; the
  single-run length ≥ 4 follows from the A₂ classification; hand-checked
  examples ↓3△↓5 = {2,3,4,5} one run of length 4). Machine confirmation is
  first-step (2) of the adopted approach.
bearing: the switch DENSITY Σ_j u_j — the parity barrier's own 2nd-order object
  — never appears as a standalone summand of S(n)². Switch signs enter only as
  factors inside products (order ≥ 2 in χ, with the distance-2 stratum at order
  4). This is a precise sense in which the fold's second moment is orthogonal to
  the one-point switch statistic, and it is what makes the weaker-input question
  (GOAL priority 4) decidable on this object.
anchor: research/approaches/squared-excess-higher-order-dyadic-correlations.md
follows-from: downset-row-intersection-meet-formula, a2-is-theta-log-squared-confirmed
```

## What is open (stated, not asserted)

The single priced question handed to research (first-step 4): is there an
orthogonality/equidistribution theorem for products of switch signs
u_j = χ(q_j)χ(q_{j+1}) along the primes at the fold's classified separations,
one that does NOT require resolving the switch-density mean?
- Yes ⟹ GOAL priority 4 (a strictly weaker arithmetic input suffices).
- No ⟹ GOAL priority 5 (SUPPLY is equivalent to a statement in the
  switch-density family), recorded as such.

Nothing here asserts a bound on S(n)², and nothing about the arithmetic of the
primes is claimed. The only asserted facts are the identity and the evenness
structural fact, both stated above with their status.
