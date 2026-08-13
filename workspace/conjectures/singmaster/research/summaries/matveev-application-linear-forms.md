# Matveev-application template — L_n + L_m = 3^a (Tiebekabe–Diouf 2021)

Source: P. Tiebekabe, I. Diouf, "On solutions of the Diophantine equation
L_n + L_m = 3^a", Malaya J. Mat. 9(02) (2021) 1–11, doi:10.26637/mjm902/001.
HAL preprint https://hal.science/hal-03243010 (downloaded as
`research/sources/matveev-application-linear-forms.full.md`).

## What this source is (and what it is not)

This is a **worked template for applying Matveev's explicit lower bound for
linear forms in logarithms** to an exponential Diophantine equation — not a
binomial-coefficient paper. Its value for this run is methodological: it shows
the exact pipeline (translate equation to a linear form in logarithms → apply
Matveev's theorem with its explicit constants → reduce with continued
fractions via Dujella–Pethő) that GOAL.md's "effective height bound with a
computed constant for a specific (k1,k2) family (Baker / linear forms in
logarithms)" partial-result option would follow. It is a secondary reference
for the Matveev theorem statement.

## Statements it uses (converted from its §2)

- **Theorem 2.9 (Matveev [8])**: Let n ≥ 1, L a number field of degree D,
  η1,…,ηl nonzero in L, b1,…,bl integers with B = max|bi|. If
  Λ = η1^b1 ··· ηl^bl ≠ 1, then the explicit lower bound
  `ln|Λ| > − C(l,D) · (log B + ...)` holds with the standard Matveev-type
  constants (the digest shows the theorem in the paper's own notation; the
  concrete inequality is at the paper's Theorem 2.9).
- **Lemma 2.10 (Dujella–Pethő)**: continued-fraction reduction: if p/q is a
  convergent of κ with q > 6M and ε := ‖μq‖ − M‖κq‖ > 0, then an explicit
  inequality has no solution — the computational reduction step that turns a
  Matveev bound into a finite check.
- **Lemma 2.11 (Legendre)**: rational approximation criterion.
- **Theorem 3.1**: the only solutions of L_n + L_m = 3^a in nonnegative
  integers n ≥ m, a are (1,0,1) and (4,0,2). Lemma 3.2 bounds a ≤ n+2 <
  1.2×10^20 for n > 200 — this is the "explicit computed constant" that
  Matveev's bound produces before the continued-fraction reduction to
  n ≤ 200.

## Bearing for the run

- Confirms the **exact tool chain** for an effective-Baker bound on a specific
  curve family: Matveev (2000) explicit bound + Dujella–Pethő continued
  fraction reduction. For the run's small-`k` curves (e.g. C(x,2)=C(y,k)
  hyperelliptic family) the same chain is what a computed constant would look
  like, and this source shows the constants are concrete numbers.
- The Matveev theorem statement here (Theorem 2.9) is quoted but not itself
  the original primary (Matveev 2000, Izv. Math. 64); for the library to
  cite the constants authoritatively it should hold Matveev's paper or a
  standard transcription (e.g. Bugeaud's book). That remains a gap for the
  effective-bound thread — record in REQUESTS.md.
- Also cites Laurent–Mignotte–Nesterenko two-log bound and Bugeaud–Mignotte–
  Siksek modified Matveev, both standard alternatives.

```claim
id: matveev-application-template
statement: Tiebekabe-Diouf 2021 solve L_n + L_m = 3^a completely (only
  (4,0,2) and (1,0,1)) using the standard effective pipeline: reduce to a
  linear form in two logarithms, apply Matveev's explicit lower bound (their
  Thm 2.9; constants concrete) to get a <= n+2 < 1.2e20 for n > 200, then
  Dujella-Petho continued-fraction reduction to finish. This is a working
  template for an effective Baker-type bound with a computed constant on a
  specific exponential Diophantine family.
hypotheses: two-term exponential equation; algebraic numbers of bounded
  degree/height.
holds-here: yes as a template — the run's small-k binomial-equality curves
  reduce to similar exponential/logarithmic forms; the specific L_n+L_m = 3^a
  equation is NOT the run's equation.
status: asserted-by-source (full text held)
bearing: shows the shape of a deliverable "effective bound with computed
  constant"; the Matveev primary is now held at
  research/sources/matveev-2000-homogeneous-linear-form.full.md (claim
  matveev-2000-explicit-constants-primary) for the authoritative constants.
anchor: research/summaries/matveev-application-linear-forms.md
```