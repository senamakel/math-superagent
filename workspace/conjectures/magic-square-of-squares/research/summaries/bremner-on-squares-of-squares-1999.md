# Bremner, "On squares of squares", Acta Arith. 88 (1999) 289–297

[[bremner-on-squares-of-squares-1999]]

The foundational source for problem (A), the "squared square": nine entries all perfect
squares, maximise how many of the 8 line-sums are equal. It also records the canonical
7-square true-magic-square witness used throughout this run.

Source full text: [[bremner-on-squares-of-squares-1999]] → `research/sources/bremner-on-squares-of-squares-1999.full.md`

## Established statements

**Parametrisation (eq. 2).** Every 3×3 magic square of rationals is
```
a−b  a+b+c  a−c
a+b−c  a  a−b+c
a+c  a−b−c  a+b
```
trivial (repeated entry) iff `bc(b²−c²)(b²−4c²)(4b²−c²)=0`. (This is the run's
`(c,u,v)` form with different letters; identical structure — four centre-line APs.)

**Elliptic reduction (eq. 3, "Robertson's observation").** A MSS of squares exists iff
there are three rational points of `2E(Q)`, `E: y² = x(x²−c²)`, whose x-coordinates are in
arithmetic progression. A point `(X,Y)∈E(Q)` lies in `2E(Q)` iff `{X, X±c}` are all rational
squares. `E` has rational torsion = {2-torsion} only. This is the *restrictive* single-curve
reformulation; a small search found only one non-torsion AP triple, on a rank-3 curve.

**Squared-square infinite families.** Via the fibration `E: λ(λ²−1)Y² = X(X²−1)` over
`Q(λ)`, one gets infinitely many parametrized squared squares (all sums equal except the
non-principal diagonal). Smallest entries have degree 8, 16, 20, 24, … in the parameter;
the author expects squared squares for every degree `d≡0 mod 4`, `d≥16`, and none for
`d≡6 mod 8` (conjecture, not proved). The magic condition becomes vanishing of a
polynomial.

**Extension-field MSS exist — the hinge.** Substituting a root θ of the magic-polynomial
gives a MSS with entries in `Q(θ)`. A linear factor would give a *rational* MSS, but none
arises. Smallest-degree genuine MSS: **degree 4** over `Q(√3,√133)`:
```
(5−13√3)²  (17+9√3)²  (22−4√3)²
(23−√3)²   532        (23+√3)²
(22+4√3)²  (17−9√3)²  (5+13√3)²
```
with magic constant 3·532 = 1596.
(**Correction of the OCR'd "133·22"**: exact row-sum arithmetic in `Q(√3)`
forces the centre to 532 = 133·2² = 2²·7·19 = (2√133)², not 2926 = 133·22;
Bremner II 2001's independently printed transposed grid carries the centre
`2²·7·19` = 532 and the same eight square entries over `Q(√3)`, so the two
sources agree. Verified: `code/bremner_deg4_check.py`, exact arithmetic.)
Also a one-parameter family over `Q(i,√(µ³−µ))`, and one MSS over `Q(u)` of degree 27.

**Witness.** The 7-square true magic square:
```
373²  289²  565²
360721 425²  23²
205²  527²  222121
```
7 square entries; an example with 8 distinct square entries is unknown.

## Implications for this run

- Confirms the parametrisation and the elliptic reformulation (`robertson-elliptic-reduction`).
- Non-existence over `Q` **cannot** be a purely structural/geometric impossibility: genuine
  MSS exist over `Q(√3,√133)` and odd-degree fields. Any proof must use rationalness/
  integrality essentially. This is the run's key "proves too much" guard.
- The 7-square witness is the mandatory near-miss every impossibility lemma must survive.

## Contradictions / cautions

- Robertson 1996 (the `robertson-magic-squares-of-squares-1996` download) is the *same PDF*
  as this 1999 paper under a different filename; no separate content.

```claim
id: bremner-deg4-centre-532
statement: The degree-4 MSS over Q(√3,√133) printed in Bremner 1999 has centre
  532 = 133·2² = 2²·7·19 and magic constant 1596, not 2926 = "133·22" as the
  OCR'd text reads. All eight r-terms of the printed entries cancel exactly;
  Bremner II 2001 prints the same grid transposed with centre "2²·7·19" = 532,
  an independent agreement. 532 = (2√133)² is a square in Q(√133).
hypotheses: the printed nine entries; exact arithmetic in Q(√3)
holds-here: yes
status: checked
bearing: the extension-field MSS hinge (non-existence cannot be purely
  structural) stands unchanged; only the literal centre value is corrected;
  verified by exact row/column/diagonal arithmetic in Q(√3); script
  code/bremner_deg4_check.py records the field arithmetic
anchor: research/summaries/bremner-on-squares-of-squares-1999.md
```

