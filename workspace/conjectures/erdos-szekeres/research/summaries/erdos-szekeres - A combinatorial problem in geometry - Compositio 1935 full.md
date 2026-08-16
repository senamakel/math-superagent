# Erdős & Szekeres 1935, "A combinatorial problem in geometry", Compositio Math. 2, 463–470

Source: https://www.numdam.org/article/CM_1935__2__463_0.pdf
Full text: [[erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full]]

The founding paper. Introduces the problem (attributed to Esther Klein): find the least
$N(n)$ such that every $N(n)$ points in general position (no three collinear) in the plane
contain $n$ in convex position. Gives two finiteness proofs and the conjecture.

## What it establishes

1. **Klein's ES(4)=5 proof.** From 5 general-position points one can always pick 4 forming a
   convex quadrilateral. If hull is a quad or pentagon, trivial; if hull is a triangle $ABC$
   with two interior points $D,E$, then two of $A,B,C$ lie on the same side of line $DE$, and
   with $D,E$ and those two a convex quadrilateral forms. (The classic proof, reproduced exactly.)
2. **The 4-criterion / equivalence.** $n$ points form a convex $n$-gon iff every 4 of them form
   a convex quadrilateral. This reduces convexity of a set to convexity of its 4-subsets — the fact
   every later SAT encoding (Peters–Szekeres, Dumitru) leans on. Used with Ramsey.
3. **First proof (Ramsey)**: a quantitative Ramsey coloring of the 4-subsets of $N$ points as
   convex/concave; gives finiteness but a huge bound ($2^{10000}$-ish at $n=5$; see intro).
4. **Second proof (cups–caps)**: any set of $f(k,\ell)$ points contains a $k$-cup or an
   $\ell$-cap, and $N(n) \le f(n,n) = \binom{2n-4}{n-2}+1 \approx 4^n/\sqrt n$.

```claim
id: es35-finiteness
statement: For every n >= 3 there is a least N(n) such that every N(n) planar points in general position contain n in convex position.
hypotheses: planar points, general position (no 3 collinear)
holds-here: yes
status: proved
bearing: N(n)=ES(n) is finite; the whole investigation is about its exact value.
anchor: research/sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md
```

```claim
id: es35-cups-caps-bound
statement: ES(n) <= f(n,n) = C(2n-4, n-2) + 1, where f(k,l) is the least N such that any N-point set contains a k-cup or an l-cap.
hypotheses: planar general-position points
holds-here: yes
status: proved
bearing: the ~4^n upper bound; the whole modern upper-bound line is subtracting from this.
anchor: research/sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md
```

```claim
id: es35-four-criterion
statement: n planar points in general position form a convex n-gon iff every 4 of them form a convex quadrilateral.
hypotheses: general position
holds-here: yes
status: proved
bearing: reduces convexity to 4-set local checks; basis of all SAT orientation encodings. (Equivalent 4-set criterion stated in Dumitru and Peters–Szekeres.)
anchor: research/sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md
```

## What it asserts

The conjecture $N(n)=2^{n-2}+1$, with the supporting values $N(3)=3, N(4)=5$ (Klein),
$N(5)=9$ (Makai; proof unpublished at the time, first published by Kalbfleisch et al.).

## Implication for this run

Conjecture is upper-bound-only (lower bound settled in 1960). The original cups–caps argument
is lossy only in the *reduction* to cups/caps, not in $f$ itself ($f$ is tight, see
Morris–Soltan Thm 2.5). So an exact bound needs a structural/stability argument, not more
counting — the sabotage no counting method has beaten.
