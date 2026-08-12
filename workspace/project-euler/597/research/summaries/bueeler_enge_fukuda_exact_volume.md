# Büeler–Enge–Fukuda: Exact Volume Computation for Polytopes — A Practical Study

Büeler, Enge, Fukuda, in *Polytopes — Combinatorics and Computation*, Birkhäuser, pp. 131–154 (2000). Book chapter, hal-03029034. [[bueeler_enge_fukuda_exact_volume.full]]

## What it establishes

A practical comparative study of exact polytope-volume algorithms, centred on the **triangulation method**: triangulate the polytope (e.g. by reverse-search, Motzkin-style signed decomposition, or recursive schemes) and sum the exact simplex volumes. Reports on which method beats which on which polytope classes (Delaunay triangulation vs. signed-decomposition vs. recursive schemes; the Lasserre-style recursive evaluation of the characteristic function).

## Hypotheses and whether they hold here

Hypotheses: the input is a single convex polytope given by facet inequalities; the task is its Euclidean volume. PE 597 needs the measure of a **union** of parity cells over a hyperplane arrangement; the number of cells (the genuine cost) grows super-exponentially with n and is not supplied by this source. The source itself notes that triangulation-based exact volume is expensive and best on polytopes of moderate dimension/facet count.

## What it lets this run compute / rule out

Corroborates that exact-volume machinery exists and is standard, but — like Latte — it operates **after** the cells are known. It neither enumerates arrangement chambers nor scales anything past the n≈5 barrier. The run's blocker (arrangement enumeration) is untouched by this tier.

## Does not settle

Any coefficient or value of p(n,L); the arrangement size; n=13. Read as confirmation that exact rational volume of a single polytope is feasible in principle, not that the union-of-cells route is tractable at n=13.

## Why it does not help at n=13

The cost of every method in this study is dominated by the polytope's combinatorial complexity (faces/triangles), which is exactly what explodes here. Dead end as a solver for the target.
