# RSK / Greene–Kleitman growth diagram and last-passage percolation

```approach
idea: Encode the Gilbreath triangle's "defects" (halved entries outside {0,1}, i.e. original entries outside {0,2}) as a 0–1 environment and represent the iterated-difference dynamics as a Fomin growth diagram / RSK shape, so that Greene's theorem converts the block length b_k into a last-passage-percolation time and the regeneration events into record times of a corner-growth model.
mechanism: The proved block-lemma content is that the {0,2} interior evolves as XOR = Rule 90 = Pascal mod 2, i.e. a linear CA over GF(2) whose rows are the Sierpinski gasket. The classical companion fact is that Pascal's-triangle-mod-2 / Rule 90 is the boundary of a corner-growth / last-passage structure: a 0–1 matrix, run through RSK row insertion, produces a shape whose first-row length is (Greene–Kleitman / Greene 1974) the maximum, over up/right lattice paths, of the number of 1s collected — a last-passage percolation (LPP) time. The proposal is to find the correct 0–1 environment (candidates: the indicator of "adjacent halved difference ≥ 1" in the block, the indicator of the intruder's position, or the sign matrix of the min-branch) under which the leading-block boundary b_k equals the LPP front and a (2,4) regeneration event equals the creation of a new cell in the RSK shape. If such a bijection exists, then (i) b_k is a monotone partition-valued (shape) process — a genuinely new invariant, not a scalar potential of the kind already machine-refuted; (ii) Greene's theorem gives b_k = max over paths of the defect count, turning "the block never dies" into "the LPP front stays ahead of the corner", a statement LPP theory controls through its time constant and KPZ fluctuation exponent; (iii) the heavy-tailed regeneration jumps become the record structure of LPP, which is the known mechanism for why the surplus outpaces consumption.
status: ungrounded-bijection
The cheap falsifying first step (run before any LPP theory): for the prime rows to depth 1000 (blocks_depth1000.json) and the halved block, form the candidate 0–1 matrices and run RSK row insertion; check whether the first-row length of the resulting shape equals the block length b_k (and whether a local Fomin growth-diagram rule reproduces the row-to-row block evolution) for every row where the block is short (k = 1..40). If no candidate matrix reproduces b_k for the first 40 rows, the bijection fails and the approach is closed cheaply; if one does, the named LPP machinery (Greene–Kleitman theorem, time constants, Rost/Johansson) becomes available — with the strong caveat in `precedent` that the LPP time constant is a GROWTH law, and that growth has never been shown to control the {0,2}-block boundary which is an EROSION+regeneration boundary, not a monotone corner.

precedent: >
  - https://doi.org/10.1214/22-ps4 (Dauvergne–Nica–Virág, RSK in LPP: unified
    RSK from Pitman transforms; the bijection powers the directed-landscape /
    KPZ scaling limit).
  - https://escholarship.org/uc/item/6z03d405 (Hegde, Probabilistic and
    geometric methods in LPP: RSK first-row length = LIS = LPP value; Greene's
    theorem: the top-k-row sum = max weight over k disjoint paths — the exact
    theorem the proposal invokes).
  - https://doi.org/10.48550/arxiv.2510.04713 (Dimitrov–Yang: LPP ↔ Schur
    processes via RSK + Greene/Fomin growth diagrams).
  - claims: rule90-interior-xor, block-lemma (apex = Sierpinski XOR), and the
    refuted rule90-identification-real-absorption-refuted (the boundary is
    nonlinear; Rule-90 governs only the interior).
  The Sierpinski/Pascal-mod-2 structure (Gamelin–Mnatsakanian 2005, fractals of
  Pascal's triangle; the run's rule90-interior-xor) is real, but no source
  connects it to RSK/LPP or to a corner-growth structure whose boundary is a
  {0,2} eroding + regenerating front. The bijection DOSE NOT EXIST in the
  literature and, crucially, the proposal gives no reason to believe the LPP
  front would equal b_k: b_k's evolution is a FREE-BOUNDARY erosion/regeneration
  (step law + recharge identity), not a monotone corner-growth shape where the
  shape's first row and its boundary coincide. RSK first-row length is
  MONOTONE in the input (adding a 1 can only grow the shape); b_k is NOT
  monotone (it drops by 1 every erosion row regardless of pattern). That
  monotonicity mismatch is the structural falsifier: no monotone partition
  shape can equal a strictly-drift-downward b_k that is rescued only by
  boundary (2,4)-events.
killed-by: null (not refuted on the merits, but the bijection is unsupported
  and the proposal itself concedes "it may not exist")
falsifies: >
  The exact minimum that would make this live: a candidate 0–1 matrix whose
  RSK first-row length tracks b_k on the short-block rows k ≤ 40. Because b_k
  decreases by exactly 1 on every non-(2,4) row (step law, proved) and jumps
  up only at (2,4)-events, while an RSK first-row length is monotone in its
  input, the test is decisive: if no candidate input reproduces the strictly-
  decreasing stretches of b_k (which cover all rows that are not the 60
  regeneration rows to depth 1000), the bijection is dead on the definition of
  the object. This is a cheap, concrete, falsifying first step and should be
  run before any LPP theory is invoked.
buy: >
  If the bijection existed, it would deliver a genuine partition-valued
  invariant (immune to the scalar-potential refutation) and put Greene's
  theorem / LPP time constants on the corner. But the burden is entirely on
  establishing the bijection, and the monotonicity mismatch (b_k strictly
  decreases under erosion; RSK first-row length is monotone in the input) makes
  existence doubtful. The cheap first step decides it.
side: regeneration (aims at a new representation of block growth and the record structure of regeneration events; does not touch erosion)
named-mathematics: RSK correspondence, Greene–Kleitman / Greene's theorem, Fomin growth diagrams, last-passage percolation / corner-growth model, KPZ universality, the Sierpinski / Pascal-mod-2 automaton (Rule 90).
speculative: The bijection is NOT established — this is explicitly a bijection hunt, and it may not exist. The value is in the objects it would deliver if it does: a partition-valued invariant of the operator (immune to the scalar-potential refutation (0,0,1,1)→(0,1,0), which only kills real-valued potentials) and a named-theorem route to bound the corner. Fomin growth diagrams and the BCZ helicoid program (already in the library) are the natural precedent to check.
falsifier: If the RSK first-row length fails to track b_k on the short-block rows (k ≤ 40), the specific bijection is dead. If it tracks b_k but the LPP environment turns out to be exactly the all-zero / Eppstein degenerate matrix in the general class, then no LPP time-constant theorem distinguishes the primes, and the approach reduces to the already-refuted non-concentration question.
