# Erdos unit distance problem — the O(n^{4/3}) bound

**Source:** Spencer, Szemerédi, Trotter, "Extremal problems in discrete
geometry", *Combinatorica* 4 (1984) 224–231 (bound). Modern treatment: Pach,
Raz, Solymosi, "Erdős's Unit Distance Problem and Rigidity", SoCG 2026,
https://doi.org/10.4230/lipics.socg.2026.83; also arXiv:2507.15679.

**How obtained:** server-side retrieval (`deep_research`) returned the exact
bound, attribution and the incidence ingredient from arXiv and textbook sources.

## What it establishes

**Theorem (Spencer–Szemerédi–Trotter 1984).** The maximum `u(n)` of the number
of unit-distance pairs among `n` points in the Euclidean plane satisfies

```
u(n) = O(n^{4/3})
```

The proof models each unit distance as an incidence between a point and a unit
circle centred at another point, then uses the **Szemerédi–Trotter incidence
theorem** — `I(P,L) = O(m^{2/3} n^{2/3} + m + n)` incidences between `m` points
and `n` lines — to bound the point-circle incidences, giving `O(n^{4/3})`.

**Supporting facts.**

- Lower bound (Erdős 1946): `u(n) = Ω(n^{1 + c/log log n})`, attained by a
  `√n × √n` grid, and Erdős conjectured `u(n) = n^{1+o(1)}`.
- The `O(n^{4/3})` upper bound has since been re-derived by Clarkson–Edelsbrunner–
  Guibas–Sharir–Welzl, Székely (crossing-number method), and Aronov–Sharir; not
  improved in the general case.
- For strictly convex norms the `O(n^{4/3})` bound persists and is optimal
  (Valtr); for norms with a straight segment in the unit-ball boundary, `Ω(n²)`
  unit distances are possible.
- Convex-polygon special case: `O(n log n)` (Füredi 1990; Brass–Pach; best
  constant Aggarwal 2015), with lower bound `~2n` (Edelsbrunner–Hajnal).

## Why it matters here

`problem.md` cites this as the constraint that "density cannot be bought" — a
unit-distance graph on `n` vertices has at most `O(n^{4/3})` edges, so a
high-chromatic graph must concentrate its edges through algebraic rigidity, not
raw density. The bound is what rules out the naive "many random points give many
edges" strategy and is the sourced basis for the "search over constructions, not
points" guidance.

## Basis and status

- `u(n) = O(n^{4/3})` — sourced (Spencer–Szemerédi–Trotter 1984, via modern
  restatements). Standard, accepted.
- Not re-verified computationally here (it is an asymptotic theorem).
