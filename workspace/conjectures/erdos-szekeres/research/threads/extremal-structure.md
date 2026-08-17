# Structural constraints on a hypothetical extremal set

The run's core structural question: what must a set X of 2^{n-2} points in general position
with NO convex n-gon look like? This thread collects the constraints the library already
establishes, so a structural lemma does not re-derive what is on disk.

```thread
question: What local/global structure is a 2^{n-2}-point set with no convex n-gon forced into, and how close must it be to the ES construction?
status: open
rests-on: es61-lower-bound, es35-cups-caps-bound, ms-cups-caps-tight, baek-balko-split, baek-balko-decomposable, damasdi-saturation, ps-es6, ms-toth-valtr-bound, smqh-no-realizable-4fold-32-no7gon
blocked-by: a structural (stability/uniqueness) theorem does not yet exist; counting methods are proved insufficient (ms-cups-caps-tight shows the loss is in the cups/caps dimension, not the lemma)
next: CURRENT (directive 22) — pattern_finder STANDING RULE: no more spectra of es_construct. No further k-subset convex spectra, no OEIS lookups on numbers off this placement, no n=8 extensions of any template quantity. The 09:58-10:06 convex-subset-spectrum round (code/out/convex_spectrum*) was directive 21's prohibition carried out then filed; it is closed/not to be extended. A pattern counts only if the quantity is defined for EVERY n-avoiding set of size 2^{n-2} and is computable on two non-isomorphic n-avoiding sets and compared (e.g. the known 32-point record set vs es_construct at the same N, or an order-type invariant that survives re-realization). If a quantity cannot be computed on a second set, it is a coordinate, not a pattern — do not file it. Live work remains the two queued tasks: (1) `lift-or-declare-strongest-template-fact` — state the strongest surviving template fact (the (n-1)-convex block-shape classification) over EVERY n-avoiding set of size 2^{n-2} (perturb es_construct off the corridor, the 32-point record set, any realizable order type) or declare it template-only and stop; (2) `nullstellensatz-grid-first-target`. Both must avoid re-describing es_construct. (Prior directive-21 text below retained for the record.)
next-old: CURRENT (directive 21) — stop mapping this template; the four descriptive es_construct
claims (bijection, pattern-classes, corner-pairs, goodness) are placement facts closed or
declared template-only. The live work is (1) task `lift-or-declare-strongest-template-fact`:
state the strongest surviving template fact (the (n-1)-convex block-shape classification)
quantified over EVERY n-avoiding set of size 2^{n-2}, and hunt a violating set (perturb
es_construct off the corridor, the 32-point record set, any realizable order type) — or
declare it template-only and stop — and (2) task `nullstellensatz-grid-first-target`: the
Nullstellensatz/Alon-Furedi Boolean-cube idea, the smallest n where the polynomial
criterion can be written and checked exactly with the degree bound stated. The cut-family
question (task `evenodd-cutfamily-which-family-realizes`) is dropped by directive 21:
single open half-planes give 4/2/0 at n=5/6/7, double-wedge gives 27 valid splits at n=7
but NOT the even/odd one — the single-line induction fails on this template at n=7, and
mapping more cut families on one placement does not move the upper bound. The even/odd block bipartition is a side-intersection at n=5,6 but NEITHER a side nor a
side-intersection at n=7, though both halves stay 6-avoiding — a settled fact, not a live
open question (directive 21 drops the "which cut family" hunt as template-mapping; do not
re-open it). ADJACENT-PROBLEM WATCH (directive 17): Horton sets and empty convex polygons
are the EMPTY-hexagon problem (H(6)=30, Heule-Scheucher) — adjacent per ROOT.md §5.4, NOT
progress toward ES(n). Do not spend calls there without a stated reduction back. Standing
settled layer lemma: outer layer of X_n has size n−1 (3,4,5,6), each layer (n−1)-avoiding,
sizes sum to 2^{n-2}. The allowable-sequence line is closed dead (steer 13, task
`allowable-sequence-continue` dropped). Do not restate the structural question as a search;
attack one precise lemma at a time and record the outcome.
```

## What the library already pins down

