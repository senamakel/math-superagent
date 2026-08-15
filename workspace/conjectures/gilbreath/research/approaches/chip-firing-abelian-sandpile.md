```approach
idea: chip-firing-abelian-sandpile
mechanism: |
  The recharge identity b_k = b_1 + sum over events i<k of (j_i+1) - (k-1) is a
  conservation law, and this run has already observed it is "the central
  accounting". The new move is to recognise that a conservation law on a path
  graph with a sink is the setting of the ABELIAN SANDPILE MODEL / chip-firing:
  heights on the line graph, toppling moves mass to neighbours, and the left
  column is the mass crossing into the sink at position 0.

  The exact dictionary: write the halved row h_k (>=0) as a height
  configuration on the half-line. The step h_{k+1}(i) = |h_k(i) - h_k(i+1)| is
  the size of the potential drop across the edge (i, i+1); equivalently it is
  the amount of "mass" that must move across that edge to level the pair to its
  minimum. So one row-to-row step is a full parallel sweep of edge-wise
  levelling, and A_k(1) = 2 h_k(1) is the drop across the leftmost edge (into
  the sink at 0).

  What the abelian-sandpile theory adds: (i) ABELIANNESS — the final stable
  configuration and the total number of topplings (the ODOMETER) are
  independent of the order of firings; and (ii) the LEAST-ACTION PRINCIPLE /
  Dhar's burning algorithm, which gives a canonical monotone object (the
  odometer function) and a certificate that a configuration cannot send more
  than a given mass to the sink.

  Named mathematics: abelian sandpile model, chip-firing on graphs, odometer
  function, least action principle, Dhar's burning algorithm, stabilisation,
  recurrent vs transient configurations.

  Speculative (and why it may fail): on a PATH graph, chip-firing is close to
  trivial — there is no branching, and the min-cut refutation already noted
  "the network is a single chain". The first step is explicitly to test whether
  the odometer collapses to the single-chain flow already refuted.
status: refuted
disposition: (b) parked — refuted, not a route to G-supply; path critical group trivial + row map conserves no mass (Directive 44 item 2).
killed-by: |
  Research (this cycle) established the collapse risk the candidate itself
  flagged: on a path (half-line) graph there is no chip-firing structure for
  the odometer / least-action machinery to add, for three independent reasons.

  (1) The defining object of the sandpile model is the CRITICAL (sandpile)
      group, whose order is the number of spanning trees of the graph
      (Kirchhoff's matrix-tree theorem), and for ANY tree — in particular any
      path — the critical group is TRIVIAL (Becker–Glass, "Cyclic Critical
      Groups of Graphs", 2016; plus the tree-critical-group literature:
      Toumpakari conjecture resolved in "The sandpile group of a tree" 2008,
      and the cone-over-tree results). A trivial group means the Laplacian
      quotient Z^{V}/{im L} has no nonzero invariant factors: there is NO
      sandpile abelian structure, no recurrent-configuration combinatorics, and
      no least-action/burning object on a path beyond the trivial one. Every
      theorem the approach wants to import (abelian property, Dhar's burning
      algorithm, odometer as a monotone vector) is a theorem about a graph
      whose sandpile group is nontrivial; on a path it degenerates.

  (2) The row map is NOT a chip-firing/conservation process at all: it does
      NOT conserve mass. The sandpile toppling rule preserves total chip mass
      (and the whole theory of number-conserving cellular automata / sand
      automata is built on a conserved invariant — see the NCCA literature:
      Durand–Formenti–Róka; Redeker 2023 "An Invitation to
      Number-Conserving CA"). The Gilbreath step h -> |h_i - h_{i+1}| has no
      conserved quantity: sum(h_{k+1}) != sum(h_k) in general (e.g.
      h=(2,0,3,1) has sum 6, next row (2,3,2) sum 7, next (1,1) sum 2; or
      h=(1,2,4,8) sum 15 -> (1,2,4) sum 7). So there is no "mass" moving to a
      sink, no toppling that preserves chips, and the odometer (which counts
      topplings of a CONSERVED quantity) has nothing to count. The row step is
      not a number-conserving cellular automaton and not an abelian sandpile
      toppling; it is a difference/levelling map.

  (3) Even granting a conservation reading, the recharge identity is already
      the exact conservation law, and it is on a single forward chain — the
      structure the min-cut refutation (held claim
      zero-sum-flow-conservation-mincut-refuted) already showed reduces any
      "certificate" to a restatement of the conjecture. The odometer's
      "least-action" content on a path is precisely "mass into sink = b_k",
      the recharge quantity itself, and a "mass into sink <= 1" certificate is
      exactly the unproved (2,4)-event sufficiency, not a new monotone bound.

  Research verdict: refuted. Path-graph chip-firing has a trivial critical
  group and no conserved mass under this map, so the abelian/least-action
  machinery does not exist here; the candidate's own kill test (path collapse)
  fires. Do not re-propose sandpile/odometer language unless a conserved
  quantity under the row map is first identified, which research found none.
precedent: |
  - https://cupola.gettysburg.edu/mathfac/39 (Becker–Glass 2016: the critical
    group of a tree is trivial; order = #spanning trees = 1 on a tree) and the
    tree-critical-group literature (The sandpile group of a tree, 2008;
    Reiner–Smith "Sandpile groups for cones over trees" arXiv:2402.15453:
    cone-over-path structure is generated by leaf vectors only, trivial in the
    pure-path case)
  - https://arxiv.org/abs/2308.00060 (Redeker 2023, "An Invitation to
    Number-Conserving Cellular Automata") and the NCCA conservation literature
    (Durand–Formenti–Róka; Hattori–Takesue): number conservation is the
    defining invariant of sand/traffic CA; the Gilbreath map conserves no sum.
  - held claim: zero-sum-flow-conservation-mincut-refuted (the single-chain
    "network" pattern this approach would repeat)
  - code/out/check_three_candidates_research.py (mass-not-conserved examples:
    (2,0,3,1) and (1,2,4,8))
first-step: |
  Closed by research: the path collapse fires. The critical group of a path is
  trivial (no sandpile structure), and the row map conserves no mass (not a
  chip-firing process), so the odometer/least-action/burning machinery has
  nothing to act on. Do not re-open unless a conserved quantity under the row
  map is found.
```

```claim
id: chip-firing-path-collapse-refuted
statement: The abelian-sandpile / chip-firing formulation of the Gilbreath recharge identity collapses on a path graph: (a) the critical (sandpile) group of any tree, hence any path, is trivial (order = number of spanning trees = 1), so there is no recurrent-configuration / abelian / least-action / burning structure to import; (b) the row map h -> |h_i - h_{i+1}| conserves no total mass (e.g. (2,0,3,1): sums 6->7->2; (1,2,4,8): 15->7), so it is not a chip-firing / number-conserving toppling process and there is no odometer counting conserved topplings; (c) a "mass into sink <= 1" certificate would be the unproved (2,4)-event sufficiency (the single-chain recharge), the same restatement the min-cut refutation closed. Hence the odometer is not a new monotone object for Gilbreath.
hypotheses: the claim that the recharge identity can be read as an abelian-sandpile conservation law on a path graph with a sink, with the odometer as a new vector-valued monotone object.
holds-here: yes
status: checked
bearing: Refutes the chip-firing-abelian-sandpile approach at the candidate's own kill test. It reduces to the already-refuted single-chain flow (trivial critical group + no conserved mass).
anchor: research/approaches/chip-firing-abelian-sandpile.md
```
