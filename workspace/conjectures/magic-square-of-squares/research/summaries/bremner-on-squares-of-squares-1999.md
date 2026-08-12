# Bremner, "On squares of squares", Acta Arith. 88 (1999) 289–297 — [[bremner-on-squares-of-squares-1999.full]]

The seminal paper. Distinguishes the **two problem variants that the literature keeps conflating**:
- **(A) "squared square"** — all nine entries perfect squares, maximise how many of the 8 line-sums are equal. Best near-miss: Sallows' LS1, 7 of 8 sums equal.
- **(B) true magic square** — all 8 sums equal, maximise how many entries are squares. Best: Bremner's own 7-square square. No 8-square example known.

## Standard parametrisation (every attack starts here)
Any 3×3 magic square of rationals has the form (Bremner eq. (2), matching problem.md's (c,u,v)):
```
a - b    a+b+c   a - c
a+b-c     a      a-b+c
a + c    a-b-c   a + b
```
with a,b,c ∈ Q. It is **trivial** (repeat entries) iff `bc(b²-c²)(b²-4c²)(4b²-c²) = 0`. This is the exact criterion for distinctness — a useful falsifier target.

## The Robertson elliptic reformulation (attributed by Bremner to Robertson [6])
Associate to the parametrised square the curve **E: y² = x(x²−c²)**. A point (X,Y) ∈ E(Q) lies in **2E(Q)** iff the triple {X, X−c, X+c} is three rational squares. Hence:
> **A magic square of squares exists ⇔ three points of 2E(Q) with x-coordinates in arithmetic progression.**

Bremner's small search for three points of E(Q) (not 2E(Q)) in AP found essentially only one nontrivial triple: (−528,26136),(−363,22869),(−198,17424) on y²=x(x²−1254²), rank 3. The constraint is very restrictive when rank E(Q) is small.

## The two 7-square near-misses (the run's witness set)
- **Sallows LS1** (eq. (1)): `[58²,46²,127²; 94²,113²,2²; 97²,82²,74²]`, 7 of 8 sums = 147² = 21609, failing non-principal diagonal = 38307.
- **Bremner's 7-square magic square**: `[373²,289²,565²; 360721,425²,23²; 205²,527²,222121]`, all 8 sums = 541875, centre 425², exactly 7 square entries, non-squares {360721,222121}. (This is the run's Bremner witness.)

## Squared-square construction and the extension-field MSS (the hinge)
Working on E as a fibration E: λ(λ²−1)Y² = X(X²−1) over Q(λ), multiples of P=(λ,1) give infinitely many parametrised squared squares. Fibres above λ=0,∞,±1 of type I₀* with five components; Shioda ⇒ rank(E(C(λ))) ≤ 2, and equals 2 (points (λ,1),(−λ,i)).

- Smallest parametrised squared square has entries of **degree 8** (16, 20 next); magic condition eq. (13): `1−4s²−170s⁴−36s⁶+81s⁸ = 0`.
- **MSS exist over proper number fields.** Family over Q(i,√(μ³−μ)); smallest-degree example over **Q(√3,√133) (degree 4)**: `[(5−13√3)²,(17+9√3)²,(22−4√3)²; (23−√3)², 133·2², (23+√3)²; (22+4√3)²,(17−9√3)²,(5+13√3)²]`; and a family over Q(u) of **degree 27** via λ=(u²−1)/(u²+2) with a degree-27 minimal polynomial. 
- **Consequence (load-bearing for this run):** non-existence over Q cannot be a purely structural/geometric fact — any valid impossibility proof must use rationalness/integrality essentially. A blanket argument would also kill these extension-field examples and is false (GOAL's falsification oracle).

```claim
id: robertson-elliptic-reduction
statement: A 3×3 magic square of squares exists iff there is c with three points of 2E(Q)
  (E: y²=x(x²−c²)) whose x-coordinates are in arithmetic progression; equivalently iff
  {X, X±c} are all rational squares for three X's in AP. The (X in 2E) ⟺ {X,X±c} squares
  part is exact and proved by the duplication formula.
hypotheses: entries rational; E: y²=x(x²−c²); non-trivial (entries distinct)
holds-here: yes
status: proved (in-source; attributed to Robertson)
bearing: anchors the elliptic reformulation as exact, not heuristic; descent/rank arguments
  must work on this curve
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md
answers: exact-reduction-magic-507c
```

```claim
id: extension-field-mss-exist
statement: 3×3 magic squares of squares (all 9 entries squares, distinct) exist over proper
  algebraic number fields — a degree-4 example over Q(√3,√133) and a one-parameter family
  over Q(i,√(μ³−μ)), plus a family over Q(u) of degree 27.
hypotheses: ground field is an extension of Q, not Q itself
holds-here: yes (these are genuinely over extension fields)
status: proved (constructed explicitly in-source)
bearing: any proof of non-existence over Q must fail on these — it must use rationalness/
  integrality, not a geometric obstruction; a blanket structural argument is false
anchor: research/sources/bremner-on-squares-of-squares-1999.full.md
```
