# Approach: triangle-graph C3 pinned-spectrum obstruction for the n3 seed

```approach
idea: Attack a putative srg(99,14,1,2) Gamma through its TRIANGLE GRAPH C3(Gamma)
  — vertices = the 231 triangles, edges = triangles sharing a vertex — rather
  than through Gamma. C3 has a pinned spectrum forced by the parameters alone:
  N^T N = 3I + C3 where N is the 99x231 point-triangle incidence matrix, and
  NN^T = 7I + A has eigenvalues 21, 10^54, 3^44 (since A has 14,3^54,-4^44), so
  C3 = 3I+N^TN -3I... precisely C3 has eigenvalues 18^1, 7^54, 0^176 (231-99=132
  zero eigenvalues added to the 44 already forced). The n3 seed — two DISJOINT
  point-triangles T1,T2 joined by exactly two point-edges (the n3≥1 case that
  G-n3-zero leaves open) — is a 2-vertex pattern in C3 whose C3-neighbourhood
  relation is fully pinned by lambda=1, mu=2. The claim: a C3 that (i) is
  18-regular with spectrum 18^1,7^54,0^176 and (ii) contains the seed as a
  twin-triangle pattern with its forced co-neighbour count, is spectrally and
  combinatorially over-determined, and the over-determination is k=14-specific
  because the pinned numbers (18,7,0 with 0-multiplicity 176) differ from the
  BvLS control's pinned numbers. This is NOT the refuted whole-graph eigenvalue
  route (9 and 243 pass the whole spectrum): it lives in C3's pinned spectrum,
  which genuinely separates 99 from the controls.
mechanism: Lambda=1 says two adjacent vertices of Gamma share exactly one common
  neighbour, which in the partial-STS triangle geometry (231 lines of size 3, 7
  per point) means every pair of points on a common line is collinear exactly
  once — so Gamma is the collinearity graph of the partial STS. Two triangles
  share a vertex iff they are C3-adjacent; they are disjoint iff not C3-adjacent.
  The n3 seed (disjoint triangles, exactly 2 cross edges) therefore pins a
  specific induced-pair configuration in C3. From the fixed degrees and the
  C3 local profile (Keramatipour claim: every two adjacent C3-vertices share
  (3k-6)/2 = 18 neighbours, and two adjacent triangles share k/2-2 = 5 common
  point-neighbours), the seed's forced C3-neighbourhood sizes become exact
  integers. Counting vertices at specified C3-distance from the seed and forcing
  the 18-regularity + co-neighbour profile against the 0-eigenspace multiplicity
  176 gives a finite, exact, over-determined system. A fractional forced
  multiplicity, or an induced substructure whose count cannot be folded into the
  pinned multiplicities, is the k=14-specific contradiction. The admissibility
  gate (must not kill 9/243): C3(rook(3)) = K_{3,3} (spectrum 3,-1^4,3... ) and
  C3(BvLS) have DIFFERENT pinned spectra (BvLS: NN^T = 22I+A, A eigen 22,4,-5 =>
  NN^T eigen 44,26^?,17^?; C3 eigen 40,23,14,0's), so the 99-specific pinned
  numbers (18,7,0^176) cannot be shared with 243 — the argument can hold at 99
  without refuting either control.
status: refuted
killed-by: The pinned spectrum claim is (a) computed WRONG and (b) parameter-determined
  either way. (a) The verified triangle-graph spectrum for a 99-graph is
  {18:1, 7:54, 0:44, -3:132} (c3_spectrum_exact_verify.captured.txt) — the 0
  multiplicity is 44, NOT the 176 the candidate asserted (it mis-merged the 132
  zero-vectors into the 0 eigenspace; they are the -3 eigenvalue, which for 99
  does not collide because st=0). (b) Even corrected, the spectrum is fixed by
  the family closed form rt=(u-1)(u+4)/2, st=(u-3)(u+2)/2 and holds identically
  for every family member: BvLS(243) realizes its own forced C3 spectrum exactly
  ({-3:648, 3:110, 12:132, 30:1} verified). So the C3 pinned spectrum carries the
  same separating-power failure as the refuted whole-graph eigenvalue, incidence
  p-rank, SNF and MacWilliams routes — 9 and 243 both realize their forced
  values, so a C3-spectral argument cannot distinguish 99. The large -3/0
  eigenspaces (132+44 of 231) make subgraph counts MORE flexible at 99, not less,
  exactly the concern the inventor flagged. Separating power must come from
  something the parameters do NOT determine, which this candidate does not supply.
first-step: (1) Compute C3(rook(3)) and C3(bvls_graph()) exactly with
  lib.triangles.triangle_graph and verify the pinned spectra including
  0-multiplicity (confirm 0-eigenvalue algebraic multiplicity 176 at 99's
  parameter set by the Jordan/rank argument on N^TN). (2) Derive the exact
  C3-neighbourhood sizes of the seed pair under lambda=1,mu=2 (how many
  C3-vertices at distance 1 and 2 from the seed, and the 5-common-neighbour
  relation). (3) Treat the forced C3-neighbourhood census + 18-regularity +
  pinned eigenvalue multiplicities as an exact linear-arithmetic system; check
  integrality and whether the census over-subscribes the 0-eigenspace. Gate:
  run the SAME census on BvLS's triangle graph and require it to be consistent,
  before believing any 99-empty result.
```

## Notes (inventor)

The distinct object from every closed line: interlacing-84 (refuted) worked in
the whole-graph spectrum of the 84-vertex outer subgraph; this works in the
*pinned spectrum of the triangle graph*, a different host with different
numeric content (3-eigenvalue 7, 0-multiplicity 176) whose values separate 99
from 243. Not the incidence p-rank/SNF line (that is N's p-rank, already
grounded); this is C3's spectrum. Speculative: the 0-eigenspace has enormous
multiplicity (176/231) which usually makes a graph *more* flexible about
subgraph counts, not less, so the separating power must be pinned down by the
exact 18-regular co-neighbour census before it is believed.
