Solve by probabilistic and extremal combinatorics on hypergraphs, with a
SAT-backed decision procedure underneath every construction. Deciding whether a
given `n`-uniform hypergraph has Property B is a satisfiability instance — one
Boolean per vertex, two clauses per edge (not-all-true, not-all-false) — so
every claimed construction can be verified exactly and cheaply. Use that: never
argue about a specific hypergraph's colourability in prose.

The oracle for this problem is that decision procedure together with a
symmetry-broken search for the fewest edges at small `n`, and it must reproduce
`m(2)=3` and `m(3)=7` on its own before anything it later reports is trusted.
Establish and state the bound on the number of vertices a minimal example needs;
without it the search space is not finite and the search is not a search.

Never enumerate 2-colourings past about twenty vertices, and never enumerate
hypergraphs without symmetry breaking. Both are exponential in the wrong
variable and both are what stops this problem being computed further.

The two sides are different work. The lower bound is a random 2-colouring with a
repair step (Radhakrishnan–Srinivasan), heavily worked; the upper bound is
Erdős's 1964 random construction giving `n^2 2^n`, essentially untouched since,
with `n 2^n` conjectured. Prefer the upper bound: a construction is checkable by
the oracle, and the missing factor of `n` sits there. Say which side any
approach is on.

Use sat_solver for every colourability question and for the bounded searches,
coder for construction families, symbolic_math for the union-bound and local
lemma computations, and pattern_finder on whatever small-`n` data the search
produces.
