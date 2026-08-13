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

mechanism: The effective quadratic Chabauty pipeline (Balakrishnan–Dogra et al.)
requires: (1) a plane model of the curve, (2) its Jacobian and its Mordell–Weil
group generators, (3) a prime p of good reduction, (4) computation of p-adic
height pairings and Coleman integrals. For the Bremner II Category VII curves,
all of these are achievable: the quartics are explicit (eq. 12-13), the genus
is computable, a 2-descent gives upper bounds on the Mordell–Weil rank, and p-adic
integration is implemented. The "hinge" is whether the quadratic Chabauty
condition r < g + ρ(J) − 1 holds; this is verifiable by computing the
Néron–Severi rank of the Jacobian (which for hyperelliptic Jacobians split from
a K3 fibration is often at least 2).

status: refuted (as a route for the 7→8 transition)
killed-by: the three Bremner II eq. (13) quartics at λ=13 — the explicit
  7→8-transition curves — all have GENUS 1, not genus ≥ 2. This run computed
  this directly (code/out/bremner2_quartics.txt: F(x) = Q(x,1) squarefree
  degree 4 with non-zero discriminant in each case; HyperellipticCurve route A
  and sympy discriminant route B agree: GENUS 1 for (13a),(13b),(13c)). Quadratic
  Chabauty — like classical Chabauty — is designed for genus ≥ 2 curves and the
  formula r < g + ρ(J) − 1 presupposes g ≥ 2 (for g = 1 it would read
  r < 1 + ρ − 1 = ρ, which says nothing beyond the elliptic case). For genus-1
  curves the correct tool is ordinary elliptic 2-descent/Selmer on E: y²=F(x),
  not Chabauty–Kim. So the candidate's "fallback when classical Chabauty fails"
  never engages: classical Chabauty never engages either, because neither the
  classical r<g nor the quadratic r<g+ρ−1 hypothesis is relevant to elliptic
  curves. The correct per-curve target is a rational point on E: y²=F(x) lying
  on both (12) and one of (13); Bremner's search (p+q+n(λ)+d(λ) ≤ 1000) already
  found no such point beyond the λ=13,(p,q)=(9,2) witness.

  This refutation is about the 7→8 transition specifically. Quadratic Chabauty
  as a general technique is real, published and grounded (see precedent), but
  its object here — the eq. (13) curves — is genus 1, so the technique's
  hypotheses (curve of genus ≥ 2) fail for the exact curves the approach
  proposed to run it on. Any 7→8 analysis must instead use elliptic-curve
  methods on Y²=F(x) (2-descent, elliptic Selmer, BSD parity), which are the
  subject of the root-number-parity-four-curves candidate.

speculation-vs-established: ESTABLISHED (literature): quadratic Chabauty /
  Chabauty–Kim is a real theorem family with the r < g + ρ(J) − 1 criterion;
  Balakrishnan–Dogra–Müller–Tuitman–Vonk and later works prove and implement
  it for genus-2 (and higher) curves. ESTABLISHED (this run, checked): the
  eq. (13) quartics at λ=13 are genus 1 (bremner2_quartics.txt). REFUTED
  (by that combination): the candidate's decisive hypothesis r < g + ρ(J) − 1
  is not the right question for genus-1 curves; the approach's object is not
  a genus-≥2 curve. The speculation that "the curves' Jacobians carry enough
  extra structure (ρ(J) > 1) for quadratic Chabauty to apply" never gets off
  the ground because the curves are elliptic.

precedent:
  - M. Kim, "The motivic fundamental group of P¹∖{0,1,∞} and the theorem of
    Siegel", Invent. Math. 161 (2005); M. Kim, "The unipotent Albanese map and
    Selmer varieties for curves", Publ. RIMS (2009) — foundations of
    Chabauty–Kim.
  - J. Balakrishnan, N. Dogra, "Quadratic Chabauty and rational points I:
    p-adic heights", Duke Math. J. 167 (2018) 1981–2038 — the depth-2 method and
    the r < g + ρ(J) − 1 criterion for genus-2 curves.
  - J. Balakrishnan, N. Dogra, J.S. Müller, J. Tuitman, J. Vonk, "Explicit
    Chabauty–Kim for the split Cartan modular curve of level 13", Ann. of Math.
    189 (2019) — the first full non-abelian Chabauty computation (genus ≥ 2).
  - Geometric quadratic Chabauty, Expositiones Math. 41 (2023) 631–674
    (sciencedirect S0723086923000452) — same r < g + ρ − 1 criterion,
    genus > 1 hypothesis.
  - This run: code/out/bremner2_quartics.txt (genus 1 for all three eq.(13)
    quartics at λ=13, two independent routes).
  - No published application of quadratic Chabauty to the MSS curves exists;
    the closest are the general genus-2 rational-point computations (e.g. the
    quadratic-Chabauty classification of hyperelliptic Atkin–Lehner quotients,
    Res. Number Theory 2022). None of these is this problem's curve, and the
    MSS curves are genus 1 anyway.
first-step: none for quadratic Chabauty. The correct next step for the 7→8
  transition is elliptic 2-descent/Selmer on E: y²=F(x) for the three eq.(13)
  quartics, i.e. the mechanism of root-number-parity-four-curves, not
  Chabauty–Kim. Recorded so nobody re-proposes Chabauty (classical or
  quadratic) on genus-1 MSS curves.
```
