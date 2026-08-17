# Refutation report — current rung `R-one-interior` (target of this arm)

**Refuter verdict on the current weakened rung: `proved` (hand + machine).**
The statement is trivially true; there is no counterexample. This is a positive
finding, not a refutation — but it is what a careful attack on this rung yields,
and it is worth recording because the weakened ledger still lists the rung
`open`.

## Statement attacked

From `research/weakened/es-conjecture.md`, rung id `R-one-interior` (stance in
ledger: open; merge text misdescribes it — see below):

> For every n >= 4, every set of 2^(n-2)+1 points in general position with at
> most one interior point (a point strictly inside the convex hull of the set)
> contains n points in convex position.

## One-line hand proof (covers ALL n, no search needed)

A set with at most one interior point has at least 2^(n-2) points ON its convex
hull. Because the set is in general position (no three collinear), every hull
point is a vertex of the hull, and the hull vertices of a finite planar set form
a convex polygon, i.e. are in convex position. Since 2^(n-2) >= n for every
n >= 4 (equality at n=4, strict above), the hull alone already supplies n points
in convex position. **QED.**

Crucially this regime has no chirotope/realizability gap: hull vertices are
extreme in every realization of the order type, so "hull vertices in convex
position" is true for every realizable set. The tightest case n=4 (5 points,
>=4 hull vertices, need a convex quadrilateral) is exactly the proved library
claim ES(4)=5 (`es-exact-values`, `es35-four-criterion`).

## Machine results (fresh `find_counterexample` runs this session)

Both existing TPTP problems under `code/refute/`, re-run fresh:

1. `r-one-interior-n4.p` — tightest case n=4 (5 points), weakest faithful
   fragment (ccw totals + cyclic symmetry, interior via Caratheodory triangle,
   at-most-one-interior, convex4 via the 4-point criterion).
   **`proved`** (SZS Theorem).
2. `r-one-interior-n4-fullcc.p` — same n=4 case over the FULL Knuth CC-system
   axiom set (cyclic, antisymmetry, nondegeneracy, interiority, transitivity),
   convexity defined axiom-natively via hull edges. **`proved`** (SZS Theorem).

So even the abstract CC-system analogue of ES(4)=5 is true — the abstract
statement agrees with the proved geometric claim, and there is no unrealizable
witness lurking at n=4.

## The ledger the rung lives in

The most-likely-false candidate on the run's current plate is NOT `R-one-interior`
(it is trivially true). Two candidates genuinely worth the refuter's future
attention:

- **`R-k-interior` with k >= 2** — the merge text of `R-one-interior` actually
  describes this rung: "the trivial hull argument dies exactly when
  k > 2^(n-2)+1-n". The genuinely first nontrivial regime is the smallest n,k
  with 2^(n-2)+1-k < n, i.e. k ≥ 2^(n-2)+1-n+1. First instance: n=5 gives
  2^(5-2)+1 = 9, so k ≥ 9-5+1 = 5; n=5,k=5 (9 points, hull ≤ 4, 5 interior) is
  the first real target, not k=1. Could not encode n=5,k=5 faithfully here: it
  needs 9 points and the position of a 5-subset inside a 4-gon, beyond the
  fragment sizes this TPTP encoding reaches.

- **`es-construct-realized-pattern-classes-triangular` (the n=8 side is SAMPLED,
  so only a lower bound; a 22nd class refutes "exactly 21").** This is the single
  most likely to be false of the run's claimed structural findings because the
  n=8 evidence was K=150 realizations per candidate pattern, and sampling can
  only under-count realized classes. The n=8 enumeration is C(64,7) ≈ 6.2e8 —
  too large for an exact full sweep here — so a heavier sampled hunt for a 22nd
  class is the right next move, not a TPTP search (the claim is a computable
  property of a concrete 64-point set, not a first-order proposition amenable to
  `find_counterexample`).

## Boundaries of what this report establishes

- `proved` is relative to the axioms I wrote. The n=4 fragments are faithful to
  the general-position + hull-count + 4-point-criterion meaning of the rung, and
  the hand proof does not depend on the encoding at all — so the hand proof is
  the authority here, not the machine.
- An honest "could not encode faithfully" applies to `R-k-interior` k>=2 (needs
  too many points / positional quantifiers for this tool's fragment sizes). That
  is a capability limit of `find_counterexample` for this claim, not evidence
  either way about k>=2.

## What the run should do with this

- Mark `R-one-interior` **settled/trivial**: it is the k=1 case of the hull-count
  argument and is TRUE with margin (it is even confirmed by the already-settled
  exact values ES(3..6) = 3,5,9,17). The interior points do not begin to matter
  until k >= 2, which is `R-k-interior`.
- Redirect the refuter's attention to the n=8 sampled side of the triangular
  realized-pattern-count conjecture (hunt a 22nd realized class) and to
  `R-k-interior` k>=2 with n=5,k=5 as the first target.
