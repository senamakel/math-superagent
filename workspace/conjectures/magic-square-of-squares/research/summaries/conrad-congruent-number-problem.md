# Conrad, "The Congruent Number Problem"

[[conrad-congruent-number-problem]]

Source: Keith Conrad, "The Congruent Number Problem", The Harvard College
Mathematics Review 2.2 (2008), §6, 58–74.
https://kconrad.math.uconn.edu/articles/congruentnumber.pdf .
Full text at `research/sources/conrad-congruent-number-problem.full.md`.

## Why this is the right source for this run

The run's committed method (problem brief, GOAL.md, ROOT.md) is the arithmetic of
rational points on the single elliptic curve `E_c: y² = x(x²−c²)` — exactly the
**congruent number curve** `E_n: y² = x³ − n²x` (quadratic twist of `y²=x³−x`, j=1728).
Conrad's paper is the canonical expository treatment of precisely this family, stating
three theorems this run's argument leans on: the AP-of-squares ↔ right-triangle
correspondence (Thm 3), the curve ↔ triangle correspondence (Thm 7, the one this run's
`2E(Q)`/Robertson reduction generalises), and Tunnell's theorem (Thm 15), the
criterion for the family the run's rank question is about.

## Statements it makes, and their bearing

**Theorem 2 (Fermat, 1640).** 1 is not congruent — proved by descent on
`a²+b²=c², ab=2d²`. *Bearing:* the model of the genuine (descent, not modular-sieve)
impossibility argument this run needs; the descent produces a strictly smaller
solution, which is the shape a real proof of MSS non-existence must take.

**Theorem 3.** There is a one-to-one correspondence between right triangles with area
`n` and 3-term APs of squares with common difference `n`:
`{(a,b,c): a²+b²=c², (1/2)ab=n} ⟷ {(r,s,t): s²−r²=n, t²−s²=n}`, via
`(a,b,c)↦((b−a)/2, c/2, (b+a)/2)` and inverse `(r,s,t)↦(t−r, t+r, 2s)`.
*Bearing:* every centre AP-difference `d ∈ {u,v,u+v,u−v}` of the MSS is exactly a
congruent-number instance: `d` is "congruent" iff `e²±d` are both squares for a
rational `e` (the middle term). This is the run's `S(e)`/`Φ` structure in the
congruent-number language — a squarefree insert of `d` must be congruent.

