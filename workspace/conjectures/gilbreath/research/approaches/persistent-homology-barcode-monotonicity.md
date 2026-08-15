```approach
idea: A persistence-theoretic invariant — find a feature of the 1D sublevel-set
(persistence) barcode of the row that is MONOTONE under the absolute-difference
map and whose vanishing forces A_k(1) ∈ {0,2}. The conjecture becomes a
bottleneck-distance contraction via the persistence stability theorem.

mechanism: |
  The halved row h_k (positions i ≥ 0, h_k(0)=1 odd, h_k(i≥1) the even interior
  halved) determines the next row by h_{k+1}(i) = |h_k(i) − h_k(i+1)|. The
  leading {0,2} block of row k+1 is EXACTLY the leading run of positions i with
  |h_k(i) − h_k(i+1)| ≤ 1 (the run's own 1-Lipschitz characterization). So the
  second entry A_{k+1}(1) = 2·h_{k+1}(1) = 2·|h_k(1) − h_k(2)| is determined by
  the FIRST slope of h_k. The conjecture A_k(1) ∈ {0,2} is: the first slope of
  every halved row is 0 or 1.

  Persistent homology reading: attach to the slope sequence s(i) = |h_k(i) −
  h_k(i+1)| its 0-dimensional persistence module over the SUPERLEVEL filtration
  {i : s(i) ≥ t}. A slope value s(1) = 0,1,2,3,... is exactly the "death level"
  of the component of position 1: the left edge stays inside {0,1} iff the
  component over position 1 dies at level ≤ 1. So A_{k+1}(1) ∈ {0,2} ⟺ the
  persistence interval born at position 1 has death value ≤ 1.

  The machine is the persistence STABILITY THEOREM (Cohen-Steiner–Edelsbrunner–
  Harer 2007): the bottleneck distance between persistence diagrams is
  1-Lipschitz in the sup-norm of the underlying functions. If the row map
  h → |∂h| is non-expanding in the right functional norm (or if the diagram of
  the next row is a "morphological erosion" of the previous diagram — an
  operation with a known, controllable effect on barcodes), then the death level
  of the leftmost component is driven down toward {0,1}. Unlike every scalar
  potential tried (run-count, TV, Dirichlet energy — all refuted on the XOR
  zigzag), the persistence diagram is a SET-valued invariant with a genuine
  Lipschitz stability theorem, and unlike the refuted level-set-percolation
  (whose monotone-cluster premise was false) it does not require the level
  predicate itself to be monotone — only that the DIAGRAM move in a controlled
  way under the map.

status: refuted
side: general-class / dynamical (a persistence invariant of the operator, independent of primality)
killed-by: |
  REFUTED at its load-bearing dictionary, decidable by first principles on the
  run's own oracle rows (no search needed).

  (1) The central identity "the 0-dim superlevel death value of the component
      over position 1 equals s(1) = A_{k+1}(1)/2" is FALSE. In a superlevel
      filtration the component containing index 1 does not die at s(1); it
      dies at the saddle where it merges into a component of higher birth
      value, which for an isolated local maximum is strictly BELOW s(1).
      Concrete counterexample on the oracle row A_2 = (1,0,2,2,2,2,2,2,4,..),
      halved h=(1,0,1,1,1,1,1,1,2,..): slopes s(1)=|0-1|=1, s(2)=0, tail 0 up
      to the 2. Position 1 is a local max of value 1 flanked by the 0-plateau;
      its component dies at the 0-saddle, i.e. death = 0, while s(1) = 1. So
      death value = 0 != A_{3}(1)/2 = s(1) = 1 already at row 2 -> 3. The
      dictionary the approach is built on fails on the real rows.

  (2) Where the identity does degenerate to hold it is a PURE RESTATEMENT:
      s(1) = A_{k+1}(1)/2 by definition, so "death value of the position-1
      component <= 1 iff A_{k+1}(1) in {0,2}" carries no more information than
      the single number s(1), which the candidate itself identifies as the
      first slope. The persistence diagram at index 1 IS the conjecture
      restated — structurally identical to the refuted agama-trace and
      wasserstein-kantorovich restatements. A set-valued invariant that
      contains no more than a coordinate of its input is not an invariant.

  (3) The speculative half — that h -> |dh| induces a non-expansion or
      controllable erosion on the persistence diagram in bottleneck distance —
      is supplied by NO theorem. The Cohen-Steiner-Edelsbrunner-Harer
      persistence stability theorem bounds how the diagram of a FIXED function
      moves under a sup-norm perturbation of that function; it says nothing
      monotone about the action of the absolute-difference MAP on successive
      diagrams (a sequence of different functions), which is precisely the
      unproved transfer. And every scalar or set-valued monotonicity tried so
      far dies on the XOR zigzag of the interior (run-count, total-variation,
      Dirichlet energy all refuted); nothing in persistence theory removes
      that obstruction, because the obstruction is that A_{k+1}(1) can rise
      while a neighboring barcode feature falls.

  Verdict: refuted, killed by the false dictionary at row 2 -> 3 and the
  restatement structure. No persistence literature has been applied to the
  Gilbreath triangle (searches returned TDA papers on ODE systems and graphs
  only). Do not re-propose the persistence reading unless the death-value
  dictionary is first corrected AND a true contraction on the diagram is
  established, neither of which exists.
precedent: |
  - The persistence stability theorem (real, but misapplied here):
    Cohen-Steiner-Edelsbrunner-Harer, "Stability of Persistence Diagrams",
    Discrete Comput. Geom. 37 (2007) 103-120,
    doi:10.1007/s00454-006-1276-5; and the algebraic stability theorem
    (Chazal et al.). It bounds the diagram under perturbation of a fixed
    function; it does not supply the map-on-diagram contraction the approach
    needs.
  - held claims {agama-trace-restatement, wasserstein restatement}: the
    restatement structure this approach repeats; and the scalar-potential
    refutations (run-count, TV, Dirichlet energy) that the XOR zigzag defeats.
  - Oracle rows in problem.md / witnesses.json: A_2 halved = (1,0,1,1,1,..),
    the counterexample source for (1).
named-mathematics: persistent homology, sublevel/superlevel filtrations, persistence barcodes, the persistence stability theorem (Cohen-Steiner–Edelsbrunner–Harer), bottleneck distance, morphological erosion of persistence diagrams
speculative: The load-bearing claim — that the absolute-difference map induces a NON-EXPANSION (or a controllable erosion) on the persistence diagram in bottleneck distance, certifying the leftmost death value stays ≤ 1 — is conjectured. The stability theorem itself is a theorem; the transfer to this specific map is what must be sourced or falsified. It is entirely possible the map is not non-expanding in bottleneck distance, in which case the approach is refuted cheaply.
falsifier: If the bottleneck distance between consecutive halved rows' slope-diagrams can INCREASE (no 1-Lipschitz control), or if the leftmost component's death value is not forced down, the transfer fails — measured directly on the oracle rows before any theory is built.
first-step: |
  From the oracle rows (witnesses.json depth 600, exact integers) build, for each
  live row k: the halved row h_k, the slope sequence s_k(i) = |h_k(i) − h_k(i+1)|,
  and its 0-dim superlevel persistence diagram (a finite set of (birth, death)
  intervals). Record the death value d_k of the component over position 1 (this
  equals h_{k+1}(1), i.e. A_{k+1}(1)/2 — the first check is that the dictionary is
  right). Then compute the bottleneck distance between consecutive diagrams and
  test whether it is ≤ ||s_k − s_{k−1}||_∞ (stability is automatic) AND whether
  the leftmost death value d_k is non-increasing after smoothing out the {0,1}
  oscillation, or is bounded by the 1-Lipschitz excess of the row. Cost O(depth ×
  width), one row live. A verified monotone diagram feature is a new invariant
  candidate for Lean; a violation at a (2,4)-event pins the boundary correction.
```
