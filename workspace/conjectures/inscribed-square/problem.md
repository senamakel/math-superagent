# The Inscribed Square Problem (Toeplitz's conjecture)

## Statement

> Let `gamma : S^1 -> R^2` be a Jordan curve — a continuous, injective map of
> the circle into the plane (equivalently, the boundary of a simple closed
> curve). Then there exist four points on `gamma` that are the vertices of a
> square.

Posed by Otto Toeplitz in 1911. No smoothness, convexity, rectifiability, or
symmetry is assumed. `gamma` may be nowhere differentiable. This generality is
the entire difficulty: the standard analytic handles (tangent lines, curvature,
arc length, a well-defined normal direction) are not available for an
arbitrary Jordan curve, and any correct argument has to be topological rather
than analytic.

**Status: open** for general continuous Jordan curves. Proved for large,
natural subclasses — see "Known results" below, each recalled from memory and
to be re-established from a primary source before anything in this workspace
rests on it.

## What the statement does and does not say

- "Contains four points that form a square" means the four points, taken in
  the correct cyclic order around the square, coincide with four points of
  `gamma` — not that the square's *interior* lies inside the region the curve
  bounds, and not that the four points appear in the same cyclic order on
  `gamma` as they do on the square (they do, for the natural reason: a genuine
  inscribed square's vertex order around the curve matches its order around
  the square, but a proof has to establish this rather than assume it, since a
  degenerate "crossed" quadrilateral configuration satisfies the algebraic
  square conditions without it).
- Existence, not uniqueness or count. A curve may (and generically does) admit
  infinitely many inscribed squares; a circle admits an infinite family. The
  conjecture asks only that at least one exists.
- The curve is not required to be convex, smooth, rectifiable, or symmetric.
  Nowhere-differentiable Jordan curves (fractal boundaries, curves built by
  interpolation of Weierstrass-type functions) are legal instances and are
  exactly where the conjecture is open.
- This is the **square** problem specifically. The closely related and
  **already solved** rectangle problem (Greene–Lobb, ~2020–21, symplectic
  methods, for smooth curves: every smooth Jordan curve inscribes a rectangle
  of every aspect ratio except possibly one) is a different, weaker statement
  and must not be cited as settling this one. A cyclic-quadrilateral or
  rectangle result belongs in "related results", never in the same claim as
  "square."
- "Inscribed" here means literally landing on the curve, not merely close to
  it in Hausdorff distance. An approximate square whose vertices are `epsilon`
  off the curve is not a witness, for any `epsilon > 0`; the standard failure
  mode of a numerical approach is to report such a witness as if it were one.

## The proof technique that actually works, on the classes where it works

The one substantive tool that has produced every known positive result is a
configuration-space / degree-theory argument. State it precisely because every
partial result in the literature is some variant of it, and this workspace's
own attempts should be judged against it.

**Setup.** Parametrize four cyclically-ordered points `t1 < t2 < t3 < t4` on
`S^1` (identify `S^1 = R/Z`). They determine two chords of `gamma`: the
"diagonal" `A` from `gamma(t1)` to `gamma(t3)`, and the "diagonal" `B` from
`gamma(t2)` to `gamma(t4)`. The four points are the vertices of a square,
taken in the correct cyclic order, if and only if `A` and `B` share a
midpoint, have equal length, and are perpendicular.

**The map.** Equal length + perpendicular is one complex equation
(`B = i*A` as vectors, for the correct choice of `i` vs `-i` fixed by the
cyclic order); same midpoint is another. Define
`F(t1,t2,t3,t4) = (midpoint(A) - midpoint(B), (gamma(t2)-gamma(t4)) - i*(gamma(t1)-gamma(t3))) in R^2 x C`.
A zero of `F` at a point with all four `t_i` distinct is an inscribed square.

**The topology.** The domain of cyclically-ordered, distinct quadruples,
modulo the residual symmetry of the labeling, deformation-retracts to a
**Mobius band**. `F` extends continuously to the boundary of that space, where
adjacent parameters coincide (`t1 = t2`, `t3 = t4`) and the "square" degenerates
to a doubled segment. Because the boundary of a Mobius band double-covers its
core circle, the boundary value of the relevant component of `F` winds an odd
number of times around the origin whenever the curve is locally well-behaved
enough to compute that winding number at all — and a map on a Mobius band whose
boundary winds an odd number of times around a point cannot avoid that point in
the interior. This is a Borsuk–Ulam-flavored parity argument, not an analytic
one; the analytic hypothesis on `gamma` enters *only* in computing the boundary
winding number and in ruling out that the interior zero is itself one of the
degenerate boundary-type configurations.

