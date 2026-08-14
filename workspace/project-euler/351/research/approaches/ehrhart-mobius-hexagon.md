# Ehrhart / Möbius inversion on the hexagon

```approach
idea: Count visible lattice points as *primitive* points of the dilated hexagon polygon via Ehrhart's theorem + Möbius inversion (Baake–Grimm–Warrington primitive-point counting)
mechanism: The order-n orchard is the lattice polygon P_n = {(x,y) ∈ Z² : |x|≤n, |y|≤n, |x+y|≤n}, the regular hexagon whose vertex set is lattice points, so Ehrhart's theorem gives the exact polynomial L_P(t) = 3t² + 3t + 1 for the number of lattice points in tP. Splitting each lattice point by its primitive ancestor (divide by gcd), the primitive-point count obeys the floor-quotient relation L_P(n) − 1 = Σ_{t≤n} p(t)⌊n/t⌋, where p(t) is the number of primitive non-origin points of exact dilation order t. Möbius inversion then gives P(n) = 1 + Σ_{d≤n} μ(d)(L_P(⌊n/d⌋) − 1), which collapses exactly (the −1 kills the constant term, and Σ μ(d)⌊n/d⌋ = 1) to P(n) = 1 + 6Φ(n). Hidden = L_P(n) − P(n) = 3n² + 3n − 6Φ(n).
precedent: summatory-totient-mobius-identity; euler-phi-mobius-convolution; visible-points-primitive-corroboration; polygon-primitive-point-asymptotic; https://doi.org/10.1007/978-1-4939-2969-6_3; https://link.springer.com/article/10.1007/s11139-020-00302-w
status: adopted
first-step: (1) Verify L_P(t)=3t²+3t+1 for t=1..6 by direct point counting. (2) Establish the new structural fact of this line: split the hexagon into 6 sextants around the origin and confirm each holds exactly Φ(n) primitive points — the geometric meaning of P(n)=1+6Φ(n) — against the brute oracle for n=1..100. (3) Record Φ(n)=½Σ_{d≤n}μ(d)⌊n/d⌋(⌊n/d⌋+1) as the bridge: it is the leading term of Brown's Mertens-first totient formula (arXiv:2506.07386, a=n, b=1), so the geometric derivation and the analytic sublinear routes meet at one identity.
```

## Grounding verdict

status: grounded

The reformulation is precisely **Ehrhart theory for lattice polygons**: for a
lattice polygon P, L_P(t) = #(tP ∩ Z²) is a degree-2 polynomial in t (Ehrhart
1959/62; standard modern treatment Beck–Robins, *Counting Lattice Points in
Polytopes*, §3). For the hexagon the polynomial is 3t² + 3t + 1. The collapse
is not speculative — it is exact:

- L_P(t) − 1 = 3t(t+1).
- P(n) = 1 + Σ_{d≤n} μ(d)(L_P(⌊n/d⌋) − 1)
      = 1 + 3 Σ_{d≤n} μ(d)·⌊n/d⌋(⌊n/d⌋+1)
      = 1 + 6Φ(n)   [by `summatory-totient-mobius-identity`:
                     Φ(n) = (1/2)Σ_d μ(d)⌊n/d⌋(⌊n/d⌋+1)]
- H(n) = L_P(n) − P(n) = 3n²+3n+1 − 1 − 6Φ(n) = 3n²+3n−6Φ(n). ✓

So every hypothesis holds: the hexagon is a lattice polygon (vertices are
lattice points), t-dilations give the order-t orchard, and the primitive-point
splitting ("visible point iff gcd=1, divide by the gcd ancestor") is exactly
the Baake–Grimm–Warrington / Martin theory already in the library
(`visible-points-primitive-corroboration`, `polygon-primitive-point-asymptotic`).
The only ingredient the collapse needs — the summatory-totient Möbius identity
— is a sourced claim in the ledger (`summatory-totient-mobius-identity`,
`euler-phi-mobius-convolution`).

Whether anyone applied it *to this problem*: the Ehrhart-polynomial route to
3n²+3n+1 is standard (it is what any textbook computes for a regular hexagonal
lattice region), and the primitive-point/Möbius counting of visible points in
dilated polygons is the established method of the visible-point literature
(Martin; Hensley; Beck–Robins §3). No published PE-351 solution discovered in
this search (and none was sought — that would invalidate the run); the point
is that every theorem invoked is textbook, with hypotheses that hold exactly.

What it buys: a **new derivation** of the closed form H(n)=3n²+3n−6Φ(n), and
grounding of the whole problem in Ehrhart/visible-point theory rather than the
per-point gcd sieve. It is not a faster computation — it collapses to the same
Φ(n) — so it is a structural/derivational alternative and a verification route
(P(n) = 1+6Φ(n) can be checked on small n).

precedent:
  - summatory-totient-mobius-identity (ledger claim)
  - euler-phi-mobius-convolution (ledger claim)
  - visible-points-primitive-corroboration (ledger claim)
  - polygon-primitive-point-asymptotic (ledger claim)
  - https://doi.org/10.1007/978-1-4939-2969-6_3  (Beck & Robins, Ehrhart theory)
  - https://link.springer.com/article/10.1007/s11139-020-00302-w (visible points along curves, Möbius inversion)

## Why it is a different line

The adopted method derives H(n) = 3n²+3n−6Φ(n) by the per-point gcd=1 criterion, then sieves φ. This line never touches φ per point: the object is the *Ehrhart quasipolynomial* of a lattice polygon, and the closed form falls out of Möbius inversion of the geometric point-count. It is a new **derivation** of the closed form, and grounds the whole problem in the Baake–Grimm–Warrington theory of visible points in lattices (sources already in `research/sources/`). The final μ-sum is computationally the same object as the Möbius verification already run, so this is a structural/derivational alternative, not a faster computation — marked accordingly.

## Grounding in the library

- `research/sources/primitive-points-rational-polygons.full.md`, `research/sources/baake-grimm-warrington-visible-points-lattice.full.md` — primitive points in polygons and lattices.
- `research/summaries/mathworld-visible-point.md` — visible point iff gcd = 1.
- `euler-phi-mobius-convolution` and `summatory-totient-mobius-identity` in `research/CLAIMS.md` — the μ-identities used in the collapse.

## Key arithmetic (checked by hand here, to be re-verified by tool_builder)

- L_P(1)=7, L_P(2)=19; L_P(t)=3t²+3t+1.
- P(2)=13 = 1 + μ(1)(19−1) + μ(2)(7−1) = 1+18−6.
- P(n) = 1 + 6Φ(n); so H(n) = L_P(n) − P(n) = 3n²+3n−6Φ(n).
