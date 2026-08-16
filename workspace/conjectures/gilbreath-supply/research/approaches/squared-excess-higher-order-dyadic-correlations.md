# The second moment of the excess functional is exactly a weighted sum of ≥2-factor character correlations — and the switch density never appears as a standalone term

```approach
idea: >
  Statement (A) — the single arithmetic input the geometry routes left open,
  "E[S(n)²] = O(n) for the fixed prime string" — should not be bounded by a
  random model (that transfer is dead) but written EXACTLY in the fold's own
  coordinates. Squaring the run-telescope identity gives, for the FIXED prime
  residue string r_j = q_j mod 4 (r_0 = 2, r_j ∈ {1,3} for j ≥ 1):

      ε_d ε_{d'} = (−1)^{XOR_{j ∈ M_d △ M_{d'}} h[j]}
                 = ∏_{R ∈ runs(M_d △ M_{d'})} χ(r_{a_R}) χ(r_{b_R}),

  where [a_R, b_R−1] is a maximal consecutive run of the symmetric difference,
  the telescoping identity h[j] = [r_j ≠ r_{j+1}] sends each run to the endpoint
  pair (a_R, b_R) at separation = run length ℓ_R = b_R − a_R. Hence, pulling the
  diagonal out (ε_d² = 1),

      S(n)² = (n−2) + Σ_{d ≠ d'} ∏_R χ(r_{a_R}) χ(r_{b_R}).

  THE LOAD-BEARING FACT (a theorem, no arithmetic): the switch density
  Σ_j u_j, u_j = χ(r_j)χ(r_{j+1}) = the adjacent (separation-1) switch sign,
  NEVER appears as a standalone term of S(n)². A term equal to a single switch
  sign u_j would be a symmetric difference of size 1 (a single run of length 1,
  endpoints (j, j+1)); but |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} −
  2^{pc(d∧d')+1} is ALWAYS EVEN, so no symmetric difference is a singleton.
  Separation-1 switch signs occur only as factors multiplied by other factors
  (from the remaining runs), never alone. The minimal (distance-2) stratum is
  classified exactly: it is a sum of products u_a u_b of EXACTLY TWO switch
  signs (order 4 in χ) at classified non-adjacent positions — Type A:
  {2^a, 2^b} gives two singletons at positions separated by 2^a − 2^b;
  Type B: {2^a+2^b, 2^a} or {2^a+2^b, 2^b} gives two singletons separated by a
  power of two. Single-run terms (one factor) have separation ≥ 4 (a
  consecutive doubleton {a,a+1} would be a distance-2 pair, which the
  classification shows is always two singletons, never a doubleton).
mechanism: >
  (1) [imported, proved] linearisation + Lucas: T(n,d) = XOR_{o⊆d} h[n−1−d+o]
  = XOR_{j∈M_d} h[j], M_d = {n−1−d+o : o⊆d}; ε_d := (−1)^{T(n,d)}.
  (2) [imported, checked] excess bridge: ν₂(n) = (n−2−S(n))/2,
  S(n) = Σ_{d=2}^{n−1} ε_d, so SUPPLY ⟺ S(n) ≤ (1−2c)(n−2) eventually.
  (3) [imported, checked] run telescope, generalised to any consecutive run
  [u,v]: XOR_{j∈[u,v]} h[j] = [r_u ≠ r_{v+1}] (consecutive switch indicators
  telescope to the endpoint comparison); for r ∈ {1,3},
  (−1)^{[r_u≠r_{v+1}]} = χ(r_u)χ(r_{v+1}). Applied to each maximal run of
  M_d △ M_{d'} this gives (SQ) exactly.
  (4) [imported, theorem] the meet formula
  |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}
  (downset-row-intersection-meet-formula) makes every symmetric difference even
  and ≥ 2 for d ≠ d'; distance-2 pairs classified exactly
  (a2-is-theta-log-squared-confirmed) as two singletons (Type A/B), never a
  doubleton. Hence: (i) no singleton symmetric difference ⟹ no standalone
  switch sign; (ii) the minimal stratum is a sum of products of exactly two
  switch signs.
  (5) [imported, theorem] the distance distribution A_k is an exact n-local
  count (downset-row-code-distance-closed-form), so the weights of each
  correlation stratum are combinatorial, not fitted.
  Boundary caveat (honest): r_0 = 2 is not a unit mod 4, so χ(r_0) is
  undefined; symmetric differences whose runs touch position 0 (only pairs
  involving d = n−1, hence O(n) of them) must be read in the raw [r_a ≠ r_b]
  form. This does not affect any O(n) statement.
status: grounded (all load-bearing in-workspace claims verified/proved on disk; the squared run-telescope identity (SQ) and the evenness/standalone-switch-sign impossibility are hand-verified here and structurally sound. The open question — whether products of switch signs u_j at the fold's classified separations are strictly weaker than switch density (priority 4) or equivalent to it (priority 5) — is exactly the decidable object (SQ), and the literature (LOS 2016: r≥2 consecutive-prime patterns are open; Matomäki–Merikoski only under Siegel-zero hypotheses) gives no orthogonality theorem for these index-domain products, so the honest position is: geometry grounded, arithmetic open.)
precedent: >
  In-workspace, imported as established: linearisation-fold-weight (proved),
  excess-is-negative-character-sum (checked),
  g-run-telescope-verified (checked; telescoping to endpoint comparison over a
  consecutive run), downset-row-intersection-meet-formula
  (proved-by-derivation; even symmetric differences), a2-is-theta-log-squared-confirmed
  (checked; A₂ = Θ((log n)²), distance-2 pairs classified as two singletons),
  downset-row-code-distance-closed-form (adopted; F_n(z)=O(n) for |z|<1 is a
  theorem), meet-join-parseval-self-duality (adopted; sharp negative — geometry
  carries no pointwise force, so (A) is irreducibly arithmetic). Classical/
  sourced: χ mod 4 is the unique quadratic character of conductor 4,
  χ(q_j) = (−1/q_j) = (−1)^{(q_j−1)/2} (quadratic reciprocity).
  NEW here (hand-verified, machine verification is first-step): the SQUARED
  run-telescope identity (SQ) over symmetric differences M_d △ M_{d'} (the
  on-disk telescope is stated for down-sets and used pointwise; the second
  moment over symmetric differences is not on disk), and the evenness
  consequence — that a standalone switch-sign term is impossible, so the
  switch density is orthogonal to S(n)² as a summand, though switch signs
  appear as factors within products. The refuted
  dyadic-gap-character-correlation route established the pointwise telescope
  for the FIRST moment; the SECOND-moment form with exact combinatorial
  weights is the new object.
first-step: >
  tool_builder, exact integer/F₂ arithmetic, real residue string r_j = q_j mod 4
  (j = 0..n, r_0 = 2), oracle = s_direct/t_direct in lib.supply_fold:
  (1) VERIFY (SQ) for n ≤ 60 and every ordered pair (d,d') ∈ [2,n−1]²:
      ε_d ε_{d'} = ∏_{R∈runs(M_d△M_{d'})} (−1)^{[r_{a_R} ≠ r_{b_R}]}, computed
      independently of the literal ε_d ε_{d'} = (−1)^{T(n,d)⊕T(n,d')}; use the
      raw form at the position-0 boundary. NEGATIVE CONTROL: a 3-valued
      boundary (r mod 3, as in g_run_telescope_verify_negctrl) must break the
      identity on a positive count of pairs — otherwise the check is vacuous.
  (2) VERIFY the structural facts: (i) |M_d △ M_{d'}| even and ≥ 2 for all
      d ≠ d' in [2,n−1]; (ii) no singleton symmetric difference (⟹ no
      standalone switch-sign term); (iii) distance-2 pairs are exactly two
      non-adjacent singletons; (iv) every single-run symmetric difference has
      even run length ≥ 4. Print the run-length multiset of each symmetric
      difference for n = 8..32 as the exhibit.
  (3) COMPUTE the exact A_k-weighted decomposition of the off-diagonal sum
      Σ_{d,d'} ∏_R (−1)^{[r_{a_R}≠r_{b_R}]} for the REAL prime string for n up
      to the oracle ceiling, stratified by distance k and by run-count, and
      report which strata carry the bulk of S(n)² − (n−2).
  (4) HAND OFF the priced object to research: the single question — is there an
      orthogonality/equidistribution theorem for products of switch signs
      u_j = χ(q_j)χ(q_{j+1}) along the primes at the fold's classified
      separations (order ≥ 4 in χ, or a single higher-separation factor), one
      that does NOT require resolving the switch-density mean? Yes ⟹ GOAL
      priority 4 (a strictly weaker input). No ⟹ GOAL priority 5 (SUPPLY is
      equivalent to a statement in the switch-density family), recorded as such.
falsifier: >
  (a) (SQ) fails against the oracle → the squared telescope is misread and the
      route is dead before any arithmetic. (b) A singleton symmetric difference
      exists (a term equal to a single switch sign) → the evenness claim is
      false, switch density enters S(n)² standalone, and the honest product is
      the equivalence theorem (priority 5), not a weaker input. (c) Research
      finds the switch-sign-product correlations at the fold's classified
      separations (and the single higher-separation two-point factors) are as
      hard as switch density itself → priority 5 is the truth, recorded as
      such. Each outcome is a named result.
```

