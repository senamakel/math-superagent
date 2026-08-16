# Fernández de las Heras & Fernández de las Heras, *Three proofs of the CA conjecture* (arXiv:1306.5656)

Full text: [[three-proofs-casas-alvero_2013]]

An unpublished, **unrefereed** preprint (arXiv math.GM) that claims three proofs of CA. Per GOAL.md this joins the "claimed proofs that fail" pattern. Read enough to record why it does not stand.

## Assessment — does not help as a proof
The three "proofs" are elementary (Birkhoff interpolation, an induction via an integral representation, and a coefficient/symmetric-function argument). None survives scrutiny, and none is refuted by a specific located error — they are simply not valid arguments (this is the assessment the run's CLAIMS.md already records: unpublished, unrefereed, not a standing proof). More importantly for the run's method:

- The arguments are **pure char-0 real/complex analysis** (interpolation polynomials on C, iterated real integrals, the integral representation p_n(z)=n!∫…∫dx_n). They never mention Hasse derivatives, resultants, or the scheme over Z, and they have NO step one could exhibit as "the step that breaks in char p." By the run's own standard, a char-0 proof that does not identify its char-0 content is not even checkable against the char-p witnesses. So this source is recorded as a claimed proof that does not stand, not as a method to build on.

- Numerically, the "proof by induction" (Section 4) does the base N=2 then waves; the "third proof" (Section 5) essentially asserts that if a derivative's root is shared then that derivative forces the same c_k value — which is exactly the content of the conjecture, i.e. circular.

## What it usefully records
- It restates CA via the Abel/2-condition form and via Birkhoff (lacunary) interpolation — a reformulation family the run might note but not adopt as a proof route (it is strictly weaker than the resultant / regular-sequence formulations and offers no algebraic certificate).
- It confirms the literature pattern: claimed CA proofs are common and reliably invalid.

## What it does not settle
Nothing. No partial result, no located gap (it is simply not a valid argument), no degree settled.
