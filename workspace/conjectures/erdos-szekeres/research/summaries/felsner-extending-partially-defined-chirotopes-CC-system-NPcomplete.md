# Extending partially defined chirotopes is NP-complete (CC-system axiomatization)

<!-- source: https://export.arxiv.org/pdf/math/0504430v1.pdf | full text at research/sources/felsner-extending-partially-defined-chirotopes-CC-system-NPcomplete-full.full.md -->

**Publication.** Patrick **Baier**, *NP-completeness of Partial Chirotope Extendibility*, arXiv:math/0504430 (2005). Short research note making precise a result already implicit in Knuth's *Axioms and Hulls* (1992). (Baier notes he and Stefan Felsner worked on signotope extendibility; this note is Baier's.) It is primary for the exact statement of Knuth's CC-system axioms and for the NP-completeness of chirotope extendibility.

## Why this matters for the run

The run's SAT arm encodes the ES problem with orientation (chirotope/signotope) variables plus transitivity/signature axioms. The standing caution (in the problem brief and in CONTEXT) is that **not every abstract order type / chirotope is realizable** — realizability is ∃ℝ-complete. This note makes the quantitative lying-in-wait precise at the level the encoders actually operate:

- **Theorem.** Deciding whether a boolean function defined on a *subset* of the triples of a groundset can be extended to a *chirotope* (equivalently a pre-CC-system) is **NP-complete**.
- This is exactly the "partial SAT assignment of orientation variables" situation a solver walks through: enforcing the abstract axioms does not buy realizability, and even *completing* a partial orientation to a full abstract chirotope — before any geometric realizability question — is already NP-hard.

## The exact axioms (Knuth's CC system, as the encoders cite them)

For all distinct p,q,r,s,t (each with an implicit universal quantification):

- Axiom 1 `pqr ⇒ qrp` — cyclic symmetry
- Axiom 2 `pqr ⇒ ¬prq` — antisymmetry
- Axiom 3 `pqr ∨ prq` — nondegeneracy (exactly one orientation per triple)
- Axiom 4 `tqr ∧ ptr ∧ pqt ⇒ pqr` — interiority
- Axiom 5 `tsp ∧ tsq ∧ tsr ∧ tpq ∧ tqr ⇒ tpr` — transitivity
- Axiom 5′ `tps ∧ tqs ∧ trs ∧ tpq ∧ tqr ⇒ tpr` — dual transitivity (inter-derivable with 5)

The first four axioms alone give a *pre-CC-system*; axioms 1,2,3,5 give an equivalent notion.

## Structure of the NP-completeness (why the abstract axiomatization is a trap)

- **Lemma 1.** A pre-CC-system is characterized by each associated tournament being vortex-free. (Associated tournament of a point t: p→q iff tpq.)
- **Lemma 2.** The uniform chirotopes are exactly the pre-CC-systems.
- **Reduction.** 3SAT reduces to "extend a directed graph to a vortex-free tournament", then that tournament builds a CC-system with an additional point. Hence extending a partial CC-system (or partial chirotope) is NP-complete (Knuth's proof, made explicit here).

## Bearing on this problem

1. **Do not treat a satisfying abstract-chirotope assignment as a geometric realization.** The abstract axioms are an *under-approximation*; a satisfying assignment that happens to be non-realizable is the Balko–Valtr/abstract-order-type failure mode. This note is the sharpest statement of that: even completing a partial orientation to a *consistent abstract* chirotope is NP-hard, so a SAT solver that respects only the axioms can and will wander into non-realizable territory.
2. **Consequence for any "upper bound over all abstract order types": false.** (Balko–Valtr already refuted the abstract Peters–Szekeres conjecture.) This note reinforces that no structural upper-bound argument can be discharged purely over abstract CC systems / chirotopes; the 4-tuple realizability (pseudolinearity) constraint — or explicit rational coordinates — must be enforced.
3. It corroborates the Subercaseaux remark (held) that the order-type/signotope axioms give ~2^{Θ(n²)} abstract order types vs ~2^{Θ(n log n)} realizable ones.

## Relationship to the held library

- Complements `wikipedia-cc-system` (which holds the same five axioms via Wikipedia) with a primary scholarly treatment and the NP-completeness result.
- The Subercaseaux "Automated Symmetric Constructions" note (held) states the CC axioms in its own notation and gives the O(n⁴) encoding; the Signotope axioms (Felsner–Weil, held) are an equivalent 4-set form.
- Directly relevant to the run's planned reproduction of ES(5)=9 / ES(6)=17: the encoder must place the realizability (pseudolinearity) predicate correctly, or the search is over abstract hypergraphs where the strengthened conjecture is false.

## claim block (for CLAIMS.md)

```claim
id: chirotope-extendibility-npcomplete
statement: Deciding whether a boolean function defined on a subset of the triples of a groundset can be extended to a chirotope (equivalently a pre-CC-system) is NP-complete. Equivalently: Knuth's CC-system axioms (cyclic sym, antisym, nondegeneracy, interiority, transitivity) are the exact axiomatization of uniform chirotopes / pre-CC-systems, and extending a partial one is NP-hard.
hypotheses: abstract chirotopes / CC systems — NOT required to be realizable by planar points. Realizability (∃ℝ-completeness) is a further, harder layer not addressed here.
holds-here: true as an abstract-combinatorial statement; it is exactly WHY abstract-chirotope upper bounds cannot be trusted for the geometric ES conjecture.
status: asserted-by-source (research note directly quoting Knuth; Le 1 & Le 2 proven).
bearing: reinforces the RULED-OUT direction (abstract order-type upper bound). The run's SAT encoders must enforce 4-tuple realizability (pseudolinearity) or explicit coordinates, not merely the abstract axioms, or they can wander into non-realizable assignments.
anchor: research/sources/felsner-extending-partially-defined-chirotopes-CC-system-NPcomplete-full.full.md
```
