# Minimal polynomials for the coordinates of the Harborth graph — Gerbracht (2006)

**Source:** arxiv.org/abs/math/0609360
**Authors:** Eberhard H.-A. Gerbracht (2006)
**Full text:** NOT on disk — read via server-side read_sources (abstract + the
paper's own coordinate-machinery description).

## What this establishes — exact coordinates in high-degree number fields

- **The Harborth graph** is the smallest 4-regular planar unit-distance graph
  (52 vertices, 104 edges).
- The paper gives an **exact analytic description** of its coordinates: each
  vertex coordinate is an algebraic number defined by an explicit **minimal
  polynomial**, computed by a computer-algebra system.
- **Machinery.** Start from a parameter T (a y-coordinate, with primitive
  integer minimal polynomial P_T). Express the other y-coordinates as
  polynomials in T via the embedding equations; eliminate T by **resultants**
  to get polynomials in each coordinate alone:
  - y_D, y_E: degree 44 polynomials;
  - y_F: degree 88;
  - y_G, y_H, y_J: resultants of degree 176 in (y_P, T) then reducing by P_T,
    yielding irreducible factors of degree 22 — the minimal polynomials.
  - x-coordinates are tied to y-coordinates through the embedding equations.
- **Key point for the field arithmetic:** the coordinates cannot be expressed
  in radicals; the minimal polynomials *are* the exact description. This is
  exactly the "coordinates in a number field Q(α) given by a defining
  polynomial" regime the run's oracle must handle — not Q(√3, √11) but
  degree-22/44/88 extensions.

## Why it matters here

GOAL.md's oracle is `unit_graph(points)`: certify |x−y|² = 1 **symbolically**
over the exact algebraic field of the coordinates. The Harborth graph is the
natural max-stress test: 104 edges, all at distance exactly 1, coordinates in
a field given by minimal polynomials of degree up to 88 — too large for
Q(√3,√11) but exactly what a general exact-algebraic certifier (e.g. sympy's
`AlgebraicNumber` / field arithmetic over a defining polynomial) must handle.
Pairing it with the Heawood graph (14v/21e, degree ≤ ~4 fields) brackets the
certifier's envelope between a small rigid case and the largest classic rigid
planar unit-distance graph.

```claim
id: harborth-minimal-polynomials
statement: The Harborth graph (52 vertices, 104 edges, smallest 4-regular planar unit-distance graph) has an exact analytic embedding whose vertex coordinates are algebraic numbers with explicit minimal polynomials (degrees up to 88; y_G,y_H,y_J have irreducible factors of degree 22), not expressible in radicals. Minimal polynomials plus numerical approximations uniquely determine each coordinate.
hypotheses: the specific 4-regular planar embedding; coordinates algebraic over Q.
holds-here: yes - the natural max-stress exact-algebraic test case for the unit_graph edge certifier beyond Q(sqrt3,sqrt11).
status: sourced (Gerbracht arXiv math/0609360, via read_sources; full text not on disk)
bearing: sets the largest verified-exactly test graph for the oracle: 104 edges to certify at distance 1 in a degree-88-extensions field.
anchor: research/sources/gerbracht-harborth-2006.md
```

## Note on download

Full text network-blocked. Status: **sourced via read_sources; full text not
on disk**.