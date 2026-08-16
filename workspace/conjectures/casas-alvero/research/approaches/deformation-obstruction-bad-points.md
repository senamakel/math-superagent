# Deformation–obstruction of the char-p bad points (adopted, synthesis)

Change representation from "the resultants R_i and their generic-rank minors" to
"the cotangent complex of the arithmetic CA scheme X_n at its bad F_p-points".
The obstruction class that decides whether a char-p counterexample lifts to
Z/p² is *not* a new object: it is the rank of the Jacobian matrix M_T of the
scenario forms G_{T,i} — the same matrix whose minor-gcd J_T is the adopted
Schaub–Spivakovsky bad-prime criterion. This is the adopted engine read
fiberwise instead of generically, plus a concrete refutation search, plus the
correct home for the char-p break.

```approach
idea: The char-p counterexample points of X_n are obstructed from lifting to
      Z_p; CA in degree n is equivalent to "the pure-power point is the only
      smooth (unobstructed) point of X_n". The obstruction class at a bad
      F_p-point is computed by the cotangent complex L_{X_n/Z_p} (Illusie), and
      for the (almost) complete intersection X_n it has an explicit 2-term
      resolution by the Jacobian matrix M_T of the scenario forms G_{T,i} — the
      very matrix whose minor-gcd J_T is the adopted bad-prime-minors-criterion
      (Schaub–Spivakovsky, arXiv:2411.13967 Thm 3.1). So the new move is:
      reduce mod p, evaluate M_T at the known witness points, and check its
      rank (pointwise obstruction) instead of computing the gcd of its
      C×C minors over Z (generic obstruction). A witness that lifts to Z/p² is
      a char-0 counterexample; a witness that is obstructed is a char-0-compatible
      "good" bad point to classify.
mechanism: Two sourced engines combine.
      (1) Graf-von-Bothmer Proposition 2.2 (held): CA_{n,0} ⟺ CA_{n,p} for some
          prime p ⟺ CA_{n,p} for all but finitely many p. Hence it suffices to
          exhibit one prime p with X_n(F_p) = {pure-power point}.
      (2) Ghosh (arXiv:2402.18717, held): CA ⟺ X_n is a complete intersection;
          X_n is an almost complete intersection in every degree and its
          defining equations are the scenario forms G_{T,i} (root-difference
          coloring, adopted, gives their explicit closed form e_{n-i} of the
          root differences).
      For a complete intersection cut out by (G_{T,i}) over Z_p, the cotangent
      complex has the 2-term resolution O^m → O^k given by the Jacobian matrix
      M_T = (∂G_{T,i}/∂x_j). Illusie/Zdanowicz obstruction theory then says:
      an F_p-point x lifts to Z/p² iff M_T(x) has full rank (x is smooth).
      Zdanowicz (IMRN 2016, "Liftability of Singularities and Their Frobenius
      Morphism Modulo p²") provides exactly the computational criterion: for an
      affine complete intersection the W_2-liftability obstruction lives in
      Ext²(L_{X/k}, O_X) and is read off that Jacobian. The Schaub–Spivakovsky
      bad-prime criterion is precisely the *generic* version of this rank: p is
      bad ⟺ p | J_T = gcd of all C×C minors of M_T ⟺ M_T drops rank mod p on
      the generic fibre. The deformation approach is the *fiberwise* version:
      at which F_p-points does the rank drop, and is the pure-power point the
      only one where it does not.
charp-break: The entire content is the mixed-characteristic statement, so it is
      char-honest in the correct direction — it does not "survive mod p"
      because it is *about* reduction mod p and lifting out of it. Admissibility
      test (mandatory, GOAL.md): run the witness x^{p+1} − x^p (p = 2,3,5)
      through the pointwise computation and confirm it is reported as a
      singular (rank-deficient) F_p-point, while the pure-power point is
      reported smooth. If instead a witness lifts to Z/p², that is not a failed
      test — it is a char-0 counterexample and the line honestly converts into
      the deliverable the whole run wants. The step that must be named if the
      argument is wrong: the claimed identification "obstruction = rank drop of
      M_T at the point" holds only on the complete-intersection locus; off it
      (or at points where X_n is not locally CI) the cotangent complex has
      longer terms and the pointwise rank under- or over-counts the obstruction.
status: refuted
killed-by: blocked by the same wall it claims to beat, and its advantage is
      unmeasured — the fiberwise rank is read off the same matrix M_T as the
      adopted minor criterion, so at n=20 it faces the same C ≈ 1e20 infeasibility,
      and the claim that pointwise rank at finitely many witness points is cheaper
      than the global minor-gcd was never clocked at any n. The mixed-
      characteristic framing (obstruction = rank drop of M_T at the point) is
      absorbed into root-difference-coloring's char-p break statement; no
      separate line. Folded into research/approaches/root-difference-coloring.md.
first-step: (tool_builder, exact, oracle-guarded via lib.casas_alvero)
      For each witness (n, p) ∈ {(3,2), (5,2), (5,3), (6,5), (p+1,p) for p=2,3,5}:
      (1) confirm the witness f is an F_p-point of X_n off the pure-power locus
          (oracle is_ca_hasse True, not a pure power — guard set);
      (2) build the scenario forms G_{T,i} explicitly (root-difference closed
          form, adopted) and the Jacobian matrix M_T = (∂G_{T,i}/∂x_j), reduce
          mod p, evaluate at the witness's coefficient vector, compute its rank;
      (3) decide liftability to Z/p² by solving the linear system M_T(x)·δ ≡
          −G_{T,i}(x) mod p (with the next-order terms) — i.e. does a first-order
          correction δ to the coefficients exist mod p such that all resultants
          vanish mod p²;
      (4) repeat at the pure-power point (a_1 = … = a_{n−1} = 0): confirm full
          rank, trivial lift.
      Report, for each witness: rank of M_T(x) vs. the full rank n−1, and whether
      it lifts to Z/p². A witness that is obstructed supports the line; a
      witness that lifts is a char-0 counterexample (major result either way).
first-step-status: not run — awaiting a code-executing role
precedent: bad-prime-minors-criterion (Schaub–Spivakovsky arXiv:2411.13967
      Thm 3.1, proved: p bad ⟺ p | J_T = gcd of C×C minors of M_T);
      ghosh-complete-intersection (arXiv:2402.18717: CA ⟺ X_n complete
      intersection, almost-CI in every degree); gvb-lift (Graf-von-Bothmer
      Prop 2.2: one good prime settles the degree); Zdanowicz 2016 (IMRN,
      Ext²(L_{X/k},O_X) criterion for W_2-liftability of affine complete
      intersections, found by this run's search — the named theorem behind the
      "test lift to Z/p²" step). The pointwise/fiberwise reading of J_T as a
      rank-at-a-point computation is the run's synthesis, not a sourced theorem.
speculative: (a) the identification "obstruction class = rank drop of M_T at the
      point" is exact only on the CI locus and is the bridge to verify; (b) the
      cost claim — that pointwise rank at finitely many witness points is
      cheaper than the gcd of C ≈ 10²⁰-sized minors at n = 20 — is untested and
      is the honest reason this might beat the adopted arithmetic-jet-lift
      engine. Both are to be attacked as hard as proved: the falsifier is a
      witness (or a small-n bad point) that lifts to Z/p² with M_T full-rank,
      which would refute the bridge, and a small-n wall-clock comparison of
      pointwise-rank vs. global-minor-gcd that does not favour the pointwise
      method, which would refute the cost claim.
```