```claim
id: robertson-elliptic-reduction
statement: A 3×3 magic square of squares exists iff there exist P₀, P₁, P₂ ∈ E(Q) on
  E: y² = x(x² − c²) with x-coordinates of the *doubled* points 2P₀, 2P₁, 2P₂
  in arithmetic progression, i.e. with
    a−b = x(2P₀),  a = x(2P₁),  a+b = x(2P₂)
  and
    x(2P₂) − x(2P₁) = x(2P₁) − x(2P₀)  (= b).
  Use: a point (X, Y) ∈ E(Q) lies in 2E(Q) (i.e. X = x(2Q) for some Q ∈ E(Q))
  iff {X, X+c, X−c} are all rational squares.  E has rational torsion = {2-torsion}
  only; replacing Pᵢ by Pᵢ+T (T torsion) leaves the square unchanged.  The
  corresponding grid (entries as rational squares) is eq. (4) of Bremner 1999 p. 291,
  with centre a = x(2P₁) and magic constant 3a.
hypotheses: centre a ∈ Q with a = e² for an integer MSS (the centre is a square,
  e.g. a = 425² for the witness); c is the common difference of the anti-diagonal
  AP {a−c, a, a+c}, NOT the centre (c = 138600 for the witness, unrelated to e =
  425); distinct entries; centre a = x(2P₁)
holds-here: yes
status: proved
bearing: the run's single-curve reformulation; the standard starting point for any
  descent or AP-length argument.  The Garcia-Fritz–Pastén (2026) Theorem 1.8 bound
  — every AP of x-coordinates of points in E(Q) has length ≤ C^(r+1) — APPLIES
  DIRECTLY to the MSS AP, because the three points 2P₀, 2P₁, 2P₂ ARE points of E(Q)
  (Pᵢ ∈ E(Q) ⇒ 2Pᵢ ∈ E(Q)) and their x-coordinates a−b, a, a+b are in AP.  So the
  crux is settled: the MSS AP is an AP of x(P) for points P = 2Pᵢ ∈ E(Q); it is NOT
  merely an AP of doubled-point x-coordinates disjoint from the theorem's scope.
  The theorem therefore bounds the MSS AP by C^(rankEe+1).  It yields a
  non-existence contradiction ONLY IF C^(rankEe+1) < 3, i.e. rankEe(Q) + 1 < log_C 3;
  since C is not explicit (and invariably large), and since the Bremner-witness
  curve (rank 2) already sits inside the bound C^3 ≥ 3, no contradiction follows —
  the uniform-height approach is NOT refuted on the crux, but it is ineffective as a
  proof of non-existence without an explicit C (see uniform-height-bound-elliptic-ap).
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md pp. 290–291
answers: exact-reduction-magic-507c
verified-by: statement traced through Bremner 1999 eqs. (2)–(4) and the surrounding
  prose; the derivation is peer-reviewed (Acta Arithmetica).  Crux resolution:
  Bremner 1999 p. 290 states a−b, a, a+b are the x-coordinates of "three points in
  2E(Q)" — i.e. of the doubled points 2P₀, 2P₁, 2P₂ — and these are themselves
  points of E(Q), so Garcia-Fritz–Pastén Theorem 1.8 (APs of x(P), P ∈ E(Q))
  applies verbatim.  Independently computed on Bremner's witness: main diagonal
  {373², 425², 565²}, anti-diagonal difference c = 138600, E: y²=x³−c²x has rank 2,
  torsion order 4; x(373²)=139129 and x(425²)=180625 are in 2E(Q) (both {X,X±c}
  all squares); x(565²)=319225 is NOT (X−c=425² square but X+c=457825 not) — exactly
  2 of the 3 doubled points, matching a 7-square near-miss not an MSS.
```

```claim
id: extension-field-mss-exist
statement: 3×3 MSS (all nine entries squares, distinct) exist over proper algebraic number
  fields: degree-4 example over Q(√3,√133), a family over Q(i,√(µ³−µ)), and a degree-27
  family over Q(u).
hypotheses: none (explicit constructions given)
holds-here: yes
status: proved
bearing: rules out any blanket structural impossibility; a proof must separate
  Q from extensions; the constructions are explicit and the entries distinct
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md
```
