# Asano–Ike 2024 — The rectifiable rectangular peg problem

**Source:** Tomohiro Asano, Yuichi Ike, "The rectifiable rectangular peg problem," arXiv:2412.21057 (2024; the full text in this library is **v3, 5 Jan 2026**). Full text at [[research/sources/asano-ike-2024-rectifiable-rectangular-peg.full.md]]. Precise claim blocks with exact hypotheses, the definition of the continuous Legendrian lift, and where it enters the proof: [[research/summaries/asano-ike-2024-claim.md]].

## What it establishes — a major positive class

**Theorem 1.1.** Let c : S¹ → R² be a Jordan curve admitting a *continuous Legendrian lift*: there exists a sequence of smooth Jordan curves cₙ → c in C⁰ such that the primitives fₙ of (cₙ∘e)∗λ converge uniformly on compact subsets to a continuous f. Then c inscribes a θ-rectangle for any θ ∈ (0,π).

**Corollary 1.2 (5.9).** **Every rectifiable Jordan curve inscribes a θ-rectangle for any θ ∈ (0,π)** — in particular, **every rectifiable Jordan curve inscribes a square** (θ = π/2).

**Corollary 1.3 (5.12).** Every locally monotone curve inscribes a θ-rectangle for any θ ∈ (0,π) (hence a square).

This is, per the paper's own claim, "the first result that gives an affirmative answer to the square peg problem (i.e., θ = π/2) for all the rectifiable Jordan curves." Rectifiable = finite length (Hausdorff 1-measure), a vastly larger class than locally monotone, C¹, or two-graph curves.

**Method:** microlocal sheaf theory (Tamarkin category, sheaf quantization). The θ-rectangle problem is converted to Lagrangian intersection: Rθ(z′, w′) = (z, w) for a Hamiltonian Rθ on C², with the diagonal ∆C corresponding to degenerate rectangles; an inscribed θ-rectangle is an intersection of C×C with Rθ(C×C) off the diagonal. For smooth C there is a canonical sheaf quantization F_C whose microsupport is C×C; by completeness of the Tamarkin category under the interleaving distance, the quantization extends to continuous curves with a continuous Legendrian lift. The technical criterion (Theorem 4.1): if Ta SS•(F_C) ∩ SS•(F_C) = ∅ for all a ∈ R∖πZ, then C inscribes every θ-rectangle.

## Why it matters here

- **This is the strongest single positive result in the library for the square problem.** It strictly contains Stromquist's locally monotone curves (Corollary 1.3) — a monotone graph has finite length — and Tao's two-graphs class, and extends to all rectifiable curves.
- **GOAL.md's completion criteria change:** "an extension of the locally-monotone class" is already done by Asano–Ike (rectifiable ⊃ locally monotone). The run's own contribution must be a *strictly larger* class, or a precise obstruction statement, or a formalization — not a re-proving of the rectifiable case.
- **The gap the run can still attack:** non-rectifiable Jordan curves (infinite length, e.g., fractal boundaries) are exactly where the conjecture remains open. Asano–Ike's hypothesis is the *continuous Legendrian lift*; a non-rectifiable curve may fail it. Whether every Jordan curve admits a continuous Legendrian lift is the sharp question.
- The θ-rectangle formulation (Rθ on C²) is the modern symplectic translation of the config-space map F; the diagonal-avoidance criterion is the symplectic form of ruling out degenerate intersections.

## Claims

```claim
id: asano-ike-2024-rectifiable-square
statement: Every rectifiable Jordan curve inscribes a θ-rectangle for every θ ∈ (0, π); in particular every rectifiable Jordan curve inscribes a square.
status: asserted-by-source (arXiv preprint, Dec 2024)
evidence: Asano–Ike, arXiv:2412.21057, Theorem 1.1 + Corollary 5.9
holds-here: yes — the strongest known positive class for the square problem; strictly contains locally monotone and two-graph classes
falsifies: a rectifiable Jordan curve with no inscribed square; or a retraction/correction of the preprint
```

```claim
id: asano-ike-2024-locally-monotone-rectangle
statement: Every locally monotone Jordan curve inscribes a θ-rectangle for every θ ∈ (0, π).
status: asserted-by-source
evidence: Asano–Ike, arXiv:2412.21057, Corollary 5.12
holds-here: yes — reproves and strengthens Stromquist's theorem (square) to all rectangles; consistent with matschke2014-stromquist-locally-monotone
falsifies: a locally monotone curve with no inscribed θ-rectangle for some θ
```

```claim
id: asano-ike-2024-legendrian-lift-gap
statement: The class of Jordan curves admitting a continuous Legendrian lift (Theorem 1.1's hypothesis) contains all rectifiable curves; whether every Jordan curve admits such a lift is the sharp open question separating the solved class from the general case.
status: sourced (paper states rectifiable ⊂ class; general case open)
evidence: Asano–Ike, arXiv:2412.21057, §1.1 and Corollary 5.9
holds-here: yes — names the exact frontier: non-rectifiable curves without a continuous Legendrian lift
falsifies: a proof that every Jordan curve admits a continuous Legendrian lift (would settle the full conjecture), or a non-rectifiable curve without one
```
