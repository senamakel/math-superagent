# Inventor converging decision — three proposals (this cycle)

Memory server was down at decision time; this note stands in for `remember_memory`.

## Disposition

- **ADOPTED** `rotated-field-sturm-comparison` — restricted, displacement-centered:
  rotated-vector-field (field-rotation parameter) principle + Cherkas/Riccati
  reduction + exact Sturm comparison. See
  `research/approaches/rotated-field-sturm-comparison.md`.
- **REFUTED** `dulac-positivstellensatz-region-atlas` — exclusion-only certificate;
  cannot bound displacement zeros on cycle-supporting cells; its surviving
  certificate aspect is the run's existing Dulac/SOS nonexistence oracle
  (GOAL §3 oracle #2). See `research/approaches/dulac-positivstellensatz-region-atlas.md`.
- **NARROWED** `schwarzian-return-map-cross-ratio` — Kozlovski/Singer hypotheses
  fail for analytic Poincare diffeomorphisms; survives only for
  piecewise-smooth/unimodal/Abel-reduction return maps with a proved critical
  point and global Schwarzian sign. See
  `research/approaches/schwarzian-return-map-cross-ratio.md`.

## Why rotated-field beat the other two

It is the only candidate whose natural object is directly the parameterized
nonlinear displacement (the run's mandated object), and for which the literature
supplies a matching monotonicity/termination framework: Duff–Perko monotone
motion, Wintner–Perko termination, Gaiko and Perko quadratic rotated-field
analyses, Giacomini–Grau Sturm-certified sign tests, Gasull–Santana status note.
The Dulac atlas certifies only no-cycle regions and never touches the
displacement on cycle-supporting cells. Schwarzian requires a critical point /
unimodal interval map, which the generic analytic return diffeomorphism lacks.

## First step (tool_builder-ready)

Quadratic rotated family

    X_a = (P_a, Q_a) = (-y + a(1-x^2)y, x)

on a rational compact parameter/section box:
1. compute the rotation determinant
   D(a,s) = P_a(x(s),y(s))·∂aQ_a(x(s),y(s)) − Q_a(x(s),y(s))·∂aP_a(x(s),y(s))
   exactly (sympy over Q);
2. certify the sign of D on the box with a Sturm chain, or record the first
   sign-changing subbox (that subbox is a counterexample that narrows the scope);
3. only then derive and check the Cherkas/Riccati comparison equation for the
   displacement, with explicit nonsingularity and endpoint hypotheses.

Built-in falsifiers: sign change of D, singular Cherkas transform, mismatch
between Sturm roots of the scalar comparison equation and zeros of the nonlinear
displacement.
