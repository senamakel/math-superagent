```approach
idea: excess-maximal-invariant-set
mechanism: |
  Compute the maximal safe set of the halved operator by exact backward
  induction over the causal cone, in the run's PROVED excess coordinates, and
  synthesize a width-uniform invariant from its shape.

  THREE INPUTS, NONE ALONE ENOUGH:

  (1) My reformulation (relu-network-inductive-invariant-synthesis, superseded
      below): stop hand-hunting a scalar potential — every such potential died
      on XOR non-monotonicity — and let EXACT SET computation search the space
      of forward-invariant sets. This is the forward-invariant-SET move the
      refuted Farkas/CNS/AVE lines correctly identified as missing.

  (2) Research's machinery: PWA/ReLU invariant synthesis and complete
      reachability are real and mature (Samanipour–Poonawala arXiv:2402.04243,
      arXiv:2502.03765; Teichrib–Darup arXiv:2411.03834; Bak et al.
      arXiv:2001.07103; Isac–Zohar–Barrett–Katz CONCUR 2023, ReLU reachability
      NP-complete). The canonical maximal positively-invariant-set method is
      Blanchini "Set invariance in control" (1999) and Rakovic–Kerrigan–
      Kouramas–Mayne (2005): the maximal invariant subset of a safe set is
      UNIQUE and is the fixed point of backward preimage iteration.

  (3) The run's own PROVED coordinates (excess-renorm-identity-proved, approach
      excess-height-renormalization): halve the interior h_k(i) = A_k(i)/2 and
      take the excess t_k(i) = max(0, h_k(i) − 1). The conjectured statement
      A_k(1) ∈ {0,2} is exactly t_k(1) = 0. The one-step map is pointwise and
      exact in three disjoint cases:

          bulk:  t_k(i), t_k(i+1) ≥ 1  ⟹  t_{k+1}(i) = max(0, |t_k(i)−t_k(i+1)| − 1)
          wall:  h_k(i) ∈ {0,1}, h_k(i+1) ≥ 1 ⟹ t_{k+1}(i) = t_k(i+1) − h_k(i)
          low:   h_k(i), h_k(i+1) ∈ {0,1} ⟹ t_{k+1}(i) = 0

      plus the max principle: max_i t_k(i) is non-increasing.

  WHY THE SYNTHESIS BEATS RAW-COORDINATE SYNTHESIS. The halved map H(h)_i =
  |h_i − h_{i+1}| is positively 1-homogeneous, but the safety set {h_1 ≤ 1} is
  NOT. This is the exact scale-invariance obstruction that refuted
  comparison-order-cellular-automaton and abs-difference-operad-normal-form:
  any homogeneous/free template is blind to the 2-vs-4 distinction the
  conjecture is about, so template synthesis in raw coordinates can return a
  VACUOUS UNSAT. The excess map E(t) = (D t − 1)_+ is NOT homogeneous — the
  unit decrement and the floor at 0 are exactly where homogeneity breaks — and
  the safety condition becomes t_1 = 0. In these coordinates the safety
  condition and the non-homogeneity live in the same place. This structure is
  now PROVED, not guessed.

  THE OBJECT. For a fixed depth K define the maximal safe set of width-K
  windows over the first halved row h_1 = (1,1,2,1,2,1,2,3,1,...) (halved prime
  gaps):

      S_K = { w ∈ [0..M]^K :  the triangle induced by w = h_1(1..K)
              has h_k(1) ≤ 1 for every row k = 1..K }

  (M a height bound; |a−b| ≤ max(a,b) so the box [0..M]^K is closed under the
  map). S_K is the UNIQUE maximal set of width-K windows safe for K rows,
  computed EXACTLY by backward induction over the causal cone (no floats, no
  approximation):

      S_1 = { w : w_1 ≤ 1 },
      S_K = { w ∈ [0..M]^K : w_1 ≤ 1  and  H(w) ∈ S_{K−1} },
      H(w)_i = |w_i − w_{i+1}|  (width shrinks by one).

  This is the RKM/Blanchini backward-preimage fixed point, specialised to the
  acyclic causal cone of a half-infinite triangle (no wraparound — the run
  established the cyclic and half-infinite operators differ).

  THE DELIVERABLE. Two outcomes, both recorded results:
  (a) WINDOWED CERTIFICATE (exact, not heuristic): the real h_1(1..K) window
      lies in S_K iff the real triangle is safe at position 1 to depth K. This
      is a warranted maximal-set certificate, strictly stronger than forward
      simulation of one trajectory.
  (b) WIDTH-UNIFORM INVARIANT (the target): read off the irredundant defining
      inequalities of S_K, expressed in excess coordinates t_i = max(0, w_i − 1),
      and test whether the description STABILISES as K grows (same constraints,
      only the window length changes). A stabilised description is a parametric
      invariant; proving it forward-invariant for ALL K by induction/Lean is
      the genuine GOAL.md invariant forcing A_k(1) ∈ {0,2}.
status: adopted-executed
first-step-done: |
  EXECUTED (code/out/excess_maximal_set*.py, exact ints, M=3, K=1..10;
  backward recursion == independent forward oracle at every K).
  (a) WINDOWED CERTIFICATE DELIVERED: real prime window h_1(1..K) in S_K for
  all K; S_K is the exact backward-preimage fixed point, not an approximation.
  (b) SYNTHESIS HALF CLOSED (falsifier (b) tripped): NO fixed finite prefix
  decides S_K — for every J=1..9 the safe all-zeros J-prefix extends to an
  UNSAFE window (0,...,0,2). Density |S_K|/4^K falls toward ~0.208, ratio
  |S_K|/|S_{K-1}| -> 4, so safety is a whole-window property, not a
  bounded-prefix/bounded-shape invariant. No width-uniform finite-prefix
  invariant of this class is synthesised at widths <= 10. This is a dead-end
  for the synthesis goal (posted to BOARD as dead-end); the exact maximal-set
  certificate survives as the deliverable. Also closed a false lead: the
  apparent excess "product box" 2*3^{K-2} is an attainability artifact
  (t=max(0,w-1) collapses w=0,w=1 both to t=0, discarding the far-tail-2
  distinction that decides safety) — the forward oracle refutes reading it as
  an invariant.
precedent: |
  PWA/ReLU invariant synthesis and complete reachability: Samanipour–Poonawala
  arXiv:2402.04243 and arXiv:2502.03765; Teichrib–Darup arXiv:2411.03834;
  Dai–Landry–Pavone–Tedrake CDC 2020 (doi:10.1109/cdc42340.2020.9304201);
  Bak–Tran–Hobbs–Johnson arXiv:2001.07103; Isac–Zohar–Barrett–Katz CONCUR 2023
  (ReLU reachability NP-complete). Maximal positively-invariant set: Blanchini,
  "Set invariance in control", Automatica 35 (1999); Rakovic–Kerrigan–Kouramas–
  Mayne, IEEE TAC 50 (2005). Run claims it must respect:
  excess-renorm-identity-proved (the coordinates and exact map), and the
  scale-invariance refutations comparison-order-cellular-automaton and
  abs-difference-operad-normal-form (why raw coordinates are the wrong host).
first-step: |
  tool_builder, TODAY (exact integer enumeration, no floats, report every
  number; cost ≤ (M+1)^K per backward pass, M=3, K≤8 ⇒ ≤ 4^8 = 65,536 states —
  trivial):

  1. Load the real first halved row h_1 from witnesses.json: halve A_1(i) for
     i ≥ 1 (expect (1,1,2,1,2,1,2,3,1,...)); verify against problem.md's A_1.
  2. Implement the map H(w)_i = |w_i − w_{i+1}| and the backward recursion
     S_1 = {w : w_1 ≤ 1}, S_K = {w ∈ [0..M]^K : w_1 ≤ 1 and H(w) ∈ S_{K−1}},
     for M = 3 and K = 1..8. Represent S_K as an exact Python set of tuples;
     mind the width index (S_K has width K; H drops one entry).
  3. MEMBERSHIP: report whether h_1(1..K) ∈ S_K for each K. Expect true for
     every K (this re-derives the known depth-600 safety as a maximal-set
     certificate, not forward simulation).
  4. SHAPE EXTRACTION (the synthesis step): for each K, compute the indicator
     of S_K in excess coordinates t_i = max(0, w_i − 1) and list its
     irredundant defining inequalities (or a minimal CNF/DNF over the t_i, and
     the 0/1 block bits). Report whether the constraint FAMILY stabilises with
     K: same inequalities, only the window length grows. If it stabilises, the
     candidate parametric invariant is the report's headline; if not, say at
     which K the family changed and how.
  5. SANITY: cross-check the recursion against the oracle triangle for the real
     window (simulate forward, expect identical safety verdict), and against
     the proved wall/bulk/low cases of excess-renorm-identity-proved.
named-mathematics: maximal positively-invariant set (Blanchini; Rakovic et al.),
  PWA/ReLU invariant synthesis and complete reachability (Samanipour–Poonawala;
  Teichrib–Darup; Bak et al.; Isac et al.), the run's excess renormalization
  E(t) = (D t − 1)_+ (excess-renorm-identity-proved)
falsifier: >
  (a) If the real h_1(1..K) window leaves S_K for some K, the convention or
      encoding is wrong (the run has already verified safety to depth ≥ 600, so
      this would expose a bug, not refute GC). (b) The approach as a PROOF OF
      GC fails if no width-uniform description of S_K emerges as K grows — i.e.
      if the number/form of the defining inequalities keeps changing with the
      window length. In that case the honest deliverable is the exact windowed
      certificate plus the recorded negative bound "no compact invariant of
      this class exists at widths ≤ K". (c) The max principle caps the height,
      so the box height M only needs to bound max_i h_1(i) over the window; if
      M is set too small the computation under-approximates and must be rerun —
      report M and the window max explicitly.
side: general-class / dynamical (prime-free operator; the primes enter only as
  the one initial profile h_1 whose membership in S_K is checked)
