Solve by extremal graph theory on cycle spectra, with a complete SAT/ILP oracle
underneath every witness. The quantity is finite and exactly computable for each
`n`: "is there a graph on `n` vertices with `n + h` edges containing a cycle of
every length `3..n`?" is one satisfiability instance over edge variables plus a
per-length cycle certificate. Deciding whether a cycle of a given length exists
is NP-hard, so every cycle-spectrum computation must be complete; an incomplete
search that fails to find a cycle has proved nothing and will misclassify graphs
in exactly the direction that flatters a claim.

The oracle is that decision procedure plus the extremal graphs themselves,
stored in graph6 and re-verified by an independent checker. Their structure is
the deliverable as much as the numbers: the upper-bound construction is
recursive, and whether small exact optima look recursive is the only empirical
signal available.

The governing honesty constraint: `log_* n <= 5` throughout the computable
range, so **no computation here bears on the `log_*` term**, and any claim that
it does must be refused. The reachable target is Erdős's own stated gap,
`h(n) - log_2 n -> infinity`.

The lower bound is a counting argument — a graph with `n + h` edges has cycle
space of dimension `h + 1`, so it realises at most `2^{h+1}` cycles and hence
`2^h >> n`. Re-derive it first; it saturates at `2^h`, which is precisely why no
counting argument can produce an additive growing term. Any approach must say
what it uses beyond counting.

Use sat_solver for the pancyclicity decisions and the minimal-surplus searches,
coder for graph generation with stated symmetry breaking, and pattern_finder on
the extremal graphs and the sequence `h(n) - log_2 n`.
