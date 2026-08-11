# Factorial number system (Wikipedia) — source note

Source: https://en.wikipedia.org/wiki/Factorial_number_system (converted from HTML).

## What it establishes
The **factorial number system** (factoradic) is a mixed-radix system adapted to
numbering permutations. Precise claims, all in the "Definition" and "Permutations"
sections of the full text:

- The i-th digit from the right has base i and place value (i−1)!; digits are
  bounded 0 ≤ digit < i.
- Reading the factoradic digits as a **Lehmer code** (right-inversion table) maps
  the integers 0..n!−1 bijectively onto the permutations of n elements **in
  lexicographic order**. Concretely (n=3, table in source):
  factoradic 0:0:0!→012, 0:1:0!→021, 1:0:0!→102, 1:1:0!→120, 2:0:0!→201,
  2:1:0!→210. So the factoradic number IS the 0-based lexicographic rank.
- The n-factoradic numbers 0..n!−1 form a permutohedron under bitwise ≤.
- Conversion integer↔factoradic via repeated division by radix 1,2,3,… (quotient
  and remainder as digits), i.e. rank0(σ) = Σ_{i=1..n} c_i(σ)(n−i)! with the
  Lehmer digits c_i = right-inversion counts, 0 ≤ c_i ≤ n−i.

## Relevance to this run
This is the theoretical basis of `rank` as "Σ Lehmer digits × factorial place
weights", already captured as fact (1) in `report_cited_facts.md` (from multiple
parallel sources). It confirms, from a primary reference, that rank0 bijects
S_n onto {0..n!−1}, which is exactly the fact behind the identity
Σ_{σ∈S_n} rank(σ) = n!(n!+1)/2 (fact 3).

## What it does NOT settle
It gives **no closed form or shortcut for Σ_{τ∈⟨π⟩} rank(τ) over a cyclic
subgroup** — the unresolved step for reaching Q(10^6). It is lexicographic
rank-by-construction, not a structural identity over cyclic subgroups.

## Verdict
Confirms an existing, already-cited belief (fact 1); adds nothing new toward
the efficient-method subtask. No contradiction with memory.md.

## Contradictions
None. Fully consistent with memory.md and report_cited_facts.md.
