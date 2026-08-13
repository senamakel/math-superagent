# Research verification of arc-closure-cs-polynomial (adopted approach)

This file records the research-specialist confirmation that the adopted
approach's central algebraic reduction is internally correct and that its
external anchors hold. It does not supersede the approach file; it verifies it.

## The unit-circle polynomial reduction — verified by hand

Setup (ring centre O at origin, real axis along OS, S at d): for a type-t
planet's upper tangency point P, write z = e^{i*beta} (beta = angle of P about
O) and mu = angle of P about S. The vector from S to P is a_p*z - d (complex),
its length is b_p and its direction is e^{i*mu}. Hence

    b_p * e^{i*mu} = a_p * z - d.

The meshing condition n_p in Z is (c-p)*beta + (s+p)*mu = pi*k. Multiply by i
and exponentiate:

    e^{i(c-p)*beta} * e^{i(s+p)*mu} = e^{i*pi*k} = (-1)^k
    z^{c-p} * (a_p*z - d)^{s+p} / b_p^{s+p} = (-1)^k

so

    z^{c-p} * (a_p*z - d)^{s+p} = (-1)^k * b_p^{s+p}.

Degree in z: (c-p) + (s+p) = c + s. Confirmed by direct algebra above.

**No square roots, no spurious-root injection, no trig.** This is the cleanest
exact root-counting formulation in the ledger, and it applies on the genuine
off-centre tangency triangle rather than the coaxial lattice. The identity
n_p + n_q = c+s (computed to 60 digits at arbitrary d in winner_refine.txt) is
what collapses the four-planet condition to the single monotone condition
n_p in Z; both the identity's status (numerically established, one elementary
geometric proof short of a theorem) and the endpoint-floor evaluation remain
the run's two open items, as the approach file's first-step records.

## External anchors — hold

- Kurasov 2020 (MATEC 329:03027), full text read: GES (off-centre gear, ring,
  two different-diameter satellites) assembly is NOT the coaxial formula
  (Z1+Z3)/k = C; it is a per-satellite-pair signed sum of (central-angle x
  tooth-count) = integer multiple of pi (eq. 7/8), plus a separate
  diameter/location vector-loop closure (eqs. 9-14). This is the off-centre
  precedent for the signed angle*tooth-count congruence that the adopted model
  instantiates. Caveat: exact signs in eq. (7) are OCR-garbled; the reading is
  taken from the search abstract.
- Segade-Robleda 2012 (IntechOpen, four-gear / idler simultaneous mesh):
  simultaneous engagement requires the pitch difference around the curvilinear
  quadrilateral to be a whole number of pitches, written
  r1*alpha + r2*beta - r3*gamma - r4*delta = n*pi*m. Same structural object.
- Guo 2011 (Ch. 5, eq. 5.21-5.25), Parker-Lin 2004, Zou 2015, Sun 2017: the
  coaxial least-mesh-angle assembly condition, which the adopted model reduces
  to as d->0.

## Status

- arc-closure-cs-polynomial: **grounded / adopted** — polynomial reduction
  verified, identity and endpoint-floor the only open items.
- Phrasing the discreteness as integer tooth-count congruences, including the
  off-centre case, is well-precedented (Kurasov eq. 7/8; Segade-Robleda eq. 1);
  the multiplicative / CRT closed-form and gcd-factorisation payoff of the
  refuted number-theoretic-crt / tooth-labelling-crt approaches is NOT
  supported by any source and is contradicted in outline by the tangency-forces-
  position structure (free variable is the single centre distance d, not four
  independent tooth indices).
