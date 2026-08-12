# Latte: Software for Exact Integration of Polynomials over Polyhedra

De Loera, Dutra, Koeppe, Moreinis, Pinto, Wu, arXiv:1108.0117 (Comput. Geom. 46, 232–252). [[latte_integrale_exact_integration.full]]

## What it establishes

- Provides software for the **exact (rational) integration of polynomial functions over convex rational polyhedra**, by triangulating the polyhedron into simplexes and integrating each simplex exactly (Baran/signed-decomposition style algorithms), with speedups over earlier work.
- The integrand can be any polynomial; the result on a rational polytope is an exact rational.
- Benchmarked on a combinatorial-voting-theory challenge (approval-voting polytopes).

## Hypotheses and whether they hold here

Hypotheses: the integration region must be **one convex rational polytope**, and the polynomial integrand is given. In PE 597 the parity region is a **finite union** of simplex sections (each cell of the bump/finish arrangement), not one polytope, and each cell must be *enumerated* first. So Latte computes the exact volume of a given polytope but does **not** find the cells: the arrangement enumeration (the run's actual blocker, ~13,750 cells already at n=5, super-exponential at n=13) is upstream of anything Latte can do.

## What it lets this run compute / rule out

Confirms the "exact rational value in principle" part of the run's positive route (a cell's measure is an exact rational), but as a tool it is downstream of the blocker. It does **not** remove the need to enumerate or to find a structural reduction. Useful only if the run ever has the n=13 cell list (it does not), or as a cross-check on the small-n exact values already produced by `code/cell_exact.py`.

## Does not settle

The finite-finish parity, the arrangement size, or any coefficient of p(n,L). Pointer, not a solver.