## Why this beats the other two candidates

- **`symmetric-product-diagonal-equivariant`** had no load-bearing theorem: the
  "Schur/plethysm structure forces the radical" bridge is unsupported, and its
  only concrete content — `rad(R_1,…,R_{n−1}) = moment-curve ideal` — is
  literally CA_n restated. Springer theory describes Sym^n(A¹) and its diagonal
  but asserts nothing about the radical of the resultant ideal. Refuted for
  having no inference.
- **`galois-shared-root-partition`** is characteristic-free, so it cannot
  locate the char-0 ingredient that GOAL.md demands, and no known theorem links
  the Galois group of a counterexample to CA (the candidate admitted this). Its
  first step (polgalois on witnesses) cannot reach n = 20, where the run needs
  it, because the splitting-field degree there is astronomically large.
  Refuted as ungrounded and unable to reach the target degree.
- **`deformation-obstruction-bad-points`** alone was a reformulation, not a
  shortcut (the file said so honestly). The *synthesis* is what makes it a
  line: the obstruction class is the already-owned Jacobian M_T, so this is a
  refinement of the run's engine (generic → fiberwise rank), it lives in mixed
  characteristic where the char-p break actually is (unlike the refuted
  ℂ-analytic `milnor-local-multiplicity`), and its first step doubles as a
  concrete counterexample search (Hensel lift from known char-p witnesses).
