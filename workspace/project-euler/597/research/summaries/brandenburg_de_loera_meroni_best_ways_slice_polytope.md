# Brandenburg, De Loera & Meroni, "The Best Ways to Slice a Polytope" — summary

<!-- source: https://arxiv.org/pdf/2304.14239 | Marie-Charlotte Brandenburg, Jesús A. De Loera, Chiara Meroni, arXiv:2304.14239 (2023) -->

Full text at `research/sources/brandenburg_de_loera_meroni_best_ways_slice_polytope.full.md` (105k chars).

## What the source establishes

For a polytope P ⊂ R^d, the space of all affine hyperplane sections of P is
partitioned into finitely many **slicing chambers**, organized by pairs of
hyperplane arrangements; within one chamber the combinatorial type of the
section P ∩ H is fixed.

The key results for us:

- **Theorem 1.1**: within a fixed slicing chamber, the integral of any
  polynomial over the slice P ∩ H (in particular the volume) is a **rational
  function of the hyperplane parameters**, depending only on the chamber's
  combinatorial data.
- **Theorem 2.12**: for a fixed normal direction u and a chamber of the
  parallel-hyperplane arrangement, the integral over P ∩ H(β) is a
  **polynomial in the parameter β**.
- **Theorem 2.14**: Ehrhart counts of slices are piecewise rational in β.
- **Theorem 1.2**: the number of combinatorial types of hyperplane sections of
  a d-polytope with n vertices is O(n^{2d+12d}) — finite and polynomially
  bounded in the fixed-dimension regime (though the constant explodes).

## Bearing on PE597 — the named justification for "p(3,L), p(4,L) are rational functions of m = L/40"

The run verified exactly (n=2,3,4) that p(n,L) is a **single rational function
of m = L/40** over the physical range (n=3: (7m²−17m+12)/(18m²−45m+27); n=4:
(19m³−119m²+244m−162)/(9(m−2)(2m−5)(2m−3)); limits 7/18 and 19/36), with cell
counts L-independent and the arrangement degenerating exactly at the
denominator poles (m = k/2). The mechanism behind that empirical pattern is
this theorem: the race outcome region is a union of simplex sections; lengths
scale linearly with L (equivalently with m), so on each open chamber of the
arrangement's parameter space the parity-region volume is a rational function
of m. The theorem does not itself give the coefficients (that still needs the
arrangement), but it is the mathematical explanation of *why* the fitted
rational degree-(n−1)/(n−1) forms are one piece rather than many, and why the
physical range avoids all denominator poles (they sit at L = 20,30,40,... = m =
1/2, 1, 3/2, ..., where the arrangement degenerates — matching the run's
ncells=27 spike at the n=3 pole L=120).

## Consistency with the run's record

Consistent with `CONTEXT.md` Established: p(n,L) rational in m of degree
(n−1)/(n−1), denominator roots at half-integers m=k/2, arrangement degeneracy
at poles. This is the standard "parametric polytope volume is piecewise
polynomial/rational on chambers" theory; the run's n=2,3,4 verified points are
consistent evidence, not a proof of the n=13 extension. The theorem bounds the
chamber structure; it does not remove the arrangement-enumeration cost, so
p(13,1800) still needs the missing reduction.