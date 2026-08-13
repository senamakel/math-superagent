# Stroeker–de Weger 1999 — Elliptic binomial Diophantine equations (PRIMARY)

Source: R.J. Stroeker, B.M.M. de Weger, Math. Comp. 68 (1999) 1257–1281
(Article S 0025-5718(99)01047-9, electronically published Feb 23, 1999). Full
text read: `research/sources/stroeker-deweger-1999-elliptic-binomial.full.md`.
URL: https://math.deweger.net/papers/[28]StdW-EllBinom-MathComp[1999].pdf

## What the paper establishes

For fixed `(k,ℓ)` with `2 ≤ k < ℓ`, `C(n,k) = C(m,ℓ)` is **completely solved** for
exactly eight pairs — the only pairs in the literature that are reduced to elliptic
equations and solved by **linear forms in elliptic logarithms** (David 1995) plus
LLL reduction:

- `(2,3)`: **Avanesov** (Acta Arith. 12, 1966/67) — first ever solved pair; the
  paper's own proof is new and slightly more general (Thm B23); curve
  `Y²+Y = X³−9X+20` (W23), rank 2, basis (0,4),(3,4).
- `(2,4)`: **de Weger (QJM 47, 1996) and Pintér** (Publ. Math. Debrecen 47, 1995),
  independently; Thm B24, quartic model `V² = 3U⁴+6U³−3U²−6U+9`, minimal curve
  `Y₁² = X₁³−147X₁+610` (W24), rank 2.
- `(2,6)`: **new here** (Thm A26/B26); `Y²+Y = X³+X²−58X+1294`, rank 2,
  basis (−7,37),(8,37). **`(2,8)`, `(3,6)`, `(4,6)`, `(4,8)`:** also solved
  here (Thms A28/B28, A36/B36, A46/B46, A48/B48).
- `(3,6)`: the technically hard case — needs a **new variant** of the elliptic
  logarithms method for equations `f₃(U)=g₃(V)` (cubic = cubic), the first
  solution of any such equation; curve `15U³−15U = V³−4V²+3V` (C36),
  minimal `Y² = X³−1575X+52650` (W36), **rank 4**, basis
  (−15,270),(15,180),(45,270),(−45,180). The variant uses the cubic asymptote and
  an integral formula for the elliptic logarithm (eq. (5),(10)-(11)).
- `(3,4)`: Mordell (Pacific J. Math. 13, 1963) / de Weger (JNT 63, 1997); Thm
  B34, `Y²+Y = X³−X`, **rank 1**. Consistent with `deweger-genus3-curve` (the
  genus-3 double cover reduces to this rank-1 elliptic curve).

Each theorem comes with **complete solution tables** (T23…T48) in both the
elliptic and the binomial coordinates. The method also solves the 
`(n−1,k+1)` and `(n−2,k+1)` boundary families (no nontrivial solutions except
`C(6,1)=C(4,2)`) — announced here, detailed in [SW].

## Structural remarks that matter for this run

- For even k, `C(n,k)` is a polynomial in `(n−(k−1)/2)²` of degree k/2 with
  rational coefficients; `C(n,2)` quadratic, `C(n,4)` quartic (and quadratic in
  the square), `C(n,6)` cubic in the square, `C(n,8)` quartic in the square.
  This is the mechanism that makes the elliptic reductions work and confirms the
  run's `{2,n}` and `{4,n}` genus closed forms (genus grows like
  `floor((k1−1)/2)` resp. `3(n−1)/2`).
- For k=2 or 4 with ℓ ≥ 5, the equation is hyperelliptic of genus
  `⌊(ℓ−1)/2⌋ ≥ 2`; the paper says even `C(n,2)=C(m,5)` was then "too complex by
  far" for the practical methods — solved later by BMSST 2008 (the run holds the
  Bugeaud–Mignotte–Siksek–Stoll–Tengely paper as the method note).
- **All other (k,ℓ) are genus > 1 → Faltings: finitely many rational points,
  but no effective count.** This paper is the source of the statement "completely
  solved only for (2,3),(2,4),(3,4) [at the time, plus de Weger's (2,5)]" that
  the run's ledger (`deweger-smallk-effective`) records; it extends that solved
  list to the full eight pairs above and names the algorithm that did it.
- **Mordell–Weil basis requirement**: every solved case needs the rank and a
  basis `P₁,…,P_r` (computed with Cremona's mwrank; the (2,8) case rank 5, the
  (3,6) case rank 4), then David's lower bound on linear forms in elliptic
  logarithms with explicit constants (c₄ ~ 10⁷³ to 10²¹⁶), then LLL reduction to
  a checkable bound (M₃ ≤ ~50). This is the *exact repeatable template* for the
  run's GOAL deliverable of an effective bound with a computed constant for one
  more (k1,k2) family.
- Relative to the run's ledger, this is **effective, per-pair, non-uniform** — the
  constants (c₁,c₄,the basis heights) are curve-specific and grow with the
  coefficients, so it does not and cannot give a uniform-in-(k1,k2) bound on
  N(a). This is the same effective-per-pair / non-uniform wall as Matveev 2000,
  now demonstrated on binomial equations themselves.

## Claim

```claim
id: sdw-elliptic-logarithms-eight-pairs
statement: Stroeker-de Weger 1999 (Math. Comp. 68, 1257-1281): the equation
  C(n,k)=C(m,l) is completely solved (all integer solutions listed) for exactly
  (k,l) = (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8), by reducing each to an
  elliptic curve, computing rank and a Mordell-Weil basis via mwrank, applying
  David's explicit lower bound for linear forms in elliptic logarithms, and
  reducing with LLL. The (3,6) case (first ever cubic=cubic solution) uses a new
  variant of the elliptic logarithm method. For all other distinct (k,l) the
  curve has genus > 1 and only Faltings' ineffective finiteness applies.
hypotheses: fixed (k,l), 2<=k<l; the elliptic reductions given in Table 1; rank
  and basis data in Tables 3,9,18.
holds-here: yes — this is the primary source of the run's "small-(k1,k2)
  effectively solved" ledger row, extending it from {(2,3),(2,4),(3,4),(2,5)} to
  the full eight pairs; the method is a concrete template for one more effective
  per-pair bound with computed constants (GOAL deliverable).
status: asserted-by-source (primary full text read; the solution tables are the
  paper's own complete lists, not re-derived here)
bearing: fixes which (k1,k2) pairs are completely solved (all eight); names the
  algorithm (elliptic logarithms + David + LLL) that achieves it; leaves every
  other pair at ineffective Faltings finiteness — the uniform-in-k wall stands.
anchor: research/sources/stroeker-deweger-1999-elliptic-binomial.full.md
contradicts: (nothing — extends `deweger-smallk-effective`, which lists only
  (2,3),(2,4),(3,4) plus (2,5))
answers: none (the solved-pairs list was already partially recorded; this gives
  the primary and the full eight-pair list)
```