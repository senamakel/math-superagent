# Ferreira's claimed proof (arXiv:1506.06621) fails at equation (47)

Checked by the operator against the paper's own equations, taken from
`research/sources/arxiv-150606621-ferreira-fulltext.full.md`, which does carry
the numbered equations despite being only 6.8 KB.

## The step

The paper sets up two arithmetic progressions through the centre,

```
2e^2 = m^2 + n^2               (44)
2e^2 = (m-z)^2 + (n+w)^2       (45)
```

and subtracts them to get

```
(m-z)^2 + (n+w)^2 - m^2 - n^2 = 0        (46)
```

It then solves (46) for `z`, obtaining the two roots

```
z = m +/- sqrt(m^2 - 2nw - w^2)
```

and keeps `z2 = m - sqrt(m^2 - 2nw - w^2)`, rejecting the other because it
would make `m - z` negative. So far this is correct.

It then substitutes `z2` back into (46) and reports the result as

```
n^2 - 2nw - w^2 - (n+w)^2 = 0            (47)
```

which factors as `-2w(2n + w) = 0` and therefore forces `w = 0` or `w = -2n`.
Both are impossible for a square with distinct positive entries, and that is
the paper's contradiction.

## Why it fails

**`z2` was defined as a root of (46), so substituting it back into (46) can
only give `0 = 0`.** It is an identity, not a constraint, and it forces
nothing whatever.

Exactly:

```
m - z2 = sqrt(m^2 - 2nw - w^2)
(m - z2)^2 = m^2 - 2nw - w^2
```

so the left-hand side of (46) becomes

```
(m^2 - 2nw - w^2) + (n+w)^2 - m^2 - n^2
  = m^2 - 2nw - w^2 + n^2 + 2nw + w^2 - m^2 - n^2
  = 0
```

identically, for every `m`, `n`, `w` with the radicand non-negative.

Equation (47) is a different expression. The paper has replaced the `m^2` that
cancels with an `n^2`. The two differ by

```
0 - (n^2 - 2nw - w^2 - (n+w)^2) = 2w(2n + w)
```

which is non-zero for every `w > 0`, so (47) does not follow from the
substitution and the contradiction drawn from it is unsupported.

## Numerical confirmation

Five random admissible triples, exact where the radicand is a perfect square
and double precision otherwise:

```
 m    n   w    (46) at z2      paper's (47)
132    3   7   0               -182
 62    2   9   -4.5e-13        -234
 74    6  10   0               -440
 64    9   4   0               -176
 59    2   7   +4.5e-13        -154
```

(46) at `z2` is zero every time, as it must be. (47) is never zero. And (47)
does factor as the paper needs — `-2w(2n+w)`, checked at (n,w) = (3,5), (7,2),
(11,4) giving -110, -64, -208 — so the algebra *after* (47) is fine. The
failure is entirely in obtaining (47).

## What this settles and what it does not

It settles that this paper does not prove the conjecture, and it names the
step. It says nothing about whether the conjecture is true — the problem
remains open, which is independently corroborated by the run's own library:
Boyer/multimagie still runs a live search for an 8-square example, and
Rome–Yamagishi (2024) settle `n >= 4` while explicitly leaving `n = 3` open,
nine years after this preprint. The paper sits in `math.GM`, arXiv's category
for submissions not accepted into a substantive subject class.

```claim
id: ferreira-1506-06621-refuted
statement: The claimed proof of the non-existence of a 3x3 magic square of
  nine distinct squares in arXiv 1506.06621 (Ferreira) is invalid. Its
  equation (47) does not follow from the stated substitution. The paper solves
  its own equation (46) for z, keeps the root z2 = m - sqrt(m^2 - 2nw - w^2),
  and substitutes that root back into (46); since z2 is by construction a root
  of (46), the substitution is identically zero and constrains nothing. The
  reported (47) differs from the true result by 2w(2n + w), non-zero for every
  w > 0, so the contradiction w = 0 or w = -2n is unsupported.
hypotheses: the paper's own equations (44) through (47), with radicand
  m^2 - 2nw - w^2 non-negative
holds-here: yes, verified by direct algebra and by five random admissible
  triples
status: checked
bearing: removes a claimed resolution of this conjecture from the library; the
  problem stays open and no argument here may cite this paper as settling it.
  The failure mode is worth carrying forward, because substituting a solved
  root back into the equation it solved is an easy way to manufacture a
  vacuous identity and read it as a constraint
anchor: code/out/ferreira_proof_refuted.md; code/out/check_ferreira_proof.py;
  research/sources/arxiv-150606621-ferreira-fulltext.full.md
source: operator-computation
```
