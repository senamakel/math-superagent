# Slow-divergence integral + ECT, aimed at one open center graphic

```approach
slug: slow-divergence-integral-ect
status: adopted
idea: Sum-of-Dulac-maps slow divergence integral + ECT zero counting, aimed at one open center graphic
mechanism: After RR 2015 blow-up, the displacement is a sum of four second-type Dulac maps; represent it as a slow divergence integral in a finite-dimensional Chebyshev space, then apply the GMV extended-Chebyshev criterion to reduce the zero count to Wronskians of rationals — Sturm-decidable over Q.
first-step: For the named graphic (I^1_6b), reproduce the Roussarie–Rousseau 2015 family blow-up symbolically in sympy (reversible-stratum normal form for a triple nilpotent point at infinity surrounding a center; successive weighted blow-ups to the singular 3-dimensional foliation) and compute the slow divergence integral *as the sum over the four second-type Dulac passages*, matching the published boundary-set computation as the validation check. Deliverable: an exact slow-divergence integral with its parameter dependence, stated in Lean-ready form, plus the Wronskian(s) of the resulting finite-dimensional space as rational functions over Q.
precedent: https://doi.org/10.3934/cpaa.2018.17.1305 ; https://doi.org/10.1090/S0002-9947-2010-05007-X ; https://doi.org/10.1016/j.jde.2013.01.036 ; https://doi.org/10.1007/s12346-017-0226-3 ; https://doi.org/10.1007/s12346-022-00609-7 ; claims: drr-huzak-df2a-closed, h16-grau-manosas-villadelprat-chebyshev-2010, drr-rr-boundary-only-for-3-graphics, drr-saddle-node-normalforms-dir2002
```

## Decision (post-research)

**Adopted.** This was the only candidate research grounded, and it is the one
whose finite core the run can already finish: the GMV extended-Chebyshev (ECT)
criterion is held, the computer-assisted Wronskian/Sturm discharge is held
(Figueras–Tucker–Villadelprat 2013), and Huzak 2018 is a published
working instance of the exact mechanism (family blow-up + slow divergence
integral closes DF₂ₐ). The other two candidates are refuted as *ready routes*:
the Newton-polyhedral line lacked the central uniform finite-type theorem, and
the Nevanlinna line lacked the family-uniform characteristic bound — in both
cases the missing step was the hard part itself, not a lemma in reach.

**What research surfaced that neither of us named:** the ECT machinery and the
slow-divergence mechanism are each individually *known* — the run already
adopted GMV/ECT for the tangential (first-order, period-annulus) problem, and
Huzak's DF₂ₐ already uses the slow-divergence mechanism for a degenerate
graphic. What is **new here is the combination and its target**: the *full*
displacement of an open center graphic, written as a **sum of four second-type
Dulac maps**, with the decisive unresolved case being the strata where the
slow divergence integral vanishes identically. That combination is the gap
between "grounded" and "a bound", and it is aimed at the three remaining full
graphics (I¹₆b, H³₁₃, DI₂b) whose boundary sets Roussarie–Rousseau 2015
already did (Theorem 1.1). This is not a re-proposal of the adopted
Picard–Fuchs route: the object is the full perturbation after slow–fast
blow-up, not a first-order Abelian integral over a period annulus.

## Literature assessment (research verdict, retained)

The established name is **slow divergence integral / slow–fast cyclicity**, with
the zero-counting refinement the **extended complete Chebyshev (ECT) property
of Abelian integrals**. The GMV criterion is precise: for the stated separable
Hamiltonian forms and involutions, if the balance functions satisfy the required
CT hypotheses (including the endpoint little-o condition), then the Abelian-integral
family is an ECT-system, so every nonzero linear combination has at most
dimension-minus-one zeros counted with multiplicity. The hypotheses are
structural, not automatic: one must identify the slow–fast blow-up, derive the
integral family, and prove the CT/Wronskian conditions. The computer-assisted
literature (Figueras–Tucker–Villadelprat 2013) reduces the Wronskian nonvanishing
to polynomial resultants and Sturm's theorem — a certificate-oriented finite core.

**Direct precedent:** Huzak 2018 (CPA 17) closes DF₂ₐ by family blow-up + slow
divergence integral, with explicit bounds in the DF₁ₐ/DF₂ₐ cases. Later slow–fast
work extends this to nilpotent contact points and canards, retaining explicit
regularity/nondegeneracy hypotheses.

**The named obstruction (from the run's own RR 2015 summary):** for the three
remaining full graphics the displacement does **not** reduce to a single equation.
(I¹₆b) involves **four Dulac maps of the second type** and cannot be reduced to a
single equation; (DI₂b) has four second-type Dulac maps through semi-hyperbolic
points. RR 2015 got the *boundary* limit periodic set (a 2-dimensional displacement
studied along an invariant foliation) but not the full graphics. The new line is
therefore: **the slow divergence integral as a sum over multiple Dulac passages**,
and the question of whether that sum — not a single passage — retains a finite
ECT/Chebyshev-type property whose Wronskian is Sturm-decidable.

## Application to this problem

The mechanism is validated at DF₂ₐ; the new claim to attack is that the *full*
displacement of one named open graphic is controlled by a finite ECT space after
blow-up, including the vanishing slow-divergence strata. The failure mode to hunt
as seriously as the proof: the sum of four second-type Dulac maps may leave the
Chebyshev class (a sum of ECT functions need not be an ECT system), in which case
the finite core is not a single Wronskian but a finite-rank module — and the run
must say so and name the larger space.

## Three tests

1. Smooth test: passes only for the analytic/algebraic slow–fast reduction and a
   proved displacement/integral relation; the ECT theorem is not a generic C∞
   result. The first-step computation must record exactly where analyticity is used.
2. Uniformity: supplied on a compact parameter region only after uniform blow-up
   charts, bounded integral dimension, and uniform Wronskian certificates are
   established.
3. Counterexample hunt: DF₂ₐ validates the mechanism; the unresolved
   vanishing/degenerate strata of I¹₆b, H³₁₃, DI₂b are the required first stress
   tests — the first-step's sum-of-four-Dulac-maps integral must be checked against
   the published boundary-set computation before any new zero count is trusted.
