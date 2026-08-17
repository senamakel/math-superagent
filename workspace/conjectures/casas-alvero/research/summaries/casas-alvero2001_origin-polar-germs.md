# Casas-Alvero 2001/2002, "Higher order polar germs" — origin of the conjecture

**Source:** `research/sources/casas-alvero2001_higher-order-polar-germs_mardi-record.full.md`
(fetched from the MaRDI portal item Q5938612).

**Full text status:** Elsevier-paywalled. DOI 10.1006/jabr.2000.8727; publication
date recorded in the JS/portal as 2 June 2002; zbMATH Open docs `0985.14012`,
DE number 1623140; OpenAlex `W2003962780`; reviewed by Augusto Nobile. The
University of Barcelona's open repository (diposit.ub.edu) hosts Casas-Alvero's
other polar papers (e.g. *Polar germs, Jacobian ideal and analytic
classification of irreducible plane curve singularities*, Manuscripta Math.
172 (2023), hdl 2445/217388) but **not** this origin paper. This record is the
deepest obtainable statement of the paper's content.

## What the paper actually contains (from A. Nobile's zbMATH review text)

The conjecture is the *polynomial shadow* of a plane-curve-singularity
question. The paper studies higher-order **x-polars** of a germ of a complex
analytic plane curve.

- The first x-polar of f (curve C, f=0 near origin in C²) is the germ
  P_x(f) defined by ∂f/∂y = 0. Iterating (when the y-axis Y is not a
  component) gives x-polars P_x^(r)(f) of every order r.
- **Main result (technical):** Let C be an irreducible branch with Puiseux
  series s = Σ a_i x^{i/n} and characteristic exponents m_1/n,…,m_k/n, with
  n_i = gcd(n, m_1,…,m_i), so n_k = 1. For 1 ≤ r < n let u(r) satisfy
  n_{u(r)-1} > r ≥ n_{u(r)}. Then
  P_x^(r)(f) = D_1^(r) + … + D_{u(r)}^(r),
  where the intersection multiplicities [D_i^(r) . Y] (1 ≤ i < u(r)) are
  expressed explicitly in terms of r, n, n_1,…,n_{u(r)-1}; and each branch of
  D_i^(r) has Puiseux series matching s up to degree (m_i − 1)/n but not beyond.
- **Consequences (the load-bearing ones for why CA was asked):**
  (a) explicit formula for [C . B] for any branch B of P_x^(r)(f), in terms of
      [B,Y], n, n_i, m_j;
  (b) the ratios [C.B]/[Y.B] equal the first u(r) **polar invariants of C**
      (Teissier's);
  (c) a new proof of the Dickenstein–Sessa formula for [C . P_x^(r)(f)], and
      a new proof of **Merle's** formula expressing the polar invariants of C
      in terms of its characteristic exponents.
- Similar filtrations/statements fail for reducible germs (shown by example).

## Why this matters to the run

- This is the "singularity-theory origin" GOAL.md declares out of scope but
  says to read *enough* of to know why the question was asked. The conjecture
  is the algebraic version of a rigidity statement for higher polars: the
  more structure the Puiseux data forces on the polar decomposition, the
  harder it is for a non-power polynomial to share a root with *every*
  derivative.
- It records the canonical identifiers (zbMATH 0985.14012, OpenAlex
  W2003962780, DOI) so no later role re-invents a citation for the origin
  paper — a real contamination risk given the full text is unavailable.

## Evidence class

Asserted-by-source (Nobile's published review of the paper). The run has not
verified the polar decomposition itself; it is background motivation, not a
load-bearing step in the scheme-theoretic attack. The two prior blocked-fetch
records (UB handle 2445/135055 → 404; Elsevier paywall) are superseded by
`download_document`ing the MaRDI record, which is now held in full.
