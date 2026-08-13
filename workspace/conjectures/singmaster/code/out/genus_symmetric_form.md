# The genus formula in symmetric form, and the derivation it points at

`genus-single-closed-form-all-pairs` is now in the ledger as `checked`, with the
note that it becomes `proved` when it is derived rather than verified. This is
the step that makes the derivation reachable: the formula rewrites into a
manifestly symmetric expression whose two terms are both objects with a known
meaning.

## The rewrite

The run's form and the symmetric form are the same expression, by expanding:

```
(m-1)n - (m-2) = mn - n - m + 2 = (m-1)(n-1) + 1
```

so

```
g(m,n) = ( (m-1)(n-1) + 1 - gcd(m,n) ) / 2
```

Symmetry in `m` and `n`, which the original form only exhibited numerically, is
now on the face of it. Re-checked against the same 111 genus values with zero
mismatches, and the two numerators agree identically, not just on the table.

The numerator is even for every pair with `2 <= m < n <= 200`, i.e.
`(m-1)(n-1) + 1 = gcd(m,n) mod 2`, which is a small lemma worth stating rather
than an observation worth repeating.

## Why this is the derivation and not just a tidier formula

`C(x,m) - C(y,n)` has bidegree `(m,n)` on `P^1 x P^1`, whose arithmetic genus is
`p_a = (m-1)(n-1)`. So the formula says exactly

```
delta = p_a - g = ( (m-1)(n-1) - 1 + gcd(m,n) ) / 2
```

where `delta` is the total delta invariant of the singularities. That is a
statement to prove, not a pattern to extend: it asks for the singular points of
the curve and their delta invariants, and it predicts their sum in closed form.

The coprime case is the sharpest version of it. When `gcd(m,n) = 1`,

```
delta = (m-1)(n-1)/2 = p_a/2      and      g = p_a/2
```

so the geometric genus is exactly half the arithmetic genus, for every coprime
pair. A factor of exactly two is a quotient, and there is an obvious candidate:
`C(z,k) = z(z-1)...(z-k+1)/k!` satisfies `C(k-1-z, k) = (-1)^k C(z,k)`, because
`z -> k-1-z` negates each of the `k` linear factors. So the curve carries the
involutions `x -> m-1-x` and `y -> n-1-y` whenever the corresponding degree is
even, and their product when both are odd. The `gcd(m,n)` correction is then the
term that measures where those involutions and the branch loci interact — which
is the shape a Riemann-Hurwitz computation produces.

```claim
id: genus-symmetric-form-and-delta-prediction
statement: The genus formula g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2 for the
  projective closure of C(x,m) = C(y,n) is identically equal to
  g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2, since (m-1)n - (m-2) = (m-1)(n-1) + 1;
  symmetry in m and n is therefore an algebraic identity, not a numerical
  coincidence. Re-checked against the same 111 computed genus values with zero
  mismatches. The numerator is even for every 2 <= m < n <= 200. Since
  C(x,m) - C(y,n) has bidegree (m,n) on P^1 x P^1 with arithmetic genus
  p_a = (m-1)(n-1), the formula is equivalent to the statement that the total
  delta invariant of the singularities is ((m-1)(n-1) - 1 + gcd(m,n))/2, and in
  particular that g = p_a/2 exactly whenever gcd(m,n) = 1.
hypotheses: same as genus-single-closed-form-all-pairs - genus of the projective
  closure, diagonal pairs m = n excluded as reducible, computed values are
  Singular's. The p_a identification is for the bidegree-(m,n) curve on
  P^1 x P^1, not the plane projective closure
holds-here: yes as a restatement, which is exact and needs no computation. The
  delta-invariant reading is the consequence, and it is what is not yet proved
status: checked
bearing: converts an unexplained closed form into one concrete statement to
  prove - that the singularities of C(x,m) = C(y,n) have total delta invariant
  ((m-1)(n-1) - 1 + gcd(m,n))/2 - and supplies the mechanism to look for, since
  g = p_a/2 for coprime m, n is a factor of exactly two and C(k-1-z,k) =
  (-1)^k C(z,k) gives the involutions z -> k-1-z that could produce it. Changes
  nothing about the conjecture: Faltings stays per-pair and ineffective, and a
  proved genus formula is still not a bound and still not uniform in k
anchor: code/out/genus_symmetric_form.captured.txt;
  code/out/genus_single_closed_form.md;
  code/out/pattern_verify_genus_formula.captured.txt
source: operator-computation
```
