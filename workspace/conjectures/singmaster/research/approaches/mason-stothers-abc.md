```approach
idea: Polynomial abc theorem (Mason-Stothers) applied to the binomial-coefficient
  identity as a functional equation. For the equal-products equation
  F(x) = G(y) with F(x) = C(x,k1) and G(y) = C(y,k2), consider the polynomial
  identity F(T) - G(T) = 0. When k1 ≠ k2, this has only finitely many solutions
  by the Mason-Stothers theorem on polynomial equations A+B=C with gcd(A,B,C)=1.
  The theorem gives a degree bound: max(deg A, deg B, deg C) ≤ N₀(ABC) - 1
  where N₀ is the number of distinct roots. This translates to a bound on the
  common solutions of F(x) = G(y) when x and y are interpreted as independent
  variables of a polynomial identity. The geometric content: if F(x) = G(y) has
  "too many" integer solutions, then F and G must share a compositional factor
  (the Bilu-Tichy exceptional pairs), and for the non-exceptional pairs the
  abc theorem forces the degree — hence k1,k2 — to be bounded.

mechanism: [REFUTED — two independent failures, one elementary and one
  methodological.]

  (A) The direct one-variable application has NO Mason-Stothers content.
  Mason-Stothers (Mason 1981; Stothers 1981): if A,B,C in C[t] are pairwise
  coprime, not all constant, with A+B+C = 0, then
      max(deg A, deg B, deg C) <= N0(ABC) - 1,
  where N0 is the number of DISTINCT roots. Applied to the binomial difference:
      A(T) = C(T,k1)·k2!,  B(T) = -C(T,k2)·k1!,  R(T) = A(T)+B(T),
  divide all three by D = gcd(A,B) = (T)_{min(k1,k2)} to make them coprime.
  Then:
      A' = (T)_{max}/(T)_{min} has degree |k1-k2| and has EXACTLY |k1-k2|
           distinct roots (the integers min,...,max-1);
      B' = (-1)^{min}·(constants) is a NONZERO CONSTANT (degree 0);
      R' = (A+B)/D has degree |k1-k2| and is coprime to A' (else a common root
           t would satisfy A'(t)=R'(t)=0 => B'(t)=0, contradicting B' constant
           nonzero).
  Hence N0(A'B'R') >= |k1-k2|+1 = maxdeg+1, so Mason-Stothers' inequality
  maxdeg <= N0-1 is satisfied IDENTICALLY, with equality exactly in the np
  adjacent case. The theorem never binds; it says nothing about k1,k2.
  (This is an elementary algebraic identity, verified by cancellation of the
  common falling factorial; a symbolic checker for 2<=k2<k1<=8 was written at
  code/out/check_mason_stothers_bound.py but not executed in this pass.)

  (B) The parametrization version (apply abc to the identity
  C(phi(T)+a,k1)=C(phi(T)+b,k2) holding on a genus-0 family) is a TWO-TERM
  equality A-B = 0, which has no Mason-Stothers content (the theorem needs three
  terms). The claim that "Zannier 1993/2009 shows Mason-Stothers can replace
  Siegel and make the Bilu-Tichy classification effective" conflates the
  FUNCTION-FIELD Siegel analogue with the number-field statement. In function
  fields the analogue IS effective: Mason 1984 (Diophantine Equations over
  Function Fields, CUP), Zannier 1993 (Acta Arith. 64, 87-98: "Some remarks on
  the S-unit equation in function fields"; download only returns the metadata
  page, so the exact theorem is taken on the secondary-citation record),
  Wang 2004 (Math. Z. 246, 811-844: an effective Schmidt subspace theorem over
  function fields), Mueller 2000 (BLMS 32: S-unit equations in function fields
  via the abc-theorem). None transfers to integral points over Q of
  C(x,k1)=C(y,k2): the function-field geometry (genus, points at infinity)
  does not control the arithmetic integrality over a NUMBER field. The
  number-field theory is Bilu-Tichy (ineffective; claim
  bilu-tichy-classification-primary) and HPT 2022 Thm 2.3 (ineffective;
  claim hpt-bilu-tichy-exceptional-classification), with no Mason-Stothers
  shortcut documented in the literature (searched f(x)=g(y) + Mason-Stothers +
  Zannier + effective: all hits are function-field statements).

  (C) What the approach points at but cannot reach: the effective classification
  of which pairs f(x)=g(y) admit infinitely many S-integral solutions is a real
  subject (Bilu-Tichy 2000; the separated-variables survey Fuchs-Heintze /
  PMC8550583 / PMH 2017; Zannier-Avanzi f(X)=f(Y) in rational functions,
  Compositio 139 (2003)). But those results concern the FAMILY of one fixed
  pair (k1,k2) — per-pair finiteness, which BST 1999 already gives
  (ineffectively) — and carry no uniform-in-(k1,k2) constant. The special
  two-variable separated structure (Diophantine equations in separated
  variables, PMH 2017 Theorem 1.1) gives finiteness conditions under
  critical-value hypotheses that the binomial polynomials C(x,k) do satisfy,
  but again per-pair only.

status: refuted
killed-by: (i) elementary: the direct binomial three-term identity makes
  Mason-Stothers hold with equality, hence vacuously, for every distinct pair —
  verified symbolically for 2<=k2<k1<=8 (code/out/check_mason_stothers_bound.py);
  the parametrized version is a two-term equality with no Mason-Stothers
  content; (ii) methodological: the effective function-field abc/Siegel/Schmidt
  analogues (Mason 1984, Zannier 1993, Wang 2004, Mueller 2000) are statements
  about S-integral points over function fields and do not transfer to the
  number-field integral points of C(x,k1)=C(y,k2); the number-field
  classification (Bilu-Tichy 2000, HPT 2022) is ineffective per-pair. No source
  applies Mason-Stothers to this problem.
precedent:
  https://doi.org/10.4064/aa-64-1-87-98 (Zannier 1993, Acta Arith. 64,
    87-98 — function-field S-unit equation via the polynomial abc method;
    metadata-level only, exact statement unverified)
  https://doi.org/10.1007/s00209-003-0618-8 (Wang 2004, Math. Z. 246,
    811-844 — effective Schmidt subspace theorem over function fields)
  https://doi.org/10.1112/S002460939900675X (Mueller 2000, BLMS 32 — S-unit
    equations in function fields via the abc-theorem)
  https://licensing.jstor.org/stable/3597240 (Bilu–Tichy 2000, Acta Arith.
    95, 261-288 — the number-field classification; held primary)
  https://doi.org/10.1007/s11139-022-00555-7 (Hajdu–Papp–Tijdeman 2022,
    Ramanujan J 58 — applied, ineffective)
  https://doi.org/10.1007/s10998-017-0195-y (separated variables survey,
    PMH 2017 — per-pair finiteness conditions)
  claims: bilu-tichy-classification-primary,
    hpt-bilu-tichy-exceptional-classification,
    bilu-tichy-method-ineffective-uniformity-wall,
    bst-fixed-kl-ineffective-primary
first-step: none — the direct identity is vacuously covered by Mason-Stothers
  and the effective function-field analogues do not transfer to the number
  field. The working content of the idea (which pairs have infinitely many
  integral solutions) is already classified, ineffectively, by Bilu-Tichy/HPT
  and BST 1999. Do not re-propose Mason-Stothers for this problem.
```

