# Horváth — "Cubic sublattices" (arXiv:2203.01901)

Source: https://arxiv.org/pdf/2203.01901 (full text in `research/cubic_sublattices.md`).

**What it is.** An elementary (cross-product) proof of the cubic-sublattice existence and
classification that Goswick et al. proved with quaternions. Provides an independent,
non-quaternion route to characterize the frames.

## Statements
- **Theorem 1**: For v∈Z^3 whose squared length is divisible by d², there is a cubic
  sublattice of edge length d containing v. If v is primitive, this cubic sublattice is
  unique.
- **Construction**: for primitive v and edge d, the unique cubic sublattice is
  Γ(v,d) = {a∈Z^3 : a×v divisible by d, and (a×v)×v divisible by d²}; index d³; its
  cubic basis is given by the lemmas (exists a,b with |a|=|b|=d, c=(a×b)/d).
- **Theorem 2**: every cubic sublattice Γ⊆Z^3 = k·Γ(v,d) for unique positive integers k,d
  and primitive v. This is the *frame×(integer scale)* decomposition: k = gcd of all
  vectors, d = edge length / k.
- **Theorem 3** (converse): for primitive v and odd d there is a primitive u with a cubic
  basis of Γ(u,d) whose coordinates are exactly v. (Odd d needed; even fails mod 4.)

## Hypotheses & applicability
All statements are for Z^3, all hypotheses met for lattice cubes. This is a genuinely
independent route: it derives the frame structure from cross products rather than from
quaternion factorization. It **confirms** the frame×scale structure the run already uses in
`frame_method.py` (each cube = primitive frame k-scaled; coordinate spans from |·| sums),
and gives the uniqueness needed to count frames once.

## What it does NOT settle
It does not give a *counting formula* for the number of distinct primitive frames of edge
length ≤ n (that is the quaternion enumeration of Goswick/Kiss–Kutas). It also uses generic
sublattice uniqueness, not the 24-fold column symmetry of a *cube* (a frame = ordered cube
has an extra symmetry that the sublattice does not). So it corroborates the decomposition
but does not supply the canonical cube enumeration.

## Net value to PE 579
Corroboration, not new machinery: the frame×scale decomposition and coordinate-span formulas
in `memory.md`/`frame_method.py` match this source's characterization. No contradiction with
memory.md. Not the bottleneck; the enumeration (from quaternions) is.
