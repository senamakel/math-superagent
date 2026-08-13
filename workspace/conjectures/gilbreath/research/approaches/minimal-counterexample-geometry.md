```approach
idea: minimal-counterexample-geometry
mechanism: |
  Instead of proving regeneration always happens (universal), prove that the
  specific triangle configuration that would allow the {0,2} block to shrink to
  length 0 is impossible for any 2-then-odds start.

  The block lemma says: if row k has a leading {0,2} block of length b_k, then
  b_{k+1} ≥ b_k − 1. So to reach b = 0 from b = n requires at least n rows of
  pure erosion (b shrinks by 1 each row with no regeneration). Each erosion
  step consumes one block entry: the value A_{k+d}(b_{k+d}) at the tip of the
  shrinking block determines the next step's block length and second entry.

  Fix the number of consecutive erosion rows to, say, m. What constraints must
  the boundary values satisfy for this to happen? These constraints are a
  system of equations in the initial row entries (the primes or gaps). If we
  can prove this system has NO solution for any m beyond some bound (or for any
  m at all when the starting values come from a sequence with small enough
  gaps), then the block can never reach 0.

  This is different from all three refuted approaches:
  - mod4-pascal: tried linear lift, hit mod-8 obstruction. This approach works
    with the FULL nonlinear operator, not a congruence.
  - backward-automaton: tried local Markov property, refuted (global). This
    approach is about forward constraints on a specific length-m failure
    prefix.
  - rule90-absorption: tried uniform boundary absorption bound, refuted
    (Eppstein). This approach asks a DIFFERENT question: not "does the boundary
    get absorbed" but "what MUST the boundary look like for the block to keep
    shrinking, and is that pattern realizable?"

  The key technical step: for a pure erosion run of length m, the values at the
  shrinking block tip form a backward-difference recurrence. Starting from the
  eventual failure (A_{k+m}(1) = 4 at b = 0), we can reverse-engineer what the
  initial row's entries must have been. If those entries violate the parity
  structure (odd/even pattern) or gap bounds, the erosion run is impossible.

  This is a constraint-satisfaction approach: encode "there exists a 2-then-odds
  sequence with gaps ≤ some bound g that produces m consecutive erosion rows" as
  a SAT/SMT instance. UNSAT for all m beyond some reasonable bound would be a
  theorem: the block can never reach 0. Even UNSAT for m up to some concrete
  number (say m = 100) would be a genuine partial result: the block length can
  never drop below 100 in one erosion run given gap bound g.
status: refuted
killed-by: >
  Refuted on six grounds; see research/notes/minimal-counterexample-geometry-grounding.md.

  (1) The exact reverse-engineering theory is GLOBAL, not a bounded local
  constraint system. Muney 2026 (arXiv:2606.23721) computes the valid-extension
  set by backward preimage steps on the whole right anti-diagonal (reverse-tree,
  Prop. 18); membership is an order-sensitive analogue of Brown's subset-sum
  completeness criterion with weights reaching the whole prefix (Alkan et al.
  2023 factorial K-criterion). A finite SMT encoding is either that global
  criterion (as hard as GC) or a strictly weaker bounded approximation whose
  UNSAT proves nothing about the primes.

  (2) The class-level target statement is FALSE. Eppstein 2011 constructs, for
  ANY unbounded monotone f(n)>=2, a 2-then-odds sequence with gaps <= f(n)
  whose right edge leaves and re-enters the good regime infinitely often —
  i.e. arbitrary-length erosion runs (block up to the row's end without
  regeneration) are realizable from a 2-then-odds start with small gaps. The
  primes can only differ via the unproved CHT non-concentration hypothesis;
  the approach encodes only "2-then-odds + gaps", which is exactly the class
  Eppstein defeats.

  (3) The run's own rows contradict the "tip values form a backward-difference
  recurrence whose reverse-engineering is impossible" premise. Depth-1000 data:
  during erosion the intruder y obeys a ONE-ROW drain rule — y(k+1) = y(k) - 2
  iff the last block entry x(k)=2, else y(k+1)=y(k) — and is monotone
  non-increasing to 4 and sticks; regeneration fires exactly at (x,y)=(2,4);
  101 erosion steps conform with zero failures; genuine intruder-driven erosion
  runs of length 13 occur (k=97..109, 113..124, 147..158) and always end in
  (2,4) regeneration, never at b=0. No A_{k+m}(1)=4 at b=0 failure trajectory
  exists at all in depth 1000 (the 162..999 run is a finite-record
  width-exhaustion artifact, intruder None).

  (4) SAT/CAS counterexample hunting (MATHCHECK, Konev-Lisitsa EDC, Bright) has
  never been applied to Gilbreath, and structurally cannot be: the successful
  applications all have finite/bounded-state properties, while GC's property is
  about an unbounded array with a global extension criterion. Searches found no
  published SAT/SMT attack on GC.

  (5) The block lemma's protection is linear (n+1 rows per length-n block,
  Odlyzko 1993 p.374 + this run's proved re-derivation). "n rows of pure
  erosion to reach 0" is the consumption half; the regeneration half — that the
  boundary keeps re-entering {0,2} before b→0 — is exactly the unproved
  conjecture, reframed not solved.

  (6) CHT 2026 (Thm 1.6, Lemmas 3.7(iii)/3.8): a {0,d}-valued block propagates
  in all descendants and the only obstructions to decay are long zero-blocks /
  long shallow {0,d}-blocks — global length-height obstructions, not pointwise
  tip conditions. No known necessary condition on erosion tip values makes the
  approach's system unsatisfiable; the only exact tip theory (Muney) is global
  and, by Eppstein, satisfiable in the 2-then-odds class for arbitrary m.
precedent: >
  - https://doi.org/10.48550/arXiv.2606.23721 (Muney 2026: reverse-tree,
    valid-extension sets, global Brown-completeness-analogue criterion,
    Prop. 2/12/18, Cor. 3)
  - https://www.mdpi.com/2227-7390/11/18/4006 (Alkan et al. 2023: Gilbreath
    polynomials, factorial-weighted min/max K criterion, GC-implies bound)
  - https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html
    (Eppstein 2011: backward construction, no-regeneration runs of arbitrary
    length in the small-gap 2-then-odds class)
  - https://arxiv.org/abs/2607.08712 (Chase-Hunter-Tao 2026: Thm 1.6
    obstructions = long 0-blocks / long shallow {0,d}-blocks; Lemmas 3.7(iii),
    3.8 {0,d} propagation; unproved non-concentration hypothesis for primes)
  - https://doi.org/10.1090/S0025-5718-1993-1182247-7 + this run's
    research/notes/block_lemma.md (block lemma linear protection, constant 1)
  - MATHCHECK (Zulkoski/Ganesh/Czarnecki, IJCAI 2016) + Konev-Lisitsa (SAT 2014)
    + Bright (CACM 2022): SAT-for-conjectures exists and has never reached GC
holding-claims: larger
  anti-gilbreath-construction, odlyzko-block-lemma-exact, cht-inverse-theorem,
  regeneration-lemma-edge-2-intruder-4-established, valid-extension-nonlocal
falsifies: >
  That a bounded-window SMT system over 2-then-odds gap bounds can be UNSAT for
  all m (or even for m up to a fixed bound with a gap bound valid for ALL
  primes). Eppstein refutes the class-level claim; the run's data refute the
  reverse-difference premise; the global extension criteria refute the bounded
  encoding; and any all-primes gap bound needs the unproved CHT hypothesis.
buy: >
  None as a proof route. The salvageable residue: the run's own exact computed
  regeneration trigger (regen iff boundary (x,y)=(2,4); erosion = one-row drain)
  and Muney's reverse-tree as the correct descriptive tool. Both were already
  captured in regeneration_data.md and the backward-extension thread; the
  approach adds no new leverage.
first-step (retired): >
  Extracting the tip-value constraint system from depth-1000 data already
  succeeded and found a ONE-ROW rule with no backward coupling, satisfiable
  indefinitely (13-row erosion runs occur). Encoding that as SMT and finding
  UNSAT would contradict the run's own data; finding SAT would prove trivially
  what Eppstein already builds. No run of the SMT encoding is justified: the
  constraint system is already characterized and is satisfiable.
```