# Approach: centroid-colour determinant Δ_f (adopted)

The synthesis of the inventor's moment/Hankel proposal with what the literature
actually contains. Castryck–Laterveer–Ounaïes (arXiv:1208.5404) already *prove* a
combinatorial determinant — Δ_f, their eq. (2) — that controls exactly the
derivative-sharing structure the moment/Hankel idea wanted to capture. It lives on
the **colour** axis (which derivative orders vanish at one distinguished root, the
centroid), not the **root** axis (which roots witness a fixed derivative) that the
adopted root-difference-coloring uses. And it applies verbatim to the open degree.

```approach
idea: For a char-0 counterexample f of degree d = p+1 (p prime) with centroid c,
      let J = {j_1 < ... < j_m} ⊆ {2,…,d−2} be the derivative orders with
      f^{(j_i)}(c) = 0. Castryck Thm 2 (arXiv:1208.5404, §3) proves that the
      consistency of the linear system (13) in the normalised coefficients forces
      det Δ_f(J) ≡ 0 (mod p), where Δ_f(J) is the (m+1)×(m+1) matrix of eq. (2)
      with entries −1, j_i, binom(j_i−2, j_l−2)·j_i and (−1)^{j_i}. det Δ_f depends
      ONLY on the set J — a purely combinatorial "master determinant" on the colour
      axis {2,…,d−2}. CA becomes: every candidate centroid-colour set J must satisfy
      det Δ_f(J) ≡ 0 mod p.
mechanism: Δ_f is the transpose of root-difference-coloring. The adopted identity
      H_i(f)(β_j) = e_{n−i}(β_j − β_*) fixes the derivative i and varies the witness
      root β_j; Δ_f fixes the distinguished root (the centroid c) and varies the
      derivative order j. Its entries are binomial coefficients in the differences
      j_i − j_l (a Pascal/Hankel-type structure), not root differences. This is the
      matrix the moment-hankel proposal was reaching for and could not name: it is
      NOT the power-sum moment matrix (which Newton's identities identify with the
      run's elementary-symmetric data), but a determinant on the other axis.
      Crucially it is PROVED, not conjectured, for the whole p+1 family.
      The sharp consequence the run has not yet drawn: the open degree 20 = 19 + 1
      with p = 19 prime. Castryck Thm 2 applies verbatim to degree 20. The d = 12
      (p = 11) scenario list (eq. 3: 29392 scenarios, 5 of type 8) was computed from
      exactly this determinant; the d = 20 list has never been computed, and the
      run's only other route to degree 20 (the Schaub–Spivakovsky minors criterion)
      is infeasible at C = binom(190,18) ≈ 1e20. Computing the Δ_f-constrained
      scenario list for d = 20 is the exact, feasible analogue, and it IS the
      feasibility boundary of the reduction-mod-p method at the open degree.
      Char-p break (located): Theorem 2 is a char-0 necessary condition proved via
      the p-adic valuation v_p on C (the congruences x ≡ y ⇔ v_p(x−y) > 0). It has
      no content in characteristic p: there is no p-adic valuation on F_p, and the
      char-p witness x^{p+1} − x^p is not a "counterexample over C" to which Thm 2
      applies. The mod-p reduction of the conclusion (det Δ_f ≡ 0 mod p) is a
      consequence of the char-0 hypothesis, not a char-p statement — so the argument
      breaks in char p by vacuity of its domain, exactly the named, located,
      char-0-only step GOAL.md requires.
status: adopted
first-step: (tool_builder, exact sympy, oracle-guarded via lib.casas_alvero)
      (1) Reproduce Δ_f(J) from eq. (2) as an (m+1)×(m+1) integer matrix for any
      J = {j_1<...<j_m} ⊆ {2,…,d−2}. (2) VALIDATE against Castryck's degree-12
      data: for p=11, d=12, enumerate all J ⊆ {2,…,10} with det Δ_f(J) ≡ 0 (mod 11)
      and confirm the 2-element solutions are exactly {(3,8),(5,6),(6,8),(6,9),(7,9)}
      (their eq. 4), then reproduce the scenario counts (0,48,1668,8172,11586,6298,
      1469,146,5,0,0) of eq. (3) by counting scenarios s of each type whose index set
      ind(s) = {j : s_{d−j} = s_{d−1}} satisfies the determinant condition.
      (3) THE NEW COMPUTATION: for p=19, d=20, enumerate every J ⊆ {2,…,18} with
      |J| ≥ 2 and det Δ_f(J) ≡ 0 (mod 19); report the count and the full list. This
      is the centroid-colour constraint for the open degree 20. (4) Count the strongly
      reduced scenario list for d=20 (the analogue of eq. 3) and report the
      feasibility boundary for the reduction-mod-19 Gröbner method. All exact integer
      arithmetic; 2^17 = 131072 subsets at ≤ 18×18 determinants is milliseconds.
precedent: castryck-2012, (arXiv:1208.5404, Thm, 2,, §3:, Δ_f, determinant, eq., (2),,
      proved, necessary, condition, on, degree-(p+1), char-0, counterexamples, via,
      p-adic, valuations);, laterveer-ounaies-2012, (arXiv:1204.0450,, Prop, 7:, the,
      same, p+1, centroid, constraint, in, power-sum, language);, moment-hankel-rank,
      (refuted, this, round:, its, "master, determinant", was, Δ_f,, not, the,
      power-sum, moment, matrix);, hessian-covariant-transvectant, (refuted, this,
      round:, pure-power, ⟺, Hessian, ≡, 0, has, no, bridge, to, the, derivative,
      system)
```

## What is established and what is not

**Proved (by the source, and re-derivable from eq. 2 + system (13)):** for a char-0
counterexample of degree p+1, the set J of derivative orders vanishing at the
centroid must satisfy det Δ_f(J) ≡ 0 mod p. The matrix Δ_f is lower-triangular in
its first m rows with a final row [−1, (−1)^{j_1}, …, (−1)^{j_m}]; for m = 1 it
reduces to det = j − (−1)^j (Castryck's Lemma 18), so a single centroid colour is
impossible.

**Claimed by me (elementary, not needing computation):** 20 = 19 + 1, 19 prime, and
the run's sourced `smallest-open-degree` claim puts degree 20 as the smallest open
degree — so Theorem 2 applies with p = 19. This is the connection the run has not
previously drawn.

**NOT claimed:** this does not prove CA in degree 20. It produces (a) a proved
constraint on any degree-20 counterexample, and (b) the Δ_f-constrained scenario
count, which is the exact feasibility boundary of Castryck's reduction-mod-p method
at the open degree. Both are honest partial results; neither is a settlement.
