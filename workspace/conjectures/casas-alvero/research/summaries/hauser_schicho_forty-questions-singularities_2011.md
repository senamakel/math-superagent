# Hauser & Schicho, *Forty Questions on Singularities of Algebraic Varieties* (Asian J. Math. 15 (2011) 419–438) — origin-context source

Source URL: https://homepage.univie.ac.at/herwig.hauser/Publications/forty-questions-april-2012.pdf
DOI of journal version: Asian J. Math. 15 (2011), no. 3, 419–438.

## What this source is

The collected "forty questions" of Hauser and Schicho on singularities of algebraic
and analytic varieties, motivated by Hironaka's work. It is the **problem-list
reference** that every CA paper cites as the place where the Casas-Alvero conjecture
was posed as a named open problem among forty. The CA statement is **Problem 14** (★★).

## The canonical statement (Problem 14**, lines 421–432)

> "Casas-Alvero conjecture. We find it intriguing because it is a simple algebraic
> question on polynomials, but yet still open. Let P be a univariate polynomial over
> a field of characteristic zero. Assume that each (non constant) derivative shares a
> divisor with P. (a) Is P a monomial (ax+b)^k? (b) What could be the respective
> statement for multivariate polynomials?"

Note (attached, lines 428–432): "The conjecture was proposed by Casas-Alvero. The
common divisors may a priori be different for each derivative. A proof for polynomials
of prime degree (and several more cases) was given by Graf von Bothmer, Labs, Schicho
and van de Woestijne. For positive characteristic, there exist easy counterexamples.
For fixed degree, it is easy to set up a system of equations which has a solution over
K if and only if there is a counter-example."

## Why the run needs this in the library

- It fixes the **canonical origin-context statement**: CA is Problem 14(★★) in this
  list, confirming the char-0 hypothesis, the "common divisor with every derivative"
  form (not Hasse derivatives here), and that a degree-fixed system-of-equations
  formulation is explicitly anticipated ("it is easy to set up a system of equations
  which has a solution over K iff there is a counter-example").
- It records the **prime-power result attribution**: Graf von Bothmer, Labs, Schicho,
  van de Woestijne proved prime degree "and several more cases" — matching the held
  source `grafvonbothmer2007_infinitely_many`.
- It records **"for positive characteristic, there exist easy counterexamples"** —
  the char-p falsity, matching the run's witness family (x^{p+1}−x^p).
- **Problem 14(b)** (the multivariate analogue) is a named open question — useful
  context for the run's scope decision that multivariate generalisations are out of
  scope unless they imply a univariate case.

## Relationship to the run's agenda

This is a problem-list source, not a proof source: it states CA and its history, and
gives no new result. Its value is fixing the statement and the attribution, and being
the canonical citation for "CA is Problem 14 of Hauser–Schicho." It confirms rather
than extends the claims already held (gvb-2007 prime-power result, char-p falsity,
fixed-degree resultants). No claim block is added; the existing claims already cover
the facts it records. It is corroborating origin-context, worth having on disk so the
"CA is Problem 14(★★)" citation can be verified locally rather than recalled.
