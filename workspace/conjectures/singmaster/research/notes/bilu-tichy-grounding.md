# Bilu–Tichy classification applied to the binomial-coefficient equation — grounding note

Sources: Hajdu, Papp, Tijdeman, "The Prouhet–Tarry–Escott problem, indecomposability of
polynomials and Diophantine equations", Ramanujan J. 58 (2022) 1075–1093,
https://doi.org/10.1007/s11139-022-00555-7 (full text held at
`research/sources/prouhet-tarry-escott-indecomposability.full.md`).
Bilu, Tichy, "The Diophantine equation f(x)=g(y)", Acta Arith. 95 (2000) 261–288,
https://doi.org/10.4064/aa-95-3-261-288 .

## What the reformulation is called

The "separated-variables" Diophantine equation `f(x) = g(y)`, and its solution structure
is governed by the **Bilu–Tichy classification of standard pairs** (Acta Arith. 95
(2000)). A pair `(F,G)` of polynomials is a *standard pair* over Q if (up to order and
linear change) it is one of five kinds (powers, x²-type, Dickson pairs, and two fixed
quartic types). The theorem (Lemma 5.4 form in HPT): `f(x)=g(y)` has **infinitely many
rational solutions with bounded denominator** iff `f = φ∘F∘λ`, `g = φ∘G∘κ` with λ,κ
linear, φ∈Q[x], and (F,G) a standard pair such that F(x)=G(y) itself has infinitely
many bounded-denominator solutions.

## The precise specialization to binomial polynomials, and whether it applies here

`C(x,k) = x(x-1)...(x-k+1)/k!` has roots `{0,1,...,k-1}`, an arithmetic progression
with no terms missing — exactly the `f_{A,c,d}`, c=0,d=1,r=0 form studied in HPT
(roots ∏_{a∈A}(x-a), |A|=n-r, n > 2r^{3/2}+5r+8; for r=0 the hypothesis is
`n > 8`, i.e. degree n≥9, automatic for k≥9; small k checked separately). HPT Theorem
2.3 then gives:

> **HPT Theorem 2.3.** Let `A⊆{1,...,n}`, |A|=n-r, n>2r^{3/2}+5r+8, and `P∈Q[y]` with
> deg P≥2. Then `f_{A,c,d}(x) = P(y)` has finitely many integer solutions unless
> (i) `P(y) = f_{A,c,d}(T(y))` for some non-constant T∈Q[y], or
> (ii) `P(y) = φ*(Q(y))` where φ* is the (explicit) quadratic-composition polynomial and
> Q has at most two roots of odd multiplicity.

**Hypotheses hold here: yes.** The binomial equation `C(x,k1)=C(y,k2)` is exactly
`f_{A,c,d}(x) = P(y)` with both sides arithmetic-progression products. The paper was
motivated by Benne de Weger's question on equal/differing binomial coefficients (the
"starting point of our study was a question of Benne de Weger"). So this is NOT a
reformulation nobody has tried: it has been applied to this problem.

**What it buys.** For every non-exceptional pair `(k1,k2)` the equation is finite, and
the exceptional cases (i),(ii) are explicitly described — the infinite Singmaster
Fibonacci family `C(n+1,k+1)=C(n,k+2)` is the concrete exceptional example. That is a
*classification of which pairs give infinitely many solutions.*

## The obstruction — why it does NOT buy a uniform bound

HPT Theorem 2.3 is, in the authors' own words, **ineffective** ("This result, similarly
to the above mentioned ones, is ineffective"). It gives "finitely many" with no count
computable in the pair. It does not even give an effective per-pair bound, only
finiteness. The only *effective* result in HPT (Theorem 2.4) is for shifted power values
`f_{A,c,d}(x) = ay^ℓ+b` with ℓ unknown — NOT the binomial-equals-binomial equation.

The effective analogue that does exist for non-standard pairs (via Baker / linear forms
in logarithms) bounds the solutions in terms of the degrees and heights of f and g. For
`C(x,k)` the degree is k and the height grows with k, so the bound grows with k — it is
**not uniform in (k1,k2)**. This is the same central obstruction as Faltings/Siegel and
as the Saradha–Shorey–Tijdeman effective-but-not-uniform bound already in the library
(claim `sst-effective-shared-factor`). Uniformity would need an effective bound with a
constant independent of the pair, which the Bilu–Tichy/Baker route does not supply.

