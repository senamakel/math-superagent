# Hilbert projective metric / Birkhoff contraction

```approach
idea: |
  Reframe the Gilbreath row map as a self-map of a convex cone and attack
  regeneration with Birkhoff's Hilbert projective metric / nonlinear
  Perron–Frobenius theory. Every prior contraction attempt (ifs-attractor,
  total-variation, Ducci potential) used l1 / l∞ / quadratic norms and died
  on the known 2-Lipschitz (non-contraction) obstruction. The Hilbert metric
  is the metric that is NATIVE to monotone homogeneous maps — the one class
  the primitives of |a−b| = max(a,b) − min(a,b) belong to — and it routinely
  gives strict contraction where norm metrics fail.
mechanism: |
  The cell map |a−b| = max(a,b) − min(a,b) is built from the two canonical
  monotone, order-preserving, homogeneous (degree-1) primitives max and min.
  Birkhoff's theorem (1957; Hopf; Nussbaum's monograph) is exactly the
  structure theory of such maps: an order-preserving homogeneous map
  T: C∘ → C∘ on a cone C with finite projective diameter
  Δ = sup_{x,y} d_H(x,y) < ∞ (d_H = Hilbert projective metric) is a strict
  contraction with coefficient tanh(Δ/4) < 1, hence has a unique positive
  eigenvector (fixed ray) and every orbit converges to it projectively.

  The obstacle to apply it literally is that the coordinatewise map
  h ↦ (|h_i − h_{i+1}|)_i is NOT order-preserving (with b=4, |a−4| =
  4,2,0,2,4 as a runs 0,2,4,6,8 — it falls then rises). So the load-bearing
  question is not "is T a contraction in l1/l∞" (answered no, ifs-attractor
  refuted) but "is there a monotone homogeneous COMPANION operator whose
  fixed rays are exactly the safe rows".

  Two concrete companions to test, both natural and both previously unexamined:

  (A) The upper-envelope / lattice map. The row maximum M(h) = max_i h_i is
      monotone and provably non-increasing under the halved map (the run's
      EH-max-principle). The map that tracks the SUB-LEVEL SETS
      F_c(h) = indicator of {i : h_i ≥ c} is order-preserving, and the whole
      conjecture A_k(1) ∈ {0,2} is a statement about which sub-level sets
      reach position 1. If the induced map on the lattice of sub-level sets
      (or on the "support lattice" 2^ℕ) is a Birkhoff contraction, the safe
      configuration is the unique attractor.

  (B) The excess operator E(t)_i = max(0, |t_i − t_{i+1}| − 1) from the
      adopted excess-height-renormalization. On the cone of non-negative
      profiles it is sub-additive and dominates t ↦ t_i + t_{i+1} (max-plus
      linear). The speculation: on the quotient cone of profiles modulo the
      constant ray, some power of E (or of its monotone envelope
      t ↦ max_{j}(|t_j − t_{j+1}|−1)_+ composed with the lattice structure)
      is order-preserving homogeneous with finite projective diameter, so
      Birkhoff gives convergence to the zero profile (= safe {0,2} rows).

  What this buys, if it works: a genuine invariant — the Hilbert-distance
  drop d_H(E^m(t), safe) ≤ tanh(Δ/4)^m · d_H(t, safe) — that is a *rate*,
  not just the (settled) erosion fact. The regeneration event then shows up
  as the place where the projective distance is re-normalised, and the open
  rate question becomes "how fast does the re-normalised distance recover",
  which is a computable, nameable quantity.
status: refuted
killed-by: |
  The load-bearing hypothesis of Birkhoff's theorem — an order-preserving
  homogeneous self-map of a cone with FINITE projective diameter — fails for
  both proposed companions, on the very 2-coordinate witness that already
  killed level-set percolation. The literal map is non-monotone (|a−4| =
  4,2,0,2,4). Companion (B), the excess operator E(t)_i = max(0, |t_i−t_{i+1}|−1),
  is ALSO not order-preserving: t = (0,4) ≤ t' = (2,4) coordinatewise, yet
  E(t) = max(0,|0−4|−1) = 3 > E(t') = max(0,|2−4|−1) = 1. So E(0,4) ≰ E(2,4)
  while (0,4) ≤ (2,4). Companion (A), the sub-level-set lattice map, inherits
  the same non-monotonicity because the induced component map is |a−b| cell
  for cell. Hence no order-preserving homogeneous companion exists with the
  required finite projective diameter, and the Birkhoff–Hopf contraction
  (coefficient tanh(Δ/4)) never engages. This is the same structural
  non-monotonicity the run already refuted for level-set-percolation and
  ifs-attractor (czz2011-ducci-2-lipschitz: the map is 2-Lipschitz, not a
  contraction). The Hilbert metric machinery is real (Birkhoff 1957, Trans.
  AMS 85:219–227; Kohlberg–Pratt 1982 MOR 7:198–210; Nussbaum 1988 Mem. AMS
  391; Thompson 1963 Proc. AMS) but its generating hypotheses do not hold for
  any order-preserving companion of the Gilbreath row map. Hand-checked exact
  witness (0,4)≤(2,4), E(0,4)=3 > E(2,4)=1; no execution tool available, the
  arithmetic is one-line. NOT refuted by absence: refuted by the structural
  non-monotonicity at the candidate's own 2-coordinate falsifier gate.
side: general-class / dynamical (regeneration side; no prime distribution)
named-mathematics: |
  Hilbert projective metric, Thompson's part metric, Birkhoff–Hopf contraction
  theorem, nonlinear Perron–Frobenius theory (Nussbaum, "Hilbert's projective
  metric and iterated nonlinear maps", Mem. AMS 75 (1988); Birkhoff 1957
  Trans. AMS; Hopf 1963), order-preserving homogeneous maps, the lattice
  structure of sub-level sets.
speculative: |
  High. The exact map T is not order-preserving (minimal witness
  |a−4| at a=0,2,4,6,8 is non-monotone), so Birkhoff applies only to a
  COMPANION operator whose existence and fixed-ray classification are
  conjectural. This is the honest risk: if neither (A) nor (B) yields a
  monotone homogeneous companion with finite projective diameter, the approach
  is dead on the same "no monotonicity" ground that killed level-set
  percolation. It is NOT a restatement of ifs-attractor (which tested l1/l∞
  contraction of the literal map and was refuted); it tests a different metric
  on a different (lattice/envelope) operator.
falsifier: |
  (a) For small halved rows (entries {0..6}, length ≤ 10) compute the induced
      sub-level-set map and the excess operator's monotone envelope; if
      neither is order-preserving, or if the projective diameter does not
      shrink (Birkhoff coefficient tanh(Δ/4) ≥ 1), the mechanism fails.
  (b) A fixed ray of the companion that is NOT the zero profile (would show
      the attractor is not the safe set, so contraction alone does not force
      A_k(1) ∈ {0,2}).
first-step: |
  tool_builder (O(L^2·M) per row, L ≤ 12, M ≤ 8; exact integers; report the
  bound): implement d_H(x,y) = log max_i(x_i/y_i) − log min_i(x_i/y_i) on the
  positive cone. For the excess operator E(t)_i = max(0,|t_i−t_{i+1}|−1):
  (1) verify order-preservation numerically and print the minimal
  non-monotone witness if any; (2) compute the projective diameter Δ of the
  forward image E(cone) and the Birkhoff coefficient tanh(Δ/4); (3) iterate
  E on random profiles and measure the per-step Hilbert-distance drop to the
  zero profile. Report CONFIRMED (coefficient < 1) / REFUTED (coefficient
  ≥ 1 or non-monotone) with the exact numbers — never "theorem".
```

