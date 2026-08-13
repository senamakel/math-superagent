# Librarian cycle — 2026-08-13 (concordant-forms / θ-congruent / four-AP primary sources added)

## Gap filled

`problem.md` lists as a direction to settle early: *"Congruent numbers and concordant
forms. … Whether the four-difference condition maps onto a known concordant-forms
problem is worth settling early, because if it does, a large literature applies."*
The library did **not** hold any concordant-forms / θ-congruent primary source — the
direction was named but unanchored. This cycle fixed that with two genuine primary
sources (both open-access arXiv preprints, both MDPI/T&F-paywalled at the journal).

## Downloads added

1. **Selder & Spindler, "On θ-congruent numbers, rational squares in arithmetic
   progressions, concordant forms and elliptic curves"** — arXiv:1408.1522v2
   (Mathematics 3(1), 2015).
   - Full text: `research/sources/selder-spindler-theta-congruent-concordant-2014.html.full.md`
   - Summary + claim: `research/summaries/selder-spindler-theta-congruent-concordant-2014.md`
2. **Knaf, Selder & Spindler, "An Algorithm to Find Rational Points on Elliptic Curves
   Related to the Concordant Form Problem"** — arXiv:1907.02148v1 (2019).
   - Full text: `research/sources/knaf-selder-spindler-concordant-elliptic-algorithm-2019.html.full.md`
   - Summary + claim: `research/summaries/knaf-selder-spindler-concordant-elliptic-algorithm-2019.md`

(MDPI direct download is 403 — arXiv HTML is the access, fetched successfully.)

## What they establish (ledger now claims, both `status` in CLAIMS.md)

- `concordant-forms-iff-ell-torsion-order-2` (proved, sourced): concordant forms
  X²+mY², X²+nY² (m=−pk, n=qk, (p,q)=1, k squarefree) are concordant ⟺ E(m,n)
  y²=x(x+m)(x+n) has a rational point of order > 2. Each MSS centre-AP difference
  d∈{u,v,u+v,u−v} is the p=q=1, k=d case on the congruent-number curve E(−d,d):
  y²=x³−d²x. This is the published anchor for the run's phi-universal-set/four-AP
  identification, and Thm 4.7 gives a torsion meaning (order-4 ⟺ AP contains 0 ⟺
  isosceles θ-triangle) to Bremner's witness realising exactly two differences.
- `concordant-single-ap-solutions-computable-large` (asserted-by-source, Knaf–Selder–
  Spindler Table 1/2): individual AP-of-squares solutions are plentiful and astronomically
  large (up to 79 digits), with no known height/termination bound. Frames the four-AP
  simultaneity as the crux; the 2-descent machinery is subsumed by Bremner II's K3 data
  (cross-referenced with the `simultaneous-congruent-numbers-2selmer` refutation).

## Deliberate boundary: what these do NOT do

Both papers treat **a single** AP-of-squares. Neither addresses the defining MSS
constraint that four steps u,v,u+v,u−v share one middle term e² **and are additively
linked**. So the concordant-form dictionary is necessary context anchored to a complete
torsion classification, not an obstruction — the additive relation remains the crux,
exactly as CONTEXT.md and the four-ap-additive-triple thread already held. This was
stated explicitly in both summaries to prevent anyone treating the concordant-forms
connection as a route to non-existence.

## Net state

The two new claims are cross-referenced cleanly with `robertson-elliptic-reduction`,
`aps-of-squares-count-asymptotics`, `root-number-parity-refuted-four-curves` and the
Φ/`phi-universal-set` results. The concordant-forms direction named in problem.md is now
anchored. No further gathering is warranted except against a stated, narrower gap in
REQUESTS.md.
