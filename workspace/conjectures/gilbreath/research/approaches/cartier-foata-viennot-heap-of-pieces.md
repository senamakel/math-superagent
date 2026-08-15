# Cartier–Foata / Viennot heap of pieces

```approach
idea: |
  Model the *nonlinearity* of the Gilbreath operator — the min-branch — as a
  heap of pieces in a partially commutative (trace) monoid, in the sense of
  Cartier–Foata and Viennot. The forward dependency DAG of the triangle is
  LOCAL (cell (k,i) depends only on its two parents (k−1,i),(k−1,i+1)), so
  the min-branch choices form a genuine heap over a line graph, and the
  second column A_k(1) becomes a statistic of that heap. Regeneration is then
  a statement about the combinatorial class of the heap in the trace monoid,
  attackable with transfer-matrix / Cartier–Foata-normal-form machinery.
mechanism: |
  Write the nonlinear cell map as
      A_{k+1}(i) = A_k(i) + A_k(i+1) − 2·min(A_k(i), A_k(i+1)).
  The only non-linear datum is WHICH parent is smaller (the min-branch), i.e.
  the sign of A_k(i+1) − A_k(i). A cell therefore "uses" the comparison of its
  two parents. Two cells whose comparison data are independent COMMUTE; the
  dependency structure is a directed acyclic graph (the comparison DAG), and
  an order ideal of this DAG is exactly a *heap of pieces* in a trace monoid
  (Cartier–Foata 1969; Viennot 1986; Diekert's "Combinatorics on Traces").

  Crucially, in the FORWARD direction the DAG is two-parent local: piece (k,i)
  covers exactly (k−1,i) and (k−1,i+1). This is the opposite of the
  backward-extension situation (where the run proved valid-extension criteria
  are GLOBAL, refuting backward-extension-automaton): forward, locality is
  exact. So the heap is a finite-type, line-indexed object, and its growth
  along the left edge is governed by a transfer matrix on piece types.

  The value A_k(1) is a signed linear combination of the top row A_0 with
  coefficients given by ±1's along the min-branch choices — i.e. by the heap's
  Cartier–Foata normal form (the canonical representative of the heap in the
  trace monoid). The conjecture A_k(1) ∈ {0,2} says: the leftmost column never
  accumulates excess under this signed heap evaluation. The step law /
  regeneration event (edge,intruder)=(2,4) should then be a recognisable
  *topological* transition of the heap (e.g. the left column piece changing
  commutation class, or a "pyramid" piece being completed), which is the
  missing regeneration mechanism the scalar-potential approaches could not see.

  Named machinery available: Cartier–Foata normal form and the Möbius
  function of the trace monoid (a genuine invariant); Viennot's heap
  enumeration by transfer matrices (used for directed animals and hard-core
  models on line-indexed heaps); the "pyramid" and "zigzag" commutation
  classes that give closed-form heap generating functions.
status: refuted
killed-by: |
  A_k(1) is NOT a trace-monoid statistic: under a fixed min-branch sign
  pattern (the heap), the evolution is linear, A_k(1) = Σ c_j A_0(n+j), so
  changing top-row magnitudes with the heap held fixed changes A_k(1). The
  heap carries the sign/comparison pattern, not the magnitude difference
  that decides membership of A_k(1) in {0,2}. This is the candidate's own
  falsifier (b), violated by first principles — the same magnitude-blindness
  that refuted comparison-order-cell-automaton and sign-coherence. The local
  two-parent DAG fact is real but is bookkeeping, not a mechanism.
side: general-class / combinatorial (regeneration side; no prime distribution)
named-mathematics: |
  Cartier–Foata normal form and the partially commutative (trace) monoid
  (Cartier & Foata 1969, "Problèmes combinatoires de commutation et
  réarrangements"); Viennot's heaps of pieces (1986); Diekert,
  "Combinatorics on Traces" (LNCS 454, 1990); Möbius function of a trace
  monoid; transfer matrices for line-indexed heaps.
speculative: |
  High. The heap object is real and local, but the load-bearing claim — that
  the regeneration event is a recognisable *commutation-class* transition
  whose recurrence is forced by the heap's transfer matrix — is conjectural.
  The honest risk is that the signed evaluation A_k(1) is not a
  trace-monoid invariant (it may depend on more than the heap's class), in
  which case the heap is a bookkeeping device, not a mechanism. This is NOT
  borrow-young-diagram (refuted there because Diaconis–Fulman carries belong
  to addition while min is a subtraction borrow, and because the min-branch
  site set was claimed to be a Young diagram): here the object is a *heap /
  trace monoid element*, a different structure with different invariants.
falsifier: |
  (a) Compute the min-branch DAG on real depth-1000 rows; if a cell's
      min-branch depends on anything beyond its two parents (non-local), the
      heap premise fails. (b) If two different heap classes give the same
      A_k(1) for all top rows, A_k(1) is not a trace-monoid statistic and the
      invariant is not carried by the heap. (c) If the regeneration event does
      NOT correspond to a change in commutation class (constant class across
      a (2,4)-event), the topological mechanism is absent.
first-step: |
  tool_builder (O(depth × width), one row live; report depth and width):
  from blocks_depth1000.json reconstruct, for every cell (k,i), the
  min-branch sign s(k,i) = sign(A_{k−1}(i+1) − A_{k−1}(i)) and build the
  comparison DAG (each node ← two parents). (1) Verify locality: each node's
  parents are exactly (k−1,i),(k−1,i+1). (2) Compute the trace-monoid
  commutation: two nodes commute iff their dependency cones are disjoint;
  emit the commutation graph. (3) Extract the Cartier–Foata normal form of
  the heap at each row and check whether A_k(1) is a function of that normal
  form alone. (4) Across every (2,4)-event in the record, record the
  commutation class of the left column before and after; report whether the
  class changes. CONFIRMED/REFUTED with exact counts — never "theorem".
```

