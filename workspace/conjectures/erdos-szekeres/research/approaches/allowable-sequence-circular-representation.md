```approach
idea: Allowable-sequence (circular sequence) representation of the order type
mechanism: Replace the chirotope/orientation-triple representation with a Goodman–Pollack allowable sequence: a 2-periodic sequence of permutations of the n points in which consecutive permutations differ by reversing a set of increasing blocks, and over one full period every unordered pair is reversed exactly once. A subset in convex position has a well-known clean description here — its elements are swept by a rotating line as a contiguous staircase of reversals within one half-period. The conjecture becomes a purely sequential statement: how many elements can an allowable sequence carry before a convex k-gon (a full k-step staircase) is forced. The Erdős–Szekeres construction is rigid in this representation: the blocks T_i (|T_i| = C(n-2,i)) sit at reversal-"depth" i, so the binomial coefficients are the count of elements at each depth of a staircase with n−2 levels, and the no-convex-n-gon property is the absence of a complete staircase. Induction on the number of moves, or on the subset-of-[n−2]-valued "depth profile" of an element, is the natural place where the exact 2^{n-2} recurrence lives. This is the representation in which the C(n-2,i) are structural, not an accident.
status: refuted
killed-by: Both load-bearing mechanisms adjudicated and refuted on disk
  (`code/out/allseq_adjudicate.captured.txt`, `allseq_axiom_adjudication.captured.txt`,
  VERDICT below). (1) REVERSAL-DEPTH = ES BLOCK INDEX T_i is a STRUCTURAL
  impossibility: every allowable sequence has constant per-point reversal count
  N−1 by the pair-reversal axiom (observed 3,7,15,31 at n=4..7 vs the block
  binomials 1,4,6,4,1 / 1,5,10,10,5,1), so the binomials C(n−2,i) are NEVER
  recovered as a per-point sweep statistic. (2) CONTIGUOUS-BLOCK/STAIRCASE
  CONVEXITY is FALSE in both directions (n=4: 0/1 agree, n=5: 88/163,
  n=6: 62096/64839 — false positives: full set is one contiguous block yet not
  convex; false negatives: convex 4-sets never separable from an interior point
  in one projection). What SURVIVES: the exact circular (allowable) sequence is
  correctly constructible and the Goodman–Pollack axioms hold on es_construct at
  n=4..7 (every one of the N(N−1)/2 events a single adjacent swap or a disjoint
  tied-angle block; the old `[A] replay ok:False` was an encoder run-reversal
  bug — a tied group must be applied as independent pairwise swaps, never a
  reversed merged run); and the correct convexity-from-sequence criterion is
  pointwise extreme-in-projection (p is first-or-last in an S-restricted
  projection order ⟺ p is a hull vertex of conv(S)), which agrees with the exact
  oracle lib/es_geom on every |S|≥4 subset (n=6: 64839/64839). The survivor
  reduces to the classical "convex = all points extreme in their hull" expressed
  in sweep language — it gives no new handle on the block structure. GP80
  definition now sourced on disk (slmath-goodman-pollack-allowable-sequences-
  chapter22). Do NOT re-derive depth=block or contiguous-block convexity.
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

---

## VERDICT (adjudication, `code/out/allseq_adjudicate.py`, capture
`code/out/allseq_adjudicate.captured.txt`) — July 2025

**The depth = block-index conjecture is REFUTED; the contiguous-block convexity
characterization is FALSE as stated; the approach's utility survives only in a
weakened, different form.**

### What was computed (all exact arithmetic, `es_construct` n=4,5,6,7)

1. **Correct circular sequence reconstructed.** Sweep a directed line over the
   point set, record the projection order at every swap; all directions compared
   by exact cross product. Axioms PASS at n=4..7: every unordered pair reversed
   exactly once over the half-period; all C(N,2) events are single adjacent
   swaps (general position: no tied angles). The old `allowable_encoder.py` had
   a replay bug (merged consecutive simultaneous blocks) that made it report
   "[A] replay ok: False" while also "120/120 adjacent" — contradictory; the new
   encoder fixes this by swapping each group's pairs independently.
2. **Reversal depth is constant.** depth(p) = the number of events (swaps)
   involving p over [0,pi) = N−1 for every point (each pair crosses once). At
   n=4..7 this is 3,7,15,31 — constant, while block sizes are the binomials
   C(n−2,i). depth == block index: **FAIL at every n** (e.g. n=6: depth
   {15:16} vs blocks {1,4,6,4,1}). This is a structural impossibility, not a
   placement artifact: *any* allowable sequence has constant per-point reversal
   count N−1 by the pair-reversal axiom.
3. **Contiguous-block convexity is false.** TEST 3 (literal "S in convex
   position ⟺ some projection order has the elements of S contiguous"):
   n=4: 0/1 agree; n=5: 88/163 agree (75 disagreements); n=6: 62096/64839 agree
   (2743 disagreements). Fails in BOTH directions: full-set false positives
   (every full set is one contiguous block yet not convex) and convex 4-sets
   predicted non-convex (elements never separable from an interior point in a
   single projection).
4. **The correct characterization holds.** The proven criterion is: S is convex
   ⟺ every p∈S is a vertex of conv(S) ⟺ p is FIRST **or LAST** in some
   S-restricted projection order (min- or max-extreme along some sweep normal).
   With that criterion: n=5 163/163 PASS, n=6 64839/64839 PASS. So convexity
   IS readable from the sequence, but only pointwise-extreme, not as a block.
   (Note: `allowable_encoder.py`'s old B test used first-or-last over
   permutations but truncated at 5 disagreements, stopping at 3-subsets — every
   ‎3-subset is convex, so "all disagreements are 3-subsets, always convex"
   was an artifact of the early break, not a real signal.)

### Consequences for the approach

- The claimed correspondence "blocks T_i sit at reversal depth i" is false in
  the natural enumeration. The binomial coefficients C(n−2,i) are NOT recovered
  as a per-point sweep statistic of the circular sequence.
- "No convex n-gon = no complete staircase/contiguous block" is not viable in
  the literal sense: convex position is not a contiguous-block property.
- What survives: the exact allowable sequence is correctly constructible and
  convex position is exactly the first-or-last extreme criterion inside it.
  That is real order-type data. But it reduces to the classical statement
  "convex = all points extreme in their hull" expressed in sweep language; it
  gives no new handle on the block structure of `es_construct`.
- **Recommendation: close the depth/staircase induction branch as refuted.**
  The allowable sequence remains correct as a *vocabulary* (it is the standard
  finite encoding of an order type), but no working mechanism for the
  exact 2^{n-2} bound emerges from it. A future attempt should not re-derive
  either the depth=block or the contiguous-block convexity statement.

## AXIOM-INCONSISTENCY RESOLVED (`code/out/allseq_axiom_adjudication.py`,
capture `code/out/allseq_axiom_adjudication.captured.txt`) — tool_builder

The old `allowable_encoder.py`'s contradicting report (`[A] replay ok: False
detail:['non-adjacent swap 11,13', ...]` while `[A] of 120 events, 120 are
single adjacent reversals`) is a **bug in the encoder, not a real axiom
violation**, now pinned to its exact line.

- `es_construct` DOES have tied critical angles: n=6 has 3 tied groups (each
  size 2), n=7 has 11 tied groups (one size 3, ten size 2). These are disjoint
  parallel segments at equal slope in general position (a tied pair sharing an
  endpoint would be collinear, which general position forbids).
- The old `replay()`'s `len(g)>1` branch reverses each maximal RUN of involved
  positions. For a tied group of two disjoint side-by-side pairs `[A,B,C,D]`
  over `(A,B),(C,D)`, run-reversal gives `[D,C,B,A]`; the correct result is
  `[B,A,D,C]` (swap each pair independently). The run-reversal corrupts the
  running permutation, so the later `non-adjacent swap 11,13 / 11,12 / 2,4`
  reports (n=6) and `12,21 / 10,19 / 12,22` (n=7) are artifacts of the
  corrupted state, NOT axiom failures.
- The separate tally in the same file swapped each event's pair independently
  and correctly reported every event adjacent (120/120, 496/496); it was the
  truthful path.
- The adjudicator's corrected per-pair replay (`allseq_adjudicate.py` TEST 1)
  confirms the Goodman-Pollack axioms hold on `es_construct` at n=4..7: every
  one of the N(N-1)/2 events is a single adjacent swap (or a disjoint block of
  adjacent swaps at a tied angle), zero non-adjacent.

**Fix / moral:** a multi-event tied group must be applied as independent
adjacent pairwise swaps, never as a reversed merged run. The corrected replay
is what allseq_adjudicate.py TEST 1 uses and passes. This does not revive the
(refuted) depth=block or contiguous-block mechanisms; it only clears the
encoder's own self-check so the sequence is trustworthy as the vocabulary.
Items (1) [axioms — resolved: encoder bug], (2) [depth=block — refuted], and
(3) [convexity-from-sequence — extreme-in-projection survives] of task
`allowable-sequence-continue` are now all adjudicated.
