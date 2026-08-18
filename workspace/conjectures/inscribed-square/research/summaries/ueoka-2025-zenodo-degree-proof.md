# Ueoka 2025 — Zenodo preprint series claiming a C⁰ proof of the Toeplitz conjecture

**Source:** Yoshiki Ueoka, "The Proof of the Inscribed Square Problem using Topological Degree," Zenodo record 17847990, v5, published 2025-12-08. DOI 10.5281/zenodo.17847990. Landing page captured at `research/sources/ueoka-2025-zenodo-degree-proof.full.md` (HTML record; the 62.5 kB PDF `v5 English ToeplitzConjecture.pdf` is linked but its text is not in this library).

**Series:** five overlapping Zenodo preprints (Nov 2025 – Jan 2026), DOIs 10.5281/zenodo.17554802, .17655388, .17847990, .18243635, plus a Japanese version .18239842. All self-published by an independent researcher (PhD physics, Osaka University); a Medium post describes the collaboration as AI-assisted (Gemini). Status: **0 citations, no peer review, no expert endorsement, no independent validation or published critique found** (checked 2026-08). One version admits it is a "proof skeleton."

## What the abstract claims

For any C⁰ Jordan curve in the plane:

1. Define a continuous map F : T⁴ → R⁴ from a distance-based formulation of the square condition (four points on the curve; all sides equal and diagonals equal).
2. Approximate the C⁰ curve by a sequence of C¹ curves, giving maps Fₙ → F₀ uniformly.
3. **Claimed key steps:** a detailed analysis of ∂T⁴ shows all Fₙ are non-zero on the boundary with a **uniform positive margin**; the zero points do not approach the boundary, **excluding degenerate squares**.
4. Extend the topological degree argument from C¹ to C⁰ via the uniform limit.

## Why this is exactly the unsolved step — the falsifier is named

The two italicized claims are precisely **the two steps the peer-reviewed literature identifies as unsolved for arbitrary continuous curves** (problem.md's failure points 1 and 2; ROOT.md's shrinkout obstruction; Matschke 2009's open-dense class; Asano–Ike's continuous-Legendrian-lift hypothesis):

- **"Uniform positive margin on the boundary"** is the claim that the boundary winding number of F is well-defined and stable under C⁰ approximation. But for a wild (non-locally-monotone) curve, chords can be perpendicular at arbitrarily small scale — there is no reason the boundary map has a definite degree, and this is *the* reason Stromquist's theorem needs local monotonicity and Asano–Ike needs a lift. **A claim that this margin holds for every C⁰ curve is a claim that the entire obstruction does not exist.**
- **"Zero points stay away from the boundary"** is the claim that no inscribed square shrinks to a point. But Greene–Lobb 2024's sharpness example (a cyclic quadrilateral that is not an isosceles trapezoid fails to inscribe in some triangle, even though it inscribes in every smooth curve) shows smooth approximations *do* shrink quadrilaterals away for arbitrary C⁰ limits. **This is exactly shrinkout.**

So the record's abstract asserts, without the analytic content, the two lemmas that would be the theorem. The PDF (62.5 kB for a proof of a 115-year-old open problem) is not in this library; even if downloaded, its key steps must be read against the above before any weight is attached. **This is recorded as an unvalidated claim, not as a proof, not as a refutation.** It remains possible (a) the proof is correct, in which case this is the solution — but 0 citations, no review, and an admitted "proof skeleton" make that the prior-improbable hypothesis; (b) the proof is wrong at one of the two named steps, in which case this document is a precise record of where full-proof claims die; (c) the proof is correct for a restricted class and overclaims C⁰ generality. The library's role is to hold the claim with its exact falsifier, and the run must not build on it either way.

## Claim blocks

```claim
id: ueoka2025-full-proof-unvalidated
statement: Yoshiki Ueoka's Zenodo series (2025–26, five preprints) claims a degree-theoretic proof of the square peg problem for all C⁰ Jordan curves; it is not peer-reviewed, not cited, has no expert endorsement, and its two central claims — a uniform positive boundary margin for the maps Fₙ and non-approach of zeroes to the boundary — are exactly the steps the literature identifies as unsolved. It must not be treated as established.
hypotheses: none — a status statement about a claim.
holds-here: yes — the only full-proof claim in existence for the Toeplitz conjecture; recorded so the run can name it and not guess about it.
evidence: Zenodo record 17847990 v5 (landing page captured); DOIs 10.5281/zenodo.17554802, .17655388, .17847990, .18243635; Medium post describing AI collaboration; asano-ike-2024-status.md.
status: catalogued claim (unvalidated preprint; no independent verification)
falsifies: a peer-reviewed publication of the proof; or an independent expert verification; or a documented identification of a specific error in one of the two named steps.
```

```claim
id: ueoka2025-boundary-margin-is-the-obstruction
statement: The "uniform positive margin on the boundary" step in Ueoka's claimed proof is exactly the boundary-winding-number step that fails for wild curves in the known literature: Stromquist needs local monotonicity and Asano–Ike needs a continuous Legendrian lift precisely to make this step well-defined.
hypotheses: none — a structural comparison.
holds-here: yes — names the exact point at which any claimed C⁰ proof must be checked first.
evidence: problem.md failure point 1; ROOT.md; Matschke 2009 (open-dense class); Asano–Ike 2024 (lift hypothesis); Stromquist via Rius thesis 3.36 (local monotonicity is what makes the boundary computable).
status: derived observation (from verified sources)
falsifies: a published account showing the boundary winding number is well-defined for arbitrary C⁰ curves without extra hypotheses.
```
