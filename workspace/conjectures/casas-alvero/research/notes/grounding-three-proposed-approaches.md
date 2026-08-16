# Grounding of three proposed approaches: moment-hankel-rank, hessian-covariant-transvectant, q-derivative-deformation

What the literature says about each of the inventor's three candidate lines,
with verdicts. This is evidence for the approach files; it does not settle CA.

## 1. moment-hankel-rank — REFUTED (not a new object)

The classical fact is true and standard: a finite Hankel matrix built from
power sums of a weighted point measure has rank equal to the number of distinct
atoms (Pólya/Kronecker; flat extension Curto–Fialkow in the PSD setting). So
"pure power ⟺ rank-1 Hankel" is correct.

But the advertised premise — "a different matrix from every one the run owns" —
is false. Power sums and elementary symmetric functions are equivalent by
Newton's identities, so the "moment matrix" is the same data as the run's owned
root-difference identity H_i(f)(β_j) = e_{n−i}(β_j−β_*). And the published CA
literature already works in exactly this language:
- Laterveer–Ounaïes, arXiv:1204.0450, use Newton formulas on the power sums
  σ_m(l) of the roots of the derivatives (their Lemma 2, center-of-mass
  result).
- Castryck–Laterveer–Ounaïes, arXiv:1208.5404 (§3, Theorem 2), organise the
  degree-(p+1) counterexample constraints around a Hankel-type determinant Δ_f
  (eq. 2) that must vanish mod p.

The load-bearing bridge "CA ⟺ the disjunctions force rank H = 1" is exactly CA
itself: rank H = 1 ⟺ pure power, so "force rank 1" IS "force a pure power".
No reduction. The char-p break claim is correct (the 2-root witness has a
rank-2 moment matrix, and the Lucas-vacuous middle Hasse derivatives impose no
link), but a correct break does not supply the missing reduction.

## 2. hessian-covariant-transvectant — REFUTED (true theorem, unproved bridge)

The classical theorem is real and sourced: a homogeneous binary form F of
degree n is a perfect n-th power of a linear form iff its Hessian (second
transvectant (F,F)_2) vanishes identically. This is the r=1, µ=d case of the
Hilbert covariant in Abdesselam–Chipalkatti, "On Hilbert covariants", Canad. J.
Math. 64(5):975-994 (2012), doi:10.4153/cjm-2012-046-1 (arXiv:1010.2358), where
they prove the coefficients of the covariant cut out the perfect-power locus
scheme-theoretically.

However, NO source applies binary-form covariant/transvectant theory to the CA
derivative-sharing system. The bridge "the derivative-sharing conditions force
(F,F)_2 = 0" is the proposal's own unproved conjecture. This is the same reason
the sibling catalecticant-apolarity line was refuted in this run: the apolar
ideal of a generic binary form is generated in two degrees, so the n−1
derivative resultants are not a coordinated ladder of one covariant sequence.
The char-p break is genuinely located (the Hessian theorem divides by
factorials / integrates over char 0; for x^{p+1}−x^p over F_p the homogenised
form has vanishing Hessian yet is not a pure power), satisfying the admissibility
test, but a located break does not supply the missing inference.

## 3. q-derivative-deformation — PROPOSED, speculative (no evidence either way)

The q-derivative / Gaussian-binomial machinery exists and is well-developed
(Jackson q-derivative, q-binomial theorem, Gaussian Riemann derivatives — e.g.
Ash–Catoiu, Israel J. Math. 2022 — q-Rogers–Szegő polynomials). But NO source
has ever applied any of it to the CA problem; there is no q-Casas-Alvero
conjecture, no q-analogue of the derivative-sharing rigidity in the record.

So this proposal can neither be grounded (no precedent) nor refuted (no failed
attempt to refute). The honest verdict is proposed/speculative, precedent
empty. Its value is the cleanest char-p break of the three — a parameter
specialisation (q→1 mod p = Lucas collapse) rather than an after-the-fact
search — but that is a structural property of the family, not evidence the
family is easier. The load-bearing and unproved step is the specialisation
argument: "empty counterexample locus over Q(q) forces empty at q=1" is a
constructible-set claim that must itself survive the reducible nature of the
counterexample locus.

## What would run next (if pursued)

The draft code/research_grounding/verify_three_candidates.py encodes the exact
facts that would be checked (Hankel rank = #distinct roots at n=4,5,6 and on the
char-p witness; Hessian ≡ 0 ⟺ pure power in char 0; the Lucas collapse of the
Gaussian-binomial middle colours). It is UNVERIFIED and has never been run — it
exists as a proposal for a tool_builder/coder run, not as a measurement. All
three verdicts above rest on the cited sources, not on that script.

## Sources

- Laterveer–Ounaïes, arXiv:1204.0450 (Newton power sums, center of mass)
- Castryck–Laterveer–Ounaïes, arXiv:1208.5404 (§3 Δ_f Hankel-type determinant)
- Graf von Bothmer et al., 10.1016/j.jalgebra.2007.06.017 (weighted projective
  scheme X_d over Z; the q/reduction framing's home)
- Abdesselam–Chipalkatti, "On Hilbert covariants", Canad. J. Math. 2012,
  doi:10.4153/cjm-2012-046-1 / arXiv:1010.2358 (Hessian ⟺ perfect power,
  scheme-theoretic)
- Ash–Catoiu / Israel J. Math. 2022 (Gaussian Riemann derivatives as the
  q-machinery, not CA)
