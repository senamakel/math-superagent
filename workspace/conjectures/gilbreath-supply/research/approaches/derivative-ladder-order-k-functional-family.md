# The Δ-ladder as an explicit K-ordered functional family, priced order by order

```approach
idea: >
  Promote the already-grounded Δ-commutation invariance (claim
  derivative-ladder-identities-survive; approach derivative-ladder-delta-commutation)
  from a single invariance theorem into an explicit, correlation-order-indexed
  family of functionals
      F_K(h) := ν₂(Δ^{K-1} h) = wt(Φ_n Δ^{K-1} h),   K = 1, 2, 3, ...
  By the exact ladder (L3), F_K(h) = ν₂(n+K-1) − #{ d ∈ [2,K] : T(n+K-1, d)=1 },
  so each F_K is a functional of the fold (up to K bounded local cells). Its
  sensitivity is genuinely order K: the order-1 statistics of Δ^{K-1} h are
  order-K statistics of h. This turns GOAL priority 2 into a systematic SCAN:
  for each K, write the exact mod-4 arithmetic object Δ^{K-1} h measures, and
  price whether it is provably controlled unconditionally. The deliverable is
  either (a) the least K at which the demanded input is strictly weaker than
  pointwise mod-4 switch density, or (b) a clean theorem that every K lands at
  the length-K parity barrier. The family is exactly the "K > 1 functional" the
  reopened pass asks for, in a form whose arithmetic content is written down
  rather than abstract.

mechanism: >
  Named machinery: the F₂ difference operator Δ = 1+σ, the Frobenius collapse
  (1+σ)^{2^m} = 1+σ^{2^m} over F₂, and the binomial transform
  Δ^{K-1} h[j] = Σ_{i=0}^{K-1} C(K-1,i) h[j+i] (mod 2). Why it suits the
  problem: the ladder is an exact identity (no conjecture, no measure theory),
  so the functional family is priced exactly. Each K has a distinct arithmetic
  object: Δ^{1} h[j] = [q_j ≢ q_{j+2} mod 4] (a distance-2 two-point object,
  the parity-barrier family); Δ^{2^m} h[j] = h[j] ⊕ h[j+2^m] (a four-point
  mod-4 pattern); general K-1 gives a linear combination over a length-K window
  of the switch indicator, i.e. a length-K mod-4 pattern frequency. The scan
  locates exactly where the parity barrier first thins or fails to. This is a
  genuine application of the grounded ladder that its own file did not carry
  out: that file priced only k=1 and k=2^m and concluded "relocates onto the
  distance-2 correlation"; the family scan is the new content.
status: grounded
precedent: >
  THE LADDER IS AN ESTABLISHED, MACHINE-VERIFIED IDENTITY (in-workspace); the
  arithmetic meaning of each F_K is a mod-4 consecutive-prime pattern frequency,
  and ALL non-constant length-≥2 pattern frequencies are OPEN in the literature.
  Hence the run's own scan is what decides GOAL priority 2; the literature prices
  the barrier, not the scan's hypothesis.
  - The F₂ binomial/difference operator and higher-order directional derivatives:
    Carlet, "Boolean differential calculus and its application to switching
    theory", IEEE Trans. Comput. C-22 (1973) — the differential operators and their
    relation to the Walsh spectrum (the named home of Δ and Δ^K on Boolean
    functions); "On the boolean partial derivatives and their composition",
    Appl. Math. Lett. 24 (2011) — higher-order directional derivatives as
    compositions of partial derivatives in the ANF. These make Δ^{K-1} a standard,
    named object; the Frobenius collapse (1+σ)^{2^m}=1+σ^{2^m} is the Frobenius
    endomorphism over F₂.
  - The barrier the family hits: claim `abgs-p1-wide-open`, `lau-nonconstant-pattern-open`
    (even a single non-constant length-2 mod-4 pattern is not known to occur
    infinitely often), `maynard-pattern-densification` (refuted: lau-pattern-count-bound
    fails at modulus 4). Equal-residue (constant) patterns are covered (Shiu;
    BFTB bounded gaps), but the fold's cells — by endpoint-sign-corrected-identity,
    products over run PAIRS χ(r_a)χ(r_b) — read the non-constant side. So across
    EVERY K, Δ^{K-1}h's density is a non-constant-pattern frequency, and no
    unconditional positive-density statement exists for it in the literature.
  - In-workspace: claim `derivative-ladder-identities-survive` (the ladder
    (L1),(L4),(L5) is machine-verified); approach
    `derivative-ladder-delta-commutation` (grounded) — priced only k=1 and k=2^m;
    this family scan is the new content.
  VERDICT: grounded as an exact invariance THEOREM with a well-defined ordering,
  and the pricing is decisive: the honest product for EVERY K is the parity-barrier
  equivalence, not a weaker-input attack. The one conditional opening the scan
  could expose — a K whose Δ^{K-1} input happens to be a CONSTANT (equal-residue)
  pattern class, which Shiu/BFTB control — must be checked mechanically in the
  first step; there is no literature support that any K of the family avoids the
  non-constant barrier. The K* budget (claim kstar-exact-floor: floor(n/2)) means
  the family is only a useful functional for K ≲ n/2 terms, which is consistent
  with exactly the reopened territory.
first-step: >
  (tool_builder + research, exact arithmetic on the real residue string
  r_j = q_j mod 4, guards ν₂(53)=18 etc.) For K = 2..20: (1) compute
  Δ^{K-1} h[j] for the real prime h over j ≤ 40000, and express it as the
  minimal set of mod-4 residue-tuple (pattern) frequencies it is a linear
  statistic of; (2) for each K, record which proven inputs control that pattern
  class (PNT-AP / Dirichlet for one-point; Shiu / Maynard-Tao / BFTB for
  equal-residue strings; ABGS §9 and lau-nonconstant-pattern-open for the
  non-constant side); (3) print the first K (if any) whose demanded input is
  provably strictly weaker than pointwise switch density. FALSIFIER: if no K
  in the scan has a provable input strictly weaker than switch density, the
  honest output is the clean "every K lands at the length-K parity barrier"
  statement (GOAL priority 4 flavour), not a forced positive claim.
falsifies: >
  (a) a K whose Δ^{K-1} h pattern class is provably controlled and strictly
  weaker than switch density (then the family answers GOAL priority 2
  positively); (b) a K where the ladder identity F_K = ν₂(n+K-1) − O(K) fails
  against the oracle (a bookkeeping defect — already machine-verified for
  k ∈ {1,2,4} in the grounded approach, so this would be a regression); (c) the
  pricing showing some K's input is exactly switch density itself (then that K
  contributes nothing and the scan continues to larger K); (d) if some
  Δ^{K-1}h is a constant (equal-residue) pattern statistic controlled by
  Shiu/BFTB — the single conditional opening the scan could find that the
  literature already prices as the wrong (equal-residue) direction.
```
