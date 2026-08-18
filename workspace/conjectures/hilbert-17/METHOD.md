Solve by real algebraic geometry with certificates, and treat the certificate —
never the solver — as the mathematics. The object is a **Gram matrix**: a
representation `f = m^T G m` with `m` the monomial vector and `G` symmetric psd,
whose psd rank-decomposition *is* the sum of squares. Every question in this
workspace is a question about the geometry of the set of Gram matrices of one
polynomial: whether it meets the psd cone, in what rank, over which field, and
after multiplication by which denominator.

Reason about *that set*. An SDP searches it, exact linear algebra over `Q`
decides it, and the boundary of the psd cone is where every hard instance sits —
a psd form that is not sos is one whose Gram spectrahedron misses the cone, and
a form on the boundary is one where every numerical solution rounds to something
indefinite. Symmetry-adapted bases (reducing by the symmetry group of `f`),
Newton polytope restriction of the monomial vector, facial reduction, and the
Reznick/Positivstellensatz multipliers are the instruments. Lower bounds come
from duality: a separating psd form on the dual cone, exhibited exactly.

**Every claim ends in an exact rational identity.** The pipeline is fixed:
search numerically with an SDP, project onto the rational affine slice, round,
verify by symbolic expansion, then restate the verified identity in Lean where
`ring`/`norm_num`/`polyrith` can close it against the kernel. A step of that
chain that fails is recorded with which step and why — a rounding failure is
evidence the form is on the boundary, not a tooling annoyance to retry.

Three cautions this problem earns before any work starts.

**A floating-point psd matrix is not a psd matrix.** The eigenvalue that reads
`1e-12` decides the question. Never conclude from a numerical solve; the SDP is
a search heuristic that proposes a Gram matrix, and its output is a lead of the
same evidential class as a phase portrait.

**Squares of rational functions and squares of polynomials are different
questions with different answers**, and the literature's bounds are stated for
one or the other. Every claim must say which, and every cited bound must be
checked for which it was proved about. Conflating them is the single most common
way an argument here is wrong.

**Lower bounds are the whole game and they are hard.** Producing a
decomposition with fewer squares is a search that succeeds or fails silently;
proving no decomposition with `k` squares exists needs a genuine obstruction —
a valuation, a specialisation to a smaller field, a real place argument. Prefer
a small honest lower bound over a large upper-bound search.