## Hand check of the load-bearing identity (n=5, d=2, d'=3)

`n−1 = 4`; `M₂ = {4−2+o : o⊆2} = {2,4}`, `M₃ = {4−3+o : o⊆3} = {1,2,3,4}`;
`M₂ △ M₃ = {1,3}` = two singleton runs `[1,1]`, `[3,3]`. Then

```
ε₂ ε₃ = (−1)^{h[1] ⊕ h[3]} = (−1)^{[r₁≠r₂] ⊕ [r₃≠r₄]} = χ(r₁)χ(r₂) · χ(r₃)χ(r₄),
```

a product of two switch signs `u₁ u₃` at separation 2 (a power of two: the pair
`(2,3)` is Type B). With the real residues `r = (2, 3,1,3,3)` for
`q = (2,3,5,7,11)`: `χ(r₁)χ(r₂) = χ(3)χ(1) = −1`, `χ(r₃)χ(r₄) = χ(3)χ(3) = +1`,
product `−1`; the raw side is `h[1]=[3≠1]=1`, `h[3]=[3≠3]=0`, `(−1)^{1⊕0} = −1`. ✓

## Hand check that a single switch sign is impossible (the evenness fact)

A term equal to one switch sign `u_j = χ(r_j)χ(r_{j+1})` would require
`M_d △ M_{d'} = {j}`, i.e. a symmetric difference of size 1. But the meet
formula gives `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`, a sum
of two powers of two minus one power of two — always even (each `2^pc` is even
for `pc ≥ 1`, and `d,d' ≥ 2` forces `pc ≥ 1`). So size 1 is impossible, and no
term of `S(n)²` is a single switch sign. The switch density `Σ_j u_j` — the
parity barrier's own object — is a sum of exactly such single switch signs, so
it is orthogonal to `S(n)²` as a summand: it enters only multiplied by other
factors. ✓

