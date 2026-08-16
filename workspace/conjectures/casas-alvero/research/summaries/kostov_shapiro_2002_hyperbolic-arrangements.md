# Kostov–Shapiro, *On arrangements of roots for a real hyperbolic polynomial and its derivatives* (2002, arXiv:math/0204272)

<!-- source: https://arxiv.org/pdf/math/0204272 | PDF held in full -->

## What this source is

A classical real-analytic/real-algebraic geometry paper, cited by the run's
held Laterveer–Ounaïes constraints paper (as reference [9]) and by the Polish
school on root arrangements. It answers, for **real polynomials**, the
combinatorial question of which interleavings of the roots of P and of its
s-th derivative P^{(s)} are actually realizable — the question that underlies
the real-rooted case of CA.

## What it establishes

For a real polynomial P = x^n + a_1 x^{n-2} + … + a_{n-1} (hyperbolic = all
roots real), an **arrangement** is a chain of the roots of P and P^{(s)}
(1 ≤ s ≤ n−1) with consecutive roots related by = or <.

- **Theorem 6**: All a priori admissible root arrangements are realizable by
  real polynomials of degree n. "Admissible" means consistent with Rolle's
  theorem and "some other natural restrictions". So the only obstructions to a
  joint root-interleaving of P and P^{(s)} (over the reals) come from Rolle.
- When P has real simple roots and no common root with P^{(k)}, the *only*
  restriction on the joint arrangement is the standard Rolle theorem; and each
  permissible stratum is a smooth, contractible real algebraic variety.
- Proposition 4: a root of P of multiplicity d coinciding with a root of
  P^{(s)} (structure near coincidence); Lemma 8: real-analytic deformations
  through which arrangements live in the closure of others.
- The results are a first step toward studying the real discriminant sets
  {a ∈ R^{n−1} : Res(P,P^{(s)})=0}.

## Bearing on this run

- Supplies the classical reference the run's **real-rooted thread** cites
  (Kostov–Shapiro is reference [9] in the held Laterveer–Ounaïes paper, and
  underlies the "real-rooted ⇒ CA" restricted class that problem.md mentions
  and that Yakubovich develops via Abel–Goncharov polynomials).
- The "only obstruction is Rolle" statement is the real-variable analogue of
  what the root-difference-coloring / Abel–Goncharov machinery does in the
  complex case — it says why, over the reals, the interleaving constraints are
  so rigid that CA collapses. It does NOT transfer to char p (real topology is
  a char-0 phenomenon), which is consistent with the run's char-p-break
  analysis.

## Status

Peer-reviewed classical result (the arXiv math/0204272 version; a version
appeared in Bull. Sci. Math. 2002, matching the reference in the Laterveer–
Ounaïes bibliography). Durable, not a claimed proof.

## Caveat / what it does NOT give

It is about **which arrangements are realizable**, i.e. that most interleavings
are possible — the opposite direction from CA's constraint. It does not itself
prove the real-rooted case of CA; that requires additionally that a
CA-polynomial's arrangement be forced into the all-equal pattern, which is what
Yakubovich's Abel–Goncharov arguments add. So this source is background for the
real-rooted thread, not a settled-class result by itself.
