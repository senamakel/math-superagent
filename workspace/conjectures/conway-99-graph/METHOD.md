Solve by algebraic combinatorics and finite geometry, with exhaustive search
used only where its exhaustiveness can be argued. The object is a strongly
regular graph `srg(99, 14, 1, 2)`, equivalently the collinearity graph of a
partial linear space on 99 points with 231 lines of size 3 and 7 lines through
each point. Reason about *that geometry* — the local structure (every
neighbourhood is a perfect matching `7 K₂`), the forced extensions of a pair of
intersecting triangles, the interaction of the line set with `μ = 2`, the
adjacency algebra and its idempotents, interlacing on induced subgraphs, and the
constraints an automorphism of prime order puts on the orbit matrices. Spectral
methods, design theory, the Bose–Mesner algebra, orbit-matrix enumeration and
SAT/CP-SAT encodings of a bounded configuration are the instruments. Use every
other capability in service of that argument rather than instead of it.

Three cautions this problem earns before any work starts.

Two members of the same family **exist** — `srg(9,4,1,2)` (the `3 × 3` rook's
graph) and `srg(243,22,1,2)` (Berlekamp–van Lint–Seidel). Every nonexistence
argument therefore has a step that must break on both, and locating that step is
part of stating the argument. Run each candidate against those two graphs
through the oracle in `code/lib` before spending effort on it. In particular
every eigenvalue-only route — integrality, Krein, absolute bound, interlacing on
the whole graph — is already known to survive there, so it is refuted on
arrival, not weakened. Record it as such and do not re-derive it.

Enumeration is the standing temptation here and it is almost always the wrong
method. The space of 14-regular graphs on 99 vertices defeats any search, and
the published attempts are all under symmetry assumptions that the automorphism
results have themselves largely eliminated. A search is admissible only with a
stated search space, a symmetry reduction whose validity is argued, an isomorph
rejection method, and a sentence saying what an empty result rules out. A
SAT/CP-SAT encoding is admissible only after the same encoder has been made to
*find* `srg(9,4,1,2)` and `srg(243,22,1,2)`; an UNSAT from an untested encoder
is a bug report, not a theorem. A search that does not terminate is data about
the problem: record the space, the reduction, the machine, the wall clock at
which it was abandoned, and how far it got. That boundary is one of the few
honestly reportable results available in a first pass, and it is lost if
timeouts are silently retried at smaller parameters.

Exact integer arithmetic decides and everything else only searches. A
floating-point spectrum, a heuristic local search, or a partial extension is a
lead; only an exact common-neighbour count over the integer adjacency matrix,
an exact rank or Smith normal form, or a complete case analysis closes anything.
Any near-miss found by heuristic search must be resolved exactly before it is
cited, and a heuristic that gets close to `(99,14,1,2)` without reaching it is
not evidence of existence.

Prefer `networkx` and `numpy` with exact integer dtypes for graph work, `sympy`
for exact linear algebra over `Z` and `Q`, PARI/GP or Singular through
`symbolic_math` where a number-theoretic or algebraic identity is wanted, and
OR-Tools CP-SAT or a SAT solver through `sat_solver` for bounded configuration
questions. Say in each captured output which system ran it, over which ring, and
on which exact input file — a claim about "the graph" that cannot be traced to
an adjacency matrix on disk is not a claim.

The box this runs on has 28 CPUs and no container CPU quota, so a search over
configurations, automorphism orders or partial extensions should use them; state
the worker count and the search space in the capture.
