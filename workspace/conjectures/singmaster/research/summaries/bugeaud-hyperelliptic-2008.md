# Integral points on hyperelliptic curves (effective method)

Source: Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, Sz. Tengely,
"Integral points on hyperelliptic curves", Algebra & Number Theory 2:8 (2008)
859–885; arXiv:0801.4459.
Full text: `research/sources/bugeaud-hyperelliptic-2008.full.md`.

## What it establishes

For a hyperelliptic curve `C: Y^2 = a_n X^n + ... + a_0` with `n >= 5` and the
right-hand polynomial squarefree/irreducible, this gives:

1. **A completely explicit upper bound** on the integral points, combining
   Matveev's bounds for linear forms in logarithms, refined height estimates
   (Voutier, Bugeaud), and regulator estimates (Landau). The bound is usable
   *provided* one knows a rational point on `C` and a Mordell–Weil basis for
   the Jacobian `J(Q)`.
2. **A refined Mordell–Weil sieve** that, combined with the bound, can
   determine *all* integral points.

Illustrated by completely determining the integral points on the genus-2
models `Y^2 - Y = X^5 - X` and `Y^2 = X^5`.

Remark (from the paper's introduction) that underlies how these bounds were
historically seen as "astronomical": even with improvements the constants are
enormous. This paper's contribution is to make the bound *explicit* (hence
usable) and then drive it down with the sieve.

## Relevance to this run

This is the **method paper** behind the `C(x,2)=C(y,5)` binomial case
(Bugeaud–Mignotte–Siksek–Stoll–Tengely, credited in de Weger/MRSTT): the
binomial-equality curve for that pair is hyperelliptic and this is how its
integral points were settled. It is the machine that would produce *one specific
effective bound with a computed constant* for a chosen `(k1,k2)` family — one
of the four GOAL deliverables.

It does **not** give a bound uniform in `(k1,k2)`: every constant depends on
the specific curve (height, discriminant, regulator, Mordell–Weil rank), and
the Mordell–Weil-basis requirement is not effective uniformly in `n`. So this
confirms the shape of the obstruction: effective per-pair, not uniform in the
pair, via an explicitly-compu-table route when the curve data is available.

Evidence class: sourced (full text read).
