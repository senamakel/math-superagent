# G. Martin — primitive lattice points in rational polygons (UBC preprint)

Source: https://personal.math.ubc.ca/~gerg/papers/downloads/PPRP.pdf — full
text at `research/sources/primitive-points-rational-polygons.full.md`.

## What this source establishes

For a fixed rational polygon A, the count of primitive lattice points
(gcd(m,n)=1, i.e. visible from the origin) in the dilate tA satisfies

    #(tA ∩ P) = (6/π²)·t²·Area(A) + E_A(t)

with error E_A(t) = Ω±(t log log t) and E_A(t) = O(t(log t)^{2/3}(log log
t)^{4/3})-type bounds (extending results known for the isosceles right
triangle / summatory totient). Every rational polygon decomposes into a signed
sum of fitting triangles (Lemma: any rational polygon is a signed sum of
fitting triangles; origin-star-shaped ones, a sum).

## Hypotheses

A a rational polygon in R²; P the primitive points. The orchard's hexagon is
rational, so the asymptotic applies in principle.

## What it lets this run do

- Nothing computational: the run's method is exact integer arithmetic. This
  source confirms the asymptotic shape (visible points ~ 6/π²·area) and the
  connection between polygon primitive-point counts and the totient error
  term — context only.

## What it does not settle

- No exact formula for the hexagon; error-term bounds are not usable for the
  exact H(10⁸). Not load-bearing.

## Claims

```claim
id: polygon-primitive-point-asymptotic
statement: #(tA ∩ P) = (6/π²)t²Area(A) + E_A(t) for rational polygons A, with
E_A(t) = Ω±(t log log t) and matching upper bounds.
hypotheses: A rational polygon; P primitive points.
holds-here: yes (context only; hexagon is rational).
status: sourced (Martin, PPRP).
bearing: none for the exact answer — asymptotic context only.
anchor: research/summaries/primitive-points-rational-polygons.md
```
