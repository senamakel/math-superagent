```approach
idea: tropical-box-ball-ultradiscrete-integrable
mechanism: |
  The absolute-difference operator A_{k+1}(i) = |A_k(i) − A_k(i+1)| admits a
  tropical / max-plus algebraic formulation that connects it to the theory of
  ultradiscrete integrable systems — specifically the Box-Ball System (BBS)
  and the ultradiscrete Toda lattice.

  The key identity: for non-negative integers a, b,

      |a − b| = max(a, b) − min(a, b)

  This is a difference of max and min, which are the TWO fundamental tropical
  operations. Over the max-plus semiring (R ∪ {−∞}, max, +), the Gilbreath
  operator becomes a combination of max and min that is NOT purely max-plus
  linear, but it IS expressible as a difference of two max-plus expressions.

  More importantly, the condition for regeneration — (x, y) = (2, 4) at the
  boundary — involves a SMALL-VALUE constraint: the edge must be exactly 2
  (not 0, not ≥4) and the intruder must be exactly 4. This is a
  "level-set" condition rather than an algebraic condition. The drain law
  y → y − 2·[x=2] is ALSO a level-set-triggered decrement. The edge x
  itself is 0 or 2, i.e., it is the parity of the XOR of the halved block —
  which is exactly a "soliton" state in a binary cellular automaton.

  The Box-Ball System (Takahashi–Satsuma 1990) is an ultradiscrete integrable
  cellular automaton defined on Z_{\ge 0}-valued configurations. Its dynamics
  are: each "ball" moves to the right by one step per time unit, with
  interactions (two balls cannot occupy the same site, so they queue). The
  BBS has infinitely many conserved quantities (soliton amplitudes) and is
  exactly solvable via the ultradiscrete limit of the discrete Toda lattice.

  The CONNECTION to Gilbreath: the Rule 90 / XOR evolution inside the {0,2}
  block is known to be the mod-2 reduction of a BBS-like dynamics on the
  binary digits. More specifically, the Pascal-mod-2 / Sierpinski structure
  is the "carrier" wave of the BBS. The intruder values ≥ 4 are "incoming
  solitons" from the right, and the boundary (edge x, intruder y) is a
  "soliton-boundary interaction." The drain law is the gradual absorption
  of the soliton's amplitude, and the regeneration event (x=2, y=4) is the
  point where the soliton has been absorbed enough that its amplitude drops
  to 2 (at the halved level, dropping from t to 0 in the valuation
  formulation).

  The central conjecture in this framing: **the leading {0,2} block is a
  "vacuum" state of the BBS, and the intruder values are solitons that
  travel toward the left column at a bounded speed.** The left column
  (position 0) is a reflecting or absorbing boundary for the BBS. The
  protection of the left column (A_k(0) = 1) corresponds to the fact that
  no soliton ever reaches the boundary with sufficient amplitude to disturb
  it — all incoming solitons are absorbed (reduced to the vacuum level {0,2})
  before they reach position 0.

  If the Gilbreath triangle is exactly (or asymptotically) an ultradiscrete
  integrable system, then:

  1. There exist CONSERVED QUANTITIES (the soliton amplitudes and their
     order) that are determined by the initial row (the prime gaps) and
     are invariant under the dynamics.

  2. The interaction of solitons with the vacuum boundary is DETERMINISTIC
     and SOLVABLE — i.e., the time it takes for a soliton of amplitude a
     to be absorbed into the vacuum is a known function of a.

  3. Since the prime gaps are bounded (heuristically: Cramér's conjecture
     says p_{n+1} − p_n = O(log^2 p_n)), the soliton amplitudes are bounded,
     and the absorption time is bounded — hence the boundary is never
     reached by a soliton with amplitude > 0.

  The TROPICAL formulation: encode the triangle as a family of piecewise-
  linear functions. The operator T(f)(i) = |f(i) − f(i+1)| on an integer
  sequence f can be seen as the ultradiscrete limit of the discrete
  derivative. The iteration T^k is then the ultradiscrete k-th derivative.
  The conjecture says the ultradiscrete k-th derivative of the prime
  sequence, evaluated at position 0, is ±1 (absolute value 1) for all k.
  This is a statement about the TROPICAL SMOOTHNESS of the prime sequence:
  its tropical derivatives eventually become and stay {0,2}-valued.

  The strongest version: the Gilbreath triangle of the primes is EXACTLY
  the ultradiscrete Toda lattice with a particular initial condition, and
  the conjecture follows from the complete integrability of the Toda lattice.
  This is highly speculative. But the weaker version — that the triangle
  shares structural properties (conserved quantities, soliton absorption)
  with the BBS — is testable by computing the soliton content of the prime
  gaps and checking conservation.

  Why it beats existing approaches:
  - NOT a linear-algebraic approach (unlike Walsh-Hadamard, GF(2), Z_2)
  - NOT a combinatorial counting approach (unlike renewal, step-law)
  - It brings a completely different mathematical theory (integrable systems,
    soliton theory, tropical geometry) that has powerful exact-solvability
    results
  - The conserved-quantity structure, if it exists, would give a PROOF of
    the conjecture: conserved quantities that bound the soliton amplitude
    from above, combined with the soliton-absorption time being a function
    of amplitude, prevent any soliton from reaching the left column
  - It connects to a vast literature where exact results are available
    (Tokihiro–Takahashi–Matsukidaira–Satsuma 1996, "From soliton equations
    to integrable cellular automata through a limiting procedure")

  Speculative: the connection might be at the level of the ultra-discrete
  Painlevé equations rather than the Toda lattice, since the Gilbreath
  operator is a DIFFERENCE (derivative-like) rather than a shift. The
  ultradiscrete limit of the discrete Painlevé I equation gives a cellular
  automaton with similar absolute-difference structure. This is uncharted
  territory for the Gilbreath conjecture.
status: refuted
killed-by: |
  The tropical/BBS framing is creative but unsupported at three load-bearing
  points, two of which the existing literature directly contradicts.

  1. **The "soliton absorption" mechanism is the refuted rule90-absorbing-
     boundary in new clothes.** CHT 2026 Lemma 3.7(iii) proves that a
     {0,d}-valued block stays {0,d}-valued in ALL descendants WITHOUT
     decrease in magnitude — the exact opposite of absorption. An intruder
     value ≥ 4 adjacent to a {0,2} block is the d ≥ 2 case of a {0,d}
     block beginning at the boundary, and CHT says it persists, not that
     it drains. The drain law the run observes (y decreases by 2 when x=2)
     is a fact about the prime rows, not a consequence of any integrable
     structure, and CHT's proof that {0,d} persistence can be the generic
     obstruction refutes any claim that soliton absorption is a general
     property of the operator.

  2. **The BBS and the absolute-difference operator are structurally
     different.** The BBS moves balls rightward one site per time step
     (a shift-based CA); the Gilbreath operator |a−b| is a difference
     between neighbours producing a value at the LEFT position. The two
     CAs have different light-cone geometry: BBS information flows
     rightward, Gilbreath information flows downward with a fixed stencil
     coupling neighbours. The connection "Rule 90 is the mod-2 reduction
     of BBS" is shallow — Rule 90 is the mod-2 reduction of many CAs, and
     the fact that two systems share a mod-2 skeleton does not make one
     the ultradiscrete limit of the other. The approach's own first step
     (checking soliton conservation) is the right test, but no source
     establishes the connection, and the structural mismatch between the
     shift-based BBS and the difference-based Gilbreath operator makes
     the "exact integrable system" claim a long shot.

  3. **The conserved-quantity argument is the conjecture stated in
     integrable-systems language, not a reduction.** The claim "conserved
     soliton amplitudes prevent any soliton from reaching the left column"
     assumes (a) soliton amplitudes exist and are conserved, (b) the
     absorption time is a function of amplitude, and (c) the amplitudes are
     bounded. Each of (a), (b), (c) is a restatement of the regeneration
     problem — (a) is the existence of an invariant separating the block
     from the tail, (b) is the drain law with a uniform bound, (c) is the
     gap boundedness hypothesis. No source has established any of these
     for the Gilbreath operator on the primes, and the approach does not
     reduce them to something known.

  The approach is not worthless — the tropical/max-plus formulation
  |a−b| = max(a,b) − min(a,b) is a real identity and may provide a useful
  lens. But the BBS/soliton connection is not established in the literature
  and the absorption claim is refuted at the general-class level. The
  computational first step (checking soliton conservation) is still worth
  running as a negative-result probe, but the approach cannot be adopted
  as a proof strategy without first establishing the connection it
  postulates.
precedent: |
  No source connects the Gilbreath absolute-difference operator to the
  Box-Ball System or ultradiscrete Toda lattice. The BBS literature
  (Takahashi–Satsuma 1990, Tokihiro et al. 1996, Inoue–Takenawa 2023)
  treats a shift-based CA on the half-line; the tropical limit of the
  discrete Toda lattice produces the BBS, not a difference operator. The
  CHT (2026) and BCZ (2023) results are at the mod-2 level (Rule 90 /
  Sierpinski), which is the common ground between Rule 90 and BBS but
  does not lift to the full nonlinear Gilbreath operator. The Ducci
  literature (Ciamberlini–Marengoni 1937, Calkin–Stevens–Thomas 2005,
  Chamberland 2003) treats the same operator on cyclic sequences but does
  not connect it to integrable systems.
first-step: |
  Write a small computational exploration. For the halved Gilbreath triangle
  of the primes (depth 200, width 200), treat the entries as a BBS
  configuration. Run the standard BBS algorithm (move balls right, queueing)
  on this 2D array, treating the row index as "time" and the column index as
  "space" — but reversed (since the Gilbreath triangle goes down, while BBS
  time goes right). Specifically: transpose the triangle so that rows become
  time steps. Look for soliton tracks: trajectories where a "ball" (a value
  ≥ 2 in the halved triangle) moves rightward at a characteristic speed.

  Then compute the "soliton content" of the initial row (halved gaps between
  primes): apply the standard BBS inverse scattering transform — for each
  position, the number of balls above some threshold gives the soliton
  amplitudes. Check whether these amplitudes are CONSERVED as the Gilbreath
  triangle descends (i.e., whether the same set of soliton amplitudes
  appears in each row, just shifted rightward).

  If soliton-like conservation holds, formulate the precise ultradiscrete
  integrable system that the Gilbreath triangle corresponds to, and research
  whether its boundary-value problem has been solved. If no conservation is
  observed, record this as a negative result (the BBS connection is
  superficial) and close the approach.

  Output to code/out/tropical_bbs_exploration.{captured.txt,json}.
```