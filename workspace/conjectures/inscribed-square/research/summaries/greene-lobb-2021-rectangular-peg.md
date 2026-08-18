# Greene–Lobb 2021 — The Rectangular Peg Problem

**Source:** Joshua Evan Greene, Andrew Lobb, "The Rectangular Peg Problem," Annals of Mathematics 194(2), 2021, pp. 509–517. DOI: 10.4007/annals.2021.194.2.4. Full text on disk is the arXiv preprint arXiv:2005.09193 at [[research/sources/greene-lobb-2021-rectangular-peg.full.md]].

## What it establishes

**Theorem.** For every smooth Jordan curve γ and every rectangle R in the Euclidean plane, there exists a rectangle similar to R whose vertices lie on γ.

This solves the Rectangular Peg Problem for smooth Jordan curves — every smooth Jordan curve inscribes rectangles of *every* aspect ratio.

- The proof is **symplectic**, not the Mobius-band parity method. It identifies R² with C, takes a second copy with polar coordinate w = r·e^{iθ}, and builds from the curve γ two Lagrangian tori L, L_φ in C². A surgery (Proposition 1.1) turns their union into a smoothly **immersed Lagrangian torus**; a further argument produces a **smoothly embedded Lagrangian Klein bottle** in C².
- **Shevchishin's theorem** (no smoothly embedded Lagrangian Klein bottle in C²) gives the contradiction: the required intersection, hence the inscribed rectangle, must exist.
- Key local lemmas: equivariant Darboux–Weinstein statements (Propositions 1.2, Lemmas 1.3–1.5) building the Lagrangian torus with the correct symmetry.

## Why it matters here

- **Not a square result.** The square is the aspect-ratio-1 rectangle, but Greene–Lobb's theorem is for *smooth* Jordan curves only, and it does not transfer to continuous curves — problem.md's completion criterion explicitly says the scope of this result and why it does not transfer must be recorded.
- It is the second great attack surface (symplectic) alongside the Mobius-band parity method. Schwartz's BAMS survey "Rectangles, curves, and Klein bottles" (DOI 10.1090/bull/1755) is the exposition worth fetching next.
- Hugelmeyer's intermediate results (√3 aspect ratio 2018; at least 1/3 of aspect ratios 2021, Annals) sit between Stromquist's era and Greene–Lobb. Greene–Lobb also have follow-ons: "Cyclic quadrilaterals and smooth Jordan curves" (Invent. Math. 2023) and "Jordan curves inscribe a positive measure of rectangles."

## Claims

```claim
id: greene-lobb-2021-rectangular-peg
statement: For every smooth Jordan curve γ and every rectangle R in the Euclidean plane, there exists a rectangle similar to R whose four vertices lie on γ.
status: asserted-by-source
evidence: Greene–Lobb, Annals of Mathematics 194(2) 2021, 509–517 (DOI 10.4007/annals.2021.194.2.4); arXiv:2005.09193
holds-here: yes — this is the solved rectangle problem; it does NOT settle the square problem (smoothness hypothesis + rectangle, not square)
falsifies: a smooth Jordan curve and a rectangle R with no similar inscribed rectangle
anchor: research/sources/greene-lobb-2021-rectangular-peg.full.md
```

```claim
id: gl2021-klein-bottle-mechanism
statement: The Greene–Lobb proof works by building from γ two Lagrangian tori in C², surgering them into a smoothly embedded Lagrangian Klein bottle; Shevchishin's theorem (no smoothly embedded Lagrangian Klein bottle in C²) gives the contradiction that forces the inscribed rectangle.
status: asserted-by-source
evidence: Greene–Lobb, Annals 194(2) 2021 (main theorem and §1 construction; Shevchishin's theorem cited)
holds-here: yes — the symplectic mechanism, verified against the primary text
falsifies: a correction to the Klein-bottle construction in the primary source
anchor: research/sources/greene-lobb-2021-rectangular-peg.full.md
```

```claim
id: greene-lobb-does-not-transfer-to-continuous
statement: The Greene–Lobb rectangle theorem is proved only for smooth Jordan curves; it does not extend to general continuous Jordan curves by any known argument, and it concerns rectangles, not squares.
status: sourced
evidence: Greene–Lobb 2021 theorem statement (smooth hypothesis); no published extension to continuous curves in the library's sources
holds-here: yes — completion criterion #1 of GOAL.md: record scope and why it does not transfer
falsifies: a published proof of the rectangular peg problem for all continuous Jordan curves
```
