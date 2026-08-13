```approach
id: freys-curve-four-q-isogenies
idea: Recast the MSS as a problem about Q-rational isogenies of degree 4
  between elliptic curves.  Each AP of squares through the centre —
  a²−d, a², a²+d all squares — is equivalent via the classical congruent-
  number transformation to the elliptic curve E_d: y² = x³ − d²x having a
  point in 2E_d(Q).  But this is ALSO equivalent to: the curve
  E_{a²}: y² = x(x²−a⁴) admits a Q-rational 4-isogeny whose kernel
  contains a specific point.  The four AP conditions together force a
  configuration of four 4-isogenies on the same curve with linked kernels.
  The modular curve X₀(4) parametrising 4-isogenies is rational (genus 0),
  so one can write explicit coordinates; the four linked conditions define
  a curve C on X₀(4)⁴ whose rational points are the MSS.
status: refuted
killed-by: "P ∈ 2E(Q)" means P is a DOUBLE of some Q-point — equivalently
  {X, X±c} are rational squares — it is NOT a 4-isogeny kernel. E_n:
  y²=x³−n²x has exactly three rational 2-torsion points and lies in a
  FOUR-curve isogeny class connected by 2-isogenies (LMFDB congruent-
  number-curve knowl): there is no distinguished 4-isogeny tied to a point
  of 2E(Q); a 4-isogeny is a curve-level composite of two 2-isogenies,
  independent of which doubled point is selected. And the Robertson/Bremner
  reduction (Bremner, Acta Arith. 88 (1999) 289–297; Robertson 1996) is that
  an MSS ⇔ THREE points of 2E(Q) on the single curve E: y²=x(x²−c²) whose
  x-coordinates are in arithmetic progression — three points on one curve,
  not four linked 4-isogenies. The X₀(4)⁴ moduli curve does not match the
  actual MSS structure.
precedent:
  - "LMFDB, Congruent number curves",
    url: https://www.lmfdb.org/knowledge/show/ec.congruent_number_curve
  - "A. Bremner, On squares of squares, Acta Arith. 88 (1999) 289–297",
    url: https://matwbn.icm.edu.pl/ksiazki/aa/aa88/aa8837.pdf
    (Robertson reduction: three points in 2E(Q) with x-coords in AP)
  - "X0(N) parametrises cyclic N-isogenies; X0(4) rational; Jeon-Kwon,
    Explicit constructions of cyclic N-isogenies, arXiv:2512.21088"
  - "Claim: freys-4-isogeny-misidentifies-doubling (research/notes/
    literature-check-3-new-approaches.md)"
first-step: NONE. The doubling/4-isogeny conflation is structural. The
  correct object is the Robertson reduction (three points in 2E(Q) on one
  curve), which is the adopted uniform-height-bound-elliptic-ap thread, not
  a 4-isogeny moduli curve.
speculation: (as originally written) "the 4-isogeny formulation has not been
  applied to MSS before." True but for a bad reason: it does not correspond
  to the MSS structure at all.
```
