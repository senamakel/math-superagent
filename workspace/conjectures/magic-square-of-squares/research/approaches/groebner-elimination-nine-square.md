```approach
idea: Compute the elimination ideal J = <L_i(c,u,v) − s_i^2 : i=1..9> ∩ Z[c,u,v] of the
       full nine-square system, where L_i are the nine magic-square entries (the linear
       forms in c,u,v of the (c,u,v) parametrisation). Over the algebraic closure the
       projection (c,u,v,s) ↦ (c,u,v) is dominant (every element of an algebraically
       closed field is a square), so the Q-elimination ideal is trivial — the interesting
       ideal lives over Z, where the integrality of s_i is essential. J ⊂ Z[c,u,v] is the
       Zariski closure of the set of (c,u,v) for which all nine entries are integer
       squares. Named mathematics: elimination theory, Gröbner bases over Z, primary
       decomposition of polynomial ideals.

mechanism: The parametrisation already encodes the magic property, so the nine "entry is a
       square" conditions are the entire content. Introduce s_1..s_9, eliminate them. Over
       Q̄ the map is dominant so the Q-elimination ideal is 0; over Z the elimination ideal
       is generally nonzero and captures integrality. Three outcomes: (a) 1 ∈ J ⟹ no
       integer solution exists (a full proof of non-existence, exact, kernel-checkable via
       a Gröbner-basis computation); (b) J = (0) ⟹ no polynomial invariant in (c,u,v)
       alone, refuting this line; (c) J is a nonzero proper ideal ⟹ its generators are
       arithmetic equations every integer MSS must satisfy — a new invariant that no
       previous approach (K3, BM, 2-Selmer, Φ, S-unit) extracted, and a direct route to a
       partial result ("any integer MSS satisfies this explicit polynomial"). Distinctness
       and positivity are imposed after, not inside, the elimination.

first-step: Run a Gröbner-basis elimination over ZZ (Singular or Macaulay2; sympy's
       groebner with domain=ZZ as a fallback) on <L_i − s_i^2> ∩ Z[c,u,v], report whether
       1 ∈ J, the number and degrees of generators, and the primary decomposition. If J is
       nonzero proper, factor the generators and read off the arithmetic constraints on
       (c,u,v).

speculation-vs-established: ESTABLISHED — the (c,u,v) parametrisation and its nine linear
       forms (checked, this run: oracle_note.md); the fact that elimination over Q̄ is
       dominant (elementary: every field element of an algebraically closed field is a
       square). SPECULATION — that J over Z is nonzero and informative; the computation is
       the check, and outcome (b) refutes the line cheaply.
```
