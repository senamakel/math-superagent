```approach
idea: Allowable-sequence (circular sequence) representation of the order type
mechanism: Replace the chirotope/orientation-triple representation with a Goodman–Pollack allowable sequence: a 2-periodic sequence of permutations of the n points in which consecutive permutations differ by reversing a set of increasing blocks, and over one full period every unordered pair is reversed exactly once. A subset in convex position has a well-known clean description here — its elements are swept by a rotating line as a contiguous staircase of reversals within one half-period. The conjecture becomes a purely sequential statement: how many elements can an allowable sequence carry before a convex k-gon (a full k-step staircase) is forced. The Erdős–Szekeres construction is rigid in this representation: the blocks T_i (|T_i| = C(n-2,i)) sit at reversal-"depth" i, so the binomial coefficients are the count of elements at each depth of a staircase with n−2 levels, and the no-convex-n-gon property is the absence of a complete staircase. Induction on the number of moves, or on the subset-of-[n−2]-valued "depth profile" of an element, is the natural place where the exact 2^{n-2} recurrence lives. This is the representation in which the C(n-2,i) are structural, not an accident.
status: adopted
precedent: >
  The representation itself is standard and well-attested. Goodman & Pollack, "On the
  combinatorial classification of nondegenerate configurations in the plane" (JCTA 1980,
  doi:10.1016/0097-3165(80)90011-4) introduce the circular/allowable sequence precisely as
  the convexity-appropriate invariant of a planar configuration, and show it encodes convex
  position. The convex-subset-as-contiguous-reversal/staircase description is the standard
  furniture of the theory: see Abello–Eğecioğlu–Kumar (Discrete Comput. Geom. 14 (1995),
  doi:10.1007/bf02570710), which identifies circular sequences with maximal chains in the
  weak Bruhat order and encodes convexity via balanced tableaux; and Dobbins–Holmsen–Hubard,
  "The Erdős–Szekeres problem for non-crossing convex sets" (Mathematika 60 (2014) 463–484,
  arXiv:1305.2266), which uses the allowable-sequence duality to convexity-type results. The
  signotope formulation (pseudoline arrangements) is the same object — claim
  `signotope-rank3-pseudoline-correspondence` (Felsner–Weil 2001,
  doi:10.1016/S0166-218X(00)00232-8) — so this route and the record's SAT/signotope arm share
  their combinatorial backbone. TWO CAVEATS: (1) Hoffmann & Merckx, "A universality theorem
  for allowable sequences" (arXiv:1801.05992) show deciding realizability of an allowable
  sequence is ∃ℝ-complete — identical to the order-type trap, so an upper bound proved over
  ALL abstract allowable sequences would be stronger than the conjecture and may be false; the
  ES construction must be realized explicitly. (2) No published proof of the ES UPPER bound
  goes through allowable sequences; the literature uses them for k-set / pseudoline /
  convexity classification, not for the exact bound. So the representation and the
  convexity-staircase characterization are established, but the specific induction over the
  depth profile delivering exactly 2^{n-2} is novel and unproved — grounded as a
  reformulation, not as a proof.
first-step: (tool_builder, today) Write `code/out/allowable_encoder.py`: given an exact point set, produce its allowable sequence by sweeping a directed line and recording the permutation of points by projection; assign each point its reversal-depth (the number of times it is reversed with a point of the opposite side before the staircase completes). Then run it on the verified `es_construct` set at n=5,6,7 and check, against `es_construct.es_set_blocks`, whether the points of reversal-depth i are exactly block T_i (sizes C(n-2,i)). CRITICAL FALSIFIABILITY (lesson of the layer-profile refutation): the same depth statistic must be recomputed on a DIFFERENT realization of the same order type (permute the blocks' arc positions or use a small continuous perturbation) — if depth changes under a realization-preserving move, depth is a placement artifact like the onion layer, and the approach is refuted on arrival. Only if depth = block index in every realization of the same order type does it carry order-type structure. Then state and machine-check "convex k-subset ⟺ k-step contiguous staircase reversal" against the exact oracle `es_geom`. NOTE: signotopes (Felsner–Weil) are the same objects as pseudoline arrangements, but the new mechanism here is the depth/staircase induction over the sequence, not SAT over signotope variables.
```

## Literature report — allowable-sequence / circular representation

**What the reformulation is called.** The *allowable sequence* (or *circular sequence*)
of permutations, introduced by Goodman & Pollack (1980). It is the standard
convexity-appropriate invariant of an order type; convex subsets are described by a
contiguous block / staircase of reversals within a half-period.

**Precise statements found.**
- Goodman–Pollack 1980: each nondegenerate planar configuration of n points has an
  associated 2-periodic sequence of permutations of {1..n}, where consecutive terms are
  obtained by a sequence of adjacent reversals and each unordered pair is reversed exactly
  once per period; convexity questions are encoded by it. The paper classifies n=3,4,5
  (1, 2, 19 classes) and shows Perrin's claim that every allowable sequence is realizable
  is false (counterexample at n=5). doi:10.1016/0097-3165(80)90011-4.
- Felsner–Weil 2001: rank-3 signotopes (sign maps on triples) are in bijection with simple
  pseudoline arrangements with a fixed top cell. This makes the allowable-sequence route the
  same combinatorial object as the record's existing signotope/SAT arm.
  doi:10.1016/S0166-218X(00)00232-8; claim `signotope-rank3-pseudoline-correspondence`.
- Hoffmann–Merckx 2018: realizability of an allowable sequence is ∃ℝ-complete
  (arXiv:1801.05992). This is the analogue of the order-type realizability trap and binds
  the approach: any result over abstract allowable sequences must be checked for
  realizable witnesses before it counts against the geometric conjecture.
- Dobbins–Holmsen–Hubard 2014 (arXiv:1305.2266, Mathematika 60:463–484): use the
  allowable-sequence / pseudoline duality to carry the ES problem to non-crossing convex
  bodies and generalized configurations, improving convex-body upper bounds (h1(n) ≤
  2^{O(n² log n)}), positive-fraction and partitioned variants. Shows the allowable-sequence
  machinery is used for convexity-type results but never to settle the exact point-set bound.

**Has anyone applied it to THIS problem?** The representation has been applied to
convexity *classification* and to *generalized/body* ES-type bounds, but no published
upper bound for the exact point-set conjecture ES(n) ≤ 2^{n-2}+1 is obtained via the
allowable sequence. The crucially novel step — an induction on the per-element depth
profile that yields exactly the 2^{n-2} binomial row — has no precedent found.

**What it would buy.** A representation in which the binomial coefficients C(n-2,i) are
structural (the ES block sizes = reversal depths), turning the obstruction (no convex
n-gon = no complete staircase) into a purely sequential/permutation claim that avoids
the cups/caps counting slack. It is a genuine reformulation, but the literature provides
the vocabulary and the convexity characterization, not a proof of the bound.

**Verdict: grounded** as a reformulation on established structure; the specific induction
is new and unproved. The ∃ℝ-completeness caveat must be respected (realize everything).
