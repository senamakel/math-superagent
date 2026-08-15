# Nullstellensatz refutations as complete non-colourability certificates

```approach
idea: Certify "G is not 4-colourable" by an explicit algebraic identity
      1 = Σ_v h_v·(x_v^4 − 1) + Σ_{e=uv} g_e·(x_u^3 + x_u^2 x_v + x_u x_v^2 + x_v^3)
      over a field containing primitive 4th roots of unity (C symbolically, or
      F_p with p ≡ 1 mod 4). By the Weak Nullstellensatz this identity exists
      iff G has no 4-colouring, so a low-degree certificate exists for exactly
      the non-4-colourable graphs — a complete algebraic certificate in the
      correct direction.
mechanism: Encode colours as 4th roots of unity: x_v^4 = 1 forces each vertex to
      a colour in {1, i, −1, −i}, and the edge polynomial
      S_e = x_u^3 + x_u^2 x_v + x_u x_v^2 + x_v^3 = (x_u^4 − x_v^4)/(x_u − x_v)
      vanishes iff x_u ≠ x_v (when both are 4th roots of unity, x_u = x_v gives
      S_e = 4x_u^3 ≠ 0; x_u ≠ x_v gives S_e = 0). So the ideal
      I = ⟨x_v^4 − 1 : v∈V⟩ + ⟨S_e : e∈E⟩ cuts out exactly the proper
      4-colourings. Hilbert's Weak Nullstellensatz gives V(I) = ∅ ⟺ 1 ∈ I.
      Non-4-colourability is therefore equivalent to the existence of
      polynomials h_v, g_e realising the identity above — a "Nullstellensatz
      refutation" (De Loera–Lee–Malkin–Margulies style) / a Polynomial Calculus
      refutation (Clegg–Edmonds–Impagliazzo 1996). Searching for such a
      certificate of total degree ≤ d is one linear system over the monomial
      basis, in exact arithmetic; over F_p (p ≡ 1 mod 4) all coefficients are
      integers mod p, so no floats anywhere.
      Why this beats the refuted Alon–Tarsi line: Alon–Tarsi is a *sound but
      incomplete* certificate of colourability (an unbalanced orientation of
      max out-degree ≤ 3 proves 4-colourable, the wrong direction — see
      research/approaches/alon-tarsi-coefficient-certificate.md). A
      Nullstellensatz refutation is *complete for non-colourability*: a
      certificate exists iff the graph is genuinely not 4-colourable. It also
      satisfies the independent-re-verification discipline literally — the
      certificate shares no arithmetic with the SAT encoding or the coordinate
      field, only the abstract edge set — and it gives a search objective
      (minimum certificate degree) that grades candidate graphs even where SAT
      is instantaneous.
      SPECULATIVE part, stated as such: whether the certificate degree stays
      small enough to beat/complement the SAT oracle at the run's sizes. A
      degree-d search costs ~ (monomial count)^2 ~ poly(n, d), and the colouring
      ideal is a "complete intersection"-like encoding whose certificates are
      expected to be low degree in practice, but this is a conjecture to be
      measured, not a theorem. What would falsify the value: if the Moser
      spindle's non-3-colourability certificate has degree so large the linear
      system is bigger than the SAT run, the method is a curiosity, not a line.
status: refuted
killed-by: re-verifier-not-a-search-line (NulLA is correct and complete for
      non-colourability, but at the run's sizes it does not beat the SAT oracle
      and its deliverable — the arithmetic-independent non-4-colourability
      re-verifier — is idle until the run holds a non-4-colourable graph, which
      it does not. The live crux `G-forced-pair-exists` needs a CONSTRUCTION
      line supplying richer 4-chromatic base graphs, which Nullstellensatz does
      not provide. Not refuted as mathematics; closed in favour of
      projection-distance-equalization. Its one future role — the forced-pair
      certificate (radical membership of x_u−x_v in the colouring ideal) as an
      independent re-check and grader — is retained as a secondary check inside
      the adopted line's first step.)
precedent: The mechanism is exactly the named NulLA method — De Loera–Lee–Malkin–
      Margulies, "Hilbert's Nullstellensatz and an algorithm for proving
      combinatorial infeasibility", ISSAC 2008, https://doi.org/10.1145/1390768.1390797
      (graph k-colourability as polynomial-system solvability; a certificate
      1 = Σ h_v f_v exists iff infeasible; solved non-3-colourability for graphs
      with thousands of nodes and tens of thousands of edges). Completeness in
      the CORRECT direction is confirmed by the primary sources: De
      Loera–Lee–Margulies–Onn, "Expressing combinatorial problems by systems of
      polynomial equations and Hilbert's Nullstellensatz", CPC 18 (2009),
      https://doi.org/10.1017/s0963548309009894 (min certificate degree for
      non-3-colourability is ≥ 4); De Loera–Hillar–Malkin–Omar, "Recognizing
      graph theoretic properties with polynomial ideals", EJC 17 (2010),
      https://doi.org/10.37236/386 (Theorem 2.1: certificate iff system has no
      solution). Root-of-unity colour encoding and edge polynomial
      S_e = x_u^3+x_u^2 x_v+x_u x_v^2+x_v^3 = (x_u^4−x_v^4)/(x_u−x_v) verified
      correct (variety of the ideal = exactly the proper 4-colourings). The
      degree-risk the candidate flagged is REAL and named: Lauria–Nordström,
      "Graph colouring is hard for algorithms based on Hilbert's Nullstellensatz
      and Gröbner bases", CCC 2017, https://doi.org/10.4230/lipics.ccc.2017.2 —
      linear-degree / exponential-size certificate lower bounds for NulLA on
      bounded-degree non-k-colourable graphs; Conneryd et al., "Graph colouring
      is hard on average for polynomial calculus and Nullstellensatz", FOCS 2023,
      https://doi.org/10.1109/focs57990.2023.00007 — linear degree average-case
      even on sparse random graphs. Calibration fallback exists and is favourable
      at run sizes: Li–Lowenstein–Omar, "Low degree Nullstellensatz certificates
      for 3-colorability", EJC 23 (2016), https://doi.org/10.37236/5103 —
      computed N_k(G) for all non-3-colourable graphs on ≤ 12 vertices over GF(2)
      and found 4-critical graphs detected at small degree. Precision caveat:
      Weak Nullstellensatz is over an algebraically closed field; F_p is not, so
      the search is over F_p-bar (resolved the standard way, as DLMO do over
      GF(2)) — the certificate coefficients lie in the algebraic closure, not
      literally in F_p.
bearing: Does NOT produce a bound and does NOT beat SAT at run sizes (7–27
      vertices, where the SAT scan already costs ~0.1 s) — so it is NOT a
      search/pre-filter line. Its value is the role GOAL.md explicitly mandates:
      a mechanically checkable, arithmetic-independent certificate of
      non-4-colourability (shares no arithmetic with the SAT encoding or the
      coordinate field), i.e. the independent re-verifier for any claimed
      5-chromatic graph. That role is currently idle — the run owns NO
      non-4-colourable graph — so the immediate, concrete, tested deliverable is
      the calibration datum (non-3-colourability of the 7-vertex graph), which
      must be run to measure the degree before the re-verifier role is trusted.
first-step: Over F_p, p ≡ 1 mod 4 (e.g. p = 1009), build the monomial-linear
      system for the identity 1 = Σ h_v(x_v^4−1) + Σ g_e S_e at degree d = 1,2,…
      and calibrate: (i) Moser spindle, k = 3 — must FIND a certificate (it is
      not 3-colourable); (ii) Moser spindle, k = 4 — must find NO certificate
      (it is 4-colourable, so 1 ∉ I); (iii) the run's 7-vertex 11-edge graph
      and Moser+Moser (26v) as the non-4-colourable sanity contrast. Record the
      minimum degree found as the calibration datum, then wire it in as the
      independent re-verifier for any claimed 5-chromatic graph.
```
