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

status: refuted

first-step: None — the approach is closed.

killed-by: |
  Research (this round, agent-run-80) refutes it on two independent structural grounds.
  (1) 1 ∉ J because a full nine-square MSS exists over O_K for K=Q(√3,√133) (Bremner 1999);
  substituting that point into any polynomial in J gives 1=0 — impossible. So the hoped-for
  outcome "1 ∈ J ⟹ no integer solution" cannot occur. (2) J_Z = (0). Over Q̄ every
  affine-linear entry has a square root, so the projection is dominant and J_Q̄ = (0); by
  faithful flatness of Z → Q̄, J_Z = (0). So outcomes (a) and (c) are both impossible, and
  the "integrality makes J nonzero" premise is wrong for this specific system. A Gröbner
  basis of the zero ideal teaches nothing.

precedent: |
  This run's oracle (code/out/oracle_output.txt): (c,u,v) parametrisation completeness.
  Bremner, Acta Arith. 88 (1999): extension-field MSS.
  Faithful flatness of Z → Q̄ and elimination theory over algebraically closed fields.
  Research/approach refutation write-up at research/approaches/elimination-ideal-grobner-z.md.
```