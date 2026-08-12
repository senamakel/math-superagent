# Brandenburg, De Loera & Meroni, "Critical moments of slices and slabs of the cube (and other polyhedral norms)" (arXiv:2603.25643, 2026)

Source URL: https://arxiv.org/abs/2603.25643 (full text at `research/sources/brandenburg_de_loera_meroni_slices_slabs_2026.full.md`). Sequel to the same authors' "The Best Ways to Slice a Polytope" (arXiv:2304.14239, already in the library).

## What it establishes

A unified algebraic-combinatorial framework for **explicit, piecewise-rational, combinatorially indexed parametric formulas for volumes and higher moments of slices and slabs of polyhedral norm balls** (extending the slice framework to slabs). The parameter space of all slices is decomposed into slicing chambers governed by hyperplane arrangements; within each chamber the volume/moment is a rational function of the (a,t) slicing parameters. This yields a polynomial-time algorithm (fixed dimension) for slice/slab moments of arbitrary order, plus an algebraic analysis of their critical points. Experimentally: for the 4-d unit cube, the volumes of slices and slabs are represented by exactly fourteen distinct rational functions across maximal slicing chambers (modulo signed coordinate permutations).

## Bearing on PE597

This is the strongest current statement that "a parametric family of polytope-section volumes is piecewise rational, chamber by chamber, and each chamber's formula can be obtained without visiting the polytope cells." It is direct support for the run's verified conjecture that **p(n,L) is a single rational function of m=L/40 on the physical range** (an analogue of the Brandenburg–De Loera–Meroni slicing-chamber theorem already in the library as `brandenburg_de_loera_meroni_best_ways_slice_polytope`). **Caveat:** the objects treated are slices/slabs of a fixed polytope by a *single* sweeping hyperplane family, whereas the torpids parity arrangement is an *arrangement cut into the simplex* (a union of simplex-section cells, summed with parity signs) — so this confirms the "rational-on-a-chamber" principle the run already relies on, but does not hand over the n=13 coefficients; the chamber decomposition of the parity arrangement itself is still the hard object.

## Cross-references

- Brandenburg–De Loera–Meroni 2023 (arXiv:2304.14239): same authors' slice-paper; Thm 1.1 rational-on-chamber.
- Lasserre "Volume of slices and sections of the simplex" (hal-01095071): closed-form simplex-section volumes.
- Latte / Büeler–Enge–Fukuda: exact integration over polytopes.
- König–Koldobsky: classical cube-slice volume formulas recovered by this framework.
