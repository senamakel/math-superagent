# Approach — Mahler functional equation for the generating function

```approach
idea: Recover the fixed-point sets of f(n,d)=n from the Mahler functional
equation of the ordinary generating function G_d(x) = Σ_n f(n,d) x^n, using
the Mahler↔regular-sequence correspondence (Becker; Allouche–Shallit).
mechanism: f(n,d) is 10-regular (see the regular-sequence approach), so each
G_d is a Mahler function satisfying a linear Mahler-type functional equation
relating G_d(x) to G_d(x^10).  The known instance is A094798 (f(n,1)): its
g.f. g(x) satisfies g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))^2 g(x^10),
recorded in research/notes/oeis-catalogue-pe156.md.  The equation
f(n,d) = n is, coefficient-wise, the vanishing of the difference of G_d(x)
and x/(1−x)^2 = Σ_n n x^n.  Coefficient extraction on the Mahler equation
turns that vanishing condition into a functional identity analysed
10-adically layer by layer (blocks of 10^m consecutive coefficients), which
has a chance of yielding a recurrence or closed form for the solutions —
rather than a numeric search over the interval.
status: proposed
first-step: derive G_d(x) directly from the place-value closed form (or from
the c_d(10n+r) recurrence), substitute, and produce the linear Mahler
functional equation for each d; check that the d=1 case reduces exactly to
the quoted A094798 equation, then attempt to read the coefficient-equality
solutions off the equation.
```

## Which parts are established, which are speculation

- **Established.** The A094798 generating-function equation is quoted in
  `research/notes/oeis-catalogue-pe156.md` (sourced OEIS entry on disk). The
  theorem that a sequence is k-regular iff its generating function satisfies
  a linear Mahler functional equation is standard (Becker 1994; see
  Allouche–Shallit Ch. 5).
- **Speculation.** That the specific Mahler system for G_d is algebraically
  tractable enough to *read off* the fixed points in closed form; nothing on
  disk has derived the system for general d yet. This is a genuine transform
  route — the generating function, not pointwise digit arithmetic — and is
  research-checkable against the Mahler-function literature.
