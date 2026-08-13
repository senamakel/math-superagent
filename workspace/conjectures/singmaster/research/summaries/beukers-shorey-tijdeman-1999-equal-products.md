# Beukers–Shorey–Tijdeman 1999 — irreducibility of polynomials and arithmetic progressions with equal products of terms

Source: F. Beukers, T.N. Shorey, R. Tijdeman, "Irreducibility of polynomials and
arithmetic progressions with equal products of terms", in *Number Theory in
Progress, Vol. 1* (Proc. Int. Conf. Zakopane 1997, ed. Győry, Iwaniec,
Urbanowicz), Walter de Gruyter, Berlin 1999, pp. 11–26. This is MRSTT's
reference [4], the primary source for the run's central ineffectivity
obstruction.

Full readable text: `research/sources/number-theory-in-progress-vol1-preview.full.md`
(pp. 11–26 of the preview; this is the de Gruyter volume's sample pages and
contains the whole BST paper). Also captured the author preprint
`research/sources/beukers-shorey-tijdeman-1999-equal-products.full.md`
(from Tijdeman's Leiden page, `best1.ps`) — **that file is raw PostScript and
not human-readable**; use the volume preview for reading, the .ps only as the
archived preprint. Source URL for the preview:
https://api.pageplace.de/preview/DT0400.9783110285581_A19815788/preview-9783110285581_A19815788.pdf

## Why this paper matters for the run

The equation the run studies, `C(x,k1) = C(y,k2)`, is exactly
`x(x+1)...(x+k1-1) = Λ y(y+1)...(y+k2-1)` with `Λ = k2!/k1!` (after multiplying
by `k1!` or `k2!`). So BST Theorem 1.1 applies **directly** with `d1 = d2 = 1`.
This is the source MRSTT Remark 1.5 cites for "the number of solutions to
`(n choose m) = (m' choose n')` for fixed 2 ≤ m < m' has been shown (via
Siegel's theorem on integral points) to be finite".

## Theorem 1.1 (the fixed-pair finiteness theorem)

Let m,n integers with 1 < m < n; d1, d2 positive rationals, d1 ≠ d2 if m = n.
The equation

    x(x+d1)···(x+(m−1)d1) = y(y+d2)···(y+(n−1)d2)

admits only finitely many integral solutions x,y, **except** for the infinite
class

    x = y² + 3d2·y,  −2d2 − 3d2·y − y²   when m = 2, n = 4, d1 = 2d2.

(The exceptional class is excluded in the binomial case since d1 = d2 = 1.)
Moreover infinitely many **rational** solutions occur exactly for
(m,n) = (2,2), (2,3), (2,4), (3,3) and (m=2, n=6, d1 = 15d2/4); in all other
cases there are only finitely many rational solutions.

**Proof route (the ineffectivity, verbatim from pp. 12–13):**
"*For the remaining case gcd(m,n) = 1 no general effective method is
available. In that case, with m, n fixed, we have to resort to Siegel's famous
result on integral points on algebraic curves, which is, unfortunately,
ineffective. In addition, we can use Faltings's work on Mordell's conjecture
to make a similar statement for rational solutions as well.*" And p. 13:
"*Both results are ineffective.*" (Theorem B = Siegel, Theorem C = Faltings,
stated on p. 13.)

So for the binomial pair (k1,k2) with gcd(k1,k2) = 1 the proof gives
finiteness only via ineffective Siegel; the paper itself says no general
effective method is available there. This is the primary-source anchor for
the run's "finiteness is not a bound" obstruction. (When gcd(k1,k2) > 1,
Saradha–Shorey–Tijdeman Acta Arith. 68 (1994) gives effective bounds; see
`research/summaries/saradha-shorey-tijdeman-equal-products-1995.md`.)

## Theorem 2.2 — the genus classification (independent cross-check of the run)

For the irreducible curve `X(X+1)···(X+m−1) = ΛY(Y+1)···(Y+n−1)` (1 ≤ m ≤ n,
Λ ∈ C*), the genus is:

- **zero** only for: (m,n)=(2,2); (2,3) with Λ=±3√3/8; (2,4) with Λ=−4/9;
  (2,6) with Λ=(−10±7√7)/576.
- **one** only for: (2,3) with Λ≠±3√3/8; (2,4) with Λ≠−4/9; (2,5) with
  Λ=−1/4t, 3125t⁴−47500t²+82944=0; (2,6) with Λ=16/225; (2,8) with
  Λ=−1/4t, t³+567t²−54432t−4665600=0; (3,3); (3,4) with Λ=±3√3/2;
  (4,4) with Λ=−9/16,−16/9.
- **≥ 2 in all other cases.**

For the binomial specialization d1=d2=1, Λ = k2!/k1! > 0, so among distinct
non-diagonal pairs the genus-1 cases are exactly (m,n) = (2,3) and (2,4): Λ=6
and Λ=12, neither hitting the special Λ values listed. Hence **every other
distinct binomial pair has genus ≥ 2** — this is a proof-level confirmation
of the run's computed genus grid (Singular == Sage; CONTEXT.md "genus-1 cases
are exactly {2,3},{2,4}" and the threshold statement in
`research/approaches/genus-computation.md`), and it comes from a primary
source that does not depend on the Gröbner/singularity computation.

## Other content

- Theorem 2.1 (reducibility): `X(X+1)···(X+m−1) − ΛY(Y+1)···(Y+n−1)` over
  C[X,Y] is reducible only in the three cases (m=n, Λ=1): factor X−Y;
  (m=n odd, Λ=−1): factor X+Y+m−1; (m=2,n=4,Λ=1/4): the explicit quadratic
  factorization `(2X−Y²−3Y)(2X+2+3Y+Y²)`.
