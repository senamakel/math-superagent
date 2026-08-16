# Read-cone / column-influence bound: sparse ⇒ sublinear, an attack on SUPPLY ⇔ switch density

```approach
idea: >
  Attack the open converse lemma `G-sup-implies-switch` (research/backward/
  supply-switch-equivalence.md) — "h of zero switch density forces
  liminf ν₂(n)/n = 0" — not by searching for witnesses but by a single exact
  column bound on the fold. Coordinate j of h can be read by the fold only
  through its READ-CONE C_j(n) = { d ∈ [2,n−1] : (d − (n−1−j)) ⊆ d } (a
  submask condition). Since a cell T(n,d) is 1 only if an odd number of the
  h[j]=1 coordinates in its column set are read, the total number of odd cells
  is at most the total number of (coordinate, cell) incidences:

      ν₂(n) = wt(Φ_n h) ≤ Σ_{j=0}^{n−1} h[j] · |C_j(n)|.

  With r = n−1−j (distance from the read boundary) the cone has the exact
  description { r + s : s ⊆ ¬r } ∩ [2, n−1], so |C_j(n)| ≈ n / 2^{popcount(r)}
  for large n: a 1 at position j feeds O(n/2^{popcount(n−1−j)}) cells. The
  boundary position j = n−1 (r = 0) feeds all n−2 cells — this is the known
  single-spike amplification (e_{n−1}, sparse-fold-capacity). Every other
  position feeds exponentially fewer cells in popcount(distance).
  Consequently a density-0 string can make ν₂ linear at n only if its 1s sit
  at positions j with popcount(n−1−j) = O(1) — a rigid "dyadic alignment"
  condition on the support. The precise target for the converse lemma
  G-sup-implies-switch is the LIMINF form: since ν₂(n) ≤ n·Σ_{j∈S,j≤n−1}
  2^{−popcount(n−1−j)}, it suffices to show that for every density-0 set S
  the weighted sum W_S(n) = Σ_{j∈S,j≤n−1} 2^{−popcount(n−1−j)} is o(1) along
  infinitely many n. Sanity check (already consistent with the disk): for
  S = powers of 2, W_S(n) = Ω(1) at n = 2^m+1 (the j = 2^m term has weight 1,
  matching the measured ratio ~2/3 there) but W_S(2^m) = m·2^{−m+1} = o(1),
  which is exactly why that string has liminf 0. So the crux is NOT
  "W_S = o(1) on a density-1 set of n" (false) but "inf along a cofinal
  subsequence is 0" (the right statement). Proving this for every sparse S
  proves SUPPLY ⇔ switch density (GOAL priority 3, result 5); a sparse S
  with W_S(n) = Ω(1) for ALL large n is a concrete growing witness refuting
  the equivalence.
mechanism: >
  (1) The column inequality is exact and is the natural generalisation of the
  on-disk claim `fixed-single-1-fold-weight-bounded-by-j` (the e_j case) to an
  arbitrary support: ν₂ counts odd cells, odd cells need a 1-incidence, and
  the total incidence count is Σ_j h[j]·|C_j(n)|. Named home: the INFLUENCE of
  a coordinate in a Boolean function (wt(f) ≤ Inf_total(f) for the specific
  monotone map f = indicator of odd column parity), and the Sierpinski READ-
  CONE, which is the geometric object making the influence computable.
  (2) The cone formula |C_j(n)| ≈ n / 2^{popcount(n−1−j)} converts the problem
  into a pure additive/dyadic question about a FIXED sparse set S ⊆ N:

      is  Σ_{j∈S, j≤n−1} 2^{−popcount(n−1−j)}  = Ω(1)
      on a positive-density set of n?

  This is a measure-theoretic statement about the transformation n ↦ n−1
  composed with the popcount weight on Z (a "popcount-weighted Furstenberg"
  average over the sparse set S), and is attackable by classical ergodic
  dichotomy methods — NOT by the refuted Furstenberg measure-rigidity route,
  which was about the collapse of ×2-invariant inputs; this is about the
  weighted density of a support along the shift.
  (3) Two clean endpoints: (a) if inf_n W_S(n) = 0 (equivalently
  liminf ν₂(n)/n = 0) for every sparse S, then G-sup-sw holds and
  SUPPLY ⇔ SWITCH, a genuine negative closure theorem; (b) if some sparse S
  achieves W_S(n) = Ω(1) for ALL large n, that S is an explicit
  growing witness proving the equivalence FALSE — the witness shape the
  sparse-fold-capacity thread showed cannot be a fixed finite string.
status: grounded
precedent: >
  The column/influence bound is standard Boolean-function analysis: wt(f) ≤ total
  influence Inf_total(f), with the coordinate influence lower-bound tradition of
  Kahn–Kalai–Linial (FOCS 1988; combinatorial proof in *Edge-Isoperimetric
  Inequalities and Influences*, Combin. Probab. Comput.) — the fold's read-cone is
  its Sierpinski/Pascal-mod-2 read structure (Callan, *Sierpinski's triangle and the
  Prouhet–Thue–Morse word*, arXiv:math/0610932, Thms 1–2: the inverse Pascal mod-2
  matrix is Thue–Morse-valued; digital down-set identity). In-workspace:
  supply-fold-submask-zeta-involution, g-run-telescope-verified,
  fixed-single-1-fold-weight-bounded-by-j. The decisive crux (inf_n W_S(n)=0 for
  every density-0 S, with W_S(n)=Σ_{j∈S}2^{−popcount(n−1−j)}) is NOT a named or
  proved theorem in either direction — a genuinely open popcount-weighted dyadic
  question; no source found proves or refutes it, and a finite SAT/ILP check can
  settle the pattern. Grounding: research/grounding_three_current_candidates.md §1.
first-step: >
  tool_builder, exact integer/F₂ arithmetic, no number theory beyond the row
  set: (1) machine-verify the cone description and the column bound —
  for n ≤ 200 and every h in a small random sample plus the known witnesses,
  assert wt(Φ_n h) ≤ Σ_j h[j]·|C_j(n)| against the brute submask-XOR oracle,
  and assert |C_j(n)| = |{d∈[2,n−1] : (d−(n−1−j))⊆d}| exactly (independent
  route). (2) For S = powers of 2, squares, and balanced anti-dyadic supports,
  compute A_N = (1/N)·#{ n ≤ N : Σ_{j∈S,j≤n−1} 2^{−popcount(n−1−j)} ≥ c } for
  c = 0.05 and confirm it → 0 (this is why those strings have liminf 0).
  (3) The decisive hunt: search (SAT/ILP, n up to 64) for a sparse set S with
  wt(S ∩ [0,n−1]) = o(n) whose weighted sum stays ≥ c for ALL n in a long
  range — UNSAT across a grid of sparsity/c thresholds is evidence for (a),
  one SAT witness is the counterexample for (b). FALSIFIER: if (1) fails the
  column bound is wrong; if (3) finds a witness, G-sup-sw is false and the
  equivalence is refuted — record the witness as a claim.
falsifies: >
  (a) the column bound fails against the oracle (then the cone description is
  wrong, a pure bookkeeping defect); (b) a sparse S is found whose weighted
  sum stays bounded below on a long range (then SUPPLY is strictly weaker than
  switch density, GOAL priority 4 is the live direction, and the witness is
  the first explicit one); (c) the weighted sum can be made Ω(1) only by
  supports of positive density (then the equivalence theorem is on its way to
  a proof).
```
