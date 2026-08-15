# Klazar, "Analytic and Combinatorial Number Theory II" — Thue's theorem

## Source
- Klazar, Martin, "Analytic and Combinatorial Number Theory II" (NDMI045,
  Charles University Prague, Summer 2010; lecture notes PDF).
  Chapter 1: "Thue's theorem on Diophantine equations".
- URL: https://kam.mff.cuni.cz/~klazar/ln_antcII.pdf
- How obtained: **server-side full-text readout via `read_sources`**.
  `download_document` is refused on this host by the network boundary; this is
  a captured readout (record of the primary content returned, with provenance),
  not a stored PDF. Read its claims as `asserted` by source until re-checked
  in-workspace.

## Why this source is in the library
The run performed Thue-descent work in-workspace without a source record of the
underlying theorem: `code/out/thue_unit_descent.md` (equations `a_n + b_n ω +
c_n ω^2 = (1-ω)^n`, Thue equation `c^3 - 2 d^3 = ±...`), `code/refute/thue_*.py`,
`r35` Eisenstein/Thue work. This note supplies the primary statement of Thue's
finiteness theorem that those programs are instances of, and — importantly —
the exact scope limits that say why Thue's theorem *alone* cannot resolve
`x^p - y^q = 1` in general.

## Content established (as retrieved)

### Thue's theorem (1908/1909) — exact statement
Let `P(x, y) ∈ Z[x, y]` be a homogeneous polynomial of degree `d ≥ 3`, nonzero
and irreducible in `Z[x, y]`. For any fixed integer `m`, the Diophantine
equation

    P(x, y) = m

has only finitely many integral solutions `(x, y) ∈ Z^2`.

### Thue's inequality (1909)
Let `α ∈ C` be algebraic of degree `d`, and `ε ∈ (0, 1/2)`. Then only finitely
many fractions `p/q ∈ Q` satisfy `|α - p/q| < q^{-(d/2 + 1 + ε)}` (equivalently
the strong-approximation exponent `n/2 + 1`). Thue's theorem is proved from
this inequality (a polynomial-method / double-approximation argument): reduce
`P(x,y) = m` to rational approximation of a root of the polynomial
`P(z, 1)`, select two close rational approximations, and derive a
contradictory pair of bounds on a high-order derivative.

### Scope and limitations for `x^p - y^q = 1`
- Applies to: any irreducible homogeneous `P` of degree `d ≥ 3` equals a
  constant; more generally `P(x,y) = Q(x,y)` for `Q` of degree `< d/2 - 1`.
- Does **not** cover `x^p - y^q = 1` in general: this is a difference of two
  monomials of different degrees set equal to 1, not a single fixed irreducible
  homogeneous polynomial of degree `d ≥ 3` in two variables equal to a
  constant with **fixed** degree. For varying exponent pairs it is an
  exponential-type / S-unit equation, which needs the Baker/linear-forms
  machinery (library: `tijdeman-linear-forms-survey.md`) or Baker–Wüstholz /
  hypergeometric / subspace theorems, not Thue's theorem per se.

## Relation to the known solution
`3^2 - 2^3 = 1` is a single point; Thue finiteness is a statement about the
*number* of solutions of a *fixed-degree* equation, so it neither includes nor
excludes this one point. The run's Thue-descent applications are to fixed
*(p,q)* reductions (e.g. `x^2 - y^3 = 1` → Thue equation in `Q(cuberoot 2)`),
where the theorem is exactly the right tool, and its known solution
`(x,y)=(3,2)` is a genuine member of the finite solution set — a Thue argument
that rules it out is a false argument, and the run's `thue_unit_descent` check
(`c_n` coefficient vanishes exactly at `n ∈ {0,1}` within `|n| ≤ 2000`) is the
correct calibration that keeps the known solution.

```claim
id: thue-finiteness-theorem
statement: For a homogeneous nonzero irreducible P(x,y) ∈ Z[x,y] of degree
  d ≥ 3, the equation P(x,y) = m has only finitely many integral solutions for
  every fixed integer m; proved from Thue's inequality |α - p/q| > c q^{-(d/2+ε)}
  for algebraic α of degree d.
hypotheses: P homogeneous, deg d ≥ 3, irreducible over Z; m fixed.
holds-here: yes for the run's fixed-(p,q) Thue reductions (e.g. Q(cuberoot 2))
  — see thue_unit_descent, r35; for the full x^p - y^q = 1 with varying
  exponents Thue's theorem alone does NOT apply (scope limit above).
status: asserted-by-source (Klazar lecture notes Ch. 1; standard theorem).
anchor: research/sources/klazar-thue-theorem.primary.md
bearing: names the tool the run's fixed-exponent descents rest on and its exact
  boundary; prevents over-claiming Thue as a route to the full conjecture.
```

## Provenance note
Faithful record of a server-side readout of a freely-hosted university PDF.
`download_document` is refused on this host by the network boundary; do not
retry. The exact proof details (Siegel/Gauss lemmas, double-approximation
bounds) are summarised; for the full proof one would fetch the host — over the
boundary, unavailable here.
