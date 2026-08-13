```approach
idea: Rule 90 cellular automaton with absorbing boundary — reframe the {0,2}
      region as a Rule 90 (XOR) CA and regeneration as boundary absorption
mechanism: >
  The block lemma's internal structure shows that within the {0,2} region,
  after halving (dividing by 2), the absolute-difference operator reduces to
  XOR: |a−b|/2 = (a/2) XOR (b/2) when a,b ∈ {0,2}. This is exactly Wolfram's
  Rule 90 — the additive cellular automaton where each cell is the XOR of its
  two parents. The entire {0,2} block of the Gilbreath triangle is a Rule 90
  evolution from the initial bit-string given by A_1(2), A_1(3), ... (halved).

  Rule 90 is one of the most studied CAs. Its key properties:
  - Linear over GF(2): the state at time t is the convolution of the initial
    state with Pascal's triangle mod 2 (the Sierpinski gasket).
  - Finite strings with fixed boundary conditions have well-understood dynamics:
    periodicity, transient length, and the structure of "gliders" (the Sierpinski
    pattern itself is the Green's function).
  - The boundary between the {0,2} region and the rest of the row is where the
    "intruder" values (4, 6, 8, ...) sit. These are values ≥ 4, which, when
    halved, are ≥ 2 — they inject values outside {0,1} into the Rule-90 region.

  The regeneration question becomes: does the Rule 90 dynamics absorb these
  boundary values, converting them into {0,1} (i.e., {0,2} after doubling)?
  Specifically, if a boundary cell has halved value v ≥ 2, what happens to it
  under iteration of the absolute-difference operator?

  Key observation: values > 2, when they enter the operator, produce larger
  values until they are reduced. The question is: in the Rule 90 region adjacent
  to the boundary, does the XOR dynamics force the injected high values to
  cancel?

  The mod-4 linearization gives the exact evolution: if we track values mod 4
  (or mod 2^t), the operator is d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4). This is
  NOT Rule 90 for the full value — it's linear addition mod 4, but with sign
  flips from the absolute value. The sign pattern is determined by which of the
  two arguments is larger.

  The approach: characterize the exact sign pattern at the boundary. If the
  intruder value at position n is v, then the difference with its neighbor from
  the {0,2} block (value 0 or 2) is either v or v−2. The key invariant to hunt:
  under what conditions does |v − 0| or |v − 2| (mod 4) become 0 or 2 after
  a bounded number of iterations?

  If we can prove that any value ≥ 4, when placed next to a sufficiently long
  {0,2} block, is reduced to 0 or 2 within B rows where B is bounded by a
  function of the value (or uniformly bounded), then regeneration is proved:
  the block only needs to be long enough to absorb the intruders at its edge,
  and the prime gaps provide blocks that grow (on average) fast enough.

status: proposed
first-step: >
  Isolate every row transition where the leading {0,2} block grows (60 events
  in the depth-1000 data). For each event, extract the values at and just past
  the block boundary in the preceding row, and track how they evolve over the
  next 1-5 rows. The question: is there a uniform local pattern — e.g., does
  a boundary configuration (0, v) or (2, v) with v ≥ 4 always reduce to {0,2}
  within a fixed number of rows? Code the boundary propagator that takes a
  window [0/2-block tail, intruder, next-value] and iterates the absolute
  difference until all values are {0,2}, recording the number of rows needed.
  If the number of rows is bounded by a function of max(v) alone, that's the
  regeneration lemma.
```