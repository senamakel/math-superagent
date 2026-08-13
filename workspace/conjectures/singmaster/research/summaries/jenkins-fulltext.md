# Jenkins 2014 — Repeated binomial coefficients and high-degree curves

Source: H. Jenkins, arXiv:1411.4111 (Integers 16 (2016) #A69). Full text read.
[[jenkins-fulltext]]
(NOTE: `research/sources/jenkins-high-degree-curves.full.md` is only the arXiv
abstract page of the same paper — not a separate source.)

## The incarnation (Section 2)

`C(x,y) = C(x−a, y+b)` is the plane curve
`C_{a,b}:  ∏_{r=0}^{a+b−1}(x−y−r) − ∏_{p=0}^{a−1}(x−p)∏_{q=1}^{b}(y+q) = 0`,
total degree `a+b`. Singmaster's infinite family is `a=b=1`.

## Proposition (location of repeats)

Let `a < y`, and `ζ` the positive root of `ζ^{a+b} − (ζ+1)^a = 0`. If
`C(x,y)=C(x−a,y+b)` then `(x−a−y−b+1)/(y+b) < ζ < (x−y)/(y−a+1)`.
Consequence: all repeats of a fixed configuration have essentially the same ratio
`x/y ≈ ζ` (the bounding ratios are the extremes of the "r_i", successive binomial
ratio steps). All known nontrivial repetitions except Singmaster's lie close to the
edge, so this Proposition does not bind them.

## Theorem (finiteness for a ≠ b)

If `b ≠ a`, `C(x,y)=C(x−a,y+b)` has **finitely many** natural solutions. Proof is
NOT via Siegel/genus (which the author could not push through for the general
family): the limiting ratio `c = lim x/y` satisfies `c^{a+b}−(c+1)^a=0`; by the
Lemma, `X^n−(X+1)^r` has no quadratic real root unless `n/r=2`; combined with
Nagell–Maillet's parametrization criterion (a genus-0 curve with infinitely many
lattice points admits a rational parametrization of a rigid shape), this rules out an
infinite lattice-point set.

**The open case**: `a=b` (except (1,1)) gives the golden-ratio-like quadratic ratio,
so the Lemma does not apply and the author **leaves it open** — this is exactly the
Singmaster infinite family. Jenkins: proving `(x−y)(x−y−1)=x(y+1)` is the *only*
curve in the family with infinitely many lattice points would need a new argument;
he sketches Gröbner/singularity (worked example `a=b=2` is genus 3, nonsingular → at
most finitely many lattice points), and a possible induction `(a,b)=(n+1)` obtained
by "multiplying" the (n,n) curve by the shifted Singmaster curve.

## Structural reformulation of Singmaster (Section 4)

A multiplicity-6 value = common *integral* intersection of two of the curves `C_{a,b}`;
multiplicity 8 = three curves meeting at the same point. Singmaster's conjecture is
equivalent (stronger than necessary) to bounding how many curves can share an integral
intersection beyond a given `x`. Effective heights would need an effective Siegel or
**effective Schmidt subspace theorem**; Baker/genus-1 methods give triple-exponential
bounds, too large to use.

## Bearing for this run

Reinforces the two structural walls already on record: (1) per-curve finiteness for
`a≠b` is real but **ineffective** (no count in `a,b`), so it cannot give a
k-uniform bound; (2) the `a=b` (golden-ratio) case — the infinite family — is
precisely what Jenkins could not close, and what forces `N≥6` infinitely often.
This is the same "finiteness is not a bound" obstruction, and it confirms that the
genus computation (`g(k1,k2)`) supplies only the Faltings threshold, never a
uniform constant.

```claim
id: jenkins-ab-finite
statement: Jenkins (arXiv:1411.4111): for a != b the curve C(x,y)=C(x-a,y+b) has
  finitely many natural solutions, proved via the limiting ratio c (root of
  c^{a+b}-(c+1)^a=0) being non-quadratic (Lemma: x^n-(x+1)^r has no quadratic real
  root unless n/r=2) plus the Nagell-Maillet parametrization criterion; NOT via
  Siegel/genus. The a=b (excl (1,1)) case (quadratic/golden-ratio ratio) is left open
  -- exactly the Singmaster infinite family.
hypotheses: a<b (or a>b) natural; the configuration not cut off by the triangle edge.
holds-here: yes.
status: sourced (full text read; the a=b dead-end is the author's own statement)
bearing: confirms per-curve finiteness is ineffective in (a,b), so no k-uniform bound;
  the a=b case is the infinite family driving N>=6.
anchor: research/summaries/jenkins-fulltext.md
```
