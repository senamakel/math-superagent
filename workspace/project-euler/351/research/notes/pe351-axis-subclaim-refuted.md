# PE 351 — refutation of the axis-visible subclaim inside G-hexorchard-visibility

The lemma `G-hexorchard-visibility`'s headline formula,
H(n) = 3n^2 + 3n - 6*Phi(n), is confirmed correct (brute force at n = 5, 10,
1000 matches the statement's oracles; the final identity is corroborated).
What is attacked and refuted here is the *intermediate counting sentence* in
that lemma's first step:

> "the six boundary axes contribute n visible points each"

This sentence is false for every n >= 2.  Only the primitive point at distance
1 on each of the six axis rays is visible; on the ray through (a,0), for
example, the point (1,0) lies strictly between the origin and (a,0) whenever
a >= 2, so (a,0) is hidden (equivalently gcd(a,0) = a > 1).  Hence each axis
ray contributes exactly 1 visible point, not n, and the written arithmetic in
the first step is internally inconsistent as well:

1 + 6*(n + sum_{k=2..n} phi(k))  =  6*Phi(n) + 6n - 5   (correct evaluation),
1 + 6*Phi(n)                                         (what the lemma claims).

These differ by 6n - 6 != 0 for n >= 2.  The correct decomposition,
1 (centre) + 6*(Phi(n) - 1) (open sectors) + 6 (axes, one visible each)
= 1 + 6*Phi(n), is what the brute force actually confirms.  So the flaw is
contained in the derivation's wording/arithmetic; the final formula survives.

```claim
id: pe351-axis-visible-claim-refuted
statement: In the first-step derivation of G-hexorchard-visibility, the claim
"the six boundary axes contribute n visible points each" is false: each of the
six axis rays of the order-n hexagonal orchard carries exactly ONE visible
point (the primitive point at distance 1); all other axis points (a,0) with
a >= 2, etc. are hidden because (1,0) lies strictly between the origin and
(a,0) on the same ray. Equivalently gcd(a,0) = a > 1.  The written identity
1 + 6*(n + sum_{k=2..n} phi(k)) = 1 + 6*Phi(n) is also false by direct
arithmetic: the left side equals 6*Phi(n) + 6n - 5.  The correct decomposition
is 1 + 6*(Phi(n)-1) + 6 = 1 + 6*Phi(n).
hypotheses: n >= 2; standard visibility definition: a point is hidden iff some
lattice point lies strictly between it and the centre on the same ray; axial
coordinates with the six axes in directions (1,0),(0,1),(1,-1),(-1,0),(0,-1),
(-1,1).
holds-here: yes — this is the problem's own definition of hidden (problem.md).
status: checked — counterexample at n = 2: the distance-2 points (2,0),(0,2),
(2,-2),(-2,0),(0,-2),(-2,2) are hidden (each with its distance-1 point strictly
between it and the origin), so the six axes carry 6 visible points total, not
12.  TPTP problem code/refute/pe351-axis-visible.p, find_counterexample
verdict: refuted (CounterSatisfiable; the model has all 12 axis points
distinct, and ~visible(x2) is forced by blocks(x1,x2) and
visible(P) <=> ~exists Q blocks(Q,P)); checked by hand below.
bearing: does not touch the final answer H(10^8) = 11762187201804552 = 3n^2 +
3n - 6*Phi(n), which is independently confirmed by brute force and by
catalogued Phi(10^8); it only fixes the derivation's intermediate sentence.
anchor: research/notes/pe351-axis-subclaim-refuted.md
```

## Hand check of the refutation (the part the engine cannot vouch for)

Model domain (order-2 hexagon, axial coordinates), 12 distinct axis points,
distance 1 and 2 on each of the six rays:

    ray (1,0):  (1,0), (2,0)       blocks((1,0),(2,0))   -> hidden (2,0)
    ray (0,1):  (0,1), (0,2)       blocks((0,1),(0,2))   -> hidden (0,2)
    ray (1,-1): (1,-1), (2,-2)     blocks((1,-1),(2,-2)) -> hidden (2,-2)
    ray (-1,0): (-1,0), (-2,0)     blocks((-1,0),(-2,0)) -> hidden (-2,0)
    ray (0,-1): (0,-1), (0,-2)     blocks((0,-1),(0,-2)) -> hidden (0,-2)
    ray (-1,1): (-1,1), (-2,2)     blocks((-1,1),(-2,2)) -> hidden (-2,2)

Each distance-2 axis point satisfies is_axis_point but not visible, so the
conjecture "all axis points are visible" fails; every blocks fact is a true
geometric statement about the triangular lattice; visible is defined exactly
as "no lattice point strictly between origin and P on the same ray", and the
origin is not among the axis points (checked: no axis point equals the origin).
The model therefore falsifies the claim for n = 2, and the defect persists for
every n >= 2 by the same argument on the distance-2 point of each ray.
Coordinates of a strictly-between point are the integer midpoint parameter
t in (0,1), e.g. t*(2,0) + (1-t)*(0,0) = (2t, 0) with t = 1/2 giving (1,0).

Consequence for the hidden/visible totals (still correct):
visible_total(n) = 1 + 6*(Phi(n)-1) + 6 = 1 + 6*Phi(n), so
H(n) = (3n^2+3n+1) - (1+6*Phi(n)) = 3n^2 + 3n - 6*Phi(n) unchanged.