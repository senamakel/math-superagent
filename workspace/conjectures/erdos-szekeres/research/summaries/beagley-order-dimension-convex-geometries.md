# Beagley, "On the Order Dimension of Convex Geometries", Order 30 (2013) 837–845

Source: https://doi.org/10.1007/s11083-012-9280-2
Held text: [[beagley-order-dimension-convex-geometries.full]] — **this is the Springer landing
page only: abstract + references + metadata. The proof is paywalled and NOT on disk.**

## What the held text actually establishes

The abstract states one theorem (nothing more is held):

> The lattice of closed subsets of the planar point set of Erdős and Szekeres from 1961 — a set
> of 2^{n-2} points containing no vertex set of a convex n-gon — has order dimension n−1, and
> any larger set of points has order dimension at least n.

Closed sets = convex hulls of subsets (convex geometry cl(S) = conv(S) ∩ X); order dimension =
Dushnik–Miller dimension of the closed-set lattice.

```claim
id: beagley-order-dimension-esz
statement: For the ES 1961 extremal set (2^{n-2} points, no convex n-gon) the convex-geometry closed-set lattice has order dimension exactly n−1; every planar point set with more than 2^{n-2} points has closed-set lattice of order dimension at least n.
hypotheses: finite planar point set; lattice of conv-hull-closed subsets under inclusion; Dushnik–Miller order dimension.
holds-here: yes — reformulates the extremal constant 2^{n-2} around the very object (the ES construction) this run studies structurally.
status: asserted — only the abstract is held (paper paywalled); the proof is not on disk.
bearing: motivates the order-dimension approach (convex-geometry-order-dimension, status proposed) but does NOT establish the missing direction. "dim ≥ n for larger sets" is consistent with sets that contain a convex n-gon AND with hypothetical sets that do not; the theorem as stated never forces the convex n-gon, so it is not equivalent to ES(n)=2^{n-2}+1 and cannot be used as the load-bearing step.
anchor: research/sources/beagley-order-dimension-convex-geometries.full.md
contradicts: nothing on disk; it sharpens the approach file's caveat ("Beagley connects |X|>2^{n-2} to dim growth, not to an exact equality") by confirming the held text is abstract-only.
```

## What it implies here

- The order-dimension reformulation is real and published (Edelman–Jamison 1985; Edelman–Saks
  1988 are also cited), but the exact-constant direction needed for ES — "closed-set lattice
  dimension n−1 forces ≤ 2^{n-2} points and the absence of a convex n-gon" — is **not** in the
  held text. Any claim that order dimension proves ES must first obtain the paper or prove the
  missing converse.
- The approach's first-step (compute dim of es_construct's closed-set lattice at n=5,6,7 and
  compare with 2^{n-2} and n−1) remains a valid *test* of the reformulation, independent of the
  proof.

## Does not help

As a *proof source* for the ES upper bound it does not help: asserted theorem, abstract only.
As *evidence* that the 2^{n-2} constant is the right one it adds one independent reformulation
(2^{n-2} ↔ dimension n−1 on the extremal object), consistent with but not strengthening
`baek-balko-split`.