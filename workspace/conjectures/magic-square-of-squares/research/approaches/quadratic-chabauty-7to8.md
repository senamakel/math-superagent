# Approach: Quadratic Chabauty for the Bremner II 7→8 transition curves

```approach
idea: When the classical Chabauty–Coleman method fails because the Jacobian
rank r equals or exceeds the genus g, the next-generation method is **quadratic
Chabauty** (also "Kim's non-abelian Chabauty" or the "Chabauty–Kim method").
Developed by Minhyong Kim (2005, 2009) and made algorithmic by
Balakrishnan–Dogra–Müller–Tuitman–Vonk (2018, 2019), this method uses the
unipotent fundamental group, p-adic Hodge theory, and Coleman integration on
the Selmer variety to compute rational points on curves of genus ≥ 2 even when
r ≥ g. The key insight: the rational points C(Q) inject into a "Selmer
variety" cut out inside a non-abelian cohomology set H¹_f(G_Q, U_n), where U_n
is a quotient of the Q_p-pro-unipotent fundamental group of C. For a curve of
genus g, one uses depth 2 (hence "quadratic") and the condition that the abelian
Coleman integrals satisfy a certain linear relation plus a quadratic condition
from the p-adic height pairing. When the "Mordell–Weil rank" r and the " Néron–Severi
rank" of the Jacobian satisfy r < g + ρ(J) − 1 (a refinement of r < g), the
method still works and produces a finite set containing C(Q).

The Bremner II Category VII 7→8 transition curves are canonical candidates:
they are explicit quartics with small coefficients, come from a specific
geometric construction (fibres of the K3's elliptic fibration at certain λ),
and their Jacobian ranks are computable by 2-descent. If r ≥ g for these curves
(so classical Chabauty fails), quadratic Chabauty may still apply because the
curves are hyperelliptic, their Jacobians are isogenous to products of elliptic
curves (as they come from the K3's Mordell–Weil lattice), and the additional
structure (endomorphism ring, real multiplication, or extra Néron–Severi rank)
gives ρ(J) > 1.

mechanism: The effective quadratic Chabauty pipeline (Balakrishnan–Dogra et al.)
requires: (1) a plane model of the curve, (2) its Jacobian and its Mordell–Weil
group generators, (3) a prime p of good reduction, (4) computation of p-adic
height pairings and Coleman integrals. For the Bremner II Category VII curves,
all of these are achievable: the quartics are explicit (eq. 12-13), the genus
is computable (likely 2 or 3), a 2-descent gives upper bounds on the
Mordell–Weil rank, and p-adic integration is implemented in SageMath
(Balakrishnan's toolkit). The "hinge" is whether the quadratic Chabauty
condition r < g + ρ(J) − 1 holds; this is verifiable by computing the
Néron–Severi rank of the Jacobian (which for hyperelliptic Jacobians split from
a K3 fibration is often at least 2).

This is a genuine escalation beyond the adopted classical Chabauty–Coleman
approach: if that approach hits r ≥ g, this one provides the next level of the
Chabauty hierarchy. And it is genuinely different from the
phi-triple-curve-genus-faltings approach (which attacks the Φ additive triple
directly, without passing through Bremner's hyperelliptic reduction).

status: proposed
speculation-vs-established: ESTABLISHED — the quadratic Chabauty (Chabauty–Kim)
  theorem and its Balakrishnan–Dogra et al. algorithmic pipeline are published,
  and the Bremner II eq. (12)-(13) quartics are explicit. SPECULATION — (a) the
  decisive condition r < g + ρ(J) − 1 holds for any of the three 7→8 curves;
  (b) the curves' Jacobians carry enough extra structure (ρ(J) > 1) for
  quadratic Chabauty to apply where classical Chabauty fails. Both are
  verifiable by a finite computation (genus, 2-Selmer rank, Jacobian
  splitting); if r ≥ g + ρ(J) − 1 for all three, the approach is closed with
  that negative result.
first-step: Compute the genus and the 2-Selmer rank for the three Bremner II
  eq. (13) quartics at λ = 13 (the 7-square witness parameters). If for any
  of those curves r ≥ g, determine whether ρ(J) > 1 by computing the
  endomorphism algebra of the Jacobian (or, for genus 2, whether J splits as
  a product of elliptic curves). If r < g + ρ(J) − 1, the quadratic Chabauty
  method applies and the 8th square condition is decidable for that
  configuration. If r ≥ g + ρ(J) − 1, this too is a result (it means even
  quadratic Chabauty fails for these curves).
precedent: M. Kim, "The unipotent Albanese map and Selmer varieties for curves"
  (2005), Publ. Res. Inst. Math. Sci.; M. Kim, "The motivic fundamental group
  and p-adic integration" (2009); J. Balakrishnan, N. Dogra, J.S. Müller,
  J. Tuitman, J. Vonk, "Explicit Chabauty–Kim for the split Cartan modular
  curve of level 13" (2019), Annals Math.; J. Balakrishnan, N. Dogra, "Quadratic
  Chabauty and rational points I: p-adic heights" (2018), Duke Math. J.;
  the Bremner II quartics are in research/sources/bremner-on-squares-of-squares-II-2001.full.md.
  No published application of quadratic Chabauty to the MSS curves is known to
  this library.
```