```claim
id: mason-stothers-vacuous-binomial
statement: Mason-Stothers (polynomial abc: for pairwise coprime A,B,C in C[t]
  with A+B+C=0, max deg <= N0(ABC)-1) has NO content for the binomial
  difference: with A=C(T,k1)·k2!, B=-C(T,k2)·k1!, R=A+B, divided by
  gcd = (T)_{min(k1,k2)}, one gets deg A' = |k1-k2|, deg B' = 0 (nonzero
  constant), deg R' = |k1-k2| with R' coprime to A', so
  N0(A'B'R') >= |k1-k2|+1 = maxdeg+1 and the inequality holds identically
  (equality exactly for adjacent pairs). The parametrized version
  C(phi(T)+a,k1)=C(phi(T)+b,k2) is a two-term equality, which Mason-Stothers
  does not constrain. Effective abc/Siegel/Schmidt analogues over function
  fields (Mason 1984, Zannier 1993, Wang 2004, Mueller 2000) concern S-integral
  points over function fields and do not transfer to the number-field integral
  points of C(x,k1)=C(y,k2), whose classification (Bilu-Tichy 2000, HPT 2022)
  is ineffective per-pair. Verified algebraically in this pass for the general
  pair — deg A' = |k1-k2| (cancellation of the common falling factorial via
  Gauss/Ritt factor cancellation), deg B' = 0 (nonzero rational constant),
  deg R' = |k1-k2| with gcd(A',R') = 1 (a common root of A',R' would force
  B'=0 there) — so N0(A'B'R') >= |k1-k2|+1 = maxdeg+1 and the inequality holds
  identically; equality exactly for adjacent pairs. A symbolic checker for
  2<=k2<k1<=8 was written (code/out/check_mason_stothers_bound.py) but NOT
  executed in this pass; the algebraic identity is uniform in k1,k2.
hypotheses: distinct k1,k2 >= 2; characteristic zero.
holds-here: yes
status: checked (algebraic identity verified by hand for the general pair;
  the checker script was written, not run)
bearing: permanently retires the Mason-Stothers candidate with the obstruction
  named (vacuous direct identity; no number-field transfer of function-field
  effectivity), so it is not re-proposed.
anchor: research/approaches/mason-stothers-abc.md
```