**Theorem 7.** For `n>0`, there is a one-to-one correspondence between
`{(a,b,c): a²+b²=c², (1/2)ab=n}` and `{(x,y): y²=x³−n²x, y≠0}`, via
`(a,b,c)↦(nb/(c−a), 2n²/(c−a))` with inverse `(x,y)↦((x²−n²)/y, 2nx/y, (x²+n²)/y)`.
*Bearing:* this is **the** theorem underwriting the ellptic reduction of one AP of
squares through the centre. A point `(x,y)` with `y≠0` on `E_n` forces `x, x−c, x+c`
all squares (the `2E(Q)` membership the run's Robertson reduction uses), and a
non-torsion point generates infinitely many 3-APs of squares of common difference `n`.

**Theorem 15 (Tunnell).** For squarefree `n`, define
`f(n)=#{(x,y,z)∈Z³: x²+2y²+8z²=n}`,
`g(n)=#{(x,y,z)∈Z³: x²+2y²+32z²=n}`,
`h(n)=#{(x,y,z)∈Z³: x²+4y²+8z²=n/2}`,
`k(n)=#{(x,y,z)∈Z³: x²+4y²+32z²=n/2}`.
For odd `n`: if `n` congruent then `f(n)=2g(n)`. For even `n`: if congruent then
`h(n)=2k(n)`. Conversely (both) hold if the weak BSD conjecture holds for
`y²=x³−n²x`.
*Bearing:* Tunnell gives an **unconditional** way to certify a squarefree `n` is *not*
congruent (`f(n)≠2g(n)` or `h(n)≠2k(n)`), which is exactly the positive-rank-0 check for
the curve family this run's argument studies. For the 3×3 MSS, every one of the four
centre AP-differences `u,v,u+v,u−v` must be the common difference of a 3-AP of squares,
i.e. must have squarefree part a *congruent* number with a point of `2E(Q)`; Tunnell
gives the necessary condition each must pass (and `u,v,u+v,u−v` mutually additively
linked).

**Appendix (Lucas 1877).** `n` is congruent iff `y²=x⁴−n²` has a positive rational
solution iff `y²=x⁴+4n²` does. *Bearing:* the quartic reformulation of a single AP;
each centre difference would have to make both quartic curve families solvable.

## Explicit witnesses reproduced in the text

- `n=5`: triangle `(3/2, 20/3, 41/6)` ↦ AP `(31/12)²,(41/12)²,(49/12)²`, step 5;
  curve point `(25/4, 75/8)` on `y²=x³−25x`.
- `n=6`: triangle `(3,4,5)` ↦ AP `(1/2)²,(5/2)²,(7/2)²`, step 6; point `(12,36)` on
  `y²=x³−36x`.
- `n=7`: point `(25,120)` on `y²=x³−49x` ↦ triangle `(24/5, 35/12, 337/60)`.
- Only rational solutions to `y²=x³−x` are the three 2-torsion points `(0,0),(±1,0)`
  (1 not congruent ⇒ rank 0).

```claim
id: ap-of-squares-right-triangle-correspondence
statement: For n>0 there is a bijection between rational right triangles of area n and
  3-term APs of rational squares with common difference n, given by
  (a,b,c) ↦ ((b−a)/2, c/2, (b+a)/2) from the triangle to the square-roots (Conrad Thm 3).
hypotheses: rational a,b,c>0 with a²+b²=c², (1/2)ab=n.
holds-here: yes — each centre AP-difference of the MSS is such an n, and the MSS's
  four differences u,v,u+v,u−v must each be congruent-with-a-2E(Q)-point.
status: proved (Conrad Thm 3; direct verification)
bearing: places the run's S(e)/Φ AP-difference structure into the congruent-number
  framework; n is congruent count-wise so each difference's squarefree part must be
  congruent.
anchor: research/summaries/conrad-congruent-number-problem.md
```

```claim
id: congruent-number-curve-correspondence
statement: n>0 is congruent iff y²=x³−n²x has a rational point with y≠0, via
  (a,b,c) ↦ (nb/(c−a), 2n²/(c−a)) (Conrad Thm 7); a rational point with y≠0 then has
  infinite order (so infinitely many 3-APs of squares of step n exist).
hypotheses: rational n>0.
holds-here: yes — E_c: y²=x(x²−c²) is exactly this curve for n=c, the Robertson
  reduction's single curve; the 2E(Q) membership (x, x±c squares) is the doubled-point
  condition this run needs to verify before applying any AP-length bound.
status: proved (Conrad Thm 7; direct calculation)
bearing: the bridge between the MSS's AP-of-squares building blocks and the run's
  committed elliptic-curve argument; the curve family is the congruent-number twist
  class (j=1728).
anchor: research/summaries/conrad-congruent-number-problem.md
```

```claim
id: tunnell-criterion-for-congruent-number-curves
statement: For squarefree n, Tunnell's theta-count criterion f(n)=2g(n) (n odd) or
  h(n)=2k(n) (n even) is a necessary condition for n to be congruent (the four counts
  being ternary-quadratic-form representation counts as in Conrad Thm 15), and is
  sufficient under the weak BSD conjecture for y²=x³−n²x.
hypotheses: n squarefree positive; f,g,h,k the explicit ternary counts.
holds-here: yes — the criterion governs the curve family the run's argument is about;
  an unconditional way to certify rank-0 (non-congruent) for the twist, and a
  conditional way to certify positive rank.
status: proved (Tunnell 1983, Invent. Math. 72, 323–334; stated in Conrad Thm 15)
bearing: the exact rank-criterion tool for E_c: a candidate AP-difference c that fails
  f=2g or h=2k cannot have a point of 2E(Q), so it cannot realise a centre AP — a
  necessary check for any of the four differences u,v,u+v,u−v.
anchor: research/summaries/conrad-congruent-number-problem.md
```

## Falsifier

A squarefree `n` with `f(n)=2g(n)` (odd) or `h(n)=2k(n)` (even) but `n` not congruent
would show the weak-BSD-conditional converse is essential — but the **one-way**
necessary condition (congruent ⇒ criterion) is unconditional, so that direction cannot
be falsified by any integer. A positive rational solution to `y²=x⁴−n²` for a
Tunnell-failing `n` would contradict Lucas's appendix equivalence and Tunnell together.

## What it does NOT do

It does not touch the three-dimensional additive-linkage of four AP-differences; Conrad
treats one AP at a time through one curve. The MSS obstruction (one middle square in
*four* linked APs, on one common curve `E_c` with `c` a centre-square relationship) is
exactly the extra structure beyond the classical congruent-number problem, and this
source is the standard reference *up to* that extra structure.