- **The extremal object exists**: the ES 1961 construction is a 2^{n-2}-set with no convex
  n-gon (`es61-lower-bound`), saturated (`damasdi-saturation`). But Damásdi et al. also build
  saturated sets of only (7/8)·2^{n-2} for n≥7 — so saturation alone does NOT force size 2^{n-2}
  or near-decomposability.
- **Counting is provably lossy**: f(k,l)=C(k+l-4,k-2)+1 is tight (`ms-cups-caps-tight`), so the
  4^n bound loses entirely in the reduction to cups/caps. An exact 2^{n-2} bound needs a
  stability/uniqueness argument, not more counting.
- **Relaxed exact threshold is right (split threshold PROVED, decomposable asserted)**:
  split-k-gon threshold is exactly 2^{k-2}+1 and ES holds for decomposable sets
  (`baek-balko-split`, `baek-balko-decomposable`) — the strongest current evidence the
  2^{k-2}+1 constant is the correct one, and a concrete route: force convex position
  from a split k-gon plus structure, or show extremal sets are near-decomposable.
  STATUS UPDATE: the full SoCG 2025 PDF is now held and digested
  (`research/summaries/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md`) —
  `baek-balko-split` (Theorems 3/4/6, the split + abstract-hypergraph thresholds) is
  proved-in-source; `baek-balko-decomposable` (Theorem 8) stays asserted-by-source
  ("The proof of Theorem 8 is omitted" in the SoCG version, deferred to JCTA 2026).
  Treat the decomposable claim as load-bearing-but-unverified until the JCTA 2026
  full text is fetched; the split threshold is verified on disk.
- **The 4-set convexity criterion** (`es35-four-criterion`) reduces "no convex n-gon" to a
  finite local (4-set) condition — the handle the SAT encodings and any finite-constraint
  structural lemma use.
- **n=6 verified**: ES(6)=17 (`ps-es6`); the Peters–Szekeres encoding + cost is the oracle and
  n=7 budget model.
- **n=7 frontier**: Dumitru's SAT encoding settles only anchored subfamilies, heavy-tailed
  runtime (`dumitru-es7`, status asserted).
- **No 4-fold-symmetric 32-point no-7-gon set** (`smqh-no-realizable-4fold-32-no7gon`): full SAT
  enumeration (310,187,713 solutions, ~1 CPU-yr) shows every 4-fold-symmetric 32-point 7-gon-free
  orientation has one of 6 non-realizable inner-12 configurations; hence a hypothetical extremal
  32-point set (if it exists) has no 4-fold rotational symmetry. A concrete impossibility result
  on the ES(7) frontier.
- **200,000 abstract 32-point no-7-gon candidates, none realizable** (`kph-32-no7gon-no-realizable-found`):
  PointSAT's unconstrained search generated 200,000 abstract order-type solutions (2191 core-hrs),
  none realizable. Not a disproof of ES(7)=33 (abstract space not exhausted; realizable fraction
  shrinks with n); but it, SMQH, and Dumitru's anchored-subfamily UNSAT together mean: on the
  ES(7) frontier every computational route reaches 32-point no-7-gon candidates and none has
  realized one. The search space is almost entirely abstract/unrealizable.
- **Second recursive-self-similar extremal example: Horton's empty-plane set** (`horton-no-empty-7gon`).
  Horton 1983 gives a 2^k-point set S_k with NO EMPTY convex 7-gon whose left/right/bottom/top
  halves are all scaled translates of each other — a digit-coded staircase structurally parallel to
  the ES 1961 construction, but for the empty (stronger) requirement. This is independent evidence
  that the *recursive self-similar* shape is the natural form an extremal no-large-convex/empty
  construction takes, supporting the question "how close must an extremal 2^{n-2}-point no-convex-n-gon
  set be to the ES construction". It is the EMPTY analogue — kept distinct from the ES(n)
  convex-position conjecture and out of Established (adjacent per GOAL).

## Contradiction / hazard to keep in view

- The ordered-3-uniform-hypergraph analogue of ES FAILS (`baek-balko-split`), so an abstract
  generalization is not free; do not claim the planar result from an abstract-hypergraph
  analogue.
- Realizability is ETR-complete; a structural claim proved over all abstract order types may
  hold on unrealizable ones and be false geometrically (`aichholzer-order-db` caveat).
