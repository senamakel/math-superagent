# Conrad, "Arithmetic Progressions of Four Squares"

[[conrad-arithmetic-progressions-of-four-squares]]

Source: Keith Conrad, "Arithmetic Progressions of Four Squares",
https://kconrad.math.uconn.edu/blurbs/ugradnumthy/4squarearithprog.pdf .
Full text at `research/sources/conrad-arithmetic-progressions-of-four-squares.full.md`.

## What it establishes

The classical n=4 case of the run's exact elliptic formulation: a nonconstant 4-term
arithmetic progression of **rational** squares does **not** exist — Fermat's question
(1640). Conrad's route is the same elliptic-curve bridge the MSS uses, so it models
the method.

**Theorem 2.3.** The 4-tuples `[a,b,c,d] ∈ P³(R)` such that `a², b², c², d²` form an
arithmetic progression are parametrised by the points on the elliptic curve
`E : y² = (x−1)(x²−4)`.

**Corollary 3.3.** If a nonconstant 4-term AP of rational squares existed, there would be
infinitely many, not scalar multiples of each other.

**Theorem 3.4.** A nonconstant 4-term arithmetic progression of rational squares does not
exist.

The mechanism: `E` has exactly 8 rational points `[0,1,0], (±2,0), (1,0), (0,±2), (4,±6)`
(the `0` of Theorem 3.1), these are its **full torsion subgroup**, and every 4-AP of
squares pulls back to a rational point on `E`. Since a non-torsion rational point would
generate infinitely many (Corollary 3.3) and `E(Q)` is entirely torsion, no nonconstant
4-AP exists.

## Bearing on the 3×3 MSS

- The MSS needs a **middle square lying in four 3-term APs** (differences `u,v,u+v,u−v`),
  which is a *different, weaker-than-n=4* configuration: three distinct squares in an AP
  exist (1, 25, 49), and four distinct squares from any single AP do not.
- The method transfers: any candidate AP-of-squares structure is an intersection of
  quadrics, hence rational points on an elliptic curve (here the concrete `y²=(x−1)(x²−4)`
  with a finite Mordell–Weil group). The run's Robertson curve `E_c: y²=x(x²−c²)` is
  exactly this kind of object.
- Conrad's finite-Selmer/rank determination is the model for the claim the run's uniform-
  height and rank threads need: show a candidate curve has only its torsion points.
  Here `E(Q) ≅ Z/2 × Z/4` (Cremona form `y²=x(x+1)(x+4)`, 24A1, per van der Poorten).

```claim
id: four-squares-in-ap-elliptic-reduction
statement: A 4-tuple [a,b,c,d] whose squares form a nonconstant arithmetic progression
  is parametrised by rational points on E: y²=(x−1)(x²−4); E(Q) is exactly its 8-point
  torsion subgroup, so no nonconstant 4-term AP of rational (hence integer) squares
  exists (Conrad Thm 3.4).
hypotheses: rational (equivalently, after clearing, integer) squares; nonconstant AP.
holds-here: yes — this is the classical n=4 case; the MSS needs a middle square in four
  3-term APs, which is weaker in each AP but adds the additive-linkage obstruction.
status: proved (Conrad; finite Selmer/rank computation in the paper)
bearing: the elliptic-curve bridge Q_squares-in-AP ⇄ E(Q) is the exact method the run's
  Robertson reduction uses at length 3; Conrad is the reference for how the length-4 case
  is closed by a finite E(Q).
anchor: research/summaries/conrad-arithmetic-progressions-of-four-squares.md
```

## Falsifier

A nonconstant integer 4-term AP of squares would falsify Theorem 3.4. None exists; the
claim's elliptic bridge is independently documented in Gordon–Graham (descent proof) and
van der Poorten (descent + Cremona `y²=x(x+1)(x+4)`).
