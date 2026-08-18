# Two discrete versions of the Inscribed Square Conjecture (Sagols–Marín 2011)

**Source:** Feliú Sagols, Raúl Marín, "Two discrete versions of the Inscribed Square Conjecture and some related problems," Theoretical Computer Science 412(15), 2011, 1301–1312. DOI: 10.1016/j.tcs.2010.10.004. Earlier version: "The inscribed square conjecture in the digital plane," IWCIA 2009, LNCS 5852, 411–424.

**Record:** abstract captured via ScienceDirect search; full text paywalled (no arXiv version found).

## What it establishes (from the published abstract)

Two discrete versions of the Inscribed Square Conjecture, both proved:

1. **Digital plane version:** The conjecture holds for digital simple closed **4-curves** (4-connected pixel curves), but **fails for 8-curves**. Constructed: an infinite family of 4-curves with exactly one non-degenerate inscribed square, and an infinite family with exactly n inscribed squares for each n. An O(n²) algorithm finds inscribed squares in simple digital curves.
2. **Topological graph theory version:** Any cycle of the grid Z² contains an inscribed square with integer vertices.

Proofs rely on a theorem of Pak (piecewise-linear case).

## Why it matters here

- **The failure for 8-curves is a discrete counterexample data point:** in the digital 8-connectivity setting, the naive discrete analogue of the conjecture is FALSE. This shows the discrete analogue is delicate — the connectivity convention decides whether the analogue holds. It cautions against treating "discrete versions" as evidence for the continuous conjecture.
- The 4-curve success is a genuinely verified discrete class (via Pak's theorem), and the O(n²) algorithm is a concrete computational tool — relevant if this run ever implements a digital-plane oracle.
- Both results are about *digital* analogues, not the continuous conjecture; they neither prove nor refute Toeplitz's conjecture.

## Claims

```claim
id: sagols-marin-2011-digital-4-curves
statement: The Inscribed Square Conjecture holds for digital simple closed 4-curves (4-connected pixel curves); it fails for 8-curves. Any cycle of the grid Z² contains an inscribed square with integer vertices.
status: asserted-by-source
evidence: Sagols–Marín 2011, Theoretical Computer Science 412(15), 1301–1312 (published abstract; full text paywalled)
holds-here: no — a discrete analogue result, neither proving nor refuting the continuous conjecture; the 8-curve failure shows the discrete analogue is connectivity-sensitive
falsifies: a digital simple closed 8-curve with an inscribed square in every natural 8-digital sense; or a 4-curve without one
```