precedent: |
  - Hilbert projective metric / Birkhoff contraction theorem: G. Birkhoff,
    "Extensions of Jentzsch's theorem", Trans. AMS 85 (1957) 219–227,
    doi:10.1090/S0002-9947-1957-0087058-6 — order-preserving homogeneous maps
    with finite projective diameter contract with coefficient tanh(Δ/4).
  - Kohlberg & Pratt, "The Contraction Mapping Approach to the Perron–Frobenius
    Theory: Why Hilbert's Metric?", Math. Oper. Res. 7(2) (1982),
    doi:10.1287/moor.7.2.198 — Hilbert metric is native to order-preserving
    homogeneous maps; proves you cannot simplify it while keeping contraction.
  - R. D. Nussbaum, "Hilbert's projective metric and iterated nonlinear maps",
    Mem. AMS 75 (1988) no. 391, doi:10.1090/memo/0391 (and II, Mem. AMS 1989,
    doi:10.1090/memo/0401) — the nonlinear Perron–Frobenius / contraction
    theory in the Hilbert metric on cones.
  - A. C. Thompson, "On certain contraction mappings in a partially ordered
    vector space", Proc. AMS (1963), doi:10.1090/s0002-9939-1963-0149237-7 —
    order-metric contraction for nonlinear order-preserving maps.
  - Lemmens & Nussbaum, "Birkhoff's version of Hilbert's metric and its
    applications in analysis", in Handbook of Hilbert Geometry (2014),
    doi:10.4171/147-1/10 — survey of the contraction ratio and iteration for
    order-preserving homogeneous maps.
  - 2026 nonlinear-transfer-operator cone-contraction (J. Stat. Phys.,
    doi:10.1007/s10955-026-03586-2) — Hilbert-metric cone contraction extended
    to self-consistent nonlinear transfer operators via Gateaux order-preservation
    criteria.
  - NOT applied to Gilbreath anywhere searchable; the run's own refutations that
    bear: czz2011-ducci-2-lipschitz (map is 2-Lipschitz, not a contraction),
    ifs-attractor-contraction (no l1/l∞ contraction on the cone, pair tested
    inside the safe set), level-set-percolation (level predicate non-monotone).
    claim-ids: czz2011-ducci-2-lipschitz, ifs-contraction-falsifier-fired.

## Why this is not on disk

- **Not `ifs-attractor-contraction`** (refuted): that candidate looked for a
  strict contraction of the *literal* map T in l1/l∞ on a cone and was refuted
  (the 2-Lipschitz bound is tight inside the safe set itself). This candidate
  uses the Hilbert projective metric — the metric for *order-preserving
  homogeneous* maps — and applies it to a *companion* operator (sub-level-set
  lattice or the excess operator's monotone envelope), not to T.
- **Not `max-plus-tropical-spectral-dynamics`** (refuted): that entry asked for
  a max-plus *spectral* eigenvalue to certify A_k(1) ≤ 2, and died because a
  max-plus functional is dominated by the tail. Here the projective metric is
  used to get a *rate of convergence to the zero profile*, not an eigenvalue
  bound on the second entry.
- **Not `murota-l-convexity`** (proposed, unchecked): that entry builds an
  L♮-convex potential; this entry builds a *metric contraction*, a different
  object with a different conclusion (attractor classification vs potential
  monotonicity).
