# SMQH Erdős–Szekeres SAT encoder (Subercaseaux–Mackey–Qian–Heule), `encoders/erdos_szekeres.py`

> **Source:** `https://raw.githubusercontent.com/bsubercaseaux/automatic-symmetries/main/encoders/erdos_szekeres.py` (full plain-text held at `research/sources/smqh-erdos-szekeres-encoder.py.full.md`). The encoder behind the SMQH "Automated Symmetric Constructions in Discrete Geometry" (arXiv:2506.00224) computational claims, including the 4-fold-symmetric 32-point no-7-gon result.

## What the encoder actually encodes

`encode(n, g, forced_sym=False)` builds a CNF (via `eznf` modeler → `.cnf` file) asserting the existence of **n points in general position with no g-gon**, over **orientation (CC) variables**. This is the reference encoding this run's `sat_solver` arm must mirror to reproduce ES(5)=9 / ES(6)=17. Concretely:

- **Variables.** `cc_{p,q,r}` for every unordered triple (a Knuth CC/rank-3-chirotope orientation var), plus `<_ {p,q}` linear-order vars for the full ordering.
- **Order axioms.** Non-degeneracy (`<_pq ∨ <_qp`, `-<_pq ∨ -<_qp`) and transitivity of `<_` for all permutations — a strict total order on the points.
- **Cyclic symmetry & antisymmetry** of `cc` enforced through the `cc()` helper (signed argument reduces to an unordered triple var).
- **Ordered-signotope / CC-system axioms** (the geometry-forcing core): for certain 4-tuples, clauses of the form `<_pq, <_pr, <_ps ⊨ cc(p,q,r) ↔ cc(p,r,s)` and the at-most-one-sign-change equivalent `-<_pr,-<_qr,-<_rs ⊨ cc(p,q,r), -cc(p,r,s), cc(q,r,s)`. These are the Felsner–Weil rank-3 transitivity/signature conditions that prune toward realizable order types.
- **Convex-quadrilateral predicate.** For each 4-subset, `conv_{p,q,r,s} ↔ ((cc_{p,q,r} ↔ cc_{p,r,s}) ↔ (cc_{p,q,s} ↔ cc_{q,r,s}))` — exactly the 4-set convexity criterion (a convex quad iff the two orientation-pair equivalences agree).
- **No g-gon.** For every g-subset, `-conv_{qd}` for all its 4-subsets — i.e. no g points all of whose 4-subsets are convex, forbidding any convex g-gon. Uses the 4-set criterion to reduce "convex g-gon" to a local conjunction.
- **Symmetry (optional `forced_sym`).** Layers of `forced_sym`-fold rotation; enforces `cc` equivalence under the rotation, and (via `lex_smallest_rot`) only adds the no-g-gon clause for lexicographically-minimal rotations (isomorph rejection under the cyclic group). Adds convex-hull-layer structure clauses and same-quadrant constraints for `forced_sym == 4`.

## Why it matters for this run (the load-bearing part)

1. **This is the standard-formulation reference encoder.** It uses exactly the ingredients GOAL.md/problem brief call for on the computational arm: triple-orientation variables (rank-3 chirotope/signotope), transitivity/CC-system axioms to force an order type, the 4-set convexity criterion, and symmetry-based isomorph rejection. A reader of this run's own SAT arm should compile the *same* object.
2. **The realizability boundary is explicit here.** The CNF enforces the abstract axiomatization (necessary, not sufficient). A satisfying assignment need not be a realizable point set (realizability is ∃ℝ-complete); SMQH pair the SAT solver with Localizer exactly to separate the realizable ones — the same point Balko–Valtr make (abstract vs geometric) and the Baier/Knuth NP-hardness of even *completing* a partial chirotope.
3. **Concrete facts about the encoding's cost/shape.** The "no g-gon" clause per g-subset plus per-4-subset conv predicate is O(n⁴)-ish in variables/clauses with the C(n,g)·C(g,4) no-gon clauses; the forced-symmetry path cuts the g-subset enumeration by the cyclic group via `lex_smallest_rot` (isomorph rejection). This is the structural reason the 4-fold 32-point search was feasible while unconstrained 32-point search (PointSAT) was not.

```claim
id: smqh-erdos-szekeres-encoder
statement: SMQH's erdos_szekeres.py encodes 'exists n planar general-position points with no g-gon' as a CNF over orientation vars cc_{p,q,r} and linear-order vars, using: strict-total-order axioms; CC-system (ordered-signotope/rank-3) cyclic-symmetry+antisymmetry+transitivity clauses; a conv_{p,q,r,s} 4-set convexity predicate defined by the two orientation-pair equivalences; and a 'no g-gon' clause per g-subset (negate conv over all its 4-subsets). Optional forced_sym adds k-fold rotation equivalence clauses, lex-smallest-rotation isomorph rejection on the no-gon clause, convex-hull-layer structure, and same-quadrant constraints.
hypotheses: n points, g-gon forbidden, general position; encoding is over the abstract order-type (CC/chirotope) axioms — a satisfying assignment is NOT automatically a realizable point set.
holds-here: yes — this is the reference encoding the run's SAT arm should mirror to reproduce ES(5)=9 (n=9,g=5 no-gon UNSAT) and ideally ES(6)=17 (n=17,g=6), enforcing the 4-set convexity criterion exactly as problem.md demands.
status: catalogued (source code read this run; encoding structure extracted verbatim from the file). Not verified by running SMQH's solver here.
bearing: gives the run's computational arm its canonical SAT formulation + symmetry/isomorph-rejection pattern, and the exact shape of the realizability caveat (abstract axioms necessary, not sufficient; Localizer/coordinates required).
anchor: research/sources/smqh-erdos-szekeres-encoder.py.full.md
follows-from: cc-system-axioms, es35-four-criterion, fw-rank3-signotope-pseudoline, chirotope-extendibility-npcomplete
answers: (none of the open requests directly; complements balko-valtr-attack-baa4 as a second independent reference encoder)
```
