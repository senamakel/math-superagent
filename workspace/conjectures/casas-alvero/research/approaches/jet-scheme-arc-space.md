# Approach: jet schemes / arc spaces of the CA incidence variety

```approach
idea: The Hasse derivatives H_i f are the Taylor coefficients of f(x+t),
       i.e. they are exactly the defining equations of the truncated arc space
       of the hypersurface y = f(x): a point (r, r^{(1)}, …, r^{(m)}) of the
       m-th jet scheme satisfies D_i f(r) = 0 for i = 0..m, where D_i are the
       Hasse–Schmidt derivations. So the CA hypothesis "f(r_i) = f^{(i)}(r_i) = 0
       for some r_i, each i" is a statement about which strata of the truncated
       jet schemes J_m of the incidence variety are nonempty. The proposal:
       reformulate CA as a dimension/gluing statement on J_m — the n−1 conditions
       force the witness points r_i to glue into the single (n−1)-jet at one
       point, which is exactly "f is an n-th power". Named machinery: Mustaţă's
       dimension formulas for jet schemes of lci/canonical singularities,
       Denef–Loeser motivic integration, and the Hasse–Schmidt-derivative
       description of jet schemes (Vojta).
mechanism: For fixed n the CA scheme X_n ⊂ A^{n−1} × A^{n−1} (coefficients
       a_1..a_{n−1} and witness roots r_1..r_{n−1}, cut out by f(r_i)=H_i f(r_i)
       =0) projects to the coefficient space; CA says the projection's image is
       the pure-power curve. Jet schemes turn this into a higher-order problem
       whose *dimensions* are governed by known formulas: dim J_m of a
       hypersurface singular locus is controlled by the log-canonical threshold
       / minimal exponent (Mustaţă's theorem), and the difference dim J_m −
       (m+1) dim X detects exactly how much room the witness tuple
       (r_1,…,r_{n−1}) has to avoid the diagonal. The bet is that the incidence
       variety's jet schemes over Q have the dimension of the pure-power locus
       only, i.e. dim J_m(X_n) is forced to its diagonal value by the n−1
       conditions, whereas over F_p the jet equations (divided powers / Hasse–
       Schmidt) degenerate and the dimension jumps — the char-p witnesses live in
       the jump. The char-0 content is the divided-power structure of the jet
       algebra: over Q the i-th jet coordinate carries H_i f with its full
       degree, over F_p the ordinary-derivative relation f^{(i)} = i! H_i f
       collapses at i ≥ p.
status: proposed
first-step: (1) tool_builder, exact sympy/Singular: build the truncated jet
       algebra J_m of the CA incidence scheme for n = 4, 5 and m = 1, 2, 3
       (variables a_1..a_{n−1}, r_i, and their jet coordinates; equations are
       the Hasse-derivative compositions of f(r_i) and H_i f(r_i)), compute
       dim J_m over Q, and compare with dim of the pure-power (diagonal) locus.
       (2) Repeat over F_p for the bad primes {3,5,7} (n=4) and {2,3,7,11}
       (n=5) and locate the dimension jump where the char-p witness appears.
       (3) State Mustaţă's dim-J_m formula precisely (sourced) and check whether
       the observed Q-dimension equals the formula's prediction, as the oracle
       guard for trusting the jet route.
precedent: none. No approach in this run uses jet schemes, arc spaces, motivic
       integration, or the Hasse–Schmidt description of jets. The adopted
       `deformation-obstruction-bad-points` line lifts char-p witness *points*
       to Z_p (flatness/liftability of a point); this line is higher-order
       thickening over the *same* field (jets of the whole scheme), a different
       object.
charp-break: named and located. Jet schemes in positive characteristic are
       built from HASSE–SCHMIDT (divided-power) derivations, not the ordinary
       derivative; the identity f^{(i)} = i!·H_i f fails once p | i!, i.e. for
       i ≥ p. So the equations of J_m differ over Q and over F_p in exactly the
       degrees where the char-p counterexamples exist (H_i ≡ 0 for i ≥ p): the
       dimension jump of J_m over F_p is the precise locus of the false
       char-p statement. An argument that did not distinguish the two divided-
       power structures would survive the char-p test and is therefore wrong.
```

## What is known and what is speculative

- **Sourced (named, exact statements to be fetched):** Mustaţă's dimension
  formula for jet schemes of a hypersurface in terms of the minimal exponent /
  log-canonical threshold; Vojta's "jets via Hasse–Schmidt derivations"
  establishing that the jet algebra of a scheme is the Hasse–Schmidt algebra.
- **Definitional (Hasse derivative = Taylor coefficient):** f(x+t) = Σ H_i f(x) t^i.
  This is the *definition* of the Hasse derivative and is the bridge from the
  derivative tower to the arc space.
- **Speculative (the bet):** that dim J_m(X_n) over Q equals the diagonal value
  for all m, and the n−1 conditions are what kill the off-diagonal part. Unproved;
  the first step measures it at n=4,5 before anything larger.

## Why it is not a closed approach

`tropical-resultant-fan` (refuted) worked with the Gröbner fan / initial ideals
of the resultant ideal and died on a false emptiness premise and fan cost.
`milnor-local-multiplicity` (refuted) was the local topological degree of the
CA ideal. `osculating-curve-wronski` (adopted) is the Wronski map on Gr(n,n+1).
None of them is the arc space / jet scheme of the incidence variety, and none of
them uses the fact that the Hasse derivatives are jet coefficients — that
identification is this line's whole engine.
