# Goal

Attack the **Collatz conjecture** ($3n+1$ problem): for every positive integer
$n$, iterating $n \mapsto n/2$ (even) or $n \mapsto 3n+1$ (odd) eventually
reaches $1$.

The full statement, what it does and does not say, the obstruction that makes
it hard, and the leads into the literature are in `problem.md`. Read that
before deciding anything.

## The method this run is committed to

**Dynamical systems and Diophantine analysis**, backed by computation.
The two live obstructions in the literature are (i) ruling out an orbit that
diverges to infinity and (ii) ruling out a non-trivial cycle — both, in the
end, come down to controlling how often $3n+1$-type steps versus halving
steps occur along an orbit, which is governed by the irrationality (and
irrationality measure) of $\log 3 / \log 2$.

- **Computation** (`tool_builder`, `coder`) exists to verify orbits over large
  ranges, search for non-trivial cycles under growing bounds, and push the
  verified frontier past whatever the literature already reached. It does not
  substitute for the argument, and a verified range is evidence, not a proof.
- **Diophantine approximation** is the sharpest lever for ruling out
  non-trivial cycles: a cycle of a given shape forces a near-integer relation
  between powers of 2 and 3, and effective irrationality-measure bounds on
  $\log 3/\log 2$ translate into lower bounds on cycle length or minimum
  element. Make this argument precise rather than citing it as folklore.
- **Statistical / density arguments** (à la Tao) are useful context for what
  is already known and why the conjecture is expected to be true, but a
  result of this shape does not touch the conjecture itself — see
  `problem.md`. Do not let a run report one as progress on the open case.
- **Lean 4** (`lean_prover`) is for making a lemma true rather than
  persuasive. Formalise the statement early, and formalise each structural or
  Diophantine lemma as it stabilises.
- **The literature** (`librarian`, `scholar`, `research`) comes first and
  never stops. See below.

## Completion criteria

This run does not end by proving the conjecture. It ends by having, written
down and defended:

1. `research/ROOT.md` describing what the literature actually establishes:
   Tao's result stated exactly (and exactly what it does not claim), the
   current computational verification bound and its method, the current
   non-trivial-cycle exclusion bound and its method, and every known failed
   approach with the reason it failed.
2. `MEMORY.md` holding the structural facts this run has *established*, each
   marked proved / verified-numerically / conjectured, and each with what
   would falsify it.
3. At least one new statement that is genuinely this run's: a lemma, a
   restricted-class proof, a strengthened verification or cycle-exclusion
   bound, or a reduction. Stated exactly, attacked before it is trusted, and
   either proved, refuted, or left explicitly open with the gap named.
4. A Lean 4 file carrying the formal statement of the conjecture, plus every
   lemma proved along the way, with `#print axioms` output reported and every
   remaining `sorry` listed.
5. An honest final report: what was established, what was checked by machine,
   what remains conjecture, and what the next attempt should do.

A run that ends with "the conjecture is proved," or that reports a
density-one / almost-all-orbits result as resolving it, has failed however
good the argument reads. A run that ends with a sharper cycle-exclusion bound,
a real lemma, and a precisely stated gap has succeeded.