## Hand check that single-run terms have separation ≥ 4

`↓3 = {0,1,2,3}`, `↓5 = {0,1,4,5}`, so `↓3 △ ↓5 = {2,3,4,5}` — a single run of
length 4 — giving `ε₃ ε₅ = χ(r₂)χ(r₆)`, one factor at separation 4 (an order-2
term in χ, but NOT the switch density). A single run of length 2 would be a
consecutive doubleton `{a,a+1}`; that is a distance-2 symmetric difference,
which the A₂ classification shows is always TWO singletons (Type A/B), never a
doubleton. Hence single-run terms have even separation ≥ 4. This is the
honest correction to the first draft's "order ≥ 4 always": order-2 terms exist
but at separation ≥ 4, never at separation 1. ✓

## Why this is the synthesis the three candidates pointed at, and not their corpses

- **`cramer-gallagher-second-moment`** (refuted: model is mod-4 unbiased, and
  the fold's first moment is carried by the biased switch density). It was
  right that the SECOND MOMENT is the object, wrong to compute it in an
  unbiased random model. Here the second moment is written exactly and
  deterministically; no model, no transfer.
- **`level-set-explicit-formula-index-correlation`** (refuted: the π-level-set
  weight never leaves the index domain, so value-domain dispersion cannot act).
  It was right that χ is the character, wrong about the domain. Here χ is kept
  at prime indices with the separations the fold actually reads, exposed by the
  run telescope rather than a π-weight.
- **`haar-chaos-hypercontractive`** (refuted: Bonami–Beckner bounds a random
  input, not the fixed prime string). It was right that S(n)² is a structured
  chaos form; the correct way to open the chaos is the EXACT run-telescoped
  character product, not a moment inequality over a random cube.

## Why it is not any of the closed doors or refuted routes

- Not "h is complicated enough": the input is a named arithmetic object
  (products of switch signs u_j at the fold's classified separations), and the
  controls (all-ones, Thue–Morse, sparse) are exactly the strings whose
  switch-sign sequences are periodic/automatic and hence have NON-decaying
  autocorrelations — they must and do fail the input.
- Not `dyadic-gap-character-correlation` (refuted for the FIRST moment, whose
  bulk spreads across popcount strata): this is the SECOND moment, whose
  weights are the exact distance distribution (a theorem), and whose minimal
  stratum is read off exactly.
- Not `matomaki-radziwill-index-autocorrelation` (refuted: value-domain engine,
  g=0 collapse): no value-domain engine is claimed; and the g=0 collapse is
  evaded in the precise sense above — switch density never appears as a
  standalone summand of S(n)², only as factors inside products.
- Not the five closed doors: it spends no hypothesis on h's weight, runs,
  aperiodicity, anti-dyadicity, or periodicity.

## Honest limits

The squared identity is a reformulation, not yet a bound: it converts (A) into
a precise, weighted character-correlation statement and pins its minimal priced
object. Whether products of switch signs at the fold's separations are strictly
weaker than switch density (priority 4) or equivalent to it (priority 5) is the
open question, and the identity is exactly the object on which that question is
now decidable. The claim that a standalone switch-sign term is impossible is the
geometric consequence of even symmetric differences (a theorem), and it is the
only structural part asserted here; nothing about the arithmetic of the primes
is asserted, and no bound on S(n)² is claimed.