- Theorem A (due to Saradha–Shorey–Tijdeman, quoted): for fixed d1 > d2 > 0
  and equal lengths, `x(x+d1)···(x+(m−1)d1) = y(y+d2)···(y+(m−1)d2)` has only
  finitely many solutions m ≥ 2 with gcd(x,y,d1,d2)=1, apart from Minkowski's
  identity `2·6·10···(4m−2) = (m+1)(m+2)···(2m)`; the other solutions are
  effectively computable.
- Proposition 4.1 (genus formula): for f,g with simple stationary points,
  `2g_c = Σ_{a∈Sf}(n − 2r_a) − m + 2 − gcd(m,n)` where `r_a` counts the
  stationary points of g over the critical value f(a) — this is the tool
  behind Theorem 2.2 and a machine-verifiable formula for the run's k2=2,3,4
  closed forms.
- The known small solutions of the equal-blocks equation (1.3) are listed:
  (m,n)=(2,3): (2,1),(14,5); (3,4): (2,1),(4,2),(55,19); (3,5): (4,1),(8,2);
  (4,7): (7,1),(63,8); none with (2,4),(2,6),(2,8),(2,12),(4,8),(5,10);
  (3,6) only (8,1). Note C(16,2)=120=C(10,3) corresponds to (x,y)=(14,5)?
  check: x(x+1)/2 = y(y+1)(y+2)/6 is (1.3) with (m,n)=(2,3) — (x,y)=(14,5)
  gives C(15,2)=105... verify with the collision list rather than trusting
  this mapping here.

## Bearing for the run

- Provides the **primary statement of the ineffectivity obstruction**: for
  gcd(k1,k2)=1 no effective method is known even for fixed pairs; finiteness
  rests on ineffective Siegel.
- Its Theorem 2.2 is a **primary-source proof** that only (2,3),(2,4) have
  genus 1 among binomial pairs — matching the run's computed grid.
- The genus formula (Prop 4.1) is a checkable route for the k2=2,3,4 closed
  forms the run verified computationally.

```claim
id: bst-fixed-kl-ineffective-primary
statement: Beukers-Shorey-Tijdeman 1999 (Theorem 1.1; MRSTT [4]): for fixed
  1 < m < n and d1,d2 rational (d1 != d2 if m=n), the equal-products equation
  x(x+d1)...(x+(m-1)d1) = y(y+d2)...(y+(n-1)d2) has only finitely many integral
  solutions, except the infinite class m=2,n=4,d1=2d2 (x=y^2+3d2 y, -2d2-3d2 y-y^2).
  For gcd(m,n)=1 the proof uses Siegel's theorem, which the paper states is
  "unfortunately, ineffective"; no general effective method is available there.
hypotheses: m,n fixed; d1,d2 fixed; integral solutions x,y.
holds-here: yes — C(x,k1)=C(y,k2) is this equation with d1=d2=1 and Lambda=k2!/k1!,
  so finiteness for each fixed pair is asserted by a primary source; the
  ineffectivity for gcd(k1,k2)=1 is the run's central obstruction.
status: asserted-by-source (primary full text held at
  research/sources/number-theory-in-progress-vol1-preview.full.md)
bearing: names the exact obstruction — per-pair finiteness with no bound
  computable in (k1,k2); any uniform bound must beat this.
anchor: research/summaries/beukers-shorey-tijdeman-1999-equal-products.md
```

```claim
id: bst-genus-classification-matches-grid
statement: BST 1999 Theorem 2.2 classifies the genus of
  X(X+1)...(X+m-1) = Lambda Y(Y+1)...(Y+n-1): genus <= 1 only in the four
  genus-0 and eight genus-1 parameter cases listed; all other irreducible
  members have genus >= 2. For the binomial specialization d1=d2=1,
  Lambda = k2!/k1! > 0, the only non-diagonal genus-1 pairs are (m,n)=(2,3)
  and (2,4); every other distinct pair has genus >= 2.
hypotheses: irreducible curve; m,n >= 1; Lambda in C*.
holds-here: yes — proves at genus level that Faltings (genus>1) applies to
  every binomial pair except the two solved genus-1 cases, confirming the run's
  computed grid (CONTEXT.md "genus-1 cases are exactly {2,3},{2,4}").
status: asserted-by-source (primary full text held); the run's grid
  (Singular+Sage, genus table, k1<=12,k2<=9) independently reproduces the small
  entries, so the two routes agree where both exist.
bearing: the Faltings threshold is exact: only (2,3),(2,4) need Siegel; but
  finiteness remains ineffective (see bst-fixed-kl-ineffective-primary).
anchor: research/summaries/beukers-shorey-tijdeman-1999-equal-products.md
```

```claim
id: minkowski-identity-equal-blocks
statement: BST 1999 p. 11 (Minkowski 1968): for every positive integer m,
  2·6·10···(4m-2) = (m+1)(m+2)···(2m). As an infinite family of equal products
  of pairs of blocks; Saradha-Shorey-Tijdeman (Theorem A quoted in BST) show
  this is the only infinite family for equal lengths with fixed d1,d2 apart
  from effectively computable finitely many other solutions.
hypotheses: m >= 1; d1 > d2 fixed for the Theorem A side.
holds-here: yes — this is the equal-length exception family already recorded
  as sst-equal-length-exception-family; the identity matches
  C(2L,L)=2^L·(1·3·5···(2L-1))-type dual identities used for the N(a)>=6 family.
status: asserted-by-source (held).
bearing: constraints which families can give infinitely many equal products;
  relevant background against the infinite C(n+1,k+1)=C(n,k+2) family (which is
  unequal-length, m=2,n=4-type with d1=2d2 pattern after a change of variables).
anchor: research/summaries/beukers-shorey-tijdeman-1999-equal-products.md
```