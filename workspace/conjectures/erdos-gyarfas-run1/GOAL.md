# Goal

Attack the **Erdős–Gyárfás conjecture**: every finite simple graph with minimum
degree at least 3 contains a cycle whose length is a power of two.

The full statement, what it does and does not say, the obstruction that makes
it hard, and the leads into the literature are in `problem.md`. Read that
before deciding anything.

## The method this run is committed to

**Structural graph theory.** Reason about a minimal counterexample and what its
structure must be: connectivity, girth, degree distribution, forbidden
subgraphs, the behaviour of separators, ear decompositions, DFS trees and their
back edges, expansion, and the standard cycle-length machinery built on those.
Everything else in the runtime serves that.

- **Computation** (`tool_builder`, `coder`, `sat_solver`) exists to test the
  structural claims, generate the extremal examples that refute a guess, and
  push the verified range upward. It does not substitute for the argument.
- **SAT/SMT** (`sat_solver`) is for the finite questions the structural argument
  throws off: does a graph with this degree sequence, this girth, and no cycle
  of length 4, 8, or 16 exist on $n$ vertices? That is a satisfiability
  question, and `UNSAT` on it is a theorem about $n$.
- **Lean 4** (`lean_prover`) is for making a lemma true rather than persuasive.
  Formalise the statement early — getting it right is itself work — and
  formalise each structural lemma as it stabilises.
- **The literature** (`librarian`, `scholar`, `research`) comes first and never
  stops. See below.

## Completion criteria

This run does not end by proving the conjecture. It ends by having, written
down and defended:

1. `research/ROOT.md` describing what the literature actually establishes:
   every known partial result with its exact hypotheses and conclusion, every
   known failed approach with the reason it failed, and the current
   computational verification bound with its method.
2. `MEMORY.md` holding the structural facts this run has *established* about a
   minimal counterexample, each marked proved / verified-numerically /
   conjectured, and each with what would falsify it.
3. At least one new statement that is genuinely this run's: a lemma, a
   restricted-class proof, a strengthened verification bound, or a reduction.
   Stated exactly, attacked before it is trusted, and either proved, refuted,
   or left explicitly open with the gap named.
4. A Lean 4 file carrying the formal statement of the conjecture, plus every
   lemma proved along the way, with `#print axioms` output reported and every
   remaining `sorry` listed.
5. An honest final report: what was established, what was checked by machine,
   what remains conjecture, and what the next attempt should do.

A run that ends with "the conjecture is proved" and an argument that has not
survived attack has failed, however good the argument reads. A run that ends
with three real lemmas and a precisely stated gap has succeeded.
