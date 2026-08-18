# Lu algebraic core versus analytic zero bound — refutation report

## Target
The attacked implication was: the verified finite Bautin identities (degree-4 and degree-6 focal obstructions, including the P30 relation) by themselves support a locally uniform analytic zero bound for the H^3_14 displacement.

## Hand attack
The smallest obstruction is structural, not numerical. Polynomial identities among finitely many Taylor/focal coefficients do not imply any of the following load-bearing facts:

1. the displacement germ is defined on one common parameter/phase neighborhood;
2. the displacement is not identically zero on every non-center parameter direction;
3. the first-hit itinerary and its domain are physically exhaustive;
4. the normalized displacement has a parameter-uniform finite order after division by the center ideal;
5. the resulting analytic germ has a uniform Weierstrass degree.

A trivial analytic countermodel to the implication is `D(s,lambda)=0` for all `(s,lambda)`: all polynomial coefficient identities hold, but there are no isolated zeros and hence no zero-bound theorem of the claimed intended kind can be extracted from the identities. More damagingly, analytic families such as `D(s,t)=exp(-1/t^2) sin(s/t)` for `t>0`, extended by `D(s,0)=0`, show that even smooth parameter dependence and vanishing of any prescribed finite jet do not yield a uniform zero count without analyticity in a common rescaled chart and a nonidentity hypothesis. This is a logical countermodel to the proposed implication, not a counterexample to Lu's quadratic vector-field theorem.

## Workspace/source check
Lu's preprint explicitly separates the algebraic recurrence from the analytic argument. The source says the theorem additionally needs stopped first-hit geometry, common physical domains, center division, analytic regime classification, and local zero theorems (source lines 57–69, 330–390, 390–430, 470–525, 560–680). Its compact analytic-word theorem invokes Noetherianity, principalization, and Weierstrass preparation only after a bounded jointly analytic word and a nonidentity/projective-direction assertion are supplied (lines 510–525). Thus the finite algebraic core is not presented by the source as sufficient.

The center-domain proof itself states the missing domain hypothesis: division is allowed only for a displacement defined on a word domain star-shaped under the relevant contractions and vanishing on both complete center slices (lines 640–675). The later assembly assumes all local zero theorems before compactness (lines 470–525). These are exactly hypotheses not certified by the Bautin identities.

## Mechanical refutation attempt
TPTP problem: `code/refute/lu_core_zero_bound.p`. It encodes the two algebraic identities as axioms and the purported finite-zero-bound conclusion as conjecture. `find_counterexample` returned:

`undecided; SZS status: none reported`.

This is not evidence that the implication is true: the conjecture is not faithfully first-order formalised (`finite_zero_bound` and `displacement` are uninterpreted), so the model result cannot address Lu's mathematical theorem. No counterexample to the original quadratic-family statement was found.

## Verdict
**Refuted as a sufficiency claim; surviving only with additional analytic hypotheses.** The algebraic core is verified, but it supports an analytic zero bound only conditionally on the source's independent hypotheses: common jointly analytic first-hit domains, exhaustive finite itinerary assignment, valid center-ideal/Hadamard division, a nonidentity assertion on every nonzero projective parameter direction, and regime-specific zero theorems with uniform constants. The preprint's main theorem remains asserted/unrefereed and those bridges are not kernel-checked here.

## Search frame
The witness/countermodel lies in the class of abstract analytic germs and finite-jet algebraic constraints, not in the quadratic vector-field family; it is therefore outside any published exhaustive sweep of the 121 DRR graphics. The TPTP search reached no finite model for the deliberately uninterpreted encoding.