## Verdict for the candidate `bilu-tichy-classification`

- The reformulation is real and **named** (Bilu–Tichy classification / separated-variables
  equation).
- It has been **applied to this exact problem** by HPT (and the related small-pair solves,
  e.g. Jenkins 2014, de Weger 1997, are the same family).
- The classification component is **grounded**: it correctly describes which (k1,k2)
  pairs are exceptional.
- The hoped mechanism — "effective finiteness per-pair → uniform bound via bounding the
  number of exceptional pairs hitting one a" — **fails**: the finiteness is ineffective
  (HPT Thm 2.3) and the effective version is non-uniform in k. So the candidate cannot
  reach the deliverable. **refuted as a route to a uniform bound**, with the
  classification as the surviving grounded kernel.

```claim
id: hpt-bilu-tichy-exceptional-classification
statement: For binomial/arithmetic-progression-product polynomials f_{A,c,d} (roots an
  arithmetic progression, at most r terms missing, n>2r^{3/2}+5r+8), Hajdu-Papp-Tijdeman
  2022 Thm 2.3: f_{A,c,d}(x)=P(y) (deg P≥2) has finitely many integer solutions unless
  (i) P(y)=f_{A,c,d}(T(y)) or (ii) the explicit quadratic-composition case. C(x,k1)=C(y,k2)
  is a special case (c=0,d=1,r=0, both sides AP products). The infinite Fibonacci family
  C(n+1,k+1)=C(n,k+2) is the exceptional example.
hypotheses: A⊆{1,..,n}, |A|=n-r, n>2r^{3/2}+5r+8; deg P≥2. Holds here: yes (binomial
  polys are AP products, r=0).
holds-here: yes — verified against the primary full text
  (research/sources/prouhet-tarry-escott-indecomposability.full.md, Corollary 2.1 +
  Theorem 2.3): C(x,k1) is c=0,d=1,r=0, and the infinite Fibonacci family is the
  exceptional case of (i).
status: sourced (primary full text held; not re-derived here)
bearing: Classifies exactly which (k1,k2) give infinitely many solutions — a grounded
  structural fact. But finiteness is INEFFECTIVE (authors' own words), so it does not
  bound N(a) and does not give uniformity.
anchor: research/notes/bilu-tichy-grounding.md
```

```claim
id: bilu-tichy-method-ineffective-uniformity-wall
statement: The Bilu-Tichy/Baker route to C(x,k1)=C(y,k2) gives: (a) an INEFFECTIVE
  finiteness theorem for non-standard pairs (HPT 2022 Thm 2.3), and (b) at best an
  effective per-pair bound that grows with the degree/height of the binomial polynomials,
  hence is not uniform in (k1,k2). It therefore cannot deliver a uniform bound on N(a);
  the only effective HPT result (Thm 2.4) is for shifted power values, not equal binomials.
hypotheses: fixed pair (k1,k2); Bilu-Tichy standard-pair framework.
holds-here: yes — verified against the primary full text
  (research/sources/prouhet-tarry-escott-indecomposability.full.md): Theorem 2.3's
  finiteness is explicitly "ineffective" (authors' words), Theorem 2.4 (the only
  effective result) is for shifted power values f_{A,c,d}(x)=ay^ℓ+b, and the
  effective per-pair analogue for non-standard pairs grows with degree/height of
  C(x,k), so it is not uniform in (k1,k2).
status: sourced (primary arguments in HPT full text)
bearing: Names the exact obstruction for the bilu-tichy candidate: ineffectivity of the
  classification finiteness + non-uniformity of the effective version. This is a clean
  "cannot give a bound uniform in k" statement of the kind GOAL.md accepts.
anchor: research/notes/bilu-tichy-grounding.md
```

## Related but not applicable (searched, found, set aside)

- Barát, "Distribution of binomial coefficients and digital functions" (JLMS): studies the
  *distribution* of C(n,k) modulo prime powers and p-adic valuations — density results,
  not level-set bounds. Not a route to a uniform N(a) bound.
- Sun–Zhang 2008, "Binomial coefficients and the p-adic integral ring": p-adic density of
  C(n,k), unrelated to level-set cardinality.
