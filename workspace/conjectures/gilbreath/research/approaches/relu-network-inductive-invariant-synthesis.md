```approach
idea: relu-network-inductive-invariant-synthesis
mechanism: |
  The halved Gilbreath map H(h)_i = |h_i - h_{i+1}| is built from
  |u - v| = (u-v)_+ + (v-u)_+, and the positive part x_+ = max(0,x) is the ReLU
  nonlinearity. So the whole triangle is a FIXED piecewise-linear (ReLU) network:
  the row map is one layer of a ReLU cellular automaton, and depth-k entries are
  a fixed ReLU circuit evaluated on the initial halved gaps. The conjecture
  A_k(1) in {0,2} for all k is a SAFETY property of this ReLU dynamical system:
  the bad set is {(h, boundary) : |1 - 2h_1| >= 4} and it must be unreachable
  from the initial state.

  Every hand-hunted invariant this run tried (run-count, TV, alternating sum,
  Dirichlet energy, majorization, max-plus, L-convexity) was a SPECIFIC
  scalar functional, and each died on XOR-induced non-monotonicity. The
  different move here is to hand the search to the modern theory and tools of
  REACHABILITY/INVARIANT SYNTHESIS FOR PIECEWISE-LINEAR SYSTEMS, which are
  designed exactly for this shape and which the run has never invoked:

  - inductive invariant synthesis by templates: find coefficients c_i so that a
    polyhedral (or piecewise-linear) set S = {h : C h <= d} satisfies
    (i) initial state in S, (ii) h in S => H(h) in S, (iii) S excludes the bad
    values h_1 >= 2. This is a linear-constraint synthesis problem solvable with
    the run's smt_solver / an LP engine (Farkas-style, but for a FORWARD-INVARIANT
    SET, not a one-shot feasibility certificate — the thing the Farkas/CNS/AVE
    refutations correctly said was missing).
  - ReLU-network reachability: Marabou/Reluplex/Planet-style complete encodings,
    and abstract-interpretation domains (intervals, zonotopes, star sets) that
    over-approximate the reachable set of a ReLU network. A complete verifier
    that returns UNSAT for "some k <= K reaches the bad set" is a theorem for
    depth K; a template invariant that closes (ii) for ALL k is the target.

  The point is not to enumerate depth (that is the wrong method): it is to let a
  solver SEARCH the space of inductive invariants that every manual attempt
  failed to spot, and either return a certificate (a genuine invariant forcing
  A_k(1) in {0,2}) or return UNSAT over a stated template family (a recorded
  negative result bounding what a polyhedral invariant can do). Both are
  deliverables; the manual scalar-potential search produced neither.

  This is general-class/operator-level (no primes needed), and it attacks the
  regeneration/invariant side directly: a forward-invariant safe set is exactly
  what "events keep arriving" must be equivalent to.
status: refuted
killed-by: |
  SUPERSEDED, not falsified — the machinery transfers intact but the raw
  coordinates it was stated in are exactly the coordinates the run's
  scale-invariance refutations prohibit. The halved map H(h)_i = |h_i−h_{i+1}|
  is positively 1-homogeneous while the safety set {h_1 ≤ 1} is NOT, so a
  template/invariant family in raw coordinates cannot separate the safe value 2
  from the unsafe 4 (the identical obstruction that closed
  comparison-order-cellular-automaton and abs-difference-operad-normal-form),
  and a single-template synthesis can return a VACUOUS UNSAT. The correct host
  for the method is the run's PROVED excess coordinates t = max(0, h−1), where
  the safety condition becomes t_1 = 0 and the map E(t) = max(0, |t_i−t_{i+1}|−1)
  is genuinely non-homogeneous (the unit decrement and the floor at 0 are
  exactly where homogeneity breaks). Adopted in that corrected form as
  `excess-maximal-invariant-set`: the maximal safe set of width-K windows,
  computed exactly by the Rakovic–Kerrigan–Kouramas–Mayne / Blanchini backward-
  preimage fixed point, with the width-uniform description of S_K as the target
  invariant. The grounding's two machinery caveats (unbounded tail directions;
  reachability NP-complete) are both handled by the successor: the width-K
  backward recursion is exact and the max principle bounds the height to
  M = max window value, so the bounded-height box is a faithful
  over-approximation of the relevant state space, not a truncation.
precedent: |
  Method is real, mature, and named — this is a method-transfer, not a re-description.
  - Inductive invariant / barrier synthesis for PWA and ReLU systems:
    Samanipour-Poonawala, "Invariant Set Estimation for Piecewise Affine Dynamical
    Systems Using Piecewise Affine Barrier Function", arXiv:2402.04243; "Replacing
    K-infinity ... Leaky ReLU ... Union of Invariant Sets", arXiv:2502.03765;
    Dai-Landry-Pavone-Tedrake, CDC 2020, "Counter-example guided synthesis of neural
    network Lyapunov functions for piecewise linear systems" (doi:10.1109/cdc42340.2020.9304201);
    Teichrib-Schulze Darup, "Reachability analysis for PWA systems with NN-based
    controllers", arXiv:2411.03834 (polyhedral positively-invariant sets).
  - Complete ReLU reachability / verification: Bak-Tran-Hobbs-Johnson 2020
    (arXiv:2001.07103); Yang-Johnson-Tran et al. 2021, facet-vertex incidence
    (doi:10.1145/3447928.3456650); Isac-Zohar-Barrett-Katz, CONCUR 2023 (ReLU net
    reachability with QF-LIA spec reduces to reachability; NP-complete).
  No one has applied any of this to the Ducci/Gilbreath difference operator (searched;
  the votes target ACAS Xu/control/perception). Run claims it must respect:
    gilbreath-reduces-to-second-in-02 (the exact value the invariant must force),
    fwd-diff-identity-refuted (the linear part alone cannot certify the value),
    total-variation-oscillation-potential refuted (why a hand-hunted scalar potential
    failed; the point of handing the search to a solver).
status-caveat: |
  Two honest cautions from the machinery itself, both built into the first step:
  (1) BOUNDED-SET CAUTION. The reachable set contains unbounded tail gaps, so a true
      invariant set must be UNBOUNDED in the tail directions (only the h_1 <= 1
      direction is bounded by safety). The linear template S = {h : sum c_i h_i <= d,
      h_i >= 0} can still be unbounded (zero/negative c on tail indices) while
      excluding h_1 >= 2 — the synthesis search must allow that, not assume bounded.
  (2) EXACT REACHABILITY IS NP-COMPLETE (Isac et al. 2023). Bounded-depth K will be
      modest — a recorded bound, not a proof. Fine: the deliverable is the template
      SAT/UNSAT verdict, or the bounded K with verdict. UNSAT over a stated template
      family is a recorded negative bound on the whole polyhedral-invariant class.
first-step: |
  (a) Encode the one-step halved map H(h)_i = |h_i - h_{i+1}| = (h_i-h_{i+1})_+ +
      (h_{i+1}-h_i)_+ as a ReLU circuit; verify against the oracle rows (exact ints,
      zero mismatches expected).
  (b) Linear-template synthesis S = {h : C h <= d, h_i >= 0, unbounded in tail} with
      SMT (init in S, S forward-invariant under H, S excludes h_1 >= 2). SAT = a
      genuine invariant forcing A_k(1) in {0,2}; UNSAT over the family = recorded
      bound. Respect the bounded-set caveat in the template.
  (c) Bounded complete reachability (Marabou-style SMT) to depth K: independent
      falsification / confirmation; report K and verdict, never "theorem" for the
      bounded run.
named-mathematics: ReLU/positive-part decomposition, inductive invariant
  synthesis, abstract interpretation and complete verification of piecewise-linear
  (ReLU) networks (Reluplex/Marabou lineage), linear template synthesis
falsifier: >
  UNSAT over the template family is not failure — it is the recorded bound. The
  approach is refuted only if the synthesis returns UNSAT for every reasonable
  template family AND the bounded reachability keeps finding bad states just
  beyond each tried K, i.e. no invariant of any tried form exists and the safety
  claim is false. The decisive probe is (b): report the exact template and the
  exact SAT/UNSAT verdict.
side: general-class / dynamical (the operator is prime-free; the primes are one
  initial configuration)
```
