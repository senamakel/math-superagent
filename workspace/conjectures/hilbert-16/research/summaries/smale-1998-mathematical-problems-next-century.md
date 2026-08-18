# Smale, "Mathematical problems for the next century" (1998) — Problem 13 (Hilbert's 16th)

<!-- source: https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/muller/SmaleProblems1998.pdf | converted from PDF; full text at research/sources/smale-1998-mathematical-problems-next-century.full.md -->

## What it establishes

Problem 13 states the modern form of Hilbert's 16th (second part): for the planar
polynomial system `dx/dt = P(x,y), dy/dt = Q(x,y)`, is there a bound on the number
of limit cycles of the form `K ≤ d^q`, where `d = max(deg P, deg Q)` and `q` is a
universal constant? Smale: "Except for the Riemann hypothesis, it seems to be the
most elusive of Hilbert's problems."

History, in Smale's own words (lines 616–625 of the held full text):
- Dulac (1923) claimed every system (4) has finitely many limit cycles.
- Petrovskii–Landis (1957) purported a positive solution; a gap was found
  (Petrovskii–Landis 1959 letter); Shi Songling (1982) gave a counterexample to
  the *specific bounds* of Petrovskii–Landis for `d = 2`.
- Ilyashenko (1985) found the error in Dulac's paper.
- Écalle (1992) and Ilyashenko (1991) independently proved Dulac's assertion
  ("these two papers have yet to be thoroughly digested by the mathematical
  community" — 1998). "Thus one has the finiteness, but no bounds."

Special class (Smale's own formulation of the Liénard problem): `dx/dt = y − f(x),
dy/dt = −x`, `f` real polynomial with leading term `x^(2k+1)`, `f(0) = 0`. All
solutions circle the unique equilibrium; the Poincaré section map `T: R+ → R+` on
the positive y-axis has the limit cycles as its fixed points. Lins–de Melo–Pugh
(1977) found examples with `k` limit cycles and conjectured `k` as the upper bound;
"still no upper bound of the form (deg f)^q has been found."

Also relevant: the "Pugh problem" (`K(d)` for the 1-variable equation with
`C^∞` coefficients) — McMullen's answer: for `d > 2` there can be arbitrarily
many fixed points; the map is translation/affine/Möbius for `d = 0, 1, 2`. This is
the `C^∞` unboundedness phenomenon in miniature: **smooth coefficients allow
unbounded counts, polynomial/analytic ones (conjecturally) do not** — the smooth
test of problem.md has this exact shape.

## What it implies for this run

- The problem statement in the run's `GOAL.md`/`problem.md` is the correct modern
  form; Smale's `d^q` is a *stronger* uniform bound than H(n) < ∞ (polynomial in
  the degree). H(2) < ∞ remains open in this formulation too.
- Confirms (asserted-by-source, primary) the attribution history used in claim
  `h16-petrovskii-landis-retracted` and `h16-dulac-finiteness-theorem`:
  Petrovskii–Landis retracted; Shi Songling's counterexample targets their
  specific bounds (H(2) ≥ 4 witness); finiteness without bounds is the Écalle/
  Ilyashenko state of the art.
- The Liénard LMP conjecture (k cycles for degree 2k+1) is restated here in the
  author's own words — the survey `llibre-zhang-lienard-conjecture-survey` (held)
  documents its failure for n ≥ 6 via slow–fast constructions.

## Evidence class

`asserted-by-source` — Smale's own 1998 essay (primary), full text held. This is
the statement/history anchor, not a proof of any bound.

## Anchors

- Full text: `research/sources/smale-1998-mathematical-problems-next-century.full.md`
- Lines 601–660: Problem 13 statement, history, Liénard class, Pugh problem.
