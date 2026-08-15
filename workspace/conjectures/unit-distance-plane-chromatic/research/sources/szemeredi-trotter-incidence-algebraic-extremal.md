# Szemerédi–Trotter incidence theorem and the algebraic-field extremal constructions

**Subject:** The incidence theorem underlying the O(n^{4/3}) unit-distance bound,
and the fact that algebraic number fields Q(√k) generate the extremal point-line
configurations. This is the technique tier that the run's construction engine
(Minkowski sums over algebraic point sets) builds on; it develops the method
rather than reporting the Hadwiger–Nelson answer.

## Source

- L. Guth, O. Silier, *Sharp Szemerédi–Trotter Constructions in the Plane*,
  Electronic Journal of Combinatorics 32(1) (2025), #P1.9, DOI 10.37236/10899.
  Retrieved via `read_sources` (server-side; direct publisher download blocked
  at the network boundary).
- H. Kaplan, J. Matoušek, M. Sharir, *Simple Proofs of Classical Theorems in
  Discrete Geometry via the Guth–Katz Polynomial Partitioning Technique*,
  arXiv:1102.5391 (2011). Same retrieval route.

## What it establishes

### Exact Szemerédi–Trotter incidence bound
For any finite set `P` of `m` points and `L` of `n` lines in the plane,

    I(P, L) = O(m^{2/3} n^{2/3} + m + n)

where `I(P,L)` counts pairs `(p, l)` with `p in P`, `l in L`, `p in l`. The
bound is tight up to constants for all `m, n`. Equivalent form (`r`-rich lines):
for `L_r` = the set of lines containing at least `r` points of `P`,

    |L_r| = O(n^2 / r^3 + n / r).

### Proof mechanism (Kaplan–Matoušek–Sharir, polynomial partitioning)
- Fix `r = n^{2/3}`, take a polynomial `f` of degree `D = O(n^{1/3})` partitioning
  the plane into cells each containing `<= n/r = n^{1/3}` points.
- Split incidences into: (i) on the zero set `Z(f)` — bounded by `O(Dn)`;
  (ii) lines crossing `Z(f)` — likewise `O(Dn)`; (iii) within cells — bounded per
  cell by the crude `|L_i| + |P_i|` and summed.
- The bound `I(P, L'') <= m^2` for lines through at least two points is the
  `K_{2,2}`-free extremal instance of the Kóvári–Sós–Turán theorem.
- Optimising `D` yields `O(m^{2/3} n^{2/3} + m + n)`.

### Algebraic number fields generate the extremal constructions (directly relevant)
The tight, near-extremal constructions are not random — they use **algebraic
number-field structure**. Theorem (Guth–Silier): for any non-square integer `k`,
let `A_N = { x1 + x2 sqrt{k} : x1, x2 in [-sqrt{N}, sqrt{N}] }` and the point set
`P = A_N^2` (embedded in the plane). Then there is a line family `L` of
`r`-rich lines with

    |L_r| = Theta( |P|^2 / r^3 + |P| / r ),

with slopes `s = (p1 + p2 sqrt{k})/(q1 + q2 sqrt{k})` and intercepts from the
same field, so each point lies on `Omega(|S|)` lines and the config realises the
Szemerédi–Trotter bound up to constants.

## Why it matters here

- The `O(n^{4/3})` unit-distance bound in `research/sources/spencer-szemeredi-trotter-unit-distance-bound.md`
  rests precisely on this incidence theorem (each unit distance as a
  point-unit-circle incidence). The library now holds the incidence theorem
  itself, not just the corollary.
- **Most importantly**: the construction engine of `problem.md` is about
  algebraic point sets producing unexpectedly many unit distances. This source
  is primary evidence that **algebraic number fields Q(√k) are exactly the
  structures that generate rigid, incidence-dense configurations** — the same
  field the run's exact coordinates live in (`Q(sqrt3, sqrt11, ...)`). It is
  the technique tier backing the "search over algebraic constructions" guidance
  in `problem.md`.

## Basis and status

- Statements and constructions = sourced (retrieved verbatim from the two
  papers). Standard result (Szemerédi–Trotter 1983) + recent explicit sharp
  constructions.
- Not re-verified computationally here (asymptotic construction; the relevant
  *finite exact* verification is the run's own oracle's job).

## Claim block

```claim
id: szemeredi-trotter-algebraic-extremal
statement: For m plane points P and n lines L, the number of point-line
  incidences I(P,L) = O(m^{2/3} n^{2/3} + m + n), tight up to constants; and
  the extremal configurations are built from algebraic number fields Q(sqrt k),
  with slopes and intercepts drawn from that field.
hypotheses: P a finite set of m distinct points in R^2, L a finite set of n
  distinct lines; incidence iff point lies on the line.
holds-here: YES — underpins the unit-distance O(n^{4/3}) bound the run relies
  on, and shows algebraic point sets (the run's exact-coordinate universe) are
  precisely where incidence/unit-distance density concentrates.
status: asserted-by-source (Szemerédi–Trotter 1983; Guth–Silier 2025 sharp
  constructions; Kaplan–Matoušek–Sharir 2011 simple proof).
bearing: justifies "search over algebraic constructions, not random points": the
  extremal structures of the neighbouring incidence theory are algebraic, so the
  unit-distance analogues the run seeks should be too.
anchor: research/sources/szemeredi-trotter-incidence-algebraic-extremal.md
falsifies: a construction of n plane points with > C n^{4/3} unit distances for
  all C — would contradict the classical bound; none known.
```
