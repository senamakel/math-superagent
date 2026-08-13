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
statement: A 3×3 magic square of squares over Q exists iff there exist P₀, P₁, P₂ ∈
  E(Q) on E: y² = x(x² − c²) such that the x-coordinates of the doubled points
  2P₀, 2P₁, 2P₂ form an arithmetic progression:
    x(2P₀) = a − b,  x(2P₁) = a,  x(2P₂) = a + b,
    with  x(2P₂) − x(2P₁) = x(2P₁) − x(2P₀) = b.
  These three terms are exactly the main diagonal of the MSS (parametrisation (2)
  of Bremner 1999 p. 290), so the AP has common difference b.  The membership rule:
  a point (X, Y) ∈ E(Q) lies in 2E(Q) (i.e. X = x(2Q) for some Q ∈ E(Q)) iff
  {X, X−c, X+c} are all rational squares.  The doubling x-coordinate is
  x(2Q) = (ξ²+c²)²/(4η²) for Q = (ξ,η) (verified against the duplication formula).
  Meaning of parameters: a = x(2P₁) is the centre entry of the MSS (so a = e² is a
  square, e.g. a = 425² for Bremner's witness); c is the anti-diagonal half-difference
  {a−c, a, a+c} — NOT the centre (c = 138600 for the witness, unrelated to e = 425);
  b is the main-diagonal half-difference {a−b, a, a+b} (b = 41496 for the witness).
  CONVERSE: given three such points in 2E(Q) with x-coords in AP, the grid (4) of
  Bremner 1999 p. 291,
    [ x(2P₀)    x(2P₂)+c  x(2P₁)−c ]
    [ x(2P₂)−c  x(2P₁)    x(2P₀)+c ]
    [ x(2P₁)+c  x(2P₀)−c  x(2P₂)   ],
  is a magic square of rational squares (magic exactly when the AP condition holds),
  hence an integer MSS after clearing denominators; distinctness requires the three
  x-coords and the nine entries distinct.  E has rational torsion = {2-torsion} only;
  replacing Pᵢ by Pᵢ+T (T torsion) leaves the grid unchanged.
hypotheses: a, b, c ∈ Q, c ≠ 0 (E nonsingular); a = x(2P₁) a rational square (centre
  of the MSS); P₀, P₁, P₂ ∈ E(Q); for the integer problem the cleared-denominator
  entries are positive distinct integers
holds-here: yes
status: proved
bearing: the run's single-curve reformulation and the standard start of every descent
  or AP-length argument.  The Garcia-Fritz–Pastén (2026) Theorem 1.8 bound — every AP
  of x-coordinates of points in E(Q) has length ≤ C^(r+1) — APPLIES DIRECTLY to the MSS
  AP: the three points 2P₀, 2P₁, 2P₂ ARE points of E(Q) (Pᵢ ∈ E(Q) ⇒ 2Pᵢ ∈ E(Q)) and
  their x-coords a−b, a, a+b are in AP, so the MSS AP is an AP of x(P) for P = 2Pᵢ ∈
  E(Q) and is not outside the theorem's scope.  The theorem bounds the MSS AP by
  C^(rankEe(Q)+1); it forces non-existence only if C^(rankEe(Q)+1) < 3, i.e.
  rankEe(Q) + 1 < log_C 3.  Since C is ineffective in the paper, no contradiction
  follows from the rank-2 Bremner-witness curve (which satisfies C³ ≥ 3): the
  uniform-height approach is NOT refuted on this crux, but is ineffective without an
  explicit C (see uniform-height-bound-elliptic-ap).  Also pins the 7-square→MSS gap
  precisely: an MSS needs all three doubled x-coords in 2E, whereas the witness realises
  only two.
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md pp. 290–291 (eqs. 2–4)
answers: exact-reduction-magic-507c
verified-by: statement traced through Bremner 1999 eqs. (2)–(4) and surrounding prose
  (peer-reviewed, Acta Arithmetica 88); doubled-point formula x(2P)=(ξ²+c²)²/(4η²)
  re-derived from the duplication formula.  Hand-checked on Bremner's 7-square witness
  (exact integer arithmetic): centre a=425²=180625; MAIN diagonal {a−b,a,a+b} =
  {139129,180625,222121}={373²,425²,∎} with b=41496 and third term 222121 NOT a square;
  ANTI-diagonal {205²,425²,565²} fully square with c=138600.  In 2E(Q): X=a=180625
  (X±c=205²,565²) yes; X=a−b=139129 (X±c=23²,527²) yes; X=a+b=222121 (X−c=289² but
  X+c=360721 not square) NO.  So 2 of the 3 main-diagonal x-coords are in 2E — the
  witness is a 7-square near-miss, one doubled point short of an MSS.  This is the
  exact shape an impossibility lemma must not forbid.
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
