# Bremner, "On squares of squares", Acta Arith. 88 (1999) 289–297

[[bremner-on-squares-of-squares-1999]]

The foundational source for problem (A), the "squared square": nine entries all perfect
squares, maximise how many of the 8 line-sums are equal. It also records the canonical
7-square true-magic-square witness used throughout this run.

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
(23−√3)²   133·22     (23+√3)²
(22+4√3)²  (17−9√3)²  (5+13√3)²
```
also a one-parameter family over `Q(i,√(µ³−µ))`, and one MSS over `Q(u)` of degree 27.

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
id: robertson-elliptic-reduction
statement: A 3×3 magic square of squares exists iff there is c with three points of 2E(Q),
  E: y²=x(x²−c²), whose x-coordinates are in AP; equivalently {X,X±c} all rational squares.
hypotheses: c ∈ Q, distinct entries
holds-here: yes
status: proved
bearing: the run's single-curve reformulation; the standard starting point for descent
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md
answers: exact-reduction-magic-507c
```

```claim
id: extension-field-mss-exist
statement: 3×3 MSS (all nine entries squares, distinct) exist over proper algebraic number
  fields: degree-4 example over Q(√3,√133), a family over Q(i,√(µ³−µ)), and a degree-27
  family over Q(u).
hypotheses: none (explicit constructions given)
holds-here: yes (constructions explicit, entries distinct)
status: proved
bearing: rules out any blanket structural impossibility; a proof must separate Q from extensions
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md
```
