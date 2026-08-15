# Chord/edge condition for the projective-line parametrisation — verification

Accompanying `research/approaches/unit-circle-projective-parametrization.md`.

```claim
id: unit-circle-chord-polynomial
statement: With p(t) = ((1-t^2)/(1+t^2), 2t/(1+t^2)) the rational parametrisation
  of the unit circle, two unit-direction points p(t1), p(t2) differ by a unit
  vector (i.e. |p(t1)-p(t2)|^2 = 1, equivalently p(t1).p(t2) = 1/2) iff
  t1^2 t2^2 - 3 t1^2 - 3 t2^2 + 8 t1 t2 + 1 = 0.
hypotheses: t1, t2 real, p(t) as given; valid over any field of characteristic
  != 2 where the denominator 1+t^2 != 0.
holds-here: yes — the Moser rotation (c=5/6, s=sqrt(11)/6) corresponds to
  t = 1/sqrt(11), and the 60-degree neighbour (t1=0, t2=1/sqrt(3)) is an edge;
  t1=t2 gives (t^2+1)^2, never an edge.
status: checked
bearing: the algebraic re-encoding of the unit-distance edge condition in the
  projective-line construction engine; makes edge/coincidence conditions into
  polynomial identities over the coordinate field.
anchor: research/approaches/unit-circle-projective-parametrization.md
```

Derivation (symbolic, closed form; the file `code/verify_chord_poly.py` carries
the sympy transcription for the run):

p(t1)·p(t2) = [(1-t1^2)(1-t2^2) + 4 t1 t2] / [(1+t1^2)(1+t2^2)].

Setting this equal to 1/2 and clearing denominators:

  2[(1-t1^2)(1-t2^2) + 4 t1 t2] = (1+t1^2)(1+t2^2)

Expand LHS: 2[1 - t1^2 - t2^2 + t1^2 t2^2 + 4 t1 t2]
        = 2 - 2t1^2 - 2t2^2 + 2 t1^2 t2^2 + 8 t1 t2.
RHS: 1 + t1^2 + t2^2 + t1^2 t2^2.

Bring all to LHS: (2-1) + (-2-1)t1^2 + (-2-1)t2^2 + (2-1)t1^2 t2^2 + 8 t1 t2
  = 1 - 3t1^2 - 3t2^2 + t1^2 t2^2 + 8 t1 t2.

So the condition is t1^2 t2^2 - 3 t1^2 - 3 t2^2 + 8 t1 t2 + 1 = 0. ✓

Checks:
- t1=0, t2=1/sqrt(3): 0 - 0 - 3(1/3) + 0 + 1 = -1 + 1 = 0 ✓ (the 60-degree edge;
  |p(0)-p(1/sqrt3)|^2 = 1 indeed).
- t1=t2=t: t^4 - 3t^2 - 3t^2 + 8t^2 + 1 = t^4 + 2t^2 + 1 = (t^2+1)^2 != 0, so
  never an edge (no self-loop) ✓.
- Moser rotation: t=1/sqrt(11) gives x=(1-1/11)/(1+1/11)= (10/11)/(12/11)=5/6,
  y=2(1/sqrt11)/(12/11)= (2/sqrt11)(11/12)= sqrt11/6. So c=5/6, s=sqrt11/6 ✓.

Status of the inventor's corrected form: CONFIRMED. The chord condition is real,
  and the Moser-spindle reconstruction in t-space is a valid cheap test of the
  engine.

## What this does NOT establish

The polynomial identity is an *encoding*; it does not create a new graph, nor
resolve whether any 5-chromatic candidate's parameter system is symbolically
solvable in an accessible field. That is the value question the approach's
first-step (reconstruct the spindle in t-space) answers.