This is why "does the curve have enough local structure to make this
well-defined" is the single question that separates every proved case from the
open general case.

## Known results — leads, not imports; re-establish each before relying on it

- **Emch (1913).** Convex curves, and curves with a piecewise-analytic /
  continuously turning tangent. Predates the modern topological formulation.
- **Shnirelman (1929).** First topological (Mobius-band) argument, for
  sufficiently smooth curves; the argument had a gap in handling the
  degenerate boundary, later understood.
- **Stromquist (1989).** **Locally monotone** Jordan curves — a curve is
  locally monotone if, near every point, some rotation of coordinates makes it
  a monotone graph. This class contains every piecewise-`C^1` curve, hence
  every polygon and every `C^1` curve. This is the strongest *unconditionally
  accepted* positive result and the one this workspace should treat as the
  load-bearing theorem to formalize and build from.
- **Nielsen–Wright and related symmetry results** (various authors, 1990s–2000s):
  curves with a line or point symmetry, or curves bounding a simply connected
  region with extra regularity, extend the class further.
- **Vaughan's unpublished/folklore convex-curve argument** via a "rotating
  rectangle" continuity trick, often cited informally; find and verify a
  written source before using it, or drop it.
- **Cantarella–Denne–McCleary (2020 preprint), "Configuration spaces of
  squares."** Claims a proof of the full conjecture for *every* continuous
  Jordan curve, via a more refined configuration-space argument that tracks
  the degenerate locus with more care than Shnirelman/Stromquist. **Treat this
  as unconfirmed, not as settling the conjecture**, unless this workspace can
  independently locate a published, peer-reviewed, and widely accepted version
  and record that citation. Do not build on it as a fact; do not cite it as
  "solved."
- **Matschke's 2014 survey** ("A survey on the square peg problem") is the
  standard entry point into the full literature and should be the first source
  fetched and checked against the claims above.
- **Greene–Lobb (2020/2021), rectangle problem.** Every smooth Jordan curve
  inscribes rectangles of every aspect ratio except at most one, via
  symplectic billiards / Lagrangian Klein bottle methods. A genuinely
  different (and, for rectangles, essentially complete) technique from the
  Mobius-band parity argument; worth understanding as a second attack surface,
  not as a shortcut to the square case.

## Where the general (continuous, non-locally-monotone) case actually breaks

Name the failure point precisely, because a correct partial result here is one
that identifies exactly this and works around it for a specific subclass:

1. **No boundary winding number.** The parity argument needs a well-defined
   winding number for `F` restricted to the degenerate boundary of the
   configuration space. Local monotonicity is exactly the hypothesis that
   makes this computable. A wild curve can make the boundary map fail to be
   well-approximable by anything with a definite degree.
2. **Spurious interior zeros near the boundary.** Even where an interior zero
   of `F` is found, ruling out that it is itself degenerate (a shrinking
   "square" collapsing to a point, or a self-intersecting "crossed"
   configuration masquerading as a valid one) uses local structure that a
   general continuous curve does not have.
3. **The approximation trap.** Approximating a wild Jordan curve by a sequence
   of polygons or smooth curves produces, by Stromquist's theorem, a sequence
   of genuine inscribed squares — but their side lengths can converge to
   zero, so the limit is a single point, not a square. This is the standard,
   specific reason "take a limit of the nice case" does not finish the
   problem, and any argument in this workspace that leans on such a limit must
   show the side length is bounded away from `0` along the approximating
   sequence, or it has proved nothing.

## The trap specific to this problem

**A numerically "found" square is not a witness unless the vertices are exact
points of the actual curve, verified symbolically or with an explicit error
bound that is then closed to zero.** A root-finder locating an
approximate zero of `F` on a discretized curve will report success on almost
any curve, including ones the discretization does not faithfully represent
near a corner or a high-curvature region. Any computational claim in this
workspace must state: the exact class the curve belongs to (polygon with exact
rational/algebraic vertices, or `C^1` curve with an explicit parametrization),
the method used to certify the zero (interval arithmetic / exact algebra, not
floating-point root-finding alone), and which of the theorems above it is
therefore an instance of — a "found square" on a piecewise-linear curve is not
new mathematics, it is a numerical check of Stromquist's already-proved
theorem, and should be reported as exactly that, not as progress on the open
case.
