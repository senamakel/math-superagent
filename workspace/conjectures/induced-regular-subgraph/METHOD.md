Solve by extremal graph theory, with a solver-backed exact oracle underneath
every claim. "Does this graph have an induced regular subgraph on `k` vertices?"
is a constraint satisfaction instance — one Boolean per vertex for membership,
plus a cardinality constraint per chosen vertex fixing its degree inside the
chosen set, looped over the target degree — so it is answered by SAT or ILP and
never by enumerating vertex subsets. The subset space is `2^n` and enumerating
it is what stops this problem being computed further.

The oracle for this problem is that decision procedure, plus a search for
extremal graphs witnessing `G(k) > m`. Note the asymmetry and exploit it: a
lower bound on `G(k)` is a single explicit graph, verifiable in seconds by an
independent checker, while an upper bound requires exhaustive generation up to
isomorphism. Prefer the side that produces certificates, and always say which
half of a claimed exact value was actually done.

The oracle must reproduce `G(3)=5` and `G(4)=7` on its own before anything it
later reports is trusted, and every extremal graph it finds is stored in graph6
and re-verified by a checker that did not find it.

The standing structural discipline: Ramsey's theorem already gives
`F(n) >> log n` by producing a clique or an independent set — both trivially
regular. So for every argument, state which regular induced subgraph it produces.
An argument producing only a trivial one has reproduced Ramsey and improved
nothing, whatever language it is written in.

Use sat_solver for the induced-regular decision and the bounded searches, coder
for graph generation (nauty/geng-style, with symmetry breaking stated), and
pattern_finder on the sequence of extremal graphs — their structure is the
mathematical content, not just the numbers.
