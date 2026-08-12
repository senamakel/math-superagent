# MIS-FILED — replaced (summary of the correction)

**This entry previously described Shelah, "What majority decisions are
possible" (arXiv:math/0405119) as though it were a hyperplane-arrangements
source — it was NOT.** The Shelah paper is an unrelated combinatorics/social
choice paper; it has been re-filed at its honest identity:
`research/sources/shelah_majority_decisions_math0405119.full.md`.

The genuine source under this name is Stanley's **"An Introduction to
Hyperplane Arrangements"** (IAS/PCMI 2004 lecture notes, published in
Geometric Combinatorics, IAS/Park City Math. Series 13 (2007) 389–496),
filed at `research/sources/hyperplane_arrangements_stanley_ias_pcmi.full.md`
with URL https://static.ias.edu/pcmi/2004/program/Stanleynotes.pdf.

**What the genuine source establishes (Zaslavsky's theorem, Theorem 2.5):
for a real hyperplane arrangement A in R^n with characteristic polynomial
χ_A(t) (defined via the Möbius function of the intersection poset L(A)):**

- r(A) = (−1)^n χ_A(−1) — the number of regions (connected components of
  R^n \ ∪A) is given by the characteristic polynomial evaluated at −1;
- b(A) = (−1)^rank(A) χ_A(1) — the number of relatively bounded regions by
  evaluation at 1;
- r(A) and b(A) depend only on the intersection poset L(A) (Corollary 2.1).

**Bearing on PE597:** the run's parity-region argument asserts the separating
hyperplanes (v_a=v_b and event-time equalities, all linear in the normalized
speed simplex) form a hyperplane arrangement whose even-parity cells can in
principle be summed by simplex-section volumes. Zaslavsky's theorem gives the
canonical bound r(A) = |χ_A(−1)| on the number of cells from the arrangement's
intersection poset — the named justification that region count is controlled
by the combinatorial structure, not by enumeration of bump outcomes. The run's
own enumeration (n=4: 1202 cells; n=5: ~13,750) shows the practical constant
still explodes for naive cell enumeration; Zaslavsky bounds the geometry, not
the solver's cost.