## Grounding (research cycle)

**The named mathematics is real.** Viennot's heaps of pieces (1986, LNCS "Heaps of pieces, I", doi:10.1007/BFb0072524) are a visualization of the Cartier–Foata partially commutative (trace) monoid (Cartier & Foata 1969, LNCS 85, doi:10.1007/BFb0079468); Krattenthaler (2014, "The theory of heaps and the Cartier–Foata monoid", citeseerx 10.1.1.406.4016) proves heaps ⟺ trace-monoid elements; Viennot-type heaps are enumerated by transfer matrices on line-indexed heaps and have been applied to directed animals, parallelogram polyominoes (Bousquet-Mélou), Motzkin paths, orthogonal polynomials, Rogers–Ramanujan and fully-commutative elements in Coxeter groups (Shigechi 2024, arXiv:2401.12701; Chao–Macauley 2019, toric heaps). The Möbius function of the trace monoid is a genuine invariant; trace-monoid generating series are rational (Krob–Mairesse–Michos 2001, arXiv:cs/0112012).

**Not applied to Gilbreath anywhere searchable.** Searches for (trace monoid / heap / partial commutativity / commutation class) + (absolute difference / Gilbreath / iterated differences) return only trace-monoid combinatorics, never the Gilbreath operator. There is no precedent to cite; this is an original (if speculative) reframing.

**Status: refuted on its own falsifier (b), by first principles; the local-DAG half survives as a bookkeeping device only.**
- The heap DAG of the min-branch sign pattern IS two-parent local by construction (a genuine fact, and the honest half of the candidate).
- But A_k(1) is NOT a trace-monoid statistic. Under a FIXED min-branch sign pattern σ (the heap), the row evolution is linear: A_k(1) = Σ_{j} c_{k,j} A_0(n+j) with coefficients ±1 determined by σ. Changing the top-row MAGNITUDES with σ held fixed changes A_k(1) while leaving the heap (sign pattern) unchanged. So two different top rows give different A_k(1) for the same heap class — the candidate's own falsifier (b) is violated: the value is not a function of the heap alone. This is the same magnitude-blindness that killed the comparison-order and sign-coherence approaches: the sign/comparison word does not carry the values that decide {0,2}.
- Hence the conclusion "regeneration = commutation-class transition" cannot be read off the heap; the heap encodes only which parent was smaller, not how different — and the second entry's membership in {0,2} is decided by a magnitude inequality (|Δ| ≤ 2), not by sign pattern.
- Vertdict: refuted, on the candidate's own falsifier (b), by a two-top-row magnitude argument with a shared heap; the transfer-matrix enumeration machinery, while real, would be counting a structure that does not carry the invariant.
- claim-ids: fwd-diff-identity-refuted (magnitude not determined by sign), comparison-order-cellular-automaton (refuted: scale-invariance), fenchel-duality-sign-assignment-refuted (reachable sign sets do not fix the value).

## Why this is not on disk

- **Not `borrow-young-diagram-partition-invariant`** (refuted): that entry
  claimed the min-branch *sites* form a Young diagram and imported the
  Diaconis–Fulman carry dictionary; it was refuted because carries belong to
  addition while min is a subtraction borrow. This entry makes no Young-diagram
  claim and uses a *trace monoid / heap* structure (Cartier–Foata, Viennot),
  whose invariants (normal form, Möbius function) are different objects.
- **Not `backward-extension-automaton`** (refuted): that entry studied backward
  extension, which the run proved is GLOBAL. This entry studies the FORWARD
  dependency DAG, which is two-parent local by construction — the two
  directions have opposite locality properties, and this exploits the local
  one.
- **Not `binary-carry-transducer-automatic-sequence`** (refuted): that entry
  required the *input* (primes) to be automatic. Here the heap is built from
  the *comparison* structure only; no assumption on the automaticity of the
  top row is made.
