# Wolird, "A New Transformation of the Magic Square of Squares" (arXiv:2310.12164)

[[wolird-gaussian-transformation-magic-square-2023]]
Full text: `research/sources/wolird-gaussian-transformation-magic-square-2023.full.md` (arXiv:2310.12164v1, 1 Oct 2023, math.HO, 11 pp).

## What it establishes

An expository/observational note (no theorem stated as a formal result with proof). Core content is a **3-to-1 correspondence between Gaussian arithmetic triplets and Gaussian Pythagorean triples**, unfolding Fibonacci's integer arithmetic-triplet/Pythagorean-triple correspondence into ℤ[i]:

- Over integers: every Pythagorean triple A²+B²=C² yields an AP of squares (A−B)², C², (A+B)² /2-type relations; the correspondence is 1-to-1.
- Over the Gaussian integers, the analogous identity α²+β²+γ²=0 yields **three** APs of squares from one Pythagorean triple (treating each of α,β,γ as the "hypotenuse" in turn), hence 3-to-1. The author calls the three resulting APs "siblings" of a common Pythagorean triple.

**Application to the MSS.** A magic square of squares in ℤ[i] is a "slant 3×3 grid" in the complex plane containing 8 arithmetic triplets (one per centre line — 4 through the centre + 4 sides). From these 8, the 3-to-1 correspondence generates **16 more Gaussian arithmetic triplets** (8 "older" siblings centred at sums, 8 "younger" at differences) — so an MSS forces 24 Gaussian arithmetic triplets. §4 observes that a true MSS would generate near-misses among these siblings; §5 shows the Bremner square fixes the sums (perfect APs) but has non-square entries, while the Parker square fixes the entries (perfect Gaussian squares) but has mismatched sums — i.e. the two near-misses' "personality" carries to their siblings.

## Bearing on the 3×3 MSS

**Provably a dead end for the proof goal; only rephrases the puzzle.** The author's own conclusion (§5): "do these siblings tell us anything about the existence of the Magic Square of Squares? Not that the author sees directly." The note establishes no new bound, no impossibility, and no reduction to a solvable object. The Gaussian reformulation it gives is **distinct from** Onno Cain's arXiv:1908.03236 quartic/abelian-extension reformulation (the run's `gaussian-factorisation-is-cains-reformulation` claim) — Wolird gives a triangular/geometric correspondence, not a quartic factorisation constraint, and does not connect to the additive Φ condition.

**holds-here: no** — no hypothesis or statement transfers to the Q-rational MSS problem; it neither corroborates nor contradicts any run claim.

```claim
id: wolird-gaussian-sibling-3-to-1
statement: Over the Gaussian integers, arithmetic triplets of squares are in 3-to-1
  correspondence with Gaussian Pythagorean triples (solutions of alpha^2+beta^2+gamma^2=0);
  a magic square of Gaussian squares contains 8 arithmetic triplets and generates 16 more
  (older/younger siblings). This gives no statement about existence over Z or Q.
hypotheses: configuration over Z[i]; arithmetic triplet = AP of Gaussian squares
holds-here: no (it is a Z[i] observational correspondence; no Q-rational MSS constraint,
  no bound, no reduction to a solvable object)
status: asserted (expository note, no formal theorem/proof)
bearing: dead end for non-existence: it only geometrically rephrases the puzzle in Z[i]
  and the author concludes it gives no existence information. Distinct from Cain's
  Gaussian quartic-factorisation reformulation (which is itself asserted/unverified).
anchor: research/sources/wolird-gaussian-transformation-magic-square-2023.full.md
```

## Does this source help?

**No.** It is a recreational/math.HO exposition. It establishes no theorem usable here, contradicts nothing, and its author explicitly disclaims any bearing on existence. Recorded so nobody re-reads it; the `wolird-gaussian-transformation-magic-square-2023` summary now replaces the template digest in place.

## Source

Wolird, Christian. "A New Transformation of the Magic Square of Squares." arXiv:2310.12164v1 [math.HO]. https://arxiv.org/abs/2310.12164
