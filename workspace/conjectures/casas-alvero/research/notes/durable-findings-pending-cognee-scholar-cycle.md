# Durable findings this cycle (and earlier) — pending Cognee (memory server down)

The memory server has been down all cycle (14+ documented `remember_memory` failures, a
run-long condition through 2026-08). These findings are source-backed and already live
as claim blocks on disk (they render into `derived/CLAIMS.md`, which all planning roles
read), so nothing is lost — they are simply not yet in the Cognee graph store. Once the
memory server recovers, re-issue the `remember_memory` calls below.

## Finding 1 — Valabrega–Valla is the named hypothesis of the u-resultant certificate

Source: Valabrega & Valla, "Form rings and regular sequences", Nagoya Math. J. 72
(1978) 93–101 (held full text).

`B = ∏_i ord_0(R_i)` (the equality the `uresultant-converge` thread validates) is
exactly the Valabrega–Valla condition: the associated graded ring
`gr_{m_0}(K[a]/(I))` is Cohen–Macaulay / the leading forms of the R_i cut out 0 as a
complete intersection. It is STRICTLY STRONGER than regularity, hence strictly
stronger than CA. A mismatch `B ≠ ∏ ord` in a degree where CA still holds is
evidence gr is not CM, NOT a CA counterexample. It rests on the existing claims
`ord0-resultant-weighted-order-proved-all-n` (ord_0(R_i) = n(n−i)) and
`uresultant-multiplicity-trees-new` (quotient length = n^(n−2) = Cayley labelled trees).
Claim id: `valabrega-valla-initial-forms-regular-sequence` (proved). Theorem 2.3 +
Cor 2.4 verified verbatim from the held full text (lines 150–320).

## Finding 2 — Popoviciu–Erdős / Rahman: the union-dual of the CA hypothesis

Source: Q. I. Rahman, Canad. Math. Bull. 14(2) (1971) 267–269 (held full text).

For a real-rooted degree-n polynomial p, P = p·p'·…·p^{(n-1)} has ≥ n+1 distinct
zeros (over the union of all derivative zero sets) unless p is a pure power (1
distinct zero). This is the DUAL of CA: CA is about COMMON roots, this is about the
UNION of derivative zero sets. A genuine CA counterexample forces P to collapse to
≤5 distinct roots (the shared roots of f), far below n+1 — a quantitative link
between the two. Rahman's extremal shapes z(z^2−1) (n=3) and z(z^2−1)^2 (n=5) are
non-binomial constructions for the degree-20 search diversification task
(`diversify-search-constructions`). Claim id: `popoviciu-erdos-rahman-nplus2` (proved).

## Finding 3 — Abdesselam–Chipalkatti 2012: the sourced Hessian ⟺ perfect-power theorem

Source: Abdesselam & Chipalkatti, "On Hilbert covariants", arXiv:1203.4761 = Canad.
J. Math. 66(1) (2014) 3–30, DOI 10.4153/CJM-2012-046-1.

For a binary d-ic F over C, Hilbert's covariant H_{r,d}(F) vanishes identically iff F
is the perfect power of an order-r form; G_{r,d} and H_{r,d} agree up to a nonzero
rational scalar (Thm 1.1); for r=1 either reduces to the Hessian, G_{1,d} = (F,F)_2
(Prop 3.2, line 822). If r|d the saturation of the coefficient ideal J equals the
defining ideal I_X, so J cuts out the perfect-power locus scheme-theoretically
(Thm 1.2). CA's conclusion f=(x−a)^n is the r=1 / X_{1,d} (rational normal curve)
case. **The Hessian-iff-perfect-power theorem is PROVEN here**; the
`hessian-covariant-transvectant` approach died on its OTHER unproved bridge
("derivative-sharing forces (F,F)_2=0"), which this source does NOT supply. So this
is record/anchor for CA, not a route; it does not resurrect the closed approach.
Claim id: `ac-hilbert-covariant-perfect-power` (proved).
Also resolves the library mislabel: the true paper is arXiv:1203.4761, held at
`research/sources/abdesselam-chipalkatti2012_hilbert-covariants.full.md`.

## Finding 4 — Raicu–Sam–Weyman–Yang 2026: ideal of the equal-parts power locus, and it CONFIRMS AC Conj 5.1

Source: Raicu, Sam, Weyman, Yang, "Powers of binary forms and derived Hermite
reciprocity", arXiv:2602.15175 (16 Feb 2026).

For a,b≥2, d=ab, the homogeneous ideal I(X(ab)) of the locus of a-th powers of
degree-b binary forms over C is generated in degree b+1 (maximal minors of a matrix
of linear forms) and has a linear minimal free resolution; projective dimension
d−1 (Thm 1.1). The Foulkes–Howe map Sym^k(Sym^{ab}C²)→Sym^{ak}(Sym^b C²) is
injective for k≤b, surjective for k≥b (Thm 1.4). Rank criterion (eq 1.2b): for ω:
Sym^d U × Sym^b U → Sym^{d+b−2}U, ω(F,G)=0 iff [F]=[G^a]. **This proves AC's
Conjecture 5.1 (I_X generated in degree r+1) in the equal-parts case.**
BUT CA's target is b=1 (power of a single linear form = rational normal curve), the
trivial ACM case EXCLUDED from Thm 1.1. So this is supporting, not load-bearing,
for CA; its value is the ω-rank-drop homogeneous-minors description of "F=G^a",
the algebraic shape of CA's pure-power conclusion. Claim id:
`rswy-powers-binary-forms-ideal` (proved).

## Cross-source relationship (new this cycle)

Raicu et al 2026 Thm 1.1 **confirms** the Abdesselam–Chipalkatti Conjecture 5.1(c1)
(and the equality g=I_X) in the equal-parts λ=(ab) case. That is the one genuine new
cross-link: the two held sources corroborate each other on the structure of power
loci. Neither impinges on CA's b=1 rational-normal-curve target.

## Finding 6 (2026-09, scholar) — Ghosh FINITENESS accepted at AJM; the full claim is NOT

Source: Hopkins Press AJM accepted list (4/7/2026), author's UW page; arXiv abs 2402.18717.

`Soham Ghosh, "A finiteness result towards the Casas-Alvero Conjecture"`
(arXiv:2402.18717) is **accepted for publication in the American Journal of
Mathematics**. This is peer-review acceptance of the **finiteness/dimension**
results only: Thm A (projectivized CA-var. ≤ 2-dim in every characteristic),
Thm B / Cor C (finite Z-scheme, finitely many K-points, dim≤1), Thm E
(j_C(n) ≥ q(n)−1). It is **NOT** acceptance of the full claimed proof of CA
(arXiv:2501.09272), which remains an unverified 0-citation preprint (v2 Mar 2026).
CA is still open; smallest open degree stays 20. Claim id:
`ghosh-finiteness-ajm-accepted` (verified, primary sources).

## What does not help (scholar verdict, this cycle)

- `eom_resultant`, `eom_groebner-basis`, `eom_newton-diagram`: generic definition-level
  encyclopedia entries. They restate facts the run already holds with proper citations;
  no bearing past confirming terminology. (Already recorded in a prior cycle.)
- The three sources above, for CA: Valabrega–Valla, AC2012 and RSWY2026 are all
  **supporting/record**, not load-bearing. Their real value to the run is: (a) VV anchors
  the u-resultant certificate's comparison; (b) AC anchors the (refuted) Hessian approach's
  one true fact; (c) RSWY is the modern ideal-theoretic statement of the power locus but
  excludes CA's b=1 case. None introduces a new CA constraint. Filed so nobody re-derives
  them.

## Pending `remember_memory` payloads (re-issue when Cognee recovers)

1. `ac-hilbert-covariant-perfect-power` (source arXiv:1203.4761) — statement as Finding 3.
2. `rswy-powers-binary-forms-ideal` (source arXiv:2602.15175) — statement as Finding 4.
3. Cross-source: RSWY2026 Thm 1.1 confirms AC2012 Conjecture 5.1(c1) in the equal-parts